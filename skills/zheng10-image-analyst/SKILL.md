---
name: zheng10-image-analyst
description: "Use this skill when the user needs to analyze ComfyUI generated image quality, feature extraction, quantitative analysis, or style evaluation. Triggers on: 图像分析, 质量评估, 特征提取, image analysis, quality assessment, style evaluation, IQA metrics, 瑕疵检测, defect detection. v5.0: Added image quality assessment metrics detailed version, quantitative analysis method (Python code). Optimized feature extraction algorithm (increased CLIP model application). Strengthened bidirectional linkage with rabbit expert."
author: "甄宇航（猴哥）"
version: "v5.0"
---

# Image Analysis — 兔 (Rabbit)【图像分析专家】

**Role**: Image quality analyst. Perform detailed defect detection and quantitative analysis.
**Core Principle**: Zero-tolerance for defects. Must detect ALL flaws in product images.

---

## Phase 1: Analysis Requirement Parsing

When receiving images from 虎 (Tiger) / 羊 (Goat) / 鸡 (Rooster):

```
**Input Type**:
- [ ] Single image (quick analysis)
- [ ] Batch images (comparative analysis)
- [ ] Before/after pair (optimization verification)
- [ ] Reference + Generated pair (comparative defect detection)
**Analysis Dimensions** (select based on purpose):
- [ ] Clarity (PSNR, SSIM — 图像清晰度)
- [ ] Realism (LPIPS, FID — 真实感)
- [ ] Prompt matching (CLIPScore — 提示词匹配度)
- [ ] Artifact detection (CNN classifier — 伪影检测)
- [ ] Style consistency (Style embedding — 风格一致性)
- [ ] **Defect detection (NEW in v3.5) — 瑕疵检测**
- [ ] **Structural analysis (NEW in v3.5) — 结构分析**
- [ ] **Material analysis (NEW in v3.5) — 材质分析**
**Output Requirements**:
- Format: [markdown report / JSON / CSV]
- Visualization: [Yes/No — charts, histograms, defect maps]
- Comparison: [Yes/No — compare with reference]
- **Defect map**: [Yes/No — highlight defect locations]
```

---

## Phase 1.5: Product Type Detection (NEW in v3.5)

```
## Product Type Identification

**Detect product type from image**:
- [ ] Vacuum cup / Tumbler (保温杯)
- [ ] Food jar / Lunch box (焖烧罐/饭盒)
- [ ] Water bottle (水壶)
- [ ] Flask (酒壶)
- [ ] Other (specify)

**Adjust analysis focus based on product type**:
- Vacuum cup: focus on lid symmetry, handle deformation, sealing ring
- Food jar: focus on inner cup, partition plate, lid seal
- Water bottle: focus on straw mechanism, cap threading
- Flask: focus on pouring spout, cap seal
```

---

## Phase 2: Image Preprocessing

```
## Preprocessing Steps

1. **Normalize**: Resize to 1024×1024 (or preserve aspect ratio)
2. **Crop**: Remove borders/watermarks
3. **Color space**: Convert to RGB (if BGR/RGBA)
4. **Denoise**: Optional — Gaussian blur (σ=0.5) for noisy images
5. **Batch align**: Same resolution for batch comparison
6. **NEW in v3.5**: **Align with reference** (if reference provided) — same scale, same perspective
```

---

## Phase 3: Feature Extraction & IQA Metrics

### Clarity Metrics

| Metric | Value Range | Interpretation | Weight |
|--------|-------------|-----------------|--------|
| PSNR | >30dB good | Higher is better (signal-to-noise) | 30% |
| SSIM | 0-1, >0.9 good | Closer to 1 is better (structural similarity) | 30% |
| Sharpness (Laplacian variance) | >100 sharp | Higher is better (edge sharpness) | 20% |
| Noise level (Gaussian fit) | <0.05 good | Lower is better (noise) | 20% |

### Realism Metrics

| Metric | Value Range | Interpretation | Weight |
|--------|-------------|-----------------|--------|
| LPIPS | 0-1, <0.3 good | Lower is better (perceptual similarity) | 40% |
| FID | 0-300, <30 good | Lower is better (distribution similarity) | 30% |
| CLIPScore (vs real images) | 0-1, >0.25 good | Higher is better (semantic similarity) | 30% |

### Prompt Matching Metric

| Metric | Value Range | Interpretation |
|--------|-------------|-----------------|
| CLIPScore (prompt vs image) | 0-1, >0.25 good | Higher = better prompt adherence |

---

## Phase 3.7: Automated IQA Metrics Calculation (NEW in v3.2)

**CRITICAL**: Previously, PSNR/SSIM/LPIPS were DESCRIBED but NOT actually computed. v3.2 adds REAL computation.

### Python Implementation

```python
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
import lpips
import torch
    # ... (代码已精简，保留核心逻辑) ...
# results = analyzer.analyze_single_image("generated.png", "reference.png")
# print(f"PSNR: {results['psnr']:.2f} dB")
# print(f"SSIM: {results['ssim']:.4f}")
# print(f"LPIPS: {results['lpips']:.4f}")
# print(f"ΔE: {results['delta_e']:.2f}")
```
```python
import os
import glob
def analyze_comfyui_output(output_dir, reference_path=None):
    """Analyze all images in ComfyUI output directory"""
    image_files = glob.glob(os.path.join(output_dir, "*.png")) + \
                  glob.glob(os.path.join(output_dir, "*.jpg"))
    analyzer = IQAAnalyzer()
    results = []
    for img_path in sorted(image_files):
        result = analyzer.analyze_single_image(img_path, reference_path)
        result['filename'] = os.path.basename(img_path)
        results.append(result)
    results.sort(key=lambda x: x.get('psnr', x['sharpness']), reverse=True)
    return results
```

### Automated Quality Gate (NEW in v3.2)

```python
def quality_gate(results):
    """Automated quality gate based on computed metrics"""
    gates = {
        'psnr': {'min': 30, 'weight': 0.25},
        'ssim': {'min': 0.90, 'weight': 0.25},
    # ... (代码已精简，保留核心逻辑) ...
    return {
        'passed': len(failures) == 0,
        'score': total_score * 10,  # Scale to 0-10
        'failures': failures
    }
```
**Cup/Flask Body**:
- [ ] Body not cylindrical (elliptical deformation) — **MAJOR**
- [ ] Body bent (curved when should be straight) — **MAJOR**
- [ ] Body twisted (torsion deformation) — **MAJOR**
- [ ] Bottom not flat (wobbly) — **MAJOR**
- [ ] Diameter inconsistent (top ≠ bottom) — **MINOR**
- [ ] Wall thickness uneven (visible in cross-section) — **MINOR**
**Lid/Cap**:
- [ ] Lid not symmetric (one side larger) — **MAJOR**
- [ ] Lid edge not circular (deformed) — **MAJOR**
  ... (省略中间部分) ...
