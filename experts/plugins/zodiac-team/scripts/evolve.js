#!/usr/bin/env node
/**
 * evolve.js — 生肖团安全自进化引擎 (guarded self-evolution)
 * 对齐: Sentinel 自进化闭环 / SEVerA 形式化守卫 FGGM / NosisTech 审批闸门 / Eigent 可编辑对象范式
 *
 * 设计铁律 (呼应 R1-R19 全部审计):
 *   1. 模型只能"提议"，本地代码"裁决" (deterministic guardrail > prompt 约束)
 *   2. 任何进化必须 rollback-safe + 应用前打 recovery 快照
 *   3. 受限域 (模型权重/跨项目/用户记忆文件) 一律阻断
 *   4. 每条提议须绑定 R18 learnings 经验 (evidence) + R17 trace_id
 *   5. (R26 / D-50) apply 必须「真落地 或 诚实降级」:
 *        - 携带结构化 patch 且通过 白名单 + CAS + 快照 → 真写盘, 状态 APPLIED
 *        - 无可执行 patch → 契约级采纳, 状态 ADOPTED (待人工/Agent 落地)
 *        - 写盘/校验失败 → 自动回滚, 状态 APPLY_FAILED
 *        严禁再用 APPLIED 谎称一次并未发生的文件改动 (D-50 语义谎言已消除)
 *   6. (R26+) 退路无条件 —— 全树快照(520MB)可跳过/失败, 但文件级回滚点(logs/rollback/, 数 KB)只要
 *        真写盘就必先建立; 建不起来就中止不写。且 `rollback` 命令必须真能还原 (有退路还要能走退路)。
 *
 * 可编辑对象白名单 (R26 契约化; 见 settings.json evolution.editableObjects, 代码内兜底):
 *   允许: settings.json(仅策略子树标量) / prompts/ policies/ routes/ 下 .json/.md/.txt
 *   阻断: scripts/(引擎源码) agents/(角色定义) skills/(skill_source) docs/ logs/ avatars/ benchmarks/
 *         以及任何绝对路径 / '..' 越权路径 / 超尺寸文件
 *
 * 命令:
 *   propose <json>   从经验提议一次进化 (护栏校验; 含 patch 合法性预检)
 *   review  <id> <approve|reject> [理由]   鸡审批闸门
 *   apply   <id>    审批通过后应用 (有 patch→真落地 / 无 patch→ADOPTED; 均打 recovery 快照兜底)
 *   rollback <id>   用文件级回滚点把 APPLIED 记录的目标文件还原 (R26+)
 *   list              列出全部提议 (标注是否携带可执行 patch)
 *   stats             演进统计 (含护栏拦截率)
 *   export            导出 JSONL
 *   selftest          自检闭环演示 (含护栏拦截 + 真实落地 + 诚实降级 + 回滚闭环)
 *   clear             清空演示数据
 *   dedupe            跨状态去重
 *
 * 环境变量 (测试隔离用):
 *   ZODIAC_EVO_LOG=<path>      重定向进化日志, 避免 e2e/隔离测试污染真实进化流
 *   ZODIAC_EVO_SKIP_SNAPSHOT=1 跳过全树快照(520MB); 文件级回滚点仍无条件建立
 */
const fs = require('fs');
const path = require('path');
// R32/D-51b: 移除 child_process 依赖 —— 全树快照改「同进程直调 recovery」, 不再需要建子进程
const crypto = require('crypto');
const BASE = path.join(__dirname, '..');  // R221r2/R8a：E-D57 防再现，禁硬编码 marketplaces 绝对路径
const SETTINGS = path.join(BASE, 'settings.json');
const EVO_LOG = process.env.ZODIAC_EVO_LOG || path.join(BASE, 'logs', 'zodiac_evolution_log.jsonl');
// R26+: 文件级回滚点目录 — 全树快照(520MB)被跳过/失败时, 仍保证每笔落地都有退路 (呼应信条「改前必留退路」)
// R27/D-58: 改为 let —— selftest 期临时重定向到系统临时目录, 使自检不产生任何"需删除"的包内文件。
//   根因: 宿主 safe-delete 批量守卫在单次删除量超阈值时【直接终止进程】→ finally 清理中断 → 残留逐轮累积
//   (实测: 单文件删除 10/10 成功; 一次删 24 个 → 守卫 EPERM 并杀进程)。生产路径不变, 仅自检隔离。
let ROLLBACK_DIR = path.join(BASE, 'logs', 'rollback');

const s = JSON.parse(fs.readFileSync(SETTINGS, 'utf8'));
const evo = s.evolution || {};
const SAFE = evo.safety || {};
const GATE = evo.approvalGate || {};
const NOW = () => new Date().toISOString();
const sha16 = (t) => crypto.createHash('sha256').update(String(t)).digest('hex').slice(0, 16);
// R27: 回滚点展示路径 — 包内用相对路径(logs/rollback/x), 包外(selftest 的 tmp 隔离)用绝对路径
const rbRelOf = (p) => { if(!p) return null; const rel = path.relative(BASE, p); return rel.startsWith('..') ? p : rel.replace(/\\/g, '/'); };

