---
version: "2.0.5"
author: "猴哥（十二生肖团）"
name: zheng10-vision-core
display_name: 十二生肖团视觉互通层核心
display_name_en: "Vision Core"
name_en: "zheng10-vision-core"
description_zh: "十二生肖团视觉互通层核心：兔/虎/猪/鸡 四角色共享的 OLLAMA 双档视觉模型（主力 qwen3-vl:8b 快筛 / 终审 qwen3.6:latest 深看）单一调用源 + 共享视觉证据池"
description_en: "Zodiac team execution-layer skill: Vision Core. (See description_zh for full details.)"
description: 十二生肖团视觉互通层核心：兔/虎/猪/鸡 四角色共享的 OLLAMA 双档视觉模型（主力 qwen3-vl:8b 快筛 / 终审 qwen3.6:latest 深看）单一调用源 + 共享视觉证据池
license: MIT
metadata:
  author: 猴哥
  version: "2.0.5"
  tags:
    - vision-core
    - ollama-qwen3-vl:8b
    - ollama-qwen3.6-final
    - dual-stage-vision
    - shared-evidence-pool
    - cross-role-interconnection
  generated_date: 2026-07-27
  classification: P0-core
when_to_use: "在涉及「vision-core」职责的任务中调用本技能；十二生肖团视觉互通层核心：兔/虎/猪/鸡 四角色共享的 OLLAMA 双档视觉模型（主力 qwen3。"
---

# zheng10-vision-core · 视觉互通核心（单一真相源）

> **定位**：生肖团「视觉互通层」的技术基底。兔(图像分析)/虎(图像采集)/猪(风格参考)/鸡(评审) 四职能
> 不再各自写协议、各自看图，而是统一调用本技能里的 `vision_engine.js`，
> 结论写入同一份共享视觉证据池 `<架构根目录>\logs\vision_evidence.jsonl`，实现职能间互通、重复图不重复烧 token。

## 一、铁律常量（唯一权威定义，禁止各职能重复写）

- **OLLAMA 端点**：`http://127.0.0.1:11434`
- **视觉模型（双档 · 真源 = `<架构根目录>/zheng10-vision-core/config.json`）**：
  - `--stage main`（**默认**）→ `qwen3-vl:8b`：主力，快 / 批量初筛（约 6GB 显存，10~20s/张）
  - `--stage final` → `qwen3.6:latest`：终审，深 / 准细看（36B，90s+/张，引擎自动 `think:false`）
  - 口径与活文件 `VISION_MODEL_MAIN` / `VISION_MODEL_FINAL` 一致；**禁在别处手抄模型名**（D22），要改只改 config.json
- **num_ctx**：`8192`（强制项；两模型默认上下文都远超 16GB 显存可承载量，不封顶必爆显存）
- **接口**：`POST /api/chat`，`messages[].content` 为文本 prompt，`messages[].images` 为 base64 数组（**不带 data URI 前缀**）
- **超时**：主力档 `-m 240`，终审档 `-m 420`
- **返回字段**（强制）：任何结论必须带 `vision_model: "<实际模型> (OLLAMA)"` 与 `stage` 字段，缺则产物无效

## 二、共享视觉证据池（单一互通总线）

- **路径**：`<架构根目录>\logs\vision_evidence.jsonl`（append-only，按图 sha256 索引）
- **每行一条 JSON 记录**，schema：

```json
{
  "ts": "2026-07-27T13:05:00.000Z",
  "role": "rabbit|tiger|pig|rooster",
  "stage": "main|final",
  "image_hash": "sha256:<图片内容哈希>",
  "image_paths": ["<本地资源路径>"],
  "product": "吨吨桶",
  "vision_model": "qwen3-vl:8b (OLLAMA)",
  "prompt": "实际发给模型的完整 prompt（含交叉验证佐证块）",
  "analysis": "模型返回的视觉分析文本",
  "evidence_refs": [{"role": "tiger", "ts": "..."}]
}
```

- **互通规则**：四职能写入同一份池；按 `image_hash` 互通——
  同一张图若已被虎/兔/猪分析过，鸡评审该图时自动拉取这些结论作**交叉验证佐证**（反之亦然）。
- **去重**：同一张图（同 hash）不重复烧 token；先查池，命中即复用。

## 三、CLI 用法（`vision_engine.js`）

```bash
# 兔/虎/猪 分析某图（写入证据池）—— 默认主力档 qwen3-vl:8b
node vision_engine.js --role rabbit --product 吨吨桶 --image <本地资源路径> --prompt "..."

# 关键件走终审档（qwen3.6:latest，慢但更准）
node vision_engine.js --role rabbit --product 吨吨桶 --image <本地资源路径> --prompt "..." --stage final

# 鸡 评审某图（自动拉取 虎/兔/猪 对该图既有结论作佐证；自身结论也写回池）
node vision_engine.js --role rooster --product 吨吨桶 \
  --image <本地资源路径> --image <本地资源路径> --primary-hash sha256:<cand_hash> \
  --prompt-file <本地资源路径> --read-evidence --no-write --out <本地资源路径>

# 仅查某图已有证据（不调模型）
node vision_engine.js --read-evidence-only --hash sha256:abc...
```

