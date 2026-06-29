---
name: zheng10-standards-analyst
description: "auto-generated: skill package 'zheng10-standards-analyst' (awaiting human review)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "新增Phase 6: DFM自动化检查与标准合规验证"
  upgrade_date: "2026-06-19"
  tags: ["dfm", "standard-compliance", "auto-check", "agent-collaboration"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# Workflow Standards & DFM Analysis — 牛 (Ox) v7.0

**Role**: Standards enforcer and manufacturability analyst. Ensure designs meet industry standards and can be mass-produced.

**Core Principle (v3.5)**: Standards first, then design. **Defect prevention nodes MUST be included in all ComfyUI workflows.**

---

## Phase 1.2: ComfyUI Node Library (NEW in v5.0)

**Complete ComfyUI node library (50+ nodes)**:

> [引用] 完整代码已提取到 `references\code_block_01.txt`（60 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_01.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




**Output**: ComfyUI Node Library (JSON format, can be imported into ComfyUI)

---

## Phase 2: DFM (Design for Manufacturability) Analysis:

When receiving design files from 蛇 (Snake) or 鼠 (Rat):

> 📄 代码已提取到 `references\code_02.txt`（12 行，572 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: DFM (Design for Manufacturability) Analysis:

For **3D models** (from 蛇), perform DFM analysis:

> 📄 代码已提取到 `references\code_03.txt`（18 行，877 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.5: Defect Prevention Node Standards (NEW in v3.5):

**When reviewing ComfyUI workflows (from 马), CHECK for these post-processing nodes**:

> [引用] 完整代码已提取到 `references\code_block_04.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_04.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 3: Applicable Standards Matrix:

| Standard Type | China | USA | EU | Yongkang Local Supply |
|---------------|-------|-----|-----|----------------------|
| Material Safety | GB 4806 | FDA 21 CFR | EC 1935/2004 | ✅ 304/316 stainless available |
| Thermal Performance | GB/T 29606 | ASTM C240 | EN 12546 | ✅ Local testing available |
| Mechanical Safety | GB 4706 | UL 1082 | EN 60335 | ✅ Drop test lab local |
| Labeling | GB 5296 | FTC labeling | EU labeling | ⚠️ Need confirmation |
> 📄 代码已提取到 `references\code_05.txt`（13 行，476 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 5: Standards Compliance Report Output:

> 📄 代码已提取到 `references\code_06.txt`（12 行，377 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 6: Workflow Standardization (ComfyUI) (v3.5 Enhanced):

For **ComfyUI workflows** (from 马), check standards compliance:

> 📄 代码已提取到 `references\code_07.txt`（12 行，338 字节）
> 需要查看完整代码时请读取该文件。


- Receive: task assignment with design files
- Extract: product type, target market, compliance requirements
- Output: standards compliance report + DFM report + **defect prevention checklist (NEW in v3.5)**:
- Receive: 3D model + 2D drawings
- Extract: structural features, material selection
- Output: DFM manufacturability report + **defect prevention node recommendations (NEW in v3.5)**:
- If: standards compliance < 7.0 OR DFM score < 7.0
- Provide: detailed feedback, specific fix schemes
- 蛇 will: redesign and resubmit:
- 猴 will: optimize parameters for cost reduction
  ... (省略中间部分) ...
    "cfg": 7.0,
    "denoise": 1.0
  },
  "variants": {
    "sdxl_photorealistic": {"steps": 40, "cfg": 7.0},
    "sdxl_product": {"steps": 35, "cfg": 8.0},
    "lightning_fast": {"steps": 8, "cfg": 2.0, "sampler_name": "euler"},
    "img2img_refinement": {"denoise": 0.6, "steps": 25}
  }
}
> 📄 代码已提取到 `references\code_08.txt`（3 行，7 字节）
> 需要查看完整代码时请读取该文件。

json
- {
- "node": "CLIPTextEncode",
- "positive_template": {
- "product_type": "product photography",
- "material": "[material] texture, anisotropic reflection",
- "lighting": "studio lighting, softbox, rim light",
- "quality": "8k, photorealistic, highly detailed, sharp focus",
- "background": "pure white background, clean, minimal"
- },
- "negative_template": {
- "defects": "plastic texture, fake metal, blurry, low quality",
- "artifacts": "watermark, text, signature, garbled text",
- "composition": "cropped, out of frame, worst quality"
- }
- }
> 📄 代码已提取到 `references\code_09.txt`（3 行，35 字节）
> 需要查看完整代码时请读取该文件。

json
{
  "node": "CheckpointLoaderSimple",
  "standard_models": {
    "sdxl_realistic": "realisticVisionV60B1_v51VAE.safetensors",
    "sdxl_product": "productDesign_eddiemauro16.safetensors",
    "sd15_photorealistic": "realisticVisionV51_v51VAE.safetensors",
    "lightning_fast": "SDXL-Lightning.safetensors"
  },
  "vae": "vae-ft-mse-840000-ema-pruned.safetensors"
}
> 📄 代码已提取到 `references\code_10.txt`（5 行，29 字节）
> 需要查看完整代码时请读取该文件。

json
- {
- "node": "ControlNetApply",
- "standard_config": {
- "control_net": "control_v11p_sd15_canny.pth",
- "strength": 0.85,
- "start_percent": 0.0,
- "end_percent": 1.0
- },
- "product_specific": {
- "cylindrical_products": {"strength": 0.90, "preprocessor": "CannyEdgePreprocessor"},
- "complex_lids": {"strength": 1.0, "preprocessor": "CannyEdgePreprocessor"},
- "handle_details": {"strength": 0.80, "preprocessor": "CannyEdgePreprocessor"}
- }
- }
> 📄 代码已提取到 `references\code_11.txt`（3 行，41 字节）
> 需要查看完整代码时请读取该文件。


{
  "node": "ControlNetApply",
  "standard_config": {
    "control_net": "control_v11f1p_sd15_depth.pth",
    "strength": 0.75,
    "preprocessor": "MiDaS-DepthMapPreprocessor"
  }
}
> 📄 代码已提取到 `references\code_12.txt`（3 行，49 字节）
> 需要查看完整代码时请读取该文件。


{
  "node": "ControlNetApply",
  "standard_config": {
    "control_net": "control_v11p_sd15_openpose.pth",
    "strength": 0.70,
    "preprocessor": "OpenposePreprocessor"
  }
}
> 📄 代码已提取到 `references\code_13.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


{
  "node": "FaceDetailer",
  "standard_config": {
    "guide_size": 512,
    "guide_size_for": True,
    "max_size": 1024,
    "seed": -1,
    "steps": 20,
    "cfg": 8.0,
    "sampler_name": "dpmpp_2m",
    "scheduler": "karras",
    "denoise": 0.4
  },
  "product_adaptation": {
    "detail_regions": ["lid", "handle", "logo_area"],
    "mask_expansion": 20
  }
}
> 📄 代码已提取到 `references\code_14.txt`（3 行，23 字节）
> 需要查看完整代码时请读取该文件。


{
  "node": "ImageSharpen",
  "standard_config": {
    "sharpen_radius": 1.0,
    "sigma": 1.0,
    "alpha": 0.5
  }
}
> 📄 代码已提取到 `references\code_15.txt`（3 行，23 字节）
> 需要查看完整代码时请读取该文件。


{
  "node": "ColorCorrect",
  "standard_config": {
    "temperature": 0.0,
    "tint": 0.0,
    "saturation": 1.0,
    "contrast": 1.0
  },
  "product_specific": {
    "metal_products": {"contrast": 1.1, "saturation": 0.95},
    "matte_products": {"contrast": 1.05, "saturation": 0.90}
  }
}
> 📄 代码已提取到 `references\code_16.txt`（5 行，31 字节）
> 需要查看完整代码时请读取该文件。

json
    # ... (代码已精简，保留核心逻辑) ...
- "weight": 0.5,
- "trigger_words": "raw titanium, anisotropic reflection, physical based rendering"
- }
- }
- }
> 📄 代码已提取到 `references\code_17.txt`（5 行，82 字节）
> 需要查看完整代码时请读取该文件。


