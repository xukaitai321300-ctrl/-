#!/usr/bin/env node
/*
 * learn.js — 生肖团经验反思闭环（Learning Loop）引擎
 * 对齐业界：Reflexion（复盘纠错）/ FORGE（失败轨迹→可复用规则）/ 记忆 3.0 经验反思派
 *         / LangSmith 评估三层（span/trace/thread）
 * 与 R17 observability 衔接：每条经验绑定 trace_id（观测事件流的 run_id），
 *   形成 观测(run) → 复盘 → 沉淀(learning) → 复用 的闭环。
 *
 * 铁律：每次沉淀前必须已有对应 trace（不盲记）；经验流被 recovery 快照覆盖（可恢复）。
 *
 * 用法：
 *   node learn.js add '<json>'        # 沉淀一条经验（JSON 字符串，见 docs/LEARNING_LOOP.md 契约）
 *   node learn.js query [--cat X] [--kw Y]   # 按类别/关键词过滤
 *   node learn.js stats               # 按类别分布统计
 *   node learn.js export [--cat X]    # 导出（默认全量）
 *   node learn.js selftest            # 自检：渲染闭环演示后清空
 *   node learn.js clear               # 清空演示数据（生产态慎用）
 */
const fs = require('fs');
const path = require('path');

// R221r2/R8b（E-D57 防再现）：路径根从 __dirname 派生，禁硬编码 marketplaces 相对拼装
//   （旧值指向迁移前 experts 落点 ⇒ 跨包读写，包再迁移即静默写错处）
const ZODIAC = path.join(__dirname, '..');
const LOGS = path.join(ZODIAC, 'logs');
const FILE = path.join(LOGS, 'zodiac_learnings.jsonl');

// 单一真值源：经验契约从 settings.json > learnings 读取（缺省回退硬编码，行为不变）
const SETTINGS_PATH = path.join(ZODIAC, 'settings.json');
function loadSettings() { try { return JSON.parse(fs.readFileSync(SETTINGS_PATH, 'utf8')); } catch (_) { return {}; } }
const SET = loadSettings();
const LEARN = SET.learnings || {};
const CATEGORIES = (LEARN.categories && LEARN.categories.length) ? LEARN.categories : ['prompt-injection','param-tuning','workflow','tooling','eval','design','coordination'];
const REQUIRED = (LEARN.requiredFields && LEARN.requiredFields.length) ? LEARN.requiredFields : ['trace_id','category','symptom','root_cause','prevention','reusable','author'];

function ensure() {
  if (!fs.existsSync(LOGS)) fs.mkdirSync(LOGS, { recursive: true });
  if (!fs.existsSync(FILE)) fs.writeFileSync(FILE, '');
}
function readAll() {
  ensure();
  const txt = fs.readFileSync(FILE, 'utf8').trim();
  if (!txt) return [];
  return txt.split('\n').filter(Boolean).map(l => {
    try { return JSON.parse(l); } catch { return null; }
  }).filter(Boolean);
}
function append(obj) {
  ensure();
  fs.appendFileSync(FILE, JSON.stringify(obj) + '\n');
}
function nowISO() { return new Date().toISOString(); }

function add(argv) {
  const raw = argv[0];
  if (!raw) { console.log('❌ add 需传 JSON 字符串参数'); process.exit(1); }
  let obj;
  try { obj = JSON.parse(raw); } catch (e) { console.log('❌ JSON 解析失败:', e.message); process.exit(1); }
  obj.ts = obj.ts || nowISO(); // 契约要求 ts：调用方未传则自动加盖（须在必填校验前）
  const missing = REQUIRED.filter(k => !obj[k]);
  if (missing.length) { console.log('❌ 缺必填字段:', missing.join(', ')); process.exit(1); }
  if (!CATEGORIES.includes(obj.category)) {
    console.log('❌ 非法 category（应为', CATEGORIES.join('|') + '）:', obj.category);
    process.exit(1);
  }
  obj.ts = nowISO();
  obj.schemaVersion = 'reflexion-1.0';
  // D-53: 经验获得「可引用身份」——此前 learnings 记录无 id，致 evolve 的 learning_ids 只能填 run_id(trace_id) 充数。
  //       纯增量：旧记录无 id 仍可正常读取/检索，向后兼容。
  obj.id = obj.id || ('lrn_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 5));
  append(obj);
  console.log('✅ 已沉淀经验 | id=' + obj.id + ' | trace_id=' + obj.trace_id + ' | category=' + obj.category + ' | reusable=' + (obj.reusable ? 'Y' : 'N'));
}

function query(argv) {
  const items = readAll();
  let cat = null, kw = null;
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--cat') cat = argv[++i];
    if (argv[i] === '--kw') kw = argv[++i];
  }
  let out = items;
  if (cat) out = out.filter(x => x.category === cat);
  if (kw) {
    const re = new RegExp(kw, 'i');
    out = out.filter(x => (x.symptom + ' ' + x.root_cause + ' ' + x.prevention).match(re));
  }
  console.log('匹配 ' + out.length + ' 条经验' + (cat ? ' [cat=' + cat + ']' : '') + (kw ? ' [kw=' + kw + ']' : ''));
  out.forEach((x, i) => {
    console.log(`  ${i + 1}. [${x.category}] ${x.symptom.slice(0, 48)}`);
    console.log(`     └ 根因: ${x.root_cause.slice(0, 64)}`);
    console.log(`     └ 防再现: ${x.prevention.slice(0, 64)} | reusable=${x.reusable ? 'Y' : 'N'} | trace=${x.trace_id}`);
  });
}

