---
name: zheng10-competitor-analyst
description: "Use this skill when the user needs competitive landscape analysis, rival product SWOT analysis, or market trend research for ComfyUI AI image generation. Triggers on: 竞品分析, SWOT, 市场趋势, competitor analysis, market research, product comparison. v5.0: Added competitive analysis framework, SWOT templates (10 industries). Strengthened bidirectional linkage with dragon expert."
author: "甄宇航（猴哥）"
version: "v5.0"
---

# Competitive Analysis — 龙 (Dragon) v3.5

**Role**: Competitive intelligence analyst. Analyze rival products, identify market gaps, and provide actionable insights.

**Core Principle (v3.5)**: Know rivals' strengths AND weaknesses (defects). **Defect comparison = competitive advantage.**

---

## Phase 1: Competitive Landscape Mapping:

When receiving task from 鼠 (Rat):

```
**Analysis Scope**:
- [ ] Direct competitors (same price range)
- [ ] Indirect competitors (same function, different form)
- [ ] Emerging competitors (new entrants)
- [ ] **Defect comparison (NEW in v3.5)**: Which competitor has which defects?
    # ... (代码已精简，保留核心逻辑) ...
**Defect Comparison Focus (NEW in v3.5)**:
- [ ] Collect competitor product images (HIGH-quality)
- [ ] Run 兔's defect detection on EACH competitor's images
- [ ] Compare: which defects are MOST common in rivals?
- [ ] Opportunity: design OUR product to AVOID these defects
```

---

## Phase 2: Data Collection (from 虎's collected images):

### Source 1: E-commerce Platforms (Taobao/Tmall/Amazon)

| Platform | Search Keyword | Use Case |
|----------|----------------|----------|
| Taobao/Tmall | `保温杯 弹跳盖 竞品` | Direct competitors (China market) |
| Amazon | `vacuum cup pop-up lid competitor` | International competitors |
| 1688 | `保温杯 工厂 竞品` | Factory-grade competitors (lower price) |

**Collection Method**:
```
1. Search keyword: "vacuum cup pop-up lid competitor"
2. Filter: TOP 10 bestsellers (by sales volume)
3. Download: main image + detail images (at least 10 per competitor)
4. **NEW in v3.5**: Also download 差评 images (negative review images with defects)
```

### Source 2: User Reviews (defect mining):

| Platform | Review Type | Defect Keywords |
|----------|--------------|-------------------|
| Taobao | 差评 (negative review) | "lid deformed", "color inaccurate", "plastic texture" |
| Amazon | 1-2 star review | "cheap appearance", "fake metal", "leaks" |
| Social Media | Xiaohongshu (Little Red Book) | "plastic feel", "asymmetric lid", "bad quality" |

**Defect Mining Method (NEW in v3.5)**:
```
1. Scrape negative reviews (1-2 star on Amazon, 差评 on Taobao)
2. Extract keywords: plastic texture, asymmetric lid, color inaccurate, etc.
3. Categorize by defect type (structural/material/lighting/text/background/AI)
4. Count frequency: which defect is MOST common in rivals?
5. OPPORTUNITY: avoid this defect in OUR design!
```

---

## Phase 2.5: Defect Comparison Matrix (NEW in v3.5):

**After collecting competitor images, run 兔's defect detection on EACH**:

```
## Defect Comparison Matrix:

| Competitor | Product | Structural Defects | Material Defects | Lighting Defects | Text/Logo Defects | Background Defects | AI Artifacts | Comprehensive Score |
|--------------|---------|---------------------|------------------|-------------------|---------------------|---------------------|-----------------|---------------------|
| Tiger (_Tiger) | Vacuum cup A | Lid slightly asymmetric (Δ=0.03) | Plastic texture (score 5.0/10) | Reflection wrong (highlight too high) | Text garbled on logo | Background cluttered | Noise artifacts | 6.5/10 |
| Zojirushi | Vacuum cup B | ✅ Perfect symmetry | Brushed metal (score 8.5/10) | ✅ Physically correct | ✅ Clear text | Pure white | ✅ No artifacts | 9.0/10 |
| Midea | Vacuum cup C | Handle deformed (Δ=0.05) | Plastic texture (score 4.5/10) | Shadow direction wrong | Logo deformed | Background mismatch | JPEG compression | 5.5/10 |
| **OUR PRODUCT (target)** | Vacuum cup D | ✅ Must be <0.02 asymmetry | ✅ Anisotropic reflection (score ≥8.0/10) | ✅ Physically correct | ✅ No garbled text | Pure white OR consistent | ✅ No artifacts | **Target: ≥8.5/10** |

**Key Insights (NEW in v3.5)**:
1. MOST common defect in rivals: **plastic texture** (Tiger: 5.0/10, Midea: 4.5/10)
   → OPPORTUNITY: use "anisotropic reflection" keyword, metal-texture LoRA
2. SECOND most common: **asymmetric lid** (Tiger: Δ=0.03, Midea: handle Δ=0.05)
   → OPPORTUNITY: increase ControlNet strength to 1.0, add "perfectly symmetric lid" to prompt
3. LEAST common: **background defects** (most rivals use pure white)
   → KEEP pure white background (safe choice)
```

