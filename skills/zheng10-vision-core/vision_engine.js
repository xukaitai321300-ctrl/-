#!/usr/bin/env node
// zheng10-vision-core · 视觉核心（兔/虎/猪/鸡 共享调用）· 双档：主力 qwen3-vl:8b + 终审 qwen3.6:latest
// 生肖团「视觉互通层」技术基底：四角色统一调用，结论写入共享视觉证据池 (本技能目录内 logs/vision_evidence.jsonl，随 __dirname 自包含，不依赖架构根目录)
//
// 职责:
//   1) 调用 OLLAMA 多模态视觉模型 (base64 图片, 支持多图)，分两档（口径同活文件 VISION_MODEL_MAIN/FINAL）：
//        --stage main (默认) → qwen3-vl:8b   快/批量初筛（6GB 显存，10~20s/张）
//        --stage final       → qwen3.6:latest 深/准细看（36B，90s+/张，自动 think:false）
//   2) 返回结构化结果, 强制含 vision_model: "MODEL + ' (OLLAMA)'" 与 stage 字段
//   3) 写入共享视觉证据池 (append-only, 按图 sha256 索引互通)
//   4) 支持 --read-evidence 在调用前读取该图既有「其他角色」结论作交叉验证佐证
//
// ⚠️ 模型名/端点/num_ctx/分档 的唯一真源是本包目录内的 config.json（path.join(__dirname,'config.json')）；本文件仅兜底，勿在此硬编码。
//    （2026-09-12 已迁移：旧视觉模型已从 Ollama 卸载，沿用旧名必 404；迁移细节见 config.json 的 _model_note。）
//    （2026-11-20 更正：此前注释误指 <架构根目录>/zheng10-vision-core/config.json —— 该份是历史归档，
//      代码从不读它；且 9 个运行时字段与本包 config.json 完全相同，误改不会报错但也完全不生效。）

const fs = require('fs');
const cp = require('child_process');
const crypto = require('crypto');
const path = require('path');

// 单一视觉真值源：模型名/端点/超时/num_ctx/分档 统一从项目 config.json 读取。
// 改模型只需改本包目录内的 config.json（与本文件同目录），全角色生效。
function _loadVisionCfg(){
  try { return JSON.parse(fs.readFileSync(path.join(__dirname, 'config.json'),'utf8')); } catch(_) { return {}; }
}
const _VC = _loadVisionCfg();
const OLLAMA = (_VC.url || 'http://127.0.0.1:11434/api/chat').replace(/\/api\/chat$/,'');

// 双档规格表（命名口径 = 活文件 VISION_MODEL_MAIN / VISION_MODEL_FINAL，禁各写各的）
const STAGE = {
  main: {                                    // 主力：快/批量初筛（6GB 显存，10~20s/张）
    model:    _VC.model_main || _VC.model || 'qwen3-vl:8b',
    numCtx:   _VC.num_ctx || 8192,           // 强制项：不封顶必爆 16GB 显存（E: 视觉层显存事故）
    think:    false,                         // 主力档关思考：更快，避免无谓思维链
    timeoutS: Math.ceil((_VC.timeout_ms || 240000) / 1000)
  },
  final: {                                   // 终审：深/准细看（36B，90s+/张）
    model:    _VC.model_final || 'qwen3.6:latest',
    numCtx:   _VC.num_ctx_final || _VC.num_ctx || 8192,
    think:    _VC.think_final === true,      // qwen3.6 是思考模型：默认必关，否则思维链耗尽 num_predict → 正文空（D23）
    timeoutS: Math.ceil((_VC.timeout_ms_final || 420000) / 1000)
  }
};
const DEFAULT_STAGE = 'main';
const STAGE_NAMES = Object.keys(STAGE);
const LOG_DIR = path.join(__dirname, 'logs');
const EVIDENCE = path.join(LOG_DIR, 'vision_evidence.jsonl');
const NODE = process.execPath;                                  // 当前 node 可执行, 用于调用总线脚本
const BUS = path.join(__dirname, '..', 'zheng10-bus', 'zodiac_bus.js');
const BUS_TYPE = { rabbit:'analyze', tiger:'collect', pig:'style', rooster:'review' };

