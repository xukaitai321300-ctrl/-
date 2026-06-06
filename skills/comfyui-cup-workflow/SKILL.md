---
name: comfyui-cup-workflow
description: 保温杯专属ComfyUI工作流 - 生成保温杯设计图
tags: ["comfyui", "cup", "design", "workflow", "image-generation"]
---

# 保温杯专属ComfyUI工作流 (comfyui-cup-workflow)

本技能提供保温杯专属的ComfyUI工作流文件，用于生成高质量保温杯设计图。

## 功能概述#

### 1. 基础设计工作流
- 文生图：根据文字描述生成保温杯设计
- 图生图：根据参考图生成变体
- 批量生成：一次生成多个设计方案

### 2. 高级设计工作流
- 结构设计：生成保温杯结构图
- 爆炸图：生成零件爆炸图
- 渲染图：生成产品级渲染图#

### 3. 专用模型
- 保温杯结构模型
- 材料质感模型
- 产品渲染模型#

## 使用方法#

### 基础文生图
```bash
# 使用基础设计工作流
python scripts/run_workflow.py \
  --workflow workflows/cup_design_basic.json \
  --prompt "现代简约不锈钢保温杯，弹跳盖设计，车载适用" \
  --output designs/cup_basic_001.png
```

### 高级图生图
```bash
# 使用高级设计工作流
python scripts/run_workflow.py \
  --workflow workflows/cup_design_advanced.json \
  --image inputs/reference_cup.png \
  --prompt "change color to black, add logo" \
  --output designs/cup_advanced_001.png
```

### 批量生成
```bash
# 批量生成设计方案
python scripts/batch_generate.py \
  --workflow workflows/cup_design_basic.json \
  --prompts configs/prompts.txt \
  --output-dir designs/batch/
```

## 安装#

```bash
# 1. 安装ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt

# 2. 下载专用模型
python scripts/download_models.py

# 3. 启动ComfyUI
python main.py --listen 0.0.0.0 --port 8188
```

## CLI 用法#

```bash
# 查看帮助
python scripts/comfyui-cup-workflow.py --help

# 文生图（基础）
python scripts/comfyui-cup-workflow.py text2img \
  --prompt "现代简约不锈钢保温杯，弹跳盖设计" \
  --negative-prompt "low quality, blurry" \
  --output designs/cup_001.png \
  --steps 30 \
  --cfg-scale 7.5 \
  --sampler "DPM++ 2M Karras"

# 图生图（高级）
python scripts/comfyui-cup-workflow.py img2img \
  --image inputs/reference_cup.png \
  --prompt "change material to magnesium alloy" \
  --output designs/cup_variant_001.png \
  --denoise 0.75

# 批量生成
python scripts/comfyui-cup-workflow.py batch \
  --prompts configs/prompts.txt \
  --output-dir designs/batch/ \
  --count 10

# 使用自定义工作流
python scripts/comfyui-cup-workflow.py custom \
  --workflow workflows/cup_structure.json \
  --params '{"cup_type": "vacuum", "material": "stainless_steel"}' \
  --output designs/cup_structure_001.png
```

## 示例#

### 示例1: 文生图 - 基础保温杯设计
```bash
python scripts/comfyui-cup-workflow.py text2img \
  --prompt "Modern minimalist stainless steel vacuum cup, bounce lid design, car cup holder compatible, product rendering, 8k" \
  --negative-prompt "low quality, blurry, distorted, bad anatomy" \
  --output designs/cup_basic_001.png \
  --steps 30 \
  --cfg-scale 7.5 \
  --sampler "DPM++ 2M Karras" \
  --width 1024 \
  --height 1024
```

**输出**: `designs/cup_basic_001.png` - 基础保温杯设计图。

### 示例2: 图生图 - 生成材料变体
```bash
python scripts/comfyui-cup-workflow.py img2img \
  --image designs/cup_basic_001.png \
  --prompt "change material to magnesium alloy AE44, keep design" \
  --output designs/cup_magnesium_001.png \
  --denoise 0.75 \
  --steps 30
```

**输出**: `designs/cup_magnesium_001.png` - 镁合金版本设计图。

### 示例3: 批量生成 - 不同颜色方案
```bash
# 创建提示词文件
cat > configs/color_variants.txt << EOF
Modern minimalist stainless steel vacuum cup, bounce lid design, color: black, product rendering, 8k
Modern minimalist stainless steel vacuum cup, bounce lid design, color: white, product rendering, 8k
Modern minimalist stainless steel vacuum cup, bounce lid design, color: blue, product rendering, 8k
EOF

# 批量生成
python scripts/comfyui-cup-workflow.py batch \
  --prompts configs/color_variants.txt \
  --output-dir designs/color_variants/ \
  --count 3
```

**输出**: `designs/color_variants/cup_001.png`, `cup_002.png`, `cup_003.png`。

## 文件结构#

