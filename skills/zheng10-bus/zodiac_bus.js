#!/usr/bin/env node
// zheng10-bus · 生肖团通用互通总线 (全12角色共享产出池 + 静态联动映射 + inbox 事件触发)
//
// 职责:
//   1) --emit   : 角色完成产出 → 写 <日志目录>/zodiac_bus.jsonl (共享产出池)
//                并按 <日志目录>/zodiac_bus_map.json 给下游角色 append inbox (事件触发, 非轮询)
//                <日志目录> 由 resolveLogDir() 三级回退决定 (环境变量 > ~/.workbuddy/zodiac-bus-logs > 兜底旧位置)
//   2) --map    : 查某角色 emit 后会触发哪些下游 (秒级路由, 替代 LLM 临场推理)
//   3) --inbox  : 读某角色信箱 (下游秒级得通知)
//   4) --pending: 列出未处理事件
//   5) --mark-done: 标记信箱事件已处理
//   6) --pool   : 按 ref 查池 (互通去重)
//
// 设计呼应 vision-core 成功模式: 单一真相源脚本 + append-only 池 + 确定性路由。
// 与 vision-core 关系: 视觉4角经 vision-core 看图, 其结论也 --emit 到本总线(ref=image_hash)。

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { spawnSync } = require('child_process');

// 🔴 2026-10-23 架构深度审计 ⑨（结构自包含）：原为硬编码 '<架构根目录>/logs'
//    ⇒ 换机/迁项目即失效（违反 zodiac-architecture-audit ⑨「结构自包含」）
//    ⇒ 改为：环境变量 > 相对本文件 > 旧硬编码 三级回退（三处都给 ⇒ 不破坏现有行为）
function resolveLogDir(){
  const cands = [];
  if (process.env.ZODIAC_BUS_LOG_DIR) cands.push(process.env.ZODIAC_BUS_LOG_DIR);
  // 本文件位于 <skills>/zheng10-bus/ ⇒ 上溯到 .workbuddy，再上溯到用户目录
  try {
    const userDir = path.join(__dirname, '..', '..');          // ~/.workbuddy
    cands.push(path.join(userDir, 'zodiac-bus-logs'));         // 首选：与技能同级
    cands.push(path.join(userDir, 'logs'));                     // 次选：~/.workbuddy/logs
  } catch(e) {}
  cands.push(path.join(__dirname, '..', '..', 'logs'));          // 兜底：相对旧位置（保持兼容）
  for (const c of cands) {
    try { if (fs.existsSync(c) && fs.statSync(c).isDirectory()) return c; } catch(e) {}
  }
  // 全都不存在 ⇒ 返回首选（后面会 mkdir）
  return cands[0] || cands[cands.length-1];
}
const LOG_DIR = resolveLogDir();
const BUS = path.join(LOG_DIR, 'zodiac_bus.jsonl');
const MAP = path.join(LOG_DIR, 'zodiac_bus_map.json');
const INBOX_DIR = path.join(LOG_DIR, 'inbox');

// R32 · 2026-09-25：架构由 12 生肖扩至 14 角色（新增 dragon2 产品设计调整 / phoenix 自主进化协调器）
const VALID_ROLES = ['rat','ox','tiger','rabbit','dragon','dragon2','snake','horse','sheep','monkey','rooster','dog','pig','phoenix','zodiac','triz','tooling']; // R40·2026-11-05 map 扩容同步：+zodiac(主理人)/triz(TRIZ)/tooling(工具集)

function parseArgs(argv){
  const a = { mode:null, role:null, type:null, product:null, ref:null,
              content:null, contentFile:null, pendingOnly:false, id:null,
              map:false, inbox:false, pending:false, markDone:false, pool:false, selftest:false };
  for(let i=2;i<argv.length;i++){
    const k = argv[i];
    if(k==='--emit') a.mode='emit';
    else if(k==='--map') a.map = true;
    else if(k==='--inbox') a.inbox = true;
    else if(k==='--pending') a.pending = true;
    else if(k==='--mark-done') a.markDone = true;
    else if(k==='--pool') a.pool = true;
    else if(k==='--selftest') a.selftest = true;
    else if(k==='--role') a.role = argv[++i];
    else if(k==='--type') a.type = argv[++i];
    else if(k==='--product') a.product = argv[++i];
    else if(k==='--ref') a.ref = argv[++i];
    else if(k==='--content') a.content = argv[++i];
    else if(k==='--content-file') a.contentFile = argv[++i];
    else if(k==='--pending-only') a.pendingOnly = true;
    else if(k==='--id') a.id = argv[++i];
  }
  return a;
}

