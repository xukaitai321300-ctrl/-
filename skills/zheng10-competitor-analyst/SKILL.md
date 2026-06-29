---
name: zheng10-competitor-analyst
description: "auto-generated: skill package 'zheng10-competitor-analyst' (awaiting human review)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "新增Phase 6: 竞品数据自动采集与联动优化"
  upgrade_date: "2026-06-19"
  tags: ["competitor-analysis", "data-collection", "market-research", "agent-collaboration"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# Competitive Analysis — 龙 (Dragon) v7.0

**Role**: Competitive intelligence analyst. Analyze rival products, identify market gaps, and provide actionable insights.

**Core Principle (v3.5)**: Know rivals' strengths AND weaknesses (defects). **Defect comparison = competitive advantage.**

---

## Phase 1: Competitive Landscape Mapping:

When receiving task from 鼠 (Rat):

> 📄 代码已提取到 `references\code_01.txt`（12 行，547 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: Data Collection (from 虎's collected images):

### Source 1: E-commerce Platforms (Taobao/Tmall/Amazon)

| Platform | Search Keyword | Use Case |
|----------|----------------|----------|
| Taobao/Tmall | `保温杯 弹跳盖 竞品` | Direct competitors (China market) |
| Amazon | `vacuum cup pop-up lid competitor` | International competitors |
| 1688 | `保温杯 工厂 竞品` | Factory-grade competitors (lower price) |

**Collection Method**:
> 📄 代码已提取到 `references\code_02.txt`（5 行，253 字节）
> 需要查看完整代码时请读取该文件。



### Source 2: User Reviews (defect mining):

| Platform | Review Type | Defect Keywords |
|----------|--------------|-------------------|
| Taobao | 差评 (negative review) | "lid deformed", "color inaccurate", "plastic texture" |
| Amazon | 1-2 star review | "cheap appearance", "fake metal", "leaks" |
| Social Media | Xiaohongshu (Little Red Book) | "plastic feel", "asymmetric lid", "bad quality" |

**Defect Mining Method (NEW in v3.5)**:
> 📄 代码已提取到 `references\code_03.txt`（6 行，326 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.5: Defect Comparison Matrix (NEW in v3.5):

**After collecting competitor images, run 兔's defect detection on EACH**:

> 📄 代码已提取到 `references\code_04.txt`（17 行，1619 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3: SWOT Analysis (Enhanced with Defect Insights v3.5):

> 📄 代码已提取到 `references\code_05.txt`（17 行，894 字节）
> 需要查看完整代码时请读取该文件。



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

> [引用] 完整代码已提取到 `references\code_block_06.txt`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_06.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 5: Output Format (Enhanced v3.5):

> 📄 代码已提取到 `references\code_07.txt`（12 行，486 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_08.txt`（3 行，50 字节）
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
> 📄 代码已提取到 `references\code_09.txt`（15 行，449 字节）
> 需要查看完整代码时请读取该文件。


Output Quality Checklist (ALL agents MUST verify):

[ ] Format matches template (JSON/Markdown/Table)
[ ] All required fields present (timestamp/agent_id/task_id/status)
[ ] No hallucinated data (check numbers/references)
[ ] Consistent terminology (use agreed terms, not synonyms)
[ ] Proper encoding (UTF-8, no mojibake)
[ ] Readable (proper line breaks, indentation)
> 📄 代码已提取到 `references\code_10.txt`（2 行，28 字节）
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
> 📄 代码已提取到 `references\code_11.txt`（3 行，33 字节）
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
> 📄 代码已提取到 `references\code_12.txt`（2 行，27 字节）
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
> 📄 代码已提取到 `references\code_13.txt`（12 行，351 字节）
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
> 📄 代码已提取到 `references\code_14.txt`（3 行，28 字节）
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
> 📄 代码已提取到 `references\code_15.txt`（8 行，468 字节）
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
> 📄 代码已提取到 `references\code_16.txt`（15 行，511 字节）
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
> 📄 代码已提取到 `references\code_17.txt`（8 行，263 字节）
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
> 📄 代码已提取到 `references\code_18.txt`（4 行，40 字节）
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
> 📄 代码已提取到 `references\code_19.txt`（13 行，508 字节）
> 需要查看完整代码时请读取该文件。


Task Execution -> Quality Assessment -> Case Recording -> 
Pattern Extraction -> Prompt/Parameter Optimization -> Next Task (improved)
> 📄 代码已提取到 `references\code_20.txt`（12 行，578 字节）
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
> 📄 代码已提取到 `references\code_21.txt`（12 行，197 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_22.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_22.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




#### 示例 2: 鸡（Rooster）输出示例
> 📄 代码已提取到 `references\code_23.txt`（12 行，175 字节）
> 需要查看完整代码时请读取该文件。



---

### C. 表格输出模板（标准化格式）

#### 通用规则:
1. **表格标题**: 必须中文，简洁明了
2. **表格列宽**: 根据内容自动调整，保持对齐
3. **表格对齐**: 数字右对齐，文本左对齐，表头居中
4. **表格分隔线**: 使用 `|-----|------|-----|` 格式

#### 标准化表格模板:
> 📄 代码已提取到 `references\code_24.txt`（6 行，255 字节）
> 需要查看完整代码时请读取该文件。



#### 示例: 任务状态跟踪表格
> 📄 代码已提取到 `references\code_25.txt`（7 行，487 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_26.json`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_26.txt`（2 行，36 字节）
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
> 📄 代码已提取到 `references\code_27.txt`（6 行，222 字节）
> 需要查看完整代码时请读取该文件。



**示例 (Correct vs. Wrong)**:
> 📄 代码已提取到 `references\code_28.txt`（6 行，111 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 2: 必须遵循工作流程 (MANDATORY Workflow Compliance)
> 📄 代码已提取到 `references\code_29.txt`（6 行，219 字节）
> 需要查看完整代码时请读取该文件。



**工作流程 (7 Phases)**:
> 📄 代码已提取到 `references\code_30.txt`（8 行，169 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 3: 必须保证质量 (MANDATORY Quality Assurance)
> 📄 代码已提取到 `references\code_31.txt`（6 行，246 字节）
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
> 📄 代码已提取到 `references\code_32.txt`（6 行，259 字节）
> 需要查看完整代码时请读取该文件。



**错误日志格式 (Error Log Format)**:
> 📄 代码已提取到 `references\code_33.yaml`（8 行，238 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 5: 必须协作沟通 (MANDATORY Collaboration)
> 📄 代码已提取到 `references\code_34.txt`（6 行，299 字节）
> 需要查看完整代码时请读取该文件。



要点：
- **通信协议 (Communication Protocol)**:
- > 📄 代码已提取到 `references\code_35.json`（12 行，261 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 6: 必须持续学习 (MANDATORY Continuous Learning)
> 📄 代码已提取到 `references\code_36.txt`（6 行，300 字节）
> 需要查看完整代码时请读取该文件。



**学习循环 (Learning Loop)**:
> 📄 代码已提取到 `references\code_37.txt`（2 行，69 字节）
> 需要查看完整代码时请读取该文件。



---

### 条令 7: 必须尊重角色 (MANDATORY Role Respect)
> 📄 代码已提取到 `references\code_38.txt`（6 行，249 字节）
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
> 📄 代码已提取到 `references\code_39.txt`（5 行，208 字节）
> 需要查看完整代码时请读取该文件。


**Version Numbering Rules**:
- **MAJOR (X.0.0)**: Breaking changes (workflow structure changed, incompatible with old version)
- **MINOR (1.X.0)**: New features (added new nodes, improved quality)
- **PATCH (1.0.X)**: Bug fixes (fixed parameter typos, adjusted weights)
> 📄 代码已提取到 `references\code_40.txt`（17 行，447 字节）
> 需要查看完整代码时请读取该文件。



要点：
- **Example Diff Output** (unified format):
- > 📄 代码已提取到 `references\code_41.txt`（8 行，141 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_42.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_42.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




---

### Version Release:
> 📄 代码已提取到 `references\code_43.python`（12 行，369 字节）
> 需要查看完整代码时请读取该文件。


**Release Notes Template**:
> 📄 代码已提取到 `references\code_44.txt`（18 行，725 字节）
> 需要查看完整代码时请读取该文件。



---

### Version Management Best Practices:
> 📄 代码已提取到 `references\code_45.txt`（9 行，428 字节）
> 需要查看完整代码时请读取该文件。



### Version Management Workflow:
> 📄 代码已提取到 `references\code_46.txt`（2 行，90 字节）
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
> 📄 代码已提取到 `references\code_47.python`（12 行，366 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_48.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_48.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Real-time Parameter Adjustment:
> 📄 代码已提取到 `references\code_49.python`（12 行，316 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_50.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_50.txt`（2 行，38 字节）
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
- > [引用] 完整代码已提取到 `references\code_block_51.json`（22 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_51.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_52.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_52.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




### Image + Text Joint Prompt Construction:
> [引用] 完整代码已提取到 `references\code_block_53.txt`（47 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_53.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。



> [引用] 完整代码已提取到 `references\code_block_54.txt`（23 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_54.txt`（2 行，35 字节）
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
> [引用] 完整代码已提取到 `references\code_block_55.python`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_55.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### C. Version Rollback
> 📄 代码已提取到 `references\code_56.python`（16 行，507 字节）
> 需要查看完整代码时请读取该文件。



### D. Version Release
> [引用] 完整代码已提取到 `references\code_block_57.python`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_57.txt`（2 行，38 字节）
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

> [引用] 完整代码已提取到 `references\code_block_58.python`（38 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_58.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### B. 奖励机制（NEW in v5.0）

**核心思想**：当生成质量优秀时，奖励更多显存/更大batch size，加快后续生成速度。

> [引用] 完整代码已提取到 `references\code_block_59.python`（62 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_59.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### C. 显存碎片化整理机制（NEW in v5.0）

**问题**：长时间运行后，显存会出现碎片化（小块空闲显存无法被大tensor使用）。

**解决方案**：定期整理显存碎片。

> [引用] 完整代码已提取到 `references\code_block_60.python`（27 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_60.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




**触发条件**（满足任一即触发）：
- 显存碎片化 > 30%
- 连续生成 > 20 张图像后
- 检测到 OOM 错误后
- 用户手动调用 `/vram_defrag` 命令

### D. 多模型并行加载的显存调度策略（NEW in v5.0）

**场景**：需要同时加载 Checkpoint + 多个 LoRA + 多个 ControlNet。

**策略**：按需加载 + 优先级调度。

> [引用] 完整代码已提取到 `references\code_block_61.python`（58 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_61.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### E. 性能监控（优化版 - v5.0）

> [引用] 完整代码已提取到 `references\code_block_62.python`（35 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_62.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。





---

## Phase 1.2: Competitive Analysis Framework (NEW in v5.0)

**Standardized competitive analysis framework (5W2H + MOSCoW)**:

> [引用] 完整代码已提取到 `references\code_block_63.txt`（29 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_63.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




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


---

## Phase 2.7: Automated Competitive Metrics (NEW in v3.5)

**Objective**: Automatically score competitive analysis quality.

### Competitive Metrics:

> 📄 代码已提取到 `references\code_64.txt`（7 行，278 字节）
> 需要查看完整代码时请读取该文件。



### Python Implementation:

> 📄 代码已提取到 `references\code_65.python`（17 行，729 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.9: Comparative Defect Analysis (NEW in v3.5)

**Objective**: Compare defects across competitors to identify industry pain points.

### Defect Comparison Matrix:

> 📄 代码已提取到 `references\code_66.python`（16 行，514 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.11: Memory Compression (NEW in v3.5)

**Objective**: Compress competitive data to improve token efficiency.

### Compression Strategy:

1. **Competitor Data Compression**:
   - Store only key metrics (price, rating, top 3 defects)
   - Don't store full review text (too long)
   - Use summarized insights

2. **Token Budget**: 2000 tokens
   - Competitor summary: 800 tokens
   - Defect analysis: 600 tokens
   - Opportunity identification: 600 tokens


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

### 竞品图片分析的ComfyUI API调用

🐲 龙在竞品分析时，可调用ComfyUI API**增强竞品图片**：

```python
import requests
import json

# ComfyUI API地址
COMFYUI_API = "http://127.0.0.1:8188"

def enhance_competitor_image(image_path, enhancement_type="clarity"):
    """增强竞品图片（清晰度/细节/材质）"""
    # 1. 读取图片增强工作流模板
    with open('comfyui_workflow_image_enhance.json', 'r') as f:
        workflow = json.load(f)
    
    # 2. 注入竞品图片路径
    workflow["nodes"][1]["inputs"]["image"] = image_path
    
    # 3. 配置增强类型
    if enhancement_type == "clarity":
        workflow["nodes"][5]["inputs"]["denoise"] = 0.3
    elif enhancement_type == "detail":
        workflow["nodes"][5]["inputs"]["denoise"] = 0.5
    
    # 4. 提交到ComfyUI API
    response = requests.post(f"{COMFYUI_API}/prompt", json={"prompt": workflow})
    task_id = response.json()["prompt_id"]
    
    # 5. 等待处理完成
    # ... (等待逻辑)
    
    return enhanced_image_path
```

**使用场景**：
- 竞品图片模糊时，增强清晰度
- 提取竞品细节特征
- 生成竞品材质特写

---


---

## Phase 6: 竞品数据自动采集与联动优化 (NEW in v7.2)

### 6.1 竞品数据自动采集

**采集目标**：
- 产品图片（外观、细节、材质）
- 产品参数（尺寸、重量、材质、容量）
- 价格信息（电商平台、官网）
- 用户评价（好评率、差评关键词）
- 市场趋势（销量、搜索指数）

**自动采集流程**：
```
1. 接收采集任务（从🐭鼠或用户）
2. 识别竞品品牌和型号
3. 调用🐯虎（图像采集专家）采集图片
4. 调用公开API获取产品参数和价格
5. 调用爬虫脚本获取用户评价
6. 数据清洗与结构化
7. 存储到竞品数据库
8. 通知🐭鼠采集完成
```

**数据采集频率**：
- 核心竞品（Stanley、Owala、飞剑）：每周1次
- 次要竞品（其他品牌）：每月1次
- 新产品上市：实时采集

### 6.2 竞品数据实时更新

**更新触发条件**：
- 竞品官网更新产品信息
- 电商平台价格变动>5%
- 用户评价新增>100条
- 社交媒体提及量突增

**自动更新流程**：
```
1. 监控竞品数据源（官网、电商、社交媒体）
2. 检测到变化 → 触发更新任务
3. 重新采集变化的数据
4. 更新竞品数据库
5. 生成更新报告
6. 通知相关Agent（🐭鼠、🐍蛇、🐔鸡）
```

**数据版本管理**：
- 每次更新生成新版本（v1.0、v1.1...）
- 保留历史版本（便于对比分析）
- 记录更新时间和更新内容

### 6.3 与十四生肖团其他Agent的联动

**联动链1：🐲→🐯→🐰（竞品分析→图像采集→图像分析）**
```
🐲接收任务 → 识别需要采集的竞品
→ 调用🐯采集竞品图片
→ 🐯完成 → 调用🐰分析图片
→ 🐰完成 → 🐲生成竞品分析报告
→ 通知🐭任务完成
```

**联动链2：🐲→🐍（竞品分析→产品设计）**
```
🐲完成竞品分析 → 提取关键设计趋势
→ 调用🐍进行产品设计
→ 提供竞品对比输入
→ 🐍完成 → 🐲对比设计效果
→ 生成设计优化建议
```

**联动链3：🐲→🐔（竞品分析→设计评审）**
```
🐲生成竞品分析报告 → 提取评审标准
→ 调用🐔评审产品设计
→ 提供竞品对比基准
→ 🐔完成 → 🐲对比评审结果
→ 生成最终竞品策略建议
```

### 6.4 竞品分析报告自动生成

**报告内容**：
1. **竞品概览**：品牌、型号、价格、销量
2. **设计对比**：外观、材质、结构、CMF
3. **性能对比**：保温性能、耐用性、便携性
4. **用户评价对比**：好评率、差评关键词
5. **市场趋势分析**：销量趋势、搜索指数、社交媒体提及量
6. **设计建议**：基于竞品分析的设计优化建议

**报告格式**：
- Markdown文档（详细分析）
- HTML可视化报告（图表、对比表）
- PPT演示文稿（汇报用）

**自动生成流程**：
```
1. 采集竞品数据（Phase 6.1）
2. 数据分析与对比
3. 生成报告内容
4. 可视化图表生成
5. 报告排版与美化
6. 报告输出与分发
```

### 6.5 竞品监控告警

**告警规则**：
- 竞品价格下降>10% → 告警（可能影响销量）
- 竞品新品上市 → 告警（需要分析威胁）
- 竞品用户评价下降>5% → 告警（可能存在质量问题）
- 竞品社交媒体提及量突增>50% → 告警（可能有机营销或负面事件）

**告警流程**：
```
1. 监控竞品数据变化
2. 匹配告警规则
3. 生成告警报告
4. 通知🐭鼠（主理人）
5. 🐭鼠决策 → 启动应对措施
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