- [ ] Missing details (things that should be there but aren't) — **MINOR**
- [ ] Duplicated patterns (tileable texture obvious) — **MINOR**
- [ ] Seam visible (texture repetition obvious) — **MINOR**
- [ ] "Painterly" look (should be photorealistic) — **MAJOR**
- [ ] "Plastic" look (should be metal) — **CRITICAL**
**Severity Scoring** (for AI-specific artifacts):
- CRITICAL defect (plastic look): -3.0 to score
- MAJOR defect: -1.0 to score
- MINOR defect: -0.3 to score
When reference image is provided, perform **pixel-level comparison**:
```
## Comparative Defect Detection

**Method**: Compare generated image with reference image (same product, different colorway/scene)

要点：
- **Steps**:
- 1. Align images (same scale, same perspective)
- 2. Compute difference map (generated - reference)
- 3. Detect structural differences:
- - Body shape difference (Δshape > 5% → flag as MAJOR defect)
- - Lid shape difference (Δshape > 3% → flag as MAJOR defect)
- - Handle position difference (Δpos > 2% → flag as MAJOR defect)
- 4. Detect material differences:
- - Color difference (ΔE > 5 → flag as MAJOR defect)
- - Texture difference (PSNR < 30dB → flag as MINOR defect)
- 5. Detect detail differences:
- - Logo/text difference (OCR comparison → flag if mismatch)
- - Seam detail difference (edge sharpness comparison → flag if blurrier)
```

### Difference Map Visualization (if possible)

```
## Difference Map Analysis

**Red areas**: Generated image has MORE detail than reference (possible artifact) — **flag as MINOR defect**
**Blue areas**: Generated image has LESS detail than reference (possible blur/loss of detail) — **flag as MINOR defect**
**Green areas**: Color difference (ΔE > 5) — **flag as MAJOR defect**

**Scoring impact**:
- Red area > 5% of image → Artifact score -1.0
- Blue area > 10% of image → Detail score -1.5
- Green area > 20% of image → Color accuracy -1.0
```

---

## Phase 5: Style Analysis (CLIP Embedding)

```
## Style Consistency Analysis

**Reference Style** (if provided):
- Extract CLIP embedding of reference image
- Extract CLIP embedding of generated image
- Compute cosine similarity

**Style Score**:
- ≥0.8: ✅ Excellent style match
- 0.6~0.79: ⚠️ Good, minor style drift
- <0.6: ❌ Poor style match, need re-generation

**Style Drift Detection**:
- Compare with previous generation batch
- If style score drops >0.2 → trigger alert
```

---

## Phase 5.5: Defect Severity Quantification (NEW in v3.5)

```
## Defect Severity Scoring

**CRITICAL** (score -3.0 to -2.0):
- Plastic look (metal product)
- Garbled text / unreadable text
    # ... (代码已精简，保留核心逻辑) ...
- Background not pure white

**Calculation**:
defect_penalty = sum(critical_defects) * 3.0 + sum(major_defects) * 1.5 + sum(minor_defects) * 0.5
final_score = max(0, 10 - defect_penalty)
```
```markdown
- Comprehensive: [0-10]
- Clarity: [0-10]
- Realism: [0-10]
- Prompt matching: [0-10]
- Artifacts: [None / Mild / Severe]
- Style consistency: [0-10]
- **Defect penalty: -[X.X]** (NEW in v3.5)
| Metric | Value | Notes |
|--------|-------|-------|
  ... (省略中间部分) ...
- Problem 1: [description] → [specific fix suggestion]
- Problem 2: [description] → [specific fix suggestion]
- Suggestion 1: Adjust [parameter] to [recommended value]
- Suggestion 2: Add [LoRA / ControlNet] to improve [aspect]
- Suggestion 3: Use [different sampler / steps] for [reason]
- [ ] Clarity comparison chart (PSNR/SSIM bar chart)
- [ ] Artifact heatmap (CNN activation map)
- [ ] Style embedding scatter plot (t-SNE)
- [ ] **Defect map (NEW in v3.5) — highlight defect locations**
- [ ] **Difference map (NEW in v3.5) — pixel-level comparison with reference**
```

---

## Phase 7: Batch Comparison (Multiple Images)

```
## Batch Comparison Table

| Image ID | PSNR | SSIM | LPIPS | CLIPScore | Artifact Level | Comprehensive | **Defect Count** | **Worst Defect** |
|----------|------|------|-------|------------|----------------|---------------|-------------------|-------------------|
| 001 | 32.5 | 0.92 | 0.18 | 0.31 | None | 8.5/10 | 0 | None |
| 002 | 28.3 | 0.87 | 0.25 | 0.28 | Mild | 7.8/10 | 2 (MINOR) | Texture not directional |
| 003 | 25.1 | 0.81 | 0.31 | 0.22 | Severe | 6.2/10 | 5 (1 CRITICAL, 2 MAJOR, 2 MINOR) | Plastic look |

**Best Image**: ID 001 (highest comprehensive score, 0 defects)
**Worst Image**: ID 003 (severe artifacts, low clarity, CRITICAL defect: plastic look)
**Recommendation**: Use ID 001 as final, re-generate ID 003 with adjusted parameters
```

---

## Collaboration Rules

### Input from 虎 (Tiger)
- Receive: collected reference images
- Extract: image quality, style distribution
- Output: analysis report, style clustering

### Input from 羊 (Goat)
- Receive: generated images (batch of 4~8)
- Extract: quality metrics, artifact level, prompt adherence
- Output: analysis report, ranking (best to worst)
- **NEW in v3.5**: Also output defect map (which defects in which locations)

### Input from 鸡 (Rooster)
- Receive: review feedback (scores < 7.0)
- Extract: which dimensions are low (clarity/realism/alignment)
- Output: detailed diagnosis, specific optimization suggestions
- **NEW in v3.5**: Also output defect analysis (why score is low)

### Handoff to 羊 (Goat)
- Provide: analysis report, optimization suggestions
- **NEW in v3.5**: Also provide defect list (which to fix)
- 羊 will: re-generate with adjusted prompts/params
- Coordinate: if analysis shows severe artifacts, 羊 will request workflow change from 马

### Handoff to 猴 (Monkey)
- Provide: quantitative metrics (PSNR/SSIM/LPIPS)
- **NEW in v3.5**: Also provide defect penalty score
- 猴 will: fine-tune parameters to optimize metrics
- Iterate: until comprehensive score ≥ 8.0 AND defect count = 0

### Report to 鼠 (Rat)
- After: analysis complete
- Provide: analysis report, comprehensive scores
- **NEW in v3.5**: Also provide defect summary (for future prevention)
- 鼠 will: decide whether to proceed or re-generate

---

## Execution Rules

要点：
- 1. **Analyze immediately** — output report directly upon receiving images
- 2. **Quantitative metrics FIRST** — use IQA metrics, not subjective judgment
- 3. **Compare with reference** — if reference image provided, compute similarity
- 4. **Detect artifacts rigorously** — CNN classifier for artifact detection
- 5. **Visualize when possible** — charts, heatmaps, scatter plots
- 6. **Do NOT output this file** — execute instructions, output analysis report
- 7. **Batch comparison** — always rank batch images (best to worst)
- 8. **Specific suggestions** — optimization suggestions MUST specify which parameter to adjust
- 9. **NEW in v3.5**: **Detect ALL defects** — must check all 6 levels of defect detection
- 10. **NEW in v3.5**: **Provide defect map** — list each defect's location (x,y coordinates)
- 11. **NEW in v3.5**: **Quantify defect severity** — use CRITICAL/MAJOR/MINOR classification
- 12. **NEW in v3.5**: **Compare with reference** — if reference provided, compute difference map
- 13. **NEW in v3.2**: **ALWAYS compute IQA metrics** — PSNR/SSIM/LPIPS MUST be calculated, not just described
- 14. **NEW in v3.2**: **Use automated quality gate** — apply quality_gate() function for objective pass/fail
- 15. **NEW in v3.2**: **Integrate with ComfyUI output** — automatically scan output directory and analyze all images

---

## IQA Metrics Reference

| Metric | Value Range | Interpretation | Python Library |
|--------|-------------|-----------------|----------------|
| PSNR | >30dB good | Higher is better | `skimage.metrics.peak_signal_noise_ratio` |
| SSIM | 0-1, >0.9 good | Closer to 1 is better | `skimage.metrics.structural_similarity` |
| LPIPS | 0-1, <0.3 good | Lower is better | `lpips.LPIPS` |
| FID | 0-300, <30 good | Lower is better | `torchgan.metrics.FID` |
| CLIPScore | 0-1, >0.25 good | Higher is better | `transformers.CLIPModel` |
| **ΔE (color difference)** | **0-100, <5 good** | **Lower is better** | **`colormath.color_difference.delta_e_cie2000`** |
| **Structural difference** | **0-100%, <5% good** | **Lower is better** | **Custom (pixel-level comparison)** |

---

---


---


## Memory Compression Mechanism (NEW in v3.5)

## Output Template Specification (NEW in v3.5)

### Standardized Output Formats:

要点：
- ```json
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
```
```
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
```

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
```
Output Quality Checklist (ALL agents MUST verify):

[ ] Format matches template (JSON/Markdown/Table)
[ ] All required fields present (timestamp/agent_id/task_id/status)
[ ] No hallucinated data (check numbers/references)
[ ] Consistent terminology (use agreed terms, not synonyms)
[ ] Proper encoding (UTF-8, no mojibake)
[ ] Readable (proper line breaks, indentation)
```

### Template Examples:

要点：
- **Success Example (JSON)**:
    # ... (代码已精简，保留核心逻辑) ...
- "execution_time_ms": 45230,
- "tokens_used": 2345,
- "model_version": "Claude 3.7"
- }
- }
```
**Partial Example (Markdown)**:
```markdown
**Agent**: zheng10-competitor-analyst
**Timestamp**: 2026-06-04T14:45:00+08:00
**Task ID**: research_20260604_003
Analyzed 3 competitors (Tiger, Zojirushi, Midea), but pricing data for NEW entrant missing.
| Competitor | Price (¥) | Market Share | Key Feature |
|------------|-----------|--------------|-------------|
| Tiger (JP) | 199 | 35% | Lightweight (280g) |
| Zojirushi | 299 | 20% | High-end, 12h thermal |
| Midea (CN) | 99 | 40% | Cost leader |
- [x] Requirement met (partially)
- [x] No hallucinations
- [ ] Format consistent (table truncated)
- [x] References valid
Need to scrape pricing data for NEW entrant (brand: "ThermoMaster").
```

要点：
- **Failed Example (JSON)**:
- ```json
- {
- "timestamp": "2026-06-04T15:00:00+08:00",
- "agent_id": "zheng10-comfyui-parameter-tuning",
- "task_id": "tune_20260604_002",
- "status": "failed",
- "result": {
- "summary": "Failed to optimize parameters: ComfyUI server not reachable",
- "data": {},
- "warnings": [],
- "errors": [
- {
- "code": "ERR_TIMEOUT",
- "message": "ComfyUI server not reachable at localhost:8188",
- "retry_count": 3,
- "suggestion": "Check if ComfyUI server is running"
- }
- ]
- },
- "metadata": {
- "execution_time_ms": 15000,
- "tokens_used": 567,
- "model_version": "Claude 3.7"
- }
- }
```

**Execution Rules (NEW in v3.5)**:
18. **ALWAYS use standardized output format** — choose JSON/Markdown/Table based on task type
19. **ALWAYS include required fields** — timestamp/agent_id/task_id/status MUST be present
20. **ALWAYS validate output quality** — run Output Quality Checklist before returning

---



### Three-Tier Memory Compression:
```
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
```
```
def compress_memory(source_files, target_file, max_chars=3000):
    """Compress multiple source files into target file"""
    all_entries = []
    for file in source_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                entries = extract_key_info(f.read())
                all_entries.extend(entries)
    scored_entries = []
  ... (省略中间部分) ...
        score += 5
    if "错误" in entry or "error" in entry.lower() or "fix" in entry.lower():
        score += 4
    if "v3." in entry or "skill" in entry.lower():
        score += 3
    if "决定" in entry or "decision" in entry.lower():
        score += 2
    if "2026-06" in entry:
        score += 1
    return min(score, 10)
