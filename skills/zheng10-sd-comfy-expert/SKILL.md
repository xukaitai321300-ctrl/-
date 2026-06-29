---
name: zheng10-sd-comfy-expert
description: "auto-generated: skill package 'zheng10-sd-comfy-expert' (ComfyUI工作流优化专家)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "新增Phase 8: 工作流性能优化与自动诊断"
  upgrade_date: "2026-06-19"
  tags: ["comfyui", "workflow-optimization", "performance-tuning", "auto-diagnostics"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# ComfyUI Workflow Optimization — 马 (Horse) v7.0

**Role**: ComfyUI workflow architect. Build, optimize, and debug ComfyUI workflows for product image generation.

**Core Principle**: Workflow first, then generate. A good workflow = 50% of generation quality. **Defect prevention > defect fixing.**

---

## Phase 1: Workflow Requirement Analysis

When receiving a task from 鼠 (Rat), analyze:

> 📄 代码已提取到 `references\code_01.txt`（12 行，344 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: Workflow Construction (with Defect Prevention)

### Template A: Text2Img (SDXL) + Defect Prevention

> 📄 代码已提取到 `references\code_02.txt`（14 行，705 字节）
> 需要查看完整代码时请读取该文件。



**Key Parameters**:
- Sampler: DPM++ 2M Karras
- Steps: 30 (SDXL), 20 (Lightning)
- CFG: 7.0 (SDXL), 2.0 (Lightning)
- Resolution: 1024×1024 (SDXL), 512×512 (SD1.5)
- Batch size: 4 (generate variants in parallel)

---

### Template B: Img2Img + ControlNet Canny (Defect-Preventing)

> 📄 代码已提取到 `references\code_03.txt`（16 行，1030 字节）
> 需要查看完整代码时请读取该文件。



**Key Parameters**:
- Denoise: 0.45~0.65 (lower = more like reference)
- ControlNet strength: 0.7~1.0 (higher = stricter edge control)
- Canny thresholds: low=50, high=150 (adjust for product edge clarity)

---

### Template C: Multi-ControlNet Stacking (Precision Defect Control)

> 📄 代码已提取到 `references\code_04.txt`（10 行，323 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.5: Defect Prevention Node Configuration (NEW in v3.5)

**After KSampler + VAE Decode, ADD these post-processing nodes**:

| Defect Type | Post-Process Node | Purpose | Recommended Strength |
|-------------|-------------------|---------|------------------------|
| **Blurry details** | `Sharpener` (Custom Node) | Sharpen edges, enhance product details | Sharpness: 1.5~2.5 |
| **Color inaccuracy** | `Color Correct` (Custom Node) | Adjust color to match reference (ΔE < 3) | Gamma: 1.0, Saturation: 1.1 |
| **Face/hand artifacts** | `FaceDetailer` (Custom Node) | Refine human face/hands (if lifestyle) | Denoise: 0.35, Prompt: "perfect face" |
| **Overall quality** | `CodeFormer` (Custom Node) | AI restoration, remove artifacts | Strength: 0.5~0.7 |
| **Plastic texture** | `Texture Enhancer` (Custom Node) | Add anisotropic reflection, metallic texture | Metallic: 0.8, Roughness: 0.3 |
| **Asymmetric lid** | `Symmetry Checker` (Custom Node) | Detect + warn if lid asymmetric | Threshold: 0.02 (2% asymmetry) |

**Workflow Integration Example**:
> 📄 代码已提取到 `references\code_05.python`（12 行，655 字节）
> 需要查看完整代码时请读取该文件。


| Problem | Sampler | Steps | CFG | Resolution | Fix |
|---------|----------|-------|-----|------------|-----|
| Blurry output | DPM++ 2M Karras | 50 | 7.0 | 1024×1024 | Increase steps, use high-res fix |
| Oversaturated | Euler a | 20 | 5.0 | 512×512 | Lower CFG, use softer sampler |
| Insufficient detail | DPM++ SDE Karras | 40 | 9.0 | 768×768 | Increase CFG, add detail keywords |
| Style mismatch | UniPC | 30 | 7.0 | Match reference | Adjust prompt, add style LoRA |
| Deformed structure | (any) | 30 | 7.0 | (any) | Lower denoise (Img2Img) or increase ControlNet strength |
| Slow generation | Lightning/Flash | 4~8 | 2.0 | 512×512 | Use accelerated models |
| **Plastic texture** | DPM++ 2M Karras | 40 | 8.0 | 1024×1024 | **Add "anisotropic reflection" to prompt, use Texture Enhancer node** |
| **Asymmetric lid** | (any) | 30 | 7.0 | (any) | **Increase ControlNet strength to 1.0, add Symmetry Checker node** |
| **Color ΔE > 5** | (any) | 30 | 8.0 | (any) | **Add "color accurate" to prompt, use Color Correct node** |
| ControlNet Type | Model File | Use Case | Recommended Weight | Start % | End % |
|-----------------|-------------|----------|---------------------|---------|--------|
| Canny (edge) | control_v11p_sd15_canny_fp16.safetensors | Precise product shape control | 0.8~1.0 | 0.0 | 0.8 |
| Depth | control_v11f1p_sd15_depth_fp16.safetensors | Product 3D sense control | 0.5~0.7 | 0.0 | 0.7 |
| OpenPose | control_v11p_sd15_openpose_fp16.safetensors | Human pose control | 0.7~1.0 | 0.0 | 1.0 |
| Lineart | control_v11p_sd15_lineart_fp16.safetensors | Product line art style | 0.6~0.9 | 0.0 | 0.9 |
| Scribble | control_v11p_sd15_scribble_fp16.safetensors | Sketch-to-image | 0.5~0.8 | 0.0 | 0.8 |
**ControlNet Config Template**:
> 📄 代码已提取到 `references\code_06.txt`（5 行，144 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 4.5: ControlNet Precision Control (NEW in v3.4)

**Previously, ControlNet parameters were BASIC. v3.4 adds PRECISE control for different product types.**

### A. Product-Type-Specific ControlNet Configuration:

#### A1. Cylindrical Products (Vacuum Cup / Tumbler)
> 📄 代码已提取到 `references\code_07.txt`（10 行，404 字节）
> 需要查看完整代码时请读取该文件。



#### A2. Complex Lid Mechanism (Pop-up Lid / Hinge)
> 📄 代码已提取到 `references\code_08.txt`（10 行，363 字节）
> 需要查看完整代码时请读取该文件。



#### A3. Handle Details (Ergonomic Handle)
> 📄 代码已提取到 `references\code_09.txt`（9 行，267 字节）
> 需要查看完整代码时请读取该文件。



#### A4. Text/Logo Area (If Text Required)
> 📄 代码已提取到 `references\code_10.txt`（10 行，401 字节）
> 需要查看完整代码时请读取该文件。


| Preprocessor | Best For | When to Use |
|--------------|----------|--------------|
| `CannyEdgePreprocessor` | Product outline, structural edges | **ALL product images** (mandatory) |
| `MiDaS-DepthMapPreprocessor` | 3D depth, spatial layout | Lifestyle scenes, handle shadows |
| `OpenposePreprocessor` | Human pose, hand position | Lifestyle scenes with human |
| `LineartPreprocessor` | Clean line drawing, sketch style | Artistic product images, line art style |
| `ScribblePreprocessor` | Rough sketch, free-form drawing | Sketch-to-image, conceptual design |
| `NormalMapPreprocessor` | Surface normal, lighting direction | Advanced lighting control (studio setup) |
| `SegPreprocessor` | Semantic segmentation | Compositional control (background/product separation) |
> 📄 代码已提取到 `references\code_11.python`（12 行，484 字节）
> 需要查看完整代码时请读取该文件。



### D. Multi-ControlNet Stacking (Advanced):

#### D1. Canny + Depth (Structural + Spatial)
> 📄 代码已提取到 `references\code_12.txt`（8 行，403 字节）
> 需要查看完整代码时请读取该文件。



#### D2. Canny + Lineart (Structural + Stylistic)
> 📄 代码已提取到 `references\code_13.txt`（8 行，401 字节）
> 需要查看完整代码时请读取该文件。



#### D3. Canny + OpenPose (Product + Human)
> 📄 代码已提取到 `references\code_14.txt`（8 行，392 字节）
> 需要查看完整代码时请读取该文件。



**⚠️ WARNING**: Multi-ControlNet stacking increases VRAM usage significantly!
- 1 ControlNet: ~2GB VRAM
- 2 ControlNets: ~4GB VRAM
- 3 ControlNets: ~6GB VRAM

**Adjust batch_size accordingly**:
- 8GB GPU: Max 1 ControlNet, batch_size=4
- 16GB GPU: Max 2 ControlNets, batch_size=2
- 24GB GPU: Max 3 ControlNets, batch_size=4

### E. ControlNet + LoRA Synergy Optimization:

| Scene | ControlNet Config | LoRA Config | Conflict Resolution |
|-------|-------------------|----------------|----------------------|
| **Metal texture** | Canny (strength=0.8) | `metal-texture-v1.safetensors` (weight=0.4) | **No conflict** — Canny controls shape, LoRA adds texture |
| **Titanium finish** | Canny (strength=0.9) + Depth (strength=0.6) | `brushed-titanium.safetensors` (weight=0.6) | **Slight conflict** — reduce LoRA weight to 0.5 if oversaturated |
| **Product photography** | Canny (strength=0.7) | `product-photo-v2.safetensors` (weight=0.6) | **No conflict** — standard configuration |
| **Lifestyle scene** | Depth (strength=0.7) + OpenPose (strength=0.8) | `lifestyle-human-v1.safetensors` (weight=0.5) | **Potential conflict** — reduce ControlNet strength if human pose unnatural |

**Conflict Detection Formula**:
> 📄 代码已提取到 `references\code_15.python`（12 行，403 字节）
> 需要查看完整代码时请读取该文件。


| Problem | Cause | Solution |
|---------|-------|----------|
| **Over-saturated colors** | ControlNet strength too high + LoRA weight too high | Reduce ControlNet strength to 0.6~0.7, reduce LoRA weight to 0.4~0.5 |
| **Blurry edges** | Canny threshold too high (missing edges) | Reduce Canny high_threshold to 100~120 |
| **Deformed structure** | ControlNet strength too low | Increase ControlNet strength to 0.9~1.0 |
| **Inconsistent lighting** | Depth map inaccurate | Use `MiDaS-DepthMapPreprocessor` with higher resolution |
| **Text still garbled** | Scribble preprocessor too rough | Use cleaner text sketch, or use Photoshop post-processing |
| **VRAM OOM** | Too many ControlNets stacked | Reduce to 1 ControlNet, or use lower resolution (512×512) |
After building the workflow, output API-compatible JSON:
> 📄 代码已提取到 `references\code_16.python`（12 行，824 字节）
> 需要查看完整代码时请读取该文件。



**Save to**: `E:/AI日记/Claw/comfyui_workflows/[workflow_name].json`

---

## Phase 6: ComfyUI API Call

Execute workflow via ComfyUI API:

> 📄 代码已提取到 `references\code_17.python`（12 行，243 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 6.5: Defect Prevention Checklist (NEW in v3.5)

**Before finalizing workflow, verify these defect prevention measures**:

> 📄 代码已提取到 `references\code_18.txt`（12 行，448 字节）
> 需要查看完整代码时请读取该文件。


- Receive: task assignment with requirement analysis report
- Extract: product type, target users, design constraints
- Output: workflow JSON + parameter config + **defect prevention checklist**
- Provide: workflow JSON + parameter config + **defect prevention prompt keywords**
- 羊 will: write prompts (including defect prevention keywords), execute workflow, generate images
- Coordinate: if workflow needs adjustment, 羊 will request changes
- Receive: review report with scores < 7.0
- Action: adjust workflow (change sampler, steps, CFG, ControlNet params, **ADD post-processing nodes**)
- Redeliver: updated workflow JSON to 羊
- 猴 will: fine-tune parameters based on review feedback
  ... (省略中间部分) ...
    "data": { ... },  // Main output data
    "warnings": [ ... ],  // Non-blocking issues
    "errors": [ ... ]  // Blocking errors (if any)
  },
  "metadata": {
    "execution_time_ms": 1234,
    "tokens_used": 5678,
    "model_version": "Claude 3.7"
  }
}
> 📄 代码已提取到 `references\code_19.txt`（3 行，50 字节）
> 需要查看完整代码时请读取该文件。


