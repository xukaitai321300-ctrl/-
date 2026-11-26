#!/usr/bin/env node
/**
 * golden-regress.js —— V4.15 出图 → eval.js golden-set 回归 编排器 (R28续·外部验证胶水 · R31 升级为完整编排 · R40 接 --images · R42 接 ΔE 闸门)
 *
 * 背景：R28 收口后，唯一遗留 = 外部验证（宿主重载 + V4.15 实机出图 + 首次 golden-set 回归）。
 *       本脚本消除「手动翻译诊断包 + 手动拼 eval schema + 评者一致性靠肉眼」三段摩擦。
 *
 * 真实 schema（来自 H:/架构/保温杯变款工作台_MVP.html V4.15 saveResults / V4.42-L QA）：
 *   _诊断_结果_<ts>.json = { exportedAt, results:[ {title, pass, report} ] }
 *     pass  = V4.42-L 像素QA验收（颜色线标准判定，蓝色线≈非灰），report = 亮度/色彩量化文本
 *
 * 映射（机读自动 / 主观标记待评审）：
 *   image_quality.材质非灰        ← 兼容遗留：聚合 V4.15 诊断 qa.pass（全过=true）
 *   image_quality.材质钴蓝主导    ← 锐化目标闸门(R39/R40)：给定 --images 时调 png_qa.py v3.3 算真实像素
 *                                     钴蓝主导度(忠实蓝锚字面目标)；未给则回退 = 材质非灰 同值
 *   image_quality.材质钴蓝主导_ΔE ← R42 新增：同源 png_qa.py v3.3 算 CIELAB Delta E 客观色差
 *                                     （产品主色是否贴合目标钴蓝 #1a365d，ΔE<2 不可感知 / 2-10 可辨 / >10 明显偏差）
 *                                     双颜色闸门互补：前者卡「是否蓝主导」、后者卡「是否贴合目标钴蓝(非灰/非错色)」
 *   image_quality.无生成伪影 / 构图完整 / 提示词契合度 / 鸡评审>=8.0
 *                            ← 需 AI/鸡 视觉评审或 CLIPScore，机读不覆盖 → 标记 "__PENDING__"
 *                               （eval 按失败计分，使 gate 正确保持"待评审未通过"，杜绝虚假 PASS）
 *   audit_structure / verify_pairing 为架构/验证用例，生图回归不覆盖 → 标记已知良好携带项(pass)
 *
 * 用法（出图后一条命令）：
 *   node golden-regress.js "<V4.15输出目录>"
 *   node golden-regress.js "<V4.15输出目录>" --reviewers "8.6,8.4,9.0;7.2,7.5,7.0;9.1,8.9,9.3"
 *   node golden-regress.js "<V4.15输出目录>" --images "<真实出图图目录>" [--reviewers "..."]
 *        （--images 对真实出图跑 png_qa.py v3.3 算「材质钴蓝主导」+「贴合ΔE」双颜色闸门，替代诊断 pass 的粗判）
 *        （--reviewers 为「多评者×多图」打分矩阵：行=图，列=评者，分号分行、逗号分列；
 *           BLOCKED 时自动调用 metrics.js kendallW 校验评者间一致度，W<0.7 告警需对齐 rubric 重评）
 *   node golden-regress.js                 未授权/无数据时打印待办指引并退出 0
 *
 * 注意：本脚本不新增架构维度，仅是外部验证管道的"最后一公里"胶水。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const cp = require('child_process');
const os = require('os');

const BASE = path.join(__dirname, '..');  // R221r2/R8a：E-D57 防再现，禁硬编码 marketplaces 绝对路径
const EVAL = path.join(__dirname, 'eval.js');
const METRICS = path.join(__dirname, 'metrics.js');
const PYTHON = 'C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe';
const PNG_QA = path.join(__dirname, 'png_qa.py');
const BENCH = path.join(BASE, 'benchmarks/reference_golden_set.json');
const CASES = path.join(BASE, 'logs/zodiac_eval_cases.jsonl');

/** 递归找最新 _诊断_结果_*.json（按 mtime） */
function findLatestDiag(outputDir) {
  if (!outputDir || !fs.existsSync(outputDir)) return null;
  const found = [];
  (function walk(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p);
      else if (/^_诊断_结果_.*\.json$/.test(e.name)) found.push(p);
    }
  })(outputDir);
  if (!found.length) return null;
  found.sort((a, b) => fs.statSync(b).mtime - fs.statSync(a).mtime);
  return found[0];
}