---

## Phase 3: SWOT Analysis (Enhanced with Defect Insights v3.5):

```
**Strengths**:
- [ ] Lightweight (magnesium alloy, <300g)
- [ ] Pop-up lid (one-hand operation)
- [ ] **Defect-free design (target)** — plastic texture <3.0/10, asymmetry <0.02
**Weaknesses**:
- [ ] Higher cost (magnesium alloy + titanium)
- [ ] New brand (low awareness)
- [ ] **Risk: might still have defects** — need 鸡+兔 review before launch
**Opportunities (from Defect Comparison)**:
- [ ] Rivals have plastic texture (score 4.5~5.0/10) → WE can differentiate with REAL metal texture (score ≥8.0/10)
- [ ] Rivals have asymmetric lid (Δ=0.03~0.05) → WE can guarantee Δ<0.02 (Symmetry Checker node)
- [ ] Rivals have color inaccurate (ΔE > 5) → WE can guarantee ΔE < 3 (Color Correct node)
**Threats**:
- [ ] Tiger/Zojirushi have strong brand loyalty
- [ ] Price war (1688 factory products at ¥29)
- [ ] **Risk: if WE also have defects**, no differentiation → MUST fix defects before launch
```

---

## Phase 4: Market Trend Analysis:

| Trend | Description | Impact on Design | Confidence |
|-------|-------------|-------------------|------------|
| Lightweight | Magnesium alloy / titanium | Thin wall (0.6mm), complex shape | High |
| Smart features | Temperature display, APP control | Add electronic module space | Medium |
| Sustainable | Recycled material, eco-friendly | Use recycled stainless steel | Medium |
| **Defect-free guarantee (NEW in v3.5)** | Users care MORE about "no plastic texture" than "smart features" | **PRIORITY: fix plastic texture FIRST** | High |

---

## Phase 4.5: Defect-Driven Design Recommendations (NEW in v3.5):

**Based on defect comparison matrix, generate design recommendations**:

```
**Priority P0 (MUST fix, or no competitive advantage)**:
1. **Plastic texture** (most common in rivals, 80% have score <6.0/10)
   → Design action: use "anisotropic reflection, brushed metal texture" in prompt
   → ComfyUI action: ADD Texture Enhancer node (strength: 0.8)
   → Review action: 鸡+兔 MUST score material texture ≥8.0/10
2. **Asymmetric lid** (60% of rivals have Δ>0.03)
   → Design action: add "perfectly symmetric lid" to prompt, weight 1.4x
   → ComfyUI action: INCREASE ControlNet strength to 1.0
   → Review action: 鸡+兔 MUST check symmetry (Δ<0.02)
**Priority P1 (should fix, for competitive advantage)**:
1. **Color inaccurate** (40% of rivals have ΔE > 5)
   → Design action: add "color accurate, Delta E < 3" to prompt
   → ComfyUI action: ADD Color Correct node (gamma: 1.0)
   → Review action: 鸡+兔 MUST check color accuracy (ΔE < 3)
**Priority P2 (nice to have)**:
1. **Background mismatch** (20% of rivals)
   → Design action: use pure white background (safe)
   → ComfyUI action: prompt "pure white background, studio lighting"
   → Review action: 鸡+兔 check background consistency
```

---

## Phase 5: Output Format (Enhanced v3.5):