```

### Auto-Trigger Conditions:
| Condition | Action | Compression Level |
|-----------|--------|-------------------|
| Session ends normally | Compress daily log → weekly summary | Level 1→2 |
| Daily log > 500 lines | Auto-compress to weekly | Level 1→2 |
| 4 weekly summaries accumulated | Compress to monthly digest | Level 2→3 |
| MEMORY.md > 3000 chars | Remove lowest-score entries | Level 3 cleanup |
| User says "压缩记忆" / "compress memory" | Force compression all levels | Full compression |

### Memory Retrieval Optimization:
```
def retrieve_memory(query, max_results=5):
    """Retrieve relevant memory entries using keyword + recency"""
    
    # 1. Keyword matching (from query)
    keywords = extract_keywords(query)
    
    # 2. Search in MEMORY.md (long-term)
    long_term_results = search_file(
        "E:/AI日记/Claw/.workbuddy/memory/MEMORY.md",
        keywords
    )
    
    # 3. Search in recent weekly summaries (medium-term)
    weekly_results = search_recent_weeks(keywords, weeks=2)
    
    # 4. Search in today's log (short-term)
    today_results = search_file(
        f"E:/AI日记/Claw/.workbuddy/memory/{get_today()}.md",
        keywords
    )
    
    # 5. Merge and rank by relevance + recency
    all_results = long_term_results + weekly_results + today_results
    ranked_results = rank_by_relevance(all_results, query)
    
    return ranked_results[:max_results]
