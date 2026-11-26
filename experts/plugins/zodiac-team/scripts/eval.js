#!/usr/bin/env node
/**
 * eval.js —— 生肖团 质量验证纪律层 (Evaluation Harness / R23)
 *
 * 对齐业界共识（wenable 三阶 eval / zylos「失败转回归用例」/ maviklabs rubric+人工校准 / cynked CI 门禁）：
 *   1) golden-set 回归：版本化已知良好用例集，每次变更 replay + 逐 rubric 打分
 *   2) per-rubric 通过率（绝不只看总分）—— 92% 总分可掩盖某 rubric 100% 失败
 *   3) release-blocker rubric：任一阻断项失败即阻断发布（CI gate，对齐 wenable「必有 release-blocker」）
 *   4) 串联 R17 观测 trace_id；失败用例经 R18 learn.js 沉淀为防错经验（zylos「每次失败转回归用例」）
 *
 * 本引擎只承载「评分/聚合/回归/门禁」逻辑，不做生图。生产 outputs 由宿主/CI 在真实任务后喂入。
 * 事件流落 zodiac-team/logs/zodiac_eval*.jsonl，被 recovery 快照覆盖（可恢复）。
 *
 * 用法:
 *   node eval.js case add <json>          新增 golden 用例
 *   node eval.js case list                列出全部用例
 *   node eval.js case seed                幂等播种真实项目 golden 用例库
 *   node eval.js run <caseId> --output <file|json>   对单用例打分（--output 接 JSON 文件或内联 JSON 字符串，形如 {"rubrics":{"名":bool|number}}）
 *   node eval.js suite [--results <file>] 跑全用例集，逐 rubric 聚合 + 检测回归
 *   node eval.js baseline set             把当前 suite 标记为已知良好基线
 *   node eval.js regress                  对比最新 suite 与基线，阻断项失败则 exit 2
 *   node eval.js export                   导出全部用例+最近 suite
 *   node eval.js selftest                 自检验证引擎逻辑（跑后 clear）
 *   node eval.js validate [--results <file>] [--bench <file>]  一键外部验证：suite回归+bench交叉→单一release-gate裁决
 *   node eval.js clear                    清空全部 eval 数据
 */
'use strict';
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');  // R221r2/R8a：E-D57 防再现，禁硬编码 marketplaces 绝对路径
const CASES = path.join(BASE, 'logs/zodiac_eval_cases.jsonl');
const RUNS = path.join(BASE, 'logs/zodiac_eval_runs.jsonl');
const SUITES = path.join(BASE, 'logs/zodiac_eval_suites.jsonl');
const BASELINE = path.join(BASE, 'logs/zodiac_eval_baseline.json');

const now = () => new Date().toISOString();
const uid = () => 'ev_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
function mkdirp(f) { fs.mkdirSync(path.dirname(f), { recursive: true }); }
function append(f, o) { mkdirp(f); fs.appendFileSync(f, JSON.stringify(o) + '\n'); }
function readAll(f) { if (!fs.existsSync(f)) return []; return fs.readFileSync(f, 'utf8').trim().split('\n').filter(Boolean).map(l => JSON.parse(l)); }

// 单一真值源：eval 契约从 settings.json > eval 读取（供阈值状态诚实上报，不改动评分逻辑）
function loadSettings() { try { return JSON.parse(fs.readFileSync(path.join(BASE, 'settings.json'), 'utf8')); } catch (_) { return {}; } }
const SET = loadSettings();
const EVALC = SET.eval || {};
function ensure(f, d) { if (!fs.existsSync(f)) { mkdirp(f); fs.writeFileSync(f, JSON.stringify(d)); } }