[Load Checkpoint] → [Load LoRA] → [CLIPTextEncode+] → [CLIPTextEncode-]
    ↓
[Load Image] → [CannyPreprocessor] → [ControlNetApply]
    ↓
[KSampler] → [VAEDecode] → [FaceDetailer] → [ColorCorrect] → [Save Image]
> 📄 代码已提取到 `references\code_18.txt`（3 行，47 字节）
> 需要查看完整代码时请读取该文件。


[Load Checkpoint] → [Load LoRA] → [CLIPTextEncode+] → [CLIPTextEncode-]
    ↓
[Load Image] → [DepthPreprocessor] → [ControlNetApply]
    ↓
[KSampler] → [VAEDecode] → [ImageSharpen] → [ColorCorrect] → [Save Image]
> 📄 代码已提取到 `references\code_19.txt`（3 行，47 字节）
> 需要查看完整代码时请读取该文件。


[Load Checkpoint] → [Load LoRA] → [CLIPTextEncode+] → [CLIPTextEncode-]
    ↓
[Load Image] → [CannyPreprocessor] → [ControlNetApply] (strength=1.0)
    ↓
[KSampler] (CFG=8.0) → [VAEDecode] → [FaceDetailer] → [Save Image]
> 📄 代码已提取到 `references\code_20.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。

python
def validate_workflow(workflow_json):
    """Validate ComfyUI workflow against standard node library"""
    required_nodes = [
        "CheckpointLoaderSimple",
        "CLIPTextEncode",
        "KSampler",
        "VAEDecode"
    ]
    recommended_nodes = [
  ... (省略中间部分) ...
            defects.append("KSampler CFG < 6.0 (risk: prompt ignored)")
    if "ControlNetApply" in workflow_json:
        cn = workflow_json["ControlNetApply"]
        if cn.get("strength", 0) < 0.8:
            defects.append("ControlNet strength < 0.8 (risk: structural deformation)")
    return {
        "passed": len(defects) == 0,
        "defects": defects,
        "score": max(0, 10 - len(defects) * 1.5)
    }
> 📄 代码已提取到 `references\code_21.txt`（15 行，148 字节）
> 需要查看完整代码时请读取该文件。

json
- {
- "timestamp": "2026-06-04T14:30:00+08:00",
- "agent_id": "zheng10-product-researcher",
- "task_id": "task_20260604_001",
- "status": "success | partial | failed",
- "result": {
- "summary": "Brief description of result",
- "data": { ... },  // Main output data
- "warnings": [ ... ],  // Non-blocking issues
- "errors": [ ... ]  // Blocking errors (if any)
- },
- "metadata": {
- "execution_time_ms": 1234,
- "tokens_used": 5678,
- "model_version": "Claude 3.7"
- }
- }
> 📄 代码已提取到 `references\code_22.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


