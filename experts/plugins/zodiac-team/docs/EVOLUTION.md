# 安全自进化契约（Guarded Self-Evolution）

> 生肖团架构第八维能力。把 R18「经验反思闭环」积累的成败启发式，**安全地转化为系统自身的可演进改进**——
> 直接 operationalize 用户铁律「越做越聪明，越做越精细 / 吃一堑长一智」到**系统级**。
>
> 本机制**只建契约与护栏**，不盲目自动改写任何文件。实际进化须由未来真实事件触发、经鸡审批、recovery 快照兜底后执行。

---

## 一、设计原则对标表（网络对比参照 · 第十九轮）

| 业界实践 | 核心主张 | 生肖团映射 |
|---|---|---|
| **Sentinel（腾讯云, 2026-06）** | 自进化闭环可行（侦察→导航→执行→验证→反馈）；**宪法级安全必要**，确定性拦截率 28.6%；负向结果固化为永久设计模式；**确定性拦截 > Prompt 约束** | `evolution.safety.deterministicGuardrail`="local code decides, model only proposes"；`requireRollbackSafe`；拦截日志即设计模式 |
| **SEVerA（UIUC, arXiv:2603.25111）** | 形式化守卫生成模型 FGGM，数学逻辑约束 + 自我学习结合，**约束违反率降至零** | `blockedScopes` 确定性阻断（模型权重/跨项目/用户记忆文件），非软性 Prompt 约束 |
| **NosisTech 带护栏的自改进** | 核心模式=「模型可提议，本地代码裁决」；受限场景阻断、低置信阻断、非可回滚阻断；顺序=证据优先→模型其次→审批第三→版本记录最后 | `validate()` 确定性校验前置；`approvalGate` 鸡一票否决；`versionRecord` 版本留痕 |
| **Eigent Self-Evolved Agents** | 把 prompt/决策规则/工具选择视为**可编辑对象**而非固定常量；进化分「改什么/何时改/怎么改」三轴 | `whatCanEvolve=[prompt,policy,route,param]`；`whenToEvolve=inter-episode only`；`conservativeFallback` |
| **FATE（新国立, 2026-05）** | 自我疗愈：从失败中筛选→帕累托前沿→策略优化；开发/测试集严格分离防过拟合 | `minEvidenceCount=2`（多经验支撑，防单点过拟合）；`evalBridge` 预留主机 eval 验证 |

---

## 二、安全自进化闭环（与 R16/R17/R18 串联）

```
[R17 观测] 事件流(trace_id) ──┐
                                ↓
[R18 学习] 经验沉淀(learning_id, 绑定 trace_id) ──┐
                                                    ↓
        ┌─────────────────── 安全自进化循环 ───────────────────┐
        │  propose  ← 经验驱动，须绑定 learning_ids + trace_id   │
        │     ↓                                                 │
        │  validate (确定性护栏: 本地代码裁决)                    │
        │     ├─ 受限域/非可回滚/低置信/证据不足 → 🚫 BLOCKED    │
        │     ↓ 通过                                            │
        │  review  ← 鸡(rooster) 一票否决闸门                    │
        │     ├─ reject → 🚫 终止                               │
        │     ↓ approve                                         │
        │  snapshot (recovery.js 打 evo_<id> 兜底)              │
        │     ↓                                                 │
        │  apply   ← 双轨(R26/D-50):                          │
        │             有 patch → 先落文件级回滚点 → 真写盘 → APPLIED │
        │             无 patch → 契约级采纳 → ADOPTED           │
        │             patch 失败 → 自动回滚 → APPLY_FAILED      │
        │     ↓                                                 │
        │  rollback (R26+): 有退路还要能走退路 → ROLLED_BACK    │
        │     ↓                                                 │
        │  verify (evalBridge: 主机 eval 验证 held-out 任务)    │
        └─────────────────────────────────────────────────────┘
```

**关键不变量**：模型只能"提议"，本地代码"裁决"。任何进化**绝不**在单任务内自动应用（`whenToEvolve=inter-episode only`），且**真写盘前必须已有退路**（文件级回滚点无条件，全树快照可选）。

---

## 三、可进化 vs 不可进化边界

| 维度 | 可进化（whatCanEvolve） | 不可进化（whatCannotEvolve / blockedScopes） |
|---|---|---|
| 提示词 | ✅ prompt（各专家 system prompt 微调措辞） | ❌ 用户记忆文件（USER.md / MEMORY.md，由三层记忆系统承载） |
| 策略 | ✅ policy（路由/分拣优先级微调） | ❌ 模型权重（model_weights，须训练，确定性阻断） |
| 路由 | ✅ route（routingTable 增删映射） | ❌ 跨项目改动（cross_project，铁律禁止盲启） |
| 参数 | ✅ param（生图默认参数区间微调） | ❌ 技能源码（skill_source）/ 外部工具（external_tools） |

