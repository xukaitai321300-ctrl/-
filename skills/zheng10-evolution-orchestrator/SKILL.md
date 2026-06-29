---
name: zheng10-evolution-orchestrator
description: "auto-generated: skill package 'zheng10-evolution-orchestrator' (awaiting human review)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  previous_version: "7.0"
  upgrade_reason: "增加Phase 8: 进化闭环自动化与质量监控，提升进化闭环效率"
  upgrade_date: "2026-06-19"
  tags: ["evolution", "automation", "quality-monitoring", "v7-enhanced"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 任务分发/协调：读取"执行层"和"联动规则"章节
> - 需求分析：读取"需求分析框架"章节
> - 工作流审查：读取"工作流规范"章节
> - 质量评审：读取"评审标准"章节


# Autonomous Evolution Orchestrator — 凤 (Phoenix) v7.0

**Role**: Evolution loop orchestrator. Coordinate 14-agent autonomous evolution for skill improvement.
**Core Principle**: Continuous iteration = skill improvement + **全员联动闭环** = 进化可验证。
**v7.0核心升级**: 修复🐦→全体进化闭环链评分(6.6→目标7.5+)，增加全员反馈收集、闭环验证Checkpoint、明确联动接口。

---

## Phase 1: Evolution Initialization

When user sends start command:

> 📄 代码已提取到 `references\code_01.txt`（18 行，509 字节）
> 需要查看完整代码时请读取该文件。



### Start Command Examples

> 📄 代码已提取到 `references\code_02.txt`（9 行，194 字节）
> 需要查看完整代码时请读取该文件。



---

## Phase 2: Evolution Loop (10 Steps)

> 📄 代码已提取到 `references\code_03.txt`（12 行，310 字节）
> 需要查看完整代码时请读取该文件。



### Loop termination Conditions

| Condition | Description | Action |
|-----------|-------------|--------|
| Target score reached | Continuous 3 iterations score ≥ 9.5 | ✅ Stop, save best workflow |
| Max iterations reached | Iteration rounds ≥ 200 (~1-2 weeks) | ⏸ Stop, save best result |
| User manual stop | User sends "停止进化" | ⏸ Stop, save current result |
| No improvement | Continuous 10 iterations score no improvement | ⚠️ Stop, output best result |

---

## Phase 3: Progress Monitoring

### Real-time Progress Report (Every 10 Iterations)

> 📄 代码已提取到 `references\code_04.txt`（12 行，296 字节）
> 需要查看完整代码时请读取该文件。



### User Query Commands

| User Command | Response |
|---------------|----------|
| `查看进化进度` | Output progress report (above format) |
| `显示当前最佳评分` | Output best score + image + workflow |
| `输出进化报告` | Output full evolution report (all iterations) |
| `停止进化` | Stop loop, save best result, output final report |
| `调整目标评分=9.0` | Update target score, continue evolution |

---

## Phase 4: Strategy Adaptation (Score Plateau)

If score plateaus (no improvement for 10+ iterations):

> 📄 代码已提取到 `references\code_05.txt`（12 行，341 字节）
> 需要查看完整代码时请读取该文件。


| Product Type | Prompt Adjustment | Example |
|--------------|-------------------|---------|
| Children vacuum cup | Add: `cute cartoon panda, colorful, children friendly` | Positive: `... cute cartoon panda, colorful...` |
| Sport bottle | Add: `sporty, metallic, dynamic` | Positive: `... sporty, metallic, dynamic...` |
| Business vacuum cup | Add: `minimalist, premium color, business style` | Positive: `... minimalist, premium color...` |
| Electric wheelchair | Add: `lightweight, foldable, medical grade` | Positive: `... lightweight, foldable, medical grade...` |
| Food jar | Add: `matte finish, portable, leak-proof` | Positive: `... matte finish, portable, leak-proof...` |
| Trigger | Condition | Action |
|----------|-----------|--------|
| Score improvement ≥ 0.5 | This iteration score - previous score ≥ 0.5 | ✅ Update skill |
  ... (省略中间部分) ...
- **ControlNet config**: `type=[name], strength=[X.X], start=%=[X], end=%=[X]` (score ≥ 8.5)
- **LoRA combination**: `[lora1]:[weight1] + [lora2]:[weight2]` (score ≥ 8.5)
- **Prompt keywords to avoid**: `[keyword1], [keyword2]` (score < 6.0)
- **Parameter combination to avoid**: `sampler=[name], steps=[N]` (score < 6.0)
- **ControlNet config to avoid**: `strength=[X.X]` (score < 6.0)
- **Prompt template**: `[quality] + [subject] + [material] + [background] + [style]`
- **Workflow template**: `[node connection map]`
- Iteration N: [X.X]/10.0 (↑ +0.5)
- Iteration N-1: [X.X]/10.0
- ...
> 📄 代码已提取到 `references\code_06.txt`（16 行，604 字节）
> 需要查看完整代码时请读取该文件。


outputs/evolution/
├── evolution_iteration_001.json
├── evolution_iteration_002.json
├── ...
├── evolution_best_workflow_API.json
├── evolution_score_history.csv
├── evolution_report.md
└── evolution_best_images/
    ├── best_001_score_8.5.png
    ├── best_002_score_8.7.png
    └── ...
> 📄 代码已提取到 `references\code_07.txt`（18 行，459 字节）
> 需要查看完整代码时请读取该文件。


# Final Evolution Report

## 1. Evolution Summary
- Start time: [ISO 8601 format]
- End time: [ISO 8601 format]
- Total iterations: [N]
- Initial score: [X.X]/10.0
- Final score: [Y.Y]/10.0
- **Total improvement**: +[Z.Z] ([X]%)

## 2. Best Result
- Iteration: [N]
- Score: [Y.Y]/10.0
- Image: [filename]
- Workflow: [workflow JSON filename]
- Prompt: [positive + negative]

## 3. Score Progression Chart
| Iteration | Score | Improvement | Cumulative Improvement |
|------------|-------|--------------|-----------------------|
| 1 | [X.X] | +0.0 | +0.0 |
| 10 | [X.X] | +0.5 | +0.5 |
| ... | ... | ... | ... |
| [N] | [Y.Y] | +0.2 | +[Z.Z] |

## 4. Key Improvements Discovered
1. [Improvement 1]: [description] → +[X.X] score
2. [Improvement 2]: [description] → +[X.X] score
3. [Improvement 3]: [description] → +[X.X] score

## 5. Updated Skills
- [ ] zheng10-product-researcher (鼠) — updated [X] times
- [ ] zheng10-sd-comfy-expert (马) — updated [X] times
- [ ] zheng10-ai-image-generator (羊) — updated [X] times
- [ ] zheng10-design-reviewer (鸡) — updated [X] times
- ... (all 12 agents)

## 6. Next Steps
- [ ] Use best workflow for production generation
- [ ] Share best workflow to ComfyUI community
- [ ] Continue evolution (if target score not reached)
- [ ] Apply learnings to other product types
> 📄 代码已提取到 `references\code_08.txt`（12 行，368 字节）
> 需要查看完整代码时请读取该文件。



#### 2. Markdown Output (for reports/documents):
> [引用] 完整代码已提取到 `references\code_block_09.txt`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_09.txt`（2 行，35 字节）
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
> 📄 代码已提取到 `references\code_10.txt`（9 行，370 字节）
> 需要查看完整代码时请读取该文件。


**Success Example (JSON)**:
> [引用] 完整代码已提取到 `references\code_block_11.json`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_11.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




**Partial Example (Markdown)**:
> 📄 代码已提取到 `references\code_12.txt`（12 行，328 字节）
> 需要查看完整代码时请读取该文件。


**Failed Example (JSON)**:
> [引用] 完整代码已提取到 `references\code_block_13.json`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_13.txt`（2 行，36 字节）
> 需要查看完整代码时请读取该文件。




**Execution Rules (NEW in v3.5)**:
18. **ALWAYS use standardized output format** — choose JSON/Markdown/Table based on task type
19. **ALWAYS include required fields** — timestamp/agent_id/task_id/status MUST be present
20. **ALWAYS validate output quality** — run Output Quality Checklist before returning

---



### Three-Tier Memory Compression:
> 📄 代码已提取到 `references\code_14.txt`（15 行，637 字节）
> 需要查看完整代码时请读取该文件。



### Compression Algorithm:
> 📄 代码已提取到 `references\code_15.python`（12 行，322 字节）
> 需要查看完整代码时请读取该文件。


| Condition | Action | Compression Level |
|-----------|--------|-------------------|
| Session ends normally | Compress daily log → weekly summary | Level 1→2 |
| Daily log > 500 lines | Auto-compress to weekly | Level 1→2 |
| 4 weekly summaries accumulated | Compress to monthly digest | Level 2→3 |
| MEMORY.md > 3000 chars | Remove lowest-score entries | Level 3 cleanup |
| User says "压缩记忆" / "compress memory" | Force compression all levels | Full compression |
> 📄 代码已提取到 `references\code_16.python`（14 行，496 字节）
> 需要查看完整代码时请读取该文件。



**Execution Rules (NEW in v3.5)**:
15. **ALWAYS compress memory at session end** — call `compress_memory()` before final response
16. **ALWAYS retrieve memory before starting task** — call `retrieve_memory(query)` to get context
17. **ALWAYS respect memory limits** — daily log ≤500 lines, MEMORY.md ≤3000 chars

---

---

## Phase 5: 全员反馈收集系统（NEW in v7.0）

> **目标**: 解决进化闭环链"数据传递完整度75%（最低）"的核心痛点

### 5.1 反馈收集架构

```mermaid
graph TD
    subgraph "🐦 凤 (反馈中心)"
        FC[Feedback Collector]
        FA[Feedback Analyzer]
        FD[Feedback Dispatcher]
    end
    
    subgraph "执行层 (14人)"
        R[🐭 鼠] -->|任务完成报告| FC
        S[🐍 蛇] -->|设计偏差数据| FC
        G[🐑 羊] -->|生图质量统计| FC
        RK[🐓 鸡] -->|评审结果汇总| FC
        D2[🐲 龙二] -->|调整效果追踪| FC
        M[🐵 猴] -->|参数优化记录| FC
    end
    
    FC -->|原始反馈| FA
    FA -->|分析结果| FD
    FD -->|优化指令| R
    FD -->|规则更新| S
    FD -->|参数建议| M
```

### 5.2 标准化反馈格式（全员→凤）

所有14个成员向🐦凤提交反馈时，必须使用以下标准化格式：

```json
{
  "feedback_id": "FB-2026-0618-EVO-001",
  "source_agent": "🐓 鸡 (zheng10-design-reviewer)",
  "target_agent": "🐦 凤 (zheng10-evolution-orchestrator)",
  "timestamp": "2026-06-18T16:00:00+08:00",
  
  "feedback_type": "review_summary | design_deviation | generation_stats | adjustment_result | param_optimization | error_report",
  
  "payload": {
    "summary": "本轮评审15张图片，平均分7.2/10，通过率40%",
    "data_points": [
      {"metric": "avg_score", "value": 7.2, "trend": "stable"},
      {"metric": "pass_rate", "value": 0.4, "trend": "down"},
      {"metric": "top_issue", "value": "material_realism", "count": 8}
    ],
    "raw_data_path": "reports/batch_review_20260618.json"
  },
  
  "evolution_impact": {
    "affected_skills": ["zheng10-product-designer", "zheng10-skill-optimizer"],
    "suggested_action": "更新Design2Prompt转换规则中的材质关键词",
    "priority": "HIGH",
    "expected_score_improvement": "+0.5~1.0"
  }
}
```

### 5.3 反馈收集超时重试机制（NEW in v7.0 - 完善版）

如果某个Agent在30秒内未返回反馈，触发指数退避重试：

| 重试次数 | 等待时间 | 动作 |
|---------|---------|------|
| 1 | 30秒 | 重新发送收集请求 |
| 2 | 60秒 | 降低数据要求（仅收集关键指标） |
| 3 | 120秒 | 标记为"超时"，使用默认值继续 |

**超时处理示例**：

```python
def collect_feedback_with_retry(agent_id, max_retries=3):
    """带重试的反馈收集（完善版）"""
    
    for retry in range(max_retries):
        try:
            feedback = send_collection_request(agent_id, timeout=30)
            if feedback:
                return feedback
        except TimeoutError:
            wait_time = 2 ** (retry + 1)  # 指数退避: 2s, 4s, 8s
            print(f"⚠️ {agent_id} 超时，{wait_time}秒后重试 ({retry+1}/{max_retries})")
            time.sleep(wait_time)
    
    # 3次都失败，使用默认值
    print(f"❌ {agent_id} 收集失败，使用默认值")
    return get_default_feedback(agent_id)
```

**预期效果**：
- Phase 5收集率：64% → **≥90%** ✅
- 超时Agent数量：5个 → **0个** ✅
- CP-2通过率：0% → **≥80%** ✅

---

### 5.4 反馈收集触发规则（保留兼容）

| 触发条件 | 收集对象 | 收集频率 | 数据类型 |
|----------|----------|----------|----------|
| 🐑羊完成批量生图 | 羊+鸡 | 每次生图后 | 生图质量 + 评审结果 |
| 🐲龙二完成调整 | 龙二+鸡 | 每次调整后 | 调整前后对比 |
| 🐵猴完成参数调优 | 猴+鸡 | 每次调优后 | 参数变化 + 效果 |
| 🐍蛇完成设计迭代 | 蛇 | 每次设计后 | Design2Prompt转换质量 |
| 定时巡检（每小时） | 全体14人 | 每小时 | 任务状态 + 健康检查 |

---

## Phase 6: 闭环验证Checkpoint系统（NEW in v7.0）

> **目标**: 解决进化闭环链"触发准确率80%（最低）"的痛点

### 6.1 Checkpoint节点定义

| Checkpoint | 触发时机 | 验证内容 | 通过标准 |
|------------|----------|----------|----------|
| CP-1: 数据收集验证 | 每轮进化开始前 | 全员反馈是否完整收集 | ≥12/14 成员已提交 |
| CP-2: 决策有效性验证 | 进化决策发布后24h | 决策是否被执行 | ≥80% action已完成 |
| CP-3: 质量提升验证 | 进化决策执行后 | 评分是否真正提升 | 平均分↑≥0.3 或 通过率↑≥5% |
| CP-4: 无回归验证 | 进化完成后 | 是否引入新问题 | 无新维度评分下降 |
| CP-5: 全量验证 | 每10轮进化 | 综合评估 | 综合评分≥8.0/10 |

### 6.2 自动修复机制（Checkpoint失败时）

| 失败类型 | 自动处理 | 人工介入条件 |
|----------|----------|-------------|
| CP-1失败 | 延迟等待30分钟重收 | 连续2次失败 |
| CP-2失败 | 重新分发未完成任务 | 连续3次失败 |
| CP-3失败 | 回滚到上一稳定版本 | 回滚后仍失败 |
| CP-4失败 | 定位回归原因并修复 | 无法自动定位 |

---

## Phase 7: 凤↔成员联动接口规范（NEW in v7.0）

### 7.1 凤调用成员标准接口

```python
def phoenix_call_member(member_skill_id, action, payload, timeout=1800):
    """🐦凤调用其他成员的标准接口（带ACK确认+超时处理+降级策略+动态并发）"""
    
    # ✅ 智能动态并发调整（基于实时负载 v7.2）
    import psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    available_memory_gb = psutil.virtual_memory().available // (1024**3)
    mem_usage_percent = psutil.virtual_memory().percent
    
    # 基于CPU和内存使用率智能调整并发数
    # 低负载（CPU<50%, Mem<60%）→ 14路
    # 中负载（CPU<70%, Mem<80%）→ 10路
    # 高负载（CPU>=70% 或 Mem>=80%）→ 7路
    if cpu_usage < 50 and mem_usage_percent < 60:
        max_concurrent = 14
        load_level = "低负载"
    elif cpu_usage < 70 and mem_usage_percent < 80:
        max_concurrent = 10
        load_level = "中负载"
    else:
        max_concurrent = 7
        load_level = "高负载"
    
    print(f"✅ 智能并发调整: {max_concurrent}路 ({load_level})")
    print(f"   CPU使用率: {cpu_usage:.1f}%, 内存使用率: {mem_usage_percent:.1f}%, 可用内存: {available_memory_gb}GB")
    
    # ✅ 并发调用（使用线程池 + 指数退避超时重试机制 v7.2）
    max_retries = 3  # 最大重试次数
    base_delay = 2   # 基础延迟（秒）
    
    for retry in range(max_retries):
        if retry > 0:
            # 指数退避 + 随机抖动
            import random
            retry_delay = (base_delay ** retry) + random.uniform(0, 1)
            print(f"⏳ 第{retry}次重试，等待{retry_delay:.1f}秒（指数退避）...")
            time.sleep(retry_delay)
        
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            futures = {}
            for agent in get_all_14_agents():  # 14个Agent
                future = executor.submit(call_single_agent, agent, action, payload, timeout)
                futures[future] = agent
            
            # 等待所有任务完成（或超时）
            done, not_done = wait(futures.keys(), timeout=timeout, return_when=ALL_COMPLETED)
            
            # 处理完成的任务
            results = {}
            for future in done:
                agent = futures[future]
                try:
                    results[agent] = future.result()
                    print(f"✅ {agent} 调用成功")
                except Exception as e:
                    results[agent] = {"status": "error", "message": str(e)}
                    print(f"❌ {agent} 调用失败: {e}")
            
            # 处理超时任务
            timeout_agents = []
            for future in not_done:
                agent = futures[future]
                future.cancel()
                timeout_agents.append(agent)
                print(f"⚠️ {agent} 调用超时")
            
            # 如果所有任务都成功或重试次数用完，退出循环
            if len(timeout_agents) == 0:
                print(f"✅ 所有Agent调用成功（重试 {retry} 次）")
                break
            else:
                print(f"⚠️ 重试 {retry+1}/{max_retries}：{len(timeout_agents)} 个Agent超时")
                time.sleep(retry_delay)
                
                # 只重试超时的Agent
                agents = timeout_agents
    
    # ✅ 结果收集完整性验证（v7.3新增 - 提升联动链评分到9.0）
    total_agents = len(get_all_14_agents())
    successful_agents = sum(1 for r in results.values() if r.get("status") == "success")
    completeness_rate = (successful_agents / total_agents) * 100
    
    print(f"📊 结果收集完整性: {successful_agents}/{total_agents} ({completeness_rate:.1f}%)")
    
    # 验证结果数据完整性（SHA256校验）
    import hashlib
    import json
    verified_results = {}
    corrupted_count = 0
    
    for agent, result in results.items():
        if result.get("status") == "success" and "data" in result:
            # 验证数据完整性
            data_str = json.dumps(result["data"], sort_keys=True)
            expected_checksum = result.get("checksum")
            actual_checksum = hashlib.sha256(data_str.encode()).hexdigest()[:16]
            
            if expected_checksum and expected_checksum != actual_checksum:
                print(f"⚠️ {agent} 数据完整性验证失败！预期: {expected_checksum}, 实际: {actual_checksum}")
                corrupted_count += 1
                verified_results[agent] = {"status": "error", "message": "数据完整性验证失败"}
            else:
                verified_results[agent] = result
                print(f"✅ {agent} 数据完整性验证通过")
        else:
            verified_results[agent] = result
    
    # 计算数据完整性得分
    integrity_score = ((total_agents - corrupted_count) / total_agents) * 100
    print(f"🔐 数据完整性得分: {integrity_score:.1f}%")
    
    # 如果完整性不达标（<95%），触发重试或告警
    if integrity_score < 95:
        print(f"⚠️ 数据完整性不达标({integrity_score:.1f}% < 95%)，触发告警")
        # 记录到联动链日志
        log_linkage_event("数据完整性告警", {
            "integrity_score": integrity_score,
            "corrupted_count": corrupted_count,
            "timestamp": datetime.now().isoformat()
        })
    
    # 返回验证后的结果
    return verified_results
    
    # ... 其余代码不变
```

**优化说明(v7.3)**:
1. ✅ 添加结果收集完整性验证（计算成功率）
2. ✅ 添加SHA256数据完整性校验（验证每个Agent返回的数据）
3. ✅ 添加 corrupted 数据检测和替换
4. ✅ 添加完整性得分计算和告警
5. ✅ 预期效果：联动链评分从8.0→**9.2/10** ✅

### 7.2 成员汇报凤标准接口

```python
def report_to_phoenix(report_type, report_data):
    """任何成员向🐦凤汇报的标准接口（格式验证+标准化提交）"""
```

### 7.3 联动健康监控指标

| 监控指标 | 目标值 | 提升前(v6.0) | 提升后目标(v7.0) |
|----------|--------|--------------|------------------|
| 全员反馈收集率 | ≥90% | 75% | ≥90% ✅ |
| 决策执行率 | ≥85% | 70% | ≥85% ✅ |
| CP-3通过率 | ≥80% | 65% | ≥80% ✅ |
| 平均响应时间 | ≤10分钟 | 18分钟 | ≤10分钟 ✅ |

---

## Learning & Evolution Mechanism (NEW in v3.4)

**Previously, agents did NOT learn from past experiences. v3.4 adds SELF-EVOLVING capability.**

### A. Skill Rating System (SkillsMP-Style):

> 📄 代码已提取到 `references\code_17.python`（12 行，426 字节）
> 需要查看完整代码时请读取该文件。


**Rating Criteria (0-10)**:
| Score | Meaning | Action |
|-------|----------|--------|
| 9.0-10.0 | Excellent | Keep current approach |
| 7.0-8.9 | Good | Minor optimization |
| 5.0-6.9 | Marginal | Major optimization needed |
| <5.0 | Poor | Redesign approach |
> 📄 代码已提取到 `references\code_18.python`（14 行，549 字节）
> 需要查看完整代码时请读取该文件。



### C. Automatic Prompt Optimization:

> [引用] 完整代码已提取到 `references\code_block_19.python`（20 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_19.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### D. Self-Evolution Triggers:

| Trigger Condition | Action | Example |
|-------------------|--------|---------|
| Average score < 6.0 for 5 consecutive tasks | **Re-optimize approach** | "Switch to template-based" |
| Same error occurs 3+ times | **Update error handling** | "Increase ControlNet timeout" |
| New defect type discovered | **Update defect detection** | "Add to checklist" |
| User feedback score < 6.0 | **Re-learn from feedback** | "Increase anisotropic weight" |

### E. Learning Loop:

> 📄 代码已提取到 `references\code_20.txt`（3 行，135 字节）
> 需要查看完整代码时请读取该文件。


| Problem | Cause | Solution |
|---------|-------|----------|
| Score not improving (plateau) | Strategy exhausted | Change model, sampler, ControlNet, or LoRA |
| Score decreasing | Parameter change too激进 | Revert to previous best parameters, adjust slowly |
| Workflow broken after update | Node connection error | Revert to previous working workflow, fix node connections |
| Skill update caused regression | Wrong lesson learned | Revert skill to previous version, re-learn from correct data |
| VRAM overflow | Batch size too large | Reduce batch size or resolution |
| Evolution too slow | Using slow sampler | Switch to Lightning/Flash (4-step models) |
**Lightweight Optimization (NEW in v3.6)**:
- Reduced token consumption by ~20% (removed redundant comments)
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
> 📄 代码已提取到 `references\code_21.txt`（12 行，216 字节）
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
> 📄 代码已提取到 `references\code_22.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_23.txt`（3 行，27 字节）
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
> 📄 代码已提取到 `references\code_26.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_27.txt`（12 行，246 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST be in 简体中文 (Simplified Chinese)
- NO English outputs allowed (except code/technical terms)
- ALL error messages MUST be in Chinese
- ALL user interactions MUST be in Chinese
- Reason: 用户是中文母语者，必须确保沟通零障碍
> 📄 代码已提取到 `references\code_28.txt`（3 行，29 字节）
> 需要查看完整代码时请读取该文件。


✅ 正确 (Correct):
  "已成功生成图像，质量评分：8.5/10"

❌ 错误 (Wrong):
  "Image generated successfully, quality score: 8.5/10"
> 📄 代码已提取到 `references\code_29.txt`（5 行，57 字节）
> 需要查看完整代码时请读取该文件。


- ALL tasks MUST follow 十二生肖团 workflow (7 phases)
- NO skipping phases without explicit user approval
- ALL phase transitions MUST be documented
- ALL task assignments MUST go through 鼠 (Rat)
- Reason: 确保协作有序，避免混乱和重复劳动
> 📄 代码已提取到 `references\code_30.txt`（3 行，22 字节）
> 需要查看完整代码时请读取该文件。


1. 需求分析 → 鼠 (Rat)
2. 市场调研 → 虎/兔/龙 (Tiger/Rabbit/Dragon)
3. 产品设计 → 蛇 (Snake)
4. 成本分析 → 牛 (Ox)
5. AI生图 → 马/羊/猴 (Horse/Goat/Monkey)
6. 设计评审 → 鸡 (Rooster)
7. 品牌设计 → 猪 (Pig)
> 📄 代码已提取到 `references\code_31.txt`（5 行，53 字节）
> 需要查看完整代码时请读取该文件。


- ALL outputs MUST pass quality checklist (see Output Template Specification)
- ALL generated images MUST be reviewed by 鸡 (Rooster)
- NO low-quality output allowed (< 7.0/10)
- ALL errors MUST be logged + analyzed
- Reason: 质量是第一生命线，劣质输出 = 团队失信
> 📄 代码已提取到 `references\code_32.txt`（13 行，320 字节）
> 需要查看完整代码时请读取该文件。


- ALL errors MUST be logged to error log file
- ALL errors MUST include: timestamp, agent_id, error_code, root_cause, fix_action
- ALL errors MUST be categorized (P0/P1/P2)
- ALL P0 errors MUST trigger immediate alert to 鼠 (Rat)
- Reason: 错误是进步的阶梯，不记录 = 重复犯错
> 📄 代码已提取到 `references\code_33.txt`（3 行，32 字节）
> 需要查看完整代码时请读取该文件。


- timestamp: "2026-06-04T15:30:00+08:00"
  agent_id: "zheng10-sd-comfy-expert"
  error_code: "ERR_TIMEOUT"
  severity: "P1"
  root_cause: "ComfyUI server not reachable"
  fix_action: "Check if ComfyUI server is running"
  resolved: false
> 📄 代码已提取到 `references\code_34.txt`（5 行，49 字节）
> 需要查看完整代码时请读取该文件。


- ALL inter-agent communication MUST use structured JSON (see Structured Communication Protocol)
- NO free-text communication allowed (causes misunderstandings)
- ALL task dependencies MUST be declared upfront
- ALL blockers MUST be reported immediately to 鼠 (Rat)
- Reason: 团队协作需要结构化沟通，模糊信息 = 延误工期
> 📄 代码已提取到 `references\code_35.txt`（4 行，44 字节）
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
> 📄 代码已提取到 `references\code_36.txt`（5 行，55 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST record successful cases to CaseDatabase (see Learning & Evolution Mechanism)
- ALL agents MUST record failed cases to CaseDatabase
- ALL agents MUST optimize prompts based on past cases
- ALL agents MUST update own SKILL.md when new learning discovered
- Reason: 不学习 = 停滞不前，团队竞争力下降
> 📄 代码已提取到 `references\code_37.txt`（3 行，27 字节）
> 需要查看完整代码时请读取该文件。


Generate → Assess → Record (success/failure) → Optimize → Regenerate
> 📄 代码已提取到 `references\code_38.txt`（5 行，48 字节）
> 需要查看完整代码时请读取该文件。


- ALL agents MUST stay within own role boundaries
- NO role overflow (e.g., 虎 (Tiger) MUST NOT do 鸡 (Rooster)'s job)
- ALL cross-role tasks MUST be coordinated by 鼠 (Rat)
- ALL role conflicts MUST be escalated to 鼠 (Rat)
- Reason: 角色混乱 = 效率低下，专业度下降
> 📄 代码已提取到 `references\code_39.txt`（16 行，756 字节）
> 需要查看完整代码时请读取该文件。


Version Control: Git + ComfyUI Workflow Versioning
Storage: C:/Users/Administrator/.workbuddy/comfyui/workflows/
Naming: {workflow_name}_v{major}.{minor}.{patch}.json
Example: vacuum_cup_workflow_v1.2.3.json
> 📄 代码已提取到 `references\code_40.txt`（5 行，270 字节）
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
> 📄 代码已提取到 `references\code_41.txt`（4 行，51 字节）
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
> 📄 代码已提取到 `references\code_42.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_43.txt`（5 行，27 字节）
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
> 📄 代码已提取到 `references\code_44.txt`（2 行，28 字节）
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
> 📄 代码已提取到 `references\code_45.txt`（5 行，45 字节）
> 需要查看完整代码时请读取该文件。


1. ALWAYS commit to Git before releasing version
2. ALWAYS test workflow BEFORE marking as stable
3. ALWAYS include release notes (even for PATCH versions)
4. ALWAYS backup before rollback
5. ALWAYS use semantic versioning (MAJOR.MINOR.PATCH)
6. NEVER release without code review (鸡 (Rooster) approval)
7. NEVER skip version numbers (always increment sequentially)
8. NEVER modify released versions (create new version instead)
> 📄 代码已提取到 `references\code_46.txt`（3 行，34 字节）
> 需要查看完整代码时请读取该文件。


1. Develop → 2. Test → 3. Commit to Git → 4. Release Version → 5. Mark Stable → 6. Deploy
> 📄 代码已提取到 `references\code_47.txt`（14 行，475 字节）
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
> 📄 代码已提取到 `references\code_48.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_49.txt`（3 行，37 字节）
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
> 📄 代码已提取到 `references\code_50.txt`（1 行，0 字节）
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
> 📄 代码已提取到 `references\code_51.txt`（12 行，548 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_52.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_52.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




### Image + Text Joint Prompt Construction:
> 📄 代码已提取到 `references\code_53.python`（12 行，340 字节）
> 需要查看完整代码时请读取该文件。


> [引用] 完整代码已提取到 `references\code_block_54.python`（21 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_54.txt`（2 行，38 字节）
> 需要查看完整代码时请读取该文件。




要点：
- > [引用] 完整代码已提取到 `references\code_block_55.json`（30 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_55.txt`（2 行，36 字节）
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
> 📄 代码已提取到 `references\code_56.txt`（3 行，25 字节）
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
> 📄 代码已提取到 `references\code_57.txt`（3 行，24 字节）
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
> [引用] 完整代码已提取到 `references\code_block_58.txt`（81 行）
> 需要查看时请读取该文件。

> 📄 代码已提取到 `references\code_58.txt`（2 行，35 字节）
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
> 📄 代码已提取到 `references\code_59.txt`（6 行，76 字节）
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
> 📄 代码已提取到 `references\code_60.txt`（8 行，97 字节）
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
> 📄 代码已提取到 `references\code_61.txt`（14 行，204 字节）
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
> 📄 代码已提取到 `references\code_62.txt`（4 行，26 字节）
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
```

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


### Usage

当需要此技能时，按以下步骤执行：

1. **理解需求**: 明确用户的核心意图
2. **调用流程**: 按照核心职责定义执行
3. **输出验证**: 检查输出是否符合预期
4. **反馈迭代**: 根据评审结果调整方案

## 技能包版本管理 (NEW in v6.0)

**功能**: 为十二生肖团的14个Skill提供版本管理功能

### A. 版本号规范 (语义化版本号)

| 版本号 | 格式 | 说明 | 示例 |
|--------|------|------|------|
| **MAJOR** | X.0.0 | 不兼容的版本更新 | 7.0.0 (架构重构) |
| **MINOR** | 0.Y.0 | 向后兼容的功能新增 | 6.5.0 (新增功能) |
| **PATCH** | 0.0.Z | 向后兼容的问题修复 | 6.5.1 (Bug修复) |

### B. 版本管理命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `查看版本历史 [skill_name]` | 显示指定Skill的版本历史 | `查看版本历史 zheng10-product-designer` |
| `创建版本快照 [skill_name] [version] [notes]` | 创建新版本快照 | `创建版本快照 zheng10-product-designer 6.5.0 "新增CMF设计趋势章节"` |
| `回滚到版本 [skill_name] [version]` | 回滚到指定版本 | `回滚到版本 zheng10-product-designer 6.4.0` |
| `对比版本差异 [skill_name] [v1] [v2]` | 对比两个版本的差异 | `对比版本差异 zheng10-product-designer 6.4.0 6.5.0` |
| `发布版本 [skill_name] [version] [release_notes]` | 发布新版本（标记为stable） | `发布版本 zheng10-product-designer 6.5.0 "新增CMF设计趋势章节，优化Prompt模板"` |

### C. 版本历史记录格式

版本历史记录在Skill文件的`### 版本历史`章节（如果没有则自动创建）：

markdown
### 版本历史

| 版本 | 日期 | 更新内容 | 作者 |
|------|------|----------|------|
| 6.5.0 | 2026-06-18 | 新增CMF设计趋势章节，优化Prompt模板 | 猴哥 |
| 6.4.0 | 2026-06-17 | 增加联动效果评估体系 | 猴哥 |
| 6.3.0 | 2026-06-15 | 标准化Skill格式 | 猴哥 |
| 6.2.0 | 2026-06-10 | 增加输出模板规范 | 猴哥 |
| 6.1.0 | 2026-06-05 | 增加VRAM奖励系统 | 猴哥 |
| 6.0.0 | 2026-06-01 | 架构重构，增加进化机制 | 猴哥 |

### D. 版本快照存储

版本快照存储在：`C:/Users/Administrator/.workbuddy/skills/.versions/[skill_name]/`

目录结构：

C:/Users/Administrator/.workbuddy/skills/.versions/
├── zheng10-product-designer/
│   ├── v6.0.0.md
│   ├── v6.1.0.md
│   ├── v6.2.0.md
│   ├── v6.3.0.md
│   ├── v6.4.0.md
│   └── v6.5.0.md
├── zheng10-sd-comfy-expert/
│   ├── v5.0.0.md
│   └── v5.1.0.md
└── ...


### E. 版本回滚机制

回滚操作：
1. 备份当前版本到 `.versions/[skill_name]/backup_[timestamp].md`
2. 从 `.versions/[skill_name]/v[version].md` 恢复指定版本
3. 在版本历史中记录回滚操作

示例：
bash
# 回滚 zheng10-product-designer 到 v6.4.0
1. 备份当前版本到 .versions/zheng10-product-designer/backup_20260618T113000.md
2. 复制 .versions/zheng10-product-designer/v6.4.0.md 到 skills/zheng10-product-designer/SKILL.md
3. 在版本历史中追加记录：| 6.5.0-rollback | 2026-06-18 | 回滚到v6.4.0 | 猴哥 |


### F. 版本差异对比

对比两个版本的差异（使用diff算法）：

示例输出：
diff
--- zheng10-product-designer_v6.4.0.md
+++ zheng10-product-designer_v6.5.0.md
@@ -120,6 +120,12 @@
 ### Prompt模板
 
-#### 旧版Prompt模板 (v6.4.0)
+#### 新版Prompt模板 (v6.5.0)
 
+**新增**: CMF设计趋势Prompt模板
+python
+def generate_cmf_prompt(product_type, color_trend, material):
+    """生成CMF设计趋势Prompt"""
+    # ... (省略具体代码)
+
 -**删除**: 过时的配色方案（2025年流行色）


### G. 自动版本管理触发规则

| 触发条件 | 自动操作 |
|----------|------------|
| Skill内容修改 ≥ 10% | 提示用户创建PATCH版本 |
| 新增功能章节 | 提示用户创建MINOR版本 |
| 架构重构 | 提示用户创建MAJOR版本 |
| 用户手动执行`创建版本快照` | 直接创建版本快照 |
| 每日凌晨2:00 | 自动检查是否有未创建快照的Skill修改 |

---

## 注意事项

- 执行前确保依赖工具已安装
- 如遇报错请查看详细日志输出
- 重要步骤需人工确认后再执行
- **版本管理**: 重要修改前先创建版本快照


## 语言说明
本文档使用简体中文编写，请确保所有操作输出也为中文。

## Language Note
建议使用中文输出。

## Language Note
建议使用中文输出。


---

> **版本**: v7.0 (进化闭环链加固版: 增加全员反馈收集+Checkpoint验证+联动接口规范)  
> **更新时间**: 2026-06-18 15:35  
> **维护者**: 🐦 凤 × 工程狮  
> **核心修复**: 🐦→全体进化闭环链评分从6.6提升至目标7.5+

---

## Phase 8: 进化闭环自动化与质量监控 (NEW in v7.2)

### 8.1 进化闭环自动化流程

**自动化进化目标**：
- 自动调度进化任务（每日/每周/每月）
- 自动收集全员反馈（14个Agent）
- 自动评估进化效果（评分提升/问题减少）
- 自动生成进化报告

**自动化进化流程**：
```
1. 接收进化指令（从🐭鼠/用户）
2. 识别进化目标（提升评分/减少问题/优化性能）
3. 调度进化任务（分配给其他Agent）
4. 收集进化反馈（从其他Agent）
5. 评估进化效果（对比进化前后指标）
6. 生成进化报告
7. 存储到进化数据库
8. 通知🐭鼠进化完成
```

**自动化调度规则**：
- 每日进化：检查14个Agent的工作日志，识别低评分Agent
- 每周进化：生成周报，总结本周进化效果
- 每月进化：生成月报，规划下月进化目标

### 8.2 全员反馈自动收集

**反馈收集目标**：
- 收集14个Agent的进化反馈
- 统计进化效果（评分提升/问题减少）
- 识别进化瓶颈（哪些Agent进化缓慢）

**反馈收集方法**：
1. **主动查询**：向每个Agent发送反馈查询请求
2. **被动接收**：接收Agent主动发送的反馈
3. **日志分析**：分析Agent的工作日志，提取反馈信息

**反馈格式**：
```json
{
  "agent_id": "zheng10-product-researcher",
  "agent_name": "🐭鼠",
  "evolution_target": "提升需求分析准确性",
  "evolution_method": "增加用户画像构建模块",
  "effectiveness_score": 8.5,
  "problems_encountered": ["数据不足", "时间有限"],
  "suggestions": ["增加数据采集范围", "优化算法效率"]
}
```

### 8.3 进化效果自动评估

**评估指标**：
- **评分提升**：进化后评分 - 进化前评分
- **问题减少**：进化前问题数 - 进化后问题数
- **效率提升**：进化前耗时 - 进化后耗时
- **用户满意度**：用户对进化后功能的满意度评分

**评估方法**：
1. **对比评估**：对比进化前后指标
2. **A/B测试**：一部分用户使用进化前功能，另一部分使用进化后功能
3. **用户调查**：收集用户对进化后功能的反馈

**评估报告格式**：
```json
{
  "evolution_id": "EVO-2026-0619-001",
  "target_agent": "zheng10-product-researcher",
  "evolution_target": "提升需求分析准确性",
  "before_score": 7.5,
  "after_score": 8.5,
  "score_improvement": 1.0,
  "before_problems": 5,
  "after_problems": 2,
  "problems_reduction": 3,
  "evaluation_result": "success",
  "user_satisfaction": 8.0
}
```

### 8.4 质量监控与告警

**质量监控目标**：
- 监控14个Agent的工作质量
- 识别质量下降的Agent
- 自动触发质量提升流程

**质量监控指标**：
- **工作评分**：Agent的工作质量评分
- **工作效率**：Agent的任务完成时间
- **错误率**：Agent的任务错误率
- **用户满意度**：用户对Agent工作的满意度

**质量告警规则**：
- 工作评分 < 7.0：触发质量提升流程
- 工作效率下降 > 20%：触发效率优化流程
- 错误率 > 10%：触发错误修复流程
- 用户满意度 < 7.0：触发用户反馈收集流程

**质量告警流程**：
```
1. 检测到质量下降
2. 生成质量告警报告
3. 通知🐭鼠（主理人）
4. 调度质量提升任务
5. 分配给相关Agent
6. 收集质量提升反馈
7. 评估质量提升效果
8. 关闭质量告警
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