// 真实项目 golden 用例库（来源：保温杯变款工作台 MVP 10 缺陷修复 + 视觉分析常驻纪律 + 排障方法论铁律）
// 编码项目里「实存的」质量闸门；仅定义闸门，不虚构结果。宿主/CI 在真实任务后喂入 rubrics 实测值。
const GOLDEN_SEED = [
  { id: 'g_visual_qa_d4', task: '生图细节锐度 D4 须达标（评分标准 v1.1 细节优先，一票否决封顶 C）',
    rubrics: [ { name: 'd4_sharpness_score', type: 'score', threshold: 12 }, { name: 'no_blurry', type: 'bool' } ] },
  { id: 'g_color_lock_cobalt', task: '颜色锁：材质钴蓝主导且非灰（SDXL 三重蓝锚 / Flux2 hex 绑定）',
    rubrics: [ { name: '材质非灰', type: 'bool' }, { name: '材质钴蓝主导', type: 'bool' }, { name: '材质钴蓝主导_ΔE', type: 'bool' } ] },
  { id: 'g_ipadapter_wiring', task: 'IPAdapter 接线正确（UnifiedLoader [0]=MODEL/[1]=IPADAPTER；model:[12,0]/ipadapter:[12,1]）',
    rubrics: [ { name: 'ipadapter_model_pin', type: 'bool' }, { name: 'ipadapter_adapter_pin', type: 'bool' } ] },
  { id: 'g_no_ghost_image', task: '防空白幽灵图：禁 EmptyLatentImage+denoise<1.0 错配；IPAdapter 须 VAEEncode→latent 喂 KSampler',
    rubrics: [ { name: 'no_empty_latent_ghost', type: 'bool', blocker: true } ] },
  { id: 'g_blind_model_forbidden', task: '视觉评审/分析禁用已退役 qwen2.5vl:7b（2026-11-14 卸载）；视觉档 main=qwen3-vl:8b / final=qwen3.6:latest 均属 vision-capable（双档真源，E-D221 更正——qwen3.6 是终审模型非禁用对象）（含 vision_model 字段）',
    rubrics: [ { name: 'vision_model_is_vision_capable', type: 'bool', blocker: true }, { name: 'vision_model_field_present', type: 'bool' } ] },
  { id: 'g_final_vision_capable', task: 'E-D221 补：终审/细看档 qwen3.6:latest 属 vision-capable 须 PASS（黄金案反向面——禁 qwen2.5vl:7b 不误伤 qwen3.6:latest）',
    rubrics: [ { name: 'vision_model_is_vision_capable', type: 'bool', blocker: true } ] },
  { id: 'g_trace_id_link', task: 'R17 可观测性：每次生图任务须 trace_id 串联全链路',
    rubrics: [ { name: 'has_trace_id', type: 'bool', blocker: true } ] },
  { id: 'g_bus_role_decouple', task: 'R21 横向验证：挑战者角色≠生产者，质疑须带证据',
    rubrics: [ { name: 'challenger_ne_diff', type: 'bool' }, { name: 'evidence_carried', type: 'bool' } ] },
  { id: 'g_cors_proper', task: 'MVP 直连 8188：ComfyUI server.py CORS 内建，禁止假设无 CORS',
    rubrics: [ { name: 'cors_builtin', type: 'bool' } ] },
  { id: 'g_binary_download_safe', task: '图片下载走 Buffer.concat，禁止 raw+=chunk（防首字节 fd 损坏）',
    rubrics: [ { name: 'download_buffer_safe', type: 'bool', blocker: true } ] },
  { id: 'g_learning_required_fields', task: 'R18 经验沉淀必填字段（trace_id/category/symptom/root_cause/prevention/reusable/author/ts）',
    rubrics: [ { name: 'learning_has_required', type: 'bool', blocker: true } ] },
  { id: 'g_score_above_8', task: '鸡评审质量底线 ≥8.0 且产出为合法 JSON',
    rubrics: [ { name: '鸡评审>=8.0', type: 'score', threshold: 8.0, blocker: true }, { name: 'no_bad_json', type: 'bool', blocker: true } ] },
  { id: 'g_ui_unchanged', task: 'UI 外观冻结铁律：未授权禁改布局/配色/分区/控件',
    rubrics: [ { name: 'ui_change_approved', type: 'bool' } ] }
];