> 边界原则：进化只动**包内可编辑对象**，永不触碰**模型权重、用户记忆、跨项目、技能源码、外部工具**——这是 SEVerA「约束违反率归零」的工程化落地。

### 3.1 可编辑对象**落在哪个文件**（R26 / D-50 补齐）

早期契约只声明了 `whatCanEvolve`（**类型**：prompt/policy/route/param），却**未声明这些对象存在哪个文件**——
导致 `apply` 无从下手，只能"打快照 + 标记 APPLIED"而**零文件改动**（D-50）。现补齐 `evolution.editableObjects`：

| 字段 | 值 | 含义 |
|---|---|---|
| `allowFiles` | `["settings.json"]` | 仅允许 json-set 到**策略子树标量**（带 CAS 保护，不重排文件格式） |
| `allowDirs` | `["prompts/", "policies/", "routes/"]` | 提示词/策略/路由资产的存放目录 |
| `allowExt` | `[".json", ".md", ".txt"]` | 仅这三类可写 |
| `denyDirs` | `scripts/ agents/ skills/ docs/ logs/ avatars/ benchmarks/ .codebuddy-plugin/` | 引擎源码/角色定义/skill_source/文档/日志等**一律阻断** |
| `jsonSetAllowPaths` | `routingTable linkageMap rules policies prompts params` | json-set 仅限这些策略子树根 |
| `requireCas` | `true` | 必须带 `from`（旧值）做 compare-and-swap，防并发覆写 |
| `maxBytes` | `262144` | 单文件可编辑上限 |

> 设计取舍：`scripts/`（引擎源码）与 `agents/`（角色定义）**刻意**不可自改——自进化引擎改写自身代码是经典失控风险；`skills/` 对应 `whatCannotEvolve` 里的 `skill_source`。

---

## 四、确定性护栏清单（validate 函数）

每条提议须通过以下全部校验，任一失败即 `BLOCKED`（本地代码裁决，非 LLM 自觉）：

1. `rollback_safe === true`（必须可回滚）
2. `scope` 不在 `blockedScopes`（模型权重/跨项目/用户记忆文件）
3. `target_type` ∈ `whatCanEvolve`（prompt/policy/route/param）
4. `confidence ≥ 0.7`
5. `evidence_count ≥ 2`（至少 2 条 R18 经验支撑，防单点过拟合）
6. 绑定 `learning_ids`（证据追溯键：可填经验 id `lrn_*`，亦可填产生该经验的 `run_*`；见 §十）
7. 绑定 `trace_id`（引用 R17 观测 run）
8. **（R26/D-50）若携带 `patch`，须过 `editableObjects` 白名单** —— 文件须在 `allowFiles`/`allowDirs` 内、扩展名合法、路径无越权（无绝对路径 / 无 `..`）；命中 `scripts/`（引擎源码）、`agents/`（角色定义）、`skills/`（skill_source）等一律 `BLOCKED`
9. **（R26/D-50）若 `patch` 的目标文件已存在，须过干跑预检** —— `json-set` 校验目标为合法 JSON + 路径在策略子树 + CAS 旧值匹配；`text-replace` 校验 `find` 命中数 = `expectCount`。目标尚不存在（新建资产）则预检顺延至 apply 期

校验失败时若原提议为"标准场景"，保守回退为 **prompt-only repair**（`conservativeFallback`），保持系统在安全车道内继续前进。

---

## 五、鸡审批闸门（approvalGate）

- **reviewer**：`rooster-design-reviewer`（质量守门员，与协作规则「一票否决权」一致）
- **veto**：`one-vote`（单票否决，无需多轮）
- **requireSnapshotBeforeApply**：`true`（apply 前必打 recovery 快照）
- **snapshotTool**：`zodiac-team/scripts/recovery.js`

> 横向补充：多 Agent 验证（MAVEN Skeptic-Researcher-Judge、Council Mode 幻觉降 35.9%）可作为**验证层**增强——关键节点由不同"门派"专家交叉评审（如 兔量化复核 / 龙竞品对标 / 鸡终审），与鸡一票否决天然契合。

---

## 六、版本记录与回滚

- 版本记录：`logs/zodiac_evolution_log.jsonl`（被 recovery 快照覆盖，可恢复）
- **apply 三态（R26 / D-50 修正）** —— 消除"状态叫 APPLIED 却零文件改动"的语义谎言：
  - `APPLIED` — 携带可执行 `patch` 且**真写盘成功**，记录 `before_sha` / `after_sha` / `bytes_delta`（真落地）
  - `ADOPTED` — **无**机器可执行 patch，仅**契约级采纳**、未改任何文件，落地待人工/Agent（诚实降级）
  - `APPLY_FAILED` — 干跑/写盘/回读校验失败，已自动回滚（`rolled_back:true`），未写盘则直接中止
