#!/usr/bin/env node
/**
 * selftest_all —— 生肖团引擎套件统一回归门禁 (R12)
 * ---------------------------------------------------------------------------
 * 把分散在 9 个引擎(trace/learn/evolve/verify/eval/golden-regress/metrics/runtime/recovery)
 * + 总线(zheng10-bus) 的各自 selftest 聚合为「一键跑、聚合判、CI 退出码」的单一入口（10 套件）。
 *
 * 设计要点：
 *   1. 每个 suite 默认【同进程直调】已模块化引擎的 cli/main（D-61：不受「宿主禁 node 建子进程」
 *      约束，免去 10 次 node 冷启）；若入口不可 require（如被 ZODIAC_*_JS 重定向到外部实现）
 *      则走 spawnSync(process.execPath) 兜底
 *      （D-56: 不用 bare 'node'，去 PATH 依赖 + 规避宿主 shim 把 'node' 代理化后 EBUSY）
 *   2. 判定契约（D-60 三态）：子命令 EXIT===0 → ✅PASS；spawn 失败且 EBUSY/EPERM → ⚠️SKIP(环境不可达)；
 *      其余非零 → ❌FAIL。各引擎已遵守「selftest 通过即 EXIT 0」契约；
 *      eval 的 RELEASE BLOCKED 是其 selftest 的预期演示，仍 EXIT 0。
 *   3. 聚合输出：逐 suite 状态行 + 末尾汇总表；退出码 0=全绿 / 1=代码失败 / 2=环境不可达（CI 可区分，不误判）
 *   4. 路径可覆盖：ENGINE_DIR / ZODIAC_BUS_JS 环境变量优先（CI/测试可重定向）
 *   5. 对生产无害：各引擎 selftest 均受控还原（备份+try/finally），演示后零残留，不污染真实流/不灌入进化流待审批队列
 *
 * 用法：node selftest_all.js
 *       ZODIAC_BUS_JS=/tmp/fake.js node selftest_all.js   # 证伪：bus 必报 FAIL
 */
'use strict';
const { spawnSync } = require('child_process');
const path = require('path');
const { invokeInProc, entryOf } = require(path.join(__dirname, 'lib', 'inproc.js'));

const ENGINE_DIR = process.env.ZODIAC_ENGINE_DIR || __dirname;
const BUS_JS = process.env.ZODIAC_BUS_JS ||
  'C:/Users/Administrator/.workbuddy/skills/zheng10-bus/zodiac_bus.js';

// R38: 架构门禁工具目录（可覆盖；默认 SXJG 归档库 tools）
const SXJG_TOOLS = process.env.ZODIAC_SXJG_TOOLS || 'H:/SXJG/01_架构记录/tools';

// D-61(R28): 引擎已模块化(导出 cli/main) → 同进程直调, 不受「宿主禁 node 建子进程(EBUSY)」约束;
//   未模块化(如 bus 属外部技能包, 入口由自身管理) → 子进程兜底 + D-60 三态判定。
//   require 先容错: 加载失败(路径不存在/语法错)则降级子进程, 由子进程如实报错。
function tryLoad(file) { try { return require(file); } catch (_) { return null; } }

// suite 定义：name + 入口文件 + 参数（与各自引擎的 selftest 子命令一一对应）
const SUITES = [
  { name: 'trace',          file: path.join(ENGINE_DIR, 'trace.js'),          args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'trace.js')) },
  { name: 'learn',          file: path.join(ENGINE_DIR, 'learn.js'),          args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'learn.js')) },
  { name: 'evolve',         file: path.join(ENGINE_DIR, 'evolve.js'),         args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'evolve.js')) },
  { name: 'verify',         file: path.join(ENGINE_DIR, 'verify.js'),         args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'verify.js')) },
  { name: 'eval',           file: path.join(ENGINE_DIR, 'eval.js'),           args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'eval.js')) },
  { name: 'golden-regress', file: path.join(ENGINE_DIR, 'golden-regress.js'), args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'golden-regress.js')) },
  { name: 'metrics',        file: path.join(ENGINE_DIR, 'metrics.js'),        args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'metrics.js')) },
  { name: 'runtime',        file: path.join(ENGINE_DIR, 'runtime.js'),        args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'runtime.js')) },
  { name: 'recovery',       file: path.join(ENGINE_DIR, 'recovery.js'),       args: ['selftest'],   mod: tryLoad(path.join(ENGINE_DIR, 'recovery.js')) }, // R29/D-62: 最后一个未模块化引擎补齐
  { name: 'bus',            file: BUS_JS,                                     args: ['--selftest'], mod: tryLoad(BUS_JS) }, // 外部技能包(已模块化)
];