// ── 可编辑对象白名单 (契约外置 + 代码兜底, 防 settings.json 被回滚后引擎崩溃) ──────────
const EDITABLE = Object.assign({
  allowFiles: ['settings.json'],
  allowDirs: ['prompts/', 'policies/', 'routes/'],
  allowExt: ['.json', '.md', '.txt'],
  denyDirs: ['scripts/', 'agents/', 'skills/', 'docs/', 'logs/', 'avatars/', 'benchmarks/', '.codebuddy-plugin/'],
  denyReason: { 'scripts/': '引擎源码禁写', 'agents/': '角色定义禁写', 'skills/': '受限域阻断: skill_source' },
  jsonSetAllowPaths: ['routingTable', 'linkageMap', 'rules', 'policies', 'prompts', 'params'],
  requireCas: true,
  maxBytes: 262144,
}, evo.editableObjects || {});

function loadLog(p){ if(!fs.existsSync(p)) return []; return fs.readFileSync(p,'utf8').split('\n').filter(Boolean).map(l=>{try{return JSON.parse(l)}catch(e){return null}}).filter(Boolean); }
function uid(){ return 'evo_'+Date.now().toString(36)+Math.random().toString(36).slice(2,6); }
function esc(s){ return String(s).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

// ── patch 合法性校验 (确定性护栏: 本地代码裁决, 越权一律拒) ─────────────────────────
function validatePatch(patch){
  const errs = [];
  if(!patch || typeof patch !== 'object'){ return ['patch 非法: 须为对象']; }
  const f = String(patch.file || '');
  if(!f){ return ['patch.file 缺失']; }
  if(path.isAbsolute(f) || f.includes('..')){ return ['patch.file 路径越权(绝对路径/..): ' + f]; }
  const norm = f.replace(/\\/g, '/');
  const ext = path.extname(norm).toLowerCase();
  if(!EDITABLE.allowExt.includes(ext)) errs.push('patch.file 扩展名不允许: ' + ext);
  const hitDeny = EDITABLE.denyDirs.find(d => norm === d || norm.startsWith(d));
  if(hitDeny){ errs.push((EDITABLE.denyReason[hitDeny] || '禁写目录') + ': ' + norm); return errs; }
  const inAllowFile = EDITABLE.allowFiles.includes(norm);
  const inAllowDir = EDITABLE.allowDirs.some(d => norm.startsWith(d));
  if(!inAllowFile && !inAllowDir) errs.push('patch.file 不在可编辑白名单: ' + norm);
  if(patch.op === 'json-set'){
    if(!patch.path) errs.push('json-set 需 patch.path');
    else {
      const root = String(patch.path).split('.')[0];
      if(!EDITABLE.jsonSetAllowPaths.includes(root)) errs.push('json-set 路径不在策略子树: ' + root);
    }
    if(!('to' in patch)) errs.push('json-set 需 patch.to');
    if(patch.from === undefined && EDITABLE.requireCas) errs.push('json-set 需 patch.from (CAS 旧值, 防并发覆写)');
  } else if(patch.op === 'text-replace'){
    if(typeof patch.find !== 'string' || !patch.find) errs.push('text-replace 需 patch.find');
    if(typeof patch.replace !== 'string') errs.push('text-replace 需 patch.replace');
    if(patch.expectCount !== undefined && (!Number.isInteger(patch.expectCount) || patch.expectCount < 1)) errs.push('patch.expectCount 须为正整数');
  } else {
    errs.push('patch.op 不支持: ' + (patch.op || '(空)') + ' (仅 json-set / text-replace)');
  }
  return errs;
}

function getByPath(o, p){ return p.split('.').reduce((a, k) => (a == null ? undefined : a[k]), o); }

// JSON 标量最小替换: 只改 "key": <标量> 的值部分, 不重排整文件 (避免 JSON.stringify 破坏原格式/内联数组)
function jsonScalarSetText(raw, keyPath, from, to){
  const key = String(keyPath).split('.').pop();
  const re = new RegExp('("' + esc(key) + '"\\s*:\\s*)(?:"(?:[^"\\\\]|\\\\.)*"|-?\\d+(?:\\.\\d+)?|true|false|null)');
  const hits = raw.match(new RegExp(re.source, 'g'));
  if(!hits || hits.length !== 1) return { ok:false, err:'json-set 定位失败: key "' + key + '" 匹配数 ' + (hits ? hits.length : 0) + ' (需唯一)' };
  let obj;
  try { obj = JSON.parse(raw); } catch (e) { return { ok:false, err:'目标非合法 JSON: ' + e.message }; }
  const cur = getByPath(obj, keyPath);
  if(EDITABLE.requireCas && from !== undefined && JSON.stringify(cur) !== JSON.stringify(from)){
    return { ok:false, err:'CAS 失配: 现值 ' + JSON.stringify(cur) + ' ≠ 期望 ' + JSON.stringify(from) };
  }
  const newTxt = JSON.stringify(to);
  return { ok:true, text: raw.replace(re, (m, p1) => p1 + newTxt), casOld: cur };
}

// 干跑: 在内存中验证 patch 能否落地, 返回 apply() 以产出新内容 (绝不写盘)
function dryRunPatch(patch){
  const verrs = validatePatch(patch);
  if(verrs.length) return { ok:false, err:'patch 校验失败: ' + verrs.join('; ') };
  const abs = path.join(BASE, patch.file.replace(/\\/g, '/'));
  if(!fs.existsSync(abs)) return { ok:false, err:'目标文件不存在: ' + patch.file };
  const raw = fs.readFileSync(abs, 'utf8');
  if(raw.length > EDITABLE.maxBytes) return { ok:false, err:'目标文件超最大可编辑尺寸 (' + raw.length + ' > ' + EDITABLE.maxBytes + ')' };
  if(patch.op === 'json-set'){
    const r = jsonScalarSetText(raw, patch.path, patch.from, patch.to);
    if(!r.ok) return r;
    return { ok:true, abs, raw, kind:patch.op, apply:() => r.text };
  }
  const n = raw.split(patch.find).length - 1;
  if(n === 0) return { ok:false, err:'text-replace 未匹配到 find 文本' };
  if(patch.expectCount !== undefined && n !== patch.expectCount) return { ok:false, err:'text-replace 匹配数 ' + n + ' ≠ 期望 ' + patch.expectCount };
  const next = raw.split(patch.find).join(patch.replace);
  if(next.length > EDITABLE.maxBytes) return { ok:false, err:'替换后超最大可编辑尺寸' };
  return { ok:true, abs, raw, kind:patch.op, apply:() => next };
}

// 确定性护栏校验 (本地代码裁决，模型只提议)
function validate(prop){
  const errs=[];
  if(!SAFE.requireRollbackSafe || !prop.rollback_safe) errs.push('非 rollback-safe: 进化必须可回滚');
  if(SAFE.blockedScopes && SAFE.blockedScopes.includes(prop.scope)) errs.push('受限域阻断: '+prop.scope);
  if(!evo.whatCanEvolve || !evo.whatCanEvolve.includes(prop.target_type)) errs.push('不可进化目标: '+prop.target_type+' (仅限 '+evo.whatCanEvolve.join('/')+')');
  if((prop.confidence||0) < (SAFE.minConfidence||0.7)) errs.push('置信度不足: '+(prop.confidence||0)+' < '+(SAFE.minConfidence||0.7));
  if((prop.evidence_count||0) < (SAFE.minEvidenceCount||2)) errs.push('证据不足: '+(prop.evidence_count||0)+' < '+(SAFE.minEvidenceCount||2));
  if(!prop.learning_ids || !prop.learning_ids.length) errs.push('未绑定 R18 经验: 须引用 learnings 经验 id');
  if(!prop.trace_id) errs.push('未绑定 R17 trace_id');
  // R26: patch 在提议期即预检 — 白名单/op 静态校验必跑; 目标已存在时追加干跑(JSON/CAS/匹配数)早暴露
  //      (目标文件尚不存在 = 新建资产, 允许, 预检留到 apply 期)
  if(prop.patch){
    const verrs = validatePatch(prop.patch);
    verrs.forEach(e => errs.push(e));
    if(!verrs.length){
      const pabs = path.join(BASE, String(prop.patch.file).replace(/\\/g, '/'));
      if(fs.existsSync(pabs)){
        const d = dryRunPatch(prop.patch);
        if(!d.ok) errs.push('patch 干跑预检失败: ' + d.err);
      }
    }
  }
  return errs;
}

function propose(prop){
  const errs = validate(prop);
  const status = errs.length? 'BLOCKED':'PROPOSED';
  const logs = loadLog(EVO_LOG);
  // 幂等-1: 同意图已审批/否决/应用/采纳/回滚(终态) → 忽略重提, 防噪声 (R19 演进策略: 合并/降级/检索, 防记忆库膨胀成噪声)
  //   注: ROLLED_BACK / ROLLBACK_FAILED 亦属终态决策 — 意图已被完整走完一轮, 重提即为噪声;
  //       若确需再试, 应携带新证据/新上下文形成不同的 proposed_change (可追溯性优于重复条目)。
  //   APPLY_FAILED 刻意**不**列入: 写盘受阻属可重试的瞬时失败, 允许重提。
  const TERMINAL = ['APPROVED','REJECTED','APPLIED','ADOPTED','ROLLED_BACK','ROLLBACK_FAILED'];
  const decided = logs.find(x=> x.target===prop.target && x.proposed_change===prop.proposed_change && TERMINAL.includes(x.status));
  if(decided){
    // 已决策意图被重提: 不新增条目(防噪声), 但记录本次触发(observability 幂等追踪)
    decided.trace_ids = Array.from(new Set([...(decided.trace_ids||[decided.trace_id].filter(Boolean)), ...(prop.trace_id?[prop.trace_id]:[])]));
    decided.learning_ids = Array.from(new Set([...(decided.learning_ids||[]), ...(prop.learning_ids||[])]));
    decided.recount = (decided.recount||1)+1;
    decided.last_retried = NOW();
    fs.mkdirSync(path.dirname(EVO_LOG),{recursive:true});
    fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
    console.log('⏭️ 忽略重提 ['+decided.id+'] 已'+decided.status+', 已记录本次触发: '+prop.target_type+'@'+prop.target);
    return decided;
  }
  // 幂等-2: 相同 PROPOSED/BLOCKED 同意图合并而非重复追加
  const dup = logs.find(x=> x.target===prop.target && x.proposed_change===prop.proposed_change && (x.status==='PROPOSED'||x.status==='BLOCKED'));
  if(dup){
    const mergedLearning = Array.from(new Set([...(dup.learning_ids||[]), ...(prop.learning_ids||[])]));
    const mergedTraces = Array.from(new Set([...(dup.trace_ids||[dup.trace_id].filter(Boolean)), ...(prop.trace_id?[prop.trace_id]:[])]));
    dup.learning_ids = mergedLearning;
    dup.trace_ids = mergedTraces;
    dup.trace_id = prop.trace_id || dup.trace_id;
    dup.evidence_count = Math.max(dup.evidence_count||0, prop.evidence_count||0);
    dup.recount = (dup.recount||1)+1;
    dup.ts = NOW();
    dup.status = status;
    dup.errors = errs;
    if(prop.patch) dup.patch = prop.patch;
    fs.mkdirSync(path.dirname(EVO_LOG),{recursive:true});
    fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
    console.log('🔄 合并重复提议 ['+dup.id+'] (第'+dup.recount+'次): '+prop.target_type+'@'+prop.target);
    return dup;
  }
  const id = uid();
  const rec = {id, ts:NOW(), status, errors:errs, recount:1, ...prop};
  fs.mkdirSync(path.dirname(EVO_LOG),{recursive:true});
  fs.appendFileSync(EVO_LOG, JSON.stringify(rec)+'\n');
  if(errs.length){ console.log('🚫 护栏拦截 ['+id+']:'); errs.forEach(e=>console.log('   - '+e)); }
  else console.log('✅ 提议通过护栏 ['+id+']: '+prop.target_type+'@'+prop.target+(prop.patch?'  [含可执行 patch: '+prop.patch.op+'@'+prop.patch.file+']':'  [无 patch → 应用时降级为 ADOPTED]'));
  return rec;
}

function review(id, decision, reason){
  const logs = loadLog(EVO_LOG);
  const r = logs.find(x=>x.id===id);
  if(!r){ console.log('未找到提议 '+id); return; }
  if(r.status!=='PROPOSED'){ console.log('提议状态不可审批: '+r.status); return; }
  r.status = decision==='approve' ? 'APPROVED' : 'REJECTED';
  r.review = {by: GATE.reviewer, decision, reason: reason||'', ts:NOW()};
  fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
  console.log((decision==='approve'?'✅ 鸡审批通过':'🚫 鸡否决')+' ['+id+']'+(reason?' 理由: '+reason:''));
}

// ── 文件级回滚点 (R26+) ────────────────────────────────────────────────────────
// 与全树 recovery 快照互补: 快照可能被跳过/失败/过大, 而单文件退路仅数 KB, 必须无条件建立
function rbName(id, relFile){
  const safe = relFile.replace(/[\\/]/g, '__').replace(/[^A-Za-z0-9_.\-]/g, '_');
  return id + '__' + safe;
}
// R27/D-58b: nameId 可选覆盖文件名中的 id —— 自检传固定值, 使回滚点文件名恒定(重复覆盖, 零累积);
//   生产不传则用真实 id, 行为不变。
function saveRollbackPoint(id, relFile, content, nameId){
  fs.mkdirSync(ROLLBACK_DIR, { recursive: true });
  const f = path.join(ROLLBACK_DIR, rbName(nameId || id, relFile));
  // 同时留一份元数据, 便于 rollback 命令还原到正确路径
  fs.writeFileSync(f, content);
  fs.writeFileSync(f + '.meta.json', JSON.stringify({
    id, file: relFile, ts: NOW(), sha: sha16(content), bytes: content.length,
  }, null, 2));
  return f;
}

// R26: apply 双轨 — 有 patch 真落地 / 无 patch 诚实降级为 ADOPTED (D-50 语义谎言消除)
function apply(id, opts){
  opts = opts || {};
  const logs = loadLog(EVO_LOG);
  const r = logs.find(x=>x.id===id);
  if(!r){ console.log('未找到提议 '+id); return; }
  if(r.status!=='APPROVED'){ console.log('须先经鸡审批通过才能应用 (当前 '+r.status+')'); return; }

  // ① 写盘前干跑校验 (越权/失配/不匹配 一律拦在写盘之前)
  let run = null;
  if(r.patch){
    run = dryRunPatch(r.patch);
    if(!run.ok){
      r.status='APPLY_FAILED';
      r.apply_error={ ts:NOW(), reason:run.err, rolled_back:true };
      fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
      console.log('🚫 落地中止(未写盘) ['+id+']: '+run.err);
      return;
    }
  }

  // ② 兜底双保险: ①文件级回滚点(无条件, 数 KB 必成) + ②全树 recovery 快照(可选)
  // D-51b(R32): 快照名由 `evo_<uid>` 改为**固定名** —— uid 名每轮新增一个目录(实测累积 5 个 ≈12GB 物理);
  //   固定名 + recovery 覆盖前清空 ⇒ 累积恒为 1 个。可用 opts.snapName 覆写。
  const snapName = opts.snapName || 'evo_pre_apply';
  let snapOk = false, realName = snapName, rbPath = null;
  const before = run ? fs.readFileSync(run.abs, 'utf8') : null;
  if(run){
    // 只要是"真落地", 先无条件留退路 — 不留退路就不写盘 (信条「改前必留退路」)
    try {
      rbPath = saveRollbackPoint(id, r.patch.file, before, opts.rbNameId);
      console.log('💾 文件级回滚点: logs/rollback/' + rbName(id, r.patch.file) + '  (sha=' + sha16(before) + ')');
    } catch (e) {
      console.log('🚫 无法建立文件级回滚点, 已中止(不留退路不写盘): ' + e.message);
      return;
    }
  }
  if(opts.skipSnapshot){
    console.log('📸 全树快照(跳过: selftest 模式, 避免全树快照拖慢回归)');
  } else {
    try {
      // D-51b(R32): 同进程直调 recovery(其已模块化) —— 原 execFileSync 依赖 node 建子进程, 受限宿主恒 EBUSY
      const recoveryMod = require(path.join(__dirname, 'recovery.js'));
      realName = recoveryMod.snapshot(snapName, { fixedName: true }) || snapName;
      console.log('📸 全树快照(真): ' + snapName + ' -> ' + realName);
      snapOk = true;
    } catch (e) { console.log('⚠️ 全树快照失败(文件级回滚点仍在, 不影响可回滚性): ' + e.message); }
  }

  // ③ 落地 or 降级
  if(run){
    try {
      const next = run.apply();
      fs.writeFileSync(run.abs, next);
      const back = fs.readFileSync(run.abs, 'utf8');
      if(back !== next) throw new Error('回读不一致(写入被篡改或拦截)');
      r.status='APPLIED';
      const _rbDisp = rbRelOf(rbPath);
      r.applied={ ts: NOW(), mode:'patched', file:r.patch.file, op:r.patch.op,
        before_sha: sha16(before), after_sha: sha16(next), bytes_delta: next.length - before.length,
        snapshot: realName, snapshotLabel: snapName, snapshotReal: snapOk,
        rollbackPoint: _rbDisp,
        rollbackCmd: 'node evolve.js rollback ' + id,
        note: '真实落地: '+r.patch.file+' ('+r.patch.op+') ; 回滚点 '+_rbDisp
              +(snapOk?' + 全树快照 '+realName:' (全树快照已跳过/失败, 文件级回滚点可用)') };
      fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
      console.log('✅ 已真实落地 ['+id+'] -> '+r.patch.file+' ['+r.patch.op+'] '+
        (r.applied.bytes_delta>=0?'+':'')+r.applied.bytes_delta+'B  (回滚: node evolve.js rollback '+id+')');
      return;
    } catch (e) {
      let rolled = false;
      try { fs.writeFileSync(run.abs, before); rolled = (fs.readFileSync(run.abs,'utf8')===before); } catch(_){}
      r.status='APPLY_FAILED';
      r.apply_error={ ts:NOW(), reason:'写入/校验失败: '+e.message, rolled_back:rolled,
        rollbackPoint: rbPath ? rbRelOf(rbPath) : null };
      fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
      console.log('🚫 落地失败'+(rolled?'已回滚':'⚠️ 回滚失败(可用回滚点恢复: node evolve.js rollback '+id+')')+' ['+id+']: '+e.message);
      return;
    }
  }
  // 无 patch: 诚实降级 — 契约级采纳, 落地待人工/Agent
  r.status='ADOPTED';
  r.adopted={ ts:NOW(), snapshot: realName, snapshotLabel: snapName, snapshotReal: snapOk,
    note: '契约级采纳(未改任何文件): 本提议无机器可执行 patch, 落地须由人工/Agent 按其 proposed_change 执行 '+
          '(对齐 whenToEvolve: gated, never intra-task auto-apply)' };
  fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
  console.log('📝 已采纳(契约级, 未落地) ['+id+'] -> '+snapName+(snapOk?' (全树快照已建立)':' (未打全树快照; 无文件改动, 无需回滚点)'));
}

// R26+: 回滚 — 用文件级回滚点把目标文件还原到 apply 之前 (有退路, 还要能走退路)
function rollback(id){
  const logs = loadLog(EVO_LOG);
  const r = logs.find(x=>x.id===id);
  if(!r){ console.log('未找到提议 '+id); return; }
  if(r.status!=='APPLIED'){ console.log('仅 APPLIED 记录可回滚 (当前 '+r.status+')'); return; }
  const rel = (r.applied && r.applied.file) || (r.patch && r.patch.file);
  if(!rel){ console.log('记录缺 file 信息, 无法回滚'); return; }
  // R27: 优先用记录的回滚点路径(兼容 selftest 的 tmp 隔离), 回退到按 id 重算
  const _rp = r.applied && r.applied.rollbackPoint;
  const rb = _rp ? (path.isAbsolute(_rp) ? _rp : path.join(BASE, _rp))
                 : path.join(ROLLBACK_DIR, rbName(id, rel));
  if(!fs.existsSync(rb)){
    console.log('回滚点不存在: '+(rbRelOf(rb) || rbName(id,rel))+' (可能未建立或已清理)'); return;
  }
  const original = fs.readFileSync(rb, 'utf8');
  const abs = path.join(BASE, rel);
  const cur = fs.existsSync(abs) ? fs.readFileSync(abs, 'utf8') : null;
  if(cur === original){ console.log('ℹ️ 目标文件已与回滚点一致, 无需回滚 ['+id+']'); return; }
  const meta = path.join(rb + '.meta.json');
  if(fs.existsSync(meta)){
    try {
      const m = JSON.parse(fs.readFileSync(meta, 'utf8'));
      if(m.sha !== sha16(original)) console.log('⚠️ 回滚点 sha 与元数据不符, 仍按回滚点内容恢复');
    } catch(_){}
  }
  fs.writeFileSync(abs, original);
  const okr = (fs.readFileSync(abs, 'utf8') === original);
  r.status = okr ? 'ROLLED_BACK' : 'ROLLBACK_FAILED';
  r.rollback = { ts: NOW(), file: rel, restored_sha: sha16(original),
    prev_sha: cur ? sha16(cur) : null, ok: okr };
  fs.writeFileSync(EVO_LOG, logs.map(l=>JSON.stringify(l)).join('\n')+'\n');
  console.log((okr?'↩️ 已回滚':'🚫 回滚校验失败')+' ['+id+'] -> '+rel+' (恢复 sha='+sha16(original)+')');
}

function list(){
  const logs=loadLog(EVO_LOG);
  if(!logs.length){ console.log('(无进化提议)'); return; }
  console.log('=== 进化提议 ('+logs.length+') ===');
  logs.forEach(r=>{
    const tag = r.patch ? ('patch:'+r.patch.op+'@'+r.patch.file) : '无patch(契约级)';
    console.log(`[${r.status}] ${r.id} ${r.target_type}@${r.target} conf=${r.confidence} ev=${r.evidence_count} ${tag}`);
  });
}
function stats(){
  const logs=loadLog(EVO_LOG);
  const by={PROPOSED:0,BLOCKED:0,APPROVED:0,REJECTED:0,APPLIED:0,ADOPTED:0,APPLY_FAILED:0,ROLLED_BACK:0,ROLLBACK_FAILED:0};
  logs.forEach(r=>by[r.status]=(by[r.status]||0)+1);
  console.log('=== 演进统计 ==='); Object.keys(by).forEach(k=>console.log(`  ${k}: ${by[k]}`));
  console.log('  护栏拦截率: '+(logs.length? (by.BLOCKED/logs.length*100).toFixed(1)+'%':'0%'));
  console.log('  真实落地率: '+(logs.length? (by.APPLIED/logs.length*100).toFixed(1)+'%':'0%'));
}
function exportJson(){ console.log(JSON.stringify(loadLog(EVO_LOG),null,2)); }

function selftest(){
  // 受控验证: 备份真实 EVO_LOG, 演示后 try/finally 还原, 避免 demo 条目污染真实进化流 (R19 完整性)
  const _bk = fs.existsSync(EVO_LOG) ? fs.readFileSync(EVO_LOG, 'utf8') : '';
  // R27/D-58: 回滚点隔离到系统临时目录 —— 自检不产生任何"需删除"的包内文件,
  //   从源头规避 safe-delete 批量守卫(单次删除超阈值会直接终止进程 → finally 中断 → 残留逐轮累积)。
  const _rbOrig = ROLLBACK_DIR;
  ROLLBACK_DIR = path.join(require('os').tmpdir(), 'zodiac_evo_rb_selftest');
  const PROMPTS = path.join(BASE, 'prompts');
  const TF = path.join(PROMPTS, '_selftest_evolve.txt');
  const TFJ = path.join(PROMPTS, '_selftest_evolve.json');
  const hadDir = fs.existsSync(PROMPTS);
  let pass = 0, fail = 0;
  let _stray = [];   // R33/D-72: 包内夹具残留登记(清理失败时非空)
  const ok = (cond, label) => { if(cond){ console.log('✅ '+label); pass++; } else { console.log('❌ '+label); fail++; } };
  try {
    fs.writeFileSync(EVO_LOG, ''); // 演示须在空库上跑: 否则幂等-1 会命中历史决策、[5] 会误取真实待审记录 (同 D-55 假绿根源)
    console.log('=== evolve.js 自检: 安全自进化闭环 (模型提议 / 本地代码裁决) ===\n');
    console.log('[1] 合法提议 (R18经验驱动, prompt-only, rollback-safe)');
    propose({target_type:'prompt', scope:'intra_package', target:'goat-ai-image-generator', proposed_change:'在生图 prompt 头部加 cobalt-blue 锚以抑制全灰', confidence:0.86, evidence_count:3, learning_ids:['L1','L2'], trace_id:'trace-selftest-1', rollback_safe:true, author:'monkey'});
    console.log('\n[2] 受限域阻断 (model_weights — 确定性护栏)');
    propose({target_type:'model_weights', scope:'model_weights', target:'SDXL', proposed_change:'fine-tune base model', confidence:0.9, evidence_count:5, learning_ids:['L1'], trace_id:'trace-selftest-2', rollback_safe:true, author:'monkey'});
    console.log('\n[3] 护栏阻断 (证据不足 + 非 rollback-safe)');
    propose({target_type:'param', scope:'intra_package', target:'ksampler.cfg', proposed_change:'auto-tune cfg', confidence:0.5, evidence_count:1, learning_ids:[], trace_id:'trace-selftest-3', rollback_safe:false, author:'monkey'});
    console.log('\n[4] 越权 patch 在提议期即被拦 (D-50 回归: 引擎源码不可写)');
    const bad = propose({target_type:'policy', scope:'intra_package', target:'zodiac-team/scripts', proposed_change:'直接改引擎源码绕过护栏', patch:{file:'scripts/evolve.js', op:'text-replace', find:'x', replace:'y'}, confidence:0.9, evidence_count:3, learning_ids:['L1'], trace_id:'trace-selftest-4', rollback_safe:true, author:'monkey'});
    ok(bad.status==='BLOCKED', 'D-50 回归: scripts/ 越权 patch 被拦 (status='+bad.status+')');

    console.log('\n[5] 无 patch 提议 → apply 应诚实降级为 ADOPTED (D-50 语义回归)');
    const okp = loadLog(EVO_LOG).find(r=>r.status==='PROPOSED' && !r.patch);
    if(okp){ review(okp.id,'approve','经验充分且 prompt-only 低风险'); apply(okp.id,{skipSnapshot:true}); }
    const adopted = loadLog(EVO_LOG).find(r=>r.id===(okp&&okp.id));
    ok(!!adopted && adopted.status==='ADOPTED', 'D-50 回归: 无 patch 提议降级为 ADOPTED, 不再谎称 APPLIED');

    console.log('\n[6] 携带 patch 提议 → apply 应真实落地 (D-50 修复实证)');
    fs.mkdirSync(PROMPTS,{recursive:true});
    fs.writeFileSync(TF, 'controlnet_strength: 0.45\ncfg: 7.0\n');
    const pp = propose({target_type:'param', scope:'intra_package', target:'zheng10-ai-image-generator',
      proposed_change:'ControlNet 强度 0.45→0.65 (selftest 真实落地演示)',
      patch:{file:'prompts/_selftest_evolve.txt', op:'text-replace', find:'0.45', replace:'0.65', expectCount:1},
      confidence:0.88, evidence_count:3, learning_ids:['L1','L2'], trace_id:'trace-selftest-6', rollback_safe:true, author:'monkey'});
    review(pp.id,'approve','参数修正可回滚');
    apply(pp.id,{skipSnapshot:true, rbNameId:'selftest'});   // D-58b: 固定回滚点名 → 重复覆盖, 零累积
    const after = fs.readFileSync(TF,'utf8');
    ok(after.includes('0.65') && !after.includes('0.45'), 'D-50 回归: patch 真实写盘 (0.45 → 0.65)');
    const rec6 = loadLog(EVO_LOG).find(r=>r.id===pp.id);
    ok(!!rec6 && rec6.status==='APPLIED' && rec6.applied && rec6.applied.before_sha!==rec6.applied.after_sha, 'D-50 回归: 状态 APPLIED 且留存 before/after SHA 证据');

    console.log('\n[6b] 回滚闭环: 文件级回滚点必建 (即使全树快照被跳过) + rollback 真能还原');
    const _rp6 = rec6 && rec6.applied && rec6.applied.rollbackPoint;
    ok(!!_rp6 && fs.existsSync(path.isAbsolute(_rp6) ? _rp6 : path.join(BASE, _rp6)),
       'R26+ 回归: 跳过全树快照时仍无条件建立文件级回滚点 (生产 logs/rollback/… ; 自检 tmp 隔离)');
    rollback(pp.id);
    const restored = fs.readFileSync(TF, 'utf8');
    ok(restored.includes('0.45') && !restored.includes('0.65'), 'R26+ 回归: rollback 真还原到 apply 前内容 (0.65 → 0.45)');
    const rec6b = loadLog(EVO_LOG).find(r=>r.id===pp.id);
    ok(!!rec6b && rec6b.status==='ROLLED_BACK' && rec6b.rollback && rec6b.rollback.ok === true,
       'R26+ 回归: 状态置 ROLLED_BACK 且留回滚审计 (restored_sha/prev_sha)');

    console.log('\n[7] 提议期干跑预检应拦下不可落地 patch (非 JSON 目标 / CAS 失配)');
    fs.writeFileSync(TF, 'cfg: 7.0\n');                                    // YAML 文本 → json-set 无从下手
    const bad2 = propose({target_type:'param', scope:'intra_package', target:'zheng10-ai-image-generator',
      proposed_change:'CFG 7.0→9.0 (目标非 JSON 文本回归)',
      patch:{file:'prompts/_selftest_evolve.txt', op:'json-set', path:'params.cfg', from:7.0, to:9.0},
      confidence:0.9, evidence_count:3, learning_ids:['L1'], trace_id:'trace-selftest-7', rollback_safe:true, author:'monkey'});
    fs.writeFileSync(TFJ, '{\n  "params": {\n    "cfg": 7.0\n  }\n}\n');  // 合法 JSON, 现值 7.0
    const bad3 = propose({target_type:'route', scope:'intra_package', target:'zodiac-team/prompts',
      proposed_change:'CAS 失配回归: 声明旧值 8.0 而实际 7.0, 应拦在写盘前',
      patch:{file:'prompts/_selftest_evolve.json', op:'json-set', path:'params.cfg', from:8.0, to:9.0},
      confidence:0.9, evidence_count:3, learning_ids:['L1'], trace_id:'trace-selftest-7b', rollback_safe:true, author:'monkey'});
    ok(bad2.status==='BLOCKED', 'D-50 回归: 目标非 JSON → json-set 提议期被拦 (key 无法唯一锚定)');
    ok(bad3.status==='BLOCKED' && bad3.errors.some(e=>e.includes('CAS 失配')),
       'D-50 回归: CAS 失配 (申报旧值 8.0 ≠ 实际 7.0) 提议期被拦 — 防并发覆写');

    console.log('\n[8] 统计 (含 真实落地/契约级采纳/失败 三态)');
    stats();
  } finally {
    // R27/D-58: 回滚点已隔离在 tmp → 无需删除任何回滚点文件, 包内删除量恒为 TF/TFJ 共 2 个 (远低于守卫阈值)
    ROLLBACK_DIR = _rbOrig;   // 还原生产回滚点目录
    // R33/D-72: 清理失败**必须可见** —— 原 `catch(_){}` 把「包内残留」完全吞掉。
    //   夹具只能落在 BASE 内(validatePatch 明确拒绝绝对路径与 '..' —— 那是 D-50 越权守卫,
    //   为省事放宽它才是真错误), 故删除通道一旦不可用(宿主 safe-delete 故障),
    //   `_selftest_evolve.*` 会**静默留在生产包体内**并被后续快照收录 —— 而自检对外宣称"包内零残留"。
    //   对策: 残留即告警(stderr, 不污染 stdout 契约) + 计入自检结论文本;
    //   **不**改 exit code —— 环境不可达与代码失败必须分态(D-60), 否则门禁会被环境噪声染红。
    try { if(fs.existsSync(TF)) fs.unlinkSync(TF); } catch(_){}
    try { if(fs.existsSync(TFJ)) fs.unlinkSync(TFJ); } catch(_){}
    if(fs.existsSync(TF)) _stray.push('prompts/_selftest_evolve.txt');
    if(fs.existsSync(TFJ)) _stray.push('prompts/_selftest_evolve.json');
    try { if(!hadDir && fs.existsSync(PROMPTS) && !fs.readdirSync(PROMPTS).length) fs.rmdirSync(PROMPTS); } catch(_){}
    if(_stray.length){
      console.error('[WARN][evolve.selftest] 包内夹具残留未能清除(删除通道不可用): ' + _stray.join(', ') +
        ' | 请手动清理, 否则会被后续快照收录');
    }
    // R27/D-58: 清理本次自检在 tmp 隔离区留下的回滚点 —— tmp 不在受管目录内, 不受 safe-delete 批量守卫约束
    //   (实测 tmpdir unlink 20/20 稳定), 故此处可安全清理, 实现「包内 + tmp」双零残留。
    try {
      const _rbTmp = path.join(require('os').tmpdir(), 'zodiac_evo_rb_selftest');
      if (fs.existsSync(_rbTmp)) {
        for (const f of fs.readdirSync(_rbTmp)) {
          if (f.includes('_selftest_evolve')) { try { fs.unlinkSync(path.join(_rbTmp, f)); } catch(_){} }
        }
        if (!fs.readdirSync(_rbTmp).length) try { fs.rmdirSync(_rbTmp); } catch(_){}
      }
    } catch(_){}
    fs.writeFileSync(EVO_LOG, _bk); // 无论演示是否抛错, 真实进化流必还原
  }
  console.log('\n自检结果: '+pass+' 通过 / '+fail+' 失败 — 印证「local code decides, model only proposes」+「apply 真落地或诚实降级」+「退路无条件且可走」。真实 EVO_LOG 与临时文件已还原(无演示污染)。' +
    (_stray.length ? ' ⚠包内夹具残留 '+_stray.length+' 项未清除: '+_stray.join(', ') : ' 包内零残留 ✅'));
  if(fail) process.exitCode = 1;
}
function clear(){ if(fs.existsSync(EVO_LOG)) fs.writeFileSync(EVO_LOG,''); console.log('已清空进化演示数据'); }
function dedupe(){
  // 跨状态去重: 每个 (target, proposed_change) 仅保留一条最强决策记录, 合并审计字段, 防日志膨胀成噪声
  // 优先级 ROLLBACK_FAILED>ROLLED_BACK>APPLIED>ADOPTED>APPLY_FAILED=APPROVED>REJECTED>BLOCKED>PROPOSED;
  //   终态(回滚/失败)必须压过 PROPOSED — 否则去重会把"已回滚"的真相丢掉、留下一条待审噪声 (R26+ 修正)
  const logs = loadLog(EVO_LOG);
  const PRIORITY = {ROLLBACK_FAILED:8, ROLLED_BACK:7, APPLIED:6, ADOPTED:5, APPLY_FAILED:4, APPROVED:4, REJECTED:3, BLOCKED:2, PROPOSED:1};
  const groups = new Map();
  for(const r of logs){ const key=r.target+'|'+r.proposed_change; if(!groups.has(key)) groups.set(key,[]); groups.get(key).push(r); }
  const out=[]; let merged=0, dropped=0;
  for(const [, recs] of groups){
    if(recs.length===1){ out.push(recs[0]); continue; }
    const canon = recs.slice().sort((a,b)=>{ const pa=PRIORITY[a.status]||0, pb=PRIORITY[b.status]||0; if(pa!==pb) return pb-pa; return (a.ts||'').localeCompare(b.ts||''); })[0];
    for(const r of recs){ if(r===canon) continue;
      canon.learning_ids = Array.from(new Set([...(canon.learning_ids||[]), ...(r.learning_ids||[])]));
      canon.trace_ids = Array.from(new Set([...(canon.trace_ids||[canon.trace_id].filter(Boolean)), ...(r.trace_ids||[r.trace_id].filter(Boolean))]));
      canon.evidence_count = Math.max(canon.evidence_count||0, r.evidence_count||0);
      canon.recount = (canon.recount||1)+(r.recount||1);
      dropped++;
    }
    merged++; out.push(canon);
  }
  fs.writeFileSync(EVO_LOG, out.map(l=>JSON.stringify(l)).join('\n')+'\n');
  console.log('✅ 去重完成: '+merged+' 组意图合并, 丢弃 '+dropped+' 条重复, 现存 '+out.length+' 条 (每组意图仅留最强决策+合并审计)。');
}

// D-61(R28): 模块化(同 trace.js) —— runtime 可在同进程内直调, 规避受限宿主 EBUSY。逻辑零改动。
function cli(argv) {
  const cmd = argv[2];
  const arg = argv[3];
  if(cmd==='propose'){ try{ propose(JSON.parse(arg)); }catch(e){ console.log('propose 需合法 JSON: '+e.message); } }
  else if(cmd==='review'){ review(argv[3], argv[4], argv[5]); }
  else if(cmd==='apply'){ apply(arg, { skipSnapshot: process.env.ZODIAC_EVO_SKIP_SNAPSHOT==='1' }); }
  else if(cmd==='rollback'){ rollback(arg); }
  else if(cmd==='list'){ list(); }
  else if(cmd==='stats'){ stats(); }
  else if(cmd==='export'){ exportJson(); }
  else if(cmd==='selftest'){ selftest(); }
  else if(cmd==='clear'){ clear(); }
  else if(cmd==='dedupe'){ dedupe(); }
  else { console.log('用法: node evolve.js <propose|review|apply|rollback|list|stats|export|selftest|clear|dedupe>'); }
}

if (require.main === module) cli(process.argv);
module.exports = { cli, propose };