- **回滚双保险（R26+）**：
  - **文件级回滚点（无条件）** — 只要"真写盘"，`apply` **先**把目标文件原文写入 `logs/rollback/<id>__<file>`（附 `.meta.json` 记录 sha/bytes）→ 建不起来就**中止不写**（不留退路不写盘）
  - **全树快照（可选）** — `recovery.js` 打 `evo_<id>`（520MB，慢）；被跳过或失败**不影响可回滚性**，因为文件级回滚点已独立存在
  - **回滚动作** — `node evolve.js rollback <id>`：仅 `APPLIED` 记录可回滚，还原后状态置 `ROLLED_BACK`（留 `restored_sha` / `prev_sha` 审计）；校验不过置 `ROLLBACK_FAILED`
- 与 R14 基线 + R15 baseline 机制联动：进化失败可一键回到已知良好版本

> **终态语义（R26+）**：`ROLLED_BACK` / `ROLLBACK_FAILED` 与 `APPLIED` / `ADOPTED` / `REJECTED` 同属**终态**，
> 参与 `propose` 的**幂等-1 防噪声去重**（同意图重提被忽略而非新增条目）与 `dedupe` 的优先级排序；
> `APPLY_FAILED` **刻意不列入**——写盘受阻属可重试的瞬时失败，允许重提。

---

## 七、各专家进化范围（建议）

| 专家 | 可进化对象 | 典型进化信号（来自 R18 经验） |
|---|---|---|
| 鼠（主理人） | policy / route | 路由分拣优先级、任务分配启发式 |
| 牛（工作流标准） | param / policy | 生产可行性判定阈值 |
| 虎（图像采集） | prompt / route | 跨模态检索措辞、素材筛选规则 |
| 兔（图像分析） | policy | 量化分析维度权重 |
| 龙（竞品分析） | prompt | SWOT 框架措辞 |
| 蛇（产品设计） | prompt / policy | CMF 设计约束表述 |
| 马（工作流优化） | param / route | ControlNet 强度区间 |
| 羊（生图核心） | prompt | 提示词锚点（如 cobalt-blue 抑制全灰）|
| 猴（参数调优） | param | 采样器/CFG 默认区间 |
| 鸡（评审） | policy | 评审清单阈值 |
| 狗（情报） | route | 情报源优先级 |
| 猪（风格参考） | prompt / policy | 风格指南表述 |

---

## 八、主机 eval 桥接路径（后续自然演进，非架构包缺陷）

`evolution.evalBridge` 预留主机 eval hook 接口：主机运行时对"已应用进化"在 held-out 任务上验证，
通过才晋升为 reusable 经验（与 R18 `learnings.evolution` 联动）。当前为静态契约，主机 hook 缺位时不影响架构完整性。

---

## 九、与 R16/R17/R18 的关系

- **R16 思考框架**：每个专家"怎么想" → 本机制决定"怎么改自己"
- **R17 观测**：提供 `trace_id` 证据链 → 本机制 `traceLink` 绑定
- **R18 学习**：提供 `learning_id` 经验 → 本机制 `evidenceLink` 引用
- **R19 进化**：把经验**应用**为实际改进（"只存不演进"→"存且演进"）

> 至此，前十八轮暴露的全部结构级差距（🔴×1 + 🟡×2）彻底关闭，并补上「学习之后」的最后一环——**安全自进化**，架构达八维完整态。

---

## 十、patch 契约与证据语义（R26 新增）

### 10.1 结构化 patch —— apply 真落地的唯一凭据

```json
{
  "target_type": "param", "scope": "intra_package",
  "target": "zheng10-ai-image-generator",
  "proposed_change": "ControlNet 强度默认 0.45 → 0.65",
  "patch": {
    "file": "prompts/cup_recipe.md",
    "op": "text-replace",
    "find": "controlnet_strength: 0.45",
    "replace": "controlnet_strength: 0.65",
    "expectCount": 1
  },
  "confidence": 0.88, "evidence_count": 3,
  "learning_ids": ["lrn_xxx", "run_xxx"], "trace_id": "run_xxx",
  "rollback_safe": true, "author": "monkey"
}
```

| `op` | 语义 | 关键字段 | 安全性来源 |
|---|---|---|---|
| `text-replace` | 精确文本替换 | `find` / `replace` / `expectCount` | 命中数必须等于期望值，防误伤 |
| `json-set` | JSON 标量最小替换（**不重排文件格式**，保留内联数组与缩进） | `path`（点分路径）/ `from`（CAS 旧值）/ `to` | 路径须在策略子树；`from` 与现值不匹配即拒 |

