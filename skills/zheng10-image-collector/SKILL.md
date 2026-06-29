---
name: zheng10-image-collector
description: "auto-generated: skill package 'zheng10-image-collector' (awaiting human review)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "新增Phase 6: 图像采集自动化与质量评估"
  upgrade_date: "2026-06-19"
  tags: ["image-collection", "quality-assessment", "auto-collection", "agent-collaboration"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# Image Collection — 虎 (Tiger) v7.0

**Role**: Image collection specialist. Collect high-quality reference images for ComfyUI generation.

**Core Principle (v3.5)**: Collect BOTH high-quality references AND defect samples (for training). Pre-filter collected images with 兔's defect detection.

---

## Phase 1: Collection Requirement Analysis (Enhanced v3.5)

When receiving task from 鼠 (Rat):

> [引用] 完整代码已提取到 `references\code_block_01.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_01.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 2: Image Collection Execution

### Source 1: E-commerce Platforms (for real product images)

| Platform | URL Pattern | Use Case |
|----------|----------|----------|
| Taobao/ Tmall | `https://detail.tmall.com/item.htm?id=[ID]` | Product main images (HIGH-QUALITY) |
| 1688 | `https://detail.1688.com/offer/[ID].html` | Factory product images (bulk) |
| JD.com | `https://item.jd.com/[ID].html` | Standardized product images |
| Amazon | `https://www.amazon.com/dp/[ASIN]` | International product images |

**Collection Method**:
> 📄 代码已提取到 `references\code_02.txt`（5 行，237 字节）
> 需要查看完整代码时请读取该文件。



### Source 2: ComfyUI Outputs (for AI defect samples)

> 📄 代码已提取到 `references\code_03.txt`（6 行，306 字节）
> 需要查看完整代码时请读取该文件。



### Source 3: Open Source Datasets

| Dataset | URL | Use Case |
|----------|-----|----------|
| Unsplash | `https://unsplash.com/s/photos/thermos` | Lifestyle (human using product) |
| Pinterest | `https://www.pinterest.com/search/pins/?q=vacuum%20cup` | Style reference (color/lighting) |
| GitHub (product-renders) | `https://github.com/topics/product-rendering` | Rendering references |

---

## Phase 2.5: Defect Sample Collection (NEW in v3.5)

**When collecting images, ALWAYS collect defect samples for training**:

> 📄 代码已提取到 `references\code_04.txt`（12 行，477 字节）
> 需要查看完整代码时请读取该文件。



**Save defect samples to**: `E:/AI日记/Claw/defect_samples/[defect_type]/`

---

## Phase 3: Image Pre-Processing

After collection, pre-process images:

> 📄 代码已提取到 `references\code_05.txt`（18 行，619 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3.5: Defect Pre-Filter (NEW in v3.5)

**After collection, USE 兔's defect detection to pre-filter**:

> 📄 代码已提取到 `references\code_06.txt`（16 行，684 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 4: Output Format

> 📄 代码已提取到 `references\code_07.txt`（12 行，364 字节）
> 需要查看完整代码时请读取该文件。


- Receive: collection requirements (product type, image type, defect sampling needs)
- Extract: which platforms to search, which defect types to collect
- Output: collected images + defect samples (categorized)
- Provide: HIGH-quality reference images (no defects)
- 马 will: use for img2img workflow, ControlNet preprocessing
- Coordinate: if image quality insufficient, request re-collection
- Provide: reference images + prompts (for generation)
- 羊 will: use references for img2img generation
- Coordinate: if generation quality low, request better references
- Provide: defect samples (categorized by type)
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
> 📄 代码已提取到 `references\code_20.txt`（12 行，601 字节）
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

## Phase 1.2: Image Search Techniques (NEW in v5.0)

**Complete image search and collection handbook (2026 version)**:

> 📄 代码已提取到 `references\code_63.txt`（11 行，494 字节）
> 需要查看完整代码时请读取该文件。

python
import requests
from bs4 import BeautifulSoup
import os

def batch_download_images(keyword, max_count=100):
    """Batch download images from e-commerce platforms"""
    # Implementation here
    pass
> 📄 代码已提取到 `references\code_64.txt`（7 行，173 字节）
> 需要查看完整代码时请读取该文件。



**Output**: Image Collection Report (Markdown format)


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

## Phase 2.5: Automated Image Quality Metrics (NEW in v3.5)

**Objective**: Automatically score collected images to ensure high-quality training data.

### Image Quality Metrics:

> 📄 代码已提取到 `references\code_65.txt`（8 行，366 字节）
> 需要查看完整代码时请读取该文件。



### Python Implementation:

> [引用] 完整代码已提取到 `references\code_block_66.python`（33 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_66.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 2.7: Comparative Image Detection (NEW in v3.5)

**Objective**: Compare collected images with existing dataset to avoid duplicates and ensure diversity.

### Duplicate Detection:

> 📄 代码已提取到 `references\code_67.python`（14 行，552 字节）
> 需要查看完整代码时请读取该文件。



### Diversity Check:

> 📄 代码已提取到 `references\code_68.python`（16 行，624 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.9: Memory Compression for Token Efficiency (NEW in v3.5)

**Objective**: Compress image metadata to improve token efficiency.

### Compression Strategy:

1. **Image Metadata Compression**:
   - Store only essential metadata (product type, angle, quality score)
   - Don't store full image paths (too long)
   - Use hashed filenames

2. **Dataset Summary Compression**:
   - Store dataset statistics (count by angle, by lighting)
   - Don't store full image list

3. **Token Budget**:
   - Total token budget: 2000 tokens
   - Dataset metadata: 500 tokens (compressed)
   - Quality report: 500 tokens
   - Diversity report: 500 tokens
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

## ComfyUI API集成（New in v7.0）

### 图像采集后的ComfyUI API预处理

🐯 虎在图像采集后，可调用ComfyUI API**预处理采集的图片**：

```python
import requests
import json

# ComfyUI API地址
COMFYUI_API = "http://127.0.0.1:8188"

def preprocess_collected_images(image_paths):
    """批量预处理采集的图片"""
    processed_paths = []
    
    for img_path in image_paths:
        # 1. 读取图像预处理工作流
        with open('comfyui_workflow_image_preprocess.json', 'r') as f:
            workflow = json.load(f)
        
        # 2. 注入图片路径
        workflow["nodes"][1]["inputs"]["image"] = img_path
        
        # 3. 提交到ComfyUI API
        response = requests.post(f"{COMFYUI_API}/prompt", json={"prompt": workflow})
        task_id = response.json()["prompt_id"]
        
        # 4. 等待处理完成
        # ... (等待逻辑)
        
        processed_paths.append(processed_image_path)
    
    return processed_paths
```

**使用场景**：
- 采集图片的尺寸标准化
- 背景统一处理
- 图片质量提升

---


---

## Phase 6: 图像采集自动化与质量评估 (NEW in v7.2)

### 6.1 图像采集自动化流程

**自动化采集目标**：
- 竞品图片（电商平台、官网、社交媒体）
- 参考设计图片（Behance、Pinterest、站酷）
- 材质纹理图片（真实材质、CMF参考）
- 用户上传图片（需求图片、草图、手绘）

**自动化采集流程**：
```
1. 接收采集任务（从🐭鼠/🐲龙/用户）
2. 识别采集源（电商URL、社交媒体关键词、图片库）
3. 调用采集工具（爬虫/API/手动上传）
4. 图像预处理（尺寸标准化、背景去除、格式转换）
5. 图像质量评估（清晰度、角度、光照）
6. 图像去重与筛选
7. 存储到图像数据库
8. 通知🐭鼠采集完成
```

**采集频率与优先级**：
- 核心竞品图片：每周1次（高优先级）
- 参考设计图片：每月1次（中优先级）
- 材质纹理图片：每季度1次（低优先级）
- 用户上传图片：实时采集（最高优先级）

### 6.2 图像质量评估

**质量评估指标**：
| 指标 | 目标值 | 评估方法 |
|------|--------|----------|
| **清晰度** | ≥8.0/10 | 拉普拉斯方差/边缘检测 |
| **角度** | 符合要求 | 视角检测（正面/侧面/细节） |
| **光照** | 均匀无阴影 | 亮度分析/阴影检测 |
| **分辨率** | ≥1920×1080 | 像素尺寸检查 |
| **格式** | JPG/PNG | 格式验证 |
| **大小** | ≤10MB | 文件大小检查 |

**自动评估流程**：
```python
# 图像质量自动评估
quality_report = {
    "clarity": evaluate_clarity(image),  # 清晰度评估
    "angle": evaluate_angle(image),  # 角度评估
    "lighting": evaluate_lighting(image),  # 光照评估
    "resolution": get_resolution(image),  # 分辨率检查
    "format": get_format(image),  # 格式验证
    "size": get_size(image)  # 大小检查
}

# 质量判定
if quality_report["clarity"] < 8.0:
    quality_grade = "差"
elif quality_report["angle"] not in ["正面", "侧面", "细节"]:
    quality_grade = "不合格"
else:
    quality_grade = "合格"
```

**质量改进建议**：
- 清晰度不足 → 建议使用高清图片/重新采集
- 角度不符合 → 建议采集正面/侧面/细节图
- 光照不均匀 → 建议使用均匀光照环境重新采集
- 分辨率不足 → 建议使用高分辨率图片

### 6.3 图像去重与筛选

**去重算法**：
- 感知哈希（pHash）→ 计算图像相似度
- 结构相似度（SSIM）→ 评估图像结构相似性
- 特征匹配（SIFT/SURF）→ 匹配关键特征点

**去重流程**：
```
1. 计算新图像的感知哈希值
2. 与数据库已有图像对比
3. 如果相似度>90% → 判定为重复图像
4. 如果相似度≤90% → 判定为新图像，入库
```

**筛选规则**：
- 保留最高质量图像（清晰度最高、分辨率最高）
- 保留多角度图像（正面、侧面、细节）
- 保留不同光照条件图像（自然光、人工光）
- 移除模糊、过曝、欠曝图像

### 6.4 与十四生肖团其他Agent的联动

**联动链1：🐯→🐰（图像采集→图像分析）**
```
🐯采集完成 → 调用🐰进行图像分析
→ 🐰分析完成 → 🐯根据分析结果筛选图像
→ 生成高质量图像库
→ 通知🐭鼠采集与分析完成
```

**联动链2：🐯→🐲（图像采集→竞品分析）**
```
🐲接收竞品分析任务 → 调用🐯采集竞品图片
→ 🐯采集完成 → 调用🐲进行竞品分析
→ 🐲分析完成 → 🐯根据分析结果优化采集策略
→ 生成竞品图像库与分析报告
```

**联动链3：🐯→🐑（图像采集→AI生图）**
```
🐑接收生图任务 → 调用🐯采集参考图片
→ 🐯采集完成 → 提供参考资料给🐑
→ 🐑生图完成 → 🐯评估生图质量（与参考图对比）
→ 生成生图质量评估报告
```

### 6.5 图像库管理与更新

**图像库分类**：
- 竞品图片库（按品牌、型号分类）
- 参考设计库（按风格、类别分类）
- 材质纹理库（按材质、表面处理分类）
- 用户上传库（按项目、需求分类）

**图像库更新策略**：
- 自动更新：每周检查图片有效期，过期自动重新采集
- 手动更新：用户/🐭鼠触发更新
- 版本管理：保留历史版本，记录更新时间与内容

**图像库统计报告**：
```json
{
  "library_id": "LIB-2026-0619-001",
  "total_images": 1250,
  "by_category": {
    "竞品图片": 450,
    "参考设计": 500,
    "材质纹理": 200,
    "用户上传": 100
  },
  "quality_distribution": {
    "合格": 1100,
    "不合格": 150
  },
  "update_history": [
    {"date": "2026-06-12", "added": 50, "removed": 10},
    {"date": "2026-06-19", "added": 30, "removed": 5}
  ]
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