参数：
- `--stage`：`main`（默认，主力 qwen3-vl:8b 快筛）| `final`（终审 qwen3.6:latest 深看）；`--final` 为等价简写
- `--role`：`rabbit|tiger|pig|rooster`（必填，常规模式）
- `--product`：产品名（写入池，便于检索）
- `--image`：图片路径，**可重复**传多张（图1=参考，图2=待审…）
- `--primary-hash`：互通索引 key（默认取第一张图的 hash；鸡评审时传候选图 hash）
- `--prompt` / `--prompt-file`：二选一
- `--read-evidence`：调用前读该图其他职能既有结论，注入 prompt 作佐证
- `--no-write`：只调模型、不写池（由调用方自行写结构化记录时用）
- `--out`：结果写 JSON 文件（含 `vision_model` 字段）

## 四、四职能路由契约（接线铁律）

兔/虎/猪/鸡 各自的 SKILL.md **必须**把「调用视觉模型看图片」改为调本技能，删除各自重复的
`node -e`/curl 段落，只保留一行路由 + 本文件引用。协议细节（端点/模型/base64/证据池/分档）只在本文件维护，
**单一真相源**，避免改一处漏三处。

## 五、确定性裁决说明

两档模型均为非确定性模型；各职能在拿到 `analysis` 后仍需自己的**确定性硬判**（如鸡的 `hardVerdict`
属性+分数闸门、灰区复评）。本核心只负责「真看图 + 出带 `vision_model` 字段的结论 + 互通证据」，
不替代业务裁决逻辑。

---

## 六、v5.0 保温杯出图提示词资产吸收（视觉判定相关）

> 统一源：`references/thermos_prompt_assets_v5.md`
> 本核心吸收其「二 颜色词表 / 三 负向词库 / 七 评审闸门」。四职能（兔虎猪鸡）真看图时，下列视觉判定为标配。

### 6.1 颜色锁蓝锚视觉校验（对抗色偏）
- 生成图须满足「所有配色线 posPrompt 强制染蓝 `cobalt blue`」——视觉判定时校验主色是否偏离蓝锚（尤其 B~G 线靠 `getActiveColorDesc()` 对抗的线）。
- 黑/白材质精度校验：`graphite black #252729`（8-12GU）/ `satin white`（防灰剪影）。

### 6.2 #519 提手文字幻觉视觉校验（对抗字母幻觉）
- 根因 = SDXL 在提手高光曲面固有字母幻觉（非参考图污染）。
- 视觉判定须专项检查：提手区域是否出现 `text on handle` 类字符；命中即判不通过（对齐负向加权 `(text on handle:2.2)` ×6）。

### 6.3 评审计闸（对齐鸡评审 rubric · 资产第七节）
- 幻觉 / A1 / D2 < 10 分 → **返工**。
- 综合 ≥ **B(70)** 且 D4 ≥ 12 → **通过**。
- 本核心出图结论**必须**带 `vision_model: "qwen3-vl:8b (OLLAMA)"`，缺则产物无效重做（与第一节铁律常量一致）。
- 双 QA 闸门：CIELAB ΔE76（色差，由鸡/牛侧色差工具出）+ 视觉模型（本核心），缺一不可。

---

---

---

---

## 📚 资料总线（H 盘资料入口）

> 本技能可读的 H 盘资料已登记在**资料总线**，开工前先查一遍 —— 避免"重复造轮子"和"翻不到料"。

```bash
python <本地资源路径> --role vision-core
python <本地资源路径> --kw <关键词>      # 元数据层：找「有哪些资料」
python <本地资源路径> --wb             # 工作台可挂载的料
python <本地资源路径> "一句话需求"    # 语义层：在 1.2 万篇业务库正文里找「哪一段」
python <本地资源路径> --role vision-core "..."  # 限定本角色的资料范围内检索
```

**全量索引**：`<本地资源路径>` ｜ **清单**：`<本地资源路径>`

| 资料 | 路径 | 体量 | 用途 |
|---|---|---|---|
| `img.product` | `<本地资源路径>` | 859 MB | ✅ 竞品/自家产品图 |

**硬数据优先**：凡涉及国标限值、材料参数、专利红线、竞品价格，**必须以本总线登记的真实文件为准**，不得凭记忆作答。

**出图/交付**：32 个标准提示词模板见 `<本地资源路径>`（结构化索引 `prompt_templates.json`，含分类/变量/正文/示例）。

> 两个入口分工：`lookup.py` 查**目录元数据**（有哪些资料、多大、谁能用）；`core_lookup.py` 查**内容语义**（哪份文件的哪一段讲了这件事）。

<!-- 资料总线区块结束 -->


## 配套能力调用（本技能只做主责，其余功能按需点名调用）

> 规则：**不要**把配套能力的能力顺手做在本技能里；需要哪段功能，就点名调谁。
> 配套能力已设为「仅手动调用」（`disable-model-invocation: true`），只能被点名，不会自己冒出来。

| 我需要 | 就调它 | 别自己硬做 |
|---|---|---|
| 要拆解竞品图的材质/风格/场景，或评估自己出的图 | `图像分析`、`zheng10-vision-core` | `(外部视觉分析服务)`、`(外部视觉分析)` |
| 图出来了但有瑕疵：文字幻觉、划痕、糊了、要换背景 | `局部精修`、`去背景`、`图像还原` | `(外部高清修复工作流)`、`(外部高清修复工具)` |
| 要出一张写实的保温杯产品图 | `(外部出图工作流)`、`(外部写实基座模型)`、`(外部写实基座模型)` | `(外部生图引擎，运行时按需调用)`、`(外部生图运行器)` |

完整矩阵见 `references/配套能力调用表.md`。