> 执行顺序：提议期**静态校验**（白名单/op）→ 目标存在则**干跑**（JSON/CAS/命中数）→ 鸡审批 → **快照** → **写盘** → **回读校验** → 失败**自动回滚**。

### 10.2 learning_ids 语义（D-53 澄清）

`learning_ids` 是**证据追溯键**，而非"必须等于某条 `learnings` 记录的 id"：

- **R26 起**，`learn.js` 的 `add()` 为每条经验生成 `id`（`lrn_*`）→ **新经验可被 id 精确引用**
- **历史记录**多填 `run_*`（产生该经验的 run_id / trace_id）——因该经验自身也携带同一 `trace_id`，**可反查等价**，故保留兼容、不回改历史

### 10.3 runtime 编排的口径澄清（D-52）

`runtime.js` 每阶段后**无条件**触发 `verify → learn → evolve.propose`。头部注释原先写作「(挑战成立) learn」，易误解为"判定成立后才沉淀"。
实际语义：本编排层**不预判挑战成立与否**（成立与否由 `verify.js` 的 `resolve` 裁决，需鸡/人介入），故 `learn` 是「**触发对抗审计即沉淀过程经验**」。

### 10.4 回滚点契约（R26+）

**设计信条**：**改前必留退路；有退路，还要能走退路。**

| 退路层 | 位置 | 建立时机 | 成本 | 可跳过 |
|---|---|---|---|---|
| 文件级回滚点 | `logs/rollback/<id>__<file>`（+ `.meta.json`） | **真写盘之前，无条件** | 数 KB | ❌ 建不起来则**中止不写盘** |
| 全树快照 | `recovery` snapshots（`evo_<id>`） | apply 前（可配） | 520 MB / 慢 | ✅ 跳过不影响可回滚性 |

- `applied.rollbackPoint` 记录路径：**包内为相对路径**（`logs/rollback/…`）；自检隔离期回滚点落在系统临时目录，此时记录**绝对路径**（`rollback` 命令两种形态都能读）
- `applied.rollbackCmd` 直接给出回滚命令
- `node evolve.js rollback <id>` 仅接受 `APPLIED` 状态；还原成功后状态 → `ROLLED_BACK`
- 回滚前会校验 `.meta.json` 的 `sha` 与回滚点内容一致（不一致仅告警，仍按回滚点内容恢复）

> 为什么不全靠全树快照？520MB + 数十秒的成本让它在**回归/隔离测试**中必然被跳过，
> 一旦跳过就出现"APPLIED 但无回滚点"——即"名义可回滚、实际无处可退"。文件级回滚点把这句话变成真的。

### 10.5 测试隔离（R26+）

e2e / 回归测试若直接写真实进化流，会污染日志并撞上"幂等-1 防噪声去重"（同意图重提被忽略，导致测试不可重复）。
引擎提供两个环境变量做隔离：

| 环境变量 | 作用 |
|---|---|
| `ZODIAC_EVO_LOG=<path>` | 重定向进化日志（真实流一字不动，可用 SHA 复核隔离性） |
| `ZODIAC_EVO_SKIP_SNAPSHOT=1` | 跳过 520MB 全树快照（文件级回滚点仍**无条件**建立） |

**R27 / D-58：自检期回滚点目录整体隔离到系统临时目录**（`os.tmpdir()/zodiac_evo_rb_selftest`）。

> **根因（实测）**：宿主 `safe-delete` 带**批量删除守卫**——单次删除量超阈值会**直接终止进程**（`EPERM: rename ...state.json`）。
> 原实现把自检回滚点写进包内 `logs/rollback/`，`finally` 再逐个删；一旦某轮删除量超阈值，进程被杀 → `finally` 中断 → 回滚点残留；
> 残留又让下一轮删除量更大 → **恶性循环累积**（实测一次跑批留下 6 组、每次恰好 1 组的规律间隔）。
> 对照实验：**单文件删除 10/10 成功**，**一次删 24 个必触发** —— 证明这是"量的阈值"而非"偶发"。
>
> **修法**：自检回滚点全部落在 tmp（tmp 不在受管目录内、不受守卫约束，实测 20/20 稳定），
> 使包内删除量恒为演示资产的 **2 个**文件；再配合 `finally` 清理 tmp，达成**包内 + tmp 双零残留**。

### 10.6 宿主运行环境约束（R27 / D-59）

本机宿主限制 **node 创建子进程**：`spawnSync` 无论用 `process.execPath` 还是 bare `node` 一律 `EBUSY`（已做最小反证）。