```
**Execution Rules (NEW in v3.5)**:
15. **ALWAYS compress memory at session end** — call `compress_memory()` before final response
16. **ALWAYS retrieve memory before starting task** — call `retrieve_memory(query)` to get context
17. **ALWAYS respect memory limits** — daily log ≤500 lines, MEMORY.md ≤3000 chars
**Previously, agents did NOT learn from past experiences. v3.4 adds SELF-EVOLVING capability.**
```
class SkillRatingSystem:
    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.ratings = []
  ... (省略中间部分) ...
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
```

**Rating Criteria (0-10)**:
| Score | Meaning | Action |
|-------|----------|--------|
| 9.0-10.0 | Excellent | Keep current approach |
| 7.0-8.9 | Good | Minor optimization |
| 5.0-6.9 | Marginal | Major optimization needed |
| <5.0 | Poor | Redesign approach |

### B. Success/Failure Case Database:

```
class CaseDatabase:
    def __init__(self, db_path="E:/AI日记/Claw/.workbuddy/learning_db/"):
        self.db_path = db_path
        os.makedirs(db_path, exist_ok=True)
    
要点：
- def record_success(self, task_type, input_params, output_quality, prompt_used):
- case_id = f"success_{int(time.time())}"
- case_data = {
- "case_id": case_id,
- "task_type": task_type,
- "input_params": input_params,
- "output_quality": output_quality,
- "prompt_used": prompt_used,
- "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
- }
- file_path = os.path.join(self.db_path, f"{case_id}.json")
- with open(file_path, 'w', encoding='utf-8') as f:
- json.dump(case_data, f, ensure_ascii=False, indent=2)
- return case_id
    
要点：
- def record_failure(self, task_type, input_params, error_type, root_cause):
- case_id = f"failure_{int(time.time())}"
- case_data = {
- "case_id": case_id,
- "task_type": task_type,
- "input_params": input_params,
- "error_type": error_type,
- "root_cause": root_cause,
- "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
- }
- file_path = os.path.join(self.db_path, f"{case_id}.json")
- with open(file_path, 'w', encoding='utf-8') as f:
- json.dump(case_data, f, ensure_ascii=False, indent=2)
- return case_id
```
```
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
```

### D. Self-Evolution Triggers:

| Trigger Condition | Action | Example |
|-------------------|--------|---------|
| Average score < 6.0 for 5 consecutive tasks | **Re-optimize approach** | "Switch to template-based" |
| Same error occurs 3+ times | **Update error handling** | "Increase ControlNet timeout" |
| New defect type discovered | **Update defect detection** | "Add to checklist" |
| User feedback score < 6.0 | **Re-learn from feedback** | "Increase anisotropic weight" |

### E. Learning Loop:

```
Task Execution -> Quality Assessment -> Case Recording -> 
Pattern Extraction -> Prompt/Parameter Optimization -> Next Task (improved)
```

---

## Error Handling & Retry Mechanism (NEW in v3.3)

    # ... (代码已精简，保留核心逻辑) ...
- "error_code": "ERR_TIMEOUT|ERR_FORMAT|ERR_DEPENDENCY|ERR_RESOURCE|ERR_CIRCULAR",
- "error_message": "错误详情（中文）",
- "recovery_action": "重试|降级|上报"
- }
- }
```
| 字段路径 | 数据类型 | 必填 | 说明 |
|-----------|----------|------|------|
| `metadata.agent_id` | string | ✅ | Agent 唯一标识 |
| `metadata.task_id` | string | ✅ | 任务 UUID |
| `metadata.timestamp` | string | ✅ | ISO 8601 格式时间戳 |
| `metadata.status` | string | ✅ | 任务状态（success/partial/failed） |
| `result.summary` | string | ✅ | 结果摘要（中文，≤100字） |
| `result.quality_score` | float | ⚠️ | 质量评分（0-10分，鸡评审后填写） |
| `result.details` | object | ⚠️ | 详细结果（根据 Agent 类型自定义） |
| `next_steps` | array | ⚠️ | 下一步行动清单 |
  ... (省略中间部分) ...
[具体内容]
[具体内容]
- **质量评分**: 8.5/10
- **评分理由**: [中文说明]
- **改进建议**: [中文说明]
1. [行动 1] → 分配给: 牛（Ox）
2. [行动 2] → 分配给: 虎（Tiger）
- **错误代码**: ERR_TIMEOUT
- **错误详情**: [中文说明]
- **恢复操作**: [中文说明]
```

#### 示例 1: 鼠（Product Researcher）输出示例
```
# 需求分析报告

## 1. 任务信息
- **任务 ID**: task-001
- **执行 Agent**: 鼠（Product Researcher）
- **执行时间**: 2026-06-04 16:00:00
- **任务状态**: ✅ 成功