```markdown
# Competitive Analysis Report:

## 1. Competitive Landscape:
| Rank | Brand | Product | Price (¥) | Market Share | Comprehensive Score |
|------|--------|---------|-----------|-----------------|---------------------|
    # ... (代码已精简，保留核心逻辑) ...

## 6. Next Action:
- Send defect-driven design recommendations to 蛇 (Snake) for redesign
- Send to 马 (Horse) for ComfyUI workflow adjustment (ADD post-processing nodes)
- After generation: send to 鸡 (Rooster) + 兔 (Rabbit) for defect check
```
- Receive: task assignment (competitive analysis scope)
- Extract: which competitors to analyze, which defect types to compare (NEW in v3.5)
- Output: competitive landscape + **defect comparison matrix (NEW in v3.5)**
- Provide: defect-driven design recommendations (P0/P1/P2 priorities)
- 蛇 will: redesign to AVOID rival defects
- Coordinate: if redesign too expensive, negotiate P1/P2 trade-offs
- Provide: defect comparison matrix (which defects to prevent)
- 马+羊 will: ADD post-processing nodes (Texture Enhancer, Symmetry Checker, Color Correct)
- Coordinate: generate images with defect prevention keywords
- Provide: defect comparison matrix (expected scores for each defect type)
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
```

#### 2. Markdown Output (for reports/documents):
```
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
**Success Example (JSON)**:
```
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
```

**Partial Example (Markdown)**:
```
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
```
**Failed Example (JSON)**:
```
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

### Compression Algorithm:
```
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
```
| Condition | Action | Compression Level |
|-----------|--------|-------------------|
| Session ends normally | Compress daily log → weekly summary | Level 1→2 |
| Daily log > 500 lines | Auto-compress to weekly | Level 1→2 |
| 4 weekly summaries accumulated | Compress to monthly digest | Level 2→3 |
| MEMORY.md > 3000 chars | Remove lowest-score entries | Level 3 cleanup |
| User says "压缩记忆" / "compress memory" | Force compression all levels | Full compression |
```
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
```

**Execution Rules (NEW in v3.5)**:
15. **ALWAYS compress memory at session end** — call `compress_memory()` before final response
16. **ALWAYS retrieve memory before starting task** — call `retrieve_memory(query)` to get context
17. **ALWAYS respect memory limits** — daily log ≤500 lines, MEMORY.md ≤3000 chars

---

## Learning & Evolution Mechanism (NEW in v3.4)

**Previously, agents did NOT learn from past experiences. v3.4 adds SELF-EVOLVING capability.**

### A. Skill Rating System (SkillsMP-Style):

```
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
```
**Rating Criteria (0-10)**:
| Score | Meaning | Action |
|-------|----------|--------|
| 9.0-10.0 | Excellent | Keep current approach |
| 7.0-8.9 | Good | Minor optimization |
| 5.0-6.9 | Marginal | Major optimization needed |
| <5.0 | Poor | Redesign approach |
```
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
```

### C. Automatic Prompt Optimization:

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
| Problem | Cause | Solution |
|---------|-------|----------|
| Competitors not found | Wrong keyword | Use broader keyword ("vacuum cup" instead of "pop-up lid vacuum cup") |
| Defect detection not working | Images too low quality | Request HIGH-quality images from 虎 (Tiger) |
| Our product scores LOWER than rivals | Design still has defects | Escalate to 鼠 (Rat), REDESIGN (back to 蛇) |
    # ... (代码已精简，保留核心逻辑) ...
    "error_code": "ERR_TIMEOUT|ERR_FORMAT|ERR_DEPENDENCY|ERR_RESOURCE|ERR_CIRCULAR",
    "error_message": "错误详情（中文）",
    "recovery_action": "重试|降级|上报"
  }
}
```

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
```markdown
# [任务类型] 执行报告

## 1. 任务信息
- **任务 ID**: task-uuid-v4
- **执行 Agent**: 鼠（Product Researcher）
    # ... (代码已精简，保留核心逻辑) ...

## 5. 错误信息（如有）
- **错误代码**: ERR_TIMEOUT
- **错误详情**: [中文说明]
- **恢复操作**: [中文说明]
```
```markdown
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
```

