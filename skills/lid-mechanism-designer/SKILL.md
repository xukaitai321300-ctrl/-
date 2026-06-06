---
name: lid-mechanism-designer
description: 弹跳盖机构设计技能 - 设计优化弹跳盖结构与弹簧机构
tags: ["lid", "mechanism", "spring", "bounce", "hinge", "engineering"]
---

# 弹跳盖机构设计技能 (lid-mechanism-designer)

本技能专门用于弹跳盖保温杯的盖子机构设计，包括弹簧计算、铰链设计、防误触机制。

## 功能概述

### 1. 弹跳盖结构设计
- 计算弹簧参数（劲度、预压、行程）
- 设计铰链机构
- 优化开盖手感
- 生成机构图纸

### 2. 防误触设计
- 设计锁定机构
- 计算误触力度阈值
- 优化按钮位置

### 3. ComfyUI集成
- 生成弹跳盖结构图
- 生成爆炸图
- 生成动画演示

## 使用方法

### 基础设计
```bash
python scripts/design_lid_mechanism.py \
  --spring-type "compression" \
  --force-open 15 \
  --force-close 5 \
  --output designs/lid_mechanism_15N.png
```

### 弹簧计算
```bash
python scripts/calculate_spring.py \
  --wire-diameter 2.0 \
  --coils 8 \
  --outer-diameter 10.0 \
  --material "stainless_steel_304" \
  --output designs/spring_calc.xlsx
```

### ComfyUI生成
```bash
python scripts/generate_lid_comfyui.py \
  --prompt "弹跳盖保温杯，弹簧机构，爆炸图" \
  --workflow workflows/lid_mechanism_basic.json \
  --output designs/
```

## 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装ComfyUI（可选）
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt

# 下载专用模型
python scripts/download_models.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/lid-mechanism-designer.py --help

# 设计弹跳盖机构
python scripts/lid-mechanism-designer.py design \
  --force-open 15 \
  --force-close 5 \
  --spring-type "compression" \
  --output designs/lid_mechanism.png

# 计算弹簧参数
python scripts/lid-mechanism-designer.py calculate-spring \
  --wire-diameter 2.0 \
  --coils 8 \
  --outer-diameter 10.0 \
  --material "stainless_steel_304" \
  --output designs/spring_params.json

# 生成爆炸图
python scripts/lid-mechanism-designer.py explode-view \
  --input designs/lid_mechanism.png \
  --output designs/explosion_view.png \
  --count 8

# 优化防误触
python scripts/lid-mechanism-designer.py optimize-safety \
  --input designs/lid_mechanism.png \
  --target-force 20 \
  --output designs/lid_mechanism_safe.png
```

## 示例

### 示例1: 设计15N开盖力的弹跳盖
```bash
python scripts/lid-mechanism-designer.py design \
  --force-open 15 \
  --force-close 5 \
  --spring-type "compression" \
  --lid-material "stainless_steel_304" \
  --output designs/lid_15N.png
```

**输出**: `designs/lid_15N.png` - 弹跳盖机构设计图。

### 示例2: 计算弹簧参数
```bash
python scripts/lid-mechanism-designer.py calculate-spring \
  --wire-diameter 2.0 \
  --coils 8 \
  --outer-diameter 10.0 \
  --free-length 30.0 \
  --material "stainless_steel_304" \
  --output designs/spring_2mm_8coils.json
```

**输出**: `designs/spring_2mm_8coils.json` - 弹簧参数JSON。

### 示例3: 使用ComfyUI生成爆炸图
```bash
python scripts/generate_lid_comfyui.py \
  --prompt "弹跳盖保温杯爆炸图，弹簧、铰链、按钮分离展示" \
  --workflow workflows/lid_explosion.json \
  --output designs/explosion_view.png
```

**输出**: `designs/explosion_view.png` - 弹跳盖爆炸图。

## 文件结构#

```
lid-mechanism-designer/
├── SKILL.md                            # 本文件
├── README.md                           # 详细说明文档
├── requirements.txt                    # Python依赖
├── scripts/                           # 可执行脚本
│   ├── lid-mechanism-designer.py     # 主程序
│   ├── design_lid_mechanism.py      # 机构设计
│   ├── calculate_spring.py           # 弹簧计算
│   ├── generate_lid_comfyui.py      # ComfyUI生成
│   └── download_models.py            # 下载模型
├── workflows/                         # ComfyUI工作流文件
│   ├── lid_mechanism_basic.json     # 基础机构设计
│   ├── lid_mechanism_advanced.json  # 高级机构设计
│   └── lid_explosion.json           # 爆炸图生成
├── configs/                           # 配置文件
│   ├── spring_db.json                # 弹簧参数数据库
│   └── material_db.json             # 材料数据库
├── models/                            # AI模型文件
│   ├── lid_mechanism.safetensors
│   └── spring_analysis.safetensors
├── examples/                          # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_spring.py
│   └── example_3_comfyui.py
└── tests/                            # 测试文件
    ├── test_design.py
    └── test_spring.py
```

## 设计参数#

### 开盖力选项
- **10N** - 轻柔款（女性/老人适用）
- **15N** - 标准款（通用）
- **20N** - 加固款（防误触）

### 弹簧类型选项
- `compression` - 压缩弹簧（常用）
- `extension` - 拉伸弹簧（少见）
- `torsion` - 扭转弹簧（特殊设计）

### 材料选项
- `stainless_steel_304` - 食品级不锈钢304（常用）
- `stainless_steel_316` - 医疗级不锈钢316（高端）
- `magnesium_alloy` - 镁合金（轻量化）

## 工作流程#

### 阶段1: 需求分析#
1. 确定开盖力要求
2. 选择弹簧类型
3. 确定材料要求

### 阶段2: 弹簧计算#
1. 计算弹簧参数（劲度、预压、行程）
2. 选择线径、圈数、外径
3. 验证疲劳寿命

### 阶段3: 机构设计#
1. 设计铰链机构
2. 设计按钮机构
3. 设计锁定机构（防误触）

### 阶段4: 生成图纸#
1. 使用ComfyUI生成机构图
2. 生成爆炸图
3. 输出工程图纸

## 注意事项#

⚠️ **重要提示**:
1. 生成的机构设计需要工程验证才能投产
2. ComfyUI需要单独安装并运行
3. 弹簧疲劳寿命需要实验验证
4. 防误触力度需要人体工学验证

## 相关技能#

- `vacuum-cup-design-suite` - 保温杯设计专用技能包
- `cup-structure-designer` - 杯体结构设计
- `material-selector` - 材料选型助手
- `comfyui-cup-workflow` - 保温杯专属ComfyUI工作流

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