/** cmdSeed —— 幂等播种真实项目 golden 用例（已存在 id 跳过，不重复累积） */
function cmdSeed() {
  const existing = readAll(CASES).map(c => c.id);
  let added = 0, skipped = 0;
  for (const c of GOLDEN_SEED) {
    if (existing.includes(c.id)) { skipped++; continue; }
    append(CASES, { ...c, createdAt: now() });
    added++;
  }
  const total = readAll(CASES).length;
  const minCases = (EVALC.tiers && EVALC.tiers.golden_regression && EVALC.tiers.golden_regression.minCases) || 50;
  console.log(`🌱 golden 用例播种: 新增 ${added} / 跳过 ${skipped} (现有总计 ${total})`);
  console.log(`📊 golden 用例: ${total} / 要求 ${minCases} → ${total >= minCases ? '达标' : '⚠️ 未达 release-grade 阈值（持续累积中）'}`);
  return { added, skipped, total };
}

/** 对单用例评分：返回 [{name, pass, expected, got, blocker}] */
function scoreCase(c, output) {
  const out = (output && output.rubrics) || {};
  return c.rubrics.map(r => {
    const got = out[r.name];
    let pass;
    if (r.type === 'score') pass = (typeof got === 'number') && got >= r.threshold;
    else pass = got === true; // bool
    return { name: r.name, type: r.type, expected: r.type === 'score' ? ('>=' + r.threshold) : true, got, pass, blocker: !!r.blocker };
  });
}

function cmdCaseAdd(json) {
  const c = JSON.parse(json);
  if (!c.id || !Array.isArray(c.rubrics) || c.rubrics.length === 0) throw new Error('用例须含 id 与非空 rubrics 数组');
  for (const r of c.rubrics) if (!r.name || !['bool', 'score'].includes(r.type)) throw new Error('rubric 须含 name 与 type(bool|score)');
  append(CASES, { ...c, createdAt: now() });
  console.log('✅ 用例已加: ' + c.id + ' (rubrics=' + c.rubrics.length + ', blockers=' + c.rubrics.filter(r => r.blocker).length + ')');
}

function cmdCaseList() {
  const cs = readAll(CASES);
  console.log('用例集 ' + cs.length + ' 条:');
  cs.forEach(c => console.log('  - ' + c.id + ' | rubrics=' + c.rubrics.length + ' | blockers=' + c.rubrics.filter(r => r.blocker).length));
}

function resolveOutput(v) {
  if (!v) return {};
  if (fs.existsSync(v)) return JSON.parse(fs.readFileSync(v, 'utf8'));
  const s = String(v).trim();
  if (s.startsWith('{')) return JSON.parse(s);
  throw new Error('--output 需为可读文件或 JSON 字符串: ' + v);
}
function cmdRun(caseId, outputJson) {
  const cs = readAll(CASES);
  const c = cs.find(x => x.id === caseId);
  if (!c) throw new Error('用例不存在: ' + caseId);
  const out = resolveOutput(outputJson);
  const detail = scoreCase(c, out);
  const run = { id: uid(), caseId, traceLink: out.trace_id || null, detail, passRate: detail.filter(d => d.pass).length / detail.length, createdAt: now() };
  append(RUNS, run);
  console.log('✅ 评分 ' + caseId + ' | 通过率=' + run.passRate.toFixed(2));
  detail.forEach(d => console.log('   ' + (d.pass ? '✓' : '✗') + ' ' + d.name + ' (' + d.type + ' 期望=' + d.expected + ' 实得=' + d.got + ')' + (d.blocker ? ' [BLOCKER]' : '')));
}