| 受影响 | 现象 | 对策 |
|---|---|---|
| `selftest_all.js` 聚合门禁 | 9 suite 全 `EBUSY` → 0/9 假 FAIL | **R28 已修（D-60 + D-61）**：① 三态判定——`EBUSY` 记 `SKIP` 而非 `FAIL`，退出码 2；② 已模块化引擎改**同进程直调** → **9/9 ALL GREEN（全 `[inproc]`）**；**R29 补入 `recovery` → 10/10** |
| `runtime.js` 集成链路 | 阶段末触发 `trace/learn/evolve` 失败 → 4 项断言失败 | **R28 已修（D-61）**：四引擎模块化后改「同进程直调 + 输出捕获」（`lib/inproc.js`），子进程仅作兜底 → `runtime selftest` **全绿** |
| `zodiac_bus.js` selftest | T1/T2 三项 `downstream=null` 假失败 | **已修（R27）**：同进程函数调用 + 输出捕获 → 10/10；**R28** 再补 `module.exports` 供聚合器同进程调用 |

> 判据：**EBUSY 不得记作代码回归，但也不得静默**——必须在输出中明示"环境不可达"。
> **R28 结论**：经 D-61 模块化后，引擎套件已**不再依赖子进程**；上述 `EBUSY` 约束现仅对
> 「未模块化的外部引擎」生效（此时按 D-60 三态记 `SKIP`，并给出 Python 兜底指引）。
> **R29 结论**：10 个 JS 引擎**全部模块化完毕**（末位 `recovery` 由 D-62 补齐），`EBUSY` 约束
> 现仅对「被 `ZODIAC_*_JS` 重定向到外部实现」这一情形生效。

### 10.7 同进程集成与三态门禁（R28 / D-60 · D-61）

**背景**：宿主对 `spawnSync` 的封锁，使 JS 层的聚合/集成在受限会话下"名义存在、实际不可验证"。
R28 做两件事，使其转为**真可验证**。

**（1）D-61 引擎模块化 —— 摆脱子进程**

约定：每个引擎把顶层 CLI 分发包进 `cli(argv)`（或 `main(argv)`），并加 `require.main` 守卫：

```js
if (require.main === module) cli(process.argv);
module.exports = { cli };
```

- `argv` 统一为**完整进程 argv**（`['node', scriptPath, ...args]`）
- 已模块化：引擎套件 `trace` `learn` `evolve` `verify` `eval` `metrics` `golden-regress` `runtime`
  ＋ **`recovery`（R29 / D-62）** ＋ 外部技能包 `zodiac_bus`
- 导出名统一为 `cli`（`main` 作向后兼容别名；R29 / D-63 补齐 `metrics` / `golden-regress`）
- 调用方（`runtime.js` / `selftest_all.js`）经 **`lib/inproc.js`** 同进程直调并捕获 stdout

`lib/inproc.js` 的两条护栏（缺一即会伤到调用方）：

| 护栏 | 若缺失的后果 |
|---|---|
| `process.exit()` → 抛异常并转为 `status` | 被调引擎参数校验失败时 `process.exit(1)`，会**杀死调用方进程** |
| 保存 / 恢复 `process.exitCode` | 被调引擎（如 `evolve selftest`）会设 `exitCode`，**污染调用方退出码** |

**（2）D-60 聚合门禁三态 —— 不再把"环境不可达"伪装成"代码失败"**

| 态 | 触发条件 | 输出 | 退出码 |
|---|---|---|---|
| ✅ PASS | 子命令 `EXIT===0` | `PASS` | — |
| ⚠️ SKIP | spawn 失败且 `EBUSY/EPERM/EACCES` | `SKIP`（环境不可达，非代码回归） | 2 |
| ❌ FAIL | 其余非零 / 超时 / 非环境类 spawn 失败 | `FAIL` + 子套件尾部输出 | 1 |

退出码契约：**`0`=全绿 / `1`=代码失败 / `2`=环境不可达**（CI 可区分而不误判）。
判定逻辑抽出为纯函数 `classifySpawn(res)` 并自带 `--selftest`（10 条用例）——否则受限宿主下
`FAIL` 分支永远触发不到，会留下**测不到的盲区**。

**成效（实测）**

| 指标 | R28 前 | R28 后 |
|---|---|---|
| `node selftest_all.js`（受限宿主） | 0/9 假 FAIL | **9/9 ALL GREEN（全 `[inproc]`）** → R29 **10/10** |
| `node runtime.js selftest` | 4 项断言失败 | **全绿** |
| 兜底路径 | 依赖 Python 手工脚本 | `selftest_all.py` 固化于包内；JS 版已自足，Python 仅作**独立复核** |

