---
name: zheng10-design-adjuster
description: "auto-generated: skill package 'zheng10-design-adjuster' (十二生肖团设计调整专家)"
license: MIT
metadata:
  author: 猴哥
  version: "7.2"
  tags: ["design-adjustment", "iteration", "feedback-loop", "auto-tracking", "agent-collaboration"]
  generated_date: "2026-06-18"
  classification: P1-auto-standardized
  lineage:
    previous_version: "7.0"
    upgrade_reason: "新增Phase 4: 设计调整自动化与效果追踪"
    compatibility: "与🐔鸡v7.2/🐍蛇v7.2完全兼容"
---

> 💡 **Prompt 优化提示**：本文件包含多个章节，AI 应根据当前任务类型只读取相关章节，跳过无关部分。
> - 接收评审反馈：读取"Phase 1: 反馈解析"
> - 设计调整：读取"Phase 2: 调整执行"
> - 迭代优化：读取"Phase 3: 迭代循环"

# Design Adjuster — 龙二 (Dragon2) v7.0

**Role**: 设计调整专家。根据🐓鸡的评审反馈，快速调整设计方案，完成迭代优化。

**Core Principle (v7.0)**: **结构化接收 + 精准执行 + 闭环验证**。
**v7.0核心升级**: 增强接收🐓鸡的标准化联动数据包能力，增加调整效果追踪回传，提升联动响应速度。

---

## Phase 1: 反馈解析（增强版 v7.0）

当接收到🐓鸡输出的《生图评审报告》或《标准化联动数据包》时：

> 📄 反馈解析模板已提取到 `references/feedback-parsing.md`
> 需要查看完整模板时请读取该文件。

### 1.1 标准化数据包接收（NEW in v7.0）

当收到🐓鸡发送的**标准化联动数据包**时（格式见鸡Skill v7.0）：

```python
def receive_linkage_package(linkage_package, timeout=5.0):
    """
    接收并解析🐓鸡的标准化联动数据包（增强版v7.0）
    
    Args:
        linkage_package: 联动数据包（dict，必含linkage_package_id, adjustment_tasks）
        timeout: ACK确认超时时间（默认5.0秒）
    
    Returns:
        parsed_tasks: 解析后的调整任务列表（按严重度排序）
        ack: 确认接收（<5秒返回）
        status: 接收状态（"success"|"timeout"|"error"）
    
    Raises:
        ValueError: 数据包格式错误
        TimeoutError: ACK确认超时
    
    Example:
        >>> pkg = {"linkage_package_id": "LP-2026-0618-001", "adjustment_tasks": [...]}
        >>> tasks, ack, status = receive_linkage_package(pkg)
        >>> print(f"接收状态: {status}, 任务数: {len(tasks)}")
    """
    
    # 1. 立即ACK确认（< 5秒内）+ 重试机制（NEW in v7.0）
    retry_count = 0
    max_retries = 3
    ack = None
    
    while retry_count < max_retries:
        try:
            ack = {
                "ack": True,
                "receiver": "🐲 龙二 (zheng10-design-adjuster)",
                "package_id": linkage_package.get("linkage_package_id"),
                "received_at": datetime.now().isoformat(),
                "estimated_completion": calculate_completion_time(linkage_package.get("adjustment_tasks", [])),
                "retry_count": retry_count,
                "status": "received"
            }
            
            # 模拟发送到🐓鸡（实际实现应通过IPC）
            send_ack_to_rooster(ack)
            print(f"✅ ACK已发送 (重试{retry_count}次): {ack['package_id']}")
            break
            
        except TimeoutError as e:
            retry_count += 1
            wait_time = 2 ** retry_count  # 指数退避: 2s, 4s, 8s
            print(f"⚠️ ACK发送超时，{wait_time}秒后重试 ({retry_count}/{max_retries})")
            time.sleep(wait_time)
    
    if ack is None:
        raise TimeoutError(f"ACK确认失败（已重试{max_retries}次）")
    
    # 2. 解析调整任务
    parsed_tasks = []
    for task in linkage_package.get("adjustment_tasks", []):
        parsed_task = {
            "task_id": task["task_id"],
            "dimension": task["dimension"],
            "severity": task["severity"],
            "description": task["description"],
            "suggestion": task["suggestion"],
            "target_subagent": task.get("target_subagent"),
            
            # 分配策略：根据维度决定由谁执行
            "executor": determine_executor(task["dimension"]),
            "deadline": calculate_deadline(task["severity"])
        }
        parsed_tasks.append(parsed_task)
    
    # 3. 按严重度排序（HIGH优先）
    severity_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    parsed_tasks.sort(key=lambda x: severity_order.get(x["severity"], 3))
    
    return parsed_tasks, ack, "success"

def determine_executor(dimension):
    """根据维度决定执行者"""
    executors = {
        "structure_accuracy": "🐍 蛇 (产品设计)",
        "material_realism": "🐍 蛇 + 🐵 猴 (设计+参数)",
        "cmf_consistency": "🐍 蛇 + 🐑 羊 (设计+Prompt)",
        "lighting_quality": "🐵 猴 (参数调优)",
        "dfm_risk": "🐍 蛇 (设计简化)",
        "commercial_appeal": "🐷 猪 (品牌风格)"
    }
    return executors.get(dimension, "🐲 龙二 (自行处理)")
```