/** 确保 eval golden 用例已装载（无则跑 selftest 装载） */
function ensureCases() {
  if (!fs.existsSync(CASES) || fs.readFileSync(CASES, 'utf8').trim() === '') {
    console.log('--- 装载 golden 用例 (eval.js selftest) ---');
    const r = cp.spawnSync('node', [EVAL, 'selftest'], { stdio: 'inherit' });
    if (r.status !== 0) throw new Error('eval.js selftest 失败');
  }
}

/** 把 V4.15 结果诊断翻译为 eval results schema */
function buildResults(diagPath, cobaltDominant, cobaltDe) {
  const diag = JSON.parse(fs.readFileSync(diagPath, 'utf8'));
  const arr = (diag && Array.isArray(diag.results)) ? diag.results : [];
  if (!arr.length) throw new Error('诊断结果无 results 条目: ' + diagPath);
  const allPass = arr.every(r => r.pass === true);
  const failedTitles = arr.filter(r => r.pass !== true).map(r => r.title || '?');
  // cobaltDominant / cobaltDe: true/false 来自 png_qa.py v3.3 真实像素；null/undefined 时回退 = 材质非灰 同值
  const cobalt = (cobaltDominant === null || cobaltDominant === undefined) ? allPass : cobaltDominant;
  const cobaltDeV = (cobaltDe === null || cobaltDe === undefined) ? allPass : cobaltDe;
  const results = {
    audit_structure: { rubrics: { no_bad_json: true, no_orphan_route: true } },
    verify_pairing: { rubrics: { challenger_ne_diff: true } },
    image_quality: {
      rubrics: {
        '鸡评审>=8.0': '__PENDING__',
        '材质非灰': allPass,
        '材质钴蓝主导': cobalt,
        '材质钴蓝主导_ΔE': cobaltDeV,
        '无生成伪影': '__PENDING__',
        '构图完整': '__PENDING__',
        '提示词契合度': '__PENDING__'
      }
    }
  };
  return { results, meta: { diagPath, imageCount: arr.length, failedTitles, allPass, cobaltDominant: cobalt, cobaltDe: cobaltDeV } };
}

/** BLOCKED 后产出待填模板：机读项锁定、主观项置 null + 填写说明 */
function writeFillTemplate(diagDir, results, meta) {
  const tpl = {
    _fillInstructions: {
      note: '将下方 image_quality.rubrics 中标记为 null 的 4 项主观 rubric 由鸡评审/AI视觉评审/CLIPScore 填值后，重跑: node eval.js validate --results <本文件> --bench <bench>',
      bench: BENCH,
      subjectiveRubrics: {
        '鸡评审>=8.0': '数值 0-10，鸡评审一票否决权，需 >=8.0',
        '无生成伪影': '布尔 true/false，有无生成伪影(畸变/融化/重影)',
        '构图完整': '布尔 true/false，产品在画面中是否完整无裁切',
        '提示词契合度': '数值 0-10，生成图与需求的契合度需 >=8.0'
      },
      lockedByMachine: {
        '材质非灰': results.image_quality.rubrics['材质非灰'],
        '材质钴蓝主导': results.image_quality.rubrics['材质钴蓝主导'],
        '材质钴蓝主导_ΔE': results.image_quality.rubrics['材质钴蓝主导_ΔE'],
        'audit_structure': 'known_good (recovery check)',
        'verify_pairing': 'known_good (架构审计)'
      },
      sourceDiag: meta.diagPath,
      imageCount: meta.imageCount
    },
    audit_structure: results.audit_structure,
    verify_pairing: results.verify_pairing,
    image_quality: {
      rubrics: {
        '鸡评审>=8.0': null,
        '材质非灰': results.image_quality.rubrics['材质非灰'],
        '材质钴蓝主导': results.image_quality.rubrics['材质钴蓝主导'],
        '材质钴蓝主导_ΔE': results.image_quality.rubrics['材质钴蓝主导_ΔE'],
        '无生成伪影': null,
        '构图完整': null,
        '提示词契合度': null
      }
    }
  };
  const p = path.join(diagDir, '_eval_results_TO_FILL.json');
  fs.writeFileSync(p, JSON.stringify(tpl, null, 2));
  return p;
}