**Agent**: [agent_id]
**Timestamp**: [timestamp]
**Task ID**: [task_id]
[Brief summary of result]
[Detailed content...]
- [ ] Requirement met
- [ ] No hallucinations
- [ ] Format consistent
- [ ] References valid
[If partial/failed, what to do next]
> 📄 代码已提取到 `references\code_23.txt`（15 行，449 字节）
> 需要查看完整代码时请读取该文件。


Output Quality Checklist (ALL agents MUST verify):

[ ] Format matches template (JSON/Markdown/Table)
[ ] All required fields present (timestamp/agent_id/task_id/status)
[ ] No hallucinated data (check numbers/references)
[ ] Consistent terminology (use agreed terms, not synonyms)
[ ] Proper encoding (UTF-8, no mojibake)
[ ] Readable (proper line breaks, indentation)
> 📄 代码已提取到 `references\code_24.txt`（12 行，181 字节）
> 需要查看完整代码时请读取该文件。


**Partial Example (Markdown)**:
> 📄 代码已提取到 `references\code_25.txt`（15 行，648 字节）
> 需要查看完整代码时请读取该文件。



要点：
- **Failed Example (JSON)**:
- > [引用] 完整代码已提取到 `references\code_block_26.json`（25 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_26.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




**Execution Rules (NEW in v3.5)**:
18. **ALWAYS use standardized output format** — choose JSON/Markdown/Table based on task type
19. **ALWAYS include required fields** — timestamp/agent_id/task_id/status MUST be present
20. **ALWAYS validate output quality** — run Output Quality Checklist before returning

---



### Three-Tier Memory Compression:
> 📄 代码已提取到 `references\code_27.txt`（15 行，637 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_28.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_28.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




### Auto-Trigger Conditions:
| Condition | Action | Compression Level |
|-----------|--------|-------------------|
| Session ends normally | Compress daily log → weekly summary | Level 1→2 |
| Daily log > 500 lines | Auto-compress to weekly | Level 1→2 |
| 4 weekly summaries accumulated | Compress to monthly digest | Level 2→3 |
| MEMORY.md > 3000 chars | Remove lowest-score entries | Level 3 cleanup |
| User says "压缩记忆" / "compress memory" | Force compression all levels | Full compression |

### Memory Retrieval Optimization:
> [引用] 完整代码已提取到 `references\code_block_29.txt`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_29.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



**Execution Rules (NEW in v3.5)**:
15. **ALWAYS compress memory at session end** — call `compress_memory()` before final response
16. **ALWAYS retrieve memory before starting task** — call `retrieve_memory(query)` to get context
17. **ALWAYS respect memory limits** — daily log ≤500 lines, MEMORY.md ≤3000 chars
**Previously, agents did NOT learn from past experiences. v3.4 adds SELF-EVOLVING capability.**
> 📄 代码已提取到 `references\code_30.txt`（16 行，590 字节）
> 需要查看完整代码时请读取该文件。



**Rating Criteria (0-10)**:
| Score | Meaning | Action |
|-------|----------|--------|
| 9.0-10.0 | Excellent | Keep current approach |
| 7.0-8.9 | Good | Minor optimization |
| 5.0-6.9 | Marginal | Major optimization needed |
| <5.0 | Poor | Redesign approach |

### B. Success/Failure Case Database:

> [引用] 完整代码已提取到 `references\code_block_31.txt`（37 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_31.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> 📄 代码已提取到 `references\code_32.txt`（18 行，932 字节）
> 需要查看完整代码时请读取该文件。



### D. Self-Evolution Triggers:

| Trigger Condition | Action | Example |
|-------------------|--------|---------|
| Average score < 6.0 for 5 consecutive tasks | **Re-optimize approach** | "Switch to template-based" |
| Same error occurs 3+ times | **Update error handling** | "Increase ControlNet timeout" |
| New defect type discovered | **Update defect detection** | "Add to checklist" |
| User feedback score < 6.0 | **Re-learn from feedback** | "Increase anisotropic weight" |

### E. Learning Loop:

> 📄 代码已提取到 `references\code_33.txt`（3 行，135 字节）
> 需要查看完整代码时请读取该文件。



---

## Error Handling & Retry Mechanism (NEW in v3.3)

    # ... (代码已精简，保留核心逻辑) ...
