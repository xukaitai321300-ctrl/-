# 运行时集成闭环（Runtime Integration Loop）

> 生肖团架构 **R22** 交付。把 R17 观测 / R18 学习闭环 / R19 安全自进化 / R21 横向验证层 **四层契约真正串成单一可运行闭环**，并补「治理护栏」——对齐 2026 工业界「从方法论到生产运行时」共识。

## 一、为什么需要这一层（对标 gap）

R16–R21 已把架构做到**十维完整态**，但十维是**静态契约 + 独立引擎**（trace.js / learn.js / evolve.js / verify.js 各自为政）。工业界在「能力齐全」之后的共识高度一致——**缺的不是更多能力，而是把能力串成可运行的生产闭环 + 为失败设计的治理护栏**：

| 工业来源 | 核心结论 | 我们的缺口 |
|---|---|---|
| data-gate《Multi-Agent Orchestration at Scale 2026》 | 成功团队四面解耦：**编排 / 无状态执行 / 持久状态 / 每 span 可观测**；铁律=版本化+回滚、为失败设计、战略人审 | 四引擎未串成「编排-执行-状态-观测」闭环 |
| appscale《Serverless Multi-Agent 2026》 | 2024–25 最大错误=把 agent 当长状态进程；2026 收敛为**显式图编排+无状态执行器+持久状态+每 span 可观测**，并给 5 阶成熟度 ladder | 缺「单一 run_id 贯穿全链路」的编排层 |
| agentmarketcap《Swarm Tax》 | 多 Agent 成本 3–10×、延迟 4×、错误级联；解法=**三层 token 预算 + 模型路由 + 熔断**；且「**治理 > 监控**」（监控只报账单，治理才拦行为） | 有观测(报账单)但无预算/熔断(拦行为) |
| dev.to《12 Agents in Production》 | 生产教训：人审层 + 隔离 + **消息深度计数器防无限循环** + 每层 kill switch | 缺深度上限与熔断 |
| Waxell Runtime | 治理层须「**高于 agent 代码**」强制预算/熔断/路由，不依赖 agent 自觉 | 缺治理层 |

## 二、闭环图（十维 → 运行时集成）

```
        ┌──────────────── 单一 run_id (≈ observability.trace_id) ────────────────┐
        │                                                                          │
  鼠(主理人) run ──▶ [P1]需求 ──▶ [P3]设计 ──▶ [P5]生图 ──▶ [P6]评审 ──▶ 整合交付
                          │              │              │              │
                    R21 verify      R21 verify      R21 verify      R21 verify
                    (龙↔蛇对抗)    (兔↔羊过程)    (猴↔鸡对抗)    鸡终审
                          │              │              │              │
                   挑战成立? ──▶ R18 learn  (沉淀防错经验, 绑 trace_id)
                                          │
                                   inter-episode ──▶ R19 evolve (确定性护栏→鸡审批→recovery快照→应用)
                                          │
                          R17 trace 全程记录(可串/可聚合/可回放)
        └──────────────────────────────────────────────────────────────────────────┘

   治理护栏(贯穿全程, 高于 agent 代码):
     • 深度计数器 depth ≤ 5  (防无限循环, 对齐 12-agents)
     • token 预算 + 熔断      (超预算即 halt, 治理层非监控层)
     • human-in-the-loop 升级闸 (仅高风/低置信升鼠+鸡, 战略人审非全审批)
```

## 三、引擎与契约

- **引擎**：`zodiac-team/scripts/runtime.js`（命令：`run / phase / budget / escalate / status / export / selftest / clear`）
- **契约**：`settings.json > runtime`（schemaVersion=runtime-integration-1.0，含 maxDepth / defaultBudget / circuit / humanInLoop / fourStreamLink）
- **事件流**：`logs/zodiac_runtime.jsonl`，被 recovery 快照覆盖（可恢复）
- **四流聚合**：`runtime.js export <runId>` 尝试聚合 trace/learn/verify/evolve 四 sink（存在才读，不强耦合）

## 四、治理护栏（确定性本地裁决，非 LLM 自觉）

| 护栏 | 值 | 触发动作 | 对标 |
|---|---|---|---|
| 深度上限 `MAX_DEPTH` | 5 | `depth>5` 丢弃阶段并日志 | dev.to 12-agents 深度计数器 |
| token 预算 `DEFAULT_BUDGET` | 200000 | 超预算 → `circuit=tripped` + `halted=true`，待人工/回滚 | Swarm Tax 三层预算 / Waxell 熔断 |
| 80% 预警 | 0.8×budget | 接近阈值告警 | 工业成本监控多阈值 |
| 人审升级闸 | 鼠+鸡 | 仅高风/低置信触发，非全审批 | data-gate 战略人审 |

## 五、与 R16–R21 的串联

- **R17 observability**：run_id = trace_id，全链路「能串」
- **R18 learnings**：verify 挑战成立 → 经验沉淀，绑同一 run_id
- **R19 evolution**：inter-episode 阶段 → 安全自进化提议（确定性护栏→鸡审批→快照）
- **R21 verification**：每阶段后自动触发角色解耦对抗审计（确定性护栏：挑战者≠生产者）

## 六、关键边界（铁律）

- runtime 是**薄编排层**，不复刻四引擎逻辑，仅以统一 run_id 串联 + 治理护栏
- 不自动应用进化（inter-episode only，R19 铁律）
- 不强耦合四引擎文件存在性（export 容错）
- 全部落 logs/ 被 recovery 覆盖 → 出错即 `node recovery.js restore after_r22`