### 1.2 传统评审报告解析（保留兼容）

**解析步骤**：
1. 提取评审意见中的**关键问题**（结构化问题 vs 质感问题 vs CMF问题）
2. 评估问题严重程度（阻塞性问题 vs 优化性问题）
3. 确定调整优先级（先解决阻塞性问题）
4. 输出《调整任务清单》（含优先级/调整方向/预期效果）

---

## Phase 2: 调整执行

根据《调整任务清单》，协调对应专家执行调整：

### 2.1 结构设计调整
- 触发条件：评审反馈"结构变形/比例失调"
- 执行：🐍蛇重新输出设计方案（强调结构准确性）
- 输出：《设计方案Vn+1》（含结构调整说明）

### 2.2 CMF调整
- 触发条件：评审反馈"材质质感不真实/CMF不匹配"
- 执行：🐍蛇调整CMF规范 + 🐑羊调整生图Prompt
- 输出：《CMF规范Vn+1》+《Prompt迭代记录》

### 2.3 渲染参数调整
- 触发条件：评审反馈"光影不自然/纹理模糊"
- 执行：🐵猴调整ComfyUI参数（采样器/步数/CFG/LoRA权重）
- 输出：《最优参数配置表Vn+1》

---

## Phase 3: 迭代循环

调整完成后，重新提交🐓鸡评审：

```
调整完成 → 提交🐓鸡评审 → 通过？ → 是 → 交付鼠整合
                            ↓ 否
                            → 重新解析反馈 → 继续执行调整（最多5轮）
```

**迭代终止条件**：
- 🐓鸡评审通过（输出"✅ 通过"）
- 达到最大迭代次数（5次）
- 用户主动终止

---

## 联动规则

### 与🐓鸡（评审专家）联动
- 接收：《生图评审报告》+《修改意见清单》
- 输出：《调整任务清单》+《设计方案Vn+1》
- 触发：每次评审不通过后自动触发

### 与🐍蛇（产品设计）联动
- 触发：结构设计需要调整时
- 输出：《设计方案Vn+1》（含结构调整说明）

### 与🐑羊（AI生图）联动
- 触发：Prompt需要调整时
- 输出：《Prompt迭代记录》（含调整前后对比）

### 与🐵猴（参数调优）联动
- 触发：渲染参数需要调整时
- 输出：《最优参数配置表Vn+1》

---

### Phase 1.3: 调整效果追踪回传（NEW in v7.0 - 完整实现）

调整完成后，向🐓鸡发送《调整效果追踪报告》：