function stats() {
  const items = readAll();
  const byCat = {};
  let reusable = 0;
  for (const x of items) {
    byCat[x.category] = (byCat[x.category] || 0) + 1;
    if (x.reusable) reusable++;
  }
  console.log('总经验=' + items.length + ' | 可复用=' + reusable + ' (' + (items.length ? Math.round(reusable / items.length * 100) : 0) + '%)');
  CATEGORIES.forEach(c => {
    const n = byCat[c] || 0;
    const bar = '#'.repeat(Math.min(n, 30));
    console.log(`  ${c.padEnd(16)} ${String(n).padStart(3)} ${bar}`);
  });
}

function exportAll(argv) {
  const items = readAll();
  let cat = null;
  for (let i = 0; i < argv.length; i++) if (argv[i] === '--cat') cat = argv[++i];
  const out = cat ? items.filter(x => x.category === cat) : items;
  console.log(JSON.stringify(out, null, 2));
}

function clear() {
  ensure();
  fs.writeFileSync(FILE, '');
  console.log('🧹 已清空经验流（生产态慎用）');
}

function selftest() {
  console.log('=== learn.js selftest ===');
  // 受控验证: 备份真实经验流, 演示后 try/finally 还原, 避免 demo 污染 + 杜绝 clear() 全清丢库风险 (R19 完整性)
  const _bk = fs.existsSync(FILE) ? fs.readFileSync(FILE, 'utf8') : '';
  try {
    const demo = [
      {
        trace_id: 'run_selftest_001', category: 'param-tuning',
        symptom: '保温杯出图全灰，无产品轮廓',
        root_cause: 'prompt 首位 stainless steel 占 CLIP 最高注意力→SDXL 认产品灰',
        prevention: '三重蓝锚：材质染蓝+头部蓝前缀+尾部颜色锁 NOT gray',
        reusable: true, author: 'monkey'
      },
      {
        trace_id: 'run_selftest_002', category: 'tooling',
        symptom: '单文件 HTML 改完整段静默失效',
        root_cause: '脚本任一处语法错→整段 <script> 静默失效',
        prevention: '每次改完必 node --check 抽脚本校验',
        reusable: true, author: 'rat'
      },
      {
        trace_id: 'run_selftest_003', category: 'workflow',
        symptom: 'Edit 误判 workflowDeps 收尾边界，首次未命中',
        root_cause: '漏读 phases 数组闭合行 `    ]`',
        prevention: 'Edit 前必须 Read 实机确认精确字节边界',
        reusable: true, author: 'rat'
      }
    ];
    demo.forEach(d => {
      d.ts = nowISO(); d.schemaVersion = 'reflexion-1.0'; append(d);
    });
    console.log('--- 已注入 3 条演示经验 ---');
    stats();
    console.log('--- 按类别查询(=workflow) ---');
    query(['--cat', 'workflow']);
    console.log('--- 闭环演示：观测(run_selftest_003) → 复盘 → 沉淀(workflow) → 可检索复用 ✅ ---');
  } finally {
    fs.writeFileSync(FILE, _bk); // 无论演示是否抛错, 真实经验流必还原(不丢生产经验)
    console.log('真实经验流已受控还原(无演示污染, 不丢生产经验)');
  }
}

// D-61(R28): 模块化(同 trace.js) —— runtime 可在同进程内直调, 规避受限宿主 EBUSY。逻辑零改动。
function cli(argv) {
  const cmd = argv[2];
  const args = argv.slice(3);
  switch (cmd) {
    case 'add': add(args); break;
    case 'query': query(args); break;
    case 'stats': stats(); break;
    case 'export': exportAll(args); break;
    case 'selftest': selftest(); break;
    case 'clear': clear(); break;
    default:
      console.log('用法: node learn.js <add|query|stats|export|selftest|clear>');
      process.exit(1);
  }
}

if (require.main === module) cli(process.argv);
module.exports = { cli, add };