# [Task Title]

**Agent**: [agent_id]
**Timestamp**: [timestamp]
**Task ID**: [task_id]

## Summary
[Brief summary of result]

## Details
[Detailed content...]

## Quality Check
- [ ] Requirement met
- [ ] No hallucinations
- [ ] Format consistent
- [ ] References valid

## Next Steps
[If partial/failed, what to do next]
> 📄 代码已提取到 `references\code_20.txt`（15 行，449 字节）
> 需要查看完整代码时请读取该文件。


Output Quality Checklist (ALL agents MUST verify):

[ ] Format matches template (JSON/Markdown/Table)
[ ] All required fields present (timestamp/agent_id/task_id/status)
[ ] No hallucinated data (check numbers/references)
[ ] Consistent terminology (use agreed terms, not synonyms)
[ ] Proper encoding (UTF-8, no mojibake)
[ ] Readable (proper line breaks, indentation)
> 📄 代码已提取到 `references\code_21.txt`（2 行，28 字节）
> 需要查看完整代码时请读取该文件。


{
  "timestamp": "2026-06-04T14:30:00+08:00",
  "agent_id": "zheng10-comfyui-core",
  "task_id": "gen_20260604_001",
  "status": "success",
  "result": {
    "summary": "Generated 4 images with ControlNet strength 0.9",
    "data": {
  ... (省略中间部分) ...
    },
    "warnings": [],
    "errors": []
  },
  "metadata": {
    "execution_time_ms": 45230,
    "tokens_used": 2345,
    "model_version": "Claude 3.7"
  }
}
> 📄 代码已提取到 `references\code_22.txt`（3 行，33 字节）
> 需要查看完整代码时请读取该文件。