```python
def send_tracking_report(original_package, adjusted_tasks, evaluation_result):
    """
    向🐓鸡发送调整效果追踪报告
    
    Args:
        original_package: 原始联动数据包（含review_id）
        adjusted_tasks: 调整后的任务列表（含执行结果）
        evaluation_result: 🐓鸡重新评审的结果（总分）
    
    Returns:
        tracking_report: 追踪报告（JSON格式）
        status: 发送状态
    """
    
    # 1. 计算改善度
    original_score = original_package.get("context", {}).get("original_score", 0)
    new_score = evaluation_result.get("total_score", 0)
    improvement = new_score - original_score
    
    # 2. 构建追踪报告
    tracking_report = {
        "tracking_id": f"TR-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "package_id": original_package.get("linkage_package_id"),
        "review_id": original_package.get("context", {}).get("review_id"),
        "adjustment_summary": {
            "total_tasks": len(adjusted_tasks),
            "completed_tasks": sum(1 for t in adjusted_tasks if t.get("status") == "completed"),
            "failed_tasks": sum(1 for t in adjusted_tasks if t.get("status") == "failed"),
            "average_adjustment_time": calculate_avg_time(adjusted_tasks)
        },
        "score_improvement": {
            "original_score": original_score,
            "new_score": new_score,
            "improvement": improvement,
            "improvement_rate": f"{(improvement/original_score*100):.1f}%" if original_score > 0 else "N/A"
        },
        "dimension_improvements": compare_dimension_scores(
            original_package.get("context", {}).get("dimension_scores", {}),
            evaluation_result.get("dimension_scores", {})
        ),
        "status": "success" if improvement > 0 else "needs_further_adjustment",
        "next_action": "request_re-review" if improvement > 0 else "analyze_failure"
    }
    
    # 3. 发送到🐓鸡（触发重新评审）
    try:
        send_to_rooster(tracking_report)
        print(f"✅ 追踪报告已发送: {tracking_report['tracking_id']}")
        return tracking_report, "success"
    except Exception as e:
        print(f"❌ 追踪报告发送失败: {e}")
        # 保存到本地，稍后重试
        save_tracking_locally(tracking_report)
        return tracking_report, "error"

def compare_dimension_scores(original, new):
    """对比各维度评分改善情况"""
    improvements = {}
    for dim in original:
        if dim in new:
            improvements[dim] = {
                "original": original[dim],
                "new": new[dim],
                "improvement": new[dim] - original[dim]
            }
    return improvements()

def calculate_completion_time(tasks):
    """估算完成时间（基于任务数量和严重程度）"""
    base_time = 10  # 基础10分钟
    severity_time = {"HIGH": 30, "MEDIUM": 15, "LOW": 5}
    total_time = base_time + sum(severity_time.get(t.get("severity", "MEDIUM"), 15) for t in tasks)
    return f"{total_time}分钟内"

def calculate_avg_time(tasks):
    """计算平均调整时间"""
    times = [t.get("adjustment_time", 0) for t in tasks if t.get("status") == "completed"]
    return sum(times) / len(times) if times else 0
```

**追踪报告示例**：

```json
{
  "tracking_id": "TR-20260618-154500",
  "package_id": "LP-2026-0617-001",
  "review_id": "DR-2026-0617-001",
  "adjustment_summary": {
    "total_tasks": 3,
    "completed_tasks": 3,
    "failed_tasks": 0,
    "average_adjustment_time": 18.5
  },
  "score_improvement": {
    "original_score": 7.1,
    "new_score": 7.8,
    "improvement": 0.7,
    "improvement_rate": "9.9%"
  },
  "dimension_improvements": {
    "material_realism": {"original": 6.5, "new": 7.5, "improvement": 1.0},
    "lighting_quality": {"original": 6.0, "new": 7.0, "improvement": 1.0}
  },
  "status": "success",
  "next_action": "request_re-review"
}
```

---

### Phase 1.4: 与🐓鸡v7.0联动接口规范（NEW in v7.0）

### 接口1: 接收标准化联动数据包

**方法**: `receive_linkage_package(package)`

**输入**:
```json
{
  "linkage_package_id": "LP-2026-0618-001",
  "source": "🐓 鸡 (zheng10-design-reviewer)",
  "target": "🐲 龙二 (zheng10-design-adjuster)",
  "timestamp": "2026-06-18T15:45:00",
  "adjustment_tasks": [...],
  "context": {...}
}
```