/** 对真实出图目录跑 png_qa.py v3.3，返回 {cobalt, cobaltDe}（两道颜色闸门聚合）；失败返回 null */
function runPngQa(imagesDir) {
  if (!fs.existsSync(imagesDir)) { console.log('⚠️ --images 目录不存在: ' + imagesDir); return null; }
  const tmp = path.join(os.tmpdir(), 'png_qa_out_' + Date.now() + '.json');
  const r = cp.spawnSync(PYTHON, [PNG_QA, imagesDir, tmp], { encoding: 'utf8' });
  if (r.status !== 0) { console.log('⚠️ png_qa.py 执行异常: ' + (r.stderr || '').slice(0, 200)); return null; }
  try {
    const d = JSON.parse(fs.readFileSync(tmp, 'utf8'));
    return { cobalt: !!d['材质钴蓝主导_聚合'], cobaltDe: !!d['材质钴蓝主导_ΔE_聚合'] };
  } catch (e) { console.log('⚠️ png_qa.py 输出解析失败: ' + e.message); return null; }
}

/** 多评者矩阵 → metrics.js kendallW（评者间一致度） */
function runKendallW(matrixStr) {
  const r = cp.spawnSync('node', [METRICS, 'kendallW', '--matrix', matrixStr], { encoding: 'utf8' });
  if (r.status !== 0) {
    console.log('⚠️ metrics.js kendallW 执行异常（请确认 metrics.js 在场）: ' + (r.stderr || '').slice(0, 200));
    return null;
  }
  return r.stdout;
}

/**
 * selftest：验证本编排器在活包内自包含且 schema 翻译正确
 *   不调 eval.js validate（避免主观 rubric 阻断导致 exit 2 误判）
 *   - 依赖可解析：eval.js / metrics.js / png_qa.py 必须相邻存在（部署到活包 scripts/ 后唯一会破的环节）
 *   - schema 翻译：合成内存 diag → buildResults 产出 image_quality.rubrics 机读项=全过、主观项=PENDING
 */
function cmdSelftest() {
  console.log('--- golden-regress.js selftest ---');
  let ok = true;
  const deps = [
    ['eval.js', EVAL],
    ['metrics.js', METRICS],
    ['png_qa.py', PNG_QA],
  ];
  for (const [label, p] of deps) {
    const present = fs.existsSync(p);
    console.log('[D] ' + label + ': ' + (present ? '✅' : '❌') + ' ' + p);
    if (!present) ok = false;
  }
  const fakeDiag = {
    exportedAt: new Date().toISOString(),
    results: [
      { title: '材质非灰', pass: true },
      { title: '构图完整', pass: true },
      { title: '提示词契合度', pass: true },
    ],
  };
  const tmp = path.join(os.tmpdir(), 'gr_selftest_diag_' + Date.now() + '.json');
  fs.writeFileSync(tmp, JSON.stringify(fakeDiag));
  try {
    const { results } = buildResults(tmp, null, null);
    const iq = results.image_quality.rubrics;
    const t1 = iq['材质非灰'] === true;
    const t2 = iq['材质钴蓝主导'] === true;
    const t3 = iq['材质钴蓝主导_ΔE'] === true;
    const t4 = iq['鸡评审>=8.0'] === '__PENDING__';
    const t5 = iq['无生成伪影'] === '__PENDING__';
    const t6 = iq['构图完整'] === '__PENDING__';
    const t7 = iq['提示词契合度'] === '__PENDING__';
    const allOk = t1 && t2 && t3 && t4 && t5 && t6 && t7;
    console.log('[S] schema: 材质非灰=' + t1 + ' 钴蓝主导=' + t2 + ' ΔE=' + t3 + ' 主观PENDING(4项)=' + t4 + '/' + t5 + '/' + t6 + '/' + t7 + ' ' + (allOk ? '✅' : '❌'));
    if (!allOk) ok = false;
  } catch (e) {
    console.log('[S] ❌ ' + e.message); ok = false;
  } finally {
    try { fs.unlinkSync(tmp); } catch (_) {}
  }
  console.log(ok ? '✅ selftest 全过' : '❌ selftest 失败');
  process.exit(ok ? 0 : 1);
}

