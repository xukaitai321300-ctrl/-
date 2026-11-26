# Changelog

# 牛 - ComfyUI工作流标准专家


Format: [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
Versioning: [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/)

---

## [Unreleased]

### Added
- 

### Changed
- 

---

## [v7.2.2] - 2026-09-22

### Fixed
- **代码围栏补齐（第十轮 F 类，含此前判据漏收的 `markdown` 型）**：2 处代码块的开启围栏
  反引号丢失，只剩孤立语言词。围栏总数 76 → 80（偶数）；错位 0 处 · 末尾已闭合 ·
  来源追踪校验通过（原文逐行全覆盖，**零删除零改文**）。
  - 边界判据 v3：向前取**第一个命中**者 —— `> 📄 代码已提取到` / `> [引用] 完整代码已提取到` /
    已有围栏 / 文档级标题（`### X. 标题`）；**不使用普通标题**（markdown 内容自带标题会截断段）。
  - 工具：`evolution/fix_r9_fences.py` v3 + 判据公共库 `evolution/fence_lib.py`。markdown 型 2 处（第九轮判据漏收）

## [v7.2.1] - 2026-09-22

### Fixed
- **代码围栏补齐（第九轮 F 类）**：历史「代码提取到 `references/`」操作导致 26 处代码块的
  **开启围栏反引号丢失**，只剩孤立语言词（`json` / `python` / `diff` 等）。后果：围栏总数变奇数
  → 其后所有配对整体反转 → 渲染时大段正文被吞进代码块、段落代码裸露为普通文本。
  - 修复：26 处语言词 → ` ```lang `；段尾补闭合围栏（围栏总数 25 → 76，偶数）
  - 验收：错位 0 处 · 末尾已闭合 · **来源追踪校验通过**（原文逐行全覆盖，零删除零改文）
  - 工具：`evolution/fix_r9_fences.py`（新增，含三重自洽硬门槛）另含 `> [引用] 完整代码已提取到` 型段尾标记 3 处

## [v6.0] - 2026-06-08

### Added
- 增加与 ox-standards-analyst 专家的双向联动
- 新增 DFM（可制造性）分析工作流节点标准

### Changed
- 更新工作流规范模板（适配 SDXL 和 ControlNet 节点）
- 更新 YAML frontmatter 格式（符合 agentskills.io 规范）

---

## [v5.0] - 2026-05-18

### Added
- Initial skill package creation
- Basic skill description and trigger words
- Expert linkage setup