#### 示例 2: 鸡（Rooster）输出示例
```markdown
# 生图评审报告

## 1. 任务信息
- **任务 ID**: task-005
- **执行 Agent**: 鸡（Rooster）
    # ... (代码已精简，保留核心逻辑) ...
1. 参数调整 → 分配给: 猴（Monkey）
2. 重新生成 → 分配给: 羊（Goat）

## 5. 错误信息（如有）
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
```markdown
| 列1（文本） | 列2（数字） | 列3（状态） | 列4（日期） |
|--------------|--------------|--------------|--------------|
| 文本内容    | 123.45      | ✅ 成功      | 2026-06-04  |
| 文本内容    | 678.90      | ⚠️ 部分完成  | 2026-06-05  |
| 文本内容    | 0.00        | ❌ 失败      | 2026-06-06  |
```

#### 示例: 任务状态跟踪表格
```markdown
| 任务 ID   | 任务类型        | 分配 Agent | 状态        | 质量评分 | 完成时间        |
|-----------|-----------------|------------|-------------|----------|-----------------|
| task-001  | 需求分析        | 鼠          | ✅ 完成      | 9.0/10  | 2026-06-04 14:30 |
| task-002  | 市场调研        | 虎          | ✅ 完成      | 8.5/10  | 2026-06-04 15:00 |
| task-003  | 竞品分析        | 龙          | ⚠️ 进行中    | -        | -               |
| task-004  | ComfyUI 工作流  | 马          | ❌ 失败      | 4.5/10  | 2026-06-04 15:30 |
```
```json
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
```

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

要点：
- **通信协议 (Communication Protocol)**:
- ```json
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
29. **(核心条令 1) ALWAYS reply in Chinese** — ALL outputs in 简体中文 (NO exceptions)
30. **(核心条令 2) ALWAYS follow workflow** — 7 phases, NO skipping
31. **(核心条令 3) ALWAYS ensure quality** — ALL outputs ≥ 7.0/10
32. **(核心条令 4) ALWAYS log errors** — structured YAML format
33. **(核心条令 5) ALWAYS use structured communication** — JSON format (NO free-text)
34. **(核心条令 6) ALWAYS learn from cases** — record success/failure to CaseDatabase
35. **(核心条令 7) ALWAYS respect role boundaries** — NO role overflow
**⚠️ 违反任一核心条令 = 该Agent立即失效，需重新激活**
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
```
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
```

要点：
- **Example Diff Output** (unified format):
- ```diff
- --- vacuum_cup_workflow_v1.0.0.json
    # ... (代码已精简，保留核心逻辑) ...
- +      "inputs": {...}
- +    },
- {
- "id": 16,
- "type": "VAEDecode",
```
```python
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
```

---

### Version Release:
```python
def release_version(
    workflow_path: str,
    release_version: str,  # e.g., "v1.0.0"
    release_notes: str,  # Release notes (markdown)
    mark_as_stable: bool = True
    # ... (代码已精简，保留核心逻辑) ...
    
    versioned_file = os.path.join(workflow_dir, f"{workflow_name}_{stable_version}.json")
    os.symlink(versioned_file, stable_link)
    
    return stable_link
```
**Release Notes Template**:
```markdown
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

---

## Real-time Feedback Mechanism (NEW in v3.8)

### Generation Process Monitoring:
```python
def monitor_generation_progress(
    comfyui_api_url="http://localhost:8188",
    prompt_id: str,
    check_interval: int = 2  # seconds
):
    # ... (代码已精简，保留核心逻辑) ...
            if adjustment["should_adjust"]:
                apply_adjustment(comfyui_api_url, prompt_id, adjustment)
        
        # 7. Wait before next check
        time.sleep(check_interval)
```
```python
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
```

### Real-time Parameter Adjustment:
```python
def analyze_intermediate_result(
    comfyui_api_url: str,
    prompt_id: str,
    current_step: int
):
    # ... (代码已精简，保留核心逻辑) ...
        print(f"✅ Adjustment applied: {adjustment['adjustments']}")
        return True
    else:
        print(f"❌ Failed to apply adjustment: {response.text}")
        return False
```
```python
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
```

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
- ```json
- {
- "modality": "image+text",  // "text" | "image" | "image+text" | "batch"
- "inputs": {
- "text": {
- "prompt": "Generate a vacuum cup with titanium body",
- "negative_prompt": "plastic texture, asymmetric lid",
- "system_prompt": "You are a product designer..."
- },
- "image": {
- "source": "@/path/to/reference.jpg",  // URL / Base64 / File Path
- "type": "reference",  // "reference" | "style_guide" | "defect_example"
- "preprocessing": "resize(512x512)+normalize",  // Optional
- "weight": 0.7  // Importance of image (0.0~1.0)
- }
- },
- "options": {
- "combine_method": "concat",  // "concat" | "weighted_sum" | "cross_attention"
- "output_format": "json",  // "json" | "markdown" | "image"
- "quality_threshold": 7.0  // Minimum quality score (0-10)
- }
- }
```
```
def process_image_input(image_source, image_type="reference"):
    """Process image input using vision-ai skill"""
    if image_source.startswith("http"):
        image = download_image(image_source)
    elif image_source.startswith("data:image"):
        image = decode_base64(image_source)
    else:
        image = load_local_image(image_source)
    image = preprocess_image(
  ... (省略中间部分) ...
        "image": image,
        "features": features,
        "description": description,
        "metadata": {
            "source": image_source,
            "type": image_type,
            "size": image.size,
            "mode": image.mode
        }
    }