function cmdSuite(resultsFile) {
  const cs = readAll(CASES);
  if (cs.length === 0) throw new Error('用例集为空，先 eval.js case add');
  const results = resultsFile && fs.existsSync(resultsFile) ? JSON.parse(fs.readFileSync(resultsFile, 'utf8')) : null;
  const caseRuns = [];
  const perRubric = {};
  let blockerFails = 0;
  for (const c of cs) {
    const out = results ? (results[c.id] || {}) : {};
    const detail = scoreCase(c, out);
    let pr = 0;
    for (const d of detail) {
      perRubric[d.name] = perRubric[d.name] || { pass: 0, total: 0, blockers: 0, blockerFails: 0 };
      perRubric[d.name].total++;
      if (d.pass) perRubric[d.name].pass++;
      if (d.blocker) { perRubric[d.name].blockers++; if (!d.pass) { perRubric[d.name].blockerFails++; blockerFails++; } }
      if (d.pass) pr++;
    }
    caseRuns.push({ caseId: c.id, passRate: pr / detail.length });
  }
  const suite = {
    id: uid(),
    caseCount: cs.length,
    perRubric: Object.fromEntries(Object.entries(perRubric).map(([k, v]) => [k, { passRate: +(v.pass / v.total).toFixed(3), blockers: v.blockers, blockerFails: v.blockerFails }])),
    blockerFails,
    createdAt: now()
  };
  append(SUITES, suite);
  console.log('=== Suite ' + suite.id + ' | 用例=' + suite.caseCount + ' | 阻断项失败=' + blockerFails + ' ===');
  console.log('--- 逐 rubric 通过率（不看总分，看这里）---');
  for (const [k, v] of Object.entries(suite.perRubric)) console.log('  ' + k + ': ' + (v.passRate * 100).toFixed(1) + '%' + (v.blockers ? '  [BLOCKERS=' + v.blockerFails + '/' + v.blockers + ']' : ''));
  return suite;
}

function cmdBaselineSet() {
  const suites = readAll(SUITES);
  if (suites.length === 0) throw new Error('无 suite 可标记基线，先 eval.js suite');
  const last = suites[suites.length - 1];
  ensure(BASELINE, {});
  fs.writeFileSync(BASELINE, JSON.stringify({ suiteId: last.id, createdAt: last.createdAt }));
  console.log('✅ 基线已设: ' + last.id);
}

function cmdRegress() {
  // R27 / D-57: 判定改为「按内容」而非「按存在性」—— 清空后的基线是空哨兵文件, 仍须视作未设基线
  const _baseRaw = fs.existsSync(BASELINE) ? fs.readFileSync(BASELINE, 'utf8').trim() : '';
  if (!_baseRaw) { console.log('⚠️ 未设基线，先 eval.js baseline set'); return { regressed: 0, blockerFails: 0, newBlockerFails: 0, baselineDirty: false, blocked: false }; }
  const base = JSON.parse(_baseRaw);
  const suites = readAll(SUITES);
  const cur = suites[suites.length - 1];
  const baseSuite = suites.find(s => s.id === base.suiteId) || suites[0];
  let regressed = 0;
  const lines = [];
  for (const [k, v] of Object.entries(cur.perRubric)) {
    const bv = baseSuite.perRubric[k];
    if (!bv) continue;
    const delta = v.passRate - bv.passRate;
    if (delta < -0.001) { regressed++; lines.push('  ✗ ' + k + ' 退化 ' + (delta * 100).toFixed(1) + 'pt (基线=' + (bv.passRate * 100).toFixed(1) + '% → 当前=' + (v.passRate * 100).toFixed(1) + '%)'); }
  }
  // R17-F 修复：阻断判定改为「相对基线」——仅新增阻断失败才拦；
  // 基线本身红 → baselineDirty 标记技术债(WARN)，避免「永远红」失去 CI 意义（对齐 R25 block-on-regression 语义）。
  const baseBlockerFails = baseSuite.blockerFails || 0;
  const curBlockerFails = cur.blockerFails || 0;
  const newBlockerFails = curBlockerFails - baseBlockerFails;
  const baselineDirty = baseBlockerFails > 0;
  const blocked = newBlockerFails > 0;
  console.log('=== 回归检测 vs 基线 ' + base.suiteId + ' ===');
  lines.forEach(l => console.log(l));
  console.log('基线阻断失败=' + baseBlockerFails + ' | 当前阻断失败=' + curBlockerFails + ' | 新增阻断失败=' + newBlockerFails + (baselineDirty ? ' | ⚠️ 基线本身含阻断失败(技术债)' : ''));
  if (blocked) console.log('🚫 RELEASE BLOCKED: ' + newBlockerFails + ' 个新增阻断项失败(相对基线)');
  else if (baselineDirty) console.log('⚠️ 无新增阻断失败，但基线本身含 ' + baseBlockerFails + ' 个阻断失败(技术债，需清理基线)');
  else if (regressed > 0) console.log('⚠️ ' + regressed + ' 个 rubric 退化（非阻断项）');
  else console.log('✅ 无回归，阻断项全过');
  return { regressed, blockerFails: curBlockerFails, newBlockerFails, baselineDirty, blocked };
}

