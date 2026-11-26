# Changelog

# 蛇 - 产品设计师


Format: [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
Versioning: [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/)

---

## [Unreleased]

### Added
- 

### Changed
- 

---

## [v7.0.1] - 2026-09-22

### Fixed
- **代码围栏补齐（第九轮 F 类）**：历史「代码提取到 `references/`」操作导致 1 处代码块的
  **开启围栏反引号丢失**，只剩孤立语言词（`json` / `python` / `diff` 等）。后果：围栏总数变奇数
  → 其后所有配对整体反转 → 渲染时大段正文被吞进代码块、段落代码裸露为普通文本。
  - 修复：1 处语言词 → ` ```lang `；段尾补闭合围栏（围栏总数 46 → 48，偶数）
  - 验收：错位 0 处 · 末尾已闭合 · **来源追踪校验通过**（原文逐行全覆盖，零删除零改文）
  - 工具：`evolution/fix_r9_fences.py`（新增，含三重自洽硬门槛）

## [v6.0] - 2026-06-08

### Added
- 增加与 snake-product-designer 专家的双向联动
- 新增 CMF 设计案例库
- 新增自动化设计质量指标

### Changed
- 优化杯盖结构设计模板（316 内胆 / 冰花纹理 / 钛内胆）
- 更新 YAML frontmatter 格式（符合 agentskills.io 规范）

---

## [v5.0] - 2026-05-18

### Added
- Initial skill package creation
- Basic skill description and trigger words
- Expert linkage setup