const VALID_ROLES = ['rabbit', 'tiger', 'pig', 'rooster'];
// 各角色评审/分析时, 作为佐证读取的其他角色集合 (鸡读虎/兔/猪; 其余读除自身外全部)
const CORROB_ROLES = {
  rooster: ['tiger', 'rabbit', 'pig'],
  rabbit:  ['tiger', 'pig', 'rooster'],
  tiger:   ['rabbit', 'pig', 'rooster'],
  pig:     ['rabbit', 'tiger', 'rooster']
};

function parseArgs(argv){
  const a = { role:null, product:null, images:[], prompt:null, promptFile:null,
              readEvidence:false, readEvidenceOnly:false, hash:null, primaryHash:null,
              noWrite:false, out:null, stage:DEFAULT_STAGE };
  for(let i=2;i<argv.length;i++){
    const k = argv[i];
    if(k==='--stage') a.stage = argv[++i];
    else if(k==='--final') a.stage = 'final';   // 兼容项目惯例（_audit_aireview.cjs --final）
    else if(k==='--role') a.role = argv[++i];
    else if(k==='--product') a.product = argv[++i];
    else if(k==='--image') a.images.push(argv[++i]);
    else if(k==='--prompt') a.prompt = argv[++i];
    else if(k==='--prompt-file') a.promptFile = argv[++i];
    else if(k==='--read-evidence') a.readEvidence = true;
    else if(k==='--read-evidence-only') a.readEvidenceOnly = true;
    else if(k==='--hash') a.hash = argv[++i];
    else if(k==='--primary-hash') a.primaryHash = argv[++i];
    else if(k==='--no-write') a.noWrite = true;
    else if(k==='--out') a.out = argv[++i];
  }
  return a;
}

function sha256File(p){
  const buf = fs.readFileSync(p);
  return 'sha256:' + crypto.createHash('sha256').update(buf).digest('hex');
}

// 读取该图 hash 下、除 excludeRole 外、且角色在 allow 集合内的既有结论
function readEvidenceFor(hash, excludeRole, allow){
  if(!fs.existsSync(EVIDENCE)) return [];
  const out = [];
  const lines = fs.readFileSync(EVIDENCE, 'utf8').split('\n').filter(Boolean);
  for(const ln of lines){
    try{
      const e = JSON.parse(ln);
      if(e.image_hash === hash && e.role !== excludeRole && (!allow || allow.includes(e.role))){
        out.push({ role:e.role, ts:e.ts, analysis:e.analysis, product:e.product });
      }
    }catch(_){}
  }
  return out;
}

// 按档调用；final 档若首轮正文为空（思考模型吞 num_predict）自动重试一次（D23）
function callModel(imagesB64, prompt, stage){
  const S = STAGE[stage] || STAGE[DEFAULT_STAGE];
  const t = Date.now();
  let content = _post(imagesB64, prompt, S);
  if(!content && S.think === false && stage === 'final'){
    content = _post(imagesB64, prompt, S);   // 重试一次：qwen3.6 偶发空正文
  }
  return { content, elapsed:((Date.now()-t)/1000).toFixed(1) };
}

function _post(imagesB64, prompt, S){
  const payload = { model:S.model, messages:[{ role:'user', content:prompt, images:imagesB64 }],
                    stream:false, think:S.think, options:{ num_ctx:S.numCtx } };
  const pj = path.join(LOG_DIR, '_vq_tmp_'+Date.now()+'.json');
  fs.writeFileSync(pj, JSON.stringify(payload));
  // --noproxy "*"：本机端口禁用代理，否则 curl 走系统代理必失败（铁律 T4）
  const out = cp.execSync(`curl -s --noproxy "*" -m ${S.timeoutS} -X POST ${OLLAMA}/api/chat -d @${pj}`, {encoding:'utf8', maxBuffer:1e8});
  try{ fs.unlinkSync(pj); }catch(_){}
  const j = JSON.parse(out);
  return (j && j.message && j.message.content) ? j.message.content.trim() : '';
}