function loadMap(){
  if(!fs.existsSync(MAP)) return { edges:{} };
  try{ return JSON.parse(fs.readFileSync(MAP,'utf8')); }
  catch(_){ return { edges:{} }; }
}

function genId(){
  return 'evt_' + Date.now().toString(36) + '_' + crypto.randomBytes(2).toString('hex');
}

function appendJsonl(file, obj){
  if(!fs.existsSync(path.dirname(file))) fs.mkdirSync(path.dirname(file), {recursive:true});
  fs.appendFileSync(file, JSON.stringify(obj)+'\n');
}

function readJsonl(file){
  if(!fs.existsSync(file)) return [];
  return fs.readFileSync(file,'utf8').split('\n').filter(Boolean).map(ln=>{
    try{ return JSON.parse(ln); }catch(_){ return null; }
  }).filter(Boolean);
}

function summarize(content){
  if(!content) return null;
  if(typeof content==='string'){
    try{ const j = JSON.parse(content); content = j; }catch(_){ return content.slice(0,120); }
  }
  if(content.summary) return String(content.summary).slice(0,160);
  if(content.analysis) return String(content.analysis).slice(0,160);
  if(content.tasks) return 'tasks:'+JSON.stringify(content.tasks).slice(0,120);
  return JSON.stringify(content).slice(0,160);
}

// 静默孤岛告警: 当 role.type 边键未命中 map 且无裸角色键兜底时,
// 事件仍写入产出池但下游为空 —— 此前无提示, 易误判"总线断联"(R8 现场).
// 仅作 stderr 观测告警, 不改变数据流(下游仍为空, 调用方 JSON 输出不变).
function warnSilentIsland(role, text){
  console.error('⚠️ [zodiac-bus] 边键 "' + text + '" 未命中 zodiac_bus_map.json，且无裸角色键 "' + role + '" → 下游为空。');
  console.error('   事件已写入产出池，但没有任何下游角色收到通知（静默孤岛）。');
  console.error('   请核对 --type 是否精确匹配 map 边键（如 rabbit.analyze / sheep.render）。参考: <LOG_DIR>/zodiac_bus_map.json');
}

// ---- 核心: emit ----
function doEmit(A){
  if(!A.role || !VALID_ROLES.includes(A.role)){ console.error('❌ --role 必填且∈ '+VALID_ROLES.join('/')); process.exit(1); }
  if(!A.type){ console.error('❌ --emit 需要 --type'); process.exit(1); }
  let payload = null;
  if(A.contentFile){ payload = fs.readFileSync(A.contentFile,'utf8'); }
  else if(A.content){ payload = A.content; }
  else { payload = '{}'; }

  const evtId = genId();
  const rec = {
    id: evtId,
    ts: new Date().toISOString(),
    role: A.role,
    type: A.type,
    product: A.product || null,
    ref: A.ref || null,
    content: (()=>{ try{ return JSON.parse(payload); }catch(_){ return payload; } })(),
    version: 1
  };
  if(!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR, {recursive:true});
  appendJsonl(BUS, rec);

  // 按映射表给下游 append inbox (事件触发)
  const map = loadMap();
  const key = A.role + '.' + A.type;
  const keyHit = map.edges && map.edges[key];
  const roleHit = map.edges && map.edges[A.role];
  if(!keyHit && !roleHit){
    warnSilentIsland(A.role, key);
  }
  let downstream = keyHit ? keyHit : (roleHit || []);
  downstream = Array.from(new Set(downstream.filter(r=>VALID_ROLES.includes(r) && r!==A.role)));

  let notified = [];
  const summary = summarize(rec.content);
  for(const d of downstream){
    const inboxFile = path.join(INBOX_DIR, d + '.jsonl');
    // 去重: 同 (from,to,ref,type) 已 pending 则跳过
    const existing = readJsonl(inboxFile);
    const dup = existing.find(e=> e.from===A.role && e.role===d && e.ref===A.ref && e.type===A.type && e.status==='pending');
    if(dup) continue;
    const evt = {
      id: genId(),
      ts: rec.ts,
      from: A.role,
      type: A.type,
      role: d,            // recipient
      ref: A.ref || null,
      payload_ref: evtId, // 指向 bus 池记录
      status: 'pending',
      content_summary: summary
    };
    appendJsonl(inboxFile, evt);
    notified.push(d);
  }

  const result = { ok:true, event_id:evtId, notified, downstream };
  console.log(JSON.stringify(result, null, 2));
}

