#!/usr/bin/env node
/**
 * metrics.js —— 评者间一致度元指标工具（R30 精炼 · 由 R29 TeamFusion 发现工程化）
 *
 * 背景：R29 网络对比参照第三角度（设计 Agent 人在回路评测）中，TeamFusion 研究揭示
 *   「设计者间一致度低（Kendall's W=0.37）」是开放式设计协作的真实质量问题。
 *   当时标为"前瞻"；本轮工程化落地，给 鸡评审 主观 rubric 加量化一致性校验：
 *   - 多评者给同一批图打分时，用 Kendall's W 量整体一致度（W∈[0,1]，1=完全一致）；
 *   - 单图多评者打分时，用量化 std/均值 量该图的一致度，超阈值则告警。
 *
 * 这不改变 eval 的阻断逻辑（__PENDING__ 仍须人工填值），而是为"填值"环节加一道
 * 一致性质检——与微软 Magentic-UI ActionGuard / EdgeVerve AI4UI 两段 HITL 的
 * "人工门禁须可靠"理念一致，是质量纪律层的细化，非架构维度膨胀。
 *
 * 用法：
 *   node metrics.js kendallW --matrix "9,8,7;9,8,7;9,8,7"     多图×多评者 → W
 *   node metrics.js agree --scores "8.6,8.4,9.0"             单图多评者 → mean±std + 告警
 *   node metrics.js selftest                                内置自测（完美一致→W=1；反转→W≈0.11）
 *
 * 矩阵约定：行=图(object)，列=评者(rater)；分数越高越好。
 */
'use strict';
const cp = require('child_process');

/** 对一组分数做平均秩（处理并列） */
function rankAverage(scores) {
  const n = scores.length;
  const idx = scores.map((v, i) => i).sort((a, b) => scores[a] - scores[b]);
  const rank = new Array(n).fill(0);
  let i = 0;
  while (i < n) {
    let j = i;
    while (j + 1 < n && scores[idx[j + 1]] === scores[idx[i]]) j++;
    const avg = (i + j) / 2 + 1; // 1-based 平均秩
    for (let k = i; k <= j; k++) rank[idx[k]] = avg;
    i = j + 1;
  }
  return rank;
}

/** Kendall's coefficient of concordance W（多评者×多图） */
function kendallW(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;
  if (rows < 2) throw new Error('kendallW 需至少 2 个对象(图)');
  if (cols < 2) throw new Error('kendallW 需至少 2 名评者');
  for (const r of matrix) if (r.length !== cols) throw new Error('矩阵列数不一致');

  const R = new Array(rows).fill(0);
  for (let c = 0; c < cols; c++) {
    const colScores = matrix.map(r => r[c]);
    const rk = rankAverage(colScores);
    for (let i = 0; i < rows; i++) R[i] += rk[i];
  }
  const Rmean = (cols * (rows + 1)) / 2;
  let S = 0;
  for (const ri of R) S += (ri - Rmean) * (ri - Rmean);
  const W = (12 * S) / (cols * cols * (Math.pow(rows, 3) - rows));
  return { W, R, Rmean, S };
}

/** 单图多评者一致性：mean / std / 告警 */
function scoreAgreement(scores, warnStd = 1.0) {
  const n = scores.length;
  if (n < 2) return { mean: scores[0], std: 0, warn: false, note: '单评者无一致度可言' };
  const mean = scores.reduce((a, b) => a + b, 0) / n;
  const variance = scores.reduce((a, b) => a + (b - mean) * (b - mean), 0) / n;
  const std = Math.sqrt(variance);
  const min = Math.min(...scores), max = Math.max(...scores);
  return { mean: +mean.toFixed(2), std: +std.toFixed(2), min, max, warn: std > warnStd, warnStd };
}

function parseMatrix(str) {
  return str.split(';').map(row => row.split(',').map(s => {
    const v = parseFloat(s.trim());
    if (isNaN(v)) throw new Error('非数值: ' + s);
    return v;
  }));
}

