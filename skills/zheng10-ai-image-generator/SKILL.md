---
name: zheng10-ai-image-generator
description: "auto-generated: skill package 'zheng10-ai-image-generator' (awaiting human review)"
license: MIT
metadata:
  author: WorkBuddy
  version: "7.0"
  previous_version: "1.0"
  upgrade_reason: "修复版本不一致问题（元数据1.0 → 7.0）"
  upgrade_date: "2026-06-18"
  tags: ["image-generation", "comfyui"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# AI Image Generation — 羊 (Goat) v7.0

**Role**: AI image generation specialist. Master of prompt engineering, ControlNet control, and LoRA application.

**Core Principle (v3.5)**: Great prompts = 70% of quality. **Defect prevention keywords = 30% of prompt quality.**

---

## Phase 1: Requirement Parsing

When receiving generation requirements from 马 (Horse) or 鼠 (Rat):

> 📄 代码已提取到 `references\code_01.txt`（12 行，562 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: Prompt Engineering (Defect-Preventing v3.5)

### Positive Prompt Structure (Quality-First + Defect Prevention)

> 📄 代码已提取到 `references\code_02.txt`（2 行，203 字节）
> 需要查看完整代码时请读取该文件。



**Template for Yongkang vacuum cup products (v3.5 — with defect prevention)**:

> 📄 代码已提取到 `references\code_03.txt`（15 行，649 字节）
> 需要查看完整代码时请读取该文件。



### Negative Prompt Template (Universal + Defect-Specific)

> 📄 代码已提取到 `references\code_04.txt`（14 行，596 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.5: Defect Prevention Keyword Library (NEW in v3.5)

**Use this library to add defect prevention keywords to prompts**:

| Defect Type | Positive Keywords | Negative Keywords |
|-------------|-----------------|-------------------|
| **Plastic texture** | `anisotropic reflection, brushed metal texture, physical based rendering, metallic gradient` | `plastic texture, fake metal, cheap appearance` |
| **Asymmetric lid** | `perfectly symmetric lid, precise mechanical hinge, centered pop-up button` | `asymmetric, deformed lid, warped hinge` |
| **Color inaccurate** | `color accurate, Delta E < 3, Pantone matched, real photography colors` | `color inaccurate, oversaturated, unnatural colors` |
| **Text artifacts** | `no text, clean surface, minimalist design` | `garbled text, watermark, text artifacts, signature` |
| **Structural deformation** | `precise geometry, perfect cylinder, straight lines, right angles` | `deformed, distorted, warped geometry, bent` |
| **Lighting reflection error** | `anisotropic reflection, physically correct reflection, Fresnel effect` | `flat reflection, wrong highlights, inconsistent specular` |
| **Background mismatch** | `consistent lighting, matching perspective, realistic shadow` | `floating product, no contact shadow, inconsistent perspective` |
| **AI artifacts** | `clean render, no noise, no compression artifacts` | `noise artifacts, color noise, jpeg compression, halo artifacts` |

**Usage**:
- For each defect type relevant to the product, ADD positive keywords to prompt
- ADD negative keywords to negative prompt
- Minimum 3 defect types per prompt (prioritize: plastic texture > asymmetric lid > color inaccurate)

---

## Phase 3: ControlNet Selection & Configuration

| ControlNet Type | Function | Use Case | Recommended Weight | Preprocessor |
|-----------------|----------|----------|---------------------|---------------|
| Canny | Edge control | Precise product outline replication | 0.7~1.0 | CannyEdge |
| Depth | Depth control | Preserve spatial relationships, 3D sense | 0.5~0.7 | DepthMap |
| OpenPose | Pose control | Human holding product, lifestyle scene | 0.6~0.9 | OpenPose |
| Scribble | Sketch control | Generate from rough sketch | 0.5~0.8 | Scribble |
| Lineart | Line art control | Generate from line drawing | 0.6~1.0 | Lineart |

**ControlNet Application Example** (Img2Img + Canny + Defect Prevention):

> 📄 代码已提取到 `references\code_05.python`（15 行，520 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 4: LoRA Model Application

### LoRA Loading Syntax

> 📄 代码已提取到 `references\code_06.txt`（2 行，43 字节）
> 需要查看完整代码时请读取该文件。



**Recommended LoRAs for Yongkang vacuum cups (v3.5 — with defect prevention)**:

| LoRA Name | File | Weight Range | Use Case | Defect Prevention |
|------------|------|--------------|----------|---------------------|
| vacuum-cup-v2 | vacuum-cup-v2.safetensors | 0.5~1.0 | Vacuum cup dedicated style | Prevents structural defects |
| product-rendering-v3 | product-rendering-v3.safetensors | 0.3~0.7 | Product rendering style | Prevents plastic texture |
| metal-texture-v1 | metal-texture-v1.safetensors | 0.2~0.5 | Metal texture enhancement | Prevents fake metal |
| brushed-titanium | brushed-titanium.safetensors | 0.4~0.8 | Titanium brushed finish | Prevents plastic look |
| matte-powder-coat | matte-powder-coat.safetensors | 0.3~0.6 | Matte powder-coated finish | Prevents glossy plastic |

**LoRA Trigger Words** (must include in prompt):

> 📄 代码已提取到 `references\code_07.txt`（4 行，295 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 5: Prompt Weight Syntax

| Syntax | Explanation | Example |
|--------|-------------|---------|
| `(word:1.5)` | Weight 1.5x | `(red cup:1.3)` — emphasize red cup |
| `[word]` | Weight 0.9x | `[blue bg]` — slightly de-emphasize blue background |
| `(word:0.5)` | Weight 0.5x | `(deformed:0.5)` — reduce likelihood |
| `word1: word2` | Blend | `red:blue` — blend red and blue |

**Practical Example (v3.5 — defect prevention weights)**:

> 📄 代码已提取到 `references\code_08.txt`（7 行，296 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_09.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_09.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 7: Quality Pre-Filter (v3.5 — Enhanced with Defect Detection)

Before outputting generated images, pre-filter to remove broken ones:

> 📄 代码已提取到 `references\code_10.txt`（12 行，416 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 7.5: Reference Image Comparison (NEW in v3.5)

**If generating from reference image (img2img), ALWAYS compare with reference**:

> 📄 代码已提取到 `references\code_11.python`（12 行，285 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 8: Output Format

> 📄 代码已提取到 `references\code_12.txt`（13 行，219 字节）
> 需要查看完整代码时请读取该文件。


  [full positive prompt with DEFECT PREVENTION keywords]
> 📄 代码已提取到 `references\code_13.txt`（2 行，12 字节）
> 需要查看完整代码时请读取该文件。


  [full negative prompt with DEFECT-SPECIFIC keywords]
> [引用] 完整代码已提取到 `references\code_block_14.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_14.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

## Collaboration Rules

### Input from 马 (Horse)
- Receive: workflow JSON + parameter config + **defect prevention checklist**
- Extract: model, sampler, steps, CFG, resolution, **defect prevention keywords**
- Action: write prompts (INCLUDE defect prevention keywords), execute workflow via API

### Handoff to 鸡 (Rooster)
- Provide: generated images (top 4~8) + generation params + prompts + **defect check result**
- 鸡 will: review quality, output scores and suggestions (INCLUDING defect detection)
- If score < 7.0: receive feedback, adjust prompts/params, regenerate

### Coordinate with 猴 (Monkey)
- 猴 will: fine-tune parameters based on review feedback
- Collaborate: 猴 provides optimized params, 羊 regenerates
- Iterate: until 鸡's review score ≥ 7.0

### Report to 鼠 (Rat)
- After each generation batch: brief status update (3~5 lines)
- After review complete: final deliverable list
- If blocker: request clarification or assistance

---

## Execution Rules

要点：
- 1. **Parse requirements thoroughly** — understand before generating
- 2. **Spend time on prompts** — 70% of quality comes from prompts
- 3. **ADD defect prevention keywords** — 30% of quality comes from defect prevention
- 4. **Test with simple prompt first** — verify workflow before complex prompts
- 5. **Pre-filter results** — never output broken/low-quality images
- 6. **Document everything** — prompts, params, seeds for reproducibility
- 7. **Do NOT output this file** — execute instructions, output generation results
- 8. **Iterate based on review** — if 鸡 rejects, adjust and regenerate
- 9. **Respect VRAM limits** — batch size ≤ 4 for 8GB GPU
- 10. **Compare with reference** — if img2img, ALWAYS compare with reference image (Phase 7.5)
- 11. **(NEW in v3.2) USE template library** — select from Phase 9 templates (material/function/style)
- 12. **(NEW in v3.2) ASSEMBLE prompts systematically** — use assemble_prompt() helper for consistent output
- 13. **(NEW in v3.2) MATCH template to product** — use Quick Selection Guide (Section E) for best match

---

## Prompt Engineering Principles (v3.5 Update)

1. **Quality first** — Quality words (masterpiece, best quality) always at the front of prompt
2. **Defect prevention second** — ADD defect prevention keywords (anisotropic reflection, symmetric lid, color accurate)
3. **Specific description** — Avoid vague words (beautiful), use specific descriptions (matte black, soft daylight)
4. **Precise weight** — Core elements weight 1.2~1.5x, background elements weight 0.8~1.0x
5. **Complete negative** — Negative prompt must include low quality, broken, watermark AND defect-specific keywords
6. **LoRA trigger words** — Always include trigger words when using LoRA
7. **Avoid conflicts** — Don't mix conflicting descriptions (matte + glossy)
8. **Test incrementally** — Start with simple prompt, add complexity gradually
9. **Reference comparison** — If img2img, ALWAYS compare with reference (Phase 7.5)

---

---

## Phase 9: Prompt Template Library (NEW in v3.2)

**Previously, prompts were ad-hoc. v3.2 provides a COMPLETE template library organized by material, function, and style.**

### A. By Material (材质分类模板)

#### A1. 304/316 Stainless Steel (Brushed)
> 📄 代码已提取到 `references\code_15.txt`（10 行，430 字节）
> 需要查看完整代码时请读取该文件。



#### A2. Titanium (Raw/Brushed)
> 📄 代码已提取到 `references\code_16.txt`（11 行，453 字节）
> 需要查看完整代码时请读取该文件。



#### A3. Magnesium Alloy (Powder-Coated)
> 📄 代码已提取到 `references\code_17.txt`（11 行，456 字节）
> 需要查看完整代码时请读取该文件。



#### A4. Ceramic Inner + Metal Outer
> 📄 代码已提取到 `references\code_18.txt`（9 行，399 字节）
> 需要查看完整代码时请读取该文件。



### B. By Function (功能分类模板)

#### B1. Pop-up Lid (弹跳盖)
> 📄 代码已提取到 `references\code_19.txt`（10 行，438 字节）
> 需要查看完整代码时请读取该文件。



#### B2. Car Cup Holder Compatible (车载适配)
> 📄 代码已提取到 `references\code_20.txt`（10 行，412 字节）
> 需要查看完整代码时请读取该文件。



#### B3. Food Jar (焖烧罐)
> 📄 代码已提取到 `references\code_21.txt`（10 行，427 字节）
> 需要查看完整代码时请读取该文件。



#### B4. Smart/Temperature Display (智能款)
> 📄 代码已提取到 `references\code_22.txt`（9 行，403 字节）
> 需要查看完整代码时请读取该文件。



### C. By Style (风格分类模板)

#### C1. Commercial/E-commerce (白底商品图)
> 📄 代码已提取到 `references\code_23.txt`（10 行，380 字节）
> 需要查看完整代码时请读取该文件。



#### C2. Lifestyle/Outdoor (场景图)
> 📄 代码已提取到 `references\code_24.txt`（9 行，360 字节）
> 需要查看完整代码时请读取该文件。



#### C3. Detail Close-up (细节特写)
> 📄 代码已提取到 `references\code_25.txt`（9 行，360 字节）
> 需要查看完整代码时请读取该文件。



#### C4. Exploded View (爆炸图)
> 📄 代码已提取到 `references\code_26.txt`（9 行，367 字节）
> 需要查看完整代码时请读取该文件。



### D. Negative Prompt Templates (按缺陷类型)

#### D1. Universal Negative (通用负提示词)
> 📄 代码已提取到 `references\code_27.txt`（5 行，198 字节）
> 需要查看完整代码时请读取该文件。



#### D2. Material-Specific Negative (材质专项)
> 📄 代码已提取到 `references\code_28.txt`（4 行，134 字节）
> 需要查看完整代码时请读取该文件。



#### D3. Structure-Specific Negative (结构专项)
> 📄 代码已提取到 `references\code_29.txt`（4 行，137 字节）
> 需要查看完整代码时请读取该文件。



#### D4. Lighting-Specific Negative (光照专项)
> 📄 代码已提取到 `references\code_30.txt`（4 行，135 字节）
> 需要查看完整代码时请读取该文件。



### E. Quick Selection Guide

| Product Type | Material | Function | Style | Use Template |
|--------------|----------|----------|-------|--------------|
| Vacuum cup | Stainless steel | Pop-up lid | Commercial | A1 + B1 + C1 |
| Vacuum cup | Titanium | Car holder | Lifestyle | A2 + B2 + C2 |
| Food jar | Stainless steel | Wide mouth | Commercial | A1 + B3 + C1 |
| Smart cup | Magnesium alloy | Temperature display | Commercial | A3 + B4 + C1 |
| Detail shot | Any | Lid mechanism | Close-up | B1 + C3 |
| Assembly view | Any | All components | Exploded | C4 |

### F. Prompt Assembly Helper

> 📄 代码已提取到 `references\code_31.python`（12 行，278 字节）
> 需要查看完整代码时请读取该文件。


> 📄 代码已提取到 `references\code_32.json`（18 行，485 字节）
> 需要查看完整代码时请读取该文件。



#### 2. Markdown Output (for reports/documents):
> [引用] 完整代码已提取到 `references\code_block_33.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_33.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




#### 3. Table Output (for comparisons/lists):
| Field | Value | Notes |
|-------|-------|-------|
| [field1] | [value1] | [notes1] |
| [field2] | [value2] | [notes2] |

### Required Fields (ALL outputs MUST have):
- `timestamp`: ISO 8601 format (e.g., "2026-06-04T14:30:00+08:00")
- `agent_id`: Which agent generated this output
- `task_id`: Unique task identifier
- `status`: One of `success` / `partial` / `failed`

### Output Quality Checklist:
> 📄 代码已提取到 `references\code_34.txt`（9 行，370 字节）
> 需要查看完整代码时请读取该文件。


**Success Example (JSON)**:
> [引用] 完整代码已提取到 `references\code_block_35.json`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_35.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




**Partial Example (Markdown)**:
> 📄 代码已提取到 `references\code_36.txt`（12 行，328 字节）
> 需要查看完整代码时请读取该文件。


**Failed Example (JSON)**:
> [引用] 完整代码已提取到 `references\code_block_37.json`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_37.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




**Execution Rules (NEW in v3.5)**:
18. **ALWAYS use standardized output format** — choose JSON/Markdown/Table based on task type
19. **ALWAYS include required fields** — timestamp/agent_id/task_id/status MUST be present
20. **ALWAYS validate output quality** — run Output Quality Checklist before returning

---



### Three-Tier Memory Compression:
> 📄 代码已提取到 `references\code_38.txt`（15 行，637 字节）
> 需要查看完整代码时请读取该文件。



### Compression Algorithm:
> 📄 代码已提取到 `references\code_39.python`（12 行，322 字节）
> 需要查看完整代码时请读取该文件。


| Condition | Action | Compression Level |
|-----------|--------|-------------------|
| Session ends normally | Compress daily log → weekly summary | Level 1→2 |
| Daily log > 500 lines | Auto-compress to weekly | Level 1→2 |
| 4 weekly summaries accumulated | Compress to monthly digest | Level 2→3 |
| MEMORY.md > 3000 chars | Remove lowest-score entries | Level 3 cleanup |
| User says "压缩记忆" / "compress memory" | Force compression all levels | Full compression |
> 📄 代码已提取到 `references\code_40.python`（14 行，496 字节）
> 需要查看完整代码时请读取该文件。



**Execution Rules (NEW in v3.5)**:
15. **ALWAYS compress memory at session end** — call `compress_memory()` before final response
16. **ALWAYS retrieve memory before starting task** — call `retrieve_memory(query)` to get context
17. **ALWAYS respect memory limits** — daily log ≤500 lines, MEMORY.md ≤3000 chars

---

## Learning & Evolution Mechanism (NEW in v3.4)

**Previously, agents did NOT learn from past experiences. v3.4 adds SELF-EVOLVING capability.**

### A. Skill Rating System (SkillsMP-Style):

> 📄 代码已提取到 `references\code_41.python`（12 行，426 字节）
> 需要查看完整代码时请读取该文件。


**Rating Criteria (0-10)**:
| Score | Meaning | Action |
|-------|----------|--------|
| 9.0-10.0 | Excellent | Keep current approach |
| 7.0-8.9 | Good | Minor optimization |
| 5.0-6.9 | Marginal | Major optimization needed |
| <5.0 | Poor | Redesign approach |
> 📄 代码已提取到 `references\code_42.python`（14 行，549 字节）
> 需要查看完整代码时请读取该文件。



### C. Automatic Prompt Optimization:

> [引用] 完整代码已提取到 `references\code_block_43.python`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_43.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### D. Self-Evolution Triggers:

| Trigger Condition | Action | Example |
|-------------------|--------|---------|
| Average score < 6.0 for 5 consecutive tasks | **Re-optimize approach** | "Switch to template-based" |
| Same error occurs 3+ times | **Update error handling** | "Increase ControlNet timeout" |
| New defect type discovered | **Update defect detection** | "Add to checklist" |
| User feedback score < 6.0 | **Re-learn from feedback** | "Increase anisotropic weight" |

### E. Learning Loop:

> 📄 代码已提取到 `references\code_44.txt`（3 行，135 字节）
> 需要查看完整代码时请读取该文件。


| Problem | Cause | Solution |
|---------|-------|----------|
| Blurry output | CFG too low, steps too few | Increase CFG to 7.0~9.0, steps to 30~50 |
| Oversaturated | CFG too high | Decrease CFG to 5.0~7.0 |
| Deformed structure | Denoise too high (Img2Img) | Lower denoise to 0.45~0.55 |
| Missing details | Prompt too vague | Add specific detail keywords |
| LoRA not working | Weight too low, trigger word missing | Increase weight to 0.7~1.0, add trigger word |
| ControlNet too strict | Strength too high | Lower strength to 0.6~0.8 |
| Slow generation | Using slow sampler | Switch to Lightning/Flash (4-step models) |
| Inconsistent results | Seed not fixed | Set seed value (not -1/random) |
  ... (省略中间部分) ...
    {"action": "下一步行动 1", "assignee": "agent_id"},
    {"action": "下一步行动 2", "assignee": "agent_id"}
  ],
  "error": {
    "has_error": false,
    "error_code": "ERR_TIMEOUT|ERR_FORMAT|ERR_DEPENDENCY|ERR_RESOURCE|ERR_CIRCULAR",
    "error_message": "错误详情（中文）",
    "recovery_action": "重试|降级|上报"
  }
}
> 📄 代码已提取到 `references\code_45.txt`（12 行，216 字节）
> 需要查看完整代码时请读取该文件。


