---

version: "7.2.4"

author: "猴哥（十二生肖团）"

name: zheng10-skill-optimizer

display_name: "十二生肖团元层工具·技能优化与参数调优双专家"

display_name_en: "Skill Optimizer"

name_en: "zheng10-skill-optimizer"

description_zh: "十二生肖团元层工具·技能优化与参数调优双专家。Phase 1 ComfyUI 参数调优（采样器/步数/CFG/LoRA 权重速查表）｜Phase 2 技能质量审计（12 段标准）｜Phase 3 自动化技能升级｜Phase 4 批量优化 12 生肖技能；与鸡、羊、鼠联动。非十二生肖成员，属扩展元层。"

description_en: "Zodiac team execution-layer skill: Skill Optimizer. (See description_zh for full details.)"

description: "十二生肖团元层工具·技能优化与参数调优双专家。Phase 1 ComfyUI 参数调优（采样器/步数/CFG/LoRA 权重速查表）｜Phase 2 技能质量审计（12 段标准）｜Phase 3 自动化技能升级｜Phase 4 批量优化 12 生肖技能；与鸡、羊、鼠联动。非十二生肖成员，属扩展元层。"

license: MIT

metadata:

  author: 猴哥

  version: "7.2.4"

  previous_version: "7.1"

  upgrade_reason: 增加Phase 6参数调优自动化与智能推荐，提升调优效率

  upgrade_date: 2026-06-19

  tags:

    - skill-optimization

    - parameter-tuning

    - evolution-loop

    - linkage

    - auto-tuning

  generated_date: 2026-06-15

  classification: P0-core-standardized

when_to_use: "在涉及「skill-optimizer」职责的任务中调用本技能；十二生肖团元层工具·技能优化与参数调优双专家。"

---

> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。

> - 任务分发/协调：读取"执行层"和"联动规则"章节

> - 需求分析：读取"需求分析框架"章节

> - 工作流审查：读取"工作流规范"章节

> - 质量评审：读取"评审标准"章节





# Skill Optimizer — 元层工具（参数调优 & 能力优化双职能）



**Dual Role**: Parameter tuning expert (ComfyUI) + Skill quality auditor (12-section standard).



**Core Principle**: Data-driven optimization. Every parameter change must have a measurable quality improvement.



---



## Phase 1: Parameter Optimization (ComfyUI Tuning)



When receiving generation results that need improvement:



> 📄 代码已提取到 `references\code_01.txt`（12 行，376 字节）

> 需要查看完整代码时请读取该文件。







### Parameter Tuning Reference Table



| Quality Issue | Sampler | Steps | CFG | Resolution | ControlNet Strength |

|---------------|---------|-------|-----|------------|---------------------|

| Blur / lack of detail | DPM++ 2M SDE Karras | 36 | 6.5 | 1024×1024 | 0.8 |

| Oversaturation | DPM++ 2M SDE Karras | 28 | 4.5 | 512×512 | 0.6 |

| Insufficient detail | DPM++ 2M SDE Karras | 36 | 6.5 | 768×768 | 0.7 |

| Style mismatch | DPM++ 2M SDE Karras | 30 | 5.5 | Match reference | 0.8 |

| Distortion (img2img) | DPM++ 2M SDE Karras | 30 | 5.5 | Original | Increase to 0.9 |

| Noise / artifacts | DPM++ 2M SDE Karras | 32 | 5.0 | 512×512 | 0.5 |



### LoRA Tuning Guide



| LoRA Type | Purpose | Recommended Weight |

|------------|---------|---------------------|

| Detail Tweaker | Increase fine details | 0.5-0.8 |

| Negative Hand | Fix bad hands/anatomy | 0.8-1.2 |

| Style LoRA | Apply specific style | 0.3-0.7 |

| Product Photography | Improve product render quality | 0.6-1.0 |



---



## Phase 2: Skill Quality Audit (12-Section Standard)



When receiving a skill file path or skill name:



> [引用] 完整代码已提取到 `references\code_block_02.txt`（21 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_02.txt`（563 字节）

> 需要查看完整代码时请读取该文件。









### 12-Section Standard (v7.0)



要点：

- | # | Section Name | Required | Description |

- |---|--------------|----------|-------------|

- | 1 | Core Positioning | ✅ Required | Role definition, core goals |

- | 2 | Core Capability Modules | ✅ Required | Function module table |

- | 3 | Working Principle | ✅ Required | Workflow explanation |

- | 4 | Output Structure | ✅ Required | Output format definition |

- | 5 | Collaboration Rules | ⭕ Optional | Multi-agent collaboration |

- | 6 | Execution Rules | ✅ Required | Do's and Don'ts |

- | 7 | Example Library | ✅ Required (v3.0 new) | 3-5 example dialogues |

- | 8 | Parameter Tuning Guide | ✅ Required (v3.0 new) | Performance optimization |

- | 9 | Data Interface | ⭕ Optional | External data source interface |

- | 10 | Advanced Capabilities | ⭕ Optional | Advanced feature expansion |

- | 11 | Troubleshooting | ✅ Required | Common issues + solutions |

- | 12 | Summary | ⭕ Optional | Core points summary |



---



## Phase 3: Automated Skill Upgrade



When audit report shows missing/low-quality sections:



> 📄 代码已提取到 `references\code_03.txt`（12 行，407 字节）

> 需要查看完整代码时请读取该文件。







### Upgrade Report Template



> 📄 代码已提取到 `references\code_04.txt`（12 行，301 字节）

> 需要查看完整代码时请读取该文件。







---



## Phase 4: Batch Skill Optimization (for 12 Zodiac Skills)



When receiving request to optimize all zodiac skills:



> [引用] 完整代码已提取到 `references\code_block_05.txt`（20 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_05.txt`（542 字节）

