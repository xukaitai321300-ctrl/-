# 横向验证层契约（Adversarial Verification Layer）

> 维度编号：**R21 · 第十维** — 在「方法论资产化（R20）」之后，把行业共识的**横向验证层**正式落地，
> 补齐 R19 末标注为「横向补充」、此前未正式闭环的 MAVEN 式对抗审计能力。
> 对齐：MAVEN（arXiv:2605.07646 Skeptic-Researcher-Judge + In-Step Epistemic Auditing）、
> segmentfault 四验证模式、Atla/Cohere/DeepMind 元评估（arXiv:2606.21627）。

---

## 一、为什么需要这一层（来自网络对标的核心洞察）

生肖团前九维已有 **鸡的单一终态门禁**（LLM-as-Judge 单视角）。但行业研究明确指出这是**典型失败模式**：

1. **自我同意偏差**：「让 LLM 验证自身输出，它往往会同意自己」——同一模型身兼生成/评估/批评，
   会复现同样的推理结构，修正幅度极小（Reflexion 研究：自我反思大多只是重复先前错误认知）。
2. **末端盲区**：「到了生产环境，它可能在第四步之前就悄悄积累了三个错误决策，最终输出自信流畅但完全错误，
   且最后没人发现问题，因为根本没信号捕捉链条末端只剩一个干净结果。」
3. **多 Agent 验证靠多样性生效**：第二个 Agent 带着**不同角色设定、上下文、人设**介入，给出截然不同的推理路径——
   这正是单 Agent 自我纠正失败之处能生效的机制。

**MAVEN 的核心原则**：高质量的推理需要**对抗与审计**，而对抗与审计需要**角色解耦**
（Skeptic-Researcher-Judge 循环 + 黑板架构 + In-Step 实时认知审计）。

**代价规律**：验证本质上比生成简单，验证者不需要最贵的模型——
「一个较小但配备精细评分标准的专用验证模型，表现持续优于一个大模型临时充当自检角色」。

**元评估（who-watches-the-watcher）**：AI 评委自身也需被评估（Atla/Cohere/DeepMind arXiv:2606.21627）。
故本层规定：**鸡的 critique 本身落 observability 事件流，供下游 eval 审计**。

---

## 二、四验证模式与本层的映射

| 模式（参考） | 特征 | 本层采用 |
|---|---|---|
| 1. 输出评分（LLM-as-Judge） | 单评委单视角，流畅幻觉易拿高分 | **已有**：鸡终态门禁（保留为终审） |
| 2. Reflexion 自我批评 | 回声室失效 | **不采用**：禁止同角色自审 |
| 3. 对抗辩论 | 双人设互批 + Judge 综合 | **采用**：Skeptic(challenger)-Researcher(producer)-Judge(鸡) |
| 4. 过程验证 | 逐步审计，防错误级联 | **采用**：在 workflowDeps 阶段边界做验证（见 `$phases`） |

本层 = 模式 3（对抗）+ 模式 4（过程）的组合，模式 1（鸡）降格为**终审仲裁**而非唯一验证。

---

## 三、闭环图（与 R16–R19 串联）

```
羊(P5 生图) ──产出──> 兔(挑战者, 不同角色) ──challenge(带证据)──> 羊 respond(反驳+证据)
                                                         │ maxRounds=2
                                                         ▼ 未收敛
                                                   鼠(协调) + 鸡(终审 Judge)
                                                         │ verdict: uphold/overturn/rework
                                                         ▼
                                              结论落 zodiac_verifications.jsonl
                                              鸡 critique 同步落 observability(元评估)
                                                         │
                                                         ▼ (若 overturn/rework)
                                              learn.js 沉淀经验 → evolve.js 安全自进化(下一轮)
```

---

## 四、契约（settings.json > verification）