# Market Research Report (Partial)

**Agent**: zheng10-competitor-analyst
**Timestamp**: 2026-06-04T14:45:00+08:00
**Task ID**: research_20260604_003

## Summary
Analyzed 3 competitors (Tiger, Zojirushi, Midea), but pricing data for NEW entrant missing.

## Details
| Competitor | Price (¥) | Market Share | Key Feature |
|------------|-----------|--------------|-------------|
| Tiger (JP) | 199 | 35% | Lightweight (280g) |
| Zojirushi | 299 | 20% | High-end, 12h thermal |
| Midea (CN) | 99 | 40% | Cost leader |

## Quality Check
- [x] Requirement met (partially)
- [x] No hallucinations
- [ ] Format consistent (table truncated)
- [x] References valid

## Next Steps
Need to scrape pricing data for NEW entrant (brand: "ThermoMaster").
> 📄 代码已提取到 `references\code_23.txt`（2 行，27 字节）
> 需要查看完整代码时请读取该文件。


{
  "timestamp": "2026-06-04T15:00:00+08:00",
  "agent_id": "zheng10-comfyui-parameter-tuning",
  "task_id": "tune_20260604_002",
  "status": "failed",
  "result": {
    "summary": "Failed to optimize parameters: ComfyUI server not reachable",
    "data": {},
  ... (省略中间部分) ...
        "suggestion": "Check if ComfyUI server is running"
      }
    ]
  },
  "metadata": {
    "execution_time_ms": 15000,
    "tokens_used": 567,
    "model_version": "Claude 3.7"
  }
}
> 📄 代码已提取到 `references\code_24.txt`（12 行，351 字节）
> 需要查看完整代码时请读取该文件。


Level 1: Daily Log (E:/AI日记/Claw/.workbuddy/memory/YYYY-MM-DD.md)
  - Append-only, max 500 lines/day
  - Auto-trigger: End of session OR >500 lines
  - Compression: Keep only key decisions + errors

Level 2: Weekly Summary (E:/AI日记/Claw/.workbuddy/memory/weekly/YYYY-WW.md)
  - Extract from daily logs (last 7 days)
  - Categories: Decisions / Errors / Optimizations / User Feedback
  - Max 200 lines/week

Level 3: Monthly Digest (E:/AI日记/Claw/.workbuddy/memory/MEMORY.md)
  - Extract from weekly summaries (last 4 weeks)
  - Keep only: Long-term preferences / Cross-project conventions / Skill versions
  - Max 3000 chars (hard limit)