function doMap(A){
  if(!A.role){ console.error('❌ --map 需要 --role'); process.exit(1); }
  const map = loadMap();
  const key = (A.type) ? A.role+'.'+A.type : null;
  const viaKey = key && map.edges ? (map.edges[key]||[]) : [];
  const viaRole = map.edges ? (map.edges[A.role]||[]) : [];
  if(A.type && !viaKey.length && !viaRole.length){
    warnSilentIsland(A.role, key);
  }
  const merged = Array.from(new Set([...viaKey, ...viaRole]));
  console.log(JSON.stringify({ role:A.role, type:A.type||null, downstream:merged }, null, 2));
}

function doInbox(A){
  if(!A.role){ console.error('❌ --inbox 需要 --role'); process.exit(1); }
  const f = path.join(INBOX_DIR, A.role + '.jsonl');
  let items = readJsonl(f);
  if(A.pendingOnly) items = items.filter(e=>e.status==='pending');
  console.log(JSON.stringify(items, null, 2));
}

function doPending(A){
  const roles = A.role ? [A.role] : VALID_ROLES;
  const out = [];
  for(const r of roles){
    const f = path.join(INBOX_DIR, r + '.jsonl');
    const items = readJsonl(f).filter(e=>e.status==='pending');
    for(const it of items) out.push({ recipient:r, ...it });
  }
  console.log(JSON.stringify(out, null, 2));
}

function doMarkDone(A){
  if(!A.role || !A.id){ console.error('❌ --mark-done 需要 --role --id'); process.exit(1); }
  const f = path.join(INBOX_DIR, A.role + '.jsonl');
  if(!fs.existsSync(f)){ console.error('❌ 信箱不存在'); process.exit(1); }
  const items = readJsonl(f);
  let found = false;
  for(const it of items){ if(it.id===A.id){ it.status='done'; found=true; } }
  fs.writeFileSync(f, items.map(i=>JSON.stringify(i)).join('\n')+'\n');
  console.log(JSON.stringify({ ok:found, role:A.role, id:A.id }));
}

function doPool(A){
  if(!A.ref){ console.error('❌ --pool 需要 --ref'); process.exit(1); }
  const items = readJsonl(BUS).filter(e=>e.ref===A.ref);
  console.log(JSON.stringify(items, null, 2));
}

// ---- R11: map ↔ 12-agent 接线一致性静态校验支撑函数 ----
// 探测 experts 插件目录 (跨环境候选路径, 命中即返回, 否则 null → 优雅降级 SKIP)
function getExpertsDir(){
  // 测试/CI 可经此 env 覆盖目录 (默认不设置则走下方候选)
  if(process.env.ZODIAC_BUS_EXPERTS_DIR && fs.existsSync(process.env.ZODIAC_BUS_EXPERTS_DIR)){
    return process.env.ZODIAC_BUS_EXPERTS_DIR;
  }
  // R32 · 2026-09-25：优先「实际运行层」——宿主注册层 agents/zodiac-team/agents
  //   语义：S3 校验的是「map ↔ 真正会被加载执行的 agent 定义」是否漂移。
  //   市场副本（未注册的 my-experts / experts）降为兜底候选。
  const cands = [
    '~/.workbuddy/agents/zodiac-team/agents',
    path.join(process.env.USERPROFILE||'', '.workbuddy/agents/zodiac-team/agents'),
    '~/.workbuddy/plugins/marketplaces/experts/plugins',
    path.join(process.env.USERPROFILE||'', '.workbuddy/plugins/marketplaces/experts/plugins'),
    path.join(process.env.HOME||'', '.workbuddy/plugins/marketplaces/experts/plugins')
  ];
  for(const c of cands){ if(c && fs.existsSync(c)) return c; }
  return null;
}

