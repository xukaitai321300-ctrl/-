# 生肖团 · 运行态可观测性契约（Observability Contract）

> 生成日期：2026-07-19 | 轮次：第十七轮（r17）「分析，网络对比参照，完善」
> 目的：补齐第十五/十六轮遗留的唯一 🔴 结构级差距——**运行态可观测性（运行时 tracing）**。

---

## 一、为什么需要（差距来源）

前十六轮把架构做到了「结构一致 + 可恢复 + 有基线 + 专家有思考框架 + 流程有显式 DAG」。
但静态 `check` 自检只能验证「配置对不对」，无法回答运行时问题：

- 一次任务里鼠把需求路由给了谁？依据是什么？
- 鸡在 P6 门禁是「通过」还是「否决」？为什么？
- 马/羊/猴在 P5 并行生图各花了多少时间？哪次 token 异常飙高？
- 某个阶段失败后，恢复动作（recovery）是否真的生效？

这就是业界所谓 **Agent Observability**——当「多步骤 / 多工具 / 多人调试」任一成立时，就必须有 tracing（LangChain 2026 报告：89% 组织已落地某种可观测性，62% 有逐步 tracing）。

**主机（WorkBuddy 运行时）的 tracing hook 非架构包可独立提供。** 因此 r17 采用业界推荐的**最小可用栈**：以「结构化事件流(JSONL)」先落地三保证，待主机提供 hook 时，本契约已 OTel 对齐，可直接桥接。

---

## 二、设计原则（来自网络对标）

| 来源 | 关键结论 | 本架构落地 |
|---|---|---|
| LangChain《Agent Observability》 | 多步骤/多工具/他人调试任一成立即需 tracing；捕获 LLM 调用、工具调用、检索、推理转移、状态变化 | 事件类型覆盖路由/工具/门禁/异常 |
| Zylos Research 2026-04 | 最小可用栈 = 结构化日志 + trace 捕获 + 会话成本；OpenTelemetry 成默认标准 | trace.js（记录+查询+时间线+统计） |
| AgentOps span 模型 | SESSION→AGENT→WORKFLOW→OPERATION→LLM/TOOL 层级；span 含 ID/Name/Kind/Start/End/Status/Attributes | settings.observability.spanKinds + 事件层级 |
| OpenTelemetry GenAI SemConv | gen_ai.* 属性命名；prompt/completion 作为 span event；trace_id 串联 | 必填字段含 trace_id+session_id；截断 200–500 字符脱敏 |
| imchenway（中文实践） | 三保证：能串(trace_id+session_id) / 能聚合(可分组字段) / 能回放(脱敏重建) | trace.js timeline/stats/export |

---

## 三、事件契约（机器可读，来自 settings.json > observability）

### 3.1 必填字段（requiredFields）
`trace_id` · `session_id` · `ts`(ISO8601) · `agent`(生肖专家包 id) · `phase`(workflowDeps 阶段 id) · `span_kind` · `event_type` · `status`(ok/error)

### 3.2 选填字段（optionalFields）
`latency_ms` · `cost_usd` · `tokens_in` · `tokens_out` · `retry_count` · `decision` · `guardrail_hit` · `attributes`

### 3.3 事件类型（eventTypes）
| 类型 | 含义 | 典型触发者 |
|---|---|---|
| `session_start` | 一次完整任务会话开始 | 鼠（接收需求） |
| `phase_enter` | 进入某 workflowDeps 阶段 | 各阶段 owner |
| `agent_dispatch` | 鼠路由分发至某生肖专家 | 鼠 |
| `routing_decision` | 路由/调度决策（含依据） | 鼠 |
| `tool_call` | 专家调用工具/技能（参数摘要+结果+耗时） | 各专家 |
| `review_gate` | 鸡质量门禁（通过/否决+依据） | 鸡 |
| `error` | 执行异常（错误类型+恢复动作） | 出错专家 |
| `phase_complete` | 阶段完成 | 各阶段 owner |
| `session_end` | 会话结束（总耗时/总步数/成功与否） | 鼠 |

### 3.4 span 层级（spanKinds）
`SESSION`（根，一次任务）→ `AGENT`（某生肖）→ `WORKFLOW`/`OPERATION`（阶段内步骤）→ `LLM`/`TOOL`（具体调用）

---

