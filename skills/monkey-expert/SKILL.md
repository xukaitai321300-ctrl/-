---
name: monkey-expert
description: 猴专家（ComfyUI参数调优专家）技能包，负责参数迭代优化、模型调优、A/B测试。包含参数调优、模型微调、A/B测试、性能评估等功能。是十二生肖团的参数调优者。
version: 1.2.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-06
tags: [monkey-expert, parameter-tuning, model-fine-tuning, a/b-testing, twelve-zodiac-team]
dependencies: [python>=3.8, json, argparse, numpy, pandas]
---

# 猴专家（ComfyUI参数调优专家）技能包

## 功能概述

本技能包提供 ComfyUI 参数调优功能，包含：

1. **参数调优** - 提示词权重调整、采样参数优化、VAE参数优化、ControlNet参数优化
2. **模型微调** - LoRA 权重调整、Textual Inversion 参数优化、模型融合参数调整
3. **A/B 测试** - 参数组合对比测试、生成质量评估、最优参数推荐
4. **性能评估** - 生成速度评估、显存占用评估、生成质量评估

猴专家是十二生肖团的**参数调优者**，负责参数迭代优化、模型调优、A/B测试。在十二生肖团工作流中，猴专家位于第5阶段（AI生图阶段），接收羊专家的生成图，进行参数调优，然后将优化后的参数返回给羊专家重新生成。

## 安装 (Installation)

1. 确保已安装 Python 3.8+。
2. 安装依赖库：
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
3. 本技能包无需额外配置，开箱即用。

## 使用方法 (Usage)

### 命令行使用 (Command Line Usage)

```bash
# 调优参数（提示词权重调整）
python scripts/parameter_tuning_tool.py --prompt "a vacuum cup" --steps 30 --cfg_scale 7.5

# 微调模型（LoRA 权重调整）
python scripts/model_fine-tuning_tool.py --model "stable-diffusion-v1-5" --lora "path/to/lora.safetensors" --lora_weight 0.7

# A/B 测试（参数组合对比测试）
python scripts/ab_testing_tool.py --config "path/to/config.json" --test_count 5

# 性能评估（生成速度评估）
python scripts/performance_evaluation_tool.py --image_dir "path/to/images" --metric "speed"
```

### Python 使用 (Python Usage)

```python
from monkey_expert import ParameterTuner, ModelFineTuner, ABTester

# 创建参数调优器
tuner = ParameterTuner()

# 调优提示词权重
optimized_params = tuner.tune_promptWeight(
    prompt="a vacuum cup",
    original_weight=1.0,
    target_score=90
)

# 创建模型微调器
finetuner = ModelFineTuner()

# 微调 LoRA 权重
optimized_lora = finetuner.tuneLoraWeight(
    model="stable-diffusion-v1-5",
    lora_path="path/to/lora.safetensors",
    original_weight=0.5,
    target_score=90
)

# 创建 A/B 测试器
abtester = ABTester()

# 执行 A/B 测试
ab_results = abtester.runTest(
    config_path="path/to/config.json",
    test_count=5
)

# 获取最优参数
best_params = abtester.getBestParams(ab_results)
```

## 详细功能说明

### 1. 参数调优 (Parameter Tuning)

#### 1.1 提示词权重调整 (Prompt Weight Adjustment)

**功能**：调整提示词中各个关键词的权重，以优化生成图的质量。

**输入**：
- `prompt`：提示词字符串（例如："a vacuum cup, magnesium alloy, lightweight"）
- `original_weight`：原始权重（默认：1.0）
- `target_score`：目标评分（默认：90）

**输出**：
- `optimized_params.json`：优化后的参数配置，包含：
  - `prompt`：优化后的提示词
  - `weights`：各个关键词的权重
  - `expected_score`：预期评分

**示例**：
```bash
python scripts/parameter_tuning_tool.py --prompt "a vacuum cup, magnesium alloy, lightweight" --original_weight 1.0 --target_score 90
```

**输出文件示例** (`optimized_params.json`)：
```json
{
  "prompt": "a vacuum cup, (magnesium alloy:1.2), (lightweight:1.1)",
  "weights": {
    "magnesium alloy": 1.2,
    "lightweight": 1.1
  },
  "expected_score": 92
}
```

