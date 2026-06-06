# 猴专家技能包 (十二生肖团 - 猴专家)#

猴专家（ComfyUI参数调优专家）技能包，负责参数迭代优化、模型调优、A/B测试。包含参数调优、模型微调、A/B测试、性能评估等功能。是十二生肖团的参数调优者。

## 功能特性#

- **参数调优** - 提示词权重调整、采样参数优化、VAE参数优化#
- **模型微调** - LoRA 权重调整、Textual Inversion 参数优化、模型融合参数调整#
- **A/B 测试** - 参数组合对比测试、生成质量评估、最优参数推荐#

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。#
2. 本技能包无需额外 Python 依赖（仅使用标准库：json, argparse）。#

## 使用方法 (Usage)#

```bash
# 调优参数#
python scripts/parameter_tuning_tool.py --prompt "a vacuum cup" --steps 30#

# 微调模型#
python scripts/model_fine-tuning_tool.py --model "stable-diffusion-v1-5" --lora "path/to/lora.safetensors"#

# A/B 测试#
python scripts/ab_testing_tool.py --config "path/to/config.json"#
```

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）