function main(){
  const A = parseArgs(process.argv);

  // 模式A: 仅查证据 (不调模型)
  if(A.readEvidenceOnly){
    if(!A.hash){ console.error('❌ --read-evidence-only 需要 --hash'); process.exit(1); }
    const ev = readEvidenceFor(A.hash, null, null);
    console.log(JSON.stringify({ hash:A.hash, evidence:ev }, null, 2));
    return;
  }

  // 常规模式: 校验必填
  if(!A.role || !VALID_ROLES.includes(A.role)){ console.error('❌ 需要 --role ∈ '+VALID_ROLES.join('/')); process.exit(1); }
  if(A.images.length===0){ console.error('❌ 需要至少 --image <路径>'); process.exit(1); }
  if(!A.prompt && !A.promptFile){ console.error('❌ 需要 --prompt 或 --prompt-file'); process.exit(1); }
  if(!STAGE_NAMES.includes(A.stage)){ console.error('❌ --stage ∈ '+STAGE_NAMES.join('/')); process.exit(1); }

  // 互通索引 key: 优先 --primary-hash, 否则取第一张图 hash
  const hashes = A.images.map(sha256File);
  const primaryHash = A.primaryHash || hashes[0];

  // 读既有证据 (交叉验证佐证)
  let evidenceRefs = [];
  if(A.readEvidence){
    const allow = CORROB_ROLES[A.role] || VALID_ROLES.filter(r=>r!==A.role);
    evidenceRefs = readEvidenceFor(primaryHash, A.role, allow);
  }

  // 组装 prompt (注入佐证块)
  let prompt = A.prompt || fs.readFileSync(A.promptFile,'utf8');
  if(evidenceRefs.length>0){
    const blk = evidenceRefs.map(e=>`【${e.role} 对同图的既有结论】(${e.ts})\n${e.analysis}`).join('\n\n');
    prompt = prompt + '\n\n===== 交叉验证佐证（其他角色对该图已有结论，请参考但不盲从）=====\n' + blk;
  }

  // 调模型
  const S = STAGE[A.stage];
  const imagesB64 = A.images.map(p=>fs.readFileSync(p).toString('base64'));
  const { content, elapsed } = callModel(imagesB64, prompt, A.stage);

  // 写证据池 (除非 --no-write: 由调用方自行写结构化记录)
  const record = {
    ts: new Date().toISOString(),
    role: A.role,
    stage: A.stage,
    image_hash: primaryHash,
    image_paths: A.images,
    product: A.product || null,
    vision_model: S.model + ' (OLLAMA)',
    prompt: prompt,
    analysis: content,
    evidence_refs: evidenceRefs.map(e=>({role:e.role, ts:e.ts}))
  };
  if(!A.noWrite){
    if(!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR, {recursive:true});
    fs.appendFileSync(EVIDENCE, JSON.stringify(record)+'\n');
    // 双向闭环: 视觉结论同时 emit 到通用互通总线 (zheng10-bus), 使非视觉角色按 image_hash 感知
    try{
      const bt = BUS_TYPE[A.role] || 'analyze';
      const cf = path.join(LOG_DIR, '_bus_'+Date.now()+'.json');
      fs.writeFileSync(cf, JSON.stringify({ summary:(content||'').slice(0,150), role:A.role, image_hash:primaryHash }));
      cp.execSync(`"${NODE}" "${BUS}" --emit --role ${A.role} --type ${bt} --product "${A.product||''}" --ref ${primaryHash} --content-file "${cf}"`, {encoding:'utf8', maxBuffer:1e8});
      try{ fs.unlinkSync(cf); }catch(_){}
    }catch(e){ /* 总线写入失败不影响视觉结论 */ }
  }

  const result = {
    vision_model: S.model + ' (OLLAMA)',
    stage: A.stage,
    role: A.role,
    image_hash: primaryHash,
    elapsed,
    analysis: content,
    evidence_used: evidenceRefs.length,
    evidence_refs: evidenceRefs.map(e=>({role:e.role, ts:e.ts}))
  };
  if(A.out) fs.writeFileSync(A.out, JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
}

try{ main(); }
catch(e){ console.error('❌ vision_engine error:', e.message); process.exit(1); }