**边界与降级**：`ZODIAC_ENGINE_DIR` / `ZODIAC_BUS_JS` 指向不存在路径时，`tryLoad` 失败 →
自动降级子进程 → 按三态记 `SKIP`/`FAIL`（已实测两例）。

> 配套纪律：`selftest` 与 e2e 结束后必须自清理（临时资产文件 + `logs/rollback/` 中本次产生的回滚点），
> 并保证**幂等**——连跑两次后仓库状态一致、无残留。

### 10.8 套件全覆盖与接口一致性收尾（R29 / D-62 · D-63）

**背景**：D-61 的模块化在 R28 只覆盖了「门禁内」的 9 个 suite；`recovery.js` 因**没有 selftest 子命令**
而游离于门禁之外（10 个 JS 引擎中唯一），且 9 个引擎的导出名并不统一。

**（1）D-62 —— `recovery` 模块化 + 沙盒自检：门禁覆盖 9 → 10**

- 与其余引擎同构：路径根由 `const` 改为可 `rebindRoots()` 重绑定，顶层分发包进 `cli(argv)`，
  加 `require.main` 守卫 + `module.exports`
- 新增 `selftest`（**15 条断言**）。**硬约束：全程隔离在 `os.tmpdir()` 沙盒** —— 靠 `rebindRoots`
  把 `SRC`/`SKILLS`/快照根整体指向伪树，`finally` 中**先还原路径根、再清沙盒**。
  由此自检做到**毫秒级、可重复、生产零接触**：不碰 2.5 GB 级真实快照目录，不写入生产 `RECOVERY_LOG.jsonl`
- 取证面：递归计数 / `linkageMap`→双层技能解析 / 快照「双层 + 三层」双双落地 / `resolveName` 三态
  （精确·标签后缀·不存在）/ 基线标记往返 / `copyDirSafe` 往返一致 / `safeRename` + `safeRmDir` /
  `verify` 沙盒内可执行

**（2）D-63 —— 导出名统一为 `cli`**

`lib/inproc.js` 的 `entryOf()` **同时接受 `cli` 与 `main`**，故功能无碍；但 R28 遗留
`metrics` / `golden-regress` 导出 `main`，与其余 7 个引擎的 `cli` 不一致 —— 属"外表一致、内里两名"的
可维护性隐患。R29 统一为 `module.exports = { cli: main, main }`（`main` 保留作**向后兼容别名**）。

**成效（实测）**

| 指标 | R28 后 | R29 后 |
|---|---|---|
| `node selftest_all.js` | 9/9 ALL GREEN | **10/10 ALL GREEN（全 `[inproc]`）** |
| `python selftest_all.py`（独立路径） | 9/9 | **10/10** |
| 可 `require` 且零副作用 | 7/9（2 个导出名不一） | **9/9** |
| `recovery selftest` | 无 | **15 通过 / 0 失败**（连跑 3 次幂等，沙盒零残留） |

**零回归取证**（改前/改后**逐字节**对比 `list` / `baseline show` / `check` 三例）：三例完全一致 ✔；
`usage` 仅多出新增的 `selftest` 一行说明（**有意新增，非回归**）。

**证伪取证**：`ZODIAC_BUS_JS` 假路径 → 9/10 `FAIL bus`、退出码 1 ✔；
`ZODIAC_ENGINE_DIR` 指向不存在 → 1/10、退出码 1 ✔（通过路径与失败路径**均被真实触发**）。

> 判据：**「不在门禁内」不等于「无需一致性」**——游离的引擎会成为判据与命名的长期盲区。
> 隔离型自检的清理顺序是**先还原路径根、后删沙盒**（顺序颠倒会误删真实目录或留下悬挂指向）。

### 10.9 取证强度与留痕可达性（R30 / D-64 · D-65）

**背景**：R29 自认两项低危 gap——G1「`docs/EVOLUTION.md` 无字节级备份」、G2「`recovery` 有 1 条恒真断言」。
R30 先复核定性，再做修复；**两项中 1 项定性被修正**。

**（1）G2 定性成立 → D-64：恒真断言 → 数值断言**

R29 第 8 条断言写作 `verify(snapName); chk(true, '…无异常')`——**只要不抛异常即通过**，
不校验任何数值。这是**伪断言**：它出现在断言总数里，却**不产生任何取证力**。根因是 `verify()`
只 `console.log` 而不返回值，调用方无从读取数据。

修复：`verify()` 返回结构化结果（`snapshotFiles` / `liveFiles` / `jsonErrors` / 技能双向计数），
自检端改为 **5 条数值断言**（JSON 零错误 / live 数＝伪树实数 / 快照数＝源＋2 / 双·三层技能双向各＝1）。
两个既有调用点（CLI `verify`、自检取证）**均忽略返回值** → CLI 输出零影响（已逐字节回归）。

