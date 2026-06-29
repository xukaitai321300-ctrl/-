# Changelog

# 猴 - ComfyUI参数调优专家


Format: [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)
Versioning: [Semantic Versioning 2.0.0](https://semver.org/lang/zh-CN/)

---

## [Unreleased]

### Added
- 

### Changed
- 

---

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
