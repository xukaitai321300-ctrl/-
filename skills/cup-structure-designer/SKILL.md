---
name: cup-structure-designer
description: 杯体结构设计技能 - 生成保温杯杯体结构设计方案
tags: ["design", "cup", "structure", "engineering", "cad"]
---

# 杯体结构设计技能 (cup-structure-designer)

本技能专门用于保温杯杯体结构设计，生成可制造的结构方案。

## 功能概述

### 1. 杯体结构设计
- 生成杯体3D结构图
- 计算壁厚与强度
- 优化真空层设计
- 生成工程图纸

### 2. 材料选型建议
- 不锈钢304/316选型
- 镁合金/碳纤维应用建议
- 材料成本估算

### 3. ComfyUI集成
- 调用ComfyUI生成设计图
- 支持文生图、图生图
- 批量生成设计方案

## 使用方法

### 基础设计
```bash
python scripts/design_cup_structure.py \
  --capacity 500 \
  --material "stainless_steel" \
  --wall-thickness 0.8 \
  --output design_500ml.png
```

### 高级设计（ComfyUI）
```bash
python scripts/design_cup_structure_comfyui.py \
  --prompt "500ml vacuum cup, double wall, stainless steel 304" \
  --workflow workflows/cup_structure_basic.json \
  --output designs/
```

### 批量设计
```bash
python scripts/batch_design.py \
  --config configs/batch_design.json \
  --output-dir designs/batch/
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

## CLI 用法

```bash
# 查看帮助
python scripts/cup-structure-designer.py --help

# 生成基础杯体结构
python scripts/cup-structure-designer.py generate \
  --capacity 500 \
  --material "stainless_steel_304" \
  --wall-thickness 0.8 \
  --vacuum-layer 0.2

# 优化现有设计
python scripts/cup-structure-designer.py optimize \
  --input design_500ml.png \
  --target "lighter, stronger" \
  --output optimized_design.png

# 批量生成设计方案
python scripts/cup-structure-designer.py batch-generate \
  --capacities 350 500 750 \
  --materials "stainless_steel_304" "magnesium_alloy" \
  --output-dir designs/batch/
```

## 示例

### 示例1: 生成500ml不锈钢保温杯结构
```bash
python scripts/cup-structure-designer.py generate \
  --capacity 500 \
  --material "stainless_steel_304" \
  --wall-thickness 0.8 \
  --vacuum-layer 0.2 \
  --output designs/cup_500ml_stainless.png
```

**输出**: `designs/cup_500ml_stainless.png` - 500ml不锈钢保温杯结构图

### 示例2: 使用ComfyUI生成设计变体
```bash
python scripts/design_cup_variant_comfyui.py \
  --reference designs/cup_500ml_stainless.png \
  --variation "change material to magnesium alloy" \
  --count 4 \
  --output designs/variants/
```

**输出**: 4个材料变体设计图

### 示例3: 批量生成不同容量的设计
```bash
python scripts/batch_design.py \
  --config configs/batch_500ml_1000ml.json \
  --output-dir designs/batch/ \
  --workflow workflows/cup_structure_basic.json
```

**输出**: 批量设计图（500ml, 750ml, 1000ml）

## 文件结构

```
cup-structure-designer/
├── SKILL.md                       # 本文件
├── README.md                      # 详细说明文档
├── requirements.txt               # Python依赖
├── scripts/                      # 可执行脚本
│   ├── cup-structure-designer.py    # 主程序
│   ├── design_cup_structure.py     # 结构设计
│   ├── design_cup_variant_comfyui.py  # ComfyUI变体生成
│   ├── batch_design.py             # 批量设计
│   └── download_models.py          # 下载模型
├── workflows/                    # ComfyUI工作流文件
│   ├── cup_structure_basic.json     # 基础结构设计
│   ├── cup_structure_advanced.json # 高级结构设计
│   └── cup_variant.json           # 变体生成
├── configs/                      # 配置文件
│   ├── batch_500ml_1000ml.json   # 批量设计配置
│   └── material_db.json           # 材料数据库
├── models/                       # AI模型文件
│   ├── cup_structure.safetensors
│   └── cup_rendering.safetensors
├── examples/                     # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_comfyui.py
│   └── example_3_batch.py
└── tests/                       # 测试文件
    ├── test_design.py
    └── test_workflow.py
```

## 设计参数

### 容量选项
- 350ml - 便携款
- 500ml - 标准款
- 750ml - 大容量款
- 1000ml - 超大容量款

### 材料选项
- `stainless_steel_304` - 食品级不锈钢304
- `stainless_steel_316` - 医疗级不锈钢316
- `magnesium_alloy_ae44` - 镁合金AE44（轻量化）
- `carbon_fiber_t300` - 碳纤维T300（高端）

### 壁厚选项
- 0.6mm - 超薄（轻量化）
- 0.8mm - 标准（平衡）
- 1.0mm - 加厚（耐用）

## 工作流程

### 阶段1: 需求分析
1. 确定容量需求
2. 选择材料类型
3. 确定壁厚要求

### 阶段2: 结构设计
1. 使用ComfyUI生成基础结构
2. 计算强度与真空层
3. 生成工程图纸

### 阶段3: 优化迭代
1. 评估设计方案
2. 优化材料使用
3. 生成最终设计

## 注意事项

⚠️ **重要提示**:
1. 生成的设计需要工程验证才能投产
2. ComfyUI需要单独安装并运行
3. 材料成本会随市场波动，仅供参考

## 相关技能

- `vacuum-cup-design-suite` - 保温杯设计专用技能包
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