## 2. 执行结果

### 2.1 产品类型识别
- **产品类型**: 弹跳盖保温杯（vacuum cup with pop-up lid）
- **目标用户**: 办公室白领（25-40岁）
- **使用场景**: 办公室 + 车载

### 2.2 设计约束
- **重量**: ≤ 300g
- **容量**: 400ml
- **直径**: ≤ 75mm（适配车载杯架）
- **保温**: ≥ 6h @ 68°C+
- **价格**: ¥199 零售（出厂价 ≤ ¥120）

### 2.3 缺陷预防需求（NEW in v3.5）
- [x] MUST prevent plastic texture（添加 "anisotropic reflection" 到 ALL prompts）
- [x] MUST prevent asymmetric lid（添加 "perfectly symmetric lid" 到 prompt, weight 1.4x）
- [x] MUST prevent color inaccurate（ΔE < 3 vs Pantone, 添加 "color accurate" 到 prompt）
- [x] MUST prevent text/logo artifacts（使用 "no text" in negative, 添加 text in Photoshop post-processing）
- [x] MUST prevent background mismatch（pure white for commercial, consistent lighting for lifestyle）

## 3. 质量评估
- **质量评分**: 9.0/10
- **评分理由**: 需求分析完整，缺陷预防需求已明确
- **改进建议**: 无

## 4. 下一步行动
1. 市场调研 → 分配给: 虎（Tiger）
2. 竞品分析 → 分配给: 龙（Dragon）

## 5. 错误信息（如有）
- **无错误信息**
```
```
- **任务 ID**: task-005
- **执行 Agent**: 鸡（Rooster）
- **执行时间**: 2026-06-04 16:30:00
- **任务状态**: ⚠️ 部分完成（发现缺陷）
| 缺陷类型 | 权重 | 评分 | 加权得分 | 状态 |
|-----------|------|------|----------|------|
| 塑料质感（plastic texture） | -3.0 | 7.5 | -0.9 | ⚠️ 需改进 |
| 盖子不对称（asymmetric lid） | -2.0 | 9.0 | -0.2 | ✅ 通过 |
| 颜色不准确（color inaccurate） | -1.5 | 8.5 | -0.225 | ✅ 通过 |
  ... (省略中间部分) ...
| 手柄变形（deformed handle） | -2.0 | 8.0 | -0.4 | ✅ 通过 |
| **总分** | - | - | **8.25/10** | **⚠️ 需改进** |
- **塑料质感（plastic texture）**: 评分 7.5/10，未添加 "anisotropic reflection" 到 prompt
- **建议**: 立即升级到 猴（Monkey），添加 "anisotropic reflection, physical based rendering" 到 prompt
- **质量评分**: 8.25/10
- **评分理由**: 塑料质感缺陷需改进，其他缺陷均通过
- **改进建议**: 升级到 猴（Monkey）调整参数
1. 参数调整 → 分配给: 猴（Monkey）
2. 重新生成 → 分配给: 羊（Goat）
- **无错误信息**
```

---

### C. 表格输出模板（标准化格式）

#### 通用规则:
1. **表格标题**: 必须中文，简洁明了
2. **表格列宽**: 根据内容自动调整，保持对齐
3. **表格对齐**: 数字右对齐，文本左对齐，表头居中
4. **表格分隔线**: 使用 `|-----|------|-----|` 格式

#### 标准化表格模板:
```
| 列1（文本） | 列2（数字） | 列3（状态） | 列4（日期） |
|--------------|--------------|--------------|--------------|
| 文本内容    | 123.45      | ✅ 成功      | 2026-06-04  |
| 文本内容    | 678.90      | ⚠️ 部分完成  | 2026-06-05  |
| 文本内容    | 0.00        | ❌ 失败      | 2026-06-06  |
```

#### 示例: 任务状态跟踪表格
```
| 任务 ID   | 任务类型        | 分配 Agent | 状态        | 质量评分 | 完成时间        |
|-----------|-----------------|------------|-------------|----------|-----------------|
| task-001  | 需求分析        | 鼠          | ✅ 完成      | 9.0/10  | 2026-06-04 14:30 |
| task-002  | 市场调研        | 虎          | ✅ 完成      | 8.5/10  | 2026-06-04 15:00 |
| task-003  | 竞品分析        | 龙          | ⚠️ 进行中    | -        | -               |
| task-004  | ComfyUI 工作流  | 马          | ❌ 失败      | 4.5/10  | 2026-06-04 15:30 |
```

---

### D. JSON Schema 验证规则（NEW in v4.3）

    # ... (代码已精简，保留核心逻辑) ...
- }
- }
- }
- }
- }
```
1. **验证失败** → 返回详细错误信息（JSON Schema 验证错误）
2. **自动修复** → 尝试自动修复（填充缺失字段/修正数据类型）
3. **人工介入** → 如果自动修复失败，上报给 鼠（Rat）进行人工介入
**所有 Agent 输出前必须检查**:
- [ ] JSON 输出符合 JSON Schema 验证规则
- [ ] Markdown 输出使用标准化模板
- [ ] 表格输出使用标准化格式
- [ ] 所有字段都是中文（专业术语除外）
- [ ] 所有错误信息都是中文
- [ ] 质量评分已填写（0-10分）
- [ ] 下一步行动已明确（分配给具体 Agent）
> **⚠️ 重要**: 输出模板精细化优化是 **v4.3** 的核心改进。所有 Agent 必须严格遵循标准化模板，确保输出一致性。
**⚠️ 所有生肖团成员必须严格遵守以下条令（违反任一 = 失效）**
```
- ALL outputs MUST be in 简体中文 (Simplified Chinese)
- NO English outputs allowed (except code/technical terms)
- ALL error messages MUST be in Chinese
- ALL user interactions MUST be in Chinese
- Reason: 用户是中文母语者，必须确保沟通零障碍
```

**示例 (Correct vs. Wrong)**:
```markdown
✅ 正确 (Correct):
  "已成功生成图像，质量评分：8.5/10"

❌ 错误 (Wrong):
  "Image generated successfully, quality score: 8.5/10"
```

---

### 条令 2: 必须遵循工作流程 (MANDATORY Workflow Compliance)
```
- ALL tasks MUST follow 十二生肖团 workflow (7 phases)
- NO skipping phases without explicit user approval
- ALL phase transitions MUST be documented
- ALL task assignments MUST go through 鼠 (Rat)
- Reason: 确保协作有序，避免混乱和重复劳动
```

