---
name: vacuum-cup-design-suite
description: 保温杯设计专用技能包 - 以ComfyUI图文生图/文生图/产品图片生成为核心
tags: ["design", "cup", "vacuum", "comfyui", "ai-generation", "product-design"]
---

# 保温杯设计专用技能包

本技能包以 **ComfyUI 图文生图/文生图/产品图片生成** 为核心，提供保温杯从概念到成品的全流程AI辅助设计。

## 核心功能

### 1. ComfyUI 产品图片生成（核心）
- **文生图**: 根据文字描述生成保温杯设计图
- **图生图**: 根据参考图生成变体设计
- **图文混合**: 结合文字描述和参考图生成设计

### 2. 设计工作流
- 杯体结构设计
- 弹跳盖机构设计
- 材料选型助手
- 成本控制分析

## 使用方法

### 基础文生图
```bash
# 生成保温杯设计图
python scripts/generate_cup_design.py \
  --prompt "现代简约不锈钢保温杯，弹跳盖设计，车载适用" \
  --output design_v1.png \
  --style "product rendering, 8k, photorealistic"
```

### 高级图生图
```bash
# 根据参考图生成变体
python scripts/generate_cup_variant.py \
  --reference design_v1.png \
  --variation "change color to black, add logo" \
  --output design_v2.png
```

### ComfyUI 工作流调用
```bash
# 使用专属ComfyUI工作流
python scripts/run_comfyui_workflow.py \
  --workflow comfyui_cup_design.json \
  --params '{"cup_type": "vacuum", "lid_type": "bounce", "material": "stainless_steel"}'
```

## 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装ComfyUI（如果尚未安装）
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt

# 下载保温杯专属模型
python scripts/download_models.py
```

## CLI 用法

```bash
# 查看帮助
python scripts/vacuum_cup_design.py --help

# 生成基础设计
python scripts/vacuum_cup_design.py generate \
  --prompt "弹跳盖保温杯，车载适用" \
  --material "不锈钢" \
  --capacity "500ml"

# 批量生成设计方案
python scripts/vacuum_cup_design.py batch-generate \
  --prompts prompts.txt \
  --output-dir designs/

# 优化现有设计
python scripts/vacuum_cup_design.py optimize \
  --input design.png \
  --target "lighter, more ergonomic" \
  --output optimized_design.png
```

## 示例

### 示例 1: 文生图 - 基础保温杯
```bash
python scripts/vacuum_cup_design.py generate \
  --prompt "现代简约不锈钢保温杯，弹跳盖设计，车载适用，黑色" \
  --style "product rendering, studio lighting, 8k"
```

**输出**: `designs/cup_design_20260605_001.png`

### 示例 2: 图生图 - 变体设计
```bash
python scripts/vacuum_cup_design.py vary \
  --input designs/cup_design_20260605_001.png \
  --changes "change color to white, add bamboo pattern" \
  --count 4
```

**输出**: 4个变体设计图

### 示例 3: ComfyUI 工作流
```bash
python scripts/run_comfyui_workflow.py \
  --workflow workflows/cup_design_basic.json \
  --params '{"cup": {"material": "stainless_steel", "capacity": 500, "lid_type": "bounce"}, "render": {"style": "product", "resolution": "8k"}}'
```

## 文件结构

```
vacuum-cup-design-suite/
├── SKILL.md              # 本文件
├── README.md             # 详细说明文档
├── requirements.txt      # Python依赖
├── scripts/             # 可执行脚本
│   ├── vacuum_cup_design.py      # 主程序
│   ├── generate_cup_design.py   # 文生图
│   ├── generate_cup_variant.py  # 图生图
│   ├── run_comfyui_workflow.py  # ComfyUI工作流
│   └── download_models.py       # 下载模型
├── workflows/           # ComfyUI工作流文件
│   ├── cup_design_basic.json     # 基础设计工作流
│   ├── cup_design_advanced.json # 高级设计工作流
│   └── cup_variant.json         # 变体生成工作流
├── models/              # AI模型文件
│   ├── cup_structure.safetensors
│   └── cup_rendering.safetensors
├── examples/            # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_variant.py
│   └── example_3_workflow.py
└── tests/              # 测试文件
    ├── test_design.py
    └── test_workflow.py
```

## 工作流程

### 阶段1: 概念设计（文生图）
1. 输入文字描述: "现代简约不锈钢保温杯，弹跳盖设计"
2. AI生成多张概念图
3. 选择满意的设计方向

### 阶段2: 细化设计（图生图）
1. 选择概念图作为参考
2. 输入修改要求: "改变颜色为黑色，添加logo"
3. AI生成变体设计

### 阶段3: 结构设计（ComfyUI工作流）
1. 使用 `cup_design_basic.json` 工作流
2. 设置参数: 材料、容量、盖子类型
3. 生成结构设计图

### 阶段4: 渲染输出
1. 使用 `cup_design_advanced.json` 工作流
2. 设置渲染参数: 分辨率、光照、材质
3. 输出产品级渲染图

## 注意事项

⚠️ **重要提示**:
1. ComfyUI必须单独安装并运行
2. 首次使用需要下载AI模型（约5GB）
3. 生成高质量图片需要强大的GPU（推荐NVIDIA RTX 3060+）
4. 所有生成的设计仅供参考，实际生产需要工程验证

## 相关技能

- `cup-structure-designer` - 杯体结构设计
- `lid-mechanism-designer` - 弹跳盖机构设计
- `material-selector` - 材料选型助手
- `comfyui-cup-workflow` - 保温杯专属ComfyUI工作流

## 支持

如有问题，请提交Issue或联系开发团队。

## 许可证

MIT License

## CLI Usage

```bash
# 命令行使用方法
python scripts/example.py --help

# 示例命令
python scripts/example.py --input input.jpg --output output.jpg
```