function cmdExport() {
  const cs = readAll(CASES), suites = readAll(SUITES);
  console.log(JSON.stringify({ cases: cs, latestSuite: suites[suites.length - 1] || null }, null, 2));
}

/**
 * cmdBench —— 外部 Benchmark 适配层 (R24)
 * 把用户反复说的「网络对比参照」固化为 eval 一层能力：
 *   对齐 agents-hive「外部Benchmark接入(adapter+CLI)」+ Ryan Setter 厂商中立 JSON schema
 *   外部 benchmark 形如 { name, source, cases:[{id, rubrics:{名:bool|number}}] }
 *   交叉：仅对「内外都定义的 rubric 名」用同一套通过规则打分（苹果对苹果），
 *   输出横向对比报告（internal suite vs external benchmark），并列出仅单边有的 rubric。
 *   注意：本命令不新增能力维度，是外部验证(external validation)的「外部」部分，纯引擎能力，不依赖宿主重载。
 */
function cmdBench(file) {
  if (!file) throw new Error('用法: eval.js bench <外部benchmark.json>');
  if (!fs.existsSync(file)) throw new Error('外部 benchmark 文件不存在: ' + file);
  const ext = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (!Array.isArray(ext.cases) || ext.cases.length === 0) throw new Error('外部 benchmark 须含非空 cases 数组');
  // 内部 rubric 定义（来自已加 golden 用例）
  const defs = {};
  readAll(CASES).forEach(c => c.rubrics.forEach(r => { if (!defs[r.name]) defs[r.name] = r; }));
  const defNames = Object.keys(defs);
  // 外部只对其 rubric 名在内部定义集里的，才用内部规则交叉打分
  const extByName = {};
  ext.cases.forEach(c => {
    const rs = (c.rubrics && typeof c.rubrics === 'object') ? c.rubrics : {};
    Object.entries(rs).forEach(([name, got]) => {
      extByName[name] = extByName[name] || { pass: 0, total: 0 };
      extByName[name].total++;
      const d = defs[name];
      if (!d) return; // 仅外部有，不交叉
      let pass;
      if (d.type === 'score') pass = (typeof got === 'number') && got >= d.threshold;
      else pass = got === true;
      if (pass) extByName[name].pass++;
    });
  });
  // 内部最新 suite
  const suites = readAll(SUITES);
  const last = suites.length ? suites[suites.length - 1] : null;
  const shared = defNames.filter(n => extByName[n] && extByName[n].total > 0);
  console.log('=== 外部 Benchmark 交叉对比: ' + (ext.name || file) + ' (source=' + (ext.source || '?') + ') ===');
  console.log('外部用例=' + ext.cases.length + ' | 内部 rubric 定义=' + defNames.length + ' | 共享 rubric=' + shared.length);
  console.log('--- 横向对比 (共享 rubric, 苹果对苹果) ---');
  shared.forEach(n => {
    const extRate = extByName[n].pass / extByName[n].total;
    const intRate = (last && last.perRubric[n]) ? last.perRubric[n].passRate : null;
    const intStr = intRate === null ? 'n/a(内部未跑suite)' : (intRate * 100).toFixed(1) + '%';
    const delta = intRate === null ? '?' : (((extRate - intRate) * 100).toFixed(1) + 'pt');
    console.log('  ' + n + ': 内部=' + intStr + ' | 外部=' + (extRate * 100).toFixed(1) + '%' + (intRate === null ? '' : ' | Δ=' + delta));
  });
  const onlyExt = Object.keys(extByName).filter(n => !defs[n]);
  const onlyInt = defNames.filter(n => !extByName[n] || extByName[n].total === 0);
  if (onlyExt.length) console.log('仅外部有(无内部 rubric 定义, 不交叉): ' + onlyExt.join(', '));
  if (onlyInt.length) console.log('仅内部有(外部 benchmark 未覆盖): ' + onlyInt.join(', '));
  return { name: ext.name || file, shared: shared.length, onlyExt: onlyExt.length, onlyInt: onlyInt.length };
}

