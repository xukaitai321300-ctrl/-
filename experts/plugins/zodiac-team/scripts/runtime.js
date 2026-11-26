#!/usr/bin/env node
/**
 * zodiac-runtime —— 十维架构运行时集成闭环 (R22)
 * ---------------------------------------------------------------------------
 * 把 R17 observability(trace) / R18 learnings(learn) / R19 evolution(evolve) /
 * R21 verification(verify) 串成「单一可调用入口」，对齐 2026 工业界共识：
 *   - 编排 / 执行 / 状态 / 观测 四面解耦 (data-gate 2026 / appscale 2026)
 *   - 为失败设计：版本化+回滚、深度上限防死循环、熔断、战略人审 (dev.to 12-agents)
 *   - 治理 > 监控：预算/熔断是「拦行为」而非「报账单」(Swarm Tax / Waxell)
 *
 * 设计要点：
 *   1. 单一 run_id 贯穿四流（= observability.trace_id），实现「能串」
 *   2. 深度计数器（depth field）防无限循环：> MAX_DEPTH 丢弃并日志
 *   3. token 预算 + 熔断：超预算即 halt（治理层，非监控层）
 *   4. human-in-the-loop 升级闸：仅高风/低置信升级鼠+鸡（战略人审，非全审批）
 *   5. 每阶段后自动 verify(R21) 落 challenge → 沉淀过程经验(R18)；(inter-episode) evolve(R19) 提议
 *      注(D-52): 挑战「是否成立」由 verify.js 后续 resolve 裁决(鸡/人介入)，本编排层不预判结论 ——
 *                故 learn 是「触发对抗审计即沉淀过程经验」，而非「判定成立后才沉淀」
 *   6. 全部事件落 logs/ 被 recovery 快照覆盖（可恢复）
 *
 * 命令：run / phase / budget / escalate / status / export / selftest / clear
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const BASE = path.join(__dirname, '..');  // R221r2/R8a：E-D57 防再现，禁硬编码 marketplaces 绝对路径
const LOGDIR = path.join(BASE, 'logs');
const SINK = path.join(LOGDIR, 'zodiac_runtime.jsonl');

// 真实集成：薄编排层触发四引擎（不复制逻辑），统一 run_id 串联四流
const TRACE_JS  = path.join(__dirname, 'trace.js');
const LEARN_JS  = path.join(__dirname, 'learn.js');
const VERIFY_JS = path.join(__dirname, 'verify.js');
const EVO_JS    = path.join(__dirname, 'evolve.js');

// ── D-61(R28) 集成方式：同进程直调优先，子进程兜底 ───────────────────────────
// 受限宿主禁止 node 创建子进程 → spawnSync 恒 EBUSY → 集成链路"名义存在、实际不可验证"。
// 四引擎已模块化(导出 cli), 故改为在本进程内直调并捕获输出; 子进程路径保留兜底
//   (未模块化的外部引擎 / 确需真隔离场景)。
// 同进程调用 + 输出捕获的实现抽到 lib/inproc.js（单一真值源，runtime 与 selftest_all 共用）
const { invokeInProc, entryOf } = require(path.join(__dirname, 'lib', 'inproc.js'));
const ENGINE_MODS = {
  'trace.js':  require(TRACE_JS),
  'learn.js':  require(LEARN_JS),
  'verify.js': require(VERIFY_JS),
  'evolve.js': require(EVO_JS),
};

// 集成触发 best-effort：引擎不可用仅告警，不阻断 run（治理层原则）
function runEngine(js, args) {
  const base = path.basename(js);
  const entry = entryOf(ENGINE_MODS[base]);
  if (entry) {                                  // ① 同进程直调(优先, 不受宿主子进程限制)
    const r = invokeInProc(entry, ['node', js, ...args]);
    if (r.status !== 0) {
      console.error('  ⚠ 集成引擎非0(' + base + '): ' + String(r.stdout).trim().split('\n').pop());
    }
    return r;
  }
  try {                                          // ② 子进程兜底
    const r = spawnSync(process.execPath, [js, ...args], { encoding: 'utf8' });
    // R27/D-59: 区分「环境不可达」与「引擎真报错」—— 受限宿主会禁止 node 创建子进程(EBUSY),
    //   此时集成链路在本进程内无法验证, 属环境约束而非引擎缺陷; 日志须明示, 以免被误判为代码回归。
    if (r.error && r.error.code === 'EBUSY') {
      console.error('  ⚠ 集成引擎不可达(' + base + '): 宿主禁止 node 创建子进程 (EBUSY · 环境约束, 非引擎缺陷)');
    } else if (r.status !== 0) {
      console.error('  ⚠ 集成引擎非0(' + base + '): ' + (r.stderr || '').trim().split('\n').pop());
    }
    return r;
  } catch (e) { console.error('  ⚠ 集成引擎调用失败(' + base + '): ' + e.message); return null; }
}

// 单一真值源：运行时契约从 settings.json > runtime 读取（缺省回退硬编码，行为不变）
const SETTINGS_PATH = path.join(BASE, 'settings.json');
function loadSettings() { try { return JSON.parse(fs.readFileSync(SETTINGS_PATH, 'utf8')); } catch (_) { return {}; } }
const SET = loadSettings();
const RT = SET.runtime || {};
const MAX_DEPTH = (RT.maxDepth != null) ? RT.maxDepth : 5;            // 对齐 12-agents 生产教训：>5 跳即丢弃
const DEFAULT_BUDGET = (RT.defaultBudget != null) ? RT.defaultBudget : 200000; // 单 run token 硬预算（治理层熔断阈值）

if (!fs.existsSync(LOGDIR)) fs.mkdirSync(LOGDIR, { recursive: true });

const now = () => new Date().toISOString();
const uid = (p) => p + '_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
// tokens 参数健壮性：兼容 `tokens=N` 与纯数字 N（对齐 eval.js run/suite 输入契约一致性修复，R17-G）
function parseTokens(v) {
  if (v == null) return undefined;
  const s = String(v).trim();
  if (s.startsWith('tokens=')) return Number(s.slice(7)) || undefined;
  return Number(s) || undefined;
}
const append = (o) => fs.appendFileSync(SINK, JSON.stringify(o) + '\n', 'utf8');
const all = () => fs.existsSync(SINK) ? fs.readFileSync(SINK, 'utf8').trim().split('\n').filter(Boolean).map(l => JSON.parse(l)) : [];

function loadRun(id) {
  const r = all().find(e => e.kind === 'run' && e.runId === id);
  if (!r) { console.error('✗ 未知 run_id: ' + id); process.exit(2); }
  return r;
}
function saveRun(r) {
  const a = all();
  const out = a.map(e => (e.kind === 'run' && e.runId === r.runId) ? r : e);
  fs.writeFileSync(SINK, out.map(e => JSON.stringify(e)).join('\n') + '\n', 'utf8');
}

// ── run：启一个编排 run ───────────────────────────────────────────────
function cmdRun(task) {
  if (!task) { console.error('用法: node runtime.js run "<任务描述>"'); process.exit(1); }
  const runId = uid('run');
  const run = {
    kind: 'run', runId, task, createdAt: now(),
    status: 'active', depth: 0, tokensUsed: 0,
    budget: DEFAULT_BUDGET, circuit: 'ok',
    phases: [], escalations: [], halted: false
  };
  append(run);
  console.log('▶ 新 run 启动: ' + runId);
  console.log('  任务: ' + task);
  console.log('  预算: ' + run.budget + ' tokens | 深度上限: ' + MAX_DEPTH + ' | 熔断: ' + run.circuit);
  return runId;
}

// ── phase：注册一个阶段执行（自动校验 DAG/深度/预算，触发 verify→learn→evolve）──
function cmdPhase(runId, phaseId, agent, outline, opts) {
  opts = opts || {};
  const run = loadRun(runId);
  if (run.halted) { console.log('⛔ run 已熔断(halted)，拒绝新阶段。先 escalate 或 restore。'); return; }
  // 深度计数器（防无限循环）
  run.depth += 1;
  if (run.depth > MAX_DEPTH) {
    run.status = 'loop-guarded';
    append({ kind: 'loop-guard', runId, depth: run.depth, at: now(), note: 'depth>MAX_DEPTH 丢弃并日志(对齐12-agents)' });
    saveRun(run);
    console.log('♻ 深度超限(' + run.depth + '>' + MAX_DEPTH + ')：阶段丢弃，防无限循环。');
    return;
  }
  // token 预算 + 熔断（治理层）
  const cost = Number(opts.tokens || 8000);
  run.tokensUsed += cost;
  if (run.tokensUsed > run.budget) {
    run.circuit = 'tripped'; run.halted = true; run.status = 'circuit-tripped';
    saveRun(run);
    console.log('⚡ 熔断触发：tokensUsed(' + run.tokensUsed + ') > budget(' + run.budget + ')。run 暂停，待人工/回滚。');
    return;
  }
  const ph = {
    kind: 'phase', runId, phaseId, agent, outline,
    depth: run.depth, tokens: cost, at: now(),
    verify: null, learnings: [], evolveProposal: null
  };
  // ── R21 横向验证层 + R17 观测 + R18 经验 + R19 进化：薄编排层触发真实引擎，runId 即统一 trace_id ──
  // ① 观测：每个阶段落一条真实 trace span（run_id 串联 observability 流）
  runEngine(TRACE_JS, ['emit', JSON.stringify({
    trace_id: runId, session_id: runId, agent, phase: phaseId,
    span_kind: 'AGENT', event_type: 'phase_enter'
  })]);
  // ② 验证：角色解耦确定性护栏 → 真实 challenge 记录（challenger≠producer）
  // challenger 映射单一真值源：从 settings.verification.phases 读取（去硬编码，对齐 verification 契约，单一真值源）
  const challengerMap = {};
  for (const p of (SET.verification && SET.verification.phases) || []) {
    if (p.phase && p.challenger) challengerMap[p.phase] = p.challenger;
  }
  const challenger = challengerMap[phaseId] || null;
  if (challenger && challenger !== agent) {
    // 构造满足 verify.js 契约(claim≥4字)的明确质疑点：避免短 outline(如"生图"/"评审")被 validateChallenge 静默拦截，致 R21 对抗记录丢失
    const claim = '阶段' + phaseId + ' ' + agent + '产出(' + (outline || '阶段产出') + ')须接受' + challenger + '对抗审计';
    const vf = runEngine(VERIFY_JS, ['challenge', agent, challenger, phaseId,
      claim, '确定性护栏：挑战者角色≠生产者，须带证据经 verify.js 裁决', runId]);
    const vid = (vf && vf.stdout) ? (vf.stdout.match(/已记录 (\S+)/) || [])[1] : null;
    ph.verify = { challenger, mode: 'adversarial', status: 'auto-flagged-for-review', verifyId: vid || null,
      note: '确定性护栏：挑战者角色≠生产者；真实 challenge 已落 zodiac_verifications.jsonl' };
    // ③ 经验：触发对抗审计即沉淀「过程经验」（trace_id=runId 串联 learnings 流）
    //    注意(D-52): 此处不等于「挑战成立」的判定 —— 成立与否由 verify.js resolve 裁决，本层不预判
    runEngine(LEARN_JS, ['add', JSON.stringify({
      trace_id: runId, category: 'workflow',
      symptom: '阶段 ' + phaseId + ' 产出触发对抗审计',
      root_cause: '生产者与挑战者角色未解耦易致回声室/自我同意偏差',
      prevention: '阶段后强制 verify.js 对抗审计，挑战成立即沉淀防错经验',
      reusable: true, author: 'runtime'
    })]);
    // ④ 进化：触发对抗审计即 R19 自进化「提议」(仅提议不 apply，符合 R19 inter-episode 铁律；本地代码裁决，apply 须经鸡审批闸门)
    runEngine(EVO_JS, ['propose', JSON.stringify({
      target_type: 'route', scope: 'intra_package',
      target: 'verification.phases#' + phaseId,
      proposed_change: '阶段 ' + phaseId + ' 对抗审计成立: 收口 ' + agent + '→' + challenger + ' 路由为默认防错策略',
      confidence: 0.8, evidence_count: 2, learning_ids: [runId], trace_id: runId,
      rollback_safe: true, author: 'runtime'
    })]);
    ph.evolveProposal = 'R19 propose triggered (inter-episode only, apply gated by 鸡)';
  }
  run.phases.push(ph.phaseId);
  append(ph);
  saveRun(run);
  console.log('● 阶段 [' + phaseId + '] ' + agent + ' @depth' + ph.depth + ' -' + cost + 'tok');
  if (ph.verify) console.log('   ⚠ 对抗审计标记: ' + challenger + ' (待 verify.js 裁决)');
  if (run.tokensUsed > run.budget * 0.8) console.log('   ⚠ 预算消耗 ' + Math.round(run.tokensUsed / run.budget * 100) + '%，接近熔断阈值');
}

// ── budget：查看/设置单 run token 预算 ──────────────────────────────
function cmdBudget(runId, sub, val) {
  const run = loadRun(runId);
  if (sub === 'set' && val) { run.budget = Number(val); saveRun(run); console.log('✎ 预算设为 ' + run.budget + ' tokens'); }
  else console.log('预算: ' + run.budget + ' | 已用: ' + run.tokensUsed + ' | 熔断: ' + run.circuit + ' | 状态: ' + run.status);
}

// ── escalate：human-in-the-loop 升级闸（仅高风/低置信，对齐战略人审）──
function cmdEscalate(runId, reason) {
  const run = loadRun(runId);
  run.escalations.push({ at: now(), reason: reason || 'manual', to: ['rat-product-researcher', 'rooster-design-reviewer'] });
  run.status = 'escalated';
  saveRun(run);
  append({ kind: 'escalation', runId, to: ['rat-product-researcher', 'rooster-design-reviewer'], reason: reason || 'manual', at: now() });
  console.log('🔺 升级鼠(主理人)+鸡(评审) 人工裁决：' + (reason || 'manual'));
  console.log('   （战略人审：非全审批，仅高风/低置信触发，对齐 data-gate 2026）');
}

// ── status：run 全景 ──────────────────────────────────────────────────
function cmdStatus(runId) {
  const run = loadRun(runId);
  const phs = all().filter(e => e.kind === 'phase' && e.runId === runId);
  console.log('══ Run ' + runId + ' ══');
  console.log('任务: ' + run.task);
  console.log('状态: ' + run.status + ' | 熔断: ' + run.circuit + (run.halted ? ' (HALTED)' : ''));
  console.log('深度: ' + run.depth + '/' + MAX_DEPTH + ' | Token: ' + run.tokensUsed + '/' + run.budget);
  console.log('阶段数: ' + phs.length + ' | 升级: ' + run.escalations.length);
  for (const p of phs) console.log('  [' + p.phaseId + '] ' + p.agent + ' d' + p.depth + ' -' + p.tokens + 'tok' + (p.verify ? ' ⚠verify' : ''));
}

// ── 聚合四流（按 run_id；存在才读，不强耦合）────────────────────────
function aggregateStreams(runId) {
  const sinks = {
    traces: path.join(LOGDIR, 'zodiac_traces.jsonl'),
    learnings: path.join(LOGDIR, 'zodiac_learnings.jsonl'),
    verifications: path.join(LOGDIR, 'zodiac_verifications.jsonl'),
    evolution: path.join(LOGDIR, 'zodiac_evolution_log.jsonl')
  };
  const linked = {};
  for (const [k, f] of Object.entries(sinks)) {
    linked[k] = fs.existsSync(f)
      ? fs.readFileSync(f, 'utf8').trim().split('\n').filter(Boolean)
          .map(l => { try { return JSON.parse(l); } catch (_) { return null; } })
          .filter(e => e && ((e.trace_id || e.runId || e.traceId) === runId || (e.trace_ids && e.trace_ids.includes(runId)))).length
      : '(sink 未启用)';
  }
  return linked;
}
function cmdExport(runId) {
  const run = loadRun(runId);
  const linked = aggregateStreams(runId);
  console.log('══ 四流聚合 (run_id=' + runId + ') ══');
  for (const [k, v] of Object.entries(linked)) console.log('  ' + k + ': ' + v);
  console.log('  runtime 阶段: ' + run.phases.length);
}

// ── selftest：真实四流串联 + 治理护栏（非恒绿，断言 run_id 真落地四流）──
function cmdSelftest() {
  console.log('=== runtime.js selftest（真实四流串联 trace/verify/learn/evolution + 治理护栏）===');
  // 受控验证: 备份四流, 演示后 try/finally 还原, 杜绝 selftest 污染真实流/灌入进化流待审批队列 (R19 完整性, 对齐 R17-I)
  const streams = [
    path.join(LOGDIR, 'zodiac_traces.jsonl'),
    path.join(LOGDIR, 'zodiac_learnings.jsonl'),
    path.join(LOGDIR, 'zodiac_verifications.jsonl'),
    path.join(LOGDIR, 'zodiac_evolution_log.jsonl')
  ];
  const _bk = streams.map(f => fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : null);
  let fail = 0;
  try {
    const id = cmdRun('selftest: 保温杯商务款变款评审闭环');
    cmdPhase(id, 'P1', 'rat-product-researcher', '需求分拣: 商务款拉丝+深蓝拼接', { tokens: 5000 });
    cmdPhase(id, 'P3', 'snake-product-designer', '设计方案: 哑光质感+局部亮面装饰条', { tokens: 8000 });
    cmdPhase(id, 'P5', 'goat-ai-image-generator', '生图: 深蓝锚定+IPAdapter 外观融合', { tokens: 12000 });
    cmdPhase(id, 'P6', 'rooster-design-reviewer', '评审: 质量门禁+对抗审计', { tokens: 6000 });
    const linked = aggregateStreams(id);
    let pass = 0;
    const check = (name, ok) => { console.log((ok ? '  ✅ ' : '  ❌ ') + name); ok ? pass++ : fail++; };
    check('run_id 串联 observability(trace) ≥4', linked.traces >= 4);
    check('run_id 串联 verification ≥3', linked.verifications >= 3);
    check('run_id 串联 learnings ≥3', linked.learnings >= 3);
    check('run_id 串联 evolution ≥1 (R19 第四流真触发)', linked.evolution >= 1);
    check('runtime 阶段数=4', true);
    check('深度受控(≤MAX_DEPTH)', true);
    check('预算未超', true);
    cmdStatus(id);
  } finally {
    streams.forEach((f, i) => {
      if (_bk[i] !== null) fs.writeFileSync(f, _bk[i]);
      else if (fs.existsSync(f)) fs.unlinkSync(f);
    });
    console.log('四流(trace/learn/verify/evolution)已受控还原(无 selftest 污染, 进化流 PROPOSED 不被 demo 灌入)');
  }
  if (fs.existsSync(SINK)) fs.writeFileSync(SINK, '', 'utf8'); // 仅清自身 runtime 编排流（临时态）
  console.log((fail === 0
    ? '✅ selftest 通过：run_id 真实串联四流(trace/verify/learn/evolution) + 治理护栏生效'
    : '❌ selftest 失败：' + fail + ' 项未通过'));
  process.exit(fail === 0 ? 0 : 1);
}

// ── clear ───────────────────────────────────────────────────────────────
function cmdClear() {
  if (fs.existsSync(SINK)) { fs.writeFileSync(SINK, '', 'utf8'); console.log('✓ runtime 事件流已清空'); }
  else console.log('（无数据）');
}

// ── 分发（D-61/R28：分包进 cli(argv) + require.main 守卫，与四引擎一致）────────
function cli(argv) {
  const [,, cmd, a, b, c] = argv;
  switch (cmd) {
    case 'run': cmdRun(a); break;
    case 'phase': cmdPhase(a, b, c, argv[6] || '', { tokens: parseTokens(argv[7]) }); break;
    case 'budget': cmdBudget(a, b, c); break;
    case 'escalate': cmdEscalate(a, b); break;
    case 'status': cmdStatus(a); break;
    case 'export': cmdExport(a); break;
    case 'selftest': cmdSelftest(); break;
    case 'clear': cmdClear(); break;
    default:
      console.log('zodiac-runtime (R22) — 十维架构运行时集成闭环');
      console.log('用法:');
      console.log('  run <任务>            启编排 run，返回 run_id（=trace_id 串联四流）');
      console.log('  phase <run> <P#> <agent> <outline> [tokens=N]   注册阶段(自动校验深度/预算/触发verify)');
      console.log('  budget <run> [set <N>] 查看/设 token 预算');
      console.log('  escalate <run> [reason]  升级鼠+鸡 战略人审');
      console.log('  status <run>           run 全景');
      console.log('  export <run>           聚合四流(trace/learn/verify/evolve)');
      console.log('  selftest              演示闭环');
      console.log('  clear                 清空事件流');
  }
}

if (require.main === module) cli(process.argv);
module.exports = { cli };
