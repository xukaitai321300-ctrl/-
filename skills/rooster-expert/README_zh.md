# 鸡专家技能包 (十二生肖团 - 鸡专家)#

鸡专家（AI生图评审专家）技能包，负责评审生成图质量、质量守门员。包含生图质量评审、质量守门员、评审标准管理等功能。是十二生肖团的生图质量把关者。

## 功能特性#

- **生图质量评审** - 真实感评估、材质感评估、灯光自然度评估#
- **质量守门员** - 一票否决权、质量红线管理、评审标准执行#
- **评审标准管理** - 评审标准制定、标准更新、标准执行监督#

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。#
2. 本技能包无需额外 Python 依赖（仅使用标准库：json, argparse）。#

## 使用方法 (Usage)#

```bash
# 评审生成图质量#
python scripts/image_review_tool.py --image "path/to/image.jpg"#

# 执行质量守门员功能#
python scripts/quality_gatekeeper_tool.py --image "path/to/image.jpg" --standard "high"#
```

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）