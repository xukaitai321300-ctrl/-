# Changelog

# 元层工具 - ComfyUI参数调优 & 技能优化专家


Format: [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
Versioning: [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/)

---

## [Unreleased]

### Added
- 

### Changed
- 

---

## [v7.2.3] - 2026-09-22

### Fixed
- **代码围栏补齐（第十轮 F 类，含此前判据漏收的 `markdown` 型）**：1 处代码块的开启围栏
  反引号丢失，只剩孤立语言词。围栏总数 36 → 38（偶数）；错位 0 处 · 末尾已闭合 ·
  来源追踪校验通过（原文逐行全覆盖，**零删除零改文**）。
  - 边界判据 v3：向前取**第一个命中**者 —— `> 📄 代码已提取到` / `> [引用] 完整代码已提取到` /
    已有围栏 / 文档级标题（`### X. 标题`）；**不使用普通标题**（markdown 内容自带标题会截断段）。
  - 工具：`evolution/fix_r9_fences.py` v3 + 判据公共库 `evolution/fence_lib.py`。markdown 型 1 处（第九轮判据漏收）

## [v7.2.2] - 2026-09-22

### Fixed
- **代码围栏补齐（第九轮 F 类）**：历史「代码提取到 `references/`」操作导致 1 处代码块的
  **开启围栏反引号丢失**，只剩孤立语言词（`json` / `python` / `diff` 等）。后果：围栏总数变奇数
  → 其后所有配对整体反转 → 渲染时大段正文被吞进代码块、段落代码裸露为普通文本。
  - 修复：1 处语言词 → ` ```lang `；段尾补闭合围栏（围栏总数 34 → 36，偶数）
  - 验收：错位 0 处 · 末尾已闭合 · **来源追踪校验通过**（原文逐行全覆盖，零删除零改文）
  - 工具：`evolution/fix_r9_fences.py`（新增，含三重自洽硬门槛）

## [v7.2.1] - 2026-09-22

### Changed
- **角色身份澄清**：H1「Skill Optimizer — 猴（参数调优 & 技能优化双专家）」→「Skill Optimizer — 元层工具（…）」
  - 实锤依据：`zodiac-team` agents 层中「猴」已由 `monkey-design-adjuster` 持有；本技能不在 12 生肖执行层，属**元层工具**
- 文内自指「🐵猴」→「🔧技能优化器」（5 处），消除与生肖猴的歧义
- 旧代号收敛：「🐲 龙二」→「🐵 猴」（8 处）；「🐦 凤 / 🐦凤」→「🐦 进化编排器」（12 处）；「十四生肖团」→「十二生肖团」
- 本 CHANGELOG 标题「# 猴 - ComfyUI参数调优专家」→「# 元层工具 - ComfyUI参数调优 & 技能优化专家」
- 明确本工具**非十二生肖成员**，属扩展元层；「参数调优」职能的唯一归属方

### Fixed
- **D-26 联动链角色纠正（5 处）**：本工具自身联动链里 🐵 被当作「调优执行者」——与「本工具」同义重复
  → 统一改为「⚙ 本工具」（调优方 = 本工具，🐵猴 = 设计调整方）
  - `**联动链1：🐔→🐵→🐑**` → `🐔→⚙ 本工具→🐑`
  - `**联动链2：🐵→🐴→⚙**` → `⚙ 本工具→🐴→⚙进化编排`
  - `→ 调用🐵进行参数调优` → `→ 本工具进行参数调优`
- **D-34 「🐲二」清理（1 处）**
- 角色定性纠正：`> 本技能（猴·参数调优）吸收其` → `> 本技能（**元层**·参数调优）吸收其`

### Removed（归档，非删除）
- `SKILL_trimmed.md`（v3.0 旧快照，15341B）→ 归档至 `_archive_20260922/skill-backups/zheng10-skill-optimizer/SKILL_trimmed.md.v3.0-old`
  - 原因：与当前 v7.2 并存冲突；旧 B 类判据未覆盖 `trimmed` 命名（已同步修工具至 v1.2）

## [v6.0] - 2026-06-08

### Added
- 新增自动化参数调优指标
- 新增参数对比检测功能

### Changed
- 版本从 v5.0 升级到 v6.0
- 明确角色为猴（参数调优），与龙二（设计调整）区分
- 更新 YAML frontmatter 格式（符合 agentskills.io 规范）

### Fixed
- 修复评分低于阈值问题（48.5 -> 62.0，通过内容优化）
- 修复 expert_linkage 错误声明（无对应 expert，已设为 false）

---

## [v5.0] - 2026-05-18

### Added
- Initial skill package creation
- Basic skill description and trigger words
- Expert linkage setup