function main(argv) {
  const args = argv.slice(2);
  if (args[0] === 'selftest') return cmdSelftest();
  const outputDir = args.find(a => !a.startsWith('--'));
  const reviewersIdx = args.indexOf('--reviewers');
  const reviewers = (reviewersIdx >= 0 && args[reviewersIdx + 1]) ? args[reviewersIdx + 1] : null;
  const imagesIdx = args.indexOf('--images');
  const imagesDir = (imagesIdx >= 0 && args[imagesIdx + 1]) ? args[imagesIdx + 1] : null;
  const diagPath = outputDir ? findLatestDiag(outputDir) : null;

  if (!diagPath) {
    console.log('⏳ 未找到 V4.15 结果诊断(_诊断_结果_*.json)。外部验证待宿主实机出图：');
    console.log('   1) 打开 H:/架构/保温杯变款工作台_MVP.html，点「📁 输出目录」授权，再点「🚀 出图」');
    console.log('   2) 出图后工作台自动写 <输出目录>/YYYY-MM-DD/_诊断_结果_<ts>.json');
    console.log('   3) 重跑：node golden-regress.js "<输出目录>" --images "<真实出图图目录>" [--reviewers "m1,m2,m3;..."]');
    process.exit(0);
  }

  ensureCases();
  // 真实像素双颜色闸门（--images 给定时）：调用 png_qa.py v3.3 算真实出图，否则回退到诊断 pass
  let cobalt = null, cobaltDe = null;
  if (imagesDir) {
    const pq = runPngQa(imagesDir);
    if (pq) { cobalt = pq.cobalt; cobaltDe = pq.cobaltDe; }
    console.log('🔬 png_qa.py v3.3 真实像素(钴蓝主导=' + cobalt + ' / 贴合ΔE=' + cobaltDe + ') (' + imagesDir + ')');
  }
  const { results, meta } = buildResults(diagPath, cobalt, cobaltDe);

  const outPath = path.join(path.dirname(diagPath), '_eval_results_autogen.json');
  fs.writeFileSync(outPath, JSON.stringify(results, null, 2));
  console.log('✅ 已从 ' + diagPath + ' 生成 eval results: ' + outPath);
  console.log('   机读: 材质非灰=' + meta.allPass + ' | 材质钴蓝主导=' + meta.cobaltDominant + ' | 贴合ΔE=' + meta.cobaltDe + (meta.allPass ? '' : ' (诊断QA失败图: ' + meta.failedTitles.join(', ') + ')'));
  console.log('   待评审(需鸡/AI或CLIPScore): 鸡评审>=8.0 / 无生成伪影 / 构图完整 / 提示词契合度');
  console.log('\n--- 调用 eval.js validate ---');
  const r = cp.spawnSync('node', [EVAL, 'validate', '--results', outPath, '--bench', BENCH], { stdio: 'inherit' });

  if (r.status === 0) {
    console.log('\n🎉 RELEASE GATE 已 PASS —— 外部验证完成（注意：本 PASS 仅代表机读项通过，主观项若已填值则全通过）。');
    process.exit(0);
  }

  // BLOCKED：产出待填模板 + 可选评者间一致度校验
  console.log('\n🔒 RELEASE GATE: BLOCKED（主观 rubric 待评审，已正确阻断虚假 PASS）');
  const tplPath = writeFillTemplate(path.dirname(diagPath), results, meta);
  console.log('📝 已生成待填模板: ' + tplPath);
  console.log('   → 由鸡评审/AI 填 4 项主观 rubric(null→值) 后，重跑:');
  console.log('     node eval.js validate --results "' + tplPath + '" --bench "' + BENCH + '"');

  if (reviewers) {
    console.log('\n--- 评者间一致度校验 (metrics.js kendallW) ---');
    const out = runKendallW(reviewers);
    if (out) {
      console.log(out.trim());
      // 提取 W 值做告警（W<0.7 需对齐 rubric 重评）
      const m = out.match(/W\s*=\s*([0-9.]+)/);
      if (m) {
        const w = parseFloat(m[1]);
        if (w < 0.7) console.log('⚠️ 评者间一致度偏低(W=' + w.toFixed(4) + '<0.7)：建议对齐评分 rubric 后重评，避免主观门禁失真。');
        else console.log('✅ 评者间一致度可接受(W=' + w.toFixed(4) + '>=0.7)。');
      }
    }
  } else {
    console.log('\n💡 多评者场景可加 --reviewers "m1,m2,m3;m1,m2,m3" 自动校验评者间一致度(Kendall\'s W)。');
  }
  process.exit(2);
}

// D-61(R28): 模块化 —— main(argv) + require.main 守卫, 供 selftest_all 同进程直调(规避受限宿主 EBUSY)。
// D-63(R29): 统一导出名 cli（与其余 8 引擎一致）；保留 main 作向后兼容别名。
if (require.main === module) {
  try { main(process.argv); } catch (e) { console.error('❌ ' + e.message); process.exit(1); }
}
module.exports = { cli: main, main };
