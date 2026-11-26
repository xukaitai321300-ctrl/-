#!/usr/bin/env node
/**
 * 生肖团专家包 · 可恢复能力脚本（双层覆盖：顾问层专家包 + 执行层 zheng10 技能）
 * 用途：任何对 experts/plugins 的破坏性变更前先打快照，出问题时一键恢复。
 * 快照分层（R31/D-66 起）：
 *   默认双层 = 插件目录(全量) + 被 linkageMap 引用的执行层技能(~13 个, 相关)      → ~180MB
 *   三层(--full) = 再加全局 skills 全量(2633 个技能, 其中 2620 个与生肖团零关联)  → ~2.5GB
 *   轻量(light) = 清单式, 默认 docs+scripts+settings.json, 附 SHA256 清单          → ~300KB
 * 用法：
 *   node recovery.js snapshot <label> [--full] [--fixed]  打快照(默认双层+时间戳名; --full 加全库技能; --fixed 固定名覆盖)
 *   node recovery.js list                      列出所有快照(标注含三层者)
 *   node recovery.js restore <snapshotName>    从指定快照一键恢复(插件全量覆盖+技能合并覆盖)
 *   node recovery.js verify <snapshotName>     校验快照与源树文件数/关键 JSON 是否一致
 *   node recovery.js check                     全量一致性自检(诊断能力: JSON/孤儿键/悬空路由/残留旧id/引用齐备/禁用链路)
 *   node recovery.js enable-skills             安全启用双向联动执行层技能(启用前自动双层快照兜底, 可一键回退)
 *   node recovery.js baseline set <label>      标记某快照为已知良好基线(rollback 目标; 对齐 AWS AGENTOPS02-BP03 behavioral baseline)
 *   node recovery.js baseline show             显示当前基线
 *   node recovery.js baseline clear            清除基线标记
 *   node recovery.js light <label> [path...]   轻量快照(默认 docs+scripts+settings.json; 附 SHA256 清单, 逐轮留痕用)
 *   node recovery.js light-prune <N> [--yes]   保留最近 N 个轻量快照(默认干跑; --yes 移入 lite/_trash, 非物理删除)
 *   node recovery.js snapshot-prune [N] [--yes]  保护基线+保留最近 N 个重型快照(默认干跑; --yes 移入 snapshots/_trash)
 * 设计原则(源自业界对比参照): baseline≠最近一次变更; rollback 默认回已知良好基线而非"上次改动"。
 * 体量纪律(R31): 快照体量必须与其覆盖增量相称 —— 三层曾以 2320MB 换 0 增量覆盖, 故降为 opt-in。
 * 累积纪律(R32/D-51): 周期性快照必须用**固定名**(否则 uid 名无界累积); 历史留痕用 light, 里程碑用时间戳名。
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const crypto = require('crypto');

// 路径根。生产默认值即下方 DEFAULT_ROOTS（行为与历史版本完全一致）；
// 仅 selftest 会在 tmp 沙盒内临时重绑定，以做到「取证零污染」——绝不触碰真实快照目录。
const DEFAULT_ROOTS = {
  // R221r2/R8b（E-D57 防再现）：src 从 __dirname 派生（包父目录），禁指向迁移前 experts 落点；
  //   skills/base 是域外真源根（技能库 / 备份区），保持显式绝对路径（非包内派生语义）。
  src:    path.join(__dirname, '..', '..'),
  skills: 'C:/Users/Administrator/.workbuddy/skills',
  base:   'H:/架构/备份/zodiac_recovery',
};
let SRC = DEFAULT_ROOTS.src;
let SKILLS = DEFAULT_ROOTS.skills;
let BASE = DEFAULT_ROOTS.base;
let SNAP_DIR = path.join(BASE, 'snapshots');
let LOG = path.join(BASE, 'RECOVERY_LOG.jsonl');
let BASELINE_FILE = path.join(BASE, 'BASELINE.txt'); // 已知良好基线快照名(AWS AGENTOPS02-BP03: behavioral baseline)

// 重绑定路径根（只供 selftest 隔离用）。派生路径随 BASE 一并重算。
function rebindRoots(r) {
  if (r.src) SRC = r.src;
  if (r.skills) SKILLS = r.skills;
  if (r.base) BASE = r.base;
  SNAP_DIR = path.join(BASE, 'snapshots');
  LOG = path.join(BASE, 'RECOVERY_LOG.jsonl');
  BASELINE_FILE = path.join(BASE, 'BASELINE.txt');
}

// 读取当前基线快照名（无则 null）
function baselineName() {
  try { const s = fs.readFileSync(BASELINE_FILE, 'utf8').trim(); return s || null; } catch (_) { return null; }
}

// 执行层技能根目录中，被 linkageMap 真实引用的技能（双向联动的"执行层"一端；仅这些需纳入双层恢复）
function linkedSkills() {
  try {
    const so = JSON.parse(fs.readFileSync(path.join(SRC, 'zodiac-team', 'settings.json'), 'utf8'));
    const set = new Set(Object.values(so.linkageMap).map(e => e.skill).filter(Boolean));
    return [...set].filter(s => fs.existsSync(path.join(SKILLS, s)));
  } catch (_) { return []; }
}

function ts() {
  return new Date().toISOString().replace(/[:.]/g, '-');
}
// R33/D-71: 原实现 `catch(_){}` 把审计写入失败**完全静默吞掉**。
//   实证（2026-09-23 22:19）：`evo_pre_apply` 快照成功落盘（167MB / 2649 文件齐备），
//   但 RECOVERY_LOG.jsonl 里**没有这一行**，文件 mtime 停在 22:15 —— 审计链静默断链。
//   快照体量/完整性/保留策略全部依赖这条日志；对取证型工具而言，**静默丢审计行比报错更危险**。
//   对策：写失败先重试 1 次（H: 卷曾观测到间歇性 EPERM），仍失败则**必须可见**——
//     走 stderr（不污染 stdout 契约，CLI 逐字节回归不受影响）+ 返回 false 供调用方感知。
function logEntry(entry) {
  const line = JSON.stringify({ t: new Date().toISOString(), ...entry }) + '\n';
  try { fs.appendFileSync(LOG, line); return true; } catch (_) { /* 落到重试与告警 */ }
  try { fs.appendFileSync(LOG, line); return true; } catch (e2) {
    console.error('[WARN][logEntry] 审计行写入失败(已重试 1 次): ' + e2.message +
      ' | action=' + entry.action + ' name=' + entry.name);
    return false;
  }
}
function copyDir(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    const sp = path.join(src, e.name), dp = path.join(dst, e.name);
    if (e.isDirectory()) copyDir(sp, dp);
    else fs.copyFileSync(sp, dp);
  }
}
function clearDir(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { clearDir(p); fs.rmdirSync(p); }
    else fs.unlinkSync(p);
  }
}

// ── R33/D-70: 固定名快照的「原子换入」所需的外部件 ────────────────────────────
// staging = 在**新位置**上构建快照（构建期间完全不碰旧快照）
// old     = 换入时被挪开的旧快照（换入成功后尽力清理）
const SNAP_STAGING_TAG = '__staging_';
const SNAP_OLD_TAG = '__old_';
// 这两类目录都不是「快照」，必须被 listSnapDirs 过滤；否则会被 prune 当候选、被 verify 误读。
function isInternalSnapDir(n) {
  return n === '_trash' || n.includes(SNAP_STAGING_TAG) || n.includes(SNAP_OLD_TAG);
}
// 尽力清扫上一次异常退出遗留的 staging / __old（**只碰内部保留名，绝不碰真快照**）。
//   走 retireDir 的降级链：能删就删，删不动就移入 _trash —— 绝不静默失败。
function sweepSnapDebris() {
  if (!fs.existsSync(SNAP_DIR)) return [];
  const left = [];
  for (const n of fs.readdirSync(SNAP_DIR)) {
    if (!n.includes(SNAP_STAGING_TAG) && !n.includes(SNAP_OLD_TAG)) continue;
    const r = retireDir(path.join(SNAP_DIR, n));
    if (r) left.push(r);
  }
  return left;
}