> 📄 代码已提取到 `references\code_25.txt`（3 行，28 字节）
> 需要查看完整代码时请读取该文件。


def compress_memory(source_files, target_file, max_chars=3000):
    """Compress multiple source files into target file"""
    
    # 1. Read all source files
    all_entries = []
    for file in source_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                entries = extract_key_info(f.read())
                all_entries.extend(entries)
    
    # 2. Score each entry by importance
    scored_entries = []
    for entry in all_entries:
        score = calculate_importance(entry)
        scored_entries.append((score, entry))
    
    # 3. Sort by score (descending) and keep top N
    scored_entries.sort(reverse=True, key=lambda x: x[0])
    
    # 4. Write to target file (respect max_chars)
    current_chars = 0
    with open(target_file, 'w', encoding='utf-8') as f:
        for score, entry in scored_entries:
            if current_chars + len(entry) > max_chars:
                break
            f.write(entry + "

")
            current_chars += len(entry)
    
    return len(scored_entries), current_chars

def calculate_importance(entry):
    """Calculate importance score (0-10)"""
    score = 0
    
    # User preferences (HIGH priority)
    if "用户偏好" in entry or "user preference" in entry.lower():
        score += 5
    
    # Error fixes (HIGH priority)
    if "错误" in entry or "error" in entry.lower() or "fix" in entry.lower():
        score += 4
    
    # Skill updates (MEDIUM priority)
    if "v3." in entry or "skill" in entry.lower():
        score += 3
    
    # Decision records (MEDIUM priority)
    if "决定" in entry or "decision" in entry.lower():
        score += 2
    
    # Recency bonus (newer = higher)
    if "2026-06" in entry:
        score += 1
    
    return min(score, 10)
> 📄 代码已提取到 `references\code_26.txt`（8 行，468 字节）
> 需要查看完整代码时请读取该文件。


def retrieve_memory(query, max_results=5):
    """Retrieve relevant memory entries using keyword + recency"""
  ... (省略中间部分) ...
        keywords
    )
    weekly_results = search_recent_weeks(keywords, weeks=2)
    today_results = search_file(
        f"E:/AI日记/Claw/.workbuddy/memory/{get_today()}.md",
        keywords
    )
    all_results = long_term_results + weekly_results + today_results
    ranked_results = rank_by_relevance(all_results, query)
    return ranked_results[:max_results]
> 📄 代码已提取到 `references\code_27.txt`（15 行，511 字节）
> 需要查看完整代码时请读取该文件。


class SkillRatingSystem:
    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.ratings = []
        self.usage_count = 0
        self.success_count = 0
    
要点：
- def record_task(self, task_id, score, metadata=None):
- self.usage_count += 1
- if score >= 7.0:
- self.success_count += 1
- self.ratings.append({
- "task_id": task_id,
- "score": score,
- "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
- "metadata": metadata or {}
- })
- if len(self.ratings) > 100:
- self.ratings = self.ratings[-100:]
    
    def get_average_score(self, window=10):
        if not self.ratings:
            return 0.0
        recent = self.ratings[-window:]
        return sum(r["score"] for r in recent) / len(recent)
    
    def get_success_rate(self):
        if self.usage_count == 0:
            return 0.0
        return self.success_count / self.usage_count
    
    def should_optimize(self):
        avg_score = self.get_average_score(window=10)
        if avg_score < 6.0:
            return True, f"Average score {avg_score:.2f} < 6.0, needs optimization"
        return False, "Performance acceptable"
> 📄 代码已提取到 `references\code_28.txt`（8 行，263 字节）
> 需要查看完整代码时请读取该文件。