> 需要查看完整代码时请读取该文件。







| Priority | Skill | Reason |

|----------|-------|--------|

| P0 | 产品研究 (鼠) | Main coordinator, must be highest quality |

| P0 | 出图执行 (羊) | Core generator, directly affects output |

| P0 | 设计评审 (鸡) | Quality gatekeeper, must be accurate |

| P1 | ComfyUI 架构 (马) | Workflow builder, affects efficiency |

| P1 | 设计调整 (猴) | Parameter tuner, affects quality |

| P2 | Others | Support roles, upgrade after P0/P1 |

> 📄 代码已提取到 `references\code_06.txt`（13 行，492 字节）

> 需要查看完整代码时请读取该文件。







---



## Collaboration Rules



### Input from 鸡 (Rooster)

- Receive: generation quality score (< 7.0)

- Extract: low-scoring dimensions, specific issues

- Output: parameter optimization plan (which params to adjust)



### Handoff to 羊 (Goat)

- Provide: optimized workflow JSON + parameter configuration table

- 羊 will: re-generate images with new parameters

- Coordinate: if quality still < 7.0, request further optimization



### Input from 鼠 (Rat)

- Receive: skill upgrade request (batch or single)

- Extract: skill name, target version (usually v3.0)

- Output: upgraded skill file + upgrade report



### Handoff to 鼠 (Rat)

- Provide: batch upgrade report (all zodiac skills)

- 鼠 will: decide whether to deploy upgraded skills

- Coordinate: if any skill upgrade failed, report to 鼠 for manual review



---



## Execution Rules



1. **Data-driven** — every parameter change must have A/B test proof

2. **Single variable** — only change 1-2 parameters at a time (isolate effect)

3. **Measure quality** — use 鸡's 5-dimension scoring (0-10)

4. **Backup first** — always backup original skill before upgrade

5. **Validate after** — check YAML syntax, code correctness, trigger accuracy

6. **Do NOT output this file** — execute instructions, output optimization report

7. **Batch mode** — when optimizing all zodiac skills, generate batch report

8. **Continuous improvement** — after upgrade, monitor skill performance in real usage



---



---





---





## Memory Compression Mechanism (NEW in v3.5)



## Output Template Specification (NEW in v3.5)



### Standardized Output Formats:



要点：

- > 📄 代码已提取到 `references\code_07.json`（18 行，475 字节）

> 需要查看完整代码时请读取该文件。





> 📄 代码已提取到 `references\code_08.txt`（11 行，250 字节）

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

> 📄 代码已提取到 `references\code_09.txt`（9 行，370 字节）

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

> 📄 代码已提取到 `references\code_10.txt`（2 行，32 字节）

> 需要查看完整代码时请读取该文件。



```markdown

**Agent**: 竞品分析

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

> 📄 代码已提取到 `references\code_11.txt`（4 行，36 字节）

> 需要查看完整代码时请读取该文件。



```json

