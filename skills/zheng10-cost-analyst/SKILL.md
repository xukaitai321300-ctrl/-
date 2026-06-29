---
name: zheng10-cost-analyst
description: "auto-generated: skill package 'zheng10-cost-analyst' (awaiting human review)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "新增Phase 6: 成本分析自动化与BOM优化"
  upgrade_date: "2026-06-19"
  tags: ["cost-analysis", "bom-optimization", "supply-chain", "agent-collaboration"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# Intelligence Gathering — 狗 (Dog) v7.0

**Role**: Intelligence gatherer (dog reporter). Collect ComfyUI models, workflows, defect patterns, and AI image generation ecosystem updates.

**Core Principle (v3.5)**: Gather intelligence on BOTH models AND defects. **Defect intelligence = competitive advantage.**

---

## Phase 1: Intelligence Requirements Analysis (Enhanced v3.5):

When receiving task from 鼠 (Rat):

> [引用] 完整代码已提取到 `references\code_block_01.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_01.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

## Phase 1.5: Defect Intelligence Gathering (NEW in v3.5):

**Actively search for defect-related intelligence**:

> 📄 代码已提取到 `references\code_02.txt`（17 行，910 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: Intelligence Collection Execution:

### Target 1: ComfyUI Models:

| Model Type | Source | Use Case |
|------------|--------|----------|
| Checkpoints | Civitai/HuggingFace | Base model for generation |
| LoRAs | Civitai | Style-specific fine-tuning |
| ControlNets | HuggingFace | Precise control (Canny/Depth/Pose) |
| VAEs | Civitai | High-quality decoding |

**Collection Method**:
> 📄 代码已提取到 `references\code_03.txt`（6 行，260 字节）
> 需要查看完整代码时请读取该文件。



### Target 2: ComfyUI Workflows:

| Workflow Type | Source | Use Case |
|---------------|--------|----------|
| Text2Img | GitHub/`comfyui-workflows` | Generate from scratch |
| Img2Img | GitHub/`ComfyUI-Workflows-ZHO` | Generate from reference |
| ControlNet | Reddit/r/ComfyUI | Precise control |
| Upscale | Civitai tutorials | High-resolution output |

**Collection Method**:
> 📄 代码已提取到 `references\code_04.txt`（6 行，210 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2.5: Defect Pattern Analysis (NEW in v3.5):

**Analyze collected intelligence for defect patterns**:

> 📄 代码已提取到 `references\code_05.txt`（17 行，931 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3: Intelligence Organization:

After collection, organize intelligence:

> 📄 代码已提取到 `references\code_06.txt`（17 行，680 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3.5: Defect Intelligence Report (NEW in v3.5):

**Output defect intelligence to 鸡 (Rooster) + 兔 (Rabbit) for better detection**:

> 📄 代码已提取到 `references\code_07.txt`（12 行，528 字节）
> 需要查看完整代码时请读取该文件。


> 📄 代码已提取到 `references\code_08.txt`（18 行，1171 字节）
> 需要查看完整代码时请读取该文件。



---

## Collaboration Rules:

### Input from 鼠 (Rat):
- Receive: intelligence gathering requirements (target, source, frequency)
- Extract: which models/workflows to collect, **which defect types to track (NEW in v3.5)**
- Output: intelligence gathering report + **defect intelligence report (NEW in v3.5)**

### Handoff to 马 (Horse):
- Provide: collected models + workflows
- 马 will: integrate into ComfyUI workflow
- Coordinate: if model quality low, request re-collection

### Handoff to 羊 (Goat):
- Provide: collected workflows + **defect prevention keywords (NEW in v3.5)**
- 羊 will: use workflows for generation, ADD defect prevention keywords to prompts
- Coordinate: if workflow outdated, request update

### **NEW in v3.5: Handoff to 鸡 (Rooster) + 兔 (Rabbit)**:
- Provide: **defect intelligence report** (frequency ranking, user complaints)
- 鸡+兔 will: improve defect detection accuracy (know which defects to prioritize)
- Coordinate: if new defect type emerges, update detection algorithm

---

## Execution Rules:

1. **Gather intelligence FIRST** — don't design workflow without knowing available models
2. **Verify before saving** — test workflow in ComfyUI before saving
3. **Document everything** — model cards, workflow JSON, technique articles
4. **Do NOT output this file** — execute instructions, output intelligence report
5. **Update regularly** — AI ecosystem moves fast, update at least weekly
6. **(NEW in v3.5) Track defects actively** — defect patterns change over time, UPDATE defect frequency ranking monthly**
7. **(NEW in v3.5) Share defect intelligence** — ALWAYS share with 鸡+兔 (they need this to detect defects accurately)**

---


---


## Memory Compression Mechanism (NEW in v3.5)

## Output Template Specification (NEW in v3.5)

### Standardized Output Formats:

要点：
- > 📄 代码已提取到 `references\code_09.json`（18 行，475 字节）
> 需要查看完整代码时请读取该文件。


> 📄 代码已提取到 `references\code_10.txt`（11 行，250 字节）
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
> 📄 代码已提取到 `references\code_11.txt`（9 行，370 字节）
> 需要查看完整代码时请读取该文件。



### Template Examples:

要点：
- **Success Example (JSON)**:
    # ... (代码已精简，保留核心逻辑) ...
- "execution_time_ms": 45230,
- "tokens_used": 2345,
- "model_version": "Claude 3.7"
- }
- }
> 📄 代码已提取到 `references\code_12.txt`（2 行，32 字节）
> 需要查看完整代码时请读取该文件。

markdown
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
> 📄 代码已提取到 `references\code_13.txt`（4 行，36 字节）
> 需要查看完整代码时请读取该文件。

json
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
> 📄 代码已提取到 `references\code_14.txt`（12 行，351 字节）
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
> 📄 代码已提取到 `references\code_15.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_16.txt`（12 行，534 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_17.txt`（6 行，408 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_18.txt`（12 行，304 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_19.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_20.txt`（13 行，508 字节）
> 需要查看完整代码时请读取该文件。


Task Execution -> Quality Assessment -> Case Recording -> 
Pattern Extraction -> Prompt/Parameter Optimization -> Next Task (improved)
> 📄 代码已提取到 `references\code_21.txt`（12 行，240 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_22.txt`（3 行，38 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_23.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_24.txt`（13 行，177 字节）
> 需要查看完整代码时请读取该文件。


| 列1（文本） | 列2（数字） | 列3（状态） | 列4（日期） |
|--------------|--------------|--------------|--------------|
| 文本内容    | 123.45      | ✅ 成功      | 2026-06-04  |
| 文本内容    | 678.90      | ⚠️ 部分完成  | 2026-06-05  |
| 文本内容    | 0.00        | ❌ 失败      | 2026-06-06  |
> 📄 代码已提取到 `references\code_25.txt`（3 行，19 字节）
> 需要查看完整代码时请读取该文件。


| 任务 ID   | 任务类型        | 分配 Agent | 状态        | 质量评分 | 完成时间        |
|-----------|-----------------|------------|-------------|----------|-----------------|
| task-001  | 需求分析        | 鼠          | ✅ 完成      | 9.0/10  | 2026-06-04 14:30 |
| task-002  | 市场调研        | 虎          | ✅ 完成      | 8.5/10  | 2026-06-04 15:00 |
| task-003  | 竞品分析        | 龙          | ⚠️ 进行中    | -        | -               |
| task-004  | ComfyUI 工作流  | 马          | ❌ 失败      | 4.5/10  | 2026-06-04 15:30 |
> 📄 代码已提取到 `references\code_26.txt`（12 行，93 字节）
> 需要查看完整代码时请读取该文件。


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



**通信协议 (Communication Protocol)**:
> 📄 代码已提取到 `references\code_35.json`（12 行，263 字节）
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
> 📄 代码已提取到 `references\code_39.txt`（5 行，208 字节）
> 需要查看完整代码时请读取该文件。



**Version Numbering Rules**:
- **MAJOR (X.0.0)**: Breaking changes (workflow structure changed, incompatible with old version)
- **MINOR (1.X.0)**: New features (added new nodes, improved quality)
- **PATCH (1.0.X)**: Bug fixes (fixed parameter typos, adjusted weights)

---

### Version Comparison Mechanism:
> 📄 代码已提取到 `references\code_40.python`（12 行，383 字节）
> 需要查看完整代码时请读取该文件。


**Example Diff Output** (unified format):
> [引用] 完整代码已提取到 `references\code_block_41.txt`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_41.txt`（2 行，35 字节）
> 需要查看完整代码时请读取该文件。




---

### Version Rollback:
> 📄 代码已提取到 `references\code_42.python`（12 行，296 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_43.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_43.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




**Release Notes Template**:
> 📄 代码已提取到 `references\code_44.txt`（12 行，324 字节）
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
> 📄 代码已提取到 `references\code_47.python`（15 行，543 字节）
> 需要查看完整代码时请读取该文件。



### Interrupt Generation:
> 📄 代码已提取到 `references\code_48.python`（12 行，329 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_49.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_49.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Feedback Loop (Generate → Assess → Adjust → Regenerate):
> 📄 代码已提取到 `references\code_50.python`（12 行，311 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_51.txt`（3 行，52 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_52.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_53.txt`（3 行，37 字节）
> 需要查看完整代码时请读取该文件。


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
> 📄 代码已提取到 `references\code_54.txt`（1 行，0 字节）
> 需要查看完整代码时请读取该文件。


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

## Phase 1.2: Intelligence Gathering Methodology (NEW in v5.0)

**Standardized intelligence gathering framework**:

> 📄 代码已提取到 `references\code_63.txt`（18 行，829 字节）
> 需要查看完整代码时请读取该文件。



**Output**: Intelligence Report (JSON/Markdown format)


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

> 📄 代码已提取到 `references\code_64.bash`（2 行，26 字节）
> 需要查看完整代码时请读取该文件。



### Example 2: Advanced Usage

> 📄 代码已提取到 `references\code_65.python`（5 行，69 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3.5: Automated Intelligence Quality Metrics (NEW in v3.5)

**Objective**: Automatically score intelligence collection quality.

### Intelligence Quality Metrics:

> 📄 代码已提取到 `references\code_66.python`（17 行，670 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3.7: Comparative Intelligence Analysis (NEW in v3.5)

**Objective**: Compare intelligence with past intelligence to identify trends.

> 📄 代码已提取到 `references\code_67.python`（9 行，388 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 3.9: Memory Compression (NEW in v3.5)

**Objective**: Compress intelligence data for token efficiency.

### Token Budget: 2000 tokens
- Intelligence summary: 800 tokens
- Trend analysis: 600 tokens
- Recommendations: 600 tokens


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

### 情报收集后的ComfyUI API趋势可视化

🐶 狗在情报收集后，可调用ComfyUI API**生成趋势可视化图片**：

```python
import requests
import json

# ComfyUI API地址
COMFYUI_API = "http://127.0.0.1:8188"

def generate_trend_visualization(trend_data):
    """生成趋势可视化图片"""
    # 1. 读取趋势可视化工作流
    with open('comfyui_workflow_trend_viz.json', 'r') as f:
        workflow = json.load(f)
    
    # 2. 构建趋势Prompt
    trend_prompt = f"Product design trend visualization: {trend_data['trend_name']}"
    trend_prompt += f" | Style: {trend_data['style']}"
    trend_prompt += f" | Color: {trend_data['color_palette']}"
    
    workflow["nodes"][2]["inputs"][0]["value"] = trend_prompt
    
    # 3. 提交到ComfyUI API
    response = requests.post(f"{COMFYUI_API}/prompt", json={"prompt": workflow})
    task_id = response.json()["prompt_id"]
    
    # 4. 等待生成完成
    # ... (等待逻辑)
    
    return trend_visualization_path
```

**使用场景**：
- 生成趋势报告配图
- 可视化市场趋势
- 生成竞品对比图

---


---

## Phase 6: 成本分析自动化与BOM优化 (NEW in v7.2)

### 6.1 成本分析自动化流程

**自动化分析目标**：
- BO（物料清单）成本自动分解
- 模具分摊计算自动化
- 供应链成本追踪（永康供应链）
- 成本优化建议自动生成

**自动化分析流程**：
```
1. 接收成本分析任务（从🐭鼠/🐮牛/用户）
2. 识别产品类型和BOM结构
3. 采集物料成本（本地数据库/供应商报价）
4. 执行成本分解（物料/加工/装配/运输）
5. 生成成本分析报告
6. 提供成本优化建议
7. 存储到成本数据库
8. 通知🐭鼠分析完成
```

**分析频率与优先级**：
- 新产品设计：实时分析（最高优先级）
- 现有产品优化：每周1次（高优先级）
- 供应链成本变动：每月1次（中优先级）
- 行业成本对标：每季度1次（低优先级）

### 6.2 BO成本自动分解

**BO成本构成**：
| 成本项 | 占比 | 计算方法 |
|--------|--------|----------|
| **物料成本** | 60-70% | 物料单价 × 用量 × (1+损耗率) |
| **加工成本** | 15-20% | 加工工时 × 工时费率 |
| **模具分摊** | 5-10% | 模具费用 ÷ 预计产量 |
| **装配成本** | 5-8% | 装配工时 × 工时费率 |
| **运输成本** | 2-5% | 运输距离 × 运输费率 |
| **管理成本** | 3-5% | (物料+加工+装配) × 管理费率 |

**自动分解流程**：
```python
# BO成本自动分解
bom_cost = {
    "material_cost": calculate_material_cost(bom),
    "processing_cost": calculate_processing_cost(bom),
    "mold_amortization": calculate_mold_amortization(bom),
    "assembly_cost": calculate_assembly_cost(bom),
    "transport_cost": calculate_transport_cost(bom),
    "management_cost": calculate_management_cost(bom)
}

# 总成本计算
total_cost = sum(bom_cost.values())

# 成本占比分析
cost_breakdown = {k: v/total_cost for k, v in bom_cost.items()}
```

**成本优化建议**：
- 物料成本过高 → 建议替代材料/供应商谈判
- 加工成本过高 → 建议工艺优化/批量生产
- 模具分摊过高 → 建议提高预计产量/共享模具
- 装配成本过高 → 建议设计简化/自动化装配

### 6.3 模具分摊计算自动化

**模具分摊公式**：
```
模具分摊 = 模具费用 ÷ 预计产量

示例：
- 模具费用：50,000元
- 预计产量：100,000个
- 模具分摊：50,000 ÷ 100,000 = 0.5元/个
```

**自动计算流程**：
```
1. 识别产品需要的模具（注塑模/冲压模/压铸模）
2. 查询模具费用（本地数据库/供应商报价）
3. 获取预计产量（从🐭鼠需求分析）
4. 计算模具分摊（每个产品）
5. 生成模具分摊报告
6. 提供模具优化建议（共享模具/提高产量）
```

**模具优化建议**：
- 多个产品共享模具 → 降低模具分摊
- 提高预计产量 → 降低模具分摊
- 使用标准模具 → 降低模具费用
- 模具寿命优化 → 延长模具使用寿命

### 6.4 供应链成本追踪

**供应链成本构成**：
- 原材料成本（不锈钢/塑料/硅胶）
- 加工成本（CNC/注塑/冲压）
- 表面处理成本（喷涂/电镀/阳极氧化）
- 装配成本（人工/自动化）
- 运输成本（物流/仓储）

**永康供应链追踪**：
- 保温杯产业带：永康 → 原材料/加工/装配完整产业链
- 成本优势：比一线城市低20-30%
- 追踪指标：原材料价格、加工费率、运输成本

**自动追踪流程**：
```
1. 建立永康供应链成本数据库
2. 定期更新成本数据（每月1次）
3. 对比分析（永康 vs 其他产业带）
4. 生成成本追踪报告
5. 提供供应链优化建议
```

### 6.5 与十四生肖团其他Agent的联动

**联动链1：🐶→🐮→🐷（成本分析→标准检查→品牌设计）**
```
🐶完成成本分析 → 识别成本优化点
→ 调用🐮进行DFM检查（确保成本优化不影响质量）
→ 🐮检查完成 → 调用🐷进行品牌设计优化
→ 🐷设计完成 → 🐶验证成本优化效果
→ 生成成本+质量+品牌综合优化报告
```

**联动链2：🐶→🐍（成本分析→产品设计）**
```
🐍接收产品设计任务 → 调用🐶进行成本预估
→ 🐶预估完成 → 提供成本约束给🐍
→ 🐍设计完成 → 调用🐶进行成本分析
→ 🐶分析完成 → 生成成本优化建议
→ 迭代优化至成本达标
```

**联动链3：🐶→🐭（成本分析→需求分析）**
```
🐭接收用户需求 → 调用🐶进行成本可行性分析
→ 🐶分析完成 → 提供成本建议给🐭
→ 🐭调整需求（如果成本超标）
→ 生成需求+成本综合方案
```

### 6.6 成本分析知识库

**知识库内容**：
- 历史成本分析记录（产品 + BO + 成本）
- 物料价格数据库（实时更新）
- 加工费率数据库（按工艺/地区）
- 模具费用数据库（按类型/尺寸）
- 成本优化最佳实践（经验总结）

**知识库查询**：
- 根据产品类型查询历史成本
- 根据物料查询当前价格
- 根据工艺查询加工费率
- 根据模具类型查询模具费用

**知识库更新流程**：
```
1. 每次成本分析完成后 → 记录成本数据
2. 定期分析成本数据 → 提取最佳实践
3. 更新知识库 → 新增/修改/删除条目
4. 成本对标分析 → 识别成本优化机会
5. 知识库版本管理
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