- "error_code": "ERR_TIMEOUT|ERR_FORMAT|ERR_DEPENDENCY|ERR_RESOURCE|ERR_CIRCULAR",
- "error_message": "错误详情（中文）",
- "recovery_action": "重试|降级|上报"
- }
- }
> [引用] 完整代码已提取到 `references\code_block_34.txt`（22 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_34.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




#### 示例 1: 鼠（Product Researcher）输出示例
> [引用] 完整代码已提取到 `references\code_block_35.txt`（41 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_35.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_36.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_36.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

### C. 表格输出模板（标准化格式）

#### 通用规则:
1. **表格标题**: 必须中文，简洁明了
2. **表格列宽**: 根据内容自动调整，保持对齐
3. **表格对齐**: 数字右对齐，文本左对齐，表头居中
4. **表格分隔线**: 使用 `|-----|------|-----|` 格式

#### 标准化表格模板:
> 📄 代码已提取到 `references\code_37.txt`（6 行，255 字节）
> 需要查看完整代码时请读取该文件。



#### 示例: 任务状态跟踪表格
> 📄 代码已提取到 `references\code_38.txt`（7 行，487 字节）
> 需要查看完整代码时请读取该文件。



---

### D. JSON Schema 验证规则（NEW in v4.3）

    # ... (代码已精简，保留核心逻辑) ...
- }
- }
- }
- }
- }
> 📄 代码已提取到 `references\code_39.txt`（14 行，409 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST be in 简体中文 (Simplified Chinese)
- NO English outputs allowed (except code/technical terms)
- ALL error messages MUST be in Chinese
- ALL user interactions MUST be in Chinese
- Reason: 用户是中文母语者，必须确保沟通零障碍
> 📄 代码已提取到 `references\code_40.txt`（3 行，29 字节）
> 需要查看完整代码时请读取该文件。

markdown
✅ 正确 (Correct):
  "已成功生成图像，质量评分：8.5/10"

❌ 错误 (Wrong):
  "Image generated successfully, quality score: 8.5/10"
> 📄 代码已提取到 `references\code_41.txt`（5 行，57 字节）
> 需要查看完整代码时请读取该文件。


- ALL tasks MUST follow 十二生肖团 workflow (7 phases)
- NO skipping phases without explicit user approval
- ALL phase transitions MUST be documented
- ALL task assignments MUST go through 鼠 (Rat)
- Reason: 确保协作有序，避免混乱和重复劳动
> 📄 代码已提取到 `references\code_42.txt`（3 行，22 字节）
> 需要查看完整代码时请读取该文件。


1. 需求分析 → 鼠 (Rat)
2. 市场调研 → 虎/兔/龙 (Tiger/Rabbit/Dragon)
3. 产品设计 → 蛇 (Snake)
4. 成本分析 → 牛 (Ox)
5. AI生图 → 马/羊/猴 (Horse/Goat/Monkey)
6. 设计评审 → 鸡 (Rooster)
7. 品牌设计 → 猪 (Pig)
> 📄 代码已提取到 `references\code_43.txt`（5 行，53 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST pass quality checklist (see Output Template Specification)
- ALL generated images MUST be reviewed by 鸡 (Rooster)
- NO low-quality output allowed (< 7.0/10)
- ALL errors MUST be logged + analyzed
- Reason: 质量是第一生命线，劣质输出 = 团队失信
> 📄 代码已提取到 `references\code_44.txt`（13 行，320 字节）
> 需要查看完整代码时请读取该文件。


- ALL errors MUST be logged to error log file
- ALL errors MUST include: timestamp, agent_id, error_code, root_cause, fix_action
- ALL errors MUST be categorized (P0/P1/P2)
- ALL P0 errors MUST trigger immediate alert to 鼠 (Rat)
- Reason: 错误是进步的阶梯，不记录 = 重复犯错
> 📄 代码已提取到 `references\code_45.txt`（3 行，32 字节）
> 需要查看完整代码时请读取该文件。

yaml
- timestamp: "2026-06-04T15:30:00+08:00"
  agent_id: "zheng10-sd-comfy-expert"
  error_code: "ERR_TIMEOUT"
  severity: "P1"
  root_cause: "ComfyUI server not reachable"
  fix_action: "Check if ComfyUI server is running"
  resolved: false
> 📄 代码已提取到 `references\code_46.txt`（5 行，49 字节）
> 需要查看完整代码时请读取该文件。


- ALL inter-agent communication MUST use structured JSON (see Structured Communication Protocol)
- NO free-text communication allowed (causes misunderstandings)
- ALL task dependencies MUST be declared upfront
- ALL blockers MUST be reported immediately to 鼠 (Rat)
- Reason: 团队协作需要结构化沟通，模糊信息 = 延误工期
> 📄 代码已提取到 `references\code_47.txt`（3 行，36 字节）
> 需要查看完整代码时请读取该文件。