#### 1.2 采样参数优化 (Sampling Parameter Optimization)

**功能**：优化采样参数（steps、cfg_scale、sampler等），以平衡生成质量和生成速度。

**输入**：
- `steps`：采样步数（默认：30）
- `cfg_scale`：CFG缩放因子（默认：7.5）
- `sampler`：采样器（默认："DPM++ 2M Karras"）

**输出**：
- `optimized_sampling_params.json`：优化后的采样参数

**示例**：
```bash
python scripts/parameter_tuning_tool.py --steps 30 --cfg_scale 7.5 --sampler "DPM++ 2M Karras"
```

#### 1.3 VAE参数优化 (VAE Parameter Optimization)

**功能**：优化VAE参数（VAE模型选择、VAE精度等），以提升生成图的细节和真实感。

**输入**：
- `vae_model`：VAE模型（默认："sd-vae-ft-mse"）
- `vae_precision`：VAE精度（默认："fp16"）

**输出**：
- `optimized_vae_params.json`：优化后的VAE参数

**示例**：
```bash
python scripts/parameter_tuning_tool.py --vae_model "sd-vae-ft-mse" --vae_precision "fp16"
```

#### 1.4 ControlNet参数优化 (ControlNet Parameter Optimization)

**功能**：优化ControlNet参数（ControlNet模型选择、权重、引导强度等），以提升生成图的控制精度。

**输入**：
- `controlnet_model`：ControlNet模型（默认："control_v11p_sd15_canny"）
- `controlnet_weight`：ControlNet权重（默认：1.0）
- `controlnet_guidance`：ControlNet引导强度（默认：1.0）

**输出**：
- `optimized_controlnet_params.json`：优化后的ControlNet参数

**示例**：
```bash
python scripts/parameter_tuning_tool.py --controlnet_model "control_v11p_sd15_canny" --controlnet_weight 1.0 --controlnet_guidance 1.0
```

### 2. 模型微调 (Model Fine-tuning)

#### 2.1 LoRA 权重调整 (LoRA Weight Adjustment)

**功能**：调整LoRA模型的权重，以平衡风格强度和生成质量。

**输入**：
- `model`：基础模型（例如："stable-diffusion-v1-5"）
- `lora_path`：LoRA模型路径
- `lora_weight`：LoRA权重（默认：0.5）
- `target_score`：目标评分（默认：90）

**输出**：
- `optimized_lora_params.json`：优化后的LoRA参数

**示例**：
```bash
python scripts/model_fine-tuning_tool.py --model "stable-diffusion-v1-5" --lora "path/to/lora.safetensors" --lora_weight 0.7 --target_score 90
```

#### 2.2 Textual Inversion 参数优化 (Textual Inversion Parameter Optimization)

**功能**：优化Textual Inversion参数（embedding权重等），以提升特定概念的生成质量。

**输入**：
- `embedding_path`：Textual Inversion embedding路径
- `embedding_weight`：embedding权重（默认：1.0）

**输出**：
- `optimized_embedding_params.json`：优化后的embedding参数

**示例**：
```bash
python scripts/model_fine-tuning_tool.py --embedding "path/to/embedding.pt" --embedding_weight 1.0
```

#### 2.3 模型融合参数调整 (Model Fusion Parameter Adjustment)

**功能**：调整模型融合参数（融合比例等），以结合多个模型的优势。

**输入**：
- `model1_path`：模型1路径
- `model2_path`：模型2路径
- `fusion_ratio`：融合比例（默认：0.5）

**输出**：
- `optimized_fusion_params.json`：优化后的融合参数

**示例**：
```bash
python scripts/model_fine-tuning_tool.py --model1 "path/to/model1.safetensors" --model2 "path/to/model2.safetensors" --fusion_ratio 0.5
```

### 3. A/B 测试 (A/B Testing)

#### 3.1 参数组合对比测试 (Parameter Combination Comparison Test)

**功能**：对比测试多个参数组合，找出最优参数组合。

**输入**：
- `config_path`：配置文件路径（JSON格式，包含多个参数组合）
- `test_count`：每个参数组合的测试次数（默认：5）