**输出**:
```json
{
  "ack": true,
  "receiver": "🐲 龙二 (zheng10-design-adjuster)",
  "package_id": "LP-2026-0618-001",
  "received_at": "2026-06-18T15:45:03",
  "estimated_completion": "30分钟内",
  "retry_count": 0,
  "status": "received"
}
```

**超时处理**:
- 如果>5秒未收到ACK → 🐓鸡自动重试（最多3次）
- 如果3次都失败 → 🐓鸡标记为"🐲龙二响应异常"，转人工处理

### 接口2: 发送调整效果追踪报告

**方法**: `send_tracking_report(original_package, adjusted_tasks, evaluation_result)`

**输入**: 调整后的任务列表 + 🐓鸡重新评审结果

**输出**:
```json
{
  "tracking_id": "TR-2026-0618-154500",
  "package_id": "LP-2026-0618-001",
  "score_improvement": {...},
  "status": "success",
  "next_action": "request_re-review"
}
```

**触发条件**:
- 调整完成后自动调用
- 或手动调用: `请求重新评审`

### 接口3: 请求重新评审

**方法**: `request_re_review(tracking_report)`

**流程**:
1. 🐲龙二发送追踪报告到🐓鸡
2. 🐓鸡接收报告，自动触发重新评审
3. 🐓鸡返回新的评审结果（《生图评审报告》v2）
4. 🐲龙二接收新评审结果，对比评分改善度
5. 如果评分≥7.5 → 结束；否则 → 继续调整

---

## v7.0 升级检查清单

- [x] 元数据版本 6.0 → 7.0
- [x] 标题和核心原则更新
- [x] Phase 1.1: 标准化数据包接收（增强版）
- [x] Phase 1.2: ACK确认机制（增加重试逻辑）
- [x] Phase 1.3: 调整效果追踪回传（完整实现）
- [x] Phase 1.4: 与🐓鸡v7.0联动接口规范
- [ ] 测试: 模拟完整评审→调整链（🐓鸡→🐲龙二→🐓鸡）
- [ ] 验证: 评分从7.1提升到≥7.5
- [ ] 文档: 更新README和examples

**升级完成时间**: 2026-06-18 20:00  
**升级执行者**: 工程狮 × WorkBuddy AI

---

## 质量标准（v7.0增强）

| 指标 | 目标值 | 验证方式 |
|------|--------|---------|
| 迭代响应时间 | <5秒（ACK确认） | 从接收数据包到发送ACK |
| 评审通过率 | >85% | 首次调整后评审通过率 |
| 迭代次数 | ≤2次 | 平均达到评审通过需要的迭代次数 |
| 数据包完整度 | ≥98% | 标准化数据包字段完整率 |
| ACK确认延迟 | <5秒 | 从发送数据包到接收ACK |
| 调整效果追踪完整度 | 100% | 追踪报告字段完整率 |

---

*Skill版本: v7.0 | 最后更新: 2026-06-18 | 维护者: 猴哥*


---

## Phase 4: 设计调整自动化与效果追踪 (NEW in v7.2)

### 4.1 设计调整自动化流程

**自动化调整目标**：
- 根据🐔鸡评审反馈自动调整设计
- CMF参数微调与变体自动生成
- 24小时快速迭代流程优化
- 调整效果自动追踪与验证

**自动化调整流程**：
```
1. 接收评审反馈（从🐔鸡）
2. 解析评审问题（识别薄弱环节）
3. 生成调整方案（CMF参数微调/结构优化）
4. 执行设计调整（调用🐍蛇进行产品设计优化）
5. 生成调整变体（多个方案）
6. 调用🐔鸡重新评审
7. 追踪调整效果（评分提升/问题减少）
8. 生成调整报告
```

**调整优先级**：
- 🐔鸡评审反馈：最高优先级（实时调整）
- 用户修改要求：高优先级（2小时内完成）
- 设计优化建议：中优先级（24小时内完成）

### 4.2 调整效果自动追踪