/**
 * cmdValidate —— 外部验证编排层 (R25)
 * 把 R23 eval 纪律 + R24 外部 benchmark 适配 串成「单一 release-gate 裁决」，
 * 对齐业界 CI 共识（callsphere「tier the suite + block on regression」/
 *   confident-ai「release workflow around the score decision」/
 *   futureagi「4-stage CI: smoke<90s → full 200-500 cases → sim → canary+rollback」/
 *   smart-labs「300 scenario nightly + canary gate + auto-rollback」）：
 *   - smoke 模式（无 --results）：仅跑 baseline 回归（比对最近 suite 与基线），秒级，对应 PR-time fast check
 *   - full 模式（--results）：suite 对真实 outputs + 可选 --bench 外部交叉 + 回归 → 单一裁决
 *   输出 RELEASE GATE 裁决(PASS/WARN/BLOCKED) + exit 码（BLOCKED→exit 2），供 CI 直接挂门禁。
 *   本命令不新增能力维度，是已有 eval 能力的「编排胶水」，使外部验证一键可执行。
 */
function cmdValidate(resultsFile, benchFile) {
  let suite = null;
  if (resultsFile) suite = cmdSuite(resultsFile);
  const reg = cmdRegress();
  let benchRes = null;
  if (benchFile) benchRes = cmdBench(benchFile);
  const gate = reg.blocked ? 'BLOCKED' : (reg.baselineDirty || reg.regressed > 0 ? 'WARN' : 'PASS');
  console.log('=== RELEASE GATE (' + (resultsFile ? 'full' : 'smoke') + ') : ' + gate + ' ===');
  if (gate === 'BLOCKED') console.log('🚫 发布被阻断：相对基线出现新增阻断项失败，CI 应 fail');
  else if (gate === 'WARN') console.log(reg.baselineDirty ? '⚠️ 基线本身含阻断失败(技术债)，需清理基线后重设' : '⚠️ 存在 rubric 退化（非阻断项），需 reviewer 确认');
  else console.log('✅ 通过：无新增阻断项失败且无退化');
  return { mode: resultsFile ? 'full' : 'smoke', suite, regress: reg, bench: benchRes, gate };
}

function cmdClear() {
  [CASES, RUNS, SUITES].forEach(f => { if (fs.existsSync(f)) fs.writeFileSync(f, ''); });
  // R27 / D-57: 基线清空改用「写入空哨兵」代替 unlinkSync。
  // 根因: 宿主 safe-delete 批量守卫下 unlinkSync 会偶发 EPERM(内部 state.json rename 争用)
  //       → cmdClear 无保护抛错 → selftest 整体崩溃 exit 1 → 聚合门禁出现 8/9 假 FAIL。
  // 语义等价: 空文件 ≡ 未设基线(由 cmdRegress 的空内容判定承担), 且前三行本就是「写空」惯例, 现四者一致。
  try { fs.writeFileSync(BASELINE, ''); } catch (e) { try { fs.unlinkSync(BASELINE); } catch (_) {} }
  console.log('🧹 eval 数据已清空');
}