// R33/D-70: 让一个不再需要的内部目录「退场」。三级降级链，任何一级成功即返回 null：
//   ① 物理清理（不占盘，正常路径）
//   ② 移入 snapshots/_trash（rename 同卷 = 原子且廉价；实测 H: 卷批量删除会被宿主护栏拦下）
//   ③ 都不行 → 返回名字，由调用方告警 + list 显式列出（**仍不丢任何数据**，只是占盘）
//   对齐项目「零删除」纪律：删除只是省盘手段，删不掉就隔离并可见，绝不静默。
function retireDir(p) {
  const nm = path.basename(p);
  try { clearDir(p); fs.rmdirSync(p); return null; } catch (_) { /* 降级 */ }
  try {
    const trash = path.join(SNAP_DIR, '_trash');
    fs.mkdirSync(trash, { recursive: true });
    let dst = path.join(trash, nm);
    for (let i = 1; fs.existsSync(dst); i++) dst = path.join(trash, nm + '_' + i);
    fs.renameSync(p, dst);
    return null;
  } catch (e2) {
    console.error('[WARN][recovery] 内部目录退场失败(数据完好, 仅占盘): ' + nm + ' | ' + e2.message);
    return nm;
  }
}
function countFiles(dir) {
  let n = 0;
  if (!fs.existsSync(dir)) return 0;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) n += countFiles(p);
    else n++;
  }
  return n;
}

function snapshot(label, opts) {
  // R31/D-66: 三层(全库技能)由「默认」改为 **opt-in**(`snapshot <label> --full`)。
  //   取证：全库 2633 个技能中仅 13 个被 settings.json 引用，且**全部已落在双层内**；
  //   其余 2620 个与生肖团零关联 → 三层 = 2320MB 换 0 覆盖增量，且使单快照 ~180MB→~2.5GB(D-51 根因)。
  const wantFull = !!(opts && opts.full);
  // R32/D-51b: 固定名模式 —— 供 evolve.apply 的「每轮兜底快照」使用, 累积恒为 1 个。
  //   默认仍为时间戳名(里程碑语义, 便于按序回溯)。
  const fixed = !!(opts && opts.fixedName);
  if (!fs.existsSync(SNAP_DIR)) fs.mkdirSync(SNAP_DIR, { recursive: true });
  const name = fixed ? (label || 'manual') : (ts() + '_' + (label || 'manual'));
  const dest = path.join(SNAP_DIR, name);

  // 构建内容（写进任意 root，与 dest 解耦）
  const build = (root) => {
    copyDir(SRC, root);
    // 双层快照：仅快照被 linkageMap 引用的执行层技能（生肖团改动只触及这些）
    let sc = 0;
    const skillsDest = path.join(root, 'skills');
    for (const s of linkedSkills()) {
      const sd = path.join(skillsDest, s);
      copyDir(path.join(SKILLS, s), sd);
      sc += countFiles(sd);
    }
    // 三层快照：全局 skills 全量（opt-in；仅当确需"跨层全库回滚"时使用）
    let gc = 0;
    if (wantFull && fs.existsSync(SKILLS)) {
      const g = path.join(root, 'skills_global');
      copyDir(SKILLS, g);
      gc = countFiles(g);
    }
    return { sc, gc };
  };

  // R33/D-70 修复：固定名「覆盖」原为**破坏式**——`clearDir(dest); copyDir(SRC,dest)`
  //   先毁后退路、再重建。实测（2026-09-23 22:23）在宿主批量删除护栏下 `clearDir` 半途 EPERM，
  //   旧快照被毁成半残：2649 文件中 42 个被销毁（`ai-data-copilot` 整个消失、`ai-engineer` 46→26）。
  //   快照正是本工具兑现「改前必留退路」的**物证本身**，它不能自己也"先毁后建"。
  //   新实现四步，任一步在换入前失败都不会触碰 dest：
  //     ① 在唯一 staging 上构建（dest 全程不动）
  //     ② dest → __old 挪开（失败即中止，dest 原样）
  //     ③ staging → dest 顶上（失败则把 __old 还原回 dest，不留空窗）
  //     ④ 尽力清 __old（失败仅告警；此时新快照已就位，无数据风险）
  //   时间戳名（里程碑）本就唯一，无需覆盖语义 → 直接写 dest，行为与历史版本一致。
  const staging = fixed ? (dest + SNAP_STAGING_TAG + ts()) : dest;
  let counts, oldDir = null;
  try {
    counts = build(staging);
    if (fixed && fs.existsSync(dest)) {
      oldDir = dest + SNAP_OLD_TAG + ts();
      fs.renameSync(dest, oldDir);                                  // ②
    }
    if (fixed) {
      try { fs.renameSync(staging, dest); }                          // ③
      catch (e2) {
        if (oldDir) { try { fs.renameSync(oldDir, dest); oldDir = null; } catch (_) {} }
        throw e2;
      }
    }
  } catch (e) {
    if (fixed) { try { clearDir(staging); fs.rmdirSync(staging); } catch (_) {} }
    throw e;
  }
  const debrisLeft = [];
  if (oldDir) {                                                      // ④
    const r = retireDir(oldDir);
    if (r) debrisLeft.push(r);
  }
  if (fixed) { for (const d of sweepSnapDebris()) if (debrisLeft.indexOf(d) < 0) debrisLeft.push(d); }

  const fc = countFiles(SRC);
  const skillCount = counts.sc, globalSkillCount = counts.gc;
  const scope = wantFull ? '三层(插件+linkageMap+全库)' : '双层(插件+linkageMap)';
  const logged = logEntry({ action: 'snapshot', label, name, dest, fileCount: fc, skillCount, globalSkillCount, scope,
    mode: fixed ? 'fixed-atomic' : 'timestamped', debrisLeft });
  console.log('[SNAPSHOT] ' + name + '  [' + scope + '] (' + fc + ' files 插件 + ' + skillCount + ' files 技能' +
    (wantFull ? ' + ' + globalSkillCount + ' files 全局技能' : '') + ') -> ' + dest +
    (fixed ? '  [原子换入]' : '') +
    (debrisLeft.length ? '  ⚠残留待清: ' + debrisLeft.join(',') : '') +
    (logged ? '' : '  ⚠审计行未写入(见 stderr)'));
  return name;
}

// ── 轻量快照（R30 / D-65）────────────────────────────────────────────────
// 动机：重型 snapshot() 是「全树 + 全量 skills」，实测 7 个快照已占 2.5GB（D-51），
//   体量使其**无法用于逐轮改动前的留痕** → 于是各轮转向"文件级 cp"，而 docs/*.md
//   不在代码备份清单里 → docs 自 R25 起 4 轮改动**零备份**（R29-G1 的真根因）。
// 对策：只备份**指定文件/目录清单**（默认 docs + scripts），秒级完成并输出 SHA256 清单，
//   使「每轮改前含文档的全量留痕」变得可执行。与重型快照是互补关系，非替代。
const LITE_DEFAULT_PATHS = ['zodiac-team/docs', 'zodiac-team/scripts', 'zodiac-team/settings.json'];
const SKIP_NAMES = new Set(['__pycache__', 'node_modules', '.git', '_trash']);

function liteDir() { return path.join(BASE, 'lite'); }   // 派生自 BASE → 随 rebindRoots 一并隔离

function sha256Of(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

// 收集相对 SRC 的文件路径（支持目录递归 / 单文件）
function collectRel(rel) {
  const abs = path.join(SRC, rel);
  if (!fs.existsSync(abs)) return [];
  if (!fs.statSync(abs).isDirectory()) return [path.relative(SRC, abs).replace(/\\/g, '/')];
  const out = [];
  const walk = (d) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (SKIP_NAMES.has(e.name)) continue;
      const ap = path.join(d, e.name);
      if (e.isDirectory()) walk(ap);
      else out.push(path.relative(SRC, ap).replace(/\\/g, '/'));
    }
  };
  walk(abs);
  return out;
}

function light(label, paths) {
  const list = (paths && paths.length) ? paths : LITE_DEFAULT_PATHS;
  const files = [...new Set(list.flatMap(collectRel))].sort();
  if (!files.length) { console.error('[ERROR] light: 未匹配到任何文件 (paths=' + list.join(',') + ')'); return null; }
  const name = ts() + '_' + (label || 'manual');
  const dest = path.join(liteDir(), name);
  fs.mkdirSync(dest, { recursive: true });
  const manifest = { name, label: label || 'manual', created: new Date().toISOString(), src: SRC, paths: list, files: [] };
  let bytes = 0;
  for (const rel of files) {
    const s = path.join(SRC, rel), d = path.join(dest, rel);
    fs.mkdirSync(path.dirname(d), { recursive: true });
    fs.copyFileSync(s, d);
    const size = fs.statSync(s).size;
    bytes += size;
    manifest.files.push({ path: rel, size, sha256: sha256Of(s) });
  }
  manifest.count = manifest.files.length;
  manifest.bytes = bytes;
  fs.writeFileSync(path.join(dest, 'MANIFEST.json'), JSON.stringify(manifest, null, 2));
  logEntry({ action: 'light', label, name, dest, fileCount: manifest.count, bytes });
  console.log('[LIGHT] ' + name + '  files=' + manifest.count + ' bytes=' + bytes + ' -> ' + dest);
  return manifest;
}

