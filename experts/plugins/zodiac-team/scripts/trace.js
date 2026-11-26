#!/usr/bin/env node
/**
 * trace.js — 生肖团运行态可观测性引擎（最小化可用栈）
 *
 * 对齐 OpenTelemetry GenAI Semantic Conventions + AgentOps span 模型。
 * 主机运行时接入 tracing hook 前，以「结构化事件流(JSONL)」落地三保证：
 *   - 能串：trace_id + session_id 串联一次任务全链路
 *   - 能聚合：agent / phase / event_type / status 可分组统计
 *   - 能回放：必要上下文脱敏后重建（决策依据、工具摘要、prompt 版本）
 *
 * 契约（事件字段/类型）来自 settings.json > observability，文档见
 *   zodiac-team/docs/OBSERVABILITY.md
 * 事件流落在 zodiac-team/logs/zodiac_traces.jsonl，被 recovery 快照覆盖（可恢复）。
 *
 * 用法：
 *   node trace.js emit <json>                      记录一条事件
 *   node trace.js query [--agent A][--phase P][--type T][--session S][--since ISO]
 *   node trace.js timeline [session_id]             渲染会话时间线/瀑布
 *   node trace.js stats                            全局聚合统计
 *   node trace.js export <session_id>              导出某会话事件(JSON)
 *   node trace.js selftest                        自检（发一条完整多专家会话并渲染）
 *   node trace.js clear                           清空事件流（危险!）
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ZODIAC = path.join(__dirname, '..');  // R221r2/R8a：E-D57 防再现，禁硬编码 marketplaces 绝对路径
const SETTINGS = path.join(ZODIAC, 'settings.json');

function loadSettings() {
  try { return JSON.parse(fs.readFileSync(SETTINGS, 'utf8')); }
  catch (e) { return {}; }
}
const SET = loadSettings();
const OB = SET.observability || {};
const SINK = path.join(ZODIAC, OB.sink || 'logs/zodiac_traces.jsonl');
const TRUNC = OB.truncateChars || 500;
const REQ = OB.requiredFields ||
  ['trace_id', 'session_id', 'ts', 'agent', 'phase', 'span_kind', 'event_type', 'status'];
const EVENT_TYPES = OB.eventTypes || {};

function ensureSink() {
  const dir = path.dirname(SINK);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  if (!fs.existsSync(SINK)) fs.writeFileSync(SINK, '');
}
function nowISO() { return new Date().toISOString(); }
function trunc(s) {
  if (s == null) return s;
  s = String(s);
  return s.length > TRUNC ? s.slice(0, TRUNC) + '…[trunc]' : s;
}
function uid(prefix) {
  return (prefix || '') + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
}

/** 校验并落一条结构化事件 */
function emit(event) {
  ensureSink();
  event.ts = event.ts || nowISO();
  event.span_kind = event.span_kind || 'OPERATION';
  event.status = event.status || 'ok';
  const missing = REQ.filter(f => event[f] == null || event[f] === '');
  if (missing.length) {
    console.error('[trace] 缺失必填字段: ' + missing.join(', '));
    process.exit(1);
  }
  if (EVENT_TYPES[event.event_type] == null) {
    console.error('[trace] 未知 event_type: ' + event.event_type +
      '；合法类型: ' + Object.keys(EVENT_TYPES).join(', '));
    process.exit(1);
  }
  for (const k of ['decision', 'input', 'output', 'attributes', 'note']) {
    if (event[k] != null) event[k] = trunc(event[k]);
  }
  fs.appendFileSync(SINK, JSON.stringify(event) + '\n');
  console.log('[trace] 已记录 ' + event.event_type + ' @' + event.agent + '/' + event.phase);
}

function readAll() {
  if (!fs.existsSync(SINK)) return [];
  return fs.readFileSync(SINK, 'utf8').split('\n').filter(Boolean).map(l => {
    try { return JSON.parse(l); } catch { return null; }
  }).filter(Boolean);
}

function query(opts) {
  let evs = readAll();
  if (opts.agent) evs = evs.filter(e => e.agent === opts.agent);
  if (opts.phase) evs = evs.filter(e => e.phase === opts.phase);
  if (opts.type) evs = evs.filter(e => e.event_type === opts.type);
  if (opts.session) evs = evs.filter(e => e.session_id === opts.session);
  if (opts.since) evs = evs.filter(e => e.ts >= opts.since);
  return evs;
}

function timeline(session) {
  let evs = readAll();
  if (session) evs = evs.filter(e => e.session_id === session);
  const bySess = {};
  for (const e of evs) (bySess[e.session_id] = bySess[e.session_id] || []).push(e);
  for (const sid of Object.keys(bySess)) {
    const list = bySess[sid].sort((a, b) => a.ts < b.ts ? -1 : 1);
    console.log('\n=== 会话 ' + sid + ' (' + list.length + ' 事件) ===');
    let depth = 0;
    for (const e of list) {
      const pad = '  '.repeat(Math.min(depth, 4));
      const dur = e.latency_ms != null ? ' ⏱' + e.latency_ms + 'ms' : '';
      const st = e.status === 'ok' ? '✅' : '❌';
      console.log(pad + st + ' [' + e.event_type + '] ' + e.agent + '/' + e.phase + dur +
        (e.note ? ' — ' + trunc(e.note) : ''));
      if (e.event_type === 'phase_enter') depth++;
      if (e.event_type === 'phase_complete') depth = Math.max(0, depth - 1);
    }
  }
}