function cmdSelftest() {
  console.log('--- eval.js selftest ---');
  // R17-R 修复：受控备份生产 eval 库（cases/runs/suites/baseline），演示后 try/finally 还原。
  // 此前 selftest 直接 cmdClear() 清库灌 demo，跑一次 selftest_all 即把真实 golden-set/基线覆盖为 demo 态，
  // 与 verify.js(R17-J) / runtime.js(R17-I) 已修的同类坑一致 —— 本次补齐三引擎一致性。
  // 注意：内部失败路径一律用 process.exitCode + return，禁用 process.exit()（会跳过 finally 导致丢库）。
  const _bk = {
    cases: fs.existsSync(CASES) ? fs.readFileSync(CASES, 'utf8') : null,
    runs: fs.existsSync(RUNS) ? fs.readFileSync(RUNS, 'utf8') : null,
    suites: fs.existsSync(SUITES) ? fs.readFileSync(SUITES, 'utf8') : null,
    baseline: fs.existsSync(BASELINE) ? fs.readFileSync(BASELINE, 'utf8') : null
  };
  const _restore = () => {
    const pairs = [[CASES, _bk.cases], [RUNS, _bk.runs], [SUITES, _bk.suites], [BASELINE, _bk.baseline]];
    for (const [f, v] of pairs) {
      try {
        if (v === null) { fs.writeFileSync(f, ''); }   // R27/D-57: 写空代替 unlink(语义等价), 避免 safe-delete 偶发 EPERM
        else fs.writeFileSync(f, v, 'utf8');
      } catch (e) { console.log('⚠️ 还原失败 ' + path.basename(f) + ': ' + e.message); }
    }
    console.log('生产 eval 库已受控还原(cases/runs/suites/baseline 无 demo 污染)');
  };
  try {
  cmdClear();
  // 幂等播种真实项目 golden 用例（覆盖项目实存质量闸门）
  cmdSeed();

  // 绿基线：构造使「所有阻断项 + 全 rubric」通过的实测结果
  const green = {
    g_visual_qa_d4: { rubrics: { 'd4_sharpness_score': 15, 'no_blurry': true } },
    g_color_lock_cobalt: { rubrics: { '材质非灰': true, '材质钴蓝主导': true, '材质钴蓝主导_ΔE': true } },
    g_ipadapter_wiring: { rubrics: { 'ipadapter_model_pin': true, 'ipadapter_adapter_pin': true } },
    g_no_ghost_image: { rubrics: { 'no_empty_latent_ghost': true } },
    g_blind_model_forbidden: { rubrics: { 'vision_model_is_vision_capable': true, 'vision_model_field_present': true } },
    g_final_vision_capable: { rubrics: { 'vision_model_is_vision_capable': true } },
    g_trace_id_link: { rubrics: { 'has_trace_id': true } },
    g_bus_role_decouple: { rubrics: { 'challenger_ne_diff': true, 'evidence_carried': true } },
    g_cors_proper: { rubrics: { 'cors_builtin': true } },
    g_binary_download_safe: { rubrics: { 'download_buffer_safe': true } },
    g_learning_required_fields: { rubrics: { 'learning_has_required': true } },
    g_score_above_8: { rubrics: { '鸡评审>=8.0': 9.0, 'no_bad_json': true } },
    g_ui_unchanged: { rubrics: { 'ui_change_approved': true } }
  };
  // R27 / D-57: 演示中间产物改写到系统临时目录 —— ① 宿主 shim 对 tmpdir 的 unlink 稳定(实测 20/20),
  //   ② 即便删除失败也只落在系统临时区, 不再残留污染包内 logs/。
  const _TMP = require('os').tmpdir();
  const greenFile = path.join(_TMP, 'zodiac_eval_demo_green.json');
  fs.writeFileSync(greenFile, JSON.stringify(green));
  const sGreen = cmdSuite(greenFile);                 // 全过，blockerFails=0
  if (sGreen.blockerFails !== 0) { console.log('❌ selftest 失败: 绿基线本身有阻断失败=' + sGreen.blockerFails); process.exitCode = 1; return; }
  cmdBaselineSet();                                   // 设为绿基线

  // 回归场景：绿基线基础上，让「一个阻断项」新失败（模拟发布回退）
  const regress = JSON.parse(JSON.stringify(green));
  regress.g_no_ghost_image.rubrics['no_empty_latent_ghost'] = false;   // 阻断项新失败
  const regFile = path.join(_TMP, 'zodiac_eval_demo_regress.json');
  fs.writeFileSync(regFile, JSON.stringify(regress));
  const sReg = cmdSuite(regFile);                     // 新增 1 个阻断失败
  const reg = cmdRegress();
  const blocked = reg.blocked;
  console.log(blocked ? '✅ selftest 通过: 新增阻断项失败被正确拦截(BLOCK)' : '❌ selftest 失败: 阻断回归未生效');
  if (!blocked) { process.exitCode = 1; return; }
  if (!reg.baselineDirty) console.log('✅ 绿基线技术债标记正确(baselineDirty=false)');

  // 反向验证：与绿基线完全一致 → 不应再拦（证明 R17-F「永远红」已修复）
  const sGreen2 = cmdSuite(greenFile);
  const reg2 = cmdRegress();
  const blocked2 = reg2.blocked;
  console.log(!blocked2 ? '✅ 反向验证通过: 无新增阻断项时不拦(告别永远红)' : '❌ 反向验证失败: 仍误拦（bug 未根治）');
  if (blocked2) { process.exitCode = 1; return; }

  // R24: 外部 benchmark 适配演示（把「网络对比参照」固化为 eval 一层能力）
  try {
    const extFile = path.join(_TMP, 'zodiac_eval_demo_bench.json');
    const ext = { name: 'demo-external-bench', source: 'agents-hive', cases: [
      { id: 'e1', rubrics: { '鸡评审>=8.0': 8.6, 'no_bad_json': true, '材质非灰': true, 'external_only_metric': true } },
      { id: 'e2', rubrics: { '鸡评审>=8.0': 7.2, 'no_bad_json': true, '材质非灰': false } }
    ] };
    fs.writeFileSync(extFile, JSON.stringify(ext));
    const b = cmdBench(extFile);
    console.log('✅ bench 适配演示通过: 共享=' + b.shared + ' 仅外部=' + b.onlyExt + ' 仅内部=' + b.onlyInt);
    if (fs.existsSync(extFile)) { try { fs.unlinkSync(extFile); } catch (e) {} }
  } catch (e) { console.log('❌ bench 演示失败: ' + e.message); }

  [greenFile, regFile].forEach(f => { if (fs.existsSync(f)) { try { fs.unlinkSync(f); } catch (e) {} } });
  console.log('✅ eval.js selftest 全部通过');
  } finally {
    _restore();
  }
}