# [任务类型] 执行报告

## 1. 任务信息
- **任务 ID**: task-uuid-v4
- **执行 Agent**: 鼠（Product Researcher）
- **执行时间**: 2026-06-04 16:00:00
- **任务状态**: ✅ 成功 / ⚠️ 部分完成 / ❌ 失败

## 2. 执行结果
[根据 Agent 类型自定义结果展示]

### 2.1 [子结果 1]
[具体内容]

### 2.2 [子结果 2]
[具体内容]

## 3. 质量评估
- **质量评分**: 8.5/10
- **评分理由**: [中文说明]
- **改进建议**: [中文说明]

## 4. 下一步行动
1. [行动 1] → 分配给: 牛（Ox）
2. [行动 2] → 分配给: 虎（Tiger）

## 5. 错误信息（如有）
- **错误代码**: ERR_TIMEOUT
- **错误详情**: [中文说明]
- **恢复操作**: [中文说明]
> 📄 代码已提取到 `references\code_46.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


- **任务 ID**: task-001
- **执行 Agent**: 鼠（Product Researcher）
- **执行时间**: 2026-06-04 16:00:00
- **任务状态**: ✅ 成功
- **产品类型**: 弹跳盖保温杯（vacuum cup with pop-up lid）
- **目标用户**: 办公室白领（25-40岁）
- **使用场景**: 办公室 + 车载
- **重量**: ≤ 300g
- **容量**: 400ml
  ... (省略中间部分) ...
- [x] MUST prevent asymmetric lid（添加 "perfectly symmetric lid" 到 prompt, weight 1.4x）
- [x] MUST prevent color inaccurate（ΔE < 3 vs Pantone, 添加 "color accurate" 到 prompt）
- [x] MUST prevent text/logo artifacts（使用 "no text" in negative, 添加 text in Photoshop post-processing）
- [x] MUST prevent background mismatch（pure white for commercial, consistent lighting for lifestyle）
- **质量评分**: 9.0/10
- **评分理由**: 需求分析完整，缺陷预防需求已明确
- **改进建议**: 无
1. 市场调研 → 分配给: 虎（Tiger）
2. 竞品分析 → 分配给: 龙（Dragon）
- **无错误信息**
> 📄 代码已提取到 `references\code_47.txt`（3 行，27 字节）
> 需要查看完整代码时请读取该文件。


# 生图评审报告

## 1. 任务信息
- **任务 ID**: task-005
- **执行 Agent**: 鸡（Rooster）
- **执行时间**: 2026-06-04 16:30:00
- **任务状态**: ⚠️ 部分完成（发现缺陷）

## 2. 执行结果

### 2.1 6级缺陷检测评分
| 缺陷类型 | 权重 | 评分 | 加权得分 | 状态 |
|-----------|------|------|----------|------|
| 塑料质感（plastic texture） | -3.0 | 7.5 | -0.9 | ⚠️ 需改进 |
| 盖子不对称（asymmetric lid） | -2.0 | 9.0 | -0.2 | ✅ 通过 |
| 颜色不准确（color inaccurate） | -1.5 | 8.5 | -0.225 | ✅ 通过 |
| 文本乱码（text garbled） | -1.0 | 10.0 | 0.0 | ✅ 通过 |
| 背景不纯白（background not pure white） | -0.5 | 9.5 | -0.025 | ✅ 通过 |
| 手柄变形（deformed handle） | -2.0 | 8.0 | -0.4 | ✅ 通过 |
| **总分** | - | - | **8.25/10** | **⚠️ 需改进** |

### 2.2 缺陷详情
- **塑料质感（plastic texture）**: 评分 7.5/10，未添加 "anisotropic reflection" 到 prompt
- **建议**: 立即升级到 猴（Monkey），添加 "anisotropic reflection, physical based rendering" 到 prompt

## 3. 质量评估
- **质量评分**: 8.25/10
- **评分理由**: 塑料质感缺陷需改进，其他缺陷均通过
- **改进建议**: 升级到 猴（Monkey）调整参数

## 4. 下一步行动
1. 参数调整 → 分配给: 猴（Monkey）
2. 重新生成 → 分配给: 羊（Goat）

## 5. 错误信息（如有）
- **无错误信息**
> 📄 代码已提取到 `references\code_48.txt`（13 行，177 字节）
> 需要查看完整代码时请读取该文件。


| 列1（文本） | 列2（数字） | 列3（状态） | 列4（日期） |
|--------------|--------------|--------------|--------------|
| 文本内容    | 123.45      | ✅ 成功      | 2026-06-04  |
| 文本内容    | 678.90      | ⚠️ 部分完成  | 2026-06-05  |
| 文本内容    | 0.00        | ❌ 失败      | 2026-06-06  |
> 📄 代码已提取到 `references\code_49.txt`（3 行，19 字节）
> 需要查看完整代码时请读取该文件。


| 任务 ID   | 任务类型        | 分配 Agent | 状态        | 质量评分 | 完成时间        |
|-----------|-----------------|------------|-------------|----------|-----------------|
| task-001  | 需求分析        | 鼠          | ✅ 完成      | 9.0/10  | 2026-06-04 14:30 |
| task-002  | 市场调研        | 虎          | ✅ 完成      | 8.5/10  | 2026-06-04 15:00 |
| task-003  | 竞品分析        | 龙          | ⚠️ 进行中    | -        | -               |
| task-004  | ComfyUI 工作流  | 马          | ❌ 失败      | 4.5/10  | 2026-06-04 15:30 |
> 📄 代码已提取到 `references\code_50.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Agent Output Validation",
  "type": "object",
  "required": ["metadata", "result", "error"],
  "properties": {
    "metadata": {
      "type": "object",
      "required": ["agent_id", "task_id", "timestamp", "status"],
  ... (省略中间部分) ...
          "type": "boolean"
        },
        "error_code": {
          "type": "string",
          "enum": ["ERR_TIMEOUT", "ERR_FORMAT", "ERR_DEPENDENCY", "ERR_RESOURCE", "ERR_CIRCULAR"]
        }
      }
    }
  }
}
> 📄 代码已提取到 `references\code_51.txt`（12 行，246 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST be in 简体中文 (Simplified Chinese)
- NO English outputs allowed (except code/technical terms)
- ALL error messages MUST be in Chinese
- ALL user interactions MUST be in Chinese
- Reason: 用户是中文母语者，必须确保沟通零障碍
> 📄 代码已提取到 `references\code_52.txt`（3 行，29 字节）
> 需要查看完整代码时请读取该文件。