json
{
  "from": "zheng10-product-researcher",
  "to": "zheng10-sd-comfy-expert",
  "message_type": "task_assignment",
  "payload": {
    "task_id": "gen_20260604_001",
    "requirements": "...",
    "deadline": "2026-06-04T17:00:00+08:00"
  },
  "priority": "high"
}
> 📄 代码已提取到 `references\code_48.txt`（5 行，55 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST record successful cases to CaseDatabase (see Learning & Evolution Mechanism)
- ALL agents MUST record failed cases to CaseDatabase
- ALL agents MUST optimize prompts based on past cases
- ALL agents MUST update own SKILL.md when new learning discovered
- Reason: 不学习 = 停滞不前，团队竞争力下降
> 📄 代码已提取到 `references\code_49.txt`（3 行，27 字节）
> 需要查看完整代码时请读取该文件。


Generate → Assess → Record (success/failure) → Optimize → Regenerate
> 📄 代码已提取到 `references\code_50.txt`（5 行，48 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST stay within own role boundaries
- NO role overflow (e.g., 虎 (Tiger) MUST NOT do 鸡 (Rooster)'s job)
- ALL cross-role tasks MUST be coordinated by 鼠 (Rat)
- ALL role conflicts MUST be escalated to 鼠 (Rat)
- Reason: 角色混乱 = 效率低下，专业度下降
> [引用] 完整代码已提取到 `references\code_block_51.txt`（29 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_51.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



Version Control: Git + ComfyUI Workflow Versioning
Storage: C:/Users/Administrator/.workbuddy/comfyui/workflows/
Naming: {workflow_name}_v{major}.{minor}.{patch}.json
Example: vacuum_cup_workflow_v1.2.3.json
> 📄 代码已提取到 `references\code_52.txt`（10 行，311 字节）
> 需要查看完整代码时请读取该文件。

python
def compare_workflow_versions(
    workflow_v1: str,  # Path to v1 workflow JSON
    workflow_v2: str,  # Path to v2 workflow JSON
    output_format: str = "unified"  # "unified" | "context" | "html"
):
    # ... (代码已精简，保留核心逻辑) ...

def generate_html_diff(json1, json2):
    """Generate HTML diff (for visual comparison)"""
    # (Implementation would use difflib.HtmlDiff)
    pass
> 📄 代码已提取到 `references\code_53.txt`（2 行，42 字节）
> 需要查看完整代码时请读取该文件。

diff
+++ vacuum_cup_workflow_v1.1.0.json
@@ -45,7 +45,7 @@
       "inputs": {
         "text": "a vacuum cup with titanium body",
- "cfg": 7.5,
+        "cfg": 8.0,
         "steps": 30
       }
  ... (省略中间部分) ...
       }
     },
