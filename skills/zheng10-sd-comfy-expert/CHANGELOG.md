# Changelog

# 马 - SD/ComfyUI专家


Format: [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
Versioning: [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/)

---

## [Unreleased]

### Added
- 

### Changed
- 

---

## [v7.2.1] - 2026-09-22

### Fixed
- **代码围栏补齐（第九轮 F 类）**：历史「代码提取到 `references/`」操作导致 1 处代码块的
  **开启围栏反引号丢失**，只剩孤立语言词（`json` / `python` / `diff` 等）。后果：围栏总数变奇数
  → 其后所有配对整体反转 → 渲染时大段正文被吞进代码块、段落代码裸露为普通文本。
  - 修复：1 处语言词 → ` ```lang `；段尾补闭合围栏（围栏总数 10 → 12，偶数）
  - 验收：错位 0 处 · 末尾已闭合 · **来源追踪校验通过**（原文逐行全覆盖，零删除零改文）
  - 工具：`evolution/fix_r9_fences.py`（新增，含三重自洽硬门槛）

## [v6.0] - 2026-06-08

### Added
- 增加与 horse-rendering-expert 专家的双向联动
- 新增 ControlNet 使用指南和配置模板

### Changed
- 优化 ComfyUI 工作流搭建流程
- 更新 YAML frontmatter 格式（符合 agentskills.io 规范）

---

## [v5.0] - 2026-05-18

### Added
- Initial skill package creation
- Basic skill description and trigger words
- Expert linkage setup