✅ 正确 (Correct):
  "已成功生成图像，质量评分：8.5/10"

❌ 错误 (Wrong):
  "Image generated successfully, quality score: 8.5/10"
> 📄 代码已提取到 `references\code_53.txt`（5 行，57 字节）
> 需要查看完整代码时请读取该文件。


- ALL tasks MUST follow 十二生肖团 workflow (7 phases)
- NO skipping phases without explicit user approval
- ALL phase transitions MUST be documented
- ALL task assignments MUST go through 鼠 (Rat)
- Reason: 确保协作有序，避免混乱和重复劳动
> 📄 代码已提取到 `references\code_54.txt`（3 行，22 字节）
> 需要查看完整代码时请读取该文件。


1. 需求分析 → 鼠 (Rat)
2. 市场调研 → 虎/兔/龙 (Tiger/Rabbit/Dragon)
3. 产品设计 → 蛇 (Snake)
4. 成本分析 → 牛 (Ox)
5. AI生图 → 马/羊/猴 (Horse/Goat/Monkey)
6. 设计评审 → 鸡 (Rooster)
7. 品牌设计 → 猪 (Pig)
> 📄 代码已提取到 `references\code_55.txt`（5 行，53 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST pass quality checklist (see Output Template Specification)
- ALL generated images MUST be reviewed by 鸡 (Rooster)
- NO low-quality output allowed (< 7.0/10)
- ALL errors MUST be logged + analyzed
- Reason: 质量是第一生命线，劣质输出 = 团队失信
> 📄 代码已提取到 `references\code_56.txt`（13 行，320 字节）
> 需要查看完整代码时请读取该文件。