// 扫描 agent .md 文件, 提取真实 emit 接线 (role.type 集合), 仅收合法角色避免噪音
function scanAgentEmits(dir){
  const keys = new Set();
  const EMIT_RE = /zodiac_bus\.js\s+--emit[\s\S]*?--role\s+(\w+)\s+--type\s+(\w+)/g;
  function walk(d){
    let ents=[];
    try{ ents = fs.readdirSync(d, {withFileTypes:true}); }catch(_){ return; }
    for(const e of ents){
      const p = path.join(d, e.name);
      if(e.isDirectory()){ walk(p); }
      else if(e.isFile() && e.name.endsWith('.md')){
        const txt = fs.readFileSync(p,'utf8');
        let m; EMIT_RE.lastIndex = 0;
        while((m = EMIT_RE.exec(txt))){
          const role=m[1], type=m[2];
          if(VALID_ROLES.includes(role)) keys.add(role+'.'+type);
        }
      }
    }
  }
  walk(dir);
  return keys;
}

// ---- 自检: 回归守护 R9 静默孤岛告警 + map 一致性 + R11 接线漂移 ----
function runBus(args){
  // R27/D-59: 改「同进程函数调用 + 输出捕获」—— 受限宿主会禁止 node 创建子进程(EBUSY),
  //   原 spawnSync(__filename) 使 T1/T2 三项断言全部假失败(downstream=null / stderr="")。
  //   doMap 直接消费 parseArgs 的产物且无副作用(只读 map + 输出), 故可进程内直调, 无需再起 node。
  const A = parseArgs(['node', 'zodiac_bus.js', ...args]);
  const out = [], errs = [];
  const _log = console.log, _err = console.error;
  console.log = (...a) => out.push(a.map(String).join(' '));
  console.error = (...a) => errs.push(a.map(String).join(' '));
  try {
    if (A.map) doMap(A);
    return { stdout: out.join('\n'), stderr: errs.join('\n'), status: 0 };
  } catch (e) {
    return { stdout: out.join('\n'), stderr: errs.join('\n') + '\n' + e.message, status: 1 };
  } finally {
    console.log = _log;
    console.error = _err;
  }
}