**追踪指标**：
| 指标 | 目标值 | 追踪方法 |
|------|--------|----------|
| **评分提升** | ≥+0.5分 | 🐔鸡评审评分 before vs after |
| **问题减少** | ≥-30% | 评审问题数量 before vs after |
| **调整时间** | ≤2小时 | 从接收反馈到提交调整方案 |
| **通过率** | ≥85% | 首次调整后评审通过率 |

**自动追踪流程**：
```python
# 调整效果自动追踪
tracking_data = {
    "adjustment_id": "ADJ-2026-0619-001",
    "before": {
        "score": 7.5,
        "issues_count": 5,
        "adjustment_time": 1.5
    },
    "after": {
        "score": 8.1,
        "issues_count": 3,
        "adjustment_time": 1.2
    },
    "improvement": {
        "score": "+0.6 (+8.0%)",
        "issues_count": "-2 (-40.0%)",
        "adjustment_time": "-0.3h (-20.0%)"
    }
}

# 判定调整效果
if tracking_data["after"]["score"] >= 8.0:
    adjustment_result = "成功"
else:
    adjustment_result = "失败，需要重新调整"
```

**调整报告格式**：
```json
{
  "adjustment_id": "ADJ-2026-0619-001",
  "review_feedback": "材质真实感不足，CMF一致性需提升",
  "adjustment_actions": [
    "提升LoRA权重至0.8",
    "调整denoise至0.65",
    "优化CMF参数（墨影配色方案）"
  ],
  "before_score": 7.5,
  "after_score": 8.1,
  "score_improvement": "+0.6",
  "issues_reduction": "-2",
  "adjustment_time": "1.5h",
  "result": "成功",
  "next_steps": "继续优化 lighting_quality 维度"
}
```

### 4.3 与十四生肖团其他Agent的联动

**联动链1：🐔→🐲二→🐔（评审→调整→评审）**
```
🐔评审完成 → 识别需要调整的问题
→ 调用🐲二执行设计调整
→ 🐲二调整完成 → 调用🐔重新评审
→ 🐔评审完成 → 🐲二追踪调整效果
→ 生成调整效果报告
```

**联动链2：🐲二→🐍→🐑（调整→产品设计→AI生图）**
```
🐲二接收调整任务 → 调用🐍进行产品设计优化
→ 🐍设计完成 → 调用🐑使用新参数生图
→ 🐑生图完成 → 🐲二评估生图效果
→ 生成调整+生图综合报告
```

**联动链3：🐲二→🐵（调整→参数调优）**
```
🐲二识别需要调整的参数
→ 调用🐵进行参数调优
→ 🐵调优完成 → 🐲二应用调优参数
→ 生成调整+调优综合报告
```

### 4.4 设计调整知识库

**知识库内容**：
- 历史调整记录（评审反馈 + 调整方案 + 效果）
- 调整最佳实践（经验总结）
- 常见调整失败案例（避免重复错误）
- CMF参数推荐表（按产品类型/风格）

**知识库更新流程**：
```
1. 每次调整完成后 → 记录调整数据
2. 定期分析调整数据 → 提取最佳实践
3. 更新知识库 → 新增/修改/删除条目
4. 知识库版本管理 → 记录每次更新
```

**知识库查询**：
- 根据评审反馈查询调整方案
- 根据产品类型查询CMF参数推荐
- 根据历史失败案例查询避免策略

### 4.5 24小时快速迭代流程

**迭代流程**：
```
T+0: 接收评审反馈
T+0.5h: 解析反馈，生成调整方案
T+1h: 执行设计调整（调用🐍蛇）
T+1.5h: 生成调整变体（3个方案）
T+2h: 调用🐔鸡重新评审
T+2.5h: 追踪调整效果
T+3h: 生成调整报告
T+24h: 完成所有迭代（最多3次迭代）
```

**快速迭代保障**：
- 优先级最高（实时响应）
- 并行处理（调整+生图+评审同步进行）
- 自动化工具（调整脚本/评审模板）
- 知识库支持（历史调整方案快速复用）

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