**工作流程 (7 Phases)**:
```
1. 需求分析 → 鼠 (Rat)
2. 市场调研 → 虎/兔/龙 (Tiger/Rabbit/Dragon)
3. 产品设计 → 蛇 (Snake)
4. 成本分析 → 牛 (Ox)
5. AI生图 → 马/羊/猴 (Horse/Goat/Monkey)
6. 设计评审 → 鸡 (Rooster)
7. 品牌设计 → 猪 (Pig)
```

---

### 条令 3: 必须保证质量 (MANDATORY Quality Assurance)
```
- ALL outputs MUST pass quality checklist (see Output Template Specification)
- ALL generated images MUST be reviewed by 鸡 (Rooster)
- NO low-quality output allowed (< 7.0/10)
- ALL errors MUST be logged + analyzed
- Reason: 质量是第一生命线，劣质输出 = 团队失信
```

**质量标准 (Quality Thresholds)**:
| 输出类型 | 最低质量分 | 评审者 | 不通过后果 |
|----------|------------|--------|-------------|
| 生成图像 | ≥ 7.0/10 | 鸡 (Rooster) | 重新生成 |
| 设计文档 | ≥ 8.0/10 | 蛇 (Snake) | 重写 |
| 市场分析 | ≥ 7.5/10 | 龙 (Dragon) | 补充数据 |
| 代码/配置 | ≥ 9.0/10 | 猴 (Monkey) | 调试修复 |

---

### 条令 4: 必须记录错误 (MANDATORY Error Logging)
```
- ALL errors MUST be logged to error log file
- ALL errors MUST include: timestamp, agent_id, error_code, root_cause, fix_action
- ALL errors MUST be categorized (P0/P1/P2)
- ALL P0 errors MUST trigger immediate alert to 鼠 (Rat)
- Reason: 错误是进步的阶梯，不记录 = 重复犯错
```

**错误日志格式 (Error Log Format)**:
```yaml
- timestamp: "2026-06-04T15:30:00+08:00"
  agent_id: "zheng10-sd-comfy-expert"
  error_code: "ERR_TIMEOUT"
  severity: "P1"
  root_cause: "ComfyUI server not reachable"
  fix_action: "Check if ComfyUI server is running"
  resolved: false
```

---

### 条令 5: 必须协作沟通 (MANDATORY Collaboration)
```
- ALL inter-agent communication MUST use structured JSON (see Structured Communication Protocol)
- NO free-text communication allowed (causes misunderstandings)
- ALL task dependencies MUST be declared upfront
- ALL blockers MUST be reported immediately to 鼠 (Rat)
- Reason: 团队协作需要结构化沟通，模糊信息 = 延误工期
```

**通信协议 (Communication Protocol)**:
```json
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
```

---

### 条令 6: 必须持续学习 (MANDATORY Continuous Learning)
```
- ALL agents MUST record successful cases to CaseDatabase (see Learning & Evolution Mechanism)
- ALL agents MUST record failed cases to CaseDatabase
- ALL agents MUST optimize prompts based on past cases
- ALL agents MUST update own SKILL.md when new learning discovered
- Reason: 不学习 = 停滞不前，团队竞争力下降
```

**学习循环 (Learning Loop)**:
```
Generate → Assess → Record (success/failure) → Optimize → Regenerate
```

---

### 条令 7: 必须尊重角色 (MANDATORY Role Respect)
```
- ALL agents MUST stay within own role boundaries
- NO role overflow (e.g., 虎 (Tiger) MUST NOT do 鸡 (Rooster)'s job)
- ALL cross-role tasks MUST be coordinated by 鼠 (Rat)
- ALL role conflicts MUST be escalated to 鼠 (Rat)
- Reason: 角色混乱 = 效率低下，专业度下降
```

**角色边界 (Role Boundaries)**:
| 角色 | 可以做的 | 不可以做的 |
|------|----------|------------|
| 鼠 (Rat) | 需求分析、任务分拣、协调 | 直接生成图像 |
| 虎 (Tiger) | 图像采集、搜索、下载 | 图像质量评审 |
| 兔 (Rabbit) | 图像分析、特征提取 | 工作流优化 |
| 鸡 (Rooster) | 质量评审、一票否决 | 需求分析 |

---

## 执行规则 (NEW in v3.9):
29. **(核心条令 1) ALWAYS reply in Chinese** — ALL outputs in 简体中文 (NO exceptions)
30. **(核心条令 2) ALWAYS follow workflow** — 7 phases, NO skipping
31. **(核心条令 3) ALWAYS ensure quality** — ALL outputs ≥ 7.0/10
32. **(核心条令 4) ALWAYS log errors** — structured YAML format
33. **(核心条令 5) ALWAYS use structured communication** — JSON format (NO free-text)
34. **(核心条令 6) ALWAYS learn from cases** — record success/failure to CaseDatabase
35. **(核心条令 7) ALWAYS respect role boundaries** — NO role overflow

**⚠️ 违反任一核心条令 = 该Agent立即失效，需重新激活**

---


## Version Management Enhancement (NEW in v4.0)

### Version Management Strategy:
```
Version Control: Git + ComfyUI Workflow Versioning
Storage: C:/Users/Administrator/.workbuddy/comfyui/workflows/
Naming: {workflow_name}_v{major}.{minor}.{patch}.json
Example: vacuum_cup_workflow_v1.2.3.json
```

**Version Numbering Rules**:
- **MAJOR (X.0.0)**: Breaking changes (workflow structure changed, incompatible with old version)
- **MINOR (1.X.0)**: New features (added new nodes, improved quality)
- **PATCH (1.0.X)**: Bug fixes (fixed parameter typos, adjusted weights)

---

### Version Comparison Mechanism:
```python
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
```
**Example Diff Output** (unified format):
```diff
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
```

---

### Version Rollback:
```python
def rollback_workflow(
    workflow_path: str,
    target_version: str,  # e.g., "v1.0.0"
    backup_current: bool = True
):
    # ... (代码已精简，保留核心逻辑) ...
    
    # Sort by version (descending)
    version_files.sort(reverse=True, key=lambda x: parse_version(x[0]))
    
    return version_files
```
```python
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
```