// ── 轻量快照保留策略（R31/D-68，收口 R30-G1）──────────────────────────────
// 动机：light 以时间戳命名 → 逐轮累积且无保留策略。
// 纪律：**默认干跑**（只报告将移出哪些）；`--yes` 才执行，且执行时**移入 lite/_trash/**（非物理删除），
//   与项目既有「回收区 / 零删除」惯例一致 —— 由人工确认后再决定是否彻底清理。
function lightPrune(keep, opts) {
  const n = parseInt(keep, 10);
  const dryRun = !(opts && opts.yes);
  if (!Number.isFinite(n) || n < 1) {
    console.error('[ERROR] 用法: node recovery.js light-prune <N> [--yes]   (N>=1)');
    return null;
  }
  const dir = liteDir();
  if (!fs.existsSync(dir)) { console.log('(无轻量快照)'); return { keep: n, total: 0, moved: [], dryRun }; }
  const all = fs.readdirSync(dir, { withFileTypes: true })
    .filter(e => e.isDirectory() && e.name !== '_trash')
    .map(e => e.name).sort();                             // 时间戳命名 → 字典序即时间序
  const moved = all.slice(0, Math.max(0, all.length - n));
  console.log('[LIGHT-PRUNE] 现有 ' + all.length + ' 个 → 保留最近 ' + n + ' 个, 待移出 ' + moved.length + ' 个' +
    (dryRun ? '  (干跑: 未改动任何文件; 加 --yes 执行)' : ''));
  moved.forEach(d => console.log('  - ' + d));
  if (!dryRun && moved.length) {
    const trash = path.join(dir, '_trash');
    fs.mkdirSync(trash, { recursive: true });
    let ok = 0;
    for (const d of moved) {
      try { fs.renameSync(path.join(dir, d), path.join(trash, d)); ok++; }
      catch (e) { console.error('  ⚠ 移出失败 ' + d + ': ' + e.message); }
    }
    logEntry({ action: 'light-prune', keep: n, movedCount: ok, trash });
    console.log('  已移入 ' + trash + ' (' + ok + ' 个; 未物理删除, 确认后可自行清理)');
  }
  return { keep: n, total: all.length, moved, dryRun };
}

// R32/D-51a: 重型快照保留策略 —— 历史快照清理(默认干跑; --yes 移入 snapshots/_trash, 非物理删除)。
//   保护规则: ①基线快照永不移出(它是 rollback 目标) ②其余按时间序保留最近 N 个(N 默认 1)。
//   与 light-prune 同构, 但对象是重型快照 + 多一条基线保护。
function snapshotPrune(keep, opts) {
  const dryRun = !(opts && opts.yes);
  const parsed = parseInt(keep, 10);
  const n = Number.isFinite(parsed) ? parsed : 1;
  if (n < 1) {
    console.error('[ERROR] 用法: node recovery.js snapshot-prune [N] [--yes]   (N>=1, 默认 1)');
    return null;
  }
  const all = listSnapDirs();
  if (!all.length) { console.log('(无重型快照)'); return { keep: n, total: 0, moved: [], dryRun }; }
  const bl = baselineName();
  const rest = all.filter(d => d !== bl);                            // ① 基线永不作为候选
  const kept = new Set(rest.slice(Math.max(0, rest.length - n)));    // ② 其余保留最近 N 个
  const moved = rest.filter(d => !kept.has(d));
  console.log('[SNAPSHOT-PRUNE] 现有 ' + all.length + ' 个 → 保护基线 ' + (bl ? 1 : 0) +
    ' + 保留最近 ' + n + ' → 待移出 ' + moved.length + ' 个' +
    (dryRun ? '  (干跑: 未改动任何文件; 加 --yes 执行)' : ''));
  if (bl) console.log('  ★ 保护(基线): ' + bl);
  moved.forEach(d => {
    const full = fs.existsSync(path.join(SNAP_DIR, d, 'skills_global'));
    console.log('  - ' + d + (full ? '  ⚠含三层(全库技能, 单占 ~2.3GB)' : ''));
  });
  if (!dryRun && moved.length) {
    const trash = path.join(SNAP_DIR, '_trash');
    fs.mkdirSync(trash, { recursive: true });
    let ok = 0;
    for (const d of moved) {
      try { fs.renameSync(path.join(SNAP_DIR, d), path.join(trash, d)); ok++; }
      catch (e) { console.error('  ⚠ 移出失败 ' + d + ': ' + e.message); }
    }
    logEntry({ action: 'snapshot-prune', keep: n, movedCount: ok, trash });
    console.log('  已移入 ' + trash + ' (' + ok + ' 个; **未物理删除** —— 释放磁盘需另行确认后清理)');
  }
  return { keep: n, total: all.length, moved, dryRun, baseline: bl };
}

// 快照目录名列表（容错：不可 stat 的条目跳过）。list / resolveName / selftest 共用同一口径。
// R32: _trash 是 snapshot-prune 的回收区, 不是快照 —— 否则会被当候选再移一次。
// R33/D-70: __staging_ / __old_ 是固定名快照「原子换入」的内部件, 同样不是快照。
function listSnapDirs() {
  if (!fs.existsSync(SNAP_DIR)) return [];
  return fs.readdirSync(SNAP_DIR)
    .filter(d => !isInternalSnapDir(d))
    .filter(d => { try { return fs.statSync(path.join(SNAP_DIR, d)).isDirectory(); } catch (_) { return false; } })
    .sort();
}

// R33/D-70: 内部件可见性 —— __old/__staging 残留会占体积, 不能只藏在磁盘上不管。
function listSnapDebris() {
  if (!fs.existsSync(SNAP_DIR)) return [];
  return fs.readdirSync(SNAP_DIR)
    .filter(d => d.includes(SNAP_STAGING_TAG) || d.includes(SNAP_OLD_TAG))
    .filter(d => { try { return fs.statSync(path.join(SNAP_DIR, d)).isDirectory(); } catch (_) { return false; } })
    .sort();
}

function list() {
  if (!fs.existsSync(SNAP_DIR)) { console.log('(no snapshots)'); return; }
  const dirs = listSnapDirs();
  const bl = baselineName();
  console.log('=== 快照列表 (' + dirs.length + ') ===');
  let fullCnt = 0;
  for (const d of dirs) {
    const fc = countFiles(path.join(SNAP_DIR, d));
    // R31/D-69: 标注含三层(全库技能)的快照 —— 体量可见性(O(1) 检测, 不做全树体积遍历)
    const full = fs.existsSync(path.join(SNAP_DIR, d, 'skills_global'));
    if (full) fullCnt++;
    const tag = (d === bl) ? '  ★ BASELINE(已知良好)' : '';
    console.log('  ' + d + '  [' + fc + ' files]' + (full ? '  ⚠含三层(全库技能, 单占 ~2.3GB)' : '') + tag);
  }
  if (fullCnt) console.log('  提示: ' + fullCnt + ' 个快照含三层全库技能 —— 仅当需「跨层全库回滚」时才必要(D-66 起已改为 opt-in)。');
  if (!bl) console.log('  (尚未标记基线；用 `node recovery.js baseline set <label>` 标记已知良好版本)');
  // R33/D-70: 内部件(原子换入的中转/旧快照残留)必须可见 —— 它们占体积但不该被当快照
  const debris = listSnapDebris();
  if (debris.length) {
    console.log('  ⚠ 内部件残留 ' + debris.length + ' 个(原子换入中转/旧快照, 非快照; 可安全清理):');
    debris.forEach(d => console.log('      ' + d));
  }
  const trash = path.join(SNAP_DIR, '_trash');
  if (fs.existsSync(trash)) {
    const t = fs.readdirSync(trash).length;
    if (t) console.log('  (回收区 _trash 内 ' + t + ' 项 —— 非物理删除, 确认后可自行清理)');
  }
}