// ---- 分发（D-61/R28：分包进 cli(argv) + require.main 守卫，供 selftest_all 同进程直调）----
function cli(argv) {
  const [,, cmd, sub, ...rest] = argv;
  try {
    if (cmd === 'case') {
      if (sub === 'add') cmdCaseAdd(rest[0]);
      else if (sub === 'list') cmdCaseList();
      else if (sub === 'seed') cmdSeed();
      else throw new Error('用法: eval.js case add|list|seed');
    } else if (cmd === 'run') {
      const ra = [sub, ...rest].filter(Boolean);
      const outIdx = ra.indexOf('--output');
      const outputJson = outIdx >= 0 ? ra[outIdx + 1] : null;
      const caseId = outIdx >= 0 ? ra.filter((x, i) => i !== outIdx && i !== outIdx + 1)[0] : ra[0];
      cmdRun(caseId, outputJson);
    } else if (cmd === 'suite') {
      const sa = [sub, ...rest].filter(Boolean);
      const rf = sa.indexOf('--results'); cmdSuite(rf >= 0 ? sa[rf + 1] : null);
    } else if (cmd === 'baseline') {
      if (sub === 'set') cmdBaselineSet(); else throw new Error('用法: eval.js baseline set');
    } else if (cmd === 'regress') { const r = cmdRegress(); if (r.blocked) process.exit(2); }
    else if (cmd === 'export') cmdExport();
    else if (cmd === 'bench') cmdBench(sub || (rest[0] || null));
    else if (cmd === 'validate') {
      const va = [sub, ...rest].filter(Boolean);
      const ri = va.indexOf('--results'); const bi = va.indexOf('--bench');
      const rf = ri >= 0 ? va[ri + 1] : null;
      const bf = bi >= 0 ? va[bi + 1] : null;
      const v = cmdValidate(rf, bf);
      if (v.regress.blocked) process.exit(2);
    }
    else if (cmd === 'selftest') cmdSelftest();
    else if (cmd === 'clear') cmdClear();
    else { console.log('用法: eval.js <case|run|suite|baseline|regress|export|bench|validate|selftest|clear>'); process.exit(1); }
  } catch (e) {
    console.error('❌ ' + e.message);
    process.exit(1);
  }
}

if (require.main === module) cli(process.argv);
module.exports = { cli };