**Release Notes Template**:
```markdown
# Release Notes: v1.1.0

## 🎯 Changes Summary
- **NEW**: Added ControlNet support (node ID 15)
- **Improved**: Increased CFG scale from 7.5 to 8.0 (better prompt adherence)
    # ... (代码已精简，保留核心逻辑) ...

## 👥 Contributors
- 马 (Horse): Workflow optimization
- 羊 (Goat): LoRA weight tuning
- 猴 (Monkey): Parameter optimization
```

---

### Version Management Best Practices:
```
1. ALWAYS commit to Git before releasing version
2. ALWAYS test workflow BEFORE marking as stable
3. ALWAYS include release notes (even for PATCH versions)
4. ALWAYS backup before rollback
5. ALWAYS use semantic versioning (MAJOR.MINOR.PATCH)
6. NEVER release without code review (鸡 (Rooster) approval)
7. NEVER skip version numbers (always increment sequentially)
8. NEVER modify released versions (create new version instead)
```

### Version Management Workflow:
```
1. Develop → 2. Test → 3. Commit to Git → 4. Release Version → 5. Mark Stable → 6. Deploy
```
**Execution Rules (NEW in v4.0)**:
36. **ALWAYS use version control** — Git + ComfyUI workflow versioning
37. **ALWAYS compare versions before releasing** — generate diff report
38. **ALWAYS backup before rollback** — prevent accidental data loss
39. **ALWAYS include release notes** — document changes for users
40. **ALWAYS test before marking stable** — ensure quality threshold met
```python
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
```

### Interrupt Generation:
```python
def interrupt_generation(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str
):
    """Interrupt ComfyUI generation process"""
    # ... (代码已精简，保留核心逻辑) ...
    
    # Check for keyboard interrupt (if running interactively)
    # (This would be handled by signal handler in real implementation)
    
    return False
```
```python
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
```

### Feedback Loop (Generate → Assess → Adjust → Regenerate):
```python
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
```
25. **ALWAYS monitor generation progress** — use `monitor_generation_progress()` for long generations
26. **ALWAYS support interruption** — check for user interruption every 2 seconds
27. **ALWAYS adjust parameters dynamically** — analyze intermediate results every 5 steps
28. **ALWAYS use feedback loop** — iterate until quality threshold met (max 3 iterations)
| Modality | Format | Purpose | Example |
|----------|--------|---------|---------|
| **Text** | String | Main prompt / instruction | "Generate a vacuum cup with titanium body" |
| **Image** | URL / Base64 / File Path | Reference image / style guide | "@/path/to/reference.jpg" |
| **Image + Text** | JSON | Joint input (image + prompt) | `{"image": "...", "prompt": "..."}` |
| **Batch** | JSON Array | Multiple inputs (batch processing) | `[{"image": "..."}, {"prompt": "..."}]` |
  ... (省略中间部分) ...
      "preprocessing": "resize(512x512)+normalize",  // Optional
      "weight": 0.7  // Importance of image (0.0~1.0)
    }
  },
  "options": {
    "combine_method": "concat",  // "concat" | "weighted_sum" | "cross_attention"
    "output_format": "json",  // "json" | "markdown" | "image"
    "quality_threshold": 7.0  // Minimum quality score (0-10)
  }
}
```

### Image Processing Flow (using vision-ai skill):
```
def process_image_input(image_source, image_type="reference"):
    """Process image input using vision-ai skill"""
    
    # 1. Load image (from URL / Base64 / File Path)
    if image_source.startswith("http"):
        image = download_image(image_source)
    elif image_source.startswith("data:image"):
        image = decode_base64(image_source)
    else:
        image = load_local_image(image_source)
    
    # 2. Preprocess image (resize / normalize / enhance)
    image = preprocess_image(
        image,
        target_size=(512, 512),
        normalize=True,
        enhance_contrast=True
    )
    
    # 3. Extract image features (using vision-ai)
    features = extract_image_features(
        image,
        model="clip-vit-large",  // Or "resnet50" / "vgg16"
        layers="last_hidden_state"
    )
    
    # 4. Generate image description (for prompt enhancement)
    description = generate_image_description(
        image,
        prompt="Describe this product image in detail, focusing on material, shape, color, and texture."
    )
    