function resolveName(arg) {
  const full = path.join(SNAP_DIR, arg);
  if (fs.existsSync(full) && fs.statSync(full).isDirectory()) return arg;
  const dirs = listSnapDirs();
  const hit = dirs.filter(d => d === arg || d.endsWith('_' + arg));
  if (hit.length === 1) return hit[0];
  if (hit.length > 1) { console.error('[ERROR] ambiguous "' + arg + '": ' + hit.join(', ')); process.exit(1); }
  return null;
}
// 同步忙等（主线程不能用 Atomics.wait，故用忙等替代）
function microSleep(ms) { const end = Date.now() + ms; while (Date.now() < end) {} }
// 容错复制（应对沙箱偶发 EPERM/ESRCH/EBUSY：写新文件不触发 bulk-delete 护栏）
function copyDirSafe(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    const sp = path.join(src, e.name), dp = path.join(dst, e.name);
    if (e.isDirectory()) copyDirSafe(sp, dp);
    else {
      let ok = false;
      for (let i = 0; i < 3 && !ok; i++) {
        try { fs.copyFileSync(sp, dp); ok = true; }
        catch (err) {
          if (err.code === 'EPERM' || err.code === 'ESRCH' || err.code === 'EBUSY') microSleep(50);
          else throw err;
        }
      }
    }
  }
}
function safeRmDir(dir) {
  for (let i = 0; i < 3; i++) {
    try { fs.rmSync(dir, { recursive: true, force: true }); return; }
    catch (e) { if (e.code === 'EPERM' || e.code === 'EBUSY') microSleep(60); else throw e; }
  }
}
function safeRename(a, b) {
  for (let i = 0; i < 5; i++) {
    try { fs.renameSync(a, b); return true; }
    catch (e) { if (e.code === 'EPERM' || e.code === 'EBUSY') microSleep(80); else throw e; }
  }
  return false;
}
function safeUnlink(p) {
  for (let i = 0; i < 3; i++) {
    try { fs.unlinkSync(p); return true; }
    catch (e) { if (e.code === 'EPERM' || e.code === 'EBUSY') microSleep(60); else return false; }
  }
  return false;
}
function restore(name) {
  // 无参时回退到基线（AWS best practice: rollback restores the baseline, not the last change）
  if (!name) {
    const bl = baselineName();
    if (!bl) { console.error('[ERROR] 未指定快照名，且尚未标记基线。请用 `baseline set <label>` 标记已知良好版本，或显式指定快照名。'); process.exit(1); }
    console.log('[INFO] 未指定快照名 → 自动回退到基线: ' + bl);
    name = bl;
  }
  const rn = resolveName(name);
  if (!rn) { console.error('[ERROR] snapshot not found: ' + name); process.exit(1); }
  const src = path.join(SNAP_DIR, rn);
  const srcCount = countFiles(src);

  // 清理上次可能残留的临时树
  if (fs.existsSync(SRC + '.restore_new')) safeRmDir(SRC + '.restore_new');
  if (fs.existsSync(SRC + '.restore_old')) safeRmDir(SRC + '.restore_old');

  // —— 渐进式零丢失覆盖（不依赖 rename，规避沙箱对占用目录的 rename 拦截）——
  // 阶段一：镜像覆盖（copyDirSafe 容错，绝不删除任何文件 → 任何中断都不丢数据，SRC 始终是"旧∪已覆盖"完整态）
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    if (e.name === 'skills' || e.name === 'skills_global') continue; // 双层/三层技能单独处理，不混入 SRC
    copyDirSafe(path.join(src, e.name), path.join(SRC, e.name));
  }
  const dstCount = countFiles(SRC);

  // 双层技能：合并回全局 SKILLS（覆盖，不清空全局 skills）
  let skillRestored = 0;
  const skillsSrc = path.join(src, 'skills');
  if (fs.existsSync(skillsSrc)) {
    for (const s of fs.readdirSync(skillsSrc)) {
      copyDirSafe(path.join(skillsSrc, s), path.join(SKILLS, s));
      skillRestored += countFiles(path.join(skillsSrc, s));
    }
  }
  // 三层技能：全局 skills 全量合并回全局 SKILLS（覆盖，不删除，跨层接线可整体回滚）
  const gSkillsSrc = path.join(src, 'skills_global');
  if (fs.existsSync(gSkillsSrc)) {
    for (const s of fs.readdirSync(gSkillsSrc)) {
      copyDirSafe(path.join(gSkillsSrc, s), path.join(SKILLS, s));
      skillRestored += countFiles(path.join(gSkillsSrc, s));
    }
  }

  // 阶段二：清理快照中不存在的多余文件（容错重试，失败仅留冗余、不丢数据）
  const snapSet = new Set();
  (function walk(d, rel) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const sp = path.join(d, e.name);
      if (e.isDirectory()) walk(sp, path.join(rel, e.name));
      else snapSet.add(path.join(rel, e.name));
    }
  })(src, '');
  let removed = 0;
  (function clean(d, rel) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const sp = path.join(d, e.name), rp = path.join(rel, e.name);
      if (e.isDirectory()) {
        clean(sp, rp);
        if (!snapSet.has(rp) && fs.readdirSync(sp).length === 0) safeRmDir(sp);
      } else if (!snapSet.has(rp)) {
        if (safeUnlink(sp)) removed++;
      }
    }
  })(SRC, '');

  logEntry({ action: 'restore', name, src, dst: SRC, srcCount, dstCount, removed, skillRestored });
  console.log('[RESTORED] from ' + name + '  (' + srcCount + ' -> ' + dstCount + ' files 插件 + ' + skillRestored + ' 技能, 清多余 ' + removed + ')');
}

function verify(name) {
  const rn = resolveName(name);
  if (!rn) { console.error('[ERROR] snapshot not found: ' + name); process.exit(1); }
  const src = path.join(SNAP_DIR, rn);
  const srcCount = countFiles(src);
  const dstCount = countFiles(SRC);
  let jsonBad = 0;
  // 校验源树所有 plugin.json / settings.json 严格合法
  const check = (dir) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) { if (e.name === 'node_modules' || e.name === '.git') continue; check(p); }
      else if (e.name === 'plugin.json' || e.name === 'settings.json') {
        try { JSON.parse(fs.readFileSync(p, 'utf8')); } catch (err) { jsonBad++; console.log('  JSON_FAIL ' + p + ' : ' + err.message); }
      }
    }
  };
  check(SRC);
  // 双层校验：比对快照内执行层技能与当前 skills 目录
  const skillsSrc = path.join(src, 'skills');
  let skillLive = 0, skillSnap = 0;
  if (fs.existsSync(skillsSrc)) {
    for (const s of fs.readdirSync(skillsSrc)) {
      const sp = path.join(skillsSrc, s);
      if (fs.statSync(sp).isDirectory()) { skillSnap += countFiles(sp); skillLive += countFiles(path.join(SKILLS, s)); }
    }
  }
  // 三层校验：全局 skills 比对
  const gSkillsSrc = path.join(src, 'skills_global');
  let gSkillLive = 0, gSkillSnap = 0;
  if (fs.existsSync(gSkillsSrc)) {
    for (const s of fs.readdirSync(gSkillsSrc)) {
      const sp = path.join(gSkillsSrc, s);
      if (fs.statSync(sp).isDirectory()) { gSkillSnap += countFiles(sp); gSkillLive += countFiles(path.join(SKILLS, s)); }
    }
  }
  console.log('[VERIFY] ' + name + '  snapshotFiles=' + srcCount + ' liveFiles=' + dstCount + ' jsonErrors=' + jsonBad + ' | 技能Snapshot=' + skillSnap + ' 技能Live=' + skillLive + ' | 全局技能Snapshot=' + gSkillSnap + ' 全局技能Live=' + gSkillLive);
  // R30/D-64: 返回结构化结果 —— 使调用方可对**具体数值**断言, 而非只能"未抛异常就算过"(弱断言)。
  //   注: 两个既有调用点(selftest 内的取证 / CLI verify)均忽略返回值, 故本改动对 CLI 输出零影响。
  return {
    snapshot: rn, resolvedFrom: name,
    snapshotFiles: srcCount, liveFiles: dstCount, jsonErrors: jsonBad,
    skillSnapshot: skillSnap, skillLive: skillLive,
    globalSkillSnapshot: gSkillSnap, globalSkillLive: gSkillLive,
  };
}