- {

- "timestamp": "2026-06-04T15:00:00+08:00",

- "agent_id": "ComfyUI 参数调优",

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

> 📄 代码已提取到 `references\code_12.txt`（12 行，351 字节）

> 需要查看完整代码时请读取该文件。





Level 1: Daily Log (<架构根目录>/.workbuddy/memory/YYYY-MM-DD.md)

  - Append-only, max 500 lines/day

  - Auto-trigger: End of session OR >500 lines

  - Compression: Keep only key decisions + errors



Level 2: Weekly Summary (<架构根目录>/.workbuddy/memory/weekly/YYYY-WW.md)

  - Extract from daily logs (last 7 days)

  - Categories: Decisions / Errors / Optimizations / User Feedback

  - Max 200 lines/week



Level 3: Monthly Digest (<架构根目录>/.workbuddy/memory/MEMORY.md)

  - Extract from weekly summaries (last 4 weeks)

  - Keep only: Long-term preferences / Cross-project conventions / Skill versions

  - Max 3000 chars (hard limit)

> 📄 ⚠️ 目标代码文件缺失（原碎片指向 code_block_13.*，未随库分发，内容无法恢复）。

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

> 📄 代码已提取到 `references\code_14.txt`（12 行，534 字节）

> 需要查看完整代码时请读取该文件。





def retrieve_memory(query, max_results=5):

    """Retrieve relevant memory entries using keyword + recency"""

    

    # 1. Keyword matching (from query)

    keywords = extract_keywords(query)

    

    # 2. Search in MEMORY.md (long-term)

    long_term_results = search_file(

        "<架构根目录>/.workbuddy/memory/MEMORY.md",

        keywords

    )

    

    # 3. Search in recent weekly summaries (medium-term)

    weekly_results = search_recent_weeks(keywords, weeks=2)

    

    # 4. Search in today's log (short-term)

    today_results = search_file(

        f"<架构根目录>/.workbuddy/memory/{get_today()}.md",

        keywords

    )

    

    # 5. Merge and rank by relevance + recency

    all_results = long_term_results + weekly_results + today_results

    ranked_results = rank_by_relevance(all_results, query)

    

    return ranked_results[:max_results]

> 📄 代码已提取到 `references\code_15.txt`（6 行，408 字节）

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

> 📄 代码已提取到 `references\code_16.txt`（12 行，304 字节）

> 需要查看完整代码时请读取该文件。





class CaseDatabase:

    def __init__(self, db_path="<架构根目录>/.workbuddy/learning_db/"):

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

> 📄 ⚠️ 目标代码文件缺失（原碎片指向 code_block_17.*，未随库分发，内容无法恢复）。

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

> 📄 代码已提取到 `references\code_18.txt`（13 行，508 字节）

> 需要查看完整代码时请读取该文件。





Task Execution -> Quality Assessment -> Case Recording -> 

Pattern Extraction -> Prompt/Parameter Optimization -> Next Task (improved)

> 📄 代码已提取到 `references\code_19.txt`（12 行，240 字节）

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

1. [行动 1] → 分配给: Ox

2. [行动 2] → 分配给: Tiger

- **错误代码**: ERR_TIMEOUT

- **错误详情**: [中文说明]

- **恢复操作**: [中文说明]

> 📄 代码已提取到 `references\code_20.txt`（3 行，38 字节）

> 需要查看完整代码时请读取该文件。





# 需求分析报告



## 1. 任务信息

- **任务 ID**: task-001

- **执行 Agent**: Product Researcher

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

1. 市场调研 → 分配给: Tiger

2. 竞品分析 → 分配给: Dragon



## 5. 错误信息（如有）

- **无错误信息**

> 📄 ⚠️ 目标代码文件缺失（原碎片指向 code_block_21.*，未随库分发，内容无法恢复）。

> 需要查看完整代码时请读取该文件。





- **任务 ID**: task-005

- **执行 Agent**: Rooster

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

- **建议**: 立即升级到 Monkey，添加 "anisotropic reflection, physical based rendering" 到 prompt

- **质量评分**: 8.25/10

- **评分理由**: 塑料质感缺陷需改进，其他缺陷均通过

- **改进建议**: 升级到 Monkey调整参数

1. 参数调整 → 分配给: Monkey

2. 重新生成 → 分配给: Goat

- **无错误信息**

> 📄 代码已提取到 `references\code_22.txt`（13 行，177 字节）

> 需要查看完整代码时请读取该文件。





| 列1（文本） | 列2（数字） | 列3（状态） | 列4（日期） |

|--------------|--------------|--------------|--------------|

| 文本内容    | 123.45      | ✅ 成功      | 2026-06-04  |

| 文本内容    | 678.90      | ⚠️ 部分完成  | 2026-06-05  |

| 文本内容    | 0.00        | ❌ 失败      | 2026-06-06  |

> 📄 代码已提取到 `references\code_23.txt`（3 行，19 字节）

> 需要查看完整代码时请读取该文件。





| 任务 ID   | 任务类型        | 分配 Agent | 状态        | 质量评分 | 完成时间        |

|-----------|-----------------|------------|-------------|----------|-----------------|

| task-001  | 需求分析        | 鼠          | ✅ 完成      | 9.0/10  | 2026-06-04 14:30 |

| task-002  | 市场调研        | 虎          | ✅ 完成      | 8.5/10  | 2026-06-04 15:00 |

| task-003  | 竞品分析        | 龙          | ⚠️ 进行中    | -        | -               |

| task-004  | ComfyUI 工作流  | 马          | ❌ 失败      | 4.5/10  | 2026-06-04 15:30 |

> 📄 代码已提取到 `references\code_24.txt`（12 行，93 字节）

> 需要查看完整代码时请读取该文件。





1. **验证失败** → 返回详细错误信息（JSON Schema 验证错误）

2. **自动修复** → 尝试自动修复（填充缺失字段/修正数据类型）

3. **人工介入** → 如果自动修复失败，上报给 Rat进行人工介入

**所有 Agent 输出前必须检查**:

- [ ] JSON 输出符合 JSON Schema 验证规则

- [ ] Markdown 输出使用标准化模板

- [ ] 表格输出使用标准化格式

- [ ] 所有字段都是中文（专业术语除外）

- [ ] 所有错误信息都是中文

- [ ] 质量评分已填写（0-10分）

- [ ] 下一步行动已明确（分配给具体 Agent）

> **⚠️ 重要**: 输出模板精细化优化是 **v4.3** 的核心改进。所有 Agent 必须严格遵循标准化模板，确保输出一致性。

**⚠️ 所有生肖团职能必须严格遵守以下条令（违反任一 = 失效）**

> 📄 代码已提取到 `references\code_25.txt`（6 行，222 字节）

> 需要查看完整代码时请读取该文件。







**示例 (Correct vs. Wrong)**:

> 📄 代码已提取到 `references\code_26.txt`（6 行，111 字节）

> 需要查看完整代码时请读取该文件。







---



### 条令 2: 必须遵循工作流程 (MANDATORY Workflow Compliance)

> 📄 代码已提取到 `references\code_27.txt`（6 行，219 字节）

> 需要查看完整代码时请读取该文件。







**工作流程 (7 Phases)**:

> 📄 代码已提取到 `references\code_28.txt`（8 行，169 字节）

> 需要查看完整代码时请读取该文件。







---



### 条令 3: 必须保证质量 (MANDATORY Quality Assurance)

> 📄 代码已提取到 `references\code_29.txt`（6 行，246 字节）

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

> 📄 代码已提取到 `references\code_30.txt`（6 行，259 字节）

> 需要查看完整代码时请读取该文件。







**错误日志格式 (Error Log Format)**:

> 📄 代码已提取到 `references\code_31.yaml`（8 行，238 字节）

> 需要查看完整代码时请读取该文件。







---



### 条令 5: 必须协作沟通 (MANDATORY Collaboration)

> 📄 代码已提取到 `references\code_32.txt`（6 行，299 字节）

> 需要查看完整代码时请读取该文件。







**通信协议 (Communication Protocol)**:

> 📄 代码已提取到 `references\code_33.json`（12 行，263 字节）

> 需要查看完整代码时请读取该文件。







---



### 条令 6: 必须持续学习 (MANDATORY Continuous Learning)

> 📄 代码已提取到 `references\code_34.txt`（6 行，300 字节）

> 需要查看完整代码时请读取该文件。







**学习循环 (Learning Loop)**:

> 📄 代码已提取到 `references\code_35.txt`（2 行，69 字节）

> 需要查看完整代码时请读取该文件。







---



### 条令 7: 必须尊重职能 (MANDATORY Role Respect)

> 📄 代码已提取到 `references\code_36.txt`（6 行，249 字节）

> 需要查看完整代码时请读取该文件。







**职能边界 (Role Boundaries)**:

| 职能 | 可以做的 | 不可以做的 |

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

> 📄 代码已提取到 `references\code_37.txt`（5 行，208 字节）

> 需要查看完整代码时请读取该文件。







**Version Numbering Rules**:

- **MAJOR (X.0.0)**: Breaking changes (workflow structure changed, incompatible with old version)

- **MINOR (1.X.0)**: New features (added new nodes, improved quality)

- **PATCH (1.0.X)**: Bug fixes (fixed parameter typos, adjusted weights)



---



### Version Comparison Mechanism:

> 📄 代码已提取到 `references\code_38.python`（12 行，383 字节）

> 需要查看完整代码时请读取该文件。





**Example Diff Output** (unified format):

> [引用] 完整代码已提取到 `references\code_block_39.txt`（20 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_39.txt`（398 字节）

> 需要查看完整代码时请读取该文件。









---



### Version Rollback:

> 📄 代码已提取到 `references\code_40.python`（12 行，296 字节）

> 需要查看完整代码时请读取该文件。





> [引用] 完整代码已提取到 `references\code_block_41.python`（21 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_41.python`（923 字节）

> 需要查看完整代码时请读取该文件。









**Release Notes Template**:

> 📄 代码已提取到 `references\code_42.txt`（12 行，324 字节）

> 需要查看完整代码时请读取该文件。







---



### Version Management Best Practices:

> 📄 代码已提取到 `references\code_43.txt`（9 行，428 字节）

> 需要查看完整代码时请读取该文件。







### Version Management Workflow:

> 📄 代码已提取到 `references\code_44.txt`（2 行，90 字节）

> 需要查看完整代码时请读取该文件。





**Execution Rules (NEW in v4.0)**:

36. **ALWAYS use version control** — Git + ComfyUI workflow versioning

37. **ALWAYS compare versions before releasing** — generate diff report

38. **ALWAYS backup before rollback** — prevent accidental data loss

39. **ALWAYS include release notes** — document changes for users

40. **ALWAYS test before marking stable** — ensure quality threshold met

> 📄 代码已提取到 `references\code_45.python`（15 行，543 字节）

> 需要查看完整代码时请读取该文件。







### Interrupt Generation:

> 📄 代码已提取到 `references\code_46.python`（12 行，329 字节）

> 需要查看完整代码时请读取该文件。





> [引用] 完整代码已提取到 `references\code_block_47.python`（21 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_47.python`（717 字节）

> 需要查看完整代码时请读取该文件。









### Feedback Loop (Generate → Assess → Adjust → Regenerate):

> 📄 代码已提取到 `references\code_48.python`（12 行，311 字节）

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

> 📄 代码已提取到 `references\code_49.txt`（3 行，52 字节）

> 需要查看完整代码时请读取该文件。





def process_image_input(image_source, image_type="reference"):

    """Process image input using the vision engine"""

    

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

    

    # 3. Extract image features (using vision engine)

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

> 📄 ⚠️ 目标代码文件缺失（原碎片指向 code_block_50.*，未随库分发，内容无法恢复）。

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

> 📄 代码已提取到 `references\code_51.txt`（3 行，37 字节）

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

> 📄 ⚠️ 目标代码文件缺失（原碎片指向 code_block_52.*，未随库分发，内容无法恢复）。

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

23. **ALWAYS extract image features** — use the vision engine (CLIP/ResNet)

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

> [引用] 完整代码已提取到 `references\code_block_53.python`（20 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_53.python`（766 字节）

> 需要查看完整代码时请读取该文件。









### C. Version Rollback

> 📄 代码已提取到 `references\code_54.python`（16 行，507 字节）

> 需要查看完整代码时请读取该文件。







### D. Version Release

> [引用] 完整代码已提取到 `references\code_block_55.python`（27 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_55.python`（823 字节）

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



## Prompt Library: usage_examples



### 使用示例



**示例 1**: 生成不锈钢保温杯（圆柱形）产品图



- 1. 从 by_product_type.vacuum_cup.subtypes.cylinder 获取正面提示词

- 2. 从 by_material.stainless_steel 获取材质提示词

- 3. 从 defect_prevention 获取缺陷预防提示词

- 4. 组合提示词：{product} + {material} + {defect_prevention}

- 5. 使用 (外部生图引擎)_presets.vacuum_cup_cylinder 的工作流配置



**示例提示词**: `vacuum cup, perfectly cylindrical body, stainless steel brushed texture, anisotropic reflection, leak-proof lid, no plastic texture, perfectly symmetric lid, product photography, pure white background`



**示例 2**: 生成钛金属饭盒（宽口）产品图



- 1. 从 by_product_type.food_jar.subtypes.wide_mouth 获取正面提示词

- 2. 从 by_material.titanium 获取材质提示词

- 3. 从 defect_prevention 获取缺陷预防提示词

- 4. 组合提示词：{product} + {material} + {defect_prevention}

- 5. 使用 (外部生图引擎)_presets.food_jar_wide_mouth 的工作流配置



**示例提示词**: `food jar, wide mouth, titanium body, anisotropic reflection, airtight lid, stackable design, no plastic texture, color accurate, product photography, pure white background`







---



## Phase 5.0: Memory Compression & Performance Optimization (OPTIMIZED in v5.0)



### A. 显存管理策略（优化版 - v5.0）



> [引用] 完整代码已提取到 `references\code_block_56.python`（38 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_56.python`（1496 字节）

> 需要查看完整代码时请读取该文件。









### B. 奖励机制（NEW in v5.0）



**核心思想**：当生成质量优秀时，奖励更多显存/更大batch size，加快后续生成速度。



> [引用] 完整代码已提取到 `references\code_block_57.python`（62 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_57.python`（2926 字节）

> 需要查看完整代码时请读取该文件。









### C. 显存碎片化整理机制（NEW in v5.0）



**问题**：长时间运行后，显存会出现碎片化（小块空闲显存无法被大tensor使用）。



**解决方案**：定期整理显存碎片。



> [引用] 完整代码已提取到 `references\code_block_58.python`（27 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_58.python`（1045 字节）

> 需要查看完整代码时请读取该文件。









**触发条件**（满足任一即触发）：

- 显存碎片化 > 30%

- 连续生成 > 20 张图像后

- 检测到 OOM 错误后

- 用户手动调用 `/vram_defrag` 命令



### D. 多模型并行加载的显存调度策略（NEW in v5.0）



**场景**：需要同时加载 Checkpoint + 多个 LoRA + 多个 ControlNet。



**策略**：按需加载 + 优先级调度。



> [引用] 完整代码已提取到 `references\code_block_59.python`（58 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_59.python`（2839 字节）

> 需要查看完整代码时请读取该文件。









### E. 性能监控（优化版 - v5.0）



> [引用] 完整代码已提取到 `references\code_block_60.python`（35 行）

> 需要查看时请读取该文件。



> 📄 完整代码见 `references/code_block_60.python`（1340 字节）

> 需要查看完整代码时请读取该文件。









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



### 能力优化后的ComfyUI API参数自动调优



🐵 猴在能力优化后，可调用ComfyUI API**自动调优生图参数**：



```python

import requests

import json



# ComfyUI API地址

COMFYUI_API = "http://127.0.0.1:8188"



def auto_tune_generation_params(workflow, target_metrics):

    """自动调优生图参数"""

    best_params = None

    best_score = 0

    

    # 参数搜索空间

    param_space = {

        "steps": [28, 32, 36],

        "cfg": [4.5, 5.5, 6.5],

        "denoise": [0.5, 0.6, 0.7]

    }

    

    # 网格搜索

    for steps in param_space["steps"]:

        for cfg in param_space["cfg"]:

            for denoise in param_space["denoise"]:

                # 1. 更新参数

                workflow["nodes"][5]["inputs"]["steps"] = steps

                workflow["nodes"][5]["inputs"]["cfg"] = cfg

                workflow["nodes"][5]["inputs"]["denoise"] = denoise

                

                # 2. 提交到ComfyUI API

                response = requests.post(f"{COMFYUI_API}/prompt", json={"prompt": workflow})

                task_id = response.json()["prompt_id"]

                

                # 3. 等待生成完成并评估

                # ... (评估逻辑)

                

                # 4. 记录最佳参数

                if score > best_score:

                    best_score = score

                    best_params = {"steps": steps, "cfg": cfg, "denoise": denoise}

    

    return best_params

```



**使用场景**：

- 自动找到最佳生图参数

- 针对不同产品类型优化参数

- 持续提升生图质量



---





---



#### Phase 6: 与⚙进化编排器联动（NEW in v7.0）



> **目标**: 接收⚙进化编排器的进化指令，自动优化Skill性能和质量



##### 6.1 接收进化指令



⚙进化编排器向🔧能力优化器发送标准化进化指令：



```json

{

  "evolution_id": "EVO-2026-0618-003",

  "source_agent": "⚙ 进化编排器 (进化编排)",

  "target_agent": "🐵 猴 (zheng10-skill-optimizer)",

  "timestamp": "2026-06-18T20:00:00+08:00",

  

  "evolution_type": "skill_optimization | parameter_tuning | workflow_improvement",

  

  "payload": {

    "target_skill": "产品设计",

    "optimization_goal": "提升Design2Prompt转换准确率",

    "current_score": 7.2,

    "target_score": 8.0,

    "constraints": ["保持兼容性", "不影响其他功能"]

  },

  

  "evolution_impact": {

    "affected_workflows": ["设计→生图→评审→调整"],

    "expected_improvement": "+0.8分",

    "risk_level": "LOW"

  }

}

```



##### 6.2 Skill自动优化流程



```

接收进化指令 → 分析目标Skill → 识别优化点 → 生成优化方案 → 

执行优化（A/B测试）→ 验证效果 → 提交优化报告 → ⚙进化编排器确认

```



**优化方法**：

1. **参数调优**：根据历史数据，找到最佳参数组合

2. **Prompt优化**：调整Skill中的Prompt模板，提升效果

3. **工作流优化**：简化冗余步骤，提升执行效率

4. **联动优化**：优化与其他Skill的联动逻辑



##### 6.3 优化效果验证



| 验证指标 | 优化前 | 优化后 | 提升 |

|----------|--------|--------|------|

| Skill评分 | 7.2/10 | 8.0/10 | +0.8 ✅ |

| 执行时间 | 5分钟 | 3分钟 | -40% ✅ |

| 联动成功率 | 85% | 95% | +10% ✅ |



---



### Phase 7: 与🐔鸡/🐵 猴联动（NEW in v7.0）



> **目标**: 根据评审结果和调整效果，持续优化Skill



##### 7.1 接收🐔鸡评审反馈



🐔鸡评审后，向🔧能力优化器发送评审数据分析：



```json

{

  "feedback_id": "FB-2026-0618-OPT-001",

  "source_agent": "🐔 鸡 (设计评审)",

  "target_agent": "🐵 猴 (zheng10-skill-optimizer)",

  "timestamp": "2026-06-18T20:30:00+08:00",

  

  "feedback_type": "review_analysis",

  

  "payload": {

    "avg_score": 7.2,

    "pass_rate": 0.4,

    "top_issues": [

      {"issue": "material_realism", "count": 8, "avg_score": 6.5},

      {"issue": "structure_accuracy", "count": 5, "avg_score": 7.0}

    ],

    "skill_optimization_suggestions": [

      "优化产品设计的Design2Prompt转换规则",

      "提升材质的Prompt关键词权重"

    ]

  }

}

```



##### 7.2 接收🐵 猴调整效果



🐵 猴调整后，向🔧能力优化器发送调整效果数据：



```json

{

  "feedback_id": "FB-2026-0618-OPT-002",

  "source_agent": "🐵 猴 (设计调整)",

  "target_agent": "🐵 猴 (zheng10-skill-optimizer)",

  "timestamp": "2026-06-18T21:00:00+08:00",

  

  "feedback_type": "adjustment_result",

  

  "payload": {

    "adjustment_success_rate": 0.85,

    "avg_score_improvement": 0.6,

    "top_improvement": [

      {"dimension": "material_realism", "improvement": 1.2},

      {"dimension": "lighting_quality", "improvement": 0.8}

    ],

    "skill_optimization_suggestions": [

      "优化设计调整的ACK重试逻辑",

      "提升调整效果追踪的完整度"

    ]

  }

}

```



##### 7.3 持续优化配置



🔧能力优化器根据🐔鸡和🐵 猴的反馈，**持续优化配置**：



| 优化周期 | 优化内容 | 触发条件 |

|----------|----------|----------|

| 每轮评审后 | 优化Prompt模板 | 🐔鸡评审平均分 <7.5 |

| 每次调整后 | 优化ACK重试逻辑 | 🐵 猴调整成功率 <85% |

| 每周 | 优化工作流 | 执行时间 >5分钟 |

| 每月 | 优化联动逻辑 | 联动成功率 <90% |



---



## 标准化反馈格式（向⚙进化编排器提交优化结果）



🔧能力优化器完成Skill优化后，向⚙进化编排器提交标准化反馈：



```json

{

  "feedback_id": "FB-2026-0618-OPT-003",

  "source_agent": "🐵 猴 (zheng10-skill-optimizer)",

  "target_agent": "⚙ 进化编排器 (进化编排)",

  "timestamp": "2026-06-18T21:30:00+08:00",

  

  "feedback_type": "skill_optimization_result",

  

  "payload": {

    "optimization_summary": "优化产品设计的Design2Prompt转换规则，增加材质关键词权重",

    "data_points": [

      {"metric": "Design2Prompt准确率", "before": 7.2, "after": 8.0, "improvement": +0.8},

      {"metric": "评审通过率", "before": 0.4, "after": 0.6, "improvement": +0.2},

      {"metric": "执行时间", "before": "5分钟", "after": "3分钟", "improvement": "-40%"}

    ],

    "optimization_details": "reports/optimization_20260618.json"

  },

  

  "evolution_impact": {

    "affected_skills": ["产品设计", "出图执行"],

    "suggested_next_action": "继续优化设计评审的评审准确性",

    "priority": "HIGH",

    "expected_overall_improvement": "+0.5分（整体评分）"

  }

}

```



---



## 联动规则总结



### 与⚙进化编排器（进化协调器）联动

- 接收：《进化指令》（含优化目标、当前评分、目标评分）

- 输出：《优化结果报告》（含优化方法、效果验证、下一步建议）

- 触发：⚙进化编排器发布进化决策后自动触发



### 与设计评审联动

- 接收：《评审数据分析》（含平均分、通过率、主要问题）

- 输出：《Skill优化建议》（含Prompt优化、参数调优）

- 触发：每次评审完成后自动触发



### 与🐵 设计调整联动

- 接收：《调整效果数据》（含成功率、评分提升、主要改善）

- 输出：《调整逻辑优化建议》（含ACK重试、效果追踪）

- 触发：每次调整完成后自动触发



---



## 质量标准（v7.0增强）



| 指标 | 目标值 | 验证方式 |

|------|--------|---------|

| Skill优化效果 | 评分提升≥0.5分 | 优化前后对比测试 |

| 优化执行时间 | <30分钟 | 从接收指令到提交报告 |

| 联动成功率 | ≥95% | ⚙进化编排器/🐔鸡/🐵 猴反馈 |

| 优化方案可行性 | ≥90% | A/B测试验证 |



---







### ComfyUI API集成



- **统一指南**: `<架构根目录>/docs/生肖团能力指南/十二生肖团_ComfyUI_API集成统一指南_V1.0_2026-06-18.md`

  - 所有API接口调用示例

  - 工作流JSON模板说明

  - 错误处理与性能优化



### 相关文档



| 文档 | 路径 | 说明 |

|------|------|------|

| ComfyUI安装指南 | `<架构根目录>/docs/生肖团能力指南/ComfyUI_安装与API化指南_V1.0_2026-06-18.md` | 安装与配置 |

| ComfyUI API调用指南 | `<架构根目录>/docs/生肖团能力指南/ComfyUI_工作流API调用指南_V1.0_2026-06-18.md` | 详细API文档 |

| ComfyUI工作流模板库 | `<架构根目录>/docs/生肖团能力指南/ComfyUI_工作流模板库_V2.0_2026-06-18.md` | 工作流模板 |

| 框架报告V8.0 | `<架构根目录>/docs/生肖团能力指南/十二生肖团_完整详细框架报告_V8.0_2026-06-18.md` | 最新框架 |



---



## Phase 6: 参数调优自动化与智能推荐 (NEW in v7.2)



### 6.1 参数调优自动化流程



**自动化调优流程**：

```

1. 接收调优任务（从🐔鸡/⚙进化编排器/用户）

2. 识别调优目标（提升评分、减少失败率、提升速度）

3. 生成参数调优空间（哪些参数需要调整）

4. 执行自动调优（网格搜索/随机搜索/贝叶斯优化）

5. 评估调优效果（对比调优前后指标）

6. 生成调优报告

7. 应用最优参数（或提示用户确认）

```



**调优目标与指标**：



| 调优目标 | 关键指标 | 目标值 |

|-----------|----------|--------|

| **提升生图质量** | 🐔鸡评审评分 | ≥8.0/10 |

| **减少生图失败** | 生图成功率 | ≥95% |

| **提升生图速度** | 平均推理时间 | ≤30s |

| **减少显存占用** | 显存占用率 | ≤80% |



### 6.2 智能参数推荐



**基于历史调优数据的推荐**：

- 采集历史调优记录（参数组合 + 效果）

- 训练推荐模型（机器学习/强化学习）

- 根据当前任务推荐最优参数组合

- 持续学习（每次调优后更新模型）



**推荐模型输入**：

```json

{

  "task_type": "产品图生成",

  "product_category": "保温杯",

  "style": "商务简约",

  "quality_requirement": "高",

  "history_optimization": [

    {"params": {"denoise": 0.7, "cfg_scale": 7.5}, "score": 8.2},

    {"params": {"denoise": 0.6, "cfg_scale": 8.0}, "score": 7.8}

  ]

}

```



**推荐模型输出**：

```json

{

  "recommended_params": {

    "denoise": 0.7,

    "cfg_scale": 6.0,

    "steps": 32,

    "sampler": "DPM++ 2M SDE Karras"

  },

  "expected_score": 8.3,

  "confidence": 0.85

}

```



### 6.3 与十二生肖团其他Agent的联动



**联动链1：🐔→⚙ 本工具→🐑（评审→调优→生图）**

```

🐔评审完成 → 识别需要调优的参数

→ 本工具进行参数调优

→ ⚙ 调优完成 → 调用🐑使用新参数生图

→ 🐑完成 → 🐔重新评审

→ 验证调优效果

```



**联动链2：⚙ 本工具→🐴→⚙进化编排（调优→ComfyUI→进化）**

```

本工具生成调优参数 → 调用🐴更新ComfyUI工作流

→ 🐴完成 → 调用⚙记录进化数据

→ ⚙分析进化效果

→ 生成进化报告

```



**联动链3：⚙ 本工具→调优→设计调整**

```

本工具识别设计调整需要调优的参数

→ 交由🐵猴执行设计调整

→ 🐵猴完成 → 本工具评估调整效果

→ 生成调整参数优化建议

```



### 6.4 调优效果自动评估



**评估指标**：

- 评分提升（🐔鸡评审评分 before vs after）

- 成功率提升（生图成功率 before vs after）

- 速度提升（推理时间 before vs after）

- 显存占用降低（显存占用率 before vs after）



**自动评估流程**：

```

1. 调优前基线测试（生图10次，记录指标）

2. 应用调优参数

3. 调优后测试（生图10次，记录指标）

4. 对比分析（计算提升百分比）

5. 生成评估报告

6. 决策（如果提升>5%，则应用新参数；否则回滚）

```



**评估报告格式**：

```json

{

  "optimization_id": "OPT-2026-0619-001",

  "before": {

    "score": 7.5,

    "success_rate": 0.85,

    "avg_time": 35.2,

    "vram_usage": 0.88

  },

  "after": {

    "score": 8.1,

    "success_rate": 0.93,

    "avg_time": 28.7,

    "vram_usage": 0.76

  },

  "improvement": {

    "score": "+0.6 (+8.0%)",

    "success_rate": "+0.08 (+9.4%)",

    "avg_time": "-6.5s (-18.5%)",

    "vram_usage": "-0.12 (-13.6%)"

  },

  "decision": "应用新参数",

  "confidence": 0.92

}

```



### 6.5 参数调优知识库



**知识库内容**：

- 历史调优记录（参数组合 + 效果）

- 最优参数组合（按任务类型分类）

- 调优失败案例（避免重复错误）

- 调优最佳实践（经验总结）



**知识库更新流程**：

```

1. 每次调优完成后 → 记录调优数据

2. 定期分析调优数据 → 提取最佳实践

3. 更新知识库 → 新增/修改/删除条目

4. 知识库版本管理 → 记录每次更新

```



**知识库查询**：

- 根据任务类型查询最优参数

- 根据产品类别查询推荐参数

- 根据历史失败案例查询避免策略



---



## 参考资料



### ComfyUI API集成



## 产出写通用互通总线（资料总线）



完成本角色产出后，**必须**写入生肖团通用互通总线，使下游职能按静态联动映射表秒级收到事件通知（替代被动轮询）。



```bash

node 资料总线/zodiac_bus.js --emit \

  --role monkey --type param --product <产品名> --ref param_<id> \

  --content '{"summary":"产出摘要","files":["<产出文件路径>"]}'

```



- **开工前先查信箱**感知上游通知（连接反应更迅速）：

  `node 资料总线/zodiac_bus.js --inbox --role monkey --pending-only`

- 处理完标记已读：`node 资料总线/zodiac_bus.js --mark-done --role monkey --id <事件id>`

- 联动映射（谁 emit → 通知谁）见 `<架构根目录>/logs/zodiac_bus_map.json`，改联动只改该表。

- 总线协议与 schema 见 `资料总线/SKILL.md` 与 `<架构根目录>/logs/zodiac_bus_schema.md`。



---



## v5.0 保温杯出图提示词资产吸收（采样参数推荐）



> 统一源：`references/thermos_prompt_assets_v5.md`

> 本技能（元层·参数调优）吸收其「四 采样参数」，作为生图参数推荐的**已验证真值基线**。



### 已验证采样参数（资产第四节，实机验证于工作台 V6.2026.0814.0002）

| 参数 | 推荐值 | 反例（曾踩坑） |

|---|---|---|

| 采样器 | `DPM++ 2M SDE Karras` | 非 `Euler a` |

| Steps | **28–36** | 非 85（过度采样无收益） |

| CFG | **4.5–6.5** | 非 8.0（偏高→过饱和/伪影） |

| IPAdapter 权重 | 0.5–0.7 | — |

| ControlNet(Canny/Depth) | 0.6–0.8 | — |



### ✅ 已校准（v5.0 统一吸收）

`Phase 1` 参数调优参考表、自动调优搜索空间 `param_space`（steps 已改 [28,32,36] / cfg [4.5,5.5,6.5]）、`Phase 6` 推荐输出（cfg_scale 7.5→6.0、steps 30→32、sampler→`DPM++ 2M SDE Karras`）均已对齐中央资产已验证真值（steps 28–36 / CFG 4.5–6.5）。历史高分案例库（`cfg_scale: 7.5/8.0`）为校准前实测记录，保留作对照，新推荐一律走真值区间。漂移已消除。



---



---



---



---



## 📚 资料总线（H 盘资料入口）



> 本技能可读的 H 盘资料已登记在**资料总线**，开工前先查一遍 —— 避免"重复造轮子"和"翻不到料"。



```bash

python <本地资源路径> --role skill-optimizer

python <本地资源路径> --kw <关键词>      # 元数据层：找「有哪些资料」

python <本地资源路径> --wb             # 工作台可挂载的料

python <本地资源路径> "一句话需求"    # 语义层：在 1.2 万篇业务库正文里找「哪一段」

python <本地资源路径> --role skill-optimizer "..."  # 限定本角色的资料范围内检索

```



**全量索引**：`<本地资源路径>` ｜ **清单**：`<本地资源路径>`



| 资料 | 路径 | 体量 | 用途 |

|---|---|---|---|

| `asset.scripts` | `<本地资源路径>` | 8.60 GB | 脚本 / 工具 |

| `asset.study` | `<本地资源路径>` | 53.98 GB | 学习 / 课程 |

| `asset.tutorial` | `<本地资源路径>` | 6.82 GB | 教程 / ComfyUI |



**硬数据优先**：凡涉及国标限值、材料参数、专利红线、竞品价格，**必须以本总线登记的真实文件为准**，不得凭记忆作答。



**出图/交付**：32 个标准提示词模板见 `<本地资源路径>`（结构化索引 `prompt_templates.json`，含分类/变量/正文/示例）。



> 两个入口分工：`lookup.py` 查**目录元数据**（有哪些资料、多大、谁能用）；`core_lookup.py` 查**内容语义**（哪份文件的哪一段讲了这件事）。



<!-- 资料总线区块结束 -->