function stats() {
  const evs = readAll();
  const byAgent = {}, byType = {};
  let errors = 0, latSum = 0, latN = 0;
  for (const e of evs) {
    byAgent[e.agent] = (byAgent[e.agent] || 0) + 1;
    byType[e.event_type] = (byType[e.event_type] || 0) + 1;
    if (e.status && e.status !== 'ok') errors++;
    if (e.latency_ms != null) { latSum += e.latency_ms; latN++; }
  }
  console.log('总事件=' + evs.length + ' | 错误=' + errors +
    ' | 平均耗时=' + (latN ? Math.round(latSum / latN) : 0) + 'ms');
  console.log('按专家: ' + JSON.stringify(byAgent));
  console.log('按事件: ' + JSON.stringify(byType));
}

function clearSession(sid) {
  if (!fs.existsSync(SINK)) return;
  const lines = fs.readFileSync(SINK, 'utf8').split('\n').filter(Boolean);
  const kept = lines.filter(l => { try { return JSON.parse(l).session_id !== sid; } catch { return true; } });
  fs.writeFileSync(SINK, kept.join('\n') + (kept.length ? '\n' : ''));
  console.log('  已移除 selftest session 事件 ' + (lines.length - kept.length) + ' 条');
}

function selftest() {
  const sid = uid('self_');
  const tid = uid('tr_');
  const phases = [
    ['rat-product-researcher', 'P1'],
    ['tiger-image-collector', 'P2'],
    ['rabbit-image-analyst', 'P2'],
    ['dragon-competitor-analyst', 'P2'],
    ['snake-product-designer', 'P3'],
    ['ox-standards-analyst', 'P4'],
    ['horse-rendering-expert', 'P5'],
    ['goat-ai-image-generator', 'P5'],
    ['monkey-skill-optimizer', 'P5'],
    ['rooster-design-reviewer', 'P6'],
    ['pig-brand-designer', 'P7'],
    ['rat-product-researcher', 'P9'],
  ];
  try {
    emit({ trace_id: tid, session_id: sid, agent: 'rat-product-researcher', phase: 'P1', span_kind: 'SESSION', event_type: 'session_start', status: 'ok', note: '保温杯商务款变款需求' });
    for (const [ag, ph] of phases) {
      emit({ trace_id: tid, session_id: sid, agent: ag, phase: ph, span_kind: 'AGENT', event_type: 'phase_enter', status: 'ok' });
    }
    emit({ trace_id: tid, session_id: sid, agent: 'rooster-design-reviewer', phase: 'P6', span_kind: 'OPERATION', event_type: 'review_gate', status: 'ok', decision: '通过（四维门禁≥8.0）', latency_ms: 1200 });
    emit({ trace_id: tid, session_id: sid, agent: 'rat-product-researcher', phase: 'P9', span_kind: 'OPERATION', event_type: 'session_end', status: 'ok', latency_ms: 84000, tokens_out: 1200, cost_usd: 0.018 });
    console.log('\n--- 自检时间线 ---');
    timeline(sid);
    console.log('\n--- 自检统计 ---');
    stats();
  } finally {
    clearSession(sid);
    console.log('\n真实 trace 流已受控还原(仅移除本次 selftest session, 无污染, 不丢生产事件)');
  }
}

function help() {
  console.log('trace.js — 生肖团运行态可观测性引擎');
  console.log('sink=' + SINK);
  console.log('用法:');
  console.log('  node trace.js emit <json>           记录一条结构化事件');
  console.log('  node trace.js query [--agent A][--phase P][--type T][--session S][--since ISO]');
  console.log('  node trace.js timeline [session_id]  渲染会话时间线/瀑布');
  console.log('  node trace.js stats                 全局聚合统计');
  console.log('  node trace.js export <session_id>   导出某会话事件(JSON)');
  console.log('  node trace.js selftest             自检(发一条完整多专家会话并渲染)');
  console.log('  node trace.js clear                清空事件流(危险!)');
  console.log('事件契约见 docs/OBSERVABILITY.md');
}

// D-61(R28): 模块化 —— 顶层 CLI 分包进 cli(argv) + require.main 守卫,
//   使 runtime 可在【同进程】内直调(受限宿主禁 node 建子进程 → spawnSync 恒 EBUSY → 集成链路无法验证)。
//   逻辑零改动: require.main 时行为与改造前等价。
function cli(argv) {
  const [, , cmd, ...rest] = argv;
  ensureSink();
  switch (cmd) {
    case 'emit': {
      const raw = rest.join(' ');
      let obj;
      try { obj = JSON.parse(raw); }
      catch (e) { console.error('[trace] 参数须为合法JSON: ' + raw); process.exit(1); }
      emit(obj);
      break;
    }
    case 'query': {
      const opts = {};
      for (let i = 0; i < rest.length; i++) {
        if (rest[i] === '--agent') opts.agent = rest[++i];
        else if (rest[i] === '--phase') opts.phase = rest[++i];
        else if (rest[i] === '--type') opts.type = rest[++i];
        else if (rest[i] === '--session') opts.session = rest[++i];
        else if (rest[i] === '--since') opts.since = rest[++i];
      }
      const evs = query(opts);
      console.log('命中 ' + evs.length + ' 条');
      for (const e of evs.slice(0, 50)) console.log(JSON.stringify(e));
      break;
    }
    case 'timeline': timeline(rest[0]); break;
    case 'stats': stats(); break;
    case 'export': {
      const evs = query({ session: rest[0] });
      console.log(JSON.stringify(evs, null, 2));
      break;
    }
    case 'selftest': selftest(); break;
    case 'clear': fs.writeFileSync(SINK, ''); console.log('[trace] 已清空事件流'); break;
    default: help();
  }
}

if (require.main === module) cli(process.argv);
module.exports = { cli, emit };