```
comfyui-cup-workflow/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── comfyui-cup-workflow.py     # 主程序
│   ├── run_workflow.py              # 运行工作流
│   ├── batch_generate.py            # 批量生成
│   ├── download_models.py           # 下载模型
│   └── utils.py                     # 工具函数
├── workflows/                          # ComfyUI工作流文件
│   ├── cup_design_basic.json      # 基础设计工作流
│   ├── cup_design_advanced.json  # 高级设计工作流
│   ├── cup_structure.json          # 结构设计工作流
│   ├── cup_explosion.json         # 爆炸图工作流
│   └── cup_rendering.json        # 渲染图工作流
├── models/                              # AI模型文件（下载后）
│   ├── cup_structure.safetensors
│   ├── material_rendering.safetensors
│   └── product_rendering.safetensors
├── configs/                              # 配置文件
│   ├── prompts.txt                  # 提示词配置
│   ├── negative_prompts.txt        # 负面提示词配置
│   └── sampling_params.json        # 采样参数配置
├── examples/                            # 使用示例
│   ├── example_1_text2img.py
│   ├── example_2_img2img.py
│   ├── example_3_batch.py
│   └── example_4_custom_workflow.py
└── tests/                               # 测试文件
    ├── test_text2img.py
    ├── test_img2img.py
    └── test_batch.py
```

## 工作流说明#

### 1. cup_design_basic.json（基础设计工作流）
- **输入**: 文字提示词
- **输出**: 保温杯设计图
- **适用**: 快速生成概念设计
- **采样器**: DPM++ 2M Karras
- **步数**: 30
- **CFG Scale**: 7.5

### 2. cup_design_advanced.json（高级设计工作流）
- **输入**: 文字提示词 + 参考图
- **输出**: 优化后的设计图
- **适用**: 基于参考图生成变体
- **采样器**: DPM++ 2M Karras
- **步数**: 40
- **CFG Scale**: 8.0
- **Denoise**: 0.75

### 3. cup_structure.json（结构设计工作流）
- **输入**: 文字提示词（指定结构参数）
- **输出**: 保温杯结构图
- **适用**: 生成结构设计图
- **包含**: 杯体、杯盖、弹簧机构、铰链#

### 4. cup_explosion.json（爆炸图工作流）
- **输入**: 保温杯设计图
- **输出**: 爆炸图（零件分离）
- **适用**: 展示内部结构
- **包含**: 爆炸视图、零件标注#

### 5. cup_rendering.json（渲染图工作流）
- **输入**: 保温杯设计图
- **输出**: 产品级渲染图
- **适用**: 生成营销素材
- **包含**: 光照、材质、背景#

## 提示词模板#

### 基础提示词模板
```
{style} {material} vacuum cup, {lid_type} design, {capacity}ml, 
{car_compatible}, product rendering, 8k, studio lighting, 
high quality, detailed
```

### 高级提示词模板
```
{style} {material} vacuum cup, {lid_type} design, {capacity}ml,
{car_compatible}, {surface_treatment}, {color},
product rendering, 8k, studio lighting, high quality, 
detailed, {view_angle}, {background}
```

### 负面提示词模板
```
low quality, blurry, distorted, bad anatomy, deformed, 
ugly, disfigured, poorly drawn face, mutation, mutated, 
extra limbs, extra legs, extra arms, malformed limbs, 
fused fingers, too many fingers, long neck, cross-eyed, 
polar lowres, bad anatomy, bad hands, text, error, 
missing fingers, extra digit, fewer digits, cropped, 
worst quality, low quality, blur, blurriness, 
watermark, signature, logo, bad art, poorly drawn, 
low res, weird colors, distorted proportions
```

## 工作流程#

### 阶段1: 准备工作流
1. 选择工作流文件（基础/高级/结构/爆炸/渲染）
2. 准备提示词（文字描述）
3. 准备参考图（可选）

### 阶段2: 生成设计#
1. 运行工作流
2. 调整参数（步数、CFG Scale、采样器）
3. 生成设计图#

### 阶段3: 优化迭代#
1. 评估生成结果
2. 调整提示词
3. 重新生成#

### 阶段4: 输出成果#
1. 选择合适的设计#
2. 使用渲染工作流提升质量#
3. 输出最终设计图#

## 注意事项#

⚠️ **重要提示**:
1. ComfyUI必须单独安装并运行
2. 首次使用需要下载专用模型（约5GB）
3. 生成高质量图片需要强大的GPU（推荐NVIDIA RTX 3060+）
4. 所有生成的设计仅供参考，实际生产需要工程验证#
## 相关技能#

- `vacuum-cup-design-suite` - 保温杯设计专用技能包
- `cup-structure-designer` - 杯体结构设计
- `lid-mechanism-designer` - 弹跳盖机构设计
- `material-selector` - 材料选型助手#

## 支持#

如有问题，请提交Issue或联系开发团队。

## 许可证#

MIT License

## CLI Usage

```bash
# 命令行使用方法
python scripts/example.py --help

# 示例命令
python scripts/example.py --input input.jpg --output output.jpg
```