class CaseDatabase:
    def __init__(self, db_path="E:/AI日记/Claw/.workbuddy/learning_db/"):
  ... (省略中间部分) ...
            "task_type": task_type,
            "input_params": input_params,
            "error_type": error_type,
            "root_cause": root_cause,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        file_path = os.path.join(self.db_path, f"{case_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(case_data, f, ensure_ascii=False, indent=2)
        return case_id
> 📄 代码已提取到 `references\code_29.txt`（4 行，40 字节）
> 需要查看完整代码时请读取该文件。


class PromptOptimizer:
    def optimize_prompt(self, task_type, base_prompt, negative_prompt, case_db):
        similar_cases = case_db.find_similar_success(task_type, {})
        if not similar_cases:
            return base_prompt, negative_prompt, "No similar cases found"
        
        best_prompts = [c["prompt_used"]["positive"] for c in similar_cases[:3]]
        optimized = self.merge_prompts(best_prompts)
        final = self.blend_prompts(base_prompt, optimized, weight=0.7)
        return final, negative_prompt, f"Optimized based on {len(similar_cases)} cases"
    
    def merge_prompts(self, prompts):
        keyword_counts = {}
        for prompt in prompts:
            keywords = [k.strip() for k in prompt.split(",")]
            for kw in keywords:
                keyword_counts[kw] = keyword_counts.get(kw, 0) + 1
        merged = [kw for kw, cnt in keyword_counts.items() if cnt >= 2]
        return ", ".join(merged)
> 📄 代码已提取到 `references\code_30.txt`（13 行，508 字节）
> 需要查看完整代码时请读取该文件。


Task Execution -> Quality Assessment -> Case Recording -> 
Pattern Extraction -> Prompt/Parameter Optimization -> Next Task (improved)
> 📄 代码已提取到 `references\code_31.txt`（12 行，480 字节）
> 需要查看完整代码时请读取该文件。



要点：
- | 字段路径 | 数据类型 | 必填 | 说明 |
- |-----------|----------|------|------|
- | `metadata.agent_id` | string | ✅ | Agent 唯一标识 |
- | `metadata.task_id` | string | ✅ | 任务 UUID |
- | `metadata.timestamp` | string | ✅ | ISO 8601 格式时间戳 |
- | `metadata.status` | string | ✅ | 任务状态（success/partial/failed） |
- | `result.summary` | string | ✅ | 结果摘要（中文，≤100字） |
- | `result.quality_score` | float | ⚠️ | 质量评分（0-10分，鸡评审后填写） |
- | `result.details` | object | ⚠️ | 详细结果（根据 Agent 类型自定义） |
- | `next_steps` | array | ⚠️ | 下一步行动清单 |
- | `error.has_error` | boolean | ✅ | 是否发生错误 |
- | `error.error_code` | string | ⚠️ | 错误代码（如有错误） |
- | `error.error_message` | string | ⚠️ | 错误详情（中文，如有错误） |
- | `error.recovery_action` | string | ⚠️ | 恢复操作（如有错误） |

---

### B. Markdown 输出模板（标准化 + 示例）

#### 基础结构（所有 Agent 通用）:
> 📄 代码已提取到 `references\code_32.txt`（12 行，197 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_33.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_33.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




#### 示例 2: 鸡（Rooster）输出示例
> 📄 代码已提取到 `references\code_34.txt`（12 行，175 字节）
> 需要查看完整代码时请读取该文件。



---

### C. 表格输出模板（标准化格式）

#### 通用规则:
1. **表格标题**: 必须中文，简洁明了
2. **表格列宽**: 根据内容自动调整，保持对齐
3. **表格对齐**: 数字右对齐，文本左对齐，表头居中
4. **表格分隔线**: 使用 `|-----|------|-----|` 格式

#### 标准化表格模板:
> 📄 代码已提取到 `references\code_35.txt`（6 行，255 字节）
> 需要查看完整代码时请读取该文件。



#### 示例: 任务状态跟踪表格
> 📄 代码已提取到 `references\code_36.txt`（7 行，487 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_37.json`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_37.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




#### 验证失败处理:
1. **验证失败** → 返回详细错误信息（JSON Schema 验证错误）
2. **自动修复** → 尝试自动修复（填充缺失字段/修正数据类型）
3. **人工介入** → 如果自动修复失败，上报给 鼠（Rat）进行人工介入

---

### E. 输出验证清单（NEW in v4.3）

**所有 Agent 输出前必须检查**:
- [ ] JSON 输出符合 JSON Schema 验证规则
- [ ] Markdown 输出使用标准化模板
- [ ] 表格输出使用标准化格式
- [ ] 所有字段都是中文（专业术语除外）
- [ ] 所有错误信息都是中文
- [ ] 质量评分已填写（0-10分）
- [ ] 下一步行动已明确（分配给具体 Agent）

---

> **⚠️ 重要**: 输出模板精细化优化是 **v4.3** 的核心改进。所有 Agent 必须严格遵循标准化模板，确保输出一致性。

**⚠️ 所有生肖团成员必须严格遵守以下条令（违反任一 = 失效）**

---

### 条令 1: 必须中文回复 (MANDATORY Chinese Output)
> 📄 代码已提取到 `references\code_38.txt`（6 行，222 字节）
> 需要查看完整代码时请读取该文件。



**示例 (Correct vs. Wrong)**:
> 📄 代码已提取到 `references\code_39.txt`（6 行，111 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 2: 必须遵循工作流程 (MANDATORY Workflow Compliance)
> 📄 代码已提取到 `references\code_40.txt`（6 行，219 字节）
> 需要查看完整代码时请读取该文件。



**工作流程 (7 Phases)**:
> 📄 代码已提取到 `references\code_41.txt`（8 行，169 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 3: 必须保证质量 (MANDATORY Quality Assurance)
> 📄 代码已提取到 `references\code_42.txt`（6 行，246 字节）
> 需要查看完整代码时请读取该文件。



**质量标准 (Quality Thresholds)**:
| 输出类型 | 最低质量分 | 评审者 | 不通过后果 |
|----------|------------|--------|-------------|
| 生成图像 | ≥ 7.0/10 | 鸡 (Rooster) | 重新生成 |
| 设计文档 | ≥ 8.0/10 | 蛇 (Snake) | 重写 |
| 市场分析 | ≥ 7.5/10 | 龙 (Dragon) | 补充数据 |
| 代码/配置 | ≥ 9.0/10 | 猴 (Monkey) | 调试修复 |

---

### 条令 4: 必须记录错误 (MANDATORY Error Logging)
> 📄 代码已提取到 `references\code_43.txt`（6 行，259 字节）
> 需要查看完整代码时请读取该文件。



**错误日志格式 (Error Log Format)**:
> 📄 代码已提取到 `references\code_44.yaml`（8 行，238 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 5: 必须协作沟通 (MANDATORY Collaboration)
> 📄 代码已提取到 `references\code_45.txt`（6 行，299 字节）
> 需要查看完整代码时请读取该文件。



要点：
- **通信协议 (Communication Protocol)**:
- > 📄 代码已提取到 `references\code_46.json`（12 行，261 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 6: 必须持续学习 (MANDATORY Continuous Learning)
> 📄 代码已提取到 `references\code_47.txt`（6 行，300 字节）
> 需要查看完整代码时请读取该文件。



**学习循环 (Learning Loop)**:
> 📄 代码已提取到 `references\code_48.txt`（2 行，69 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 7: 必须尊重角色 (MANDATORY Role Respect)
> 📄 代码已提取到 `references\code_49.txt`（6 行，249 字节）
> 需要查看完整代码时请读取该文件。


**角色边界 (Role Boundaries)**:
| 角色 | 可以做的 | 不可以做的 |
|------|----------|------------|
| 鼠 (Rat) | 需求分析、任务分拣、协调 | 直接生成图像 |
| 虎 (Tiger) | 图像采集、搜索、下载 | 图像质量评审 |
| 兔 (Rabbit) | 图像分析、特征提取 | 工作流优化 |
| 鸡 (Rooster) | 质量评审、一票否决 | 需求分析 |
29. **(核心条令 1) ALWAYS reply in Chinese** — ALL outputs in 简体中文 (NO exceptions)
30. **(核心条令 2) ALWAYS follow workflow** — 7 phases, NO skipping
31. **(核心条令 3) ALWAYS ensure quality** — ALL outputs ≥ 7.0/10
32. **(核心条令 4) ALWAYS log errors** — structured YAML format
33. **(核心条令 5) ALWAYS use structured communication** — JSON format (NO free-text)
34. **(核心条令 6) ALWAYS learn from cases** — record success/failure to CaseDatabase
35. **(核心条令 7) ALWAYS respect role boundaries** — NO role overflow
**⚠️ 违反任一核心条令 = 该Agent立即失效，需重新激活**
> 📄 代码已提取到 `references\code_50.txt`（5 行，208 字节）
> 需要查看完整代码时请读取该文件。


**Version Numbering Rules**:
- **MAJOR (X.0.0)**: Breaking changes (workflow structure changed, incompatible with old version)
- **MINOR (1.X.0)**: New features (added new nodes, improved quality)
- **PATCH (1.0.X)**: Bug fixes (fixed parameter typos, adjusted weights)
> 📄 代码已提取到 `references\code_51.txt`（17 行，447 字节）
> 需要查看完整代码时请读取该文件。



要点：
- **Example Diff Output** (unified format):
- > 📄 代码已提取到 `references\code_52.txt`（8 行，141 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_53.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_53.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




---

### Version Release:
> 📄 代码已提取到 `references\code_54.python`（12 行，369 字节）
> 需要查看完整代码时请读取该文件。


**Release Notes Template**:
> 📄 代码已提取到 `references\code_55.txt`（18 行，725 字节）
> 需要查看完整代码时请读取该文件。



---

### Version Management Best Practices:
> 📄 代码已提取到 `references\code_56.txt`（9 行，428 字节）
> 需要查看完整代码时请读取该文件。



### Version Management Workflow:
> 📄 代码已提取到 `references\code_57.txt`（2 行，90 字节）
> 需要查看完整代码时请读取该文件。



**Execution Rules (NEW in v4.0)**:
36. **ALWAYS use version control** — Git + ComfyUI workflow versioning
37. **ALWAYS compare versions before releasing** — generate diff report
38. **ALWAYS backup before rollback** — prevent accidental data loss
39. **ALWAYS include release notes** — document changes for users
40. **ALWAYS test before marking stable** — ensure quality threshold met

---

## Real-time Feedback Mechanism (NEW in v3.8)

### Generation Process Monitoring:
> 📄 代码已提取到 `references\code_58.python`（12 行，366 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_59.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_59.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Real-time Parameter Adjustment:
> 📄 代码已提取到 `references\code_60.python`（12 行，316 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_61.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_61.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Execution Rules (NEW in v3.8):
25. **ALWAYS monitor generation progress** — use `monitor_generation_progress()` for long generations
26. **ALWAYS support interruption** — check for user interruption every 2 seconds
27. **ALWAYS adjust parameters dynamically** — analyze intermediate results every 5 steps
28. **ALWAYS use feedback loop** — iterate until quality threshold met (max 3 iterations)

---

## Multi-modal Input Support (NEW in v3.7)

### Supported Input Modalities:
| Modality | Format | Purpose | Example |
|----------|--------|---------|---------|
| **Text** | String | Main prompt / instruction | "Generate a vacuum cup with titanium body" |
| **Image** | URL / Base64 / File Path | Reference image / style guide | "@/path/to/reference.jpg" |
| **Image + Text** | JSON | Joint input (image + prompt) | `{"image": "...", "prompt": "..."}` |
| **Batch** | JSON Array | Multiple inputs (batch processing) | `[{"image": "..."}, {"prompt": "..."}]` |

要点：
- > [引用] 完整代码已提取到 `references\code_block_62.json`（22 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_62.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_63.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_63.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




### Image + Text Joint Prompt Construction:
> [引用] 完整代码已提取到 `references\code_block_64.txt`（47 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_64.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_65.txt`（23 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_65.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。


json
- {
- "modality": "image+text",
- "inputs": {
- "text": {
- "prompt": "Generate a vacuum cup with titanium body, brushed finish, and pop-up lid",
- "negative_prompt": "plastic texture, asymmetric lid, low quality"
- },
- "image": {
- "source": "@/reference/cup_design.jpg",
- "type": "reference",
- "preprocessing": "resize(512x512)+normalize",
- "weight": 0.7
- }
- },
- "options": {
- "combine_method": "concat",
- "output_format": "json",
- "quality_threshold": 7.0
- }
- }
## Phase 4.5: Version Management Enhancement (NEW in v4.0)

### A. Version Management Strategy
- **Git Integration**: All ComfyUI workflows stored in Git repository
- **Workflow Versioning**: Each workflow JSON has version field
- **Semantic Versioning**: MAJOR.MINOR.PATCH (e.g., 2.1.3)
- **Branch Strategy**: main (stable), dev (testing), feat/* (new features)

### B. Version Comparison Mechanism
> [引用] 完整代码已提取到 `references\code_block_66.python`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_66.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### C. Version Rollback
> 📄 代码已提取到 `references\code_67.python`（16 行，507 字节）
> 需要查看完整代码时请读取该文件。



### D. Version Release
> [引用] 完整代码已提取到 `references\code_block_68.python`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_68.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### E. Version Management Best Practices
1. **Commit Message Format**: `[WorkflowName] v2.1.3 - Description`
2. **Tag Naming**: `v2.1.3-workflow-name`
3. **Rollback Policy**: Keep last 3 stable versions
4. **Testing**: Always test before release
5. **Documentation**: Update CHANGELOG.md for each release

---

---



---

## Prompt Library: comfyui_presets

| 预设名称 | Checkpoint | LoRA | Sampler |
|----------|-------------|------|---------|
| 保温杯（圆柱形）生图预设 | v1-5-pruned-emaonly.safetensors | vacuum-cup-v1.safetensors | DPM++ 2M Karras |
| 饭盒（宽口）生图预设 | v1-5-pruned-emaonly.safetensors | food-jar-v1.safetensors | DPM++ 2M Karras |
| 水壶（带手柄）生图预设 | v1-5-pruned-emaonly.safetensors | water-bottle-v1.safetensors | DPM++ 2M Karras |

**完整配置见** `prompt_library.json`


---

## Prompt Library: by_product_type

| 产品类型 | 子类型 | 正面提示词 |
|----------|--------|--------------|
| 保温杯 | 圆柱形 | perfectly cylindrical cup body, constant diameter, symmetrical left-right... |
| 保温杯 | 锥形 | tapered cup body (wider top, narrower bottom), elegant taper angle, smooth transition... |
| 饭盒 | 宽口 | wide mouth food jar (easy access), large opening diameter, stackable design... |
| 水壶 | 带手柄 | ergonomic handle, comfortable grip, sturdy handle attachment... |
| 配件 | 杯盖 | pop-up lid mechanism, smooth opening/closing, airtight seal when closed... |
| 配件 | 密封圈 | silicone seal ring, food-grade silicone, perfectly round cross-section... |

**完整提示词见** `prompt_library.json`


---

## Phase 5.0: Memory Compression & Performance Optimization (OPTIMIZED in v5.0)

### A. 显存管理策略（优化版 - v5.0）

> [引用] 完整代码已提取到 `references\code_block_69.python`（38 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_69.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### B. 奖励机制（NEW in v5.0）

**核心思想**：当生成质量优秀时，奖励更多显存/更大batch size，加快后续生成速度。

> [引用] 完整代码已提取到 `references\code_block_70.python`（62 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_70.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### C. 显存碎片化整理机制（NEW in v5.0）

**问题**：长时间运行后，显存会出现碎片化（小块空闲显存无法被大tensor使用）。

**解决方案**：定期整理显存碎片。

> [引用] 完整代码已提取到 `references\code_block_71.python`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_71.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




**触发条件**（满足任一即触发）：
- 显存碎片化 > 30%
- 连续生成 > 20 张图像后
- 检测到 OOM 错误后
- 用户手动调用 `/vram_defrag` 命令

### D. 多模型并行加载的显存调度策略（NEW in v5.0）

**场景**：需要同时加载 Checkpoint + 多个 LoRA + 多个 ControlNet。

**策略**：按需加载 + 优先级调度。

> [引用] 完整代码已提取到 `references\code_block_72.python`（58 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_72.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### E. 性能监控（优化版 - v5.0）

> [引用] 完整代码已提取到 `references\code_block_73.python`（35 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_73.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。





---

## Phase 1.2: ControlNet Usage Guide (NEW in v5.0)

**Complete ControlNet usage guide (2026 version)**:

> [引用] 完整代码已提取到 `references\code_block_74.txt`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_74.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




**Output**: Workflow Optimization Report (Markdown format)


### F. 最佳实践（优化版 - v5.0）

1. **优先使用 FP16**（半精度）- 节省50%显存
2. **及时卸载模型** - 生成任务完成后立即调用 `unload_all_temp_models()`
3. **使用 xFormers** - 进一步优化显存使用（需要安装 `xformers`）
4. **避免同时加载多个大模型** - 使用 `MultiModelVRAMScheduler` 进行调度
5. **定期整理显存碎片** - 每生成20张图像或碎片化 > 30% 时触发
6. **监控奖励系统状态** - 如果 `high_quality_mode` 解锁，可以享受更高质量的生成
7. **OOM 后自动降级** - 如果检测到 OOM，自动切换到 fp8 + batch_size=1

**版本** : v5.0 (2026-06-05)
**优化内容**: 添加奖励机制、显存碎片化整理、多模型调度策略


---

## Phase 5.5: Automated Workflow Performance Metrics (NEW in v3.5)

**Objective**: Automatically score ComfyUI workflow performance.

### Workflow Performance Metrics:

> 📄 代码已提取到 `references\code_75.python`（17 行，566 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 5.7: Comparative Workflow Analysis (NEW in v3.5)

**Objective**: Compare workflow with other workflows to identify optimization opportunities.

> 📄 代码已提取到 `references\code_76.python`（9 行，395 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 5.9: Memory Compression (NEW in v3.5)

**Objective**: Compress workflow data for token efficiency.

### Token Budget: 2000 tokens
- Workflow description: 500 tokens
- Performance metrics: 700 tokens
- Optimization suggestions: 800 tokens


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

## Phase 8: 工作流性能优化与自动诊断 (NEW in v7.2)

### 8.1 性能瓶颈识别

**ComfyUI工作流常见性能瓶颈**：
1. **显存不足**：高分辨率+高batch_size导致OOM
2. **节点冗余**：不必要的中间节点占用显存
3. **模型加载慢**：大模型（SDXL/FLUX）加载时间长
4. **ControlNet冲突**：多个ControlNet同时使用时性能下降

**诊断方法**：
```python
# 性能指标采集
performance_metrics = {
    "vram_usage": get_vram_usage(),  # 显存占用
    "inference_time": get_inference_time(),  # 推理时间
    "node_count": count_nodes(workflow),  # 节点数量
    "model_load_time": get_model_load_time()  # 模型加载时间
}

# 瓶颈识别
if performance_metrics["vram_usage"] > 0.9:
    bottleneck = "显存不足"
elif performance_metrics["node_count"] > 50:
    bottleneck = "节点冗余"
elif performance_metrics["model_load_time"] > 10:
    bottleneck = "模型加载慢"
```

### 8.2 性能优化策略

**策略1：显存优化**
- 降低输出分辨率（1920×1080 → 1280×720）
- 使用tiled VAE（分块编码，减少显存峰值）
- 启用attention slicing（减少注意力层显存占用）

**策略2：节点精简**
- 移除不必要的中间预览节点
- 合并相同功能的节点（如多个VAE编码器合并为一个）
- 使用高效节点替代（如`VAEDecodeOnly`替代`VAEDecode+VAEEncode`）

**策略3：模型加载优化**
- 使用模型缓存（避免重复加载）
- 预加载常用模型（session开始时加载）
- 使用更轻量的模型（SD1.5替代SDXL，FLUX-schnell替代FLUX-dev）

**策略4：ControlNet优化**
- 限制ControlNet数量（≤2个）
- 降低ControlNet分辨率（512×512）
- 使用轻量ControlNet（canny  → qr_monster）

### 8.3 生图失败自动诊断与修复

**常见失败类型与自动修复**：

| 失败类型 | 错误信息 | 自动诊断 | 自动修复 |
|-----------|----------|----------|----------|
| **OOM** | `CUDA out of memory` | 显存占用>95% | 降低分辨率/启用tiled VAE |
| **模型未找到** | `Model not found` | 模型路径错误 | 自动修正路径/下载模型 |
| **节点连接错误** | `Node connection error` | 节点输入输出不匹配 | 自动修正连接/使用默认连接 |
| **ControlNet冲突** | `ControlNet conflict` | 多个ControlNet权重冲突 | 降低权重/减少ControlNet数量 |
| **LoRA冲突** | `LoRA conflict` | 多个LoRA强度冲突 | 降低强度/移除冲突LoRA |

**自动诊断流程**：
```
1. 捕获错误信息
2. 匹配失败类型（查表）
3. 执行自动诊断（检查配置）
4. 生成修复方案
5. 自动应用修复（或提示用户确认）
6. 重新执行生图
7. 验证修复效果
```

### 8.4 性能监控与报告

**监控指标**：
- 生图成功率（目标≥95%）
- 平均显存占用（目标≤80%）
- 平均推理时间（目标≤30s）
- 工作流节点数（目标≤40）

**性能报告格式**：
```json
{
  "workflow_id": "WF-2026-0619-001",
  "performance": {
    "success_rate": 0.92,
    "avg_vram_usage": 0.78,
    "avg_inference_time": 28.5,
    "node_count": 35
  },
  "bottlenecks": ["显存占用偏高", "推理时间偏长"],
  "optimization_suggestions": [
    "启用tiled VAE减少显存占用",
    "使用FLUX-schnell替代FLUX-dev提升速度"
  ],
  "auto_fixes_applied": [
    "降低输出分辨率至1280×720",
    "移除冗余预览节点3个"
  ]
}
```

### 8.5 与评审联动（🐔→🐴→🐍/🐑）

**联动规则**：
1. **🐔评审反馈** → 🐴接收 → 自动诊断性能问题 → 应用优化策略
2. **优化后** → 🐴通知🐔 → 重新评审 → 验证优化效果
3. **严重问题** → 🐴通知🐭（主理人） → 人工介入

**自动优化触发条件**：
- 连续3次生图失败 → 触发自动诊断
- 显存占用持续>90% → 触发显存优化
- 推理时间>60s → 触发速度优化

---

## 参考资料 (NEW in v6.0)

### ComfyUI API调用详细指南

本Skill聚焦工作流优化，ComfyUI API调用的详细实现请参考独立指南：

**文档路径**: `H:/AI日记/Claw/ComfyUI_工作流API调用指南_V1.0_2026-06-18.md`

**指南内容**:
1. ComfyUI API接口概述
2. 工作流JSON格式详解
3. Python调用示例
4. 批量生成脚本
5. 工作流API格式转换
6. 常见错误处理
7. 性能优化建议

**快速开始**:
```python
# 1. 安装依赖
pip install requests websocket-client Pillow

# 2. 使用示例
from comfyui_client import ComfyUIClient

client = ComfyUIClient()
with open("workflow_api.json", "r") as f:
    workflow = json.load(f)

result = client.queue_prompt(workflow)
outputs = client.wait_for_completion(result["prompt_id"])
```

> 💡 **提示**: 详细代码和说明请阅读独立指南文档。