**输出**：
- `ab_test_results.json`：A/B测试结果，包含：
  - `configs`：参数组合列表
  - `results`：每个参数组合的测试结果（平均分、标准差、生成时间）
  - `best_config`：最优参数组合

**示例**：
```bash
python scripts/ab_testing_tool.py --config "path/to/config.json" --test_count 5
```

**配置文件示例** (`config.json`)：
```json
[
  {
    "name": "Config A",
    "params": {
      "steps": 30,
      "cfg_scale": 7.5,
      "sampler": "DPM++ 2M Karras"
    }
  },
  {
    "name": "Config B",
    "params": {
      "steps": 50,
      "cfg_scale": 9.0,
      "sampler": "Euler a"
    }
  }
]
```

#### 3.2 生成质量评估 (Generation Quality Evaluation)

**功能**：评估生成图的质量（使用鸡专家的评审标准）。

**输入**：
- `image_dir`：生成图目录
- `evaluation_criteria`：评估标准（默认：鸡专家评审标准）

**输出**：
- `quality_evaluation_results.json`：质量评估结果

**示例**：
```bash
python scripts/ab_testing_tool.py --image_dir "path/to/images" --evaluation_criteria "rooster_standard"
```

#### 3.3 最优参数推荐 (Optimal Parameter Recommendation)

**功能**：根据A/B测试结果，推荐最优参数组合。

**输入**：
- `ab_test_results_path`：A/B测试结果文件路径
- `optimization_target`：优化目标（默认："quality"，可选："quality"、"speed"、"balance"）

**输出**：
- `best_params_recommendation.json`：最优参数推荐

**示例**：
```bash
python scripts/ab_testing_tool.py --ab_test_results "path/to/ab_test_results.json" --optimization_target "quality"
```

### 4. 性能评估 (Performance Evaluation)

#### 4.1 生成速度评估 (Generation Speed Evaluation)

**功能**：评估生成速度（平均生成时间、显存占用等）。

**输入**：
- `image_dir`：生成图目录
- `metric`：评估指标（默认："speed"，可选："speed"、"memory"、"all"）

**输出**：
- `speed_evaluation_results.json`：速度评估结果

**示例**：
```bash
python scripts/performance_evaluation_tool.py --image_dir "path/to/images" --metric "speed"
```

#### 4.2 显存占用评估 (Memory Usage Evaluation)

**功能**：评估显存占用（峰值显存、平均显存等）。

**输入**：
- `image_dir`：生成图目录
- `metric`：评估指标（默认："memory"，可选："speed"、"memory"、"all"）

**输出**：
- `memory_evaluation_results.json`：显存占用评估结果

**示例**：
```bash
python scripts/performance_evaluation_tool.py --image_dir "path/to/images" --metric "memory"
```

#### 4.3 生成质量评估 (Generation Quality Evaluation)

**功能**：评估生成质量（使用鸡专家的评审标准）。

**输入**：
- `image_dir`：生成图目录
- `metric`：评估指标（默认："quality"，可选："quality"、"speed"、"memory"、"all"）

**输出**：
- `quality_evaluation_results.json`：质量评估结果

**示例**：
```bash
python scripts/performance_evaluation_tool.py --image_dir "path/to/images" --metric "quality"
```

## 输出文件格式

本文档的输出文件格式已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\输出文件格式规范_20260606_v1.0.md`

## 数据传输说明

本文档的数据传输说明已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\数据传输说明规范_20260606_v1.0.md`

## 案例分析

本文档的案例分析已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\案例分析集_20260606_v1.0.md`

## FAQ

本文档的FAQ已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\FAQ集_20260606_v1.0.md`

## 技能包质量

本技能包设计目标质量分数：**95+**（目标：100/100）

**当前质量分数**：92/100

**质量改进计划**：
1. **补充更多案例**（2026-06）：增加3个实际案例（车载保温杯、智能保温杯、儿童保温杯）
2. **优化A/B测试算法**（2026-07）：使用贝叶斯优化算法，减少测试次数，提升优化效率
3. **增加性能评估维度**（2026-08）：增加"生成稳定性"评估（多次生成的结果一致性）

## 版本历史

本文档的版本历史已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\版本历史集_20260606_v1.0.md`