+    {
+      "id": 15,
+      "type": "ControlNetApply",
+      "inputs": {...}
+    },
     {
       "id": 16,
       "type": "VAEDecode",
> 📄 代码已提取到 `references\code_54.txt`（5 行，28 字节）
> 需要查看完整代码时请读取该文件。

python
def rollback_workflow(
    workflow_path: str,
    target_version: str,  # e.g., "v1.0.0"
    backup_current: bool = True
):
    # ... (代码已精简，保留核心逻辑) ...
    
    # Sort by version (descending)
    version_files.sort(reverse=True, key=lambda x: parse_version(x[0]))
    
    return version_files
> 📄 代码已提取到 `references\code_55.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。

python
def release_version(
    workflow_path: str,
    release_version: str,  # e.g., "v1.0.0"
    release_notes: str,  # Release notes (markdown)
    mark_as_stable: bool = True
):
    """Release a new version of workflow"""
    if not is_valid_version(release_version):
        print(f"❌ Invalid version format: {release_version}")
  ... (省略中间部分) ...
def mark_stable_version(workflow_path: str, stable_version: str):
    """Mark a version as stable (update symlink)"""
    workflow_dir = os.path.dirname(workflow_path)
    workflow_name = os.path.basename(workflow_path).replace('.json', '')
    stable_link = os.path.join(workflow_dir, f"{workflow_name}_stable.json")
    if os.path.exists(stable_link):
        os.remove(stable_link)
    versioned_file = os.path.join(workflow_dir, f"{workflow_name}_{stable_version}.json")
    os.symlink(versioned_file, stable_link)
    return stable_link
> 📄 代码已提取到 `references\code_56.txt`（3 行，29 字节）
> 需要查看完整代码时请读取该文件。

markdown
# Release Notes: v1.1.0

## 🎯 Changes Summary
- **NEW**: Added ControlNet support (node ID 15)
- **Improved**: Increased CFG scale from 7.5 to 8.0 (better prompt adherence)
    # ... (代码已精简，保留核心逻辑) ...

## 👥 Contributors
- 马 (Horse): Workflow optimization
- 羊 (Goat): LoRA weight tuning
- 猴 (Monkey): Parameter optimization
> 📄 代码已提取到 `references\code_57.txt`（5 行，45 字节）
> 需要查看完整代码时请读取该文件。


1. ALWAYS commit to Git before releasing version
2. ALWAYS test workflow BEFORE marking as stable
3. ALWAYS include release notes (even for PATCH versions)
4. ALWAYS backup before rollback
5. ALWAYS use semantic versioning (MAJOR.MINOR.PATCH)
6. NEVER release without code review (鸡 (Rooster) approval)
7. NEVER skip version numbers (always increment sequentially)
8. NEVER modify released versions (create new version instead)
> 📄 代码已提取到 `references\code_58.txt`（3 行，34 字节）
> 需要查看完整代码时请读取该文件。


1. Develop → 2. Test → 3. Commit to Git → 4. Release Version → 5. Mark Stable → 6. Deploy
> 📄 代码已提取到 `references\code_59.txt`（7 行，386 字节）
> 需要查看完整代码时请读取该文件。

python
def monitor_generation_progress(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str,
  ... (省略中间部分) ...
            last_progress = current_progress
        if current_step > 0 and current_step % 5 == 0:  # Every 5 steps
            adjustment = analyze_intermediate_result(
                comfyui_api_url,
                prompt_id,
                current_step
            )
            if adjustment["should_adjust"]:
                apply_adjustment(comfyui_api_url, prompt_id, adjustment)
        time.sleep(check_interval)
> 📄 代码已提取到 `references\code_60.txt`（3 行，27 字节）
> 需要查看完整代码时请读取该文件。

python
def interrupt_generation(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str
):
    """Interrupt ComfyUI generation process"""
    # ... (代码已精简，保留核心逻辑) ...
    
    # Check for keyboard interrupt (if running interactively)
    # (This would be handled by signal handler in real implementation)
    
    return False
> 📄 代码已提取到 `references\code_61.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。

python
def analyze_intermediate_result(
    comfyui_api_url: str,
    prompt_id: str,
    current_step: int
):
    """Analyze intermediate generation result and decide adjustments"""
    intermediate_image = get_intermediate_image(comfyui_api_url, prompt_id, current_step)
    quick_assessment = quick_quality_check(
        intermediate_image,
  ... (省略中间部分) ...
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
> 📄 代码已提取到 `references\code_62.txt`（3 行，62 字节）
> 需要查看完整代码时请读取该文件。

python
def feedback_loop(
    initial_prompt: str,
    max_iterations: int = 3,
    quality_threshold: float = 7.0
):
    # ... (代码已精简，保留核心逻辑) ...
        "iterations": iteration,
        "final_quality_score": quality_score,
        "final_prompt": current_prompt,
        "output": generation_result["output"]
    }
> [引用] 完整代码已提取到 `references\code_block_63.txt`（22 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_63.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




### Image Processing Flow (using vision-ai skill):
> [引用] 完整代码已提取到 `references\code_block_64.txt`（45 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_64.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_65.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_65.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




### Multi-modal Quality Assessment:
> [引用] 完整代码已提取到 `references\code_block_66.txt`（53 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_66.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_67.txt`（40 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_67.txt`（2 行，35 字节）
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
> 📄 代码已提取到 `references\code_68.txt`（3 行，25 字节）
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
> 📄 代码已提取到 `references\code_69.txt`（3 行，24 字节）
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
> [引用] 完整代码已提取到 `references\code_block_70.txt`（67 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_70.txt`（2 行，35 字节）
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
> 📄 代码已提取到 `references\code_71.txt`（6 行，76 字节）
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
> 📄 代码已提取到 `references\code_72.txt`（8 行，97 字节）
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
> 📄 代码已提取到 `references\code_73.txt`（14 行，204 字节）
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
> 📄 代码已提取到 `references\code_74.txt`（4 行，26 字节）
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
> [引用] 完整代码已提取到 `references\code_block_75.txt`（24 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_75.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



Compliance Score = (DFM Score + Safety Score + Quality Score + Manufacturability Score) / 4

Where:
- DFM Score (0-10): Design for Manufacturability score
  - 10: All DFM checks passed
  - 5: Some DFM warnings
  - 0: Critical DFM violations

- Safety Score (0-10): Safety standard compliance
  - 10: Meets all safety standards (FDA/LFGB/GB)
  - 5: Meets basic safety standards
  - 0: Safety violations detected

- Quality Score (0-10): Quality standard compliance
  - 10: Meets all quality standards (ISO/ASTM)
  - 5: Meets basic quality standards
  - 0: Quality issues detected

- Manufacturability Score (0-10): Ease of manufacturing
  - 10: Easy to manufacture (simple process, common materials)
  - 5: Moderate difficulty
  - 0: Hard to manufacture (complex process, rare materials)

Quality Gate:
- Compliance Score >= 8: Proceed to production
- Compliance Score 5-7: Request design modification
- Compliance Score < 5: Reject design, redesign required
> 📄 代码已提取到 `references\code_76.txt`（4 行，29 字节）
> 需要查看完整代码时请读取该文件。

python
def calculate_compliance_score(design):
    """Calculate design compliance score (0-10)"""
    dfm = score_dfm(design)
    safety = score_safety(design)
    quality = score_quality(design)
    manufacturability = score_manufacturability(design)
    
    compliance_score = (dfm + safety + quality + manufacturability) / 4
    return round(compliance_score, 1)

def score_dfm(design):
    """Score DFM (0-10)"""
    dfm_checks = [
        'wall_thickness >= 0.8mm',
        'no_undercuts',
        'draft_angle >= 1 degree',
        'tolerance_accurate'
    ]
    passed = sum(1 for check in dfm_checks if check_passes(design, check))
    return int((passed / len(dfm_checks)) * 10)

# Usage Example
design = load_design("vacuum_cup_v3.stp")
compliance = calculate_compliance_score(design)
print(f"Compliance Score: {compliance}/10")

if compliance >= 8:
    print("✅ Proceed to production")
elif compliance >= 5:
    print("⚠️ Request design modification")
else:
    print("❌ Reject design, redesign required")
> 📄 代码已提取到 `references\code_77.txt`（10 行，239 字节）
> 需要查看完整代码时请读取该文件。


1. Extract Product Type + Key Standards from Design
   ↓
2. Search Standards Database for Similar Products (past 30 days)
   ↓
3. Compare with Top 3 Similar Designs
   - Compliance Similarity Score (0-1): How similar is the compliance?
   - Gap Detection: Does the new design have compliance gaps?
   - Best Practice Reuse: Can we reuse successful compliance patterns?
   ↓
4. Output Comparative Compliance Report
> 📄 代码已提取到 `references\code_78.txt`（4 行，33 字节）
> 需要查看完整代码时请读取该文件。


Design A: 保温杯 316内胆 0.8mm壁厚 符合FDA
Design B: 保温杯 304内胆 0.6mm壁厚 符合GB

Compliance Difference Map:
- Material: 316 vs 304 (BETTER, 316 more corrosion resistant)
- Wall Thickness: 0.8mm vs 0.6mm (BETTER, exceeds DFM minimum)
- Standards: FDA vs GB (EQUIVALENT, both food-grade)
- Overall: Design A has better compliance
> [引用] 完整代码已提取到 `references\code_block_79.txt`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_79.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。


python
class StandardsMemory:
    def __init__(self):
        self.standards_db = {}  # Compressed standards database
        self.dfm_checklist = []  # Compressed DFM checklist
    
    def load_for_product(self, product_type):
        """Load only relevant standards for product type"""
        if product_type == "vacuum_cup":
            self.standards_db = load_standards(["GB/T 29606", "FDA", "LFGB"])
        elif product_type == "electric_wheelchair":
            self.standards_db = load_standards(["ISO 7176", "GB/T 12996"])
        
        # Compress to top 10 standards
        self.standards_db = compress_to_top_10(self.standards_db)
    
    def get_dfm_checklist(self, material, process):
        """Get compressed DFM checklist"""
        checklist = load_dfm_checklist(material, process)
        # Keep only critical checks (P0)
        self.dfm_checklist = [c for c in checklist if c.priority == "P0"]
        return self.dfm_checklist

# Usage
memory = StandardsMemory()
memory.load_for_product("vacuum_cup")
checklist = memory.get_dfm_checklist("316_stainless_steel", "deep_drawing")
print(f"Loaded {len(memory.standards_db)} standards, {len(checklist)} DFM checks")
```


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

## ComfyUI API集成（New in v7.0）

### 标准分析后的ComfyUI API工作流规范检查

🐮 牛在标准分析后，可调用ComfyUI API**验证工作流规范性**：

```python
import requests
import json

# ComfyUI API地址
COMFYUI_API = "http://127.0.0.1:8188"

def validate_comfyui_workflow(workflow_path):
    """验证ComfyUI工作流规范性"""
    # 1. 读取工作流
    with open(workflow_path, 'r') as f:
        workflow = json.load(f)
    
    # 2. 检查必填节点
    required_nodes = ["CheckpointLoaderSimple", "KSampler", "VAEDecode", "SaveImage"]
    missing_nodes = []
    
    for req_node in required_nodes:
        if not any(node["type"] == req_node for node in workflow["nodes"]):
            missing_nodes.append(req_node)
    
    # 3. 检查参数范围
    warnings = []
    for node in workflow["nodes"]:
        if node["type"] == "KSampler":
            steps = node["inputs"]["steps"]
            cfg = node["inputs"]["cfg"]
            
            if steps < 20 or steps > 50:
                warnings.append(f"KSampler steps={steps} 超出推荐范围[20, 50]")
            
            if cfg < 5.0 or cfg > 15.0:
                warnings.append(f"KSampler cfg={cfg} 超出推荐范围[5.0, 15.0]")
    
    # 4. 返回验证报告
    return {
        "valid": len(missing_nodes) == 0,
        "missing_nodes": missing_nodes,
        "warnings": warnings
    }
```

**使用场景**：
- 检查ComfyUI工作流规范性
- 确保工作流符合最佳实践
- 生成工作流质量报告

---


---

## Phase 6: DFM自动化检查与标准合规验证 (NEW in v7.2)

### 6.1 DFM自动化检查流程

**DFM检查目标**：
- 面向制造的设计（Design for Manufacturability）
- 成本优化（减少加工难度、提升良率）
- 标准化合规（符合行业标准和规范）
- 可装配性（简化装配流程、减少零件数量）

**自动化检查流程**：
```
1. 接收产品设计文件（从🐍蛇/用户）
2. 识别产品类型和制造工艺
3. 执行DFM检查（尺寸、公差、材料、工艺）
4. 生成DFM检查报告
5. 提供设计优化建议
6. 通知🐍蛇设计需要优化
```

**DFM检查清单**：

| 检查项 | 检查内容 | 目标值 |
|--------|----------|--------|
| **尺寸合理性** | 最小壁厚、最大尺寸、公差范围 | 符合制造能力 |
| **材料选择** | 材料可加工性、成本、可用性 | 最优材料组合 |
| **工艺可行性** | 加工工艺、装配工艺、表面处理 | 工艺可行 |
| **成本控制** | 加工成本、材料成本、装配成本 | 成本最优 |
| **标准化合规** | 符合国标/行标/企标 | 100%合规 |

### 6.2 标准合规自动验证

**合规验证目标**：
- 保温杯：符合GB/T 29606-2013、QB/T 2332-2017
- 电动轮椅：符合GB/T 12996-2012、ISO 7176
- ComfyUI工作流：符合最佳实践和标准规范

**自动验证流程**：
```
1. 识别产品类型和适用标准
2. 读取标准文档（本地/在线）
3. 对比设计参数与标准要求
4. 生成合规验证报告
5. 标记不合规项
6. 提供整改建议
```

**合规验证报告格式**：
```json
{
  "verification_id": "DFM-2026-0619-001",
  "product_type": "保温杯",
  "standard": "GB/T 29606-2013",
  "compliance_rate": 0.92,
  "non_compliant_items": [
    {
      "item": "保温性能",
      "requirement": "≥6h (60℃→40℃)",
      "actual": "5.5h",
      "status": "不合规",
      "suggestion": "增加真空层厚度至0.8mm"
    }
  ],
  "optimization_suggestions": [
    "内胆材质从304不锈钢升级到316不锈钢",
    "真空层厚度从0.5mm增加到0.8mm"
  ]
}
```

### 6.3 与十四生肖团其他Agent的联动

**联动链1：🐮→🐍→🐔（标准检查→产品设计→设计评审）**
```
🐮接收设计文件 → 执行DFM检查
→ 生成DFM报告 → 调用🐍进行设计优化
→ 🐍优化完成 → 调用🐔进行设计评审
→ 🐔评审完成 → 🐮验证合规性
→ 生成最终合规报告
```

**联动链2：🐮→🐶（标准检查→成本分析）**
```
🐮执行DFM检查 → 识别成本优化点
→ 调用🐶进行成本分析
→ 🐶分析完成 → 🐮验证成本优化方案可行性
→ 生成成本+DFM综合优化报告
```

**联动链3：🐮→🐴（标准检查→ComfyUI工作流）**
```
🐴生成ComfyUI工作流 → 调用🐮进行规范性检查
→ 🐮检查完成 → 标记不规范节点
→ 生成工作流规范性报告
→ 调用🐴进行工作流优化
```

### 6.4 DFM知识库与最佳实践

**知识库内容**：
- 历史DFM检查记录（设计参数 + DFM问题 + 优化方案）
- 材料数据库（可加工性、成本、性能）
- 工艺数据库（加工工艺、公差能力、表面处理）
- 标准文档库（GB/QB/ISO标准）
- DFM最佳实践（经验总结）

**知识库查询**：
- 根据产品类型查询DFM检查清单
- 根据材料查询可加工性评级
- 根据工艺查询公差能力
- 根据标准查询合规要求

**知识库更新流程**：
```
1. 每次DFM检查完成后 → 记录检查数据
2. 定期分析DFM数据 → 提取最佳实践
3. 更新知识库 → 新增/修改/删除条目
4. 知识库版本管理 → 记录每次更新
```

### 6.5 DFM优化效果评估

**评估指标**：
- 合规性提升（合规率 before vs after）
- 成本降低（成本 before vs after）
- 可制造性提升（加工难度评分 before vs after）
- 良率提升（良率 before vs after）

**自动评估流程**：
```
1. DFM优化前基线测试（检查10个设计）
2. 应用DFM优化建议
3. DFM优化后测试（检查10个设计）
4. 对比分析（计算提升百分比）
5. 生成评估报告
6. 决策（如果合规率提升>5%，则应用优化建议；否则重新分析）
```

**评估报告格式**：
```json
{
  "dfm_optimization_id": "DFM-OPT-2026-0619-001",
  "before": {
    "compliance_rate": 0.85,
    "cost": 150.0,
    "manufacturability_score": 7.5,
    "yield_rate": 0.92
  },
  "after": {
    "compliance_rate": 0.93,
    "cost": 135.0,
    "manufacturability_score": 8.3,
    "yield_rate": 0.96
  },
  "improvement": {
    "compliance_rate": "+0.08 (+9.4%)",
    "cost": "-15.0 (-10.0%)",
    "manufacturability_score": "+0.8 (+10.7%)",
    "yield_rate": "+0.04 (+4.3%)"
  },
  "decision": "应用DFM优化建议",
  "confidence": 0.94
}
```

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