**（2）G1 定性被修正 → D-65：真根因是「重型快照不可达」，而非「备份清单漏了 docs」**

复核发现两点，令 G1 的原始表述（"沿用了 R28 对文档类的处理惯例"）不成立：

- `snapshot()` 拷贝的 `SRC` **本就包含 `docs/`**——不存在"docs 未被纳入快照范围"这回事
- 真实链条是：`snapshot()` = 全树 + 全量 skills，实测 7 个已占 **2.5 GB**（D-51）→
  **无法用于逐轮改动前的留痕** → 各轮转向"文件级 `cp`" → 文件级清单只列代码 →
  `docs/*.md` **自 R25 起 4 轮改动全部零备份**
  （实证：快照内 `EVOLUTION.md` 仍停留在 2026-07-30 的 8430 B 旧版，而现版 24279 B）

**对策**：新增 `light` 子命令——只备份**指定清单**（默认 `zodiac-team/docs` + `zodiac-team/scripts`），
秒级完成，并生成 `MANIFEST.json`（逐文件 `path` / `size` / `sha256`）。与重型快照构成**分层**：

| 层 | 命令 | 体量 | 频率 | 覆盖 |
|---|---|---|---|---|
| 重型 | `snapshot <label>` | 全树 + 全量 skills（**~350 MB / 个**） | 里程碑 | 插件全树 + 双/三层技能 |
| 轻量 | `light <label> [path…]` | 清单式（实测 **20 文件 / 307 KB / 1.35 s**） | **逐轮** | 默认 docs + scripts |

**取证（实测）**

| 项 | 结果 |
|---|---|
| `recovery selftest` | **23 通过 / 0 失败**（R29 的 15 条：−1 伪断言，+5 verify 量化，+4 light） |
| `node selftest_all.js` | 10/10 ALL GREEN（全 `[inproc]`） |
| CLI 零回归 | `list` / `baseline show` / `check` **逐字节一致**；`usage` 仅多 light 一行（有意新增） |
| MANIFEST 可信度 | Python **独立重算 20/20 匹配**、字节合计一致（不采信 node 侧自报） |
| light 实跑 | 1.35 s、20 文件、307 401 B；`docs/EVOLUTION.md` 的 SHA **＝ R29 账本 `sha_after`** |
| 零污染 | 真实快照仍 7 个（未增未减）、沙盒残留 0、连跑 3 次幂等 |

> 判据：**断言必须"能失败"**——恒真断言（`chk(true, …)`）在总数上冒充取证力，比没有断言更危险，
> 因为它制造"已验证"的错觉。
> 判据：**留痕机制若因体量而不可执行，纪律必然断裂**——与其反复要求"记得备份"，
> 不如让留痕便宜到顺手（`light` 把单轮留痕成本从"分钟级 / 350 MB"降到"秒级 / 300 KB"）。
> 配套：契约类文档（`docs/*.md`）与代码**同等对待**——本轮起纳入 `light` 默认清单，改前必留痕。

### 10.10 快照体量纪律与分层（R31 + R32 / D-66 ~ D-69 · D-51a · D-51b）

**背景（D-51 真根因）**：`snapshot()` 原为「全树 + 全量 skills」三层拷贝。取证发现：全库 2633 个技能中
仅 **13** 个被 `settings.json` 引用，且**全部已落在双层内**；其余 2620 个与生肖团零关联 →
**三层 = 2320 MB 换 0 覆盖增量**。

| 改动 | 内容 |
|---|---|
| **D-66** | 三层（`skills_global`）由「默认」改为 **opt-in**（`snapshot <label> --full`）；默认只做双层 |
| **D-67** | `LITE_DEFAULT_PATHS` 纳入 `zodiac-team/settings.json`（改前留痕必须覆盖配置真源） |
| **D-68** | 新增 `light-prune <N> [--yes]` —— 默认干跑，`--yes` 移入 `lite/_trash`（**非物理删除**） |
| **D-69** | `list` 标注含三层者 + 文件数（体量可见性） |
| **D-51a** | 新增 `snapshot-prune [N] [--yes]` —— **基线保护** + 保留最近 N + 移入 `snapshots/_trash` |
| **D-51b** | `evolve.apply` 兜底快照由 `evo_<uid>`（每轮新增，实测累积 5 个 ≈12 GB 物理）改为**固定名** `evo_pre_apply` |

**实测**：单轮重型快照 2.5 GB → **167 MB**（双层）。

> 判据：**体量与频率必须匹配**。安全网不该贵到用不起——否则纪律必然退化为「挑着做」。

