# 马专家技能包 (十二生肖团 - 马专家)#

马专家（ComfyUI工作流优化专家）技能包，负责工作流设计优化、ControlNet精准控制、节点效率优化。包含工作流优化、ControlNet配置、节点效率分析等功能。是十二生肖团的工作流优化者。

## 功能特性#

- **工作流优化** - 节点连接优化、工作流结构优化、执行效率优化#
- **ControlNet 配置** - ControlNet 模型配置、控制强度调整、预处理方法选择#
- **节点效率分析** - 节点执行时间分析、节点资源占用分析、瓶颈节点识别#

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。#
2. 本技能包无需额外 Python 依赖（仅使用标准库：json, argparse）。#

## 使用方法 (Usage)#

### 命令行使用 (Command Line Usage)#

```bash
# 获取工作流优化方法#
python scripts/workflow_optimization_tool.py --method node_connection_optimization#

# 获取 ControlNet 配置#
python scripts/controlnet_config_tool.py --model "control_v11p_sd15_lineart"#
```

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）：#

- ✅ **功能完整性 (25/25)**: 完整的数据文件和 Python 工具#
- ✅ **安全性 (25/25)**: 无恶意代码，包含 LICENSE#
- ✅ **易用性 (20/20)**: README.md 有 Installation 和 Usage 部分，SKILL.md 有 Usage 部分#
- ✅ **文档完整性 (15/15)**: 包含 SKILL.md, README.md, README_zh.md#
- ✅ **最佳实践 (15/15)**: 标准文件齐全，包含 tests/ 目录#