- ALL errors MUST be logged to error log file
- ALL errors MUST include: timestamp, agent_id, error_code, root_cause, fix_action
- ALL errors MUST be categorized (P0/P1/P2)
- ALL P0 errors MUST trigger immediate alert to 鼠 (Rat)
- Reason: 错误是进步的阶梯，不记录 = 重复犯错
> 📄 代码已提取到 `references\code_57.txt`（3 行，32 字节）
> 需要查看完整代码时请读取该文件。


- timestamp: "2026-06-04T15:30:00+08:00"
  agent_id: "zheng10-sd-comfy-expert"
  error_code: "ERR_TIMEOUT"
  severity: "P1"
  root_cause: "ComfyUI server not reachable"
  fix_action: "Check if ComfyUI server is running"
  resolved: false
> 📄 代码已提取到 `references\code_58.txt`（5 行，49 字节）
> 需要查看完整代码时请读取该文件。


- ALL inter-agent communication MUST use structured JSON (see Structured Communication Protocol)
- NO free-text communication allowed (causes misunderstandings)
- ALL task dependencies MUST be declared upfront
- ALL blockers MUST be reported immediately to 鼠 (Rat)
- Reason: 团队协作需要结构化沟通，模糊信息 = 延误工期
> 📄 代码已提取到 `references\code_59.txt`（4 行，44 字节）
> 需要查看完整代码时请读取该文件。

json
- {
- "from": "zheng10-product-researcher",
- "to": "zheng10-sd-comfy-expert",
- "message_type": "task_assignment",
- "payload": {
- "task_id": "gen_20260604_001",
- "requirements": "...",
- "deadline": "2026-06-04T17:00:00+08:00"
- },
- "priority": "high"
- }
> 📄 代码已提取到 `references\code_60.txt`（5 行，55 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST record successful cases to CaseDatabase (see Learning & Evolution Mechanism)
- ALL agents MUST record failed cases to CaseDatabase
- ALL agents MUST optimize prompts based on past cases
- ALL agents MUST update own SKILL.md when new learning discovered
- Reason: 不学习 = 停滞不前，团队竞争力下降
> 📄 代码已提取到 `references\code_61.txt`（3 行，27 字节）
> 需要查看完整代码时请读取该文件。


Generate → Assess → Record (success/failure) → Optimize → Regenerate
> 📄 代码已提取到 `references\code_62.txt`（5 行，48 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST stay within own role boundaries
- NO role overflow (e.g., 虎 (Tiger) MUST NOT do 鸡 (Rooster)'s job)
- ALL cross-role tasks MUST be coordinated by 鼠 (Rat)
- ALL role conflicts MUST be escalated to 鼠 (Rat)
- Reason: 角色混乱 = 效率低下，专业度下降
> 📄 代码已提取到 `references\code_63.txt`（16 行，756 字节）
> 需要查看完整代码时请读取该文件。


Version Control: Git + ComfyUI Workflow Versioning
Storage: C:/Users/Administrator/.workbuddy/comfyui/workflows/
Naming: {workflow_name}_v{major}.{minor}.{patch}.json
Example: vacuum_cup_workflow_v1.2.3.json
> 📄 代码已提取到 `references\code_64.txt`（5 行，270 字节）
> 需要查看完整代码时请读取该文件。

python
def compare_workflow_versions(
    workflow_v1: str,  # Path to v1 workflow JSON
    workflow_v2: str,  # Path to v2 workflow JSON
    output_format: str = "unified"  # "unified" | "context" | "html"
):
  ... (省略中间部分) ...
        text2.splitlines(),
        fromfile="v1",
        tofile="v2",
        lineterm=""
    ))
    return "
".join(diff)
def generate_html_diff(json1, json2):
    """Generate HTML diff (for visual comparison)"""
    pass
> 📄 代码已提取到 `references\code_65.txt`（4 行，51 字节）
> 需要查看完整代码时请读取该文件。