function doSelfTest(){
  let pass=0, fail=0; const log=[];
  function check(name, cond, detail){
    if(cond){ pass++; log.push('  ✅ '+name); }
    else { fail++; log.push('  ❌ '+name+' → '+(detail||'')); }
  }
  const map = loadMap();
  const edgeKeys = Object.keys(map.edges||{});

  // 动态取一条合法边作"正确 type"正例, 避免硬编码
  let posRole=null, posType=null;
  for(const k of edgeKeys){
    const parts=k.split('.');
    if(VALID_ROLES.includes(parts[0]) && parts[1] && (map.edges[k]||[]).length>0){ posRole=parts[0]; posType=parts[1]; break; }
  }
  check('S0 存在合法边键', !!posRole, 'edgeKeys='+edgeKeys.length);

  // T1: 错误 type → 告警触发 + 下游空 (守护 R9)
  const t1 = runBus(['--map','--role',posRole,'--type','___bogus_type___']);
  check('T1 错误type触发静默孤岛告警', /静默孤岛/.test(t1.stderr), 'stderr='+JSON.stringify(t1.stderr));
  let d1=null; try{ d1=JSON.parse(t1.stdout).downstream; }catch(_){}
  check('T1 错误type下游为空', Array.isArray(d1)&&d1.length===0, 'downstream='+JSON.stringify(d1));

  // T2: 正确 type → 不误报 + 下游非空
  const t2 = runBus(['--map','--role',posRole,'--type',posType]);
  check('T2 正确type不误报', !/静默孤岛/.test(t2.stderr), 'stderr='+JSON.stringify(t2.stderr));
  let d2=null; try{ d2=JSON.parse(t2.stdout).downstream; }catch(_){}
  check('T2 正确type下游非空', Array.isArray(d2)&&d2.length>0, 'downstream='+JSON.stringify(d2));

  // T3: map 边键源角色 + 下游目标全部合法
  let bad=[];
  for(const k of edgeKeys){
    const role=k.split('.')[0];
    if(!VALID_ROLES.includes(role)) bad.push(k+'(源角色非法)');
    for(const t of (map.edges[k]||[])) if(!VALID_ROLES.includes(t)) bad.push(k+'→'+t+'(目标非法)');
  }
  check('T3 map边键角色合法', bad.length===0, bad.join('; '));

  // ---- R11/R32: map ↔ 14-agent 接线一致性 (漂移守护) ----
  // S1: 12 角色均作为 emitter 出现
  const srcRoles = new Set(edgeKeys.map(k=>k.split('.')[0]));
  const missingEmitters = VALID_ROLES.filter(r=>!srcRoles.has(r));
  check('S1 '+VALID_ROLES.length+'角色均作为emitter', missingEmitters.length===0, '缺:'+missingEmitters.join(','));

  // S2: 边键数恰等于合法角色数 (每角色一个产出类型, 本系统不变量)
  check('S2 边键数>='+VALID_ROLES.length, edgeKeys.length>=VALID_ROLES.length, 'edges='+edgeKeys.length); // R40·2026-11-05：角色可多产出类型（如 triz.innovate+triz.asset），不变量由「恰等」放宽为「下限」

  // S3: 扫描 agent 文件, 校验 map 与 agent 接线互相对应 (防漂移)
  const expertsDir = getExpertsDir();
  if(expertsDir){
    const actualKeys = scanAgentEmits(expertsDir); // Set<"role.type">
    const noRoute = [...actualKeys].filter(k=>!edgeKeys.includes(k));
    check('S3a agent接线均有map路由', noRoute.length===0, '无路由:'+noRoute.join(','));
    const NON_AGENT_ROLES=['zodiac','triz','tooling']; // R40·2026-11-05：非 agent 层角色，接线不在 agents 目录
    const orphan = edgeKeys.filter(k=>!actualKeys.has(k) && !NON_AGENT_ROLES.includes(k.split('.')[0]));
    check('S3b map无悬空边(均有agent产出)', orphan.length===0, '悬空:'+orphan.join(','));
    log.push('  ℹ️ agent接线数='+actualKeys.size+' / map边键数='+edgeKeys.length+' / expertsDir='+expertsDir);
  } else {
    log.push('  ⏭️ S3 跳过: experts 目录未找到 (非本机环境), 仅校验 map 内部一致性');
  }

  log.push('  ℹ️ map边键数='+edgeKeys.length+' / 合法角色数='+VALID_ROLES.length);
  const ok = fail===0;
  console.log('🧪 zodiac_bus selftest: '+(ok?'ALL PASS ✅':'FAIL ❌')+' ('+pass+' passed, '+fail+' failed)');
  console.log(log.join('\n'));
  process.exit(ok?0:1);
}

// D-61(R28): 模块化 —— main(argv) + require.main 守卫, 供 selftest_all 同进程直调(规避受限宿主 EBUSY)。
function main(argv){
  const A = parseArgs(argv || process.argv);
  if(A.mode==='emit') return doEmit(A);
  if(A.map) return doMap(A);
  if(A.inbox) return doInbox(A);
  if(A.pending) return doPending(A);
  if(A.markDone) return doMarkDone(A);
  if(A.pool) return doPool(A);
  if(A.selftest) return doSelfTest();
  console.log('zheng10-bus 用法: --emit | --map | --inbox | --pending | --mark-done | --pool | --selftest');
}

if (require.main === module) {
  try{ main(process.argv); }
  catch(e){ console.error('❌ zodiac_bus error:', e.message); process.exit(1); }
}
module.exports = { main };
