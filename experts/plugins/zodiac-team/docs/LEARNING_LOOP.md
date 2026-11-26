# 生肖团 · 经验反思闭环（Learning Loop）契约

> 轮次：第十八轮「分析，网络对比参照，完善」
> 位置：对齐 R17 运行态可观测性的下一层 —— **观测 → 复盘 → 沉淀 → 复用**
> 引擎：`zodiac-team/scripts/learn.js`
> 契约：`settings.json > learnings`

---

## 一、为什么需要这一层（网络对标依据）

R17 已落地运行态可观测性（OTel 对齐的结构化事件流）。但**观测 ≠ 进步**——事件流只记录「发生了什么」，不沉淀「下次怎么做」。业界在可观测性之后的共识下一层是 **评估 + 经验反思学习闭环**：

| 业界范式 | 来源 | 核心逻辑 | 生肖团落地 |
|---|---|---|---|
| 复盘纠错（Reflection） | **Reflexion**（Shinn et al., 2023） | Agent 完成任务 → 复盘完整轨迹 → 提炼成败 → 下次规避 | learn.js 每条经验绑定 trace_id |
| 失败轨迹→可复用规则 | **FORGE**（2026, arXiv 2605.16233） | 专用 reflection agent 把失败转 Rules/Examples；population broadcast 提升 29–72% | learnings 契约字段含 reusable + prevention |
| 记忆 3.0 经验反思派 | 头条/掘金 Agent 记忆综述（2026） | 从「记信息」→「总结经验」→「自我进化」；经验记忆 ≠ 事实记忆 | 严格区分事实记忆(三层记忆系统) vs 经验记忆(本机制) |
| 评估三层 | **LangSmith**（span/trace/thread） | 先人工审真实 trace，定义无歧义成功标准，分离 capability/regression eval | trace 级复盘 → 经验；鸡为单一质量仲裁（eval 归属） |
| 演化（最缺失环节） | 掘金记忆综述 | 绝大多数系统只存不演进，记忆库膨胀成噪声 | learnings.evolution：合并/降级/检索 |

**直接 operationalize 用户铁律**：「吃一堑，长一智 / 工作日志必记录 / 犯错必记录防重复 / 越做越聪明越做越精细」。本机制把价值观变成系统能力。

---

## 二、经验契约（字段定义）

每条经验 = 一行 JSONL（`logs/zodiac_learnings.jsonl`），字段：

**必填（requiredFields）**
| 字段 | 含义 |
|---|---|
| `trace_id` | 绑定 R17 观测事件流的某次 run（run_id），形成 观测→复盘 闭环 |
| `category` | 经验类别（见下表枚举） |
| `symptom` | 表象/症状（一句话） |
| `root_cause` | 根因（结构化，非甩锅） |
| `prevention` | 防再现措施（可操作的动作） |
| `reusable` | 是否可复用（true/false） |
| `author` | 沉淀者（生肖 id，如 monkey/rat/rooster） |

**可选（optionalFields）**
| 字段 | 含义 |
|---|---|
| `confidence` | 置信度 0–1（多次验证后上调） |
| `reusable_count` | 被复用次数（演化计数） |
| `linked_fix` | 关联修复（如 commit/snapshot label） |

**类别枚举（categories）**
`prompt-injection` / `param-tuning` / `workflow` / `tooling` / `eval` / `design` / `coordination`

---

## 三、与 R17 observability 的衔接（trace_id 串联）

```
[观测 run] ──R17 zodiac_traces.jsonl (emit/query/timeline)──┐
                                                           │ trace_id
                                                           ▼
[复盘] 鼠/相关专家审 trace → 提炼成败 ──learn.js add──┐
                                                   │
                                           [沉淀 learning] ──zodiac_learnings.jsonl──┐
                                                                                   │
[复用] 下次同类任务，相关专家 query learnings ────────────────────────────────────────┘
```

- 经验不可凭空记：每次 `add` 必须携带真实 `trace_id`，否则视为「盲记」被拒（呼应 recovery 不盲动铁律）。
- 演化：相同 symptom 的多次经验自动合并，`reusable_count` 累加；超 `decayDays`(180) 未复用且 confidence 低则降级/归档。

---

## 四、与三层记忆系统的边界（事实 vs 经验分离）

> 掘金记忆综述明确指出：**事实记忆与经验记忆必须严格分离，否则逻辑错乱/幻觉**。

| 记忆类型 | 载体 | 内容 | 示例 |
|---|---|---|---|
| **事实记忆** | USER.md（跨项目）/ 项目 MEMORY.md / 工作区日志 | 用户偏好、稳定约定、长期铁律 | 「商务款=拉丝不锈钢+深蓝」「不盲信摘要」 |
| **经验记忆** | 本机制 `zodiac_learnings.jsonl` | 每次任务的成败启发式（可过期/可演进） | 「全灰根因=材质染蓝锚」「Edit 前必 Read 边界」 |

- 经验记忆**不写** USER.md/MEMORY.md（避免污染稳定事实）；事实沉淀走既有三层记忆系统。
- 经验记忆带 `ts`/`decayDays`，天然过期；事实记忆长期有效。

---

## 五、各专家复盘义务（P1–P9 对应）

| 阶段 | 主责专家 | 复盘义务（须沉淀的经验类别） |
|---|---|---|
| P1 需求分析 | 鼠 | coordination（分拣歧义）、workflow（任务拆解） |
| P2 市场调研 | 虎/兔/龙 | tooling（采集脚本）、design（风格提取） |
| P3 产品设计 | 蛇 | design（CMF 取舍）、eval（设计权衡） |
| P4 成本分析 | 牛 | workflow（标准合规）、guardrail |
| P5 AI生图 | 马/羊/猴 | param-tuning（参数根因）、prompt-injection（参考图污染） |
| P6 设计评审 | 鸡 | eval（评审否决依据）、质量门禁触发 |
| P7 品牌设计 | 猪 | design（风格一致性） |
| P8 情报收集 | 狗 | tooling（情报源）、coordination |
| P9 最终输出 | 鼠 | coordination（整合遗漏） |

**单一质量仲裁**：鸡(rooster) 为 eval 归属专家，对「好/坏」经验有最终裁定权（对齐 LangSmith eval ownership）。

---

## 六、引擎用法（learn.js）

```bash
node learn.js add '{"trace_id":"run_xxx","category":"param-tuning","symptom":"...","root_cause":"...","prevention":"...","reusable":true,"author":"monkey"}'
node learn.js query --cat workflow          # 按类别过滤
node learn.js query --kw "全灰"              # 按关键词
node learn.js stats                          # 类别分布 + 可复用率
node learn.js export --cat param-tuning      # 导出
node learn.js selftest                       # 自检渲染闭环后清空
```

---

## 七、与主机 eval hook 的未来桥接（零成本路径）

当前经验靠专家手动 `add`。未来宿主若提供 **eval/tracing hook**，可自动：
1. 对 R17 trace 打分（span/trace 级 eval）；
2. 高分通过 + 复用 ≥ N 次的经验 → 自动 promote 为 `reusable=true` 高置信规则；
3. 失败 trace → 触发 `add` 草稿供鸡裁定。

桥接路径已预留：`settings.json > learnings.evalBridge` 字段。无需改动架构包即可接入。

---

## 八、结论

本机制让生肖团从「能观测」升级到「**能进化**」——
观测(R17) 提供眼睛，思考框架(R16) 提供大脑，经验反思(R18) 提供记忆与复利。
直接对齐 Reflexion/FORGE/记忆3.0，并 operationalize 用户「越做越聪明」铁律。
