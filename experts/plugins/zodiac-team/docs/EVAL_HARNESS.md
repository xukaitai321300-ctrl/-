# EVAL_HARNESS.md —— 生肖团 质量验证纪律层 (R23)

> 把行业「能力齐全之后，强制 next step = 评估/验证纪律」落地为生肖团可运行的 eval harness。
> 让前 11 维能力闭环**可被量化问责**，而非「凭感觉说变好了」。

## 一、为什么需要这一层（网络对标结论）

R22 把 11 维能力串成生产运行时，但**没有任何手段证明它们真提升了产出质量**。
行业证据（2026）高度一致：

| 来源 | 核心结论 |
|------|---------|
| wenable《Evals in production》 | 三阶 eval：①golden-set 回归（最高杠杆，50–200 例，每次变更 replay+rubric 打分）②对抗红队 ③线上 shadow；**必有 release-blocker rubric，回归即阻断**；**绝不只看总分，要 per-rubric 通过率** |
| zylos《Agent Testing》 | **「每次生产失败都转为回归测试用例」**；隔离保证测试可复现；版本化一切（model+prompt+tools+retrieval） |
| exploreagentic《Eval Before Prod》 | 离线=回归套件+replay（CI 门禁），在线=shadow/canary；**优先确定性程序化检查，仅主观维度用 judge** |
| maviklabs《Eval Harnesses 2026》 | LLM-as-judge 须**清晰 rubric + 人工校准**（非模糊 1–10），跑 3–5 次测一致性；canary 10–30 例每变更跑 |
| cynked《Test Before Prod 2026》 | **40% agent 部署失败因跳过 eval 纪律**；eval 接入 CI 是「测过一次」与「持续测过」的区别 |

**关键洞见**：eval 不是「第 12 个能力维度」，而是让已有 11 维**可被问责的纪律层**。
它 operationalize 用户铁律「越做越聪明」——不是靠宣言，而是靠 **per-rubric 通过率趋势**。

## 二、闭环图（与 R16–R22 串联）

```
            ┌───────────────── 真实生图/审计任务产出 ─────────────────┐
            ▼                                                      │
   [R17 观测 trace] ──trace_id──► [R23 eval 评分]                    │
                                      │                              │
                          per-rubric 通过率 + 阻断项                  │
                                      │                              │
              ┌───────────────────────┼──────────────────────┐       │
              ▼                       ▼                      ▼       │
        [R18 learn.js]         [R21 verify.js]        [R22 runtime]  │
   失败用例→防错经验           鸡 rubric=release-blocker   门禁串联四流 │
              │                                              │       │
              └──────────────► 下次迭代基线 ◄───────────────┘       │
                              (eval.js baseline set)                │
```

- **串联 R17**：每次 eval run 可带 `trace_id` 绑定 R17 观测事件流
- **串联 R18**：失败用例经 `learn.js` 沉淀为防错经验（zylos「失败转回归用例」）
- **串联 R21**：鸡的评审 rubric 即 `release-blocker` 项，对齐「鸡一票否决」升级为程序化门禁
- **串联 R22**：eval 套件可在 runtime 闭环的「设计评审阶段」后自动跑

## 三、eval 契约（settings.json > eval）

```json
"eval": {
  "enabled": true,
  "schemaVersion": "eval-harness-1.0",
  "tiers": {
    "golden_regression": { "minCases": 50, "runOn": "every-change" },
    "adversarial": { "nightly": true },
    "shadow": { "first90days": true }
  },
  "scoring": {
    "principle": "per-rubric pass-rate, never aggregate-only",
    "judgeCalibration": "human-labeled subsample every quarter",
    "consistencyRuns": 3
  },
  "releaseGate": {
    "blockOnBlockerFail": true,
    "blockOnRegression": true,
    "blockerRubrics": ["鸡评审>=8.0", "no_bad_json"]
  },
  "traceLink": "observability.run_id",
  "sink": "logs/zodiac_eval_runs.jsonl"
}
```

## 四、引擎用法（zodiac-team/scripts/eval.js）

| 命令 | 作用 |
|------|------|
| `eval.js case add <json>` | 新增 golden 用例（含 rubrics + blocker 标记） |
| `eval.js case list` | 列出用例集 |
| `eval.js run <id> --output <json>` | 对单用例按 rubric 打分 |
| `eval.js suite [--results <file>]` | 跑全用例集，逐 rubric 聚合通过率 + 检测回归 |
| `eval.js baseline set` | 把当前 suite 标记为已知良好基线 |
| `eval.js regress` | 对比最新 suite 与基线；**阻断项失败则 exit 2（CI gate）** |
| `eval.js export` | 导出全部用例 + 最近 suite |
| `eval.js bench <外部benchmark.json>` | **R24 外部 benchmark 适配**：拉取公开基准映射到本地 rubric 套件，仅对「内外都定义」的共享 rubric 做苹果对苹果交叉对比，输出横向对比报告 |
| `eval.js validate [--results <file>] [--bench <bench.json>]` | **R25 外部验证编排（release-gate）**：smoke（无 --results 仅跑基线回归）/ full（真实 outputs + 可选外部交叉）单一裁决 PASS/WARN/BLOCKED，BLOCKED→exit 2（CI 门禁） |
| `eval.js selftest` | 自检验证引擎逻辑 |

**rubric 类型**：`bool`（输出须命中）/ `score`（数值须 ≥ threshold）。任一 `blocker:true` 的 rubric 失败 → `regress` 返回 BLOCK。

## 五、与主机运行时桥接（evolution/learnings.evalBridge 预留）

- 真实生图 outputs 由宿主/CI 在任务后喂入 `eval.js suite --results <file>`
- `trace_id` 自动绑定 R17 观测，失败用例可一键 `learn.js add` 沉淀
- 主机 eval hook 自动埋点为后续自然演进（r22 已预留 `evolution.evalBridge`/`learnings.evalBridge` 路径，成本趋零）

## 六、铁律边界

- eval 只评分/聚合/门禁，**不替代**鸡的语义评审（鸡 rubric 是 release-blocker 的「定义来源」，不是被 eval 取代）
- golden 集**版本化**随包走（与 recovery 快照同源），每次 prompt/route/param 变更须 replay
- **绝不只看总分**：汇报必含 per-rubric 拆解，否则退化的 8% 会被 92% 掩盖