```json
{
  "enabled": true,
  "schemaVersion": "adversarial-verify-1.0",
  "principle": "role decoupling + in-step epistemic auditing (MAVEN)",
  "phases": [
    {"phase":"P3","producer":"snake-product-designer","challenger":"dragon-competitor-analyst","mode":"adversarial","mandatory":true},
    {"phase":"P5","producer":"goat-ai-image-generator","challenger":"rabbit-image-analyst","mode":"process","mandatory":true},
    {"phase":"P6","producer":"rooster-design-reviewer","challenger":"monkey-skill-optimizer","mode":"adversarial","mandatory":false}
  ],
  "loop": {"model":"Skeptic-Researcher-Judge","maxRounds":2,"challengerMustDifferFromProducer":true,"requireEvidence":true},
  "judge": {"role":"rooster-design-reviewer","veto":"one-vote","metaEval":"critiques logged to observability"},
  "consensus": {"rule":"challenge stands if no rebuttal w/ evidence in maxRounds → escalate 鼠+鸡","escalation":"rat-product-researcher"},
  "costStrategy": "verifier uses lighter persona/rubric, not heavier model",
  "traceLink": "observability.run_id",
  "sink": "logs/zodiac_verifications.jsonl"
}
```

**确定性护栏（本地代码裁决，非 LLM 自觉）**：
- `challengerMustDifferFromProducer`：挑战者角色 ≠ 生产者角色，否则 `BLOCKED`（防回声室）
- `requireEvidence`：挑战必须带证据，空泛质疑 `BLOCKED`
- `maxRounds=2`：超过轮次强制交鸡裁决，防发散振荡
- 终审 Judge 必须为鸡（`rooster-design-reviewer`），否则告警

---

## 五、各阶段验证配对（角色解耦示例）

| 阶段 | 生产者 | 挑战者（不同角色） | 模式 | 强制 |
|---|---|---|---|---|
| P3 产品设计 | 蛇(产品设计) | 龙(竞品分析) | 对抗 | 是 |
| P5 AI生图 | 羊(生图核心) | 兔(图像分析) | 过程 | 是 |
| P6 设计评审 | 鸡(评审) | 猴(参数调优) | 对抗 | 否（鸡 critique 受元评估） |

> 配对原则：挑战者须具备生产者**不具备的视角**（竞品视角审设计、分析视角审生图、调优视角审评审），
> 用多样性打破单一模型盲区。

---

## 六、引擎与用法

引擎：`zodiac-team/scripts/verify.js`

```bash
node verify.js challenge <producer> <challenger> <phase> <claim> <evidence> [traceId]
node verify.js respond  <challengeId> <rebuttal> <evidence>
node verify.js resolve  <challengeId> <judge> <verdict> <reason>   # verdict: uphold|overturn|rework
node verify.js list [phase]
node verify.js stats
node verify.js export [out.jsonl]
node verify.js selftest
node verify.js clear
```

事件流：`zodiac-team/logs/zodiac_verifications.jsonl`，被 recovery 快照覆盖（可恢复）。

---

## 七、与既有维度的关系

- **不替代鸡门禁**：鸡保留最终一票否决；本层在鸡之前插入「过程级对抗审计」，把错误挡在级联前。
- **串联 R17 观测**：每次 challenge/resolve 可绑 `trace_id`，形成「观测→挑战→裁决→复盘」全链路。
- **串联 R18 学习**：被 uphold 的挑战 → `learn.js add` 沉淀为「设计防错经验」；被 overturn 的 → 沉淀为「误报经验」。
- **串联 R19 进化**：高频 uphold 挑战暴露的系统性弱点 → 经鸡审批进入 `evolve.js` 安全自进化。
- **元评估闭环**：鸡 critique 落 observability，未来主机 eval hook 可审计「评委是否靠谱」。

---

## 八、边界与铁律

- 验证层只**质疑与挑战**，不直接改产出；改动须经生产者 respond 或鸡 resolve 后走原流程。
- 严禁同角色自审（回声室失效）；严禁无证据空泛质疑（确定性拦截）。
- 不增加单任务延迟成本：验证者用轻量人设/精细 rubric，不用更重模型。
- 所有验证记录可恢复（recovery 快照覆盖 logs/）。