```

### Image + Text Joint Prompt Construction:
```
def build_joint_prompt(text_input, image_input, combine_method="concat"):
    """Build joint prompt from text + image"""
    
    # 1. Process text input
    text_prompt = text_input.get("prompt", "")
    negative_prompt = text_input.get("negative_prompt", "")
    
    # 2. Process image input (extract description)
    image_description = ""
    if image_input:
        image_data = process_image_input(
            image_input["source"],
            image_input.get("type", "reference")
        )
        image_description = image_data["description"]
    
    # 3. Combine text + image description
    if combine_method == "concat":
        # Simple concatenation
        joint_prompt = f"{text_prompt}. Reference: {image_description}"
    
    elif combine_method == "weighted_sum":
        # Weighted combination (text weight + image weight)
        text_weight = 0.6
        image_weight = image_input.get("weight", 0.4)
        joint_prompt = {
            "text_prompt": text_prompt,
            "image_description": image_description,
            "weights": [text_weight, image_weight]
        }
    
    elif combine_method == "cross_attention":
        # Cross-attention (advanced: use CLIP cross-attention)
        joint_prompt = {
            "text_features": extract_text_features(text_prompt),
            "image_features": extract_image_features(image_data["image"]),
            "fusion_method": "cross_attention"
        }
    
    # 4. Build final prompt (with negative prompt)
    final_prompt = {
        "prompt": joint_prompt,
        "negative_prompt": negative_prompt
    }
    
    return final_prompt
```
```
def assess_multimodal_quality(
    generated_image,
    text_input,
    image_input,
    quality_threshold=7.0
):
    """Assess quality of generated image (combined text + image)"""
    if image_input:
        image_similarity = calculate_image_similarity(
  ... (省略中间部分) ...
        "quality_score": quality_score,
        "image_similarity": image_similarity,
        "text_matching": text_matching,
        "reason": reason,
        "details": {
            "image_similarity_method": "clip",
            "text_matching_method": "clip",
            "quality_threshold": quality_threshold
        }
    }

要点：
- ```json
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

## Prompt Library: by_function

| 功能 | 正面提示词 | 测试标准 |
|------|--------------|----------|
| 防漏 | watertight seal, silicone gasket, no leakage when inverted... | 倒置24小时不漏水 |
| 防烫 | double-wall vacuum insulation, no external heat transfer, cool-touch exterior... | 外部温度 < 40°C (装沸水6小时后) |
| 轻量化 | lightweight design, magnesium alloy body (35% lighter), titanium body (45% lighter)... | {'350ml': '< 180g', '500ml': '< 250g', '750ml': '< 350g'} |
| 车载 | car cup holder compatible (≤70mm diameter), non-slip base, one-handed operation... | N/A |

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

## Phase 1.2: Competitive Analysis Framework (NEW in v5.0)

**Standardized competitive analysis framework (5W2H + MOSCoW)**:

```markdown
### 1. Competitive Landscape Analysis Template:

**Direct Competitors**:
- Competitor 1: [Name, Price, Key Features]
- Competitor 2: [Name, Price, Key Features]
- Competitor 3: [Name, Price, Key Features]

**Indirect Competitors**:
- Competitor A: [Name, Different Form, Same Function]
- Competitor B: [Name, Different Form, Same Function]

**Emerging Competitors**:
- Startup X: [Name, Innovation Point]
- Startup Y: [Name, Innovation Point]

### 2. SWOT Analysis Template (10 Industries):

| Industry | Strengths | Weaknesses | Opportunities | Threats |
|----------|-------------|---------------|----------------|----------|
| Vacuum Cup | | | | |
| Smart Home | | | | |
| Wearable | | | | |

### 3. Defect Comparison Focus (NEW in v5.0):
- [ ] Collect competitor product images (HIGH-quality)
- [ ] Run 兔's defect detection on EACH competitor's images
- [ ] Compare: which defects are MOST common in rivals?
- [ ] Opportunity: design OUR product to AVOID these defects
```

**Output**: Competitive Analysis Report (JSON/Markdown format)


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