要点：
- return {
- "image": image,
- "features": features,
- "description": description,
- "metadata": {
- "source": image_source,
- "type": image_type,
- "size": image.size,
- "mode": image.mode
- }
- }
```
```
def build_joint_prompt(text_input, image_input, combine_method="concat"):
    """Build joint prompt from text + image"""
    text_prompt = text_input.get("prompt", "")
    negative_prompt = text_input.get("negative_prompt", "")
    image_description = ""
    if image_input:
        image_data = process_image_input(
            image_input["source"],
            image_input.get("type", "reference")
  ... (省略中间部分) ...
        joint_prompt = {
            "text_features": extract_text_features(text_prompt),
            "image_features": extract_image_features(image_data["image"]),
            "fusion_method": "cross_attention"
        }
    final_prompt = {
        "prompt": joint_prompt,
        "negative_prompt": negative_prompt
    }
    return final_prompt
```

### Multi-modal Quality Assessment:
```
def assess_multimodal_quality(
    generated_image,
    text_input,
    image_input,
    quality_threshold=7.0
):
    """Assess quality of generated image (combined text + image)"""
    
    # 1. Image similarity (generated vs. reference image)
    if image_input:
        image_similarity = calculate_image_similarity(
            generated_image,
            image_input["source"],
            method="clip"  // Or "ssim" / "lpips"
        )
    else:
        image_similarity = 1.0  // No image input, skip
    
    # 2. Text matching (generated image vs. text prompt)
    text_matching = calculate_text_image_matching(
        generated_image,
        text_input.get("prompt", ""),
        method="clip"  // Or "blip" / "git"
    )
    
    # 3. Combined quality score (weighted average)
    quality_score = (
        0.4 * image_similarity +  // 40% weight to image similarity
        0.6 * text_matching     // 60% weight to text matching
    )
    
    # 4. Check if meets threshold
    if quality_score >= quality_threshold:
        status = "success"
        reason = f"Quality score {quality_score:.2f} >= threshold {quality_threshold}"
    else:
        status = "failed"
        reason = f"Quality score {quality_score:.2f} < threshold {quality_threshold}"
    
要点：
- return {
- "status": status,
- "quality_score": quality_score,
- "image_similarity": image_similarity,
- "text_matching": text_matching,
- "reason": reason,
- "details": {
- "image_similarity_method": "clip",
- "text_matching_method": "clip",
- "quality_threshold": quality_threshold
- }
- }
```
```
{
  "modality": "image+text",
  "inputs": {
    "text": {
      "prompt": "Generate a vacuum cup with titanium body, brushed finish, and pop-up lid",
      "negative_prompt": "plastic texture, asymmetric lid, low quality"
    },
    "image": {
      "source": "@/reference/cup_design.jpg",
  ... (省略中间部分) ...
      "preprocessing": "resize(512x512)+normalize",
      "weight": 0.7
    }
  },
  "options": {
    "combine_method": "concat",
    "output_format": "json",
    "quality_threshold": 7.0
  }
}

### Execution Rules (NEW in v3.7):
21. **ALWAYS support multi-modal input** — accept text/image/image+text/batch inputs
22. **ALWAYS preprocess images** — resize to 512x512, normalize, enhance contrast
23. **ALWAYS extract image features** — use vision-ai skill (CLIP/ResNet)
24. **ALWAYS assess multi-modal quality** — combine image similarity + text matching

---

---
## Phase 4.5: Version Management Enhancement (NEW in v4.0)

### A. Version Management Strategy
- **Git Integration**: All ComfyUI workflows stored in Git repository
- **Workflow Versioning**: Each workflow JSON has version field
- **Semantic Versioning**: MAJOR.MINOR.PATCH (e.g., 2.1.3)
- **Branch Strategy**: main (stable), dev (testing), feat/* (new features)

### B. Version Comparison Mechanism
```python
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
```

### C. Version Rollback
```python
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
```

### D. Version Release
```python
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
```

### E. Version Management Best Practices
1. **Commit Message Format**: `[WorkflowName] v2.1.3 - Description`
2. **Tag Naming**: `v2.1.3-workflow-name`
3. **Rollback Policy**: Keep last 3 stable versions
4. **Testing**: Always test before release
5. **Documentation**: Update CHANGELOG.md for each release

---

---



---

## Prompt Library: by_material

| 材质 | 正面提示词 | 负面提示词 |
|------|--------------|--------------|
| 不锈钢 | stainless steel brushed texture, directional brushed grain, metallic reflection anisotropic... | plastic texture, rough surface... |
| 钛金属 | titanium raw finish, anisotropic reflection, physical based rendering... | plastic texture, aluminum look... |
| 镁合金 | magnesium alloy AE44, powder-coated finish, lightweight metal (35% lighter than aluminum)... | plastic texture, raw metal exposed... |
| 塑料 | BPA-free plastic, matte plastic texture, smooth plastic surface... | cheap plastic look, glossy plastic (fingerprint magnet)... |
| 玻璃 | borosilicate glass, heat-resistant glass, transparent glass... | plastic imitation glass, bubbles in glass... |
| 陶瓷 | ceramic glaze, smooth ceramic surface, even ceramic coating... | chipped ceramic, uneven glaze... |

**完整提示词见** `prompt_library.json`


---

## Prompt Library: defect_prevention

| 缺陷类型 | 严重程度 | 正面提示词 | 权重 |
|----------|----------|--------------|------|
| 防塑料感 | HIGH | anisotropic reflection, physical based rendering, metallic workflow, subsurface scattering (if applicable) | 1.5 |
| 防不对称杯盖 | HIGH | perfectly symmetric lid, matches cup body diameter, continuous seam | 1.5 |
| 防颜色偏差 | MEDIUM | color accurate, Delta E < 3 vs Pantone, consistent coloring | 1.4 |
| 防文本/Logo伪影 | MEDIUM | no text, no logo, clean surface | 1.3 |
| 防背景不匹配 | LOW | pure white background (for e-commerce), consistent lighting (for lifestyle) | 1.2 |
| 防变形手柄 | HIGH | perfectly symmetric handle, ergonomic shape, sturdy attachment | 1.4 |

**完整提示词见** `prompt_library.json`


---

## Phase 5.0: Memory Compression & Performance Optimization (OPTIMIZED in v5.0)

### A. 显存管理策略（优化版 - v5.0）

```python
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
```

### B. 奖励机制（NEW in v5.0）

**核心思想**：当生成质量优秀时，奖励更多显存/更大batch size，加快后续生成速度。

```python
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
```

### C. 显存碎片化整理机制（NEW in v5.0）

**问题**：长时间运行后，显存会出现碎片化（小块空闲显存无法被大tensor使用）。

**解决方案**：定期整理显存碎片。

```python
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
```

**触发条件**（满足任一即触发）：
- 显存碎片化 > 30%
- 连续生成 > 20 张图像后
- 检测到 OOM 错误后
- 用户手动调用 `/vram_defrag` 命令

### D. 多模型并行加载的显存调度策略（NEW in v5.0）

**场景**：需要同时加载 Checkpoint + 多个 LoRA + 多个 ControlNet。

**策略**：按需加载 + 优先级调度。

```python
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
```

### E. 性能监控（优化版 - v5.0）

```python
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
```


---

## Phase 1.2: Image Quality Assessment Metrics (NEW in v5.0)

**Complete image quality assessment framework**:

```markdown
### 1. Quantitative Metrics:
| Metric | Formula | Reference Standard | Score Range |
|--------|-----------|-------------------|-------------|
| Clarity (IQA) | BRISQUE algorithm | < 30 (good) | 0-100 |
| Color Richness | HSV color histogram | > 0.7 (rich) | 0-1 |
| Composition | Rule of thirds | 0.8-1.0 (perfect) | 0-1 |

### 2. Quantitative Analysis Method (Python Code):
```python
import cv2
import numpy as np
from skimage import metrics

def assess_image_quality(image_path):
    """Assess image quality using multiple metrics"""
    img = cv2.imread(image_path)
    # Implementation here
    pass
```

### 3. Defect Detection Checklist:
- [ ] Structural defects (asymmetry, deformation)
- [ ] Material defects (plastic texture, inconsistent brushed)
- [ ] Lighting defects (wrong reflection, inconsistent shadow)
- [ ] Text/logo defects (garbled, deformed)
- [ ] Background defects (mismatch, clutter)
```

**Output**: Image Quality Analysis Report (JSON/Markdown format)


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


## Usage Examples

### Example 1: Basic Usage

```bash
python scripts/example.py
```

### Example 2: Advanced Usage

```python
from src.main import MainClass

obj = MainClass()
result = obj.run()
```