### 10.11 快照的原子性：退路本身不能"先毁后建"（R33 / D-70 · D-71）

**现象**：R32 端到端发现 `evolve.apply` 报「未捕获异常」。逐层取证后定性为**环境**
（宿主 safe-delete 通道 `genie-trash` 超时 / `SAFE_DELETE_FAIL_CLOSED`），
**不是引擎缺陷**（退出码 0，apply 如实降级并继续落地）。

**但取证途中挖出真缺陷 D-70（本轮最高 severity）**：固定名快照的覆盖路径是

    旧: clearDir(dest);  copyDir(SRC, dest)      ← 先毁退路、再重建

在「批量删除失败」的环境下 `clearDir` **半途失败**，旧快照被毁成半残。
实测铁证：`evo_pre_apply` 2649 文件中 **42 个被销毁**（`ai-data-copilot` 整体消失、`ai-engineer` 46→26），
账目闭合（`1722 = 1764 − 42`）。快照是本工具兑现「改前必留退路」的**物证本身，
它不能自己也先毁后建**。

**对策（四步；任一步在换入前失败都不触碰 `dest`）**

    ① 在唯一 staging 上构建（dest 全程不动）
    ② dest → __old 挪开（失败即中止，dest 原样）
    ③ staging → dest 顶上（失败则把 __old 还原回 dest，不留空窗）
    ④ 尽力清 __old —— 走三级降级链 retireDir：物理清理 → 移入 _trash → 仅告警

**D-71（同轮发现）**：`logEntry` 原为 `catch(_){}` **完全静默吞错**。实证：2026-09-23 22:19 快照成功落盘，
而 `RECOVERY_LOG.jsonl` **无该行**（mtime 停在 22:15）—— 审计链静默断链。对取证型工具，
**静默丢审计行比报错更危险**。对策：写失败先重试 1 次（H: 卷存在间歇 EPERM），
仍失败则 **stderr 告警 + 返回 `false`**（不污染 stdout 契约，CLI 逐字节回归不受影响）。

**新增内部保留名**：`__staging_` / `__old_` 属「原子换入」内部件，须被 `listSnapDirs` 过滤
（否则会被 prune 当候选、被 verify 误读），并由 `list` 显式列出残留（体量可见性）。

**取证（R33 实测）**

| 项 | 结果 |
|---|---|
| `recovery selftest` | 39 → **48 通过 / 0 失败**（+9：原子性 4 · 内部件识别 1 · 失败路径 2 · D-71 2） |
| 双路门禁 | `node selftest_all.js` **10/10** ｜ `python selftest_all.py` **10/10** |
| CLI 零回归 | `baseline show` / `check` / `usage` **逐字节一致**；`list` 仅多一行 `_trash` 可见性提示（有意新增） |
| 端到端 | **17/17**：累积恒 1 · `snapshotReal=true` · 规模同刻一致（1777 = 1777）· 零残留 · **逐包零缺失** |
| 受损快照 | 已按新路径重建：2649 → **2688**（插件 1761 + 双层技能 927），逐包差异**为空** |

> 判据：**"改前必留退路"要先作用于退路本身**。一个会毁掉自己退路的退路机制，比没有退路更危险——
> 它让人以为有退路。
> 判据：**降级必须响亮**。同级三个失败模式（删除失败 / 审计写失败 / 快照失败）全部改为**可见**，
> 且**不丢数据**（删不掉就隔离进 `_trash`：数据完好，仅占盘，`list` 可见）。

**D-72（同族新发现）**：`evolve.js selftest` 的夹具 `prompts/_selftest_evolve.{txt,json}` **落在生产包体内**，
清理走 `catch(_){}` —— 与 D-71 同一病理（静默吞错）。删除通道正常时它每轮自清，缺陷不可见；
一旦删除失败，夹具**静默留在包体**并随后被快照收录，而自检对外宣称"包内零残留"。

> 夹具**不能**移出 `BASE`：`validatePatch` 明确拒绝绝对路径与 `..`，那是 **D-50 越权守卫**
> （引擎源码不可写），为省事放宽它才是真错误。
> 故对策只做一件事：**让残留说话** —— stderr 告警 + 计入自检结论文本（`包内零残留 ✅` / `⚠残留 N 项`）。
> **不**改 exit code —— 环境不可达与代码失败必须分态（D-60），否则门禁会被环境噪声染红。
> 判据：**同一病理出现两次即应上升为模式**。D-71 与 D-72 相隔不到 1 小时、同为 `catch(_){}`：
> 「静默清理」这条纪律，应当直接写进本包的编码约定 —— 凡清理/退场路径，要么成功，要么**可见地**失败。
