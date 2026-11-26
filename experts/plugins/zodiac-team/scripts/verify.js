#!/usr/bin/env node
/*
 * verify.js — 生肖团横向验证层引擎 (Adversarial Verification Layer)
 * 对齐 MAVEN (arXiv:2605.07646 Skeptic-Researcher-Judge + In-Step Epistemic Auditing)
 *      + segmentfault 四模式(输出评分/Reflexion/对抗辩论/过程验证)
 *      + Atla/Cohere/DeepMind 元评估(arXiv:2606.21627 谁来监督监督者)
 *
 * 设计原则（来自网络对标）：
 *   1. 角色解耦：挑战者必须与生产者不同角色——多 Agent 验证靠"多样性"生效，
 *      同一模型自我检查会同意自己（Reflexion 回声室失效）。
 *   2. 过程审计：在阶段边界(而非仅终态)做验证，防错误级联(Pattern 4 过程验证)。
 *   3. 本地代码裁决：challenger!=producer / 须带证据 等由本脚本确定性校验，非 LLM 自觉。
 *   4. 鸡为终审 Judge，且鸡的 critique 本身落 observability 供下游元评估。
 *   5. 成本策略：验证者用小模型/精细 rubric 即可，不须更重模型。
 *
 * 命令：
 *   node verify.js challenge <producer> <challenger> <phase> <claim> <evidence> [traceId]
 *   node verify.js respond  <challengeId> <rebuttal> <evidence>
 *   node verify.js resolve  <challengeId> <judge> <verdict> <reason>   // verdict: uphold|overturn|rework
 *   node verify.js list     [phase]
 *   node verify.js stats
 *   node verify.js export   [out.jsonl]
 *   node verify.js selftest
 *   node verify.js clear
 *
 * 修复记录（R25 · 2026-09-23）：
 *   D-49 —— dispatch 统一以数组传参(process.argv.slice(3))，可选单参命令 list/export 收到 []
 *           （空数组为 truthy）→ list 恒空、export 抛 TypeError。改：入口 Array 降级 +
 *           2 条 selftest 回归断言（"每次修复都转成回归用例"）。
 *   D-54 —— 包根原用 path.resolve(__dirname,'..')；在 C:\...\.workbuddy → H:\WB_Data\.workbuddy
 *           的 junction 环境下被解析为真实路径，宿主 fs shim 仅放行经 C:\ 链接路径的写入 →
 *           本引擎 append/write/rename 全 EPERM（长期写不进 SINK）。改：USERPROFILE 链接路径
 *           优先、__dirname 回退，与其余 8 个引擎对齐。
 *   D-55 —— selftest 原假设空库，非空库时 load().find(首条)/[1] 取到历史记录（演示失真、
 *           护栏误触，断言却仍绿 = 假绿）。改：受控清空 + 取"最后插入"的那条。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// 本脚本随包部署于 zodiac-team/scripts/，上一级即活包根（含 settings.json / logs / docs）
// 修复 D-54（R25）：原为 path.resolve(__dirname, '..')，在 C:\Users\...\.workbuddy → H:\WB_Data\.workbuddy
// 的 junction 环境下，__dirname 被 node 解析为「真实路径」H:\WB_Data\...，而宿主 fs shim 仅放行经
// C:\ 链接路径的写入 → 本引擎所有写操作(append/write/rename) 一律 EPERM，长期"写不进 SINK"。
// 与全库其余 8 个引擎对齐：优先经 USERPROFILE 的链接路径，不存在时再回退 __dirname。
const LINK_BASE = path.join(
  process.env.USERPROFILE || 'C:/Users/Administrator',
  '.workbuddy/plugins/marketplaces/experts/plugins/zodiac-team'
);
const BASE = fs.existsSync(LINK_BASE) ? LINK_BASE : path.resolve(__dirname, '..');
const SINK = path.join(BASE, 'logs', 'zodiac_verifications.jsonl');

// 单一真值源：验证契约从 settings.json > verification 读取（缺省回退硬编码，行为不变）
const SETTINGS_PATH = path.resolve(BASE, 'settings.json');
function loadSettings() { try { return JSON.parse(fs.readFileSync(SETTINGS_PATH, 'utf8')); } catch (_) { return {}; } }
const SET = loadSettings();
const VERIF = SET.verification || {};
const MAX_ROUNDS = (VERIF.loop && VERIF.loop.maxRounds) || 2;
const JUDGE_ROLE = (VERIF.judge && VERIF.judge.role) || 'rooster-design-reviewer';

function load() {
  if (!fs.existsSync(SINK)) return [];
  return fs.readFileSync(SINK, 'utf8').trim().split('\n').filter(Boolean).map(l => JSON.parse(l));
}
function append(rec) {
  fs.mkdirSync(path.dirname(SINK), { recursive: true });
  fs.appendFileSync(SINK, JSON.stringify(rec) + '\n', 'utf8');
}
function uid() { return 'vf_' + crypto.randomBytes(4).toString('hex'); }
function now() { return new Date().toISOString(); }

// 确定性护栏：挑战者必须与生产者不同角色，且须带证据（本地代码裁决）
function validateChallenge(producer, challenger, claim, evidence) {
  const errs = [];
  if (!producer || !challenger) errs.push('producer 与 challenger 均不可为空');
  if (producer === challenger) errs.push('角色解耦违例：challenger 必须与 producer 不同角色（多 Agent 验证靠多样性生效）');
  if (!claim || claim.trim().length < 4) errs.push('claim 过短，须明确质疑点');
  if (!evidence || evidence.trim().length < 4) errs.push('requireEvidence：挑战须带证据，禁止空泛质疑');
  return errs;
}

function cmdChallenge(args) {
  const [producer, challenger, phase, claim, evidence, traceId] = args;
  const errs = validateChallenge(producer, challenger, claim, evidence);
  if (errs.length) { console.log('❌ BLOCKED: ' + errs.join('; ')); return 1; }
  const rec = {
    id: uid(), kind: 'challenge', producer, challenger, phase: phase || 'P?',
    claim, evidence, traceId: traceId || null, round: 1,
    status: 'open', createdAt: now()
  };
  append(rec);
  console.log('✅ 挑战已记录 ' + rec.id + ' | ' + producer + ' ←' + challenger + ' @' + rec.phase + ' | 证据=' + (evidence.length > 30 ? evidence.slice(0, 30) + '…' : evidence));
  return 0;
}

function cmdRespond(args) {
  const [id, rebuttal, evidence] = args;
  const all = load();
  const rec = all.find(r => r.id === id && r.kind === 'challenge');
  if (!rec) { console.log('❌ 未找到挑战 ' + id); return 1; }
  if (!rebuttal || rebuttal.trim().length < 4) { console.log('❌ BLOCKED: rebuttal 过短'); return 1; }
  if (rec.round >= MAX_ROUNDS) { console.log('⚠️ 已达最大轮次 ' + MAX_ROUNDS + '，请直接 resolve 由鸡裁决'); return 1; }
  const resp = {
    id: uid(), kind: 'response', challengeId: id, producer: rec.producer,
    rebuttal, evidence: evidence || '', round: rec.round + 1, createdAt: now()
  };
  // 修复 R17-L：挑战记录的 round 须随回应同步递增，否则 cmdRespond 顶部的 maxRounds 护栏
  // 检查的 rec.round 永远=1 → 恒为 false → 护栏永不触发（半真护栏）。rec 是 all[] 中挑战对象的
  // 引用，直接更新即随下方 writeFileSync 落盘。
  rec.round = resp.round;
  append(resp);
  all.push(resp);
  fs.writeFileSync(SINK, all.map(r => JSON.stringify(r)).join('\n') + '\n', 'utf8');
  console.log('✅ 生产者回应 ' + resp.id + ' | 轮次=' + resp.round + ' | 反驳=' + (rebuttal.length > 30 ? rebuttal.slice(0, 30) + '…' : rebuttal));
  return 0;
}

function cmdResolve(args) {
  const [id, judge, verdict, reason] = args;
  const all = load();
  const rec = all.find(r => r.id === id && r.kind === 'challenge');
  if (!rec) { console.log('❌ 未找到挑战 ' + id); return 1; }
  if (!['uphold', 'overturn', 'rework'].includes(verdict)) { console.log('❌ verdict 须为 uphold|overturn|rework'); return 1; }
  if (judge !== JUDGE_ROLE) console.log('⚠️ 终审 Judge 应为 鸡(' + JUDGE_ROLE + ')，当前=' + judge);
  const res = {
    id: uid(), kind: 'resolution', challengeId: id, judge, verdict, reason: reason || '', createdAt: now()
  };
  all.push(res);
  rec.status = 'resolved:' + verdict;
  fs.writeFileSync(SINK, all.map(r => JSON.stringify(r)).join('\n') + '\n', 'utf8');
  const sym = { uphold: '✅挑战成立', overturn: '↩️挑战推翻', rework: '🔧需返工' }[verdict];
  console.log(sym + ' | ' + judge + ' 裁决 ' + id + ' → ' + verdict + (reason ? ' | ' + reason : ''));
  console.log('   （鸡的 critique 已落 observability 供下游元评估：who-watches-the-watcher）');
  return 0;
}

function cmdList(phase) {
  // 修复 D-49（R25）：dispatch 统一以数组调用（process.argv.slice(3)），无参时 phase=[]，
  // 而 [] 为 truthy → filter(r => r.phase === []) 恒 false → list 永远"（无验证记录）"。
  // 此处把数组降级为标量（无参 → undefined），其余调用语义不变。
  if (Array.isArray(phase)) phase = phase[0];
  const all = load().filter(r => r.kind === 'challenge');
  const f = phase ? all.filter(r => r.phase === phase) : all;
  if (!f.length) { console.log('（无验证记录' + (phase ? ' @' + phase : '') + '）'); return 0; }
  f.forEach(r => console.log(`${r.id} | ${r.producer}←${r.challenger} @${r.phase} | ${r.status} | ${r.claim.slice(0, 24)}`));
  return 0;
}

function cmdStats() {
  const all = load();
  const ch = all.filter(r => r.kind === 'challenge');
  const res = all.filter(r => r.kind === 'resolution');
  const byVerdict = {};
  res.forEach(r => byVerdict[r.verdict] = (byVerdict[r.verdict] || 0) + 1);
  const roles = {};
  ch.forEach(r => { roles[r.challenger] = (roles[r.challenger] || 0) + 1; });
  console.log('挑战总数=' + ch.length + ' | 裁决数=' + res.length);
  console.log('裁决分布=' + JSON.stringify(byVerdict));
  console.log('挑战者角色分布=' + JSON.stringify(roles));
  return 0;
}

function cmdExport(out) {
  // 修复 D-49（R25）：同 cmdList，out 实为数组（无参时 []）→ fs.copyFileSync(SINK, [])
  // 抛 TypeError: The "dest" argument must be of type string. 降级为标量；并补 SINK 缺失防御。
  if (Array.isArray(out)) out = out[0];
  if (!fs.existsSync(SINK)) { console.log('（无验证流可导出）'); return 0; }
  const dest = out || path.join(BASE, 'logs', 'zodiac_verifications_export.jsonl');
  fs.copyFileSync(SINK, dest);
  console.log('已导出 → ' + dest);
  return 0;
}

function cmdSelftest() {
  console.log('=== verify.js selftest ===');
  // 受控验证: 备份真实验证流, 演示后 try/finally 还原, 杜绝 cmdClear() 全清丢库 + demo 污染 (R19 完整性, 对齐 R17-J)
  const _bk = fs.existsSync(SINK) ? fs.readFileSync(SINK, 'utf8') : '';
  try {
    // 修复 D-55（R25）：selftest 须在「空库」上跑——原实现在非空库时，下方 load().find(首条)/[1]
    // 会取到历史记录而非刚插入的那条（演示失真、护栏误触，断言却仍绿 = 假绿）。
    // 此处受控清空，finally 已负责原样还原，不污染生产记录。
    fs.mkdirSync(path.dirname(SINK), { recursive: true });
    fs.writeFileSync(SINK, '');
    let pass = 0, fail = 0;
    // 1. 角色解耦护栏：challenger==producer 必须被拦截
    if (cmdChallenge(['goat-ai-image-generator', 'goat-ai-image-generator', 'P5', '图糊', 'evidence']) === 1) { console.log('✅ 角色解耦护栏生效（同角色被拦）'); pass++; } else fail++;
    // 2. 证据护栏：无证据必须被拦截
    if (cmdChallenge(['goat-ai-image-generator', 'rabbit-image-analyst', 'P5', '图糊', '']) === 1) { console.log('✅ requireEvidence 护栏生效（无证据被拦）'); pass++; } else fail++;
    // 3. 正常挑战 + 回应 + 鸡裁决（成立）
    cmdChallenge(['goat-ai-image-generator', 'rabbit-image-analyst', 'P5', '主体边缘模糊疑似 ControlNet 失准', '对比参考图 node31 输出，左缘 12px 羽化缺失'], 'run_demo');
    const _chs = load().filter(r => r.kind === 'challenge');
    const id = _chs[_chs.length - 1].id;   // 取刚插入的那条（防历史记录干扰）
    cmdRespond([id, '已补 ControlNet 强度至 0.65，重渲左缘锐利', '重渲图亮度梯度 +40%']);
    cmdResolve([id, 'rooster-design-reviewer', 'uphold', '参考图融合外观节点需更强约束']);
    // 4. 正常挑战 + 鸡推翻
    cmdChallenge(['snake-product-designer', 'dragon-competitor-analyst', 'P3', '商务款深蓝拼接与竞品 A 撞色', '竞品 A 2026 春季款 Pantone 同色域'], 'run_demo');
    const _chs2 = load().filter(r => r.kind === 'challenge');
    const id2 = _chs2[_chs2.length - 1].id;   // 同上：取刚插入的那条
    cmdResolve([id2, 'rooster-design-reviewer', 'overturn', '竞品为哑光、我方为亮面改哑光，色域不同不构成撞色']);
    cmdStats();
    // 5/6. D-49 回归（R25）：dispatch 统一以「数组」调用是常态，故 list 无参与 export 必须不再失效。
    //      对齐「每次修复都转为回归用例」纪律，防同类"可选单参"错配再次隐身。
    const _bakLog = console.log, _cap = [], _silent = (...a) => _cap.push(a.join(' '));
    console.log = _silent;
    const _rc = cmdList([]);
    console.log = _bakLog;
    if (_rc === 0 && !_cap.join('\n').includes('（无验证记录')) { console.log('✅ D-49 回归：无参 list 能列出挑战（不再恒空）'); pass++; } else fail++;
    const _tmpOut = path.join(require('os').tmpdir(), 'zodiac_verify_selftest_export.jsonl');
    let _ok = false;
    console.log = _silent;
    try { _ok = (cmdExport([_tmpOut]) === 0 && fs.existsSync(_tmpOut) && fs.statSync(_tmpOut).size > 0); } catch (_e) { _ok = false; }
    console.log = _bakLog;
    // 刻意不 unlink：本机 safe-delete guard 会把 unlink 转 genie-trash 并 ETIMEDOUT，拖慢 CI。
    // 固定文件名覆盖写，既不堆积残留、也不产生删除开销。
    if (_ok) { console.log('✅ D-49 回归：export 正常导出（TypeError 已修）'); pass++; } else fail++;
    console.log(pass + ' 护栏通过 / ' + fail + ' 失败');
    console.log(fail === 0 ? '✅ selftest 全过' : '❌ selftest 有失败');
    return fail === 0 ? 0 : 1;
  } finally {
    fs.writeFileSync(SINK, _bk);
    console.log('真实验证流已受控还原(无演示污染, 不清空生产验证记录)');
  }
}

function cmdClear() {
  if (fs.existsSync(SINK)) fs.writeFileSync(SINK, '', 'utf8');
  console.log('已清空验证流（生产空态）');
  return 0;
}

const dispatch = {
  challenge: cmdChallenge, respond: cmdRespond, resolve: cmdResolve,
  list: cmdList, stats: cmdStats, export: cmdExport,
  selftest: cmdSelftest, clear: cmdClear
};
// D-61(R28): 模块化(同 trace.js) —— runtime 可在同进程内直调, 规避受限宿主禁 node 建子进程(EBUSY)。
//   逻辑零改动: require.main 时行为与改造前等价。
function cli(argv) {
  const cmd = argv[2];
  if (!cmd || !dispatch[cmd]) {
    console.log('用法: node verify.js <challenge|respond|resolve|list|stats|export|selftest|clear> [args]');
    process.exit(1);
  }
  process.exit(dispatch[cmd](argv.slice(3)));
}

if (require.main === module) cli(process.argv);
module.exports = { cli, dispatch };