// R38: 第 2 组 —— 架构门禁（文件系统联通稳定性），与「引擎套件」并列。
//   引擎组测「代码逻辑正确性」；架构组测「Junction 链路 / 根级索引 / 哈希基线 / 跨盘镜像 / 活跃层卫生」。
//   语义不同故分组展示，但同属「交付前必须绿」的门禁 → 共用退出码契约。
//   透传 --full：`selftest_all --full` 时架构组跑全库哈希（默认快检，秒级）。
//   目录不存在 → tryLoad 返回 null → 走子进程兜底 → 如实报 FAIL（不静默）。
const ARCH_SUITES = [
  { name: 'arch-gate', file: path.join(SXJG_TOOLS, 'sxjg_arch_gate.js'), args: [], mod: tryLoad(path.join(SXJG_TOOLS, 'sxjg_arch_gate.js')) },
];

const GROUPS = [
  { title: '引擎套件', dir: ENGINE_DIR, suites: SUITES },
  { title: '架构门禁', dir: SXJG_TOOLS, suites: ARCH_SUITES },
];

// D-60(R28): 「环境不可达」与「代码失败」必须分态。
//   历史缺陷: 受限宿主禁 node 建子进程 → 每次 spawnSync 必 EBUSY, 而旧实现一律判 ❌ FAIL,
//   汇总成 0/9 假红灯 —— 恰好违反本文档自定判据「EBUSY 不得记作代码回归, 但也不得静默」。
const ENV_BLOCK_RE = /EBUSY|EPERM|EACCES/;

// D-60: 纯判定单元 —— 把「spawn 结果 → 三态」抽成不依赖真实子进程的函数, 使 FAIL 分支可被单测
//   (受限宿主下所有 spawn 均 EBUSY, FAIL 分支无法端到端触发 → 若不抽出即留下「测不到的盲区」)。
function classifySpawn(res) {
  const spawned = !res.error;                                            // 子进程是否真的起来了
  const envBlocked = !spawned && ENV_BLOCK_RE.test(res.error.message);   // 宿主禁建子进程 → 环境不可达
  const exit = spawned ? (res.status === null ? 1 : res.status) : null;  // null = 超时 / 未起来
  return { ok: spawned && exit === 0, envBlocked, exit };                // 仅「真跑通且 EXIT 0」记 PASS
}

function runSuite(s) {
  // ① 同进程直调（已模块化引擎）—— 不受宿主子进程限制，且省去 9 次 node 冷启
  const entry = entryOf(s.mod);
  if (entry) {
    const r = invokeInProc(entry, ['node', s.file, ...s.args]);
    return { name: s.name, mode: 'inproc', ok: r.status === 0, envBlocked: false,
             exit: r.status, out: r.stdout, crashed: null };
  }
  // ② 子进程兜底（未模块化引擎 / 被 ZODIAC_*_JS 重定向到外部实现）
  // D-56: 用 process.execPath 替代 bare 'node' —— 去除对 PATH 的隐式依赖(CI/精简环境 node 常不在 PATH)
  const res = spawnSync(process.execPath, [s.file, ...s.args], { encoding: 'utf8', timeout: 120000 });
  return {
    name: s.name,
    mode: 'spawn',
    ...classifySpawn(res),
    out: (res.stdout || '') + (res.stderr || ''),
    crashed: res.error ? res.error.message : null,
  };
}

// D-60: 本聚合器自身的判定逻辑自检 —— 纯函数、不 spawn(受限宿主也能跑) → 三态分类与退出码契约可独立取证
function selfTest() {
  console.log('=== selftest_all 判定逻辑自检 (D-60 三态) ===\n');
  let p = 0, f = 0;
  const chk = (good, label) => { console.log('  ' + (good ? '✅' : '❌') + ' ' + label); good ? p++ : f++; };
  const cases = [
    ['真通过 (exit 0)',            { status: 0 },  { ok: true,  envBlocked: false, exit: 0 }],
    ['真失败 (exit 1)',            { status: 1 },  { ok: false, envBlocked: false, exit: 1 }],
    ['超时 (status null)',         { status: null }, { ok: false, envBlocked: false, exit: 1 }],
    ['环境不可达 (EBUSY)',         { error: { message: 'spawnSync node EBUSY' } }, { ok: false, envBlocked: true, exit: null }],
    ['环境不可达 (EPERM)',         { error: { message: 'EPERM: operation not permitted' } }, { ok: false, envBlocked: true, exit: null }],
    ['真失败 (ENOENT 非环境)',     { error: { message: 'spawnSync /nope ENOENT' } }, { ok: false, envBlocked: false, exit: null }],
  ];
  for (const [label, res, w] of cases) {
    const g = classifySpawn(res);
    chk(g.ok === w.ok && g.envBlocked === w.envBlocked && g.exit === w.exit,
      label + '  → ok=' + g.ok + ' envBlocked=' + g.envBlocked + ' exit=' + g.exit);
  }
  const codeOf = (blocked, failed) => failed > 0 ? 1 : (blocked > 0 ? 2 : 0);
  const codeCases = [
    [0, 0, 0, '全绿 → 0'],
    [0, 3, 1, '有代码失败 → 1'],
    [9, 0, 2, '全环境不可达 → 2'],
    [6, 0, 2, '混合(无失败) → 2'],
  ];
  for (const [b, fl, want, label] of codeCases) {
    const g = codeOf(b, fl);
    chk(g === want, '退出码契约: ' + label + '  (blocked=' + b + ', failed=' + fl + ') got=' + g);
  }
  console.log('\n自检结果: ' + p + ' 通过 / ' + f + ' 失败');
  process.exit(f ? 1 : 0);
}