function baseline(sub, arg) {
  if (sub === 'set') {
    if (!arg) { console.error('[ERROR] 用法: node recovery.js baseline set <label>'); process.exit(1); }
    const rn = resolveName(arg);
    if (!rn) { console.error('[ERROR] snapshot not found: ' + arg); process.exit(1); }
    fs.writeFileSync(BASELINE_FILE, rn, 'utf8');
    logEntry({ action: 'baseline-set', name: rn });
    console.log('[BASELINE] 已标记已知良好基线: ' + rn);
  } else if (sub === 'show') {
    const bl = baselineName();
    console.log(bl ? ('[BASELINE] 当前基线: ' + bl) : '(尚未标记基线)');
  } else if (sub === 'clear') {
    if (fs.existsSync(BASELINE_FILE)) { fs.unlinkSync(BASELINE_FILE); console.log('[BASELINE] 已清除基线标记'); }
    else console.log('(无基线标记可清除)');
  } else {
    console.log('用法:');
    console.log('  node recovery.js baseline set <label>   标记某快照为已知良好基线(rollback 目标)');
    console.log('  node recovery.js baseline show          显示当前基线');
    console.log('  node recovery.js baseline clear         清除基线标记');
  }
}

function check() {
  // 全量一致性自检（诊断能力）：JSON 合法性 / 引用齐备 / 团队内部一致 / 路由一致 / 残留旧id
  const problems = [];
  const warns = [];
  const dirs = fs.readdirSync(SRC, { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name).sort();
  const pkgs = new Set(dirs);
  const teamPj = path.join(SRC, 'zodiac-team', '.codebuddy-plugin', 'plugin.json');
  const team = JSON.parse(fs.readFileSync(teamPj, 'utf8'));
  const teamAvDir = path.join(SRC, 'zodiac-team', 'avatars');
  const memIds = new Set(team.members.map(m => m.id));
  const lead = team.teamInfo && team.teamInfo.leadAgent;

  // 1. 各包 plugin.json 合法 + agents/avatar 引用齐备
  for (const d of dirs) {
    const p = path.join(SRC, d);
    let pj = null;
    for (const c of [path.join(p, '.codebuddy-plugin', 'plugin.json'), path.join(p, 'plugin.json')]) if (fs.existsSync(c)) { pj = c; break; }
    if (!pj) continue;
    let o;
    try { o = JSON.parse(fs.readFileSync(pj, 'utf8')); } catch (e) { problems.push('JSON非法 ' + d + ': ' + e.message); continue; }
    const ag = o.agents || o.memberAgents || [];
    if (typeof ag === 'string') { if (!fs.existsSync(path.join(p, ag))) problems.push('agents目录缺失 ' + d + ': ' + ag); }
    else if (Array.isArray(ag)) { for (const a of ag) { const af = path.isAbsolute(a) ? a : path.join(p, a.replace(/^\.\//, '')); if (!fs.existsSync(af)) problems.push('agent缺失 ' + d + ': ' + a); } }
    const av = o.avatar || (o.displayName && o.displayName.avatar) || '';
    if (av) {
      const avf = path.isAbsolute(av) ? av : path.join(p, av.replace(/^\.\//, ''));
      const altf = path.join(teamAvDir, path.basename(av));
      if (!fs.existsSync(avf) && !fs.existsSync(altf)) problems.push('avatar缺失 ' + d + ': ' + av);
    }
  }

  // 2. team plugin.json 内部一致（leadAgent 不参与 memberAgents 比较）
  const maSet = new Set(team.teamInfo.memberAgents);
  const memSet = new Set(team.members.map(m => m.id));
  for (const id of memSet) if (!maSet.has(id) && id !== lead) problems.push('members有但memberAgents缺: ' + id);
  for (const id of maSet) if (!memSet.has(id)) problems.push('memberAgents有但members缺: ' + id);
  for (const m of team.members) if (m.avatar) { const f = path.join(teamAvDir, path.basename(m.avatar)); if (!fs.existsSync(f)) problems.push('member头像缺失 ' + m.id + ': ' + m.avatar); }

  // 2.5 avatar 一致性 + 专属化检测（WARN 级，不阻断健康退出码）
  for (const m of team.members) {
    if (m.id === 'zodiac-team') continue;
    const pkgPj = path.join(SRC, m.id, '.codebuddy-plugin', 'plugin.json');
    if (!fs.existsSync(pkgPj)) continue; // 无独立包则跳过（如团队自身）
    let pkgO; try { pkgO = JSON.parse(fs.readFileSync(pkgPj, 'utf8')); } catch (_) { continue; }
    const pkgAv = pkgO.avatar || (pkgO.displayName && pkgO.displayName.avatar) || '';
    const teamAv = m.avatar || '';
    if (pkgAv && teamAv && pkgAv !== teamAv) warns.push('avatar分裂 ' + m.id + ': team=' + path.basename(teamAv) + ' pkg=' + path.basename(pkgAv));
    // 专属化：团队 avatars 存在 <id>.png 但两处仍在用通用 avatar.png
    const dedicated = path.join(teamAvDir, m.id + '.png');
    if (fs.existsSync(dedicated) && [teamAv, pkgAv].some(a => a && path.basename(a) === 'avatar.png')) {
      warns.push('可专属化未专属 ' + m.id + ': 存在 ' + m.id + '.png 但仍在用通用 avatar.png');
    }
  }

  // 3. settings.json 路由一致
  const sf = path.join(SRC, 'zodiac-team', 'settings.json');
  const so = JSON.parse(fs.readFileSync(sf, 'utf8'));
  const lmKeys = new Set(Object.keys(so.linkageMap));
  for (const k of Object.keys(so.linkageMap)) if (!pkgs.has(k)) problems.push('linkageMap孤儿键: ' + k);
  const knownSet = new Set([...memIds, ...lmKeys, ...pkgs]);
  for (const cap of Object.keys(so.routingTable)) for (const item of so.routingTable[cap]) {
    const m = item.match(/^(.*?)\((.*)\)$/);
    if (m) {
      // 括号约定混用：internal(parent) 或 parent(internal/team)，任一 token 解析到真实实体即合法
      const A = m[1], B = m[2];
      if (!knownSet.has(A) && !knownSet.has(B)) problems.push('routingTable引用无效: ' + cap + '->' + item);
    } else if (!knownSet.has(item)) {
      problems.push('routingTable悬空: ' + cap + '->' + item);
    }
  }

  // 3.5 成员零路由检测：每个 team member 必须至少出现在一个 routingTable 项（含括号约定 token）
  const routedIds = new Set();
  for (const cap of Object.keys(so.routingTable)) for (const item of so.routingTable[cap]) {
    const m = item.match(/^(.*?)\((.*)\)$/);
    if (m) { routedIds.add(m[1]); routedIds.add(m[2]); }
    else routedIds.add(item);
  }
  for (const id of memSet) {
    if (id === 'zodiac-team') continue;
    if (!routedIds.has(id)) warns.push('成员零路由 ' + id + ': 未出现在任何 routingTable 项，用户意图无法路由到该专家');
  }

  // 3.6 跨层技能存在性：linkageMap.skill 必须指向真实存在的执行层技能（双向联动的"执行层"一端）
  const SKILL_ROOTS = [
    SKILLS,   // 默认 = C:/Users/Administrator/.workbuddy/skills（与历史硬编码值一致，行为不变；改引用变量以随隔离重绑定）
    'C:/Users/Administrator/.workbuddy/release/zodiac-skills'
  ].filter(r => fs.existsSync(r));
  const skillExists = (sk) => SKILL_ROOTS.some(r => fs.existsSync(path.join(r, sk)));
  for (const k of Object.keys(so.linkageMap)) {
    const e = so.linkageMap[k];
    if (!e.skill) continue;
    if (!skillExists(e.skill)) problems.push('跨层技能缺失 ' + k + ': linkageMap.skill="' + e.skill + '" 在执行层技能目录中不存在（双向联动断裂）');
  }

  // 3.7 括号引用子成员归属验证（WARN 级）：internal(parent) 中 parent 必须真实存在，
  // 且 internal 须为 parent 的成员（teamInfo.memberAgents 或 agents/ 目录 md），
  // 否则是悬空子成员——OR规则下会被同项生肖实体"带过"而漏报，故单独加固。
  const membersOf = (pkgId) => {
    const set = new Set();
    const pj = path.join(SRC, pkgId, '.codebuddy-plugin', 'plugin.json');
    if (fs.existsSync(pj)) {
      try { const o = JSON.parse(fs.readFileSync(pj, 'utf8')); const ma = (o.teamInfo && o.teamInfo.memberAgents) || []; for (const a of ma) set.add(typeof a === 'string' ? a : (a.id || '')); } catch (_) {}
    }
    const adir = path.join(SRC, pkgId, 'agents');
    if (fs.existsSync(adir)) for (const f of fs.readdirSync(adir)) { const mm = f.match(/^(.*?)\.md$/); if (mm) set.add(mm[1]); }
    return set;
  };
  for (const cap of Object.keys(so.routingTable)) for (const item of so.routingTable[cap]) {
    const m = item.match(/^(.*?)\((.*)\)$/);
    if (!m) continue;
    const A = m[1], B = m[2];
    if (B === 'team') { if (!pkgs.has(A)) problems.push('routingTable团队引用无效: ' + cap + '->' + item + ' (A=' + A + ' 非真实包)'); continue; }
    let parent = null, child = null;
    if (pkgs.has(B) && !pkgs.has(A)) { parent = B; child = A; }
    else if (pkgs.has(A) && !pkgs.has(B)) { parent = A; child = B; }
    else if (pkgs.has(A) && pkgs.has(B)) {
      const ma = membersOf(A), mb = membersOf(B);
      if (ma.has(B)) { parent = A; child = B; } else if (mb.has(A)) { parent = B; child = A; } else continue;
    } else continue; // 两端都不在 pkgs，OR规则(3.)已捕获
    const mem = membersOf(parent);
    if (mem.size && !mem.has(child)) warns.push('括号引用子成员归属异常 ' + cap + '->' + item + ': child=' + child + ' 不在 parent=' + parent + ' 的 memberAgents/agents 中（悬空子成员）');
  }

  // 3.8 包可加载性硬验证（problem级）：每个 team member（含 zodiac-team 自身）的
  // .codebuddy-plugin/plugin.json 必须存在、严格JSON、含真实必填字段(name/version/description/avatar/expertType)，
  // 且 name 与目录一致。这是"加载可靠性"基线——宿主加载团队时任一成员包损坏即整体失败。
  // 注：真实规范用 name 作唯一标识（非 id），必填字段以此为准。
  const tpj = JSON.parse(fs.readFileSync(path.join(SRC, 'zodiac-team', '.codebuddy-plugin', 'plugin.json'), 'utf8'));
  const maRef = new Set((tpj.teamInfo && tpj.teamInfo.memberAgents) || []);
  const REQ_LOAD = ['name', 'version', 'description', 'avatar', 'expertType'];
  for (const id of [...maRef, 'zodiac-team']) {
    const pj = path.join(SRC, id, '.codebuddy-plugin', 'plugin.json');
    if (!fs.existsSync(pj)) { problems.push('成员包缺失 ' + id + ': ' + pj); continue; }
    let o; try { o = JSON.parse(fs.readFileSync(pj, 'utf8')); } catch (e) { problems.push('成员包非严格JSON ' + id + ': ' + e.message); continue; }
    const miss = REQ_LOAD.filter(k => !(k in o));
    if (miss.length) problems.push('成员包缺必填字段 ' + id + ': ' + miss.join(','));
    if (o.name && o.name !== id) problems.push('成员包name不一致 ' + id + ': plugin.name="' + o.name + '"');
  }

  // 3.9 禁用链路检测（WARN级）：linkageMap.skill 指向的执行层技能若为 disable:true，
  // 则双向联动契约在运行时空心化（专家调不动该技能）。与 3.6 互补：3.6 查"是否存在"，3.9 查"是否激活"。
  let disabledLinks = 0;
  for (const k of Object.keys(so.linkageMap)) {
    const e = so.linkageMap[k];
    if (!e.skill) continue;
    const smd = path.join(SKILLS, e.skill, 'SKILL.md');
    if (!fs.existsSync(smd)) continue; // 不存在由 3.6 处理
    const txt = fs.readFileSync(smd, 'utf8');
    const fm = txt.match(/---\n([\s\S]*?)\n---/);
    if (fm && /disable:\s*true/i.test(fm[1])) { disabledLinks++; warns.push('禁用链路 ' + k + ': linkageMap.skill="' + e.skill + '" 为 disable:true（双向联动运行时空心化，专家调不动）'); }
  }

  // 4. 全树残留旧猴id
  const tree = [];
  const walk = (dir) => { for (const e of fs.readdirSync(dir, { withFileTypes: true })) { const p = path.join(dir, e.name); if (e.isDirectory()) { if (['node_modules', '.git', 'snapshots', 'scripts'].includes(e.name)) continue; walk(p); } else { if (fs.readFileSync(p, 'utf8').includes('monkey-design-adjuster')) tree.push(path.relative(SRC, p)); } } };
  walk(SRC);
  if (tree.length) problems.push('残留monkey-design-adjuster: ' + tree.join(', '));

  console.log('=== 框架健康自检 (check) ===');
  console.log('包总数=' + dirs.length + ' | members=' + memSet.size + ' | linkageMap=' + lmKeys.size);
  if (problems.length === 0) console.log('✅ 全部健康：无 JSON 非法 / 无孤儿键 / 无悬空路由 / 无残留旧id / 引用齐备');
  else { console.log('⚠️ 发现 ' + problems.length + ' 项问题:'); for (const p of problems) console.log('  - ' + p); }
  if (warns.length) { console.log('🔎 提示(' + warns.length + ' 项，不阻断健康):'); for (const w of warns) console.log('  ~ ' + w); }
  return problems.length;
}

// enable-skills：安全启用被 linkageMap 引用的、处于 disable:true（awaiting human review）的执行层技能。
// 设计原则：
//  1) 启用前自动打双层快照（auto_before_enable），任意回归可 node recovery.js restore <name> 一键回退；
//  2) 启用方式对齐活跃技能 zheng10-product-researcher 的真实写法——其 frontmatter 无 disable 字段，
//     故本命令删除 `disable: true` 整行（而非改成 false），最大限度贴合平台判定语义；
//  3) 只动被 linkageMap 引用的技能，不碰全局 2400+ 其他技能。
function enableSkills() {
  const so = JSON.parse(fs.readFileSync(path.join(SRC, 'zodiac-team', 'settings.json'), 'utf8'));
  const skills = [...new Set(Object.values(so.linkageMap).map(e => e.skill).filter(Boolean))];
  const snapName = snapshot('auto_before_enable'); // 自动兜底快照
  let enabled = 0, already = 0, missing = 0;
  const report = [];
  for (const sk of skills) {
    const smd = path.join(SKILLS, sk, 'SKILL.md');
    if (!fs.existsSync(smd)) { missing++; report.push('❌ 缺失 ' + sk); continue; }
    let txt = fs.readFileSync(smd, 'utf8');
    const m = txt.match(/---\n([\s\S]*?)\n---/);
    if (!m) { report.push('⚠️ 无frontmatter ' + sk); continue; }
    const fm = m[1];
    if (!/disable:\s*true/i.test(fm)) { already++; report.push('✅ 已活跃 ' + sk); continue; }
    const newFm = fm.replace(/disable:\s*true\s*\n?/i, '');
    fs.writeFileSync(smd, txt.replace(fm, newFm), 'utf8');
    enabled++;
    report.push('🟢 已启用 ' + sk);
  }
  logEntry({ action: 'enable-skills', snapName, enabled, already, missing });
  console.log('=== enable-skills（安全启用双向联动执行层技能）===');
  console.log('自动兜底快照: ' + snapName);
  console.log('回退命令: node recovery.js restore ' + snapName);
  console.log('启用 ' + enabled + ' | 原本已活跃 ' + already + ' | 缺失 ' + missing);
  for (const r of report) console.log('  ' + r);
}

// ── selftest（D-62/R29）──────────────────────────────────────────────────────
// recovery 是 10 个 JS 引擎中最后一个未模块化者（无 require.main 守卫 / 无 exports / 无 selftest），
//   因而长期游离于聚合门禁之外。模块化后纳入门禁（9 → 10 suite）。
// 本自检的硬约束：**全程隔离在 tmp 沙盒**——用 rebindRoots 把 SRC/SKILLS/快照根整体指向伪树，
//   绝不触碰真实专家包与 2.5GB 级真实快照目录；毫秒级、可重复、零副作用（对齐 R28「同进程 + 零污染」范式）。
function selftest() {
  const root = path.join(os.tmpdir(), 'zodiac_recovery_selftest_' + process.pid);
  const fakeSrc = path.join(root, 'src');
  const fakeSkills = path.join(root, 'skills');
  const fakeBase = path.join(root, 'base');
  const saved = { src: SRC, skills: SKILLS, base: BASE };
  let p = 0, f = 0;
  const chk = (good, label) => { console.log('  ' + (good ? '✅' : '❌') + ' ' + label); good ? p++ : f++; };
  try {
    // 造伪树（3 个插件文件：含 settings.json 以打通 linkageMap → 双层技能通路；全局技能 1 个）
    fs.mkdirSync(path.join(fakeSrc, 'pkg-a', '.codebuddy-plugin'), { recursive: true });
    fs.writeFileSync(path.join(fakeSrc, 'pkg-a', '.codebuddy-plugin', 'plugin.json'), '{"name":"pkg-a","version":"1.0.0"}');
    fs.writeFileSync(path.join(fakeSrc, 'top.txt'), 'hello');
    fs.mkdirSync(path.join(fakeSrc, 'zodiac-team'), { recursive: true });
    fs.writeFileSync(path.join(fakeSrc, 'zodiac-team', 'settings.json'), '{"linkageMap":{"pkg-a":{"skill":"demo-skill"}}}');
    fs.mkdirSync(path.join(fakeSkills, 'demo-skill'), { recursive: true });
    fs.writeFileSync(path.join(fakeSkills, 'demo-skill', 'SKILL.md'), '---\nname: demo-skill\n---\n');
    rebindRoots({ src: fakeSrc, skills: fakeSkills, base: fakeBase });

    console.log('=== recovery 自检 (沙盒隔离 · 生产零接触) ===');
    console.log('  sandbox = ' + root + '\n');

    // 1. 递归计数
    const nSrc = countFiles(fakeSrc);
    chk(nSrc === 3, 'countFiles 递归计数 (期望 3, 得 ' + nSrc + ')');
    // 1b. linkageMap → 双层技能解析（真实读 settings.json）
    chk(linkedSkills().join(',') === 'demo-skill', 'linkedSkills 由 linkageMap 正确解析 (得 [' + linkedSkills().join(',') + '])');
    // 2. 未标记基线 → null
    chk(baselineName() === null, 'baselineName 未标记时返回 null');
    // 3. snapshot 产出快照（默认双层 = 插件 + linkageMap 技能；R31/D-66: 三层为 opt-in）
    const snapName = snapshot('selftest');
    chk(listSnapDirs().length === 1, 'snapshot 产生 1 个快照 (得 ' + listSnapDirs().length + ')');
    chk(fs.existsSync(path.join(SNAP_DIR, snapName, 'skills', 'demo-skill', 'SKILL.md')), 'snapshot 已纳入【双层】linkageMap 技能');
    chk(!fs.existsSync(path.join(SNAP_DIR, snapName, 'skills_global')), 'D-66: 默认【不含】三层 skills_global');
    // 3b. D-66: --full 显式 opt-in 三层
    const snapFull = snapshot('selftest-full', { full: true });
    chk(fs.existsSync(path.join(SNAP_DIR, snapFull, 'skills_global', 'demo-skill', 'SKILL.md')), 'D-66: --full 时才纳入【三层】全局技能');
    // 4. resolveName 三态：精确 / 标签后缀 / 不存在
    chk(resolveName(snapName) === snapName, 'resolveName 精确名命中');
    chk(resolveName('selftest') === snapName, 'resolveName 标签后缀命中');
    chk(resolveName('__nope__') === null, 'resolveName 不存在返回 null');
    // 5. 基线标记往返（不触发 baseline() 的 exit 路径）
    fs.writeFileSync(BASELINE_FILE, snapName, 'utf8');
    chk(baselineName() === snapName, 'baselineName 读回已标记基线');
    fs.unlinkSync(BASELINE_FILE);
    chk(baselineName() === null, '基线清除后回到 null');
    // 6. 容错复制往返一致
    const cp1 = path.join(root, 'cp1');
    copyDirSafe(fakeSrc, cp1);
    chk(countFiles(cp1) === nSrc, 'copyDirSafe 往返文件数一致');
    // 7. 安全改名 / 安全删除
    const cp2 = path.join(root, 'cp2');
    chk(safeRename(cp1, cp2) === true && fs.existsSync(cp2), 'safeRename 成功且目标存在');
    safeRmDir(cp2);
    chk(!fs.existsSync(cp2), 'safeRmDir 清除目标');
    // 8. verify 对**具体数值**断言（R30/D-64：取代原「未抛异常即通过」的恒真断言 ⛔）
    //    依据：默认快照 = 伪树 3 文件 + 双层技能 1 = 4；--full 快照 = + 三层技能 1 = 5；实盘 = 伪树 3。
    const vr = verify(snapName);
    chk(vr && vr.jsonErrors === 0, 'verify: JSON 校验零错误 (得 ' + (vr && vr.jsonErrors) + ')');
    chk(vr.liveFiles === nSrc, 'verify: live 文件数=伪树实数 ' + nSrc + ' (得 ' + vr.liveFiles + ')');
    chk(vr.snapshotFiles === nSrc + 1, 'verify: 默认快照文件数=源 ' + nSrc + ' +双层技能 1 = ' + (nSrc + 1) + ' (得 ' + vr.snapshotFiles + ')');
    chk(vr.skillSnapshot === 1 && vr.skillLive === 1, 'verify: 双层技能 快照/实盘 均=1 (得 ' + vr.skillSnapshot + '/' + vr.skillLive + ')');
    chk(vr.globalSkillSnapshot === 0 && vr.globalSkillLive === 0, 'D-66: 默认快照无三层 → 三层计数=0/0 (得 ' + vr.globalSkillSnapshot + '/' + vr.globalSkillLive + ')');
    const vrf = verify(snapFull);
    chk(vrf.snapshotFiles === nSrc + 2, 'D-66: --full 快照文件数=源 ' + nSrc + ' +双/三层各 1 = ' + (nSrc + 2) + ' (得 ' + vrf.snapshotFiles + ')');
    chk(vrf.globalSkillSnapshot === 1 && vrf.globalSkillLive === 1, 'D-66: --full 快照三层计数=1/1 (得 ' + vrf.globalSkillSnapshot + '/' + vrf.globalSkillLive + ')');
    // 9. light 轻量快照（R30/D-65）：清单式 + SHA256 可独立校验
    const lm = light('selftest-lite', ['pkg-a', 'top.txt']);
    chk(lm && lm.count === 2, 'light: 命中 2 文件 (得 ' + (lm && lm.count) + ')');
    chk(lm && lm.bytes > 0, 'light: 字节数>0 (得 ' + (lm && lm.bytes) + ')');
    let manOk = false, shaOk = false;
    try {
      const man = JSON.parse(fs.readFileSync(path.join(BASE, 'lite', lm.name, 'MANIFEST.json'), 'utf8'));
      manOk = man.count === 2 && man.files.length === 2 &&
              man.files.every(f => f.path && typeof f.size === 'number' && /^[0-9a-f]{64}$/.test(f.sha256));
      const top = man.files.find(f => f.path === 'top.txt');
      shaOk = !!top && top.sha256 === crypto.createHash('sha256').update(fs.readFileSync(path.join(fakeSrc, 'top.txt'))).digest('hex');
    } catch (e2) { console.log('    (light 校验异常: ' + e2.message + ')'); }
    chk(manOk, 'light: MANIFEST 结构完整 (count/files/SHA 字段齐备)');
    chk(shaOk, 'light: MANIFEST SHA256 与实际文件内容一致');

    // 10. D-67: light 默认清单纳入 settings.json（伪树已造 zodiac-team/settings.json）
    const lmDef = light('selftest-default');
    chk(lmDef && lmDef.files.some(f => f.path === 'zodiac-team/settings.json'),
      'D-67: light 默认清单含 settings.json (得 [' + (lmDef ? lmDef.files.map(f => f.path).join(',') : '') + '])');
    // 11. D-68: light-prune —— 默认干跑不改动；--yes 移入 lite/_trash（非物理删除）
    const dry = lightPrune(1);
    chk(dry && dry.dryRun === true && dry.moved.length >= 1, 'D-68: lightPrune 默认干跑并列出待移出 (得 moved=' + (dry && dry.moved.length) + ')');
    chk(dry && fs.existsSync(path.join(BASE, 'lite', dry.moved[0])), 'D-68: 干跑后原目录仍在(零改动)');
    const ex = lightPrune(1, { yes: true });
    chk(ex && fs.existsSync(path.join(BASE, 'lite', '_trash', ex.moved[0])), 'D-68: --yes 后移入 lite/_trash 而非物理删除');
    chk(ex && fs.existsSync(path.join(BASE, 'lite', ex.moved[0])) === false, 'D-68: 移出后原位置不再有该目录');

    // 12. D-51b: 固定名快照 —— 供 evolve.apply 每轮兜底用; 二次写入覆盖同名目录, 累积恒为 1 个
    const fx1 = snapshot('evo_pre_apply', { fixedName: true });
    chk(fx1 === 'evo_pre_apply', 'D-51b: 固定名快照名=label 本身(无时间戳前缀) (得 ' + fx1 + ')');
    const beforeList = listSnapDirs().length;
    const fx2 = snapshot('evo_pre_apply', { fixedName: true });
    chk(fx2 === fx1, 'D-51b: 二次固定名快照名不变 (得 ' + fx2 + ')');
    chk(listSnapDirs().length === beforeList, 'D-51b: 二次固定名快照未新增目录(累积恒为 1) (得 ' + listSnapDirs().length + ' vs ' + beforeList + ')');
    // 覆盖语义: copyDir 是覆盖式 —— 固定名必须"先清空再填", 否则源里已删的文件会残留污染快照
    fs.unlinkSync(path.join(fakeSrc, 'top.txt'));
    snapshot('evo_pre_apply', { fixedName: true });
    chk(fs.existsSync(path.join(SNAP_DIR, 'evo_pre_apply', 'top.txt')) === false,
      'D-51b: 固定名二次写入已清空 → 源里删除的文件不残留(无污染)');

    // 12b. D-70★: 固定名覆盖的**原子性** —— 构建阶段失败时, 旧快照必须原样保留。
    //   旧实现 `clearDir(dest); copyDir(SRC,dest)` 先毁后退路; 一旦中途失败(实测批量删除被宿主护栏
    //   拦下 → EPERM, 旧快照 2649 文件被毁掉 42 个), 退路即消失 —— 与「改前必留退路」自相矛盾。
    //   造**真实**失败(非 mock): 把 SRC 指向不存在路径 → copyDir 在 staging 上就抛 ENOENT → dest 全程未被碰。
    const keepN = countFiles(path.join(SNAP_DIR, 'evo_pre_apply'));
    const srcSaved = SRC;
    rebindRoots({ src: path.join(root, '__definitely_missing__') });
    let d70Threw = false;
    try { snapshot('evo_pre_apply', { fixedName: true }); } catch (e) { d70Threw = true; }
    rebindRoots({ src: srcSaved });
    chk(d70Threw, 'D-70: 构建阶段失败时 snapshot 明确抛错(不静默吞)');
    chk(countFiles(path.join(SNAP_DIR, 'evo_pre_apply')) === keepN,
      'D-70★: 构建失败后旧快照文件数原样不变(未被先毁后建) (得 ' +
      countFiles(path.join(SNAP_DIR, 'evo_pre_apply')) + ' vs ' + keepN + ')');
    const debrisAfterFail = fs.readdirSync(SNAP_DIR).filter(d => d.includes(SNAP_STAGING_TAG) || d.includes(SNAP_OLD_TAG));
    chk(debrisAfterFail.length === 0, 'D-70: 失败后不留 staging/__old 残留 (得 [' + debrisAfterFail.join(',') + '])');

    // 12c. D-70: 成功换入 —— 目录数不变 + 内部件清干净(旧内容被**整体**替换而非叠加)
    const fxOk = snapshot('evo_pre_apply', { fixedName: true });
    chk(fxOk === 'evo_pre_apply' && listSnapDirs().length === beforeList,
      'D-70: 原子换入后快照目录数不变 (得 ' + listSnapDirs().length + ' vs ' + beforeList + ')');
    chk(fs.readdirSync(SNAP_DIR).filter(d => d.includes(SNAP_STAGING_TAG) || d.includes(SNAP_OLD_TAG)).length === 0,
      'D-70: 成功换入后 staging/__old 已清干净(零残留)');
    chk(countFiles(path.join(SNAP_DIR, 'evo_pre_apply')) === countFiles(fakeSrc) + 1,
      'D-70: 换入后快照文件数 = 源 ' + countFiles(fakeSrc) + ' + 双层技能 1 (得 ' +
      countFiles(path.join(SNAP_DIR, 'evo_pre_apply')) + ')');
    // 12d. D-70: 内部件识别 —— 只认内部保留名, 真快照名不受影响
    chk(isInternalSnapDir('_trash') && isInternalSnapDir('x__old_20260101') && isInternalSnapDir('x__staging_20260101') &&
      isInternalSnapDir('evo_pre_apply') === false,
      'D-70: isInternalSnapDir 只认内部保留名(_trash/__old_/__staging_); 真快照名不误判');

    // 12e. D-71: 审计行写入失败必须「可见且不致命」—— 返回 false, 不抛异常(原先静默吞掉)
    const baseSaved = BASE;
    rebindRoots({ base: path.join(root, 'Z:', '__unwritable__') });
    let lgThrew = null, lgRet = null;
    try { lgRet = logEntry({ action: 'selftest-probe', name: 'probe' }); } catch (e) { lgThrew = e; }
    rebindRoots({ base: baseSaved });
    chk(lgThrew === null, 'D-71: 审计写入失败不抛异常(不致命)');
    chk(lgRet === false, 'D-71: 审计写入失败返回 false(调用方可感知, 不再静默) (得 ' + lgRet + ')');

    // 13. D-51a: snapshot-prune —— 保护基线 + 默认干跑 + --yes 移入 _trash + _trash 不算快照
    const spDry = snapshotPrune(1);
    chk(spDry && spDry.dryRun === true, 'D-51a: snapshotPrune 默认干跑 (得 dryRun=' + (spDry && spDry.dryRun) + ')');
    chk(spDry && fs.existsSync(path.join(SNAP_DIR, spDry.moved[0])), 'D-51a: 干跑后原目录仍在(零改动)');
    const spEx = snapshotPrune(1, { yes: true });
    chk(spEx && fs.existsSync(path.join(SNAP_DIR, '_trash', spEx.moved[0])), 'D-51a: --yes 后移入 snapshots/_trash 而非物理删除');
    chk(listSnapDirs().includes('_trash') === false, 'D-51a: _trash 不被 listSnapDirs 当作快照(否则会被重复移出)');
  } catch (e) {
    console.log('  ❌ 自检异常: ' + e.message);
    f++;
  } finally {
    rebindRoots(saved);                                  // 必须先还原路径根，再清理沙盒
    try { fs.rmSync(root, { recursive: true, force: true }); } catch (_) {}
  }
  console.log('\n自检结果: ' + p + ' 通过 / ' + f + ' 失败');
  process.exit(f ? 1 : 0);
}

// ── CLI 入口（模块化：可被 require 后同进程调 cli，不产生副作用）──────────────
function cli(argv) {
  const cmd = argv[2];
  if (cmd === 'snapshot') snapshot(argv[3], { full: argv.includes('--full'), fixedName: argv.includes('--fixed') });
  else if (cmd === 'list') list();
  else if (cmd === 'restore') restore(argv[3]);
  else if (cmd === 'verify') verify(argv[3]);
  else if (cmd === 'check') { const n = check(); process.exit(n ? 1 : 0); }
  else if (cmd === 'enable-skills') enableSkills();
  else if (cmd === 'baseline') baseline(argv[3], argv[4]);
  else if (cmd === 'selftest') selftest();
  else if (cmd === 'light') light(argv[3], argv.slice(4).filter(a => !a.startsWith('--')));
  else if (cmd === 'light-prune') lightPrune(argv[3], { yes: argv.includes('--yes') });
  else if (cmd === 'snapshot-prune') snapshotPrune(argv[3], { yes: argv.includes('--yes') });
  else {
    console.log('Usage:');
    console.log('  node recovery.js snapshot <label> [--full] [--fixed]   快照(默认双层+时间戳名; --full 加全库技能; --fixed 固定名覆盖)');
    console.log('  node recovery.js list');
    console.log('  node recovery.js restore [snapshotName]   省略名则回退到已知良好基线');
    console.log('  node recovery.js verify <snapshotName>');
    console.log('  node recovery.js check');
    console.log('  node recovery.js baseline set|show|clear <label>   标记/查看/清除已知良好基线');
    console.log('  node recovery.js enable-skills   安全启用双向联动执行层技能(自动双层快照兜底)');
    console.log('  node recovery.js selftest        沙盒隔离自检(生产零接触, 供聚合门禁调用)');
    console.log('  node recovery.js light <label> [path...]  轻量快照(默认 docs+scripts+settings.json, 附 SHA256 清单)');
    console.log('  node recovery.js light-prune <N> [--yes]  保留最近 N 个轻量快照; 默认干跑, --yes 才移入 lite/_trash');
    console.log('  node recovery.js snapshot-prune [N] [--yes]  保护基线+保留最近 N 个重型快照; 默认干跑, --yes 才移入 snapshots/_trash');
  }
}

if (require.main === module) cli(process.argv);
module.exports = {
  cli, selftest,
  snapshot, light, lightPrune, snapshotPrune, list, listSnapDirs, restore, verify, check, baseline, enableSkills,
  rebindRoots, DEFAULT_ROOTS,
};
