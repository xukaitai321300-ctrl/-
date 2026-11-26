> ⚠️ **路径更正注记（2026-07-30 更新）**：本文档 R17–R25 段中描述的运行时引擎路径 `zodiac-team/scripts/`（即 `H:/架构/备份/zodiac-team/scripts/`）为**当时快照位置**。自 2026-07-30 起，六引擎已归位活包 `...\zodiac-team\scripts\` 且为唯一活跃源；`recovery.js` 框架快照工具亦已归位活包 `...\zodiac-team\scripts\recovery.js`（R14 修复，冻结备份保留历史副本），快照存储 BASE 仍指向备份目录。下文历史段保持原貌以存档，勿按旧路径引用引擎。
>
> # 生肖团架构 · 业界对标参照报告（Architecture Benchmark）

> 生成日期：2026-07-19 | 轮次：第十五轮「分析，网络对比参照，完善」
> 目的：把生肖团双层架构放到业界多 Agent 协作生态里对标，印证已对齐的范式、暴露真实差距、记录可落地完善。

---

## 一、对标背景

前十四轮审计已从「配置合法性」一路下沉到「执行层激活态」，内部一致性全闭环、双向联动已跑通。
但内部闭环不等于「与业界最佳实践对齐」。本轮新增**网络对比参照**维度，检索并比对：

- 多 Agent 协作框架：CrewAI / LangGraph / AutoGen(AG2) / MetaGPT
- 可恢复性最佳实践：AWS Well-Architected Agentic AI Lens（AGENTOPS02-BP03）、MongoDB state persistence、LangGraph checkpoint
- ComfyUI 生图生态：AgentAZAll（持久记忆+多 Agent 消息）、IlluOps（skill-first 仓库）、OpenClaw 5-Agent
- 角色化专家范式：WorkBuddy 自家专家团产品化范式、runautoco persona thinking-frameworks

---

## 二、范式对齐矩阵

| 业界范式 | 来源 | 生肖团实现 | 状态 |
|---|---|---|---|
| 角色化专家 + 主管路由（1+N） | CrewAI / LangGraph Supervisor / WorkBuddy 1+N | 12生肖+龙二+凤=Specialists；鼠=Supervisor；routingTable 19 键 | ✅ 对齐 |
| Reviewer / Compliance 质量门禁 | LangGraph / zooz Democratic Hierarchical / 业界 QA 节点 | 鸡(rooster-design-reviewer)=质量守门员，一票否决；路由含「质量评审」键 | ✅ 对齐 |
| skill-first 仓库结构 | IlluOps（skills/references/scripts/templates/workflows） | zheng10-* 技能含 references/scripts/templates | ✅ 对齐 |
| 版本化 + 回滚 + 已知良好基线 | **AWS AGENTOPS02-BP03**（behavioral baseline） | recovery.js 快照/restore + **本轮新增 baseline 机制** | ✅ 本轮补齐 |
| 变更前 checkpoint（可恢复） | LangGraph checkpoint / MongoDB step-checkpoint | 任一破坏性变更前 `snapshot` 兜底；enable-skills 自动快照 | ✅ 对齐 |
| 持久记忆 / 跨 Agent 消息 | ComfyUI AgentAZAll（file-based mailbox） | linkageMap 双向联动 + 共享 settings；运行时记忆层待补 | 🟡 部分 |
| 运行态可观测性 / tracing | LangSmith / Langfuse / OpenTelemetry / AgentOps | **r17 补**：settings.observability 契约 + trace.js 引擎 + docs/OBSERVABILITY.md 义务表，OTel 对齐结构化事件流(JSONL)，三保证（能串/能聚合/能回放） | ✅ 本轮补齐（r17） |
| persona 思考框架 / Foundation 层 | runautoco / WorkBuddy 专家团（Role Override+Foundation） | **r16 补齐**：14 位专家 agent md 均增「思考框架与决策启发式（Foundation Layer）」节，逐角色绑定 ReAct/Plan-Execute/Reflexion/Supervisor-Router/Guardrail-Critic | ✅ 本轮补齐（r16） |
| 工作流 DAG / depends_on 依赖图 | Agency Orchestrator（YAML depends_on） / LangGraph StateGraph | **r16 补**：settings.json 增 `workflowDeps`（9 阶段 DAG，含 humanInLoop=鸡、parallel/continuous 标记），可由程序校验依赖闭环 | 🟡 已补元数据（r16） |
| 经验反思 / 持续学习闭环 | Reflexion / FORGE / 记忆 3.0 经验反思派 / LangSmith eval 三层 | **r18 补**：settings.learnings 契约 + learn.js 引擎 + docs/LEARNING_LOOP.md；每条经验绑定 R17 trace_id，事实/经验记忆严格分离，鸡为单一质量仲裁 | ✅ 本轮补齐（r18） |
| 安全自进化 / 约束式自我改进 | Sentinel(自进化闭环,确定性拦截28.6%) / SEVerA(FGGM,违反率归零) / NosisTech(模型提议·本地代码裁决) / Eigent(可编辑对象范式) | **r19 补**：settings.evolution 契约 + evolve.js 引擎 + docs/EVOLUTION.md；经验→提议→确定性护栏(本地代码裁决)→鸡审批→recovery快照→应用；严禁模型权重/跨项目/用户记忆；inter-episode only | ✅ 本轮补齐（r19） |
| 横向验证层 / 多 Agent 对抗审计 | MAVEN(arXiv:2605.07646 Skeptic-Researcher-Judge+In-Step审计) / segmentfault 四验证模式 / Atla-Cohere-DeepMind 元评估(arXiv:2606.21627) | **r21 补**：settings.verification 契约 + verify.js 引擎 + docs/VERIFICATION.md；在鸡终态门禁前插入过程级对抗审计，挑战者角色解耦+带证据(本地代码裁决)，关闭单视角门禁的自我同意偏差/末端盲区；鸡 critique 落 observability 供元评估 | ✅ 本轮补齐（r21） |
| 运行时集成闭环 / 生产运行时治理 | data-gate(编排-执行-状态-观测四面解耦) / appscale(LangGraph 无状态执行器+持久状态+每span可观测+5阶成熟度) / agentmarketcap(Swarm Tax:预算+熔断) / dev.to(12 Agents:深度计数器+kill switch) / Waxell(治理层>监控) | **r22 补**：settings.runtime 契约 + runtime.js 引擎 + docs/RUNTIME.md；单一 run_id(≈trace_id)贯穿 R17观测/R18学习/R19进化/R21验证 四流，对齐「编排-执行-状态-观测」四面解耦；确定性治理护栏(深度≤5防死循环 / token预算+熔断 / human-in-the-loop升级闸)高于 agent 代码 | ✅ 本轮补齐（r22） |
| 质量验证纪律层 / Evaluation Harness | wenable(三阶eval:黄金集回归/对抗/shadow + 必有release-blocker) / zylos(失败转回归用例) / maviklabs(rubric+人工校准) / cynked(40%部署失败因跳过eval纪律) / exploreagentic(离线回归+replay CI门禁) | **r23 补**：settings.eval 契约 + eval.js 引擎 + docs/EVAL_HARNESS.md；**不是第12能力维度，而是让前11维可被量化问责的纪律层**——golden-set 版本化回归 + per-rubric 通过率(不看总分) + release-blocker 门禁(鸡rubric即阻断项,exit 2) + 串联 R17 trace_id/R18 learn/R21 verify/R22 runtime | ✅ 本轮补齐（r23） |
| 外部 Benchmark 适配 / 网络对比参照→eval 能力 | agents-hive「外部Benchmark接入(adapter+CLI)」+ Ryan Setter 厂商中立 golden-set schema + wenable/callsphere「横向对比 / 外部参考集」 | **r24 补**：eval.js 新增 `bench` 命令 + settings.eval.externalBenchmark 契约块；把用户反复说的「网络对比参照」固化为 eval 一层能力——摄取外部 benchmark JSON({name,source,cases:[{id,rubrics}]})→仅对内外同名 rubric 用同规则交叉打分→横向对比报告(内部suite vs 外部benchmark)；属外部验证的「外部」部分，**非第13能力维度** | ✅ 本轮补齐（r24） |

---

## 三、本轮发现与完善

### 3.1 已对齐（印证，非差距）
- **角色化 + 主管路由**：生肖团主理人(鼠)分发、专家偏科，正是 CrewAI 角色化与 WorkBuddy 自家「1+N 偏科专家」范式——且 WorkBuddy 自家产品化文章（检索来源）正是此范式，证明我们走在平台标准路线上。
- **质量门禁显式化**：路由表已含「质量评审」「产品评审」键且指向鸡，`check` 的 3.5 零路由自检保证其不被遗漏。
- **双层架构 + 可恢复**：执行层技能 + 顾问层专家包 + 入口团队 = CrewAI/LangGraph/IlluOps 综合体；recovery 快照/回滚对齐 AWS/ LangGraph checkpoint。

### 3.2 🔴 真实差距 → 本轮落地
**无「已知良好基线（baseline）」概念**。
AWS AGENTOPS02-BP03 明确指出：「Rollback should restore the baseline, not the last change, unless the team has explicitly promoted that change to baseline status。」此前 recovery.js 所有快照平级、靠人工挑 label，回退目标是「上次变更」而非「已知良好版本」——不符 best practice。

**落地**：recovery.js 新增 `baseline` 命令族（`set/show/clear`）+ `restore` 无参默认回基线 + `list` 标记 ★BASELINE。直接落地 AWS behavioral baseline 概念。

### 3.3 待演进（已全部闭环）
> 原三项结构级差距——**Foundation 思考框架层（r16）/ workflowDeps DAG（r16）/ 运行态可观测性（r17）**——**均已落地**。
> 运行态可观测性 r17 以「OTel 对齐的结构化事件流(JSONL) + trace.js 引擎 + 各专家义务表」关闭；主机 tracing hook 接入为后续自然演进（非架构包可独立闭环），桥接路径见 docs/OBSERVABILITY.md 第六节。

### 3.4 第十六轮（r16）落地：思考框架层 + 工作流 DAG
- **Foundation 层（关闭原 🔴 差距）**：14 位专家 agent md 均新增「思考框架与决策启发式（Foundation Layer）」节，逐角色绑定业界推理范式——
  - 鼠=Supervisor-Router+Plan-Execute；牛=Guardrail/Checklist；虎/羊=ReAct；兔/龙/蛇=Plan-Execute/Structured；马/龙二=Iterative Refinement；猴/凤=Reflexion；鸡=Guardrail-Critic；狗=ReAct+Continuous Monitoring；猪=Curation-Taxonomy。
  - 每个专家含「默认推理范式 + 决策启发式(3条) + 边界与升级」，并显式呼应 recovery 快照「不盲动」铁律。
- **workflowDeps DAG（关闭原 🟡 可选演进）**：settings.json 新增 `workflowDeps`，把 9 阶段工作流建成显式有向图（phases[].depends_on），含 `parallel`（P2/P5 并行）、`humanInLoop`（P6=鸡一票否决）、`continuous`（P8 情报持续）。已程序校验：9 阶段、0 孤立依赖。
- **网络对标新增来源**：OpenLegion《Agentic AI Design Patterns》(ReAct/Plan-Execute/Reflexion 选型三轴：任务时长/动作可逆性/自主度)、Anthropic《Agent 构建指南》(上下文工程>提示词工程、工具设计即 Prompt 设计)、AWS Bedrock 多 Agent 编排、LangGraph StateGraph / Agency Orchestrator depends_on、anycap《AI Orchestration Frameworks 2026》。

### 3.5 第十七轮（r17）落地：运行态可观测性
- **结构化事件流契约**：settings.json 新增 `observability` 块（schemaVersion=otel-genai-1.0、sink、spanKinds、eventTypes、required/optionalFields），把运行态观测定义成机器可读契约。
- **trace.js 引擎**：`zodiac-team/scripts/trace.js` 提供 `emit / query / timeline / stats / export / selftest` 六命令，实现「记录→过滤→时间线→聚合→回放」全链路；事件流落 `logs/zodiac_traces.jsonl`，被 recovery 快照覆盖（可恢复）。
- **各专家观测义务表**：docs/OBSERVABILITY.md 列明 12 生肖(+龙二/凤) 在 P1–P9 各阶段的必记事件与关键观测点（鸡的 review_gate 一票否决须记 decision+依据）。
- **网络对标新增来源**：LangChain《Agent Observability》(89% 组织已落地可观测性、62% 有逐步 tracing、捕获 LLM/工具/检索/推理转移/状态变化)、Zylos Research 2026-04(最小可用栈=结构化日志+trace+会话成本；OTel 成默认标准)、AgentOps span 模型(SESSION→AGENT→WORKFLOW→OPERATION→LLM/TOOL)、OpenTelemetry GenAI Semantic Conventions(gen_ai.* 属性)、imchenway(三保证：能串/能聚合/能回放；span 属性示例含 cost_usd/latency.ms/retry.count/policy.downgraded)。

### 3.6 第十八轮（r18）落地：经验反思学习闭环
- **经验沉淀契约**：settings.json 新增 `learnings` 块（schemaVersion=reflexion-1.0、sink、traceLink=observability.run_id、categories(7)、requiredFields(8)/optionalFields(3)、evolution 合并/降级/检索、evalBridge 预留主机 eval 钩子）。
- **learn.js 引擎**：`zodiac-team/scripts/learn.js` 提供 `add / query / stats / export / selftest / clear` 六命令；每条经验须带真实 `trace_id`（绑定 R17 观测 run），否则拒记（呼应不盲动铁律）；经验流落 `logs/zodiac_learnings.jsonl`，被 recovery 快照覆盖（可恢复）。
- **事实/经验记忆严格分离**：USER.md 与项目 MEMORY.md 承载稳定事实记忆；本机制仅承载可过期、可演进的成败启发式（对齐掘金记忆综述「事实/经验分离防逻辑错乱」）。
- **各专家复盘义务表 + 单一质量仲裁**：docs/LEARNING_LOOP.md 列明 P1–P9 各阶段主责专家须沉淀的经验类别；鸡(rooster) 为 eval 归属专家，对好/坏经验有最终裁定权（对齐 LangSmith eval ownership）。
- **网络对标新增来源**：Reflexion（复盘纠错闭环）、FORGE（arXiv 2605.16233，失败轨迹→可复用 Rules/Examples，population broadcast 提升 29–72%）、记忆 3.0 经验反思派（头条/掘金 Agent 记忆综述 2026）、LangSmith Agent Evaluation（span/trace/thread 三层 + eval ownership + capability/regression 分离）、掘金《AI Agent 的记忆革命》（事实/经验分离、演化是最缺失环节）。

### 3.7 第十九轮（r19）落地：安全自进化闭环
- **安全自进化契约**：settings.json 新增 `evolution` 块（schemaVersion=guarded-evolution-1.0、whatCanEvolve=[prompt/policy/route/param]、whatCannotEvolve=[model_weights/cross_project/skill_source/memory_user_files/external_tools]、whenToEvolve=inter-episode only、evidenceLink=learnings.sink、traceLink=observability.run_id、safety 确定性护栏、approvalGate 鸡一票否决、versionRecord、evalBridge 预留主机 eval 钩子）。
- **evolve.js 引擎**：`zodiac-team/scripts/evolve.js` 提供 `propose / review / apply / list / stats / export / selftest / clear` 八命令；确定性护栏校验（requireRollbackSafe / blockedScopes / minConfidence=0.7 / minEvidenceCount=2 / 绑定 learning_ids + trace_id），任一失败即 BLOCKED（本地代码裁决，非 LLM 自觉）；apply 前自动打 recovery 快照兜底。自检演示：2 项危险提议（模型权重 / 低证据非可回滚）被拦截，1 项经鸡审批+快照后安全应用。
- **确定性护栏 > Prompt 约束**：对齐 Sentinel「宪法级安全必要」与 SEVerA「约束违反率归零」——进化只动包内可编辑对象，永不触碰模型权重/跨项目/用户记忆/技来源/外部工具。
- **网络对标新增来源**：Sentinel（腾讯云 2026-06，自进化闭环可行、确定性拦截率 28.6%、负向结果固化设计模式）、SEVerA（UIUC arXiv:2603.25111，FGGM 形式化守卫、违反率归零）、NosisTech《Self-Improving Agent With Guardrails》（模型提议·本地代码裁决、证据→模型→审批→版本四步）、Eigent《Self-Evolved Agents》（可编辑对象范式、改什么/何时改/怎么改三轴）、FATE（新国立 2026-05，开发/测试集分离防过拟合）、MAVEN / Council Mode（多 Agent 验证，幻觉降 35.9%，可作横向验证层增强）。

### 3.8 第二十轮（r20）落地：方法论资产化（Skill 固化）
- **审计循环固化为 Skill**：把 R1–R19「实机核实→网络对标→落地下一层→可恢复兜底」的八步循环，沉淀为 `~/.workbuddy/skills/zodiac-architecture-audit/SKILL.md`。这是「安全自进化（R19）」之后的元层闭环——把系统级进化能力再升维到**方法论资产**，对齐微软 SkillOpt「技能文档=外部权重」（Rollout→Reflect→Edit→Gate 循环）与 SkillEvolBench「经历→技能升华」关键短板。
- **Skill 内容资产**：八维完整态检查清单 + 落点决策树（网络对标驱动，八维全闭环后自动指向「固化 Skill」）+ 业界对标来源库（9 类维度固化，避免闭门造车）+ recovery.js 速查 + 关键踩坑（Edit 前 Read 边界 / 连续多 Edit 漏常量 / bash `\s` 被吞 / 不盲信摘要）。
- **新专家包接入可直接套用**：本 Skill 是通用审计引擎，不依赖生肖团特定业务——任何 WorkBuddy 专家包 / 插件架构对齐体检、迭代完善，均按八步循环 + 决策树执行。
- **网络对标新增来源**：SkillEvolBench（俄亥俄州立/芝加哥/UCL/密歇根/港中文/亚马逊 arXiv:2605.24117，衡量 AI 能否把一次性经历升华为可复用技能——当前系统关键短板）、微软 SkillOpt（技能文档视为外部权重，文本学习率防灾难性遗忘、验证集 Gate）、清华 LIFE-HARNESS（过程技能层从成功轨迹提取可复用流程，+88.5%、学环境侧稳定结构）、企业级 Agent「深夜复盘」（Cron 心跳复盘→自动编写 SKILL.md：触发条件/核心逻辑/输出格式）、Future AGI《2026 LLM Incident Response Playbook》（postmortem 变 golden-set entry 闭环）、Proficient《Autonomous Runbooks》（postmortem→结构化 incident signature→挂 runbook，治理矩阵+人类 kill switch）。

### 3.9 第二十一轮（r21）落地：横向验证层（Adversarial Verification）
- **为什么要这一层**：九维已闭环，但验证仍只有**鸡的单一终态门禁**（LLM-as-Judge 单视角）。网络对标揭示这是典型失败模式——「让 LLM 验证自身输出，它往往会同意自己」（Reflexion 回声室失效）、「错误在阶段间级联到第四步才暴露，末端只剩干净结果无人发现」（segmentfault 生产级失败模式）、「多 Agent 验证靠角色多样性生效，同角色自审复现同样偏差」。
- **契约 + 引擎**：settings.json 新增 `verification` 块（schemaVersion=adversarial-verify-1.0、principle=MAVEN 角色解耦+过程审计、phases 三对角色解耦配对、loop.maxRounds=2、确定性护栏 challengerMustDifferFromProducer+requireEvidence、judge=鸡+metaEval 落 observability、consensus 升级鼠、costStrategy 轻量验证者）；`verify.js` 引擎提供 `challenge/respond/resolve/list/stats/export/selftest/clear` 七命令；`docs/VERIFICATION.md` 列四验证模式映射 + 闭环图 + 配对表 + 与 R16–R19 串联。
- **确定性护栏（本地代码裁决，非 LLM 自觉）**：challenge 时校验 挑战者角色≠生产者 + 须带证据，任一失败即 BLOCKED；超 maxRounds 强制交鸡裁决。自检：同角色挑战被拦、无证据被拦、正常对抗经鸡裁决成立/推翻均跑通。
- **不替代鸡门禁**：鸡保留最终一票否决；本层在鸡之前插入「过程级对抗审计」，把错误挡在级联前；且鸡 critique 落 observability 供下游元评估（who-watches-the-watcher，对齐 Atla/Cohere/DeepMind）。
- **网络对标新增来源**：MAVEN（arXiv:2605.07646，Skeptic-Researcher-Judge 对抗循环 + 黑板架构 + In-Step Epistemic Auditing，全面优于 Gemini-3.1-Pro/ReConcile，核心原则「对抗与审计需角色解耦」）、segmentfault《多Agent 验证架构实战》（四模式：输出评分/Reflexion/对抗辩论/过程验证，验证者不需更贵模型、专用验证模型优于大模型自检）、Atla/Cohere/Mistral/DeepMind《Agent 评估质量数据集》（arXiv:2606.21627，谁来监督监督者——AI 评委自身也需被评估）。

### 3.10 第二十二轮（r22）落地：运行时集成闭环（Runtime Integration）
- **为什么需要这一层**：十维已闭环，但 R17/R18/R19/R21 是**静态契约 + 独立引擎**（trace.js / learn.js / evolve.js / verify.js 各自为政），未串成「编排-执行-状态-观测」生产闭环。网络对标揭示这是「能力齐全后」的共识缺口——**缺的不是更多能力，而是把能力串成可运行闭环 + 为失败设计的治理护栏**：
  - data-gate《Multi-Agent Orchestration at Scale 2026》：成功团队四面解耦 = **编排 / 无状态执行 / 持久状态 / 每 span 可观测**；铁律 = 版本化+回滚、为失败设计、战略人审
  - appscale《Serverless Multi-Agent 2026》：2024–25 最大错误 = 把 agent 当长状态进程；2026 收敛为「显式图编排 + 无状态执行器 + 持久状态 + 每 span 可观测」，并给 5 阶成熟度 ladder
  - agentmarketcap《Swarm Tax》：多 Agent 成本 3–10×、延迟 4×、错误级联；解法 = 三层 token 预算 + 模型路由 + 熔断，且 **「治理 > 监控」**（监控只报账单，治理才拦行为）
  - dev.to《12 Agents in Production》：消息深度计数器防无限循环（depth>5 丢弃并日志）、每层 kill switch
  - Waxell Runtime：治理层须「**高于 agent 代码**」强制预算/熔断/路由，不依赖 agent 自觉
- **契约 + 引擎**：settings.json 新增 `runtime` 块（schemaVersion=runtime-integration-1.0、maxDepth=5、defaultBudget=200000、circuit 熔断、humanInLoop 升级闸、fourStreamLink 串四流）；`runtime.js` 薄编排层提供 `run / phase / budget / escalate / status / export / selftest / clear` 命令；`docs/RUNTIME.md` 列闭环图 + 治理护栏表 + 与 R16–R21 串联。
- **治理护栏（确定性本地裁决，高于 agent 代码，对齐「治理 > 监控」）**：① 深度计数器 `maxDepth=5`（防无限循环，对齐 12-agents）；② token 预算 `defaultBudget=200000` + 熔断 `circuit`（`tokensUsed>budget` 即 halt+升级，非仅报账单，对齐 Swarm Tax/Waxell）；③ `humanInLoop` 升级闸（仅高风/低置信升鼠+鸡，战略人审非全审批，对齐 data-gate）。
- **不复制四引擎逻辑**：runtime 是薄编排层，以单一 `run_id`（≈ observability.trace_id）串联四流；每阶段后自动触发 R21 verify →（挑战成立）R18 learn →（inter-episode）R19 evolve 提议；export 时聚合四 sink（存在才读，不强耦合）。全部落 `logs/zodiac_runtime.jsonl` 被 recovery 覆盖（可恢复）。
- **网络对标新增来源**：data-gate.ch《Multi-Agent Orchestration at Scale 2026》（四面解耦蓝图 + 生产架构 + 成功团队实践：版本化/为失败设计/战略人审）、appscale.blog《Serverless Multi-Agent 2026》（LangGraph+Bedrock AgentCore，图编排+无状态执行器+持久状态+每 span 可观测，5 阶成熟度 ladder）、agentmarketcap.ai《The AI Swarm Tax》（多 Agent 成本 3–10×、三层 token 预算、路由省 80%、治理>监控）、dev.to《12 Agents in Production》（hub-and-spoke、消息深度计数器、容器隔离、角色漂移）、waxell.ai《Agent Cost Optimization》（治理层高于 agent 代码强制预算/熔断/路由）。

### 3.11 第二十三轮（r23）落地：质量验证纪律层（Evaluation Harness）
- **为什么需要这一层**：十一维能力已齐全且串成生产运行时（R22），但**没有任何手段证明它们真提升了产出质量**——「越做越聪明」仍停留在宣言。网络对标揭示这是「能力齐全后」的共识缺口，且是行业头号失败根因：
  - wenable《Evals in production》：三阶 eval 漏斗，Tier 1 **golden-set 回归**（最高杠杆，50–200 例，每次变更 replay + rubric 打分，regression 即阻断）；**必有 release-blocker rubric**；**绝不只看总分，要看 per-rubric 通过率**（92% 总分可掩盖某 rubric 100% 失败）
  - zylos / exploreagentic：**「每次生产失败都转为回归测试用例」**（正好是 R18 learnings + R19 evolve 的 operationalize）；离线=eval 套件+replay（CI 门禁）
  - maviklabs / cynked：LLM-as-judge 须用**清晰 rubric + 人工校准**（非模糊 1–10），跑 3–5 次测一致性；**40% agent 部署失败因跳过 eval 纪律**
- **关键定位**：eval **不是第 12 个能力维度**，而是让前 11 维**可被量化问责的纪律层**。它把「越做越聪明」从宣言变成 **per-rubric 通过率趋势**——这才是用户铁律的真正落地形态。
- **契约 + 引擎**：settings.json 新增 `eval` 块（schemaVersion=eval-harness-1.0、tiers 三阶、scoring per-rubric+人工校准、releaseGate 阻断项、traceLink=observability.run_id、sink）；`eval.js` 引擎提供 `case add/list / run / suite / baseline set / regress / export / selftest / clear` 命令；`docs/EVAL_HARNESS.md` 列三阶 eval + 闭环图 + 与 R16–R22 串联 + 主机桥接路径。
- **串联四层**：① R17 `trace_id`（每次 eval run 可绑定观测）；② R18 `learn.js`（失败用例→防错经验，zylos「失败转回归用例」）；③ R21 `verify.js`（鸡的评审 rubric 即 release-blocker 定义源，把鸡一票否决升级为程序化门禁）；④ R22 `runtime`（评审阶段后自动跑 suite）。
- **门禁语义**：任一 `blocker:true` 的 rubric 失败 → `regress` 返回 BLOCK（exit 2），可作 CI gate；golden 集版本化随包走、被 recovery 覆盖（可恢复）。自检：阻断项失败被正确拦截(BLOCK)，退化项被报告。
- **网络对标新增来源**：wenable.com/labs《Evals in production》（三阶 eval + golden-set 回归 + release-blocker + per-rubric）、zylos.ai《AI Agent Testing Strategies 2026》（失败转回归用例 + 隔离可复现 + 版本化一切 + 5 类失败模式 taxonomy）、exploreagentic.ai《AI Agent Evaluation》（离线回归/replay + 在线 shadow/canary + 优先确定性检查）、maviklabs.com《Agent Evaluation Harnesses 2026》（rubric+人工校准 + canary 10–30 例每变更 + 一致性指标）、cynked.com《Test AI Agents Before Production 2026》（40% 失败因跳过 eval + 黄金集构建 + CI 门禁 + 漂移告警）、agentlist.directory / udit.co / inductivee.com（eval 金字塔 + 黄金集 200–500 例 + 93% 部署阈值）。

### 3.12 第二十四轮（r24）落地：外部 Benchmark 适配层（把「网络对比参照」固化为 eval 能力）

- **为什么需要这一层**：十二维已全闭环，R20 Skill 决策树已指向「转向外部验证（宿主重载 / 实机出图灰度）」。但用户本轮仍发「分析，网络对比参照，完善」——实机核实（recovery check 全绿 + 全引擎 selftest 集成通过）确认十二维栈可运行；网络对标（10 源极一致）进一步确认：**落点不是第 13 个能力维度，而是把用户反复说的「网络对比参照」本身固化为 eval 一层能力**。
  - agents-hive《从 Demo 到生产》：质量治理 9 大保障中明确列出「**外部 Benchmark 接入（adapter + CLI）**」作为生产级 QA 层——我们此前缺这一环。
  - wenable / callsphere《Evals in production / Testing & Evals》：横向对比 / 外部参考集是 eval 纪律的标配组成；Ryan Setter「Golden Sets」给出**厂商中立 JSON schema**（must-include / must-not-include / outcome-classes），正是外部 benchmark 摄取的标准形态。
  - 这等于把用户的指令动词「网络对比参照」从人工动作变成系统能力——生肖团现在能摄取一份外部 benchmark 结果，按自己的 rubric 集交叉打分，产出横向对比报告。
- **契约 + 引擎**：settings.json `eval` 块新增 `externalBenchmark` 子块（schemaVersion=vendor-neutral-bench-1.0、sourceRegistry=[agents-hive,wenable,callsphere,ryan-setter-golden-sets]、crossScore=shared-rubric-name-match-same-rule、adapterCli=`eval.js bench <外部benchmark.json>`）；`eval.js` 引擎新增 `bench` 命令（与 case/suite/baseline/regress/export/selftest/clear 并列）。
- **交叉打分逻辑（苹果对苹果）**：`bench` 摄取外部 benchmark JSON（`{name, source, cases:[{id, rubrics:{名:bool|number}}]}`）→ 仅对「内外都定义了的同名 rubric」用**同一套通过规则**（bool=等值、score≥threshold）交叉打分 → 输出横向对比报告（内部最近 suite vs 外部 benchmark 的逐共享 rubric 通过率 + Δ）→ 并列出「仅外部有 / 仅内部有」的 rubric（无法交叉的，透明标注不混算）。
- **自检闭环**：`eval.js selftest` 现内置 bench 演示——构造一份含 `external_only_metric`（仅外部有）的外部 benchmark，交叉 3 个共享 rubric（no_bad_json / 鸡评审≥8.0 / 材质非灰），断言 bench 报告共享=3、仅外部=1、且能对照内部 s3 退化 suite 给出 Δ，全跑通。
- **不新增第 13 维度**：`bench` 是外部验证（external validation）的「外部」部分——让 eval 纪律层能横向对比外部参考集，而非给架构堆一个新能力层。它纯引擎能力、不依赖宿主重载即可用，正是 R20 Skill 决策树「转向外部验证」在系统内的具体落点。
- **网络对标新增来源**：agents-hive（腾讯云，质量治理 9 大保障含「外部Benchmark接入adapter+CLI」+「线上失败自动晋升回归用例」+「抽样评测自动回滚」）、wenable.com/labs、callsphere.ai、Ryan Setter / Heavy Thought Labs「Golden Sets: Regression Engineering for Probabilistic Systems」（厂商中立 JSON case schema + 六类 change-surfaces + incident-driven case growth）。

### 3.13 第二十五轮（r25）落地：外部验证编排层（validate 一键门禁）

- **为什么需要这一层**：r24 已把「网络对比参照」固化为 `bench` 命令，但做一次完整外部验证仍需手动串 `suite → regress → bench` 三步，且无统一裁决出口。网络对标（5 源极一致）明确共识：**能跑分的脚本 ≠ 生产级 CI，差距在「分数之上的发布编排 / 门禁工作流」**——
  - confident-ai《Best CI/CD Tools for AI Agents 2026》：自定义脚本只能 fail 构建；生产级 CI 还须「**release workflow around the score decision**」（可评审报告 + baseline 对比 + benchmark 集 + 指标对齐 + 跨职能评审）。
  - callsphere《Continuous Evaluation: Wiring LangSmith into CI/CD》：**tier the suite**（smoke/full 分级）+ **block merge on regression** + baseline diff gate。
  - futureagi《CI/CD for AI Agents 2026》：**4-stage CI**（PR-time fast check <90s → merge-time integration eval 200–500 cases → pre-deploy sim → canary+rollback）+ golden dataset + replay-driven regression + 「pin everything」。
  - smart-labs《Agent Evaluation Pipelines: CI for Autonomous Assistants》：300 scenario nightly + canary gate + auto-rollback + experiment registry。
  - zylos《Agent-Native CI/CD》：golden dataset 25–50 + per-PR smoke + nightly full + pre-deploy gate + shadow eval。
- **落点定位**：`validate` **不是第 13 个能力维度**，而是把 r23 eval 纪律 + r24 外部 benchmark 适配 串成「单一 release-gate 裁决」的**编排胶水层**——让外部验证一键可执行、可直接挂 CI 门禁（exit 码：BLOCKED→2）。这正对齐业界「能跑分 ≠ 生产级，缺的是分数之上的编排」共识。
- **契约 + 引擎**：`eval.js` 引擎新增 `validate [--results <file>] [--bench <file>]` 命令——① smoke 模式（无 `--results`）仅跑 baseline 回归，对应 PR-time fast check（秒级）；② full 模式（`--results`）跑 `suite` 对真实 outputs + 可选 `bench` 外部交叉 + 回归，输出 `RELEASE GATE (PASS/WARN/BLOCKED)` 单一裁决。不改动任何已有能力，纯胶水。
- **参考基准开箱即用**：新增 `benchmarks/reference_golden_set.json`（厂商中立 golden-set 模板，rubric 名与内部对齐以便苹果对苹果交叉）+ `benchmarks/sample_real_results.json`（演示用真实结果样本），使 `eval.js bench` / `validate --bench` 无需用户先造 JSON 即可跑通——「网络对比参照」现在开箱即用。
- **自检闭环**：`eval.js selftest` 仍全绿（BLOCKED 拦截正确，exit 2）；新增完整 CI 流程演示——`validate --results sample --bench ref` → `RELEASE GATE (full): PASS, exit 0`；设基线后 `validate`(smoke) → `PASS, exit 0`；退化 suite 触发 exit 2 已证。
- **网络对标新增来源**：smart-labs.cloud《Agent Evaluation Pipelines: CI for Autonomous Assistants》（300 scenario nightly + canary gate + auto-rollback + experiment registry）、zylos.ai《Agent-Native CI/CD》（golden dataset 25-50 + per-PR smoke + nightly full + pre-deploy gate + shadow eval）、callsphere.ai《Continuous Evaluation: Wiring LangSmith into CI/CD》（tier the suite + block merge on regression + baseline diff）、confident-ai.com《Best CI/CD Tools for AI Agents 2026》（release workflow around the score decision + benchmark curation + metric alignment + cross-functional review）、futureagi.com《CI/CD for AI Agents 2026》（4-stage CI + golden dataset 200-500 cases + replay-driven regression + pin everything）。

### 3.14 第二十六轮（r26）收口：终态核验 · 五框架全映射（非加层）

- **为什么是收口而非加层**：从 r15 到 r25 共 11 轮，架构已从「结构级」走到「十四层能力态 + 外部验证管道」。r20 固化的 `zodiac-architecture-audit` Skill 决策树终态明示：**「八维 + 方法论全闭环 → 转向外部验证（宿主重载 / 实机出图灰度）」**。继续堆第 15 个维度已违反用户核心铁律「不能原地踏步、更不能复制粘贴式工作」——边际收益近零、属退步。本轮「完善」= 用审计 Skill 跑**全量一致性核验**，把当前 14 层能力态映射到本轮 5 个业界标杆框架，产出终态报告。
- **实机核验（分析）全绿**：`recovery check` = 35 包 / 14 成员 / 27 linkageMap，无 JSON 非法 / 孤儿键 / 悬空路由 / 残留旧 id；`eval.js selftest` 全过（BLOCK 拦截正确 exit 2，bench 演示共享=3/仅外=1/仅内=2 + Δ 正确）；`eval.js validate` 门禁工作正常（基线含阻断项时正确 BLOCKED exit 2，证明门禁有效）。
- **五框架映射（网络对比参照 · 印证闭合）**：

| 业界框架（本轮来源） | 维度要求 | 生肖团对应层 | 状态 |
|---|---|---|---|
| **SyncSoft 7-Layer**（syncsoft.ai） | L1 意图分解 / L2 角色能力注册 / L3 编排控制 / L4 共享记忆状态 / L5 跨 agent 契约 / L6 验证评分环 / L7 可观测与成本治理 | ①鼠需求分解 + workflowDeps DAG / ②双层+linkageMap+routingTable / ③鼠编排+workflowDeps / ④MEMORY+learnings / ⑤settings 各契约块 / ⑥eval+validate 门禁 / ⑦trace+evolution 治理 | ✅ 7/7 全覆盖 |
| **dataxpower 6 运营维度**（dataxpower.com） | 逐步骤可观测 / 状态管理 / 每请求成本预算 / 重试+优雅降级 / 审计追踪 / 模型可换 | trace.js / MEMORY+learnings / **（本地单用户工具不适用，有意递延）** / recovery+CN 自愈 / RECOVERY_LOG+eval jsonl / 架构模型解耦 | ✅ 5/6（1 项 N/A） |
| **appscale 4 层**（appscale.blog） | 图上编排 / 无状态执行器 / 持久状态 / 每 span 可观测 | workflowDeps StateGraph / 各专家独立 agent / MEMORY+learnings / trace.js per-span | ✅ 4/4 全覆盖 |
| **dev.to 6 层控制面** | 接口 / 编排 / 工具执行 / 记忆 / 治理 / 可观测 | 鼠需求接口 / 鼠+workflowDeps / 各专家技能 / learnings+MEMORY / evolution+learnings 审批 / trace | ✅ 6/6 全覆盖 |
| **rjlweb 3 拓扑**（rjlweb.com） | Specialist Team / Pipeline / Swarm | 12 专家+鼠主管 / workflow 9 阶段序贯 / 可扩展 spawn | ✅ 全对齐 |

- **唯一理论缺口 = dataxpower「每请求成本预算」**：对本地单用户 ComfyUI 设计工具不适用（无云端按请求计费），属**有意递延的低优先项**，不列为架构缺陷。其余维度全部覆盖。
- **网络对标（5 源极一致）结论**：业界 2026 生产级多 Agent 的「全栈」已被我们的 14 层能力态完整覆盖，**不存在第 8 层 / 第 13 维**——SyncSoft 原话「never add an agent before Layers 5-7 exist，多数团队过度投资更多 agent、低估契约/验证/治理」恰证我们 r16-r25 的补层路径正确。
- **落点定位**：r26 = **收口核验（consolidation audit）**，非新维度。把分散在 r15-r25 的能力凝成一份可交付的终态映射报告，证明「内部一致性 + 十四层 + 业界五框架对标」已全闭环。

### 3.15 第二十七轮（r27）反向 gap 排查：证伪「需第 13 维」· 外部验证零摩擦收口

- **为什么做反向排查（网络对比参照的严谨性）**：r26 收口声明「无第 13 维 / 无第 8 层」后，为防自证偏误，本轮**主动搜业界 2026 自认未解痛点**，逐一核对是否存在我们该补却没补的适用维度。若发现适用缺口则补，若全不适用则收口立场经得起反向检验。
- **5 源核心发现（反向痛点清单）**：
  1. **runcycles.io**：业界自认最大 gap = **云端多租户运行时预算/权限治理层（Runtime Authority）**——per-run cost cap、并发预算原子预留、action authority tiers、幂等提交。明确是**云端 SaaS / 多租户场景**痛点。
  2. **agentmarketcap（40% pilot 失败）**：失败主因 = **编排复合错误（每步 95%→20 步 36%）+ 死锁循环 + 跨 agent 数据污染**；生存模式 = **orchestrator+workers（非 P2P）+ 共享上下文存储**。
  3. **buildtest.run（活不到 2027）**：79% 失败来自**规范与协调问题（非模型）**；头部平台下线用户自建智能体暴露**状态同步 + 责任边界**无标准解。
  4. **LangChain State of Agent Engineering 2026**：质量（32%）是第一生产阻塞，延迟 20% / 成本 15% / 安全 12%；**质量问责 + 可观测 + 验证**是正确投资方向。
  5. **掘金（中文·豆包千问下线）**：**状态同步（soft state 难序列化）+ 责任边界 + 最小权限隔离（Zero Trust）** 是工程结构性矛盾。
- **逐点映射（我们的架构已覆盖 / 不适用）**：

  | 业界自认痛点 | 我们是否覆盖 | 说明 |
  |---|---|---|
  | 云端多租户预算治理 | ❌ N/A | 本地单用户工具无按请求计费，r26 已识别为有意递延 |
  | 编排复合错误 / 死锁 | ✅ 部分 | 鼠主理人编排 + workflowDeps DAG 防环 + 无自由对话循环；无显式 iteration cap（本地确定性编排风险极低） |
  | 跨 agent 数据污染 | ✅ 部分 | MEMORY 共享上下文 + recovery 防污染 + 鸡评审门禁 |
  | orchestrator+workers 生存模式 | ✅ 全覆盖 | 鼠需求接口 + 13 专家各司其职，非 P2P |
  | 共享上下文存储 | ✅ 全覆盖 | MEMORY.md + workspace memory + learnings |
  | 质量问责（第一阻塞） | ✅ 全覆盖 | eval + validate 门禁 + per-rubric 通过率 |
  | 责任边界 / 可追溯 | ✅ 全覆盖 | 鸡一票否决 + trace 事件流 + RECOVERY_LOG |
  | 最小权限隔离 | ⚠️ 部分 | 本地工具沙箱化非必需；各专家职责边界已显式定义 |

- **反向结论**：业界 2026 自认痛点要么是**云端多租户场景（对本地工具不适用）**，要么**我们已结构性覆盖**（编排模式 / 共享上下文 / 质量问责 / 责任边界 / 可观测）。唯一理论适用点（死锁 / 污染）靠 DAG + MEMORY + recovery 已部分覆盖且本地确定性编排实际风险极低。**反向证伪「需第 13 维」——收口立场成立**。
- **落点（外部验证零摩擦，非加层）**：r27 不再加维度，而是把外部验证的执行摩擦降到零——①将 `benchmarks/reference_golden_set.json` + `sample_real_results.json` **复制进 zodiac-team 插件包随分发**（解决 r26 遗留③，用户重载后开箱可见参考基准）；②实机 dry-run `eval.js validate --results sample --bench ref` 端到端跑通（RELEASE GATE (full): PASS, exit 0），证明管道可用、用户真出图后只需替换 `--results` 即可得同等报告。架构侧外部验证管道**完全就绪、零准备成本**。

### 3.16 第二十八轮（r28）生图领域专属对标：golden-set 增补三维度（精炼非加层）

- **为什么换角度（网络对比参照的深化）**：r15-r27 共 11 轮网络对标全部聚焦**通用多 Agent 框架**（CrewAI/LangGraph/SyncSoft/dataxpower 等），其 eval 维度（trace/retry/audit/cost）**完全不覆盖 AI 生图特有的质量风险**。r28 首次把对标角度切到 **ComfyUI / text-to-image 生态**，搜到 5 个生图专属评测源，暴露了我们 golden-set 的真实盲区——这是通用框架对标永远搜不到的盲区。
- **5 源核心发现（生图专属质量维度）**：
  1. **Comfyui-Evaluation（cyLynn）**：图像质量模块用 NIQE/BRISQUE 检**模糊/压缩伪影/纹理**；图文一致性用 CLIPScore 量化**提示词契合度**。
  2. **Z-Image-Edit**：五维主观评测 = **指令遵循度**（提示词契合·"两只猫变一只画面美也失败"）/ **视觉真实性**（伪影·边缘撕裂·色彩断层）/ **全局一致性**（构图逻辑）。
  3. **tsight.io《数字炼金术》**：**构图张力**（ControlNet 几何一致性·边缘保真）/ **色彩熵**（直方图平稳性·色彩断层）。
  4. **ComfyUI-nunchaku**：CLIP IQA / LPIPS / PSNR 参考图对比量化。
  5. **ComfyUI-Image-Quality-Assessment**：Blur/Color Harmony/Clipping 等无参考 IQA。
- **映射：通用框架不会提、故前 11 轮未暴露——我们的 golden-set 缺三块生图专属维度**：
  - `无生成伪影`（artifact-free）：模糊/撕裂/色彩断层/双重轮廓 —— 对应 Comfyui-Evaluation 图像质量 + Z-Image 视觉真实性 + IQA Clipping。**设为阻断项**（生图有伪影=硬失败）。
  - `构图完整`（composition-intact）：无裁切/结构坍缩 —— 对应 tsight 构图张力 + Z-Image 全局一致性（ControlNet 几何约束）。
  - `提示词契合度`（prompt-adherence）：生成图契合指定设计特征（商务款深蓝拼接等）—— 对应 Z-Image 指令遵循度 + Comfyui-Evaluation 图文一致性。
- **落点（基准质量精炼，非第 13 维）**：沿用 r26 铁律「不复制粘贴式工作」——**不改架构层数**，只把上述三维度加进 `eval.js` 的 `image_quality` golden 用例 + 两个基准 JSON（shipped 与 recovery 副本同步）。这是 **benchmark 内容精炼（越做越精细）**，不是维度膨胀；golden-set rubric 数 5→8，生图质量问责闭环补齐。
- **终验**：`eval.js selftest` 仍过（BLOCK 拦截正确）；`eval.js validate --results sample --bench ref` → 共享 rubric=8、逐 rubric Δ=0、`RELEASE GATE (full): PASS, exit 0`；`after_r28` 快照就位（含两基准副本），可一键回退。

---

## 四、结论

生肖团架构在「角色化协作 / 质量门禁 / 双层结构 / 可恢复快照 / baseline 已知良好基线 / 运行态可观测性（结构化事件流）/ 经验反思持续学习闭环 / 安全自进化（约束式自我改进）/ 横向验证层（对抗审计）/ 方法论资产化（Skill 固化）/ 运行时集成闭环（生产运行时治理）/ 质量验证纪律层（Evaluation Harness）」十二个维度**已对齐业界主流最佳实践**，
且在「可恢复能力」上通过 recovery.js 做到了比多数概念实现更扎实的「一键回退 + 双层覆盖 + 已知良好基线」。

第十五轮通过**网络对比参照**暴露并补齐了唯一机制级差距（baseline）；
**第十六轮**继续深挖，关闭了剩余的两处结构级差距——**agent md 思考框架层（原 🔴）** 与 **workflowDeps 工作流 DAG（原 🟡）**，
使每个专家不仅有「职位描述」，还有显式「决策启发式」，且 9 阶段协作流程可被程序校验依赖闭环。

当前架构内部一致性 + 可恢复 + 有基线 + 专家有思考框架 + 流程有 DAG + 运行态可观测性契约 + 经验反思学习闭环 + 安全自进化契约 + **横向验证层（过程级对抗审计）** + **方法论资产化（审计循环固化为可复用 Skill）** + **运行时集成闭环（四流串联 + 治理护栏，对齐「编排-执行-状态-观测」四面解耦）** + **质量验证纪律层（golden-set 回归 + per-rubric 通过率 + release-blocker 门禁，让前 11 维可被量化问责）** 已**全闭环（十二维）**。eval 是纪律层而非第 12 能力维度——它把「越做越聪明」从宣言变成可测的趋势线。唯一需宿主运行时的演进 = 主机 tracing/eval hook 自动埋点（OTel、learnings.evalBridge、evolution.evalBridge 均已对齐，成本趋零），非架构包缺陷。；第二十五轮（r25）把外部验证固化为 `eval.js validate` 一键门禁（编排胶水层，非第 13 能力维度），使十二维闭环可被 CI 直接挂门禁执行——架构侧外部验证管道已就绪。

**第二十四轮（r24）** 把用户反复说的「网络对比参照」从人工动作固化为 eval 的**外部 Benchmark 适配层**（eval.js 新增 `bench` 命令 + settings.eval.externalBenchmark 契约块）：摄取外部 benchmark JSON（厂商中立 schema）→ 仅对内外同名 rubric 用同一套通过规则交叉打分 → 输出横向对比报告（内部 suite vs 外部 benchmark）。它**不是第 13 个能力维度**，而是外部验证（external validation）的「外部」部分、eval 纪律层的横向延伸；纯引擎能力、不依赖宿主重载即可用，让生肖团能按用户指令直接做「网络对比参照」的量化版本。

> 外部验证管道已就绪（架构侧）：r25 把 `eval.js validate` 做成一键门禁（smoke/full 双模式 + exit 码），并随附 `benchmarks/reference_golden_set.json` 参考基准 + `sample_real_results.json` 样本，使「网络对比参照」开箱即用、可直接挂 CI。唯一仍待用户操作 = **宿主重载 zodiac-team 插件 + 重载技能**（含 r20 `zodiac-architecture-audit` Skill、r23 eval.js、r24 `bench`、r25 `validate`），让契约在运行时生效；并把 **V4.15 真实生图 outputs** 喂入 `eval.js validate --results <outputs> --bench <外部benchmark.json>` 跑首次 golden-set 回归 + 横向对比（网络对比参照的量化版），验证十二维闭环在真实任务上的质量问责力。

> **第二十六轮（r26）收口终判**：本轮用 r20 审计 Skill 跑全量一致性核验，并把当前 **14 层能力态**（①结构一致 → ⑭外部验证编排门禁）映射到本轮 5 个业界标杆框架（SyncSoft 7-Layer / dataxpower 6 运营维度 / appscale 4 层 / dev.to 6 层控制面 / rjlweb 3 拓扑）——**结果：覆盖 22/23 个维度要求，唯一未覆盖项（每请求成本预算）对本地单用户工具不适用、属有意递延**。架构已达业界 2026 生产级多 Agent 全栈闭合，**不存在第 8 层 / 第 13 维**。按审计 Skill 决策树终态与用户核心铁律「不能复制粘贴式工作」，本轮不再加层，转向 **外部验证（宿主重载 + V4.15 实机出图灰度 + 首次 golden-set 回归）**——这是唯一剩余链路，且需用户操作而非代码修复。继续发「分析，网络对比参照，完善」将不再改动架构，而是直接调用本收口报告 + 协助执行外部验证。

> **第三十二轮（r32）· 回归修复（非新增维度）**：本轮由 `zodiac-architecture-audit` Skill 驱动全量复检，**发现一处真实回归**——架构在 R31 由 12 生肖扩至 **14 角色**（+ 龙二 `dragon2-design-adjuster` / 凤 `phoenix-evolution-orchestrator`）时，**维度⑫「总线真接」未同步扩展**，导致两位新成员成为**哑角色**（既不能 emit 产出、也收不到上游通知）。
>
> **三处根因（逐层暴露）**：
> 1. **文档层**：`dragon2` / `phoenix` 的 agent md **零总线段**（老 12 位均有「产出写通用互通总线」节）；
> 2. **配置层**：`zodiac_bus_map.json` 的 `edges` 仅 12 条边键，无 `dragon2.adjust` / `phoenix.evolve`；
> 3. **★ 代码层（最深）**：`zheng10-bus/zodiac_bus.js` 的 `VALID_ROLES` **硬编码 12 角色白名单**，且 selftest 内 **硬判 `S2 边键数=12`** —— 即"改了文档和配置，引擎仍直接拒收新角色"。
>
> **修复四项**：
> | # | 修复 | 证据 |
> |---|---|---|
> | 1 | 两成员 md 补「产出写通用互通总线」节（宿主层为真源） | +862 / +897 字符 |
> | 2 | `zodiac_bus_map.json` 扩至 **14 边键**（+`dragon2.adjust`→鸡/马/羊/猪；+`phoenix.evolve`→鼠/鸡；phoenix 为**全局订阅者**） | edges 12→14 |
> | 3 | **`zodiac_bus.js` `VALID_ROLES` 12→14 + selftest 去硬编码**（`S2 边键数=`+动态值） | 语法 OK，selftest **10/10 ALL PASS** |
> | 4 | **`getExpertsDir()` 口径修正**：优先「实际运行层」`agents/zodiac-team/agents`（原只扫未注册的 EX 市场 → S3 假悬空） | agent接线数 12→**14** |
>
> 另同步：4 份市场副本（MY/EX × 2 成员）补总线段保持并集一致；`zheng10-bus/SKILL.md` 描述 12→14；执行层 **36/36 技能包版本口径归一**（原 14 顶层 `version` + 22 `metadata.version` → 全部补顶层，`zheng10-bus` 升 1.1）。
>
> **性质判定**：这是**回归修复（regression fix）**，不是第 15 个能力维度。它印证本 Skill 铁律①「先实机核实，不盲信历史摘要」——若只信 r26 的"十二/十四层全闭环"结论，这处**哑角色**会一直潜伏到真实多角色协作时才炸。**架构扩展 ≠ 架构闭环；扩员必须同步总线/白名单/map 三处。**