function main() {
  if (process.argv.includes('--selftest')) return selfTest();
  const FULL = process.argv.includes('--full');
  console.log('════════════════════════════════════════════════════════════');
  console.log(' 生肖团 · 双组统一回归门禁 (R12 selftest_all → R38 双组)');
  console.log(' ① 引擎套件 ENGINE_DIR = ' + ENGINE_DIR);
  console.log(' ② 架构门禁 SXJG_TOOLS = ' + SXJG_TOOLS + (FULL ? '   [--full 全库哈希]' : ''));
  console.log('════════════════════════════════════════════════════════════');

  let pass = 0, blocked = 0, failed = 0, total = 0;
  const groupLines = [];
  for (const g of GROUPS) {
    console.log('\n── ' + g.title + ' (' + g.suites.length + ') ──');
    let gp = 0, gb = 0, gf = 0;
    for (const s of g.suites) {
      // --full 仅透传给架构组（引擎组 selftest 无该参数语义）
      const args = (FULL && s.name === 'arch-gate') ? s.args.concat('--full') : s.args;
      const r = runSuite(Object.assign({}, s, { args }));
      total++;
      const tag = r.ok ? '✅ PASS' : (r.envBlocked ? '⚠️ SKIP' : '❌ FAIL');
      const why = r.envBlocked ? ' (环境不可达: 宿主禁 node 建子进程, 非代码回归)'
                : (r.crashed ? ' (' + r.crashed + ')' : '');
      console.log('  ' + tag + '  ' + r.name.padEnd(11) + ' exit=' +
        (r.exit === null ? '-' : r.exit) + ' [' + r.mode + ']' + why);
      // D-57: 失败时直出子套件尾部输出 —— 否则只能看到 exit code, 无法判断是代码缺陷还是环境 flaky
      if (!r.ok && !r.envBlocked && r.out) {
        const tail = r.out.replace(/\s+$/, '').split('\n').slice(-9);
        tail.forEach(l => console.log('      ↳ ' + l));
      }
      if (r.ok) { pass++; gp++; } else if (r.envBlocked) { blocked++; gb++; } else { failed++; gf++; }
    }
    groupLines.push(g.title + ' ' + gp + '/' + g.suites.length + (gf ? ' 🔴' : (gb ? ' ⚠️' : ' ✅')));
    if (!gp && !gb && !gf) groupLines[groupLines.length - 1] = g.title + ' 0/0（无套件）';
  }

  console.log('\n────────────────────────────────────────────────────────────');
  console.log('  分组: ' + groupLines.join('  ｜  '));
  if (failed === 0 && blocked === 0) {
    console.log('  汇总: ' + pass + '/' + total + ' 全通过  🎉 ALL GREEN');
  } else if (failed === 0) {
    console.log('  汇总: ' + pass + ' 通过 / ' + blocked + ' 环境不可达 / 0 代码失败  ⚠️ 部分未完成验证');
    console.log('  说明: 未模块化套件需起子进程, 而宿主禁 node 创建子进程(EBUSY) —— 属环境约束、非代码回归。');
    console.log('  对策: 用 Python 层等价聚合补跑全部(不受 node shim 限制):');
    console.log('        python "' + path.join(ENGINE_DIR, 'selftest_all.py') + '"');
  } else {
    console.log('  汇总: ' + pass + '/' + total + ' 通过' +
      (blocked ? ' (+' + blocked + ' 环境不可达)' : '') + '  🔴 存在失败');
  }
  console.log('════════════════════════════════════════════════════════════');

  // D-60 退出码契约: 0=全绿 / 1=存在代码失败 / 2=环境不可达(既非通过也非回归, 供 CI 区分而不误判)
  process.exit(failed > 0 ? 1 : (blocked > 0 ? 2 : 0));
}

if (require.main === module) main();
module.exports = { runSuite, classifySpawn, SUITES, ARCH_SUITES, GROUPS };