## 四、各专家观测义务（单一事实源）

> 每位专家在思考框架层（r16 落地）执行时，应在以下决策点落事件。
> 与 `workflowDeps` 阶段 id（P1–P9）严格对应。

| 专家 | 主责阶段 | 必须记录的事件 | 关键观测点 |
|---|---|---|---|
| 鼠 rat-product-researcher | P1 / P9 | session_start, routing_decision, agent_dispatch, session_end | 路由依据、是否误派、最终整合耗时 |
| 虎 tiger-image-collector | P2 | phase_enter, tool_call（采集）, error | 采集源、下载量、还原失败率 |
| 兔 rabbit-image-analyst | P2 | phase_enter, tool_call（量化分析） | 特征提取维度、评分分布 |
| 龙 dragon-competitor-analyst | P2 | phase_enter, tool_call（SWOT） | 竞品覆盖度、技术路线判定 |
| 蛇 snake-product-designer | P3 | phase_enter, review_gate(前置) | 方案结构、CMF 取舍 |
| 牛 ox-standards-analyst | P4 | phase_enter, tool_call（可行性） | 生产标准符合度、驳回原因 |
| 马 horse-rendering-expert | P5 | phase_enter, tool_call（工作流） | 工作流搭建耗时、ControlNet 命中 |
| 羊 goat-ai-image-generator | P5 | phase_enter, tool_call（生图） | IPAdapter/CLIP 信号、出图质量 |
| 猴 monkey-skill-optimizer | P5 | phase_enter, tool_call（调参迭代） | 参数组合、retry_count、收敛曲线 |
| 鸡 rooster-design-reviewer | P6 | phase_enter, review_gate | **一票否决须记 decision+依据**；四维门禁分 |
| 狗 dog-cost-analyst | P8 | phase_enter(continuous), tool_call（情报） | 情报时效、更新频率 |
| 猪 pig-brand-designer | P7 | phase_enter, tool_call（品牌视觉） | 风格一致性、素材库引用 |

> 龙二(dragon2-design-adjuster) / 凤(phoenix-evolution-orchestrator) 作为派生专家，复用对应主责专家的事件类型。

---

## 五、引擎用法（trace.js）

事件流落点：`zodiac-team/logs/zodiac_traces.jsonl`（被 recovery 快照覆盖 → 可恢复）。

```bash
# 记录一条事件（agent/phase 必须对应 workflowDeps）
node trace.js emit '{"trace_id":"tr_xxx","session_id":"s_xxx","agent":"rooster-design-reviewer","phase":"P6","span_kind":"OPERATION","event_type":"review_gate","status":"ok","decision":"通过（四维门禁≥8.0）","latency_ms":1200}'

# 过滤查询
node trace.js query --agent rooster-design-reviewer --type review_gate
node trace.js query --phase P5 --since 2026-07-19T00:00:00.000Z

# 渲染某会话时间线（瀑布）
node trace.js timeline <session_id>

# 全局聚合
node trace.js stats

# 导出某会话（脱敏后回放）
node trace.js export <session_id>

# 自检（发一条完整多专家会话并渲染，验证引擎）
node trace.js selftest
```

---

## 六、与主机 tracing hook 的桥接路径（后续演进）

本契约已对齐 OTel GenAI SemConv 的命名与 span 层级。当主机运行时提供 tracing hook 时：

1. **零改造桥接**：`trace.js emit` 的事件结构可直接 map 为 OTel span（trace_id→trace_id、event_type→span.name、agent→gen_ai.agent.name、latency_ms→duration）。
2. **自动埋点**：主机 hook 在每个专家调用前后自动 emit，无需人工在 agent md 写日志。
3. **统一 sink**：事件流可双向同步至主机 APM / Langfuse / AgentOps。

在此之前，本契约已是「能串 / 能聚合 / 能回放」的最小可用可观测栈。

---

## 七、结论

r17 关闭了前十六轮遗留的**唯一结构级差距（运行态可观测性）**：
- 机器可读契约（settings.observability）+ 人类可读契约（本 doc）+ 引擎（trace.js）+ 各专家义务表，四位一体。
- 不依赖主机运行时即可工作；一旦主机提供 hook，OTel 对齐使桥接成本趋零。
- 事件流纳入 recovery 快照，满足「可恢复」铁律。