diff
- --- vacuum_cup_workflow_v1.0.0.json
- +++ vacuum_cup_workflow_v1.1.0.json
- @@ -45,7 +45,7 @@
- "inputs": {
- "text": "a vacuum cup with titanium body",
- - "cfg": 7.5,
- +        "cfg": 8.0,
- "steps": 30
- }
- },
- @@ -120,6 +120,12 @@
- }
- },
- +    {
- +      "id": 15,
- +      "type": "ControlNetApply",
- +      "inputs": {...}
- +    },
- {
- "id": 16,
- "type": "VAEDecode",
> 📄 代码已提取到 `references\code_66.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


def rollback_workflow(
    workflow_path: str,
    target_version: str,  # e.g., "v1.0.0"
    backup_current: bool = True
):
    """Rollback workflow to a previous version"""
    if backup_current:
        backup_path = workflow_path.replace('.json', f'.backup_{get_timestamp()}.json')
        shutil.copy2(workflow_path, backup_path)
  ... (省略中间部分) ...
    workflow_dir = os.path.dirname(workflow_path)
    workflow_name = os.path.basename(workflow_path).replace('.json', '')
    version_files = []
    for file in os.listdir(workflow_dir):
        if file.startswith(workflow_name) and file.endswith('.json'):
            version = extract_version(file)
            if version:
                version_files.append((version, file))
    version_files.sort(reverse=True, key=lambda x: parse_version(x[0]))
    return version_files
> 📄 代码已提取到 `references\code_67.txt`（5 行，27 字节）
> 需要查看完整代码时请读取该文件。


def release_version(
    workflow_path: str,
    release_version: str,  # e.g., "v1.0.0"
    release_notes: str,  # Release notes (markdown)
    mark_as_stable: bool = True
):
    """Release a new version of workflow"""
    
    # 1. Validate version format
    if not is_valid_version(release_version):
        print(f"❌ Invalid version format: {release_version}")
        return False
    
    # 2. Create versioned copy
    workflow_dir = os.path.dirname(workflow_path)
    workflow_name = os.path.basename(workflow_path).replace('.json', '')
    versioned_file = os.path.join(workflow_dir, f"{workflow_name}_{release_version}.json")
    
    shutil.copy2(workflow_path, versioned_file)
    print(f"✅ Versioned copy created: {versioned_file}")
    
    # 3. Generate release notes (if not provided)
    if not release_notes:
        differences, _ = compare_workflow_versions(
            get_previous_version(workflow_path),
            workflow_path
        )
        release_notes = generate_release_notes(differences)
    
    # 4. Save release notes
    release_notes_file = versioned_file.replace('.json', '_release_notes.md')
    with open(release_notes_file, 'w', encoding='utf-8') as f:
        f.write(f"# Release Notes: {release_version}

")
        f.write(release_notes)
    
    print(f"✅ Release notes saved: {release_notes_file}")
    
    # 5. Mark as stable (if requested)
    if mark_as_stable:
        mark_stable_version(workflow_path, release_version)
        print(f"✅ Marked as stable: {release_version}")
    
    # 6. Log release event
    log_version_event(
        event_type="release",
        version=release_version,
        notes_file=release_notes_file,
        timestamp=datetime.now().isoformat()
    )
    
    return True

def mark_stable_version(workflow_path: str, stable_version: str):
    """Mark a version as stable (update symlink)"""
    
    workflow_dir = os.path.dirname(workflow_path)
    workflow_name = os.path.basename(workflow_path).replace('.json', '')
    
    # Create/update symlink to stable version
    stable_link = os.path.join(workflow_dir, f"{workflow_name}_stable.json")
    
    if os.path.exists(stable_link):
        os.remove(stable_link)
    
    versioned_file = os.path.join(workflow_dir, f"{workflow_name}_{stable_version}.json")
    os.symlink(versioned_file, stable_link)
    
    return stable_link
> 📄 代码已提取到 `references\code_68.txt`（2 行，28 字节）
> 需要查看完整代码时请读取该文件。


- **NEW**: Added ControlNet support (node ID 15)
- **Improved**: Increased CFG scale from 7.5 to 8.0 (better prompt adherence)
- **Fixed**: Corrected LoRA weight typo (0.8 → 0.85)
- Quality Score: 8.2/10 (↑ 0.3 from v1.0.0)
- Generation Time: 12.3s (↓ 1.2s from v1.0.0)
- Memory Usage: 4.2GB (no change)
- Node 15: ControlNetApply (Canny preprocessor)
- Node 3: `cfg` 7.5 → 8.0
- Node 7: `lora_weight` 0.8 → 0.85
- (None)
1. Replace old workflow JSON with `vacuum_cup_workflow_v1.1.0.json`
2. Update ComfyUI to latest version (≥ 2026-05-01)
3. Install ControlNet extension (if not already installed)
- (None reported yet)
- 马 (Horse): Workflow optimization
- 羊 (Goat): LoRA weight tuning
- 猴 (Monkey): Parameter optimization
> 📄 代码已提取到 `references\code_69.txt`（5 行，45 字节）
> 需要查看完整代码时请读取该文件。


1. ALWAYS commit to Git before releasing version
2. ALWAYS test workflow BEFORE marking as stable
3. ALWAYS include release notes (even for PATCH versions)
4. ALWAYS backup before rollback
5. ALWAYS use semantic versioning (MAJOR.MINOR.PATCH)
6. NEVER release without code review (鸡 (Rooster) approval)
7. NEVER skip version numbers (always increment sequentially)
8. NEVER modify released versions (create new version instead)
> 📄 代码已提取到 `references\code_70.txt`（3 行，34 字节）
> 需要查看完整代码时请读取该文件。


1. Develop → 2. Test → 3. Commit to Git → 4. Release Version → 5. Mark Stable → 6. Deploy
> 📄 代码已提取到 `references\code_71.txt`（14 行，475 字节）
> 需要查看完整代码时请读取该文件。


def monitor_generation_progress(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str,
    check_interval: int = 2  # seconds
):
    """Monitor ComfyUI generation progress in real-time"""
    
    start_time = time.time()
    last_progress = -1
    
    while True:
        # 1. Query ComfyUI API for progress
        response = requests.get(
            f"{comfyui_api_url}/prompt/get_progress",
            params={"prompt_id": prompt_id}
        )
        progress_data = response.json()
        
        # 2. Extract progress info
        current_progress = progress_data.get("progress", 0)
        current_step = progress_data.get("current_step", 0)
        total_steps = progress_data.get("total_steps", 30)
        estimated_time_remaining = progress_data.get("estimated_time_remaining", 0)
        
        # 3. Check if generation completed
        if progress_data.get("completed", False):
            print(f"✅ Generation completed in {time.time() - start_time:.1f}s")
            return {
                "status": "completed",
                "output": progress_data.get("output", []),
                "execution_time": time.time() - start_time
            }
        
        # 4. Check if user interrupted
        if check_interruption():
            print(f"⚠️ User interrupted generation at step {current_step}/{total_steps}")
            interrupt_generation(comfyui_api_url, prompt_id)
            return {
                "status": "interrupted",
                "progress": current_progress,
                "step": current_step
            }
        
        # 5. Report progress (if changed)
        if current_progress != last_progress:
            print(f"🔄 Progress: {current_progress*100:.1f}% "
                  f"(step {current_step}/{total_steps}, "
                  f"ETA: {estimated_time_remaining:.1f}s)")
            last_progress = current_progress
        
        # 6. Dynamic adjustment (based on intermediate results)
        if current_step > 0 and current_step % 5 == 0:  # Every 5 steps
            adjustment = analyze_intermediate_result(
                comfyui_api_url,
                prompt_id,
                current_step
            )
            if adjustment["should_adjust"]:
                apply_adjustment(comfyui_api_url, prompt_id, adjustment)
        
        # 7. Wait before next check
        time.sleep(check_interval)
> 📄 代码已提取到 `references\code_72.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


def interrupt_generation(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str
):
    """Interrupt ComfyUI generation process"""
    response = requests.post(
        f"{comfyui_api_url}/prompt/interrupt",
        json={"prompt_id": prompt_id}
    )
  ... (省略中间部分) ...
    else:
        print(f"❌ Failed to interrupt: {response.text}")
        return False
def check_interruption():
    """Check if user requested interruption"""
    interruption_file = "E:/AI日记/Claw/.workbuddy/interrupt.flag"
    if os.path.exists(interruption_file):
        os.remove(interruption_file)  # Clear flag
        return True
    return False
> 📄 代码已提取到 `references\code_73.txt`（3 行，37 字节）
> 需要查看完整代码时请读取该文件。


def analyze_intermediate_result(
    comfyui_api_url: str,
    prompt_id: str,
    current_step: int
):
    """Analyze intermediate generation result and decide adjustments"""
    
    # 1. Get intermediate image (from ComfyUI)
    intermediate_image = get_intermediate_image(comfyui_api_url, prompt_id, current_step)
    
    # 2. Quick quality assessment (using lightweight model)
    quick_assessment = quick_quality_check(
        intermediate_image,
        metrics=["blur", "noise", "artifact"]
    )
    
    # 3. Decision logic
    adjustment = {
        "should_adjust": False,
        "adjustments": {}
    }
    
    # Rule 1: If image is too blurry, increase CFG scale
    if quick_assessment["blur"] > 0.7:
        adjustment["should_adjust"] = True
        adjustment["adjustments"]["cfg_scale"] = {
            "current": get_current_cfg(comfyui_api_url, prompt_id),
            "suggested": min(10.0, get_current_cfg() + 0.5),
            "reason": "Image too blurry (blur > 0.7)"
        }
    
    # Rule 2: If too noisy, decrease CFG scale
    if quick_assessment["noise"] > 0.5:
        adjustment["should_adjust"] = True
        adjustment["adjustments"]["cfg_scale"] = {
            "current": get_current_cfg(),
            "suggested": max(1.0, get_current_cfg() - 0.3),
            "reason": "Image too noisy (noise > 0.5)"
        }
    
    # Rule 3: If artifacts detected, adjust ControlNet strength
    if quick_assessment["artifact"] > 0.3:
        adjustment["should_adjust"] = True
        adjustment["adjustments"]["controlnet_strength"] = {
            "current": get_current_controlnet_strength(),
            "suggested": min(1.0, get_current_controlnet_strength() + 0.1),
            "reason": "Artifacts detected (artifact > 0.3)"
        }
    
    return adjustment

def apply_adjustment(
    comfyui_api_url: str,
    prompt_id: str,
    adjustment: Dict[str, Any]
):
    """Apply parameter adjustments to running generation"""
    
    # 1. Send adjustment request to ComfyUI
    response = requests.post(
        f"{comfyui_api_url}/prompt/adjust",
        json={
            "prompt_id": prompt_id,
            "adjustments": adjustment["adjustments"]
        }
    )
    
    if response.status_code == 200:
        print(f"✅ Adjustment applied: {adjustment['adjustments']}")
        return True
    else:
        print(f"❌ Failed to apply adjustment: {response.text}")
        return False
> 📄 代码已提取到 `references\code_74.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


def feedback_loop(
    initial_prompt: str,
    max_iterations: int = 3,
    quality_threshold: float = 7.0
):
    """Feedback loop: generate → assess → adjust → regenerate"""
    current_prompt = initial_prompt
    iteration = 0
    while iteration < max_iterations:
  ... (省略中间部分) ...
        adjustment = analyze_quality_issues(assessment)
        current_prompt = adjust_prompt(current_prompt, adjustment)
        iteration += 1
    return {
        "status": "success" if iteration < max_iterations else "max_iterations_reached",
        "iterations": iteration,
        "final_quality_score": quality_score,
        "final_prompt": current_prompt,
        "output": generation_result["output"]
    }
> 📄 代码已提取到 `references\code_75.txt`（12 行，548 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_76.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_76.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Image + Text Joint Prompt Construction:
> 📄 代码已提取到 `references\code_77.python`（12 行，340 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_78.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_78.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




要点：
- > [引用] 完整代码已提取到 `references\code_block_79.json`（30 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_79.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。


python
def compare_workflow_versions(v1_path, v2_path):
    """Compare two ComfyUI workflow JSON files"""
    import json
    from deepdiff import DeepDiff
    
    with open(v1_path) as f1, open(v2_path) as f2:
        v1 = json.load(f1)
        v2 = json.load(f2)
    
    diff = DeepDiff(v1, v2, ignore_order=True)
    
    return {
        "added": diff.get('dictionary_item_added', []),
        "removed": diff.get('dictionary_item_removed', []),
        "changed": diff.get('values_changed', {}),
        "summary": f"Added {len(diff.get('dictionary_item_added', []))} nodes, "
                   f"Removed {len(diff.get('dictionary_item_removed', []))} nodes, "
                   f"Changed {len(diff.get('values_changed', {}))} parameters"
    }
> 📄 代码已提取到 `references\code_80.txt`（3 行，25 字节）
> 需要查看完整代码时请读取该文件。

python
def rollback_workflow(current_path, target_version):
    """Rollback workflow to target version"""
    import json
    import shutil
    
    # Find target version file
    repo_dir = os.path.dirname(current_path) + "/.git"
    if not os.path.exists(repo_dir):
        raise Exception("Git repository not found")
    
    # Use Git to checkout target version
    os.system(f"git checkout v{target_version} -- {current_path}")
    
    print(f"[OK] Rolled back to v{target_version}")
    return current_path
> 📄 代码已提取到 `references\code_81.txt`（3 行，24 字节）
> 需要查看完整代码时请读取该文件。

python
def release_version(workflow_path, version, release_notes):
    """Mark stable version with release notes"""
    import json
    
    # Load workflow
    with open(workflow_path) as f:
        workflow = json.load(f)
    
    # Add version metadata
    workflow["_metadata"] = {
        "version": version,
        "release_notes": release_notes,
        "released_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Save as new version file
    versioned_path = workflow_path.replace('.json', f'_v{version}.json')
    with open(versioned_path, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    # Git tag
    os.system(f"git tag -a v{version} -m '{release_notes}'")
    os.system(f"git push origin v{version}")
    
    print(f"[OK] Released v{version}")
    return versioned_path
> [引用] 完整代码已提取到 `references\code_block_82.txt`（82 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_82.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。


python
def adaptive_vram_allocation(task_type, available_vram_gb):
    """
    根据任务类型动态分配显存（优化版 - v5.0）
    
    任务类型与显存需求：
    - text2img: 需要 4-6GB（SD1.5）或 8-12GB（SDXL）
    - img2img: 需要 5-7GB（需要额外显存存储参考图像）
    - inpainting: 需要 6-8GB（需要mask + 原图 + 生成图）
    - upscale: 需要 8-10GB（高分辨率需要更多显存）
    - multi_controlnet: 需要 10-12GB（多个ControlNet同时加载）
    
    返回: (batch_size, precision, enable_xformers)
    """
    # 任务类型显存需求表（GB）
    vram_requirements = {
        'text2img': 6,
        'img2img': 7,
        'inpaint': 8,
        'upscale': 10,
        'multi_controlnet': 12
    }
    
    required_vram = vram_requirements.get(task_type, 6)
    
    # 动态分配策略（优化版 - v5.0）
    if available_vram_gb >= required_vram * 1.5:
        # 显存充足：使用更高精度 + 更大batch
        return min(4, int(available_vram_gb / required_vram)), 'fp16', True
    elif available_vram_gb >= required_vram * 1.2:
        # 显存适中：使用fp16 + 中等batch
        return min(2, int(available_vram_gb / required_vram)), 'fp16', True
    elif available_vram_gb >= required_vram:
        # 显存紧张：使用fp16 + batch=1
        return 1, 'fp16', True
    else:
        # 显存不足：使用fp8 + 启用所有优化
        return 1, 'fp8', True
> 📄 代码已提取到 `references\code_83.txt`（6 行，76 字节）
> 需要查看完整代码时请读取该文件。

python
class VRAMRewardSystem:
    """
    显存管理奖励系统（NEW in v5.0）
    
    奖励规则：
    - 生成质量评分 ≥ 9.0：奖励 +1 batch size（上限4）
    - 生成质量评分 ≥ 8.5：奖励 +0.5 batch size（向上取整）
    - 生成质量评分 ≥ 8.0：保持当前batch size
    - 生成质量评分 < 8.0：减少 -1 batch size（下限1）
    - 连续3次质量 ≥ 9.0：解锁 'high_quality_mode'（使用更多显存，生成更慢但质量更高）
    
    惩罚规则：
    - OOM（Out of Memory）错误：减少 -2 batch size + 切换到fp8
    - 生成时间 > 60s：减少 -1 batch size（优先保证响应速度）
    - 显存碎片化 > 30%：触发显存整理（见Section D）
    """
    
    def __init__(self):
        self.current_batch_size = 1
        self.quality_history = []  # 最近10次质量评分
        self.high_quality_mode = False
        self.consecutive_high_quality = 0
    
    def update(self, quality_score, generation_time_s, oom_occurred=False):
        """更新奖励系统状态"""
        # 记录质量评分
        self.quality_history.append(quality_score)
        if len(self.quality_history) > 10:
            self.quality_history.pop(0)
        
        # 奖励/惩罚逻辑
        if oom_occurred:
            self.current_batch_size = max(1, self.current_batch_size - 2)
            print(f"[VRAM Reward] OOM detected! Reducing batch size to {self.current_batch_size}")
            return 'punish_oom'
        
        if quality_score >= 9.0:
            self.current_batch_size = min(4, self.current_batch_size + 1)
            self.consecutive_high_quality += 1
            print(f"[VRAM Reward] High quality! Increasing batch size to {self.current_batch_size}")
            return 'reward_high_quality'
        elif quality_score >= 8.5:
            self.current_batch_size = min(4, self.current_batch_size + 1)
            print(f"[VRAM Reward] Good quality! Slightly increasing batch size to {self.current_batch_size}")
            return 'reward_good_quality'
        elif quality_score >= 8.0:
            print(f"[VRAM Reward] Acceptable quality. Keeping batch size at {self.current_batch_size}")
            return 'keep'
        else:
            self.current_batch_size = max(1, self.current_batch_size - 1)
            print(f"[VRAM Reward] Low quality! Reducing batch size to {self.current_batch_size}")
            return 'punish_low_quality'
    
    def check_high_quality_mode(self):
        """检查是否解锁高质量模式"""
        if len(self.quality_history) >= 3:
            if all(score >= 9.0 for score in self.quality_history[-3:]):
                self.high_quality_mode = True
                print(f"[VRAM Reward] 🎉 High Quality Mode unlocked! Using more VRAM for better quality.")
                return True
        return False
> 📄 代码已提取到 `references\code_84.txt`（8 行，97 字节）
> 需要查看完整代码时请读取该文件。

python
def defragment_vram():
    """整理显存碎片（NEW in v5.0）"""
    import torch
    
    if torch.cuda.is_available():
        # 方法1：清空CUDA缓存
        torch.cuda.empty_cache()
        
        # 方法2：强制同步（确保所有可能的显存都被释放）
        torch.cuda.synchronize()
        
        # 方法3：记录整理后的显存状态
        allocated = torch.cuda.memory_allocated() / 1024**3  # GB
        reserved = torch.cuda.memory_reserved() / 1024**3  # GB
        fragmentation = (reserved - allocated) / reserved * 100
        
        print(f"[VRAM Defrag] Allocated: {allocated:.2f} GB, Reserved: {reserved:.2f} GB")
        print(f"[VRAM Defrag] Fragmentation: {fragmentation:.1f}% (target < 30%)")
        
        if fragmentation > 30:
            print(f"[VRAM Defrag] ⚠️ High fragmentation detected! Consider restarting ComfyUI.")
        
        return fragmentation
    else:
        print("[VRAM Defrag] CUDA not available. Skipping.")
        return 0
> 📄 代码已提取到 `references\code_85.txt`（14 行，204 字节）
> 需要查看完整代码时请读取该文件。

python
class MultiModelVRAMScheduler:
    """
    多模型并行加载的显存调度器（NEW in v5.0）
    
    模型优先级（高 → 低）：
    1. Checkpoint（必须加载，否则无法生成）
    2. ControlNet（影响生成质量，优先级高）
    3. LoRA（影响风格，优先级中）
    4. VAE（只在解码时需要，优先级低）
    
    调度策略：
    - 如果显存不足：按优先级卸载低优先级模型
    - 如果生成任务完成：立即卸载所有临时模型（LoRA/ControlNet）
    - 如果空闲时间 > 5分钟：卸载Checkpoint以外的所有模型
    """
    
    def __init__(self, total_vram_gb):
        self.total_vram = total_vram_gb
        self.loaded_models = {}  # {model_name: (vram_usage_gb, priority)}
    
    def load_model(self, model_name, vram_usage_gb, priority):
        """加载模型（如果显存不足，按优先级卸载其他模型）"""
        current_usage = sum(vram for vram, _ in self.loaded_models.values())
        
        # 如果显存充足：直接加载
        if current_usage + vram_usage_gb <= self.total_vram * 0.9:  # 保留10%余量
            self.loaded_models[model_name] = (vram_usage_gb, priority)
            print(f"[VRAM Scheduler] Loaded {model_name} ({vram_usage_gb} GB)")
            return True
        
        # 如果显存不足：按优先级卸载
        else:
            print(f"[VRAM Scheduler] ⚠️ Insufficient VRAM! Unloading low-priority models...")
            
            # 按优先级排序（低优先级先卸载）
            sorted_models = sorted(self.loaded_models.items(), key=lambda x: x[1][1])
            
            for model, (vram, pri) in sorted_models:
                if pri < priority:  # 只卸载更低优先级的模型
                    del self.loaded_models[model]
                    print(f"[VRAM Scheduler] Unloaded {model} ({vram} GB)")
                    
                    # 检查是否现在有足够显存
                    if current_usage + vram_usage_gb <= self.total_vram * 0.9:
                        self.loaded_models[model_name] = (vram_usage_gb, priority)
                        return True
            
            # 如果仍然显存不足：返回False（加载失败）
            print(f"[VRAM Scheduler] ❌ Failed to load {model_name}: insufficient VRAM even after unloading.")
            return False
    
    def unload_all_temp_models(self):
        """卸载所有临时模型（LoRA/ControlNet），保留Checkpoint"""
        models_to_remove = [name for name, (_, priority) in self.loaded_models.items() if priority < 10]
        for model in models_to_remove:
            del self.loaded_models[model]
            print(f"[VRAM Scheduler] Unloaded temp model: {model}")
> 📄 代码已提取到 `references\code_86.txt`（4 行，26 字节）
> 需要查看完整代码时请读取该文件。

python
def log_performance_metrics(task_id, metrics, reward_system=None):
    """
    记录性能指标（优化版 - v5.0）
    
    新增功能：
    - 记录奖励系统状态（batch size变化）
    - 记录显存碎片化率
    - 自动触发显存整理（如果碎片化 > 30%）
    """
    log_file = "performance_log.jsonl"
    
    # 检查显存碎片化
    fragmentation = defragment_vram()
    
    log_entry = {
        "task_id": task_id,
        "timestamp": time.time(),
        "metrics": metrics,
        "vram_fragmentation": fragmentation,
        "batch_size": reward_system.current_batch_size if reward_system else 1,
        "high_quality_mode": reward_system.high_quality_mode if reward_system else False
    }
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    
    # 异常检测（优化版 - v5.0）
    if metrics.get("vram_usage_mb", 0) > 7000:
        print(f"[WARNING] High VRAM usage: {metrics['vram_usage_mb']} MB")
    if metrics.get("generation_time_s", 0) > 60:
        print(f"[WARNING] Slow generation: {metrics['generation_time_s']} s")
    if fragmentation > 30:
        print(f"[WARNING] High VRAM fragmentation: {fragmentation:.1f}%. Triggering defrag...")
        defragment_vram()
> 📄 代码已提取到 `references\code_87.txt`（9 行，122 字节）
> 需要查看完整代码时请读取该文件。

markdown
### 1. Basic Prompt Structure:
(masterpiece, best quality, ultra-detailed) + [subject description] + [material/finish + DEFECT PREVENTION] + [environment/background] + [composition/angle] + [lighting + PHYSICAL CORRECTNESS] + [style words] + [LoRA trigger word]

### 2. Advanced Prompt Techniques:
- **Weight control**: (keyword:1.2) or [keyword:0.8]
- **Mixed styles**: [style1:0.6] [style2:0.4]
- **Detail enhancement**: ultra-detailed, 8K uhd, ray tracing, anisotropic reflection

### 3. LoRA Model Library (50+ models):
| Model Name | Trigger Word | Best For | Weight Range | Defect Prevention |
|------------|---------------|----------|--------------|----------------------|
| Vacuum Cup Pro | vacuum_cup_pro | Product photography | 0.6-0.9 | Prevents plastic texture |
| Brushed Metal | brushed_metal | Metal texture | 0.4-0.7 | Adds anisotropic reflection |
| Perfect Symmetry | symmetric_lid | Lid/front view | 0.8-1.0 | Prevents asymmetric lid |

### 4. Defect Prevention Keywords (Must Include):
- Prevent plastic texture: anisotropic reflection, brushed metal, physical based rendering
- Prevent asymmetric lid: perfectly symmetric lid, centered pop-up button
- Prevent color inaccuracy: color accurate, Delta E < 3, real photography colors
- Prevent text artifacts: no text, no watermark, clean logo
> [引用] 完整代码已提取到 `references\code_block_88.txt`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_88.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。


python
def calculate_generation_quality(image, prompt, reference=None):
    """Calculate generation quality score (0-10)"""
    # Prompt Adherence (0-10)
    prompt_adherence = calculate_clip_similarity(image, prompt)
    
    # Image Quality (0-10)
    image_quality = calculate_iqa_metrics(image, reference)
    
    # Artifact Free (0-10)
    artifact_free = detect_artifacts(image)
    
    # Diversity (0-10): If generating multiple images
    diversity = calculate_diversity(image_set)
    
    quality_score = (prompt_adherence + image_quality + artifact_free + diversity) / 4
    return round(quality_score, 1)
> 📄 代码已提取到 `references\code_89.txt`（8 行，145 字节）
> 需要查看完整代码时请读取该文件。

python
def compare_generations(current_image, reference_image, past_generations):
    """Compare current generation with reference and past generations"""
    comparison = {
        'reference_similarity': calculate_similarity(current_image, reference_image),
        'past_diversity': calculate_diversity(current_image, past_generations),
        'improvement': calculate_improvement(current_image, past_generations[-1])
    }
    return comparison
```

---

## Phase 4: ComfyUI API调用 (NEW in v6.0)

**Objective**: 通过ComfyUI API实现程序化图像生成，支持批量生成和自动化工作流。

### 4.1 ComfyUI API接口说明

ComfyUI提供REST API接口，支持以下功能：
- `POST /prompt` - 提交生成任务
- `GET /queue` - 查询任务队列
- `GET /history` - 查询生成历史
- `GET /view` - 获取生成图片

**API Base URL**: `http://localhost:8188`

### 4.2 API调用示例 (Python)

**安装依赖**:
```bash
pip install requests websocket-client
```

**基础调用脚本**:
```python
import requests
import json
import time
import base64
from io import BytesIO
from PIL import Image

class ComfyUIClient:
    def __init__(self, base_url="http://localhost:8188"):
        self.base_url = base_url
        self.client_id = "zheng10_ai_image_generator"
    
    def queue_prompt(self, prompt_workflow):
        """提交生成任务到ComfyUI队列"""
        payload = {
            "prompt": prompt_workflow,
            "client_id": self.client_id
        }
        response = requests.post(f"{self.base_url}/prompt", json=payload)
        return response.json()
    
    def get_queue_status(self):
        """获取当前队列状态"""
        response = requests.get(f"{self.base_url}/queue")
        return response.json()
    
    def get_history(self, max_items=10):
        """获取生成历史"""
        response = requests.get(f"{self.base_url}/history")
        history = response.json()
        # 返回最近max_items个任务
        sorted_keys = sorted(history.keys(), reverse=True)
        return {k: history[k] for k in sorted_keys[:max_items]}
    
    def download_image(self, filename, subfolder="", folder_type="output"):
        """下载生成的图片"""
        params = {
            "filename": filename,
            "subfolder": subfolder,
            "type": folder_type
        }
        response = requests.get(f"{self.base_url}/view", params=params)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        return None
    
    def wait_for_completion(self, prompt_id, timeout=300):
        """等待任务完成"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            history = self.get_history()
            if prompt_id in history:
                task_info = history[prompt_id]
                if task_info.get("outputs"):
                    return task_info["outputs"]
            time.sleep(2)
        raise TimeoutError(f"Task {prompt_id} timeout after {timeout}s")

# 使用示例
if __name__ == "__main__":
    client = ComfyUIClient()
    
    # 1. 加载工作流JSON
    with open("workflow_api.json", "r") as f:
        workflow = json.load(f)
    
    # 2. 修改工作流参数（如prompt、种子等）
    workflow["5"]["inputs"]["text"] = "保温杯产品图，不锈钢材质，极简设计"
    workflow["6"]["inputs"]["seed"] = random.randint(0, 2**32-1)
    
    # 3. 提交任务
    result = client.queue_prompt(workflow)
    prompt_id = result["prompt_id"]
    print(f"Task queued: {prompt_id}")
    
    # 4. 等待完成
    outputs = client.wait_for_completion(prompt_id)
    print(f"Task completed: {outputs}")
    
    # 5. 下载图片
    for node_id, node_output in outputs.items():
        if "images" in node_output:
            for img_info in node_output["images"]:
                img = client.download_image(
                    img_info["filename"],
                    img_info["subfolder"],
                    img_info["type"]
                )
                if img:
                    img.save(f"output_{img_info['filename']}")
                    print(f"Image saved: output_{img_info['filename']}")
```

### 4.3 批量生成脚本

支持从CSV文件读取参数，批量生成图片：

```python
import csv
import random

def batch_generate_from_csv(csv_file, workflow_template, output_dir="output"):
    """从CSV批量生成图片"""
    client = ComfyUIClient()
    
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    results = []
    for i, row in enumerate(rows):
        print(f"Generating {i+1}/{len(rows)}: {row['prompt']}")
        
        # 复制工作流模板
        workflow = json.loads(json.dumps(workflow_template))
        
        # 替换参数
        workflow["5"]["inputs"]["text"] = row["prompt"]
        workflow["6"]["inputs"]["seed"] = random.randint(0, 2**32-1)
        workflow["7"]["inputs"]["batch_size"] = int(row.get("batch_size", 1))
        
        # 提交任务
        result = client.queue_prompt(workflow)
        prompt_id = result["prompt_id"]
        
        # 等待完成
        try:
            outputs = client.wait_for_completion(prompt_id)
            results.append({
                "row_index": i,
                "prompt": row["prompt"],
                "prompt_id": prompt_id,
                "outputs": outputs,
                "status": "success"
            })
        except TimeoutError as e:
            results.append({
                "row_index": i,
                "prompt": row["prompt"],
                "prompt_id": prompt_id,
                "status": "timeout",
                "error": str(e)
            })
        
        # 避免过热，每5个任务休息10秒
        if (i + 1) % 5 == 0:
            print("Resting for 10s...")
            time.sleep(10)
    
    return results

# CSV格式示例:
# prompt,batch_size,negative_prompt
# 保温杯产品图_不锈钢,1,plastic texture
# 保温杯产品图_钛合金,2,fake metal
```

### 4.4 工作流API格式转换

将ComfyUI可视化工作流转换为API格式：

```python
def convert_workflow_to_api(workflow_json):
    """将可视化工作流JSON转换为API格式"""
    api_workflow = {}
    
    for node in workflow_json["nodes"]:
        node_id = str(node["id"])
        api_workflow[node_id] = {
            "class_type": node["type"],
            "inputs": {}
        }
        
        # 转换输入参数
        for input_name, input_value in node["inputs"].items():
            if isinstance(input_value, dict) and "link" in input_value:
                # 连接输入：需要查找源节点
                source_link = input_value["link"]
                # 在实际实现中，需要遍历所有节点找到源
                api_workflow[node_id]["inputs"][input_name] = []
            else:
                # 固定值输入
                api_workflow[node_id]["inputs"][input_name] = input_value
    
    return api_workflow

# 使用ComfyUI内置功能更简单：
# 1. 在ComfyUI界面完成工作流设计
# 2. 点击"Save (API Format)"按钮
# 3. 直接保存为API格式JSON
```

### 4.5 常见错误处理

| 错误类型 | 原因 | 解决方案 |
|----------|------|----------|
| `500 Internal Server Error` | 工作流JSON格式错误 | 检查JSON语法，使用ComfyUI内置保存功能 |
| `Task timeout` | 生成时间超过等待时间 | 增加timeout参数，或优化工作流 |
| `CUDA out of memory` | 显存不足 | 减少batch_size，使用低显存模型 |
| `Connection refused` | ComfyUI服务未启动 | 启动ComfyUI: `python main.py` |

---

## Phase 7.9: Memory Compression (NEW in v3.5)

**Objective**: Compress generation history for token efficiency.

### Token Budget: 2000 tokens
- Prompt: 300 tokens
- Generation parameters: 200 tokens
- Quality metrics: 500 tokens
- Comparative analysis: 500 tokens
- Output: 500 tokens


### Usage

当需要此技能时，按以下步骤执行：

1. **理解需求**: 明确用户的核心意图
2. **调用流程**: 按照核心职责定义执行
3. **输出验证**: 检查输出是否符合预期
4. **反馈迭代**: 根据评审结果调整方案

## 注意事项

- 执行前确保依赖工具已安装
- 如遇报错请查看详细日志输出
- 重要步骤需人工确认后再执行


## 语言说明
本文档使用简体中文编写，请确保所有操作输出也为中文。

## Language Note
建议使用中文输出。

## Language Note
建议使用中文输出。


---

## Phase 7: 生图质量自适应优化 (NEW in v7.2)

> **重要**: 本章节提供生图质量自适应优化方法，根据🐔鸡的评审反馈，自动调整生图参数，提升输出质量。

### 7.1 质量自适应优化原理

**核心思路**: 根据评审反馈，识别生图过程中的质量问题，自动调整Prompt、采样参数、LoRA权重等，提升下次生图质量。

**优化循环**:
```
生图 → 🐔鸡评审 → 接收反馈 → 分析质量问题 → 调整参数 → 重新生图 → 再次评审
```

### 7.2 质量问题识别与参数调整

| 低分维度 | 参数调整方向 | 具体调整方法 |
|----------|--------------|--------------|
| **结构准确性** < 8.0 | 增强结构关键词 | 增加结构描述细节，提升Prompt中结构关键词权重 |
| **材质真实感** < 8.0 | 调整LoRA权重 | 增加材质LoRA权重（0.6→0.8），或换用更专业的材质LoRA |
| **CMF一致性** < 8.0 | 优化CMF描述 | 在Prompt中增加具体CMF描述（颜色代码、材质名称、工艺术语） |
| **光影质量** < 8.0 | 调整光照参数 | 降低光照强度（1.0→0.8），启用HDR tone mapping |
| **DFM风险** < 6.0 | 简化设计 | 在Prompt中避免过度复杂的纹理描述 |
| **商业吸引力** < 8.0 | 优化风格 | 根据目标用户偏好，调整风格关键词 |

### 7.3 自适应优化算法

```python
def adaptive_optimize(review_feedback, current_params):
    """
    根据评审反馈，自适应优化生图参数
    
    Args:
        review_feedback: 🐔鸡的评审反馈
        current_params: 当前生图参数
    
    Returns:
        optimized_params: 优化后的参数
    """
    
    optimized_params = current_params.copy()
    
    # 1. 分析评审反馈
    dimension_scores = review_feedback["dimension_scores"]
    
    # 2. 对每个低分维度，调整相关参数
    for dim, score in dimension_scores.items():
        if score < 8.0:  # 低分维度
            
            if dim == "material_realism":
                # 材质真实感不足 → 增加LoRA权重
                optimized_params["lora_weight"] = min(1.0, optimized_params.get("lora_weight", 0.6) + 0.1)
                # 增加材质关键词
                optimized_params["prompt"] += ", highly detailed material texture, realistic metal brushed"
            
            elif dim == "lighting_quality":
                # 光影质量不足 → 调整光照参数
                optimized_params["light_strength"] = 0.8
                optimized_params["hdr_tone_mapping"] = True
                # 增加光影关键词
                optimized_params["prompt"] += ", studio lighting, soft shadows, anisotropic reflection"
            
            elif dim == "structure_accuracy":
                # 结构准确性不足 → 增加结构关键词权重
                optimized_params["prompt"] += ", precise structural design, accurate proportions"
                # 使用更详细的Prompt
                optimized_params["prompt_detail_level"] = "high"
    
    # 3. 调整采样参数（通用优化）
    if review_feedback["total_score"] < 7.0:
        # 总分较低 → 增加采样步数，提升质量
        optimized_params["steps"] = min(50, optimized_params.get("steps", 30) + 10)
        # 降低CFG scale，让AI更自由发挥
        optimized_params["cfg_scale"] = max(5.0, optimized_params.get("cfg_scale", 7.5) - 0.5)
    
    return optimized_params
```

### 7.4 优化效果验证

```python
def verify_optimization(original_image, optimized_image, review_feedback):
    """验证优化效果（比较优化前后的评审评分）"""
    
    # 1. 对原图评分
    original_score = review_feedback["total_score"]
    
    # 2. 对优化后图片评分
    optimized_review = review_image(optimized_image)
    optimized_score = optimized_review["total_score"]
    
    # 3. 计算提升
    improvement = optimized_score - original_score
    
    if improvement > 0:
        print(f"✅ 优化有效！评分提升: {original_score:.1f} → {optimized_score:.1f} (+{improvement:.1f})")
        return True, optimized_score
    else:
        print(f"❌ 优化无效！评分未提升: {original_score:.1f} → {optimized_score:.1f} ({improvement:.1f})")
        return False, original_score
```

### 7.5 自适应优化工作流

```python
# 完整自适应优化工作流

# 1. 初始生图
current_params = {
    "prompt": "A vacuum cup with pop-up lid, titanium material",
    "lora_weight": 0.6,
    "steps": 30,
    "cfg_scale": 7.5
}
image = generate_image(current_params)

# 2. 评审
review_feedback = review_image(image)

# 3. 如果未通过，自适应优化
max_iterations = 5
for i in range(max_iterations):
    if review_feedback["verdict"] in ["pass", "conditional_pass"]:
        print(f"✅ 通过评审！迭代次数: {i+1}")
        break
    
    print(f"⚠️ 未通过评审，开始第{i+1}次优化...")
    
    # 自适应优化参数
    optimized_params = adaptive_optimize(review_feedback, current_params)
    
    # 重新生图
    image = generate_image(optimized_params)
    
    # 再次评审
    review_feedback = review_image(image)
    
    # 更新当前参数
    current_params = optimized_params

# 4. 输出最终结果
print(f"最终评分: {review_feedback['total_score']:.1f}")
print(f"最终 verdict: {review_feedback['verdict']}")
```

### 7.6 优化性能指标

| 指标 | 当前值 | 目标值 | 优化措施 |
|------|--------|--------|----------|
| **首次通过率** | 40% | 70% | 更好的自适应优化算法 |
| **平均迭代次数** | 3.5次 | 2.0次 |  faster convergence |
| **评分提升幅度** | +0.5/次 | +0.8/次 | 更精准的参数调整 |
| **优化时间** | 15分钟 | 8分钟 | 并行生图、缓存优化结果 |

---

*Phase 7新增于v7.2 | 最后更新: 2026-06-19 | 维护者: 猴哥*
*> v7.2新增: 生图质量自适应优化（质量问题识别、参数调整、优化算法、效果验证、性能指标）*

---

> **版本**: v7.2 (新增生图质量自适应优化)  
> **更新时间**: 2026-06-19 02:32  
> **维护者**: 🐑 羊 × 工程狮 × 🐔 鸡  
> **联动**: 接收🐔鸡评审反馈 → 自适应优化生图参数 → 重新生图 → 提升评审通过率

---

## 参考资料

### ComfyUI API集成

- **统一指南**: `H:/AI日记/Claw/十二生肖团_ComfyUI_API集成统一指南_V1.0_2026-06-18.md`
  - 所有API接口调用示例
  - 工作流JSON模板说明
  - 错误处理与性能优化

### 相关文档

| 文档 | 路径 | 说明 |
|------|------|------|
| ComfyUI安装指南 | `H:/AI日记/Claw/ComfyUI_安装与API化指南_V1.0.md` | 安装与配置 |
| ComfyUI API调用指南 | `H:/AI日记/Claw/ComfyUI_工作流API调用指南_V1.0.md` | 详细API文档 |
| ComfyUI工作流模板库 | `H:/AI日记/Claw/ComfyUI_工作流模板库_V1.0.md` | 工作流模板 |
| 框架报告V8.0 | `H:/AI日记/Claw/十二生肖团_完整详细框架报告_V8.0_2026-06-18.md` | 最新框架 |

---