function cmdKendallW(rest) {
  const mi = rest.indexOf('--matrix');
  if (mi < 0) throw new Error('用法: metrics.js kendallW --matrix "9,8,7;9,8,7;9,8,7"');
  const m = parseMatrix(rest[mi + 1]);
  const { W, R, Rmean, S } = kendallW(m);
  console.log('Kendall\'s W = ' + W.toFixed(4) + '  (1=完全一致, 0=完全不一致)');
  console.log('  对象数(图)=' + m.length + ' 评者数=' + m[0].length + '  S=' + S.toFixed(2) + '  Rmean=' + Rmean);
  console.log('  每图秩和 R=[' + R.map(x => x.toFixed(1)).join(', ') + ']');
  return W;
}

function cmdAgree(rest) {
  const si = rest.indexOf('--scores');
  if (si < 0) throw new Error('用法: metrics.js agree --scores "8.6,8.4,9.0"');
  const scores = rest[si + 1].split(',').map(s => parseFloat(s.trim()));
  const r = scoreAgreement(scores);
  console.log('单图多评者一致性: mean=' + r.mean + ' std=' + r.std + ' min=' + r.min + ' max=' + r.max);
  console.log(r.warn ? ('⚠️ 一致度偏低(std>' + r.warnStd + ')，建议复核或加评者') : '✅ 一致度可接受');
  return r;
}

function cmdSelftest() {
  console.log('--- metrics.js selftest ---');
  // 1) 完美一致 → W=1（现实化：每名评者给每张图相同分，但图间有区分度）
  const perfect = [[8.6, 8.6, 8.6], [7.2, 7.2, 7.2], [9.1, 9.1, 9.1]];
  const wp = kendallW(perfect).W;
  console.log('[T1] 完美一致 W=' + wp.toFixed(4) + (Math.abs(wp - 1) < 1e-9 ? ' ✅' : ' ❌'));
  // 2) 部分反转 → W 低
  const varied = [[9, 8, 7], [7, 8, 9], [8, 9, 7]];
  const wv = kendallW(varied).W;
  console.log('[T2] 反转分散 W=' + wv.toFixed(4) + (wv > 0 && wv < 0.5 ? ' ✅(低一致)' : ' ❌'));
  // 3) 单图多评者
  const a1 = scoreAgreement([8.6, 8.4, 9.0]);
  console.log('[T3] 单图 mean=' + a1.mean + ' std=' + a1.std + (a1.warn ? ' ⚠️' : ' ✅'));
  const a2 = scoreAgreement([6.0, 9.0, 7.5]);
  console.log('[T4] 单图 mean=' + a2.mean + ' std=' + a2.std + (a2.warn ? ' ⚠️ 一致度低 ✅(应告警)' : ' ❌(应告警)'));
  const ok = Math.abs(wp - 1) < 1e-9 && wv > 0 && wv < 0.5 && !a1.warn && a2.warn;
  console.log(ok ? '✅ selftest 全过' : '❌ selftest 失败');
  process.exit(ok ? 0 : 1);
}

function main(argv) {
  const args = argv.slice(2);
  const cmd = args[0];
  const rest = args.slice(1);
  if (cmd === 'selftest') return cmdSelftest();
  if (cmd === 'kendallW') return cmdKendallW(rest);
  if (cmd === 'agree') return cmdAgree(rest);
  console.log('用法:');
  console.log('  node metrics.js kendallW --matrix "9,8,7;9,8,7;9,8,7"');
  console.log('  node metrics.js agree --scores "8.6,8.4,9.0"');
  console.log('  node metrics.js selftest');
  process.exit(cmd ? 1 : 0);
}

// D-61(R28): 模块化 —— main(argv) + require.main 守卫, 供 selftest_all 同进程直调(规避受限宿主 EBUSY)。
// D-63(R29): 统一导出名 cli（与其余 8 引擎一致）；保留 main 作向后兼容别名。
if (require.main === module) {
  try { main(process.argv); } catch (e) { console.error('❌ ' + e.message); process.exit(1); }
}
module.exports = { cli: main, main };
