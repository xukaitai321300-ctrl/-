---
name: material-selector
description: 材料选型助手 - 为保温杯设计提供材料选型建议
tags: ["material", "selection", "advisor", "cost", "performance"]
---

# 材料选型助手 (material-selector)

本技能为保温杯设计提供智能材料选型建议，综合考虑性能、成本、可制造性。

## 功能概述#

### 1. 材料数据库
- 不锈钢304/316性能参数
- 镁合金AE44/AZ91性能参数
- 碳纤维T300/T700性能参数
- 铝合金A7003性能参数

### 2. 选型建议
- 根据使用场景推荐材料
- 计算成本差异
- 评估轻量化效果
- 分析可制造性#

### 3. ComfyUI集成
- 生成材料对比图
- 生成成本分析图
- 生成轻量化效果对比图#

## 使用方法#

### 基础选型
```bash
python scripts/select_material.py \
  --application "vacuum cup body" \
  --priority "lightweight, cost-effective" \
  --output designs/material_selection.json
```

### 成本分析
```bash
python scripts/analyze_cost.py \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" \
  --quantity 10000 \
  --output designs/cost_analysis.xlsx
```

### ComfyUI生成对比图
```bash
python scripts/generate_comparison_comfyui.py \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --workflow workflows/material_comparison.json \
  --output designs/material_comparison.png
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载材料数据库
python scripts/download_material_db.py

# 安装ComfyUI（可选）
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt
```

## CLI 用法#

```bash
# 查看帮助
python scripts/material-selector.py --help

# 基础材料选型
python scripts/material-selector.py select \
  --application "vacuum cup body" \
  --priority "lightweight, cost-effective, durable" \
  --constraints "max_cost: 50 CNY/kg, max_weight: 300g"

# 成本分析
python scripts/material-selector.py analyze-cost \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" \
  --quantity 10000 \
  --output designs/cost_analysis.xlsx

# 轻量化效果评估
python scripts/material-selector.py evaluate-lightweight \
  --base-material "stainless_steel_304" \
  --target-materials "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --output designs/lightweight_evaluation.xlsx

# ComfyUI生成对比图
python scripts/material-selector.py generate-comparison \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --workflow workflows/material_comparison.json \
  --output designs/material_comparison.png
```

## 示例#

### 示例1: 保温杯杯体材料选型
```bash
python scripts/material-selector.py select \
  --application "vacuum cup body, 500ml" \
  --priority "lightweight, cost-effective, food-safe" \
  --constraints "max_cost: 60 CNY/kg, max_weight: 280g, min_strength: 200MPa" \
  --output designs/cup_body_material_selection.json
```

**输出**: `designs/cup_body_material_selection.json` - 材料选型建议JSON。

### 示例2: 成本分析（不锈钢304 vs 镁合金AE44）
```bash
python scripts/material-selector.py analyze-cost \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" \
  --quantity 10000 \
  --cup-weight 280 \
  --output designs/cost_analysis_10000units.xlsx
```

**输出**: `designs/cost_analysis_10000units.xlsx` - 成本分析Excel。

### 示例3: 使用ComfyUI生成材料对比图
```bash
python scripts/generate_comparison_comfyui.py \
  --materials "stainless_steel_304" "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --properties "density" "strength" "cost" "manufacturability" \
  --workflow workflows/material_comparison.json \
  --output designs/material_comparison.png
```

**输出**: `designs/material_comparison.png` - 材料对比图。

## 文件结构#

```
material-selector/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── material-selector.py           # 主程序
│   ├── select_material.py             # 材料选型
│   ├── analyze_cost.py                # 成本分析
│   ├── evaluate_lightweight.py        # 轻量化评估
│   ├── generate_comparison_comfyui.py  # ComfyUI生成对比图
│   └── download_material_db.py       # 下载材料数据库
├── workflows/                          # ComfyUI工作流文件
│   ├── material_comparison.json      # 材料对比图生成
│   ├── cost_analysis_chart.json      # 成本分析图表生成
│   └── lightweight_effect.json       # 轻量化效果生成
├── data/                               # 数据文件
│   ├── material_db.json              # 材料数据库
│   ├── cost_db.json                 # 成本数据库
│   └── manufacturing_db.json        # 可制造性数据库
├── examples/                           # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_cost.py
│   └── example_3_comfyui.py
└── tests/                              # 测试文件
    ├── test_selection.py
    └── test_analysis.py
```

## 材料数据库#

### 不锈钢304
- **密度**: 7.93 g/cm³
- **强度**: 520 MPa
- **成本**: ~35 CNY/kg
- **食品级**: ✅
- **可制造性**: ⭐⭐⭐⭐⭐

### 镁合金AE44
- **密度**: 1.78 g/cm³（比铝轻35%+）
- **强度**: 280 MPa
- **成本**: ~80 CNY/kg
- **食品级**: ❌（需涂层）
- **可制造性**: ⭐⭐⭐

### 碳纤维T300
- **密度**: 1.76 g/cm³（比钢轻70%+）
- **强度**: 3530 MPa
- **成本**: ~200 CNY/kg
- **食品级**: ❌（需涂层）
- **可制造性**: ⭐⭐

## 工作流程#

### 阶段1: 需求分析#
1. 确定应用场景（杯体/杯盖/配件）
2. 确定优先级（轻量化/成本/性能）
3. 确定约束条件（最大成本/最大重量/最小强度）

### 阶段2: 材料筛选#
1. 从材料数据库中筛选候选材料
2. 评估性能参数
3. 计算成本差异#

### 阶段3: 轻量化评估#
1. 计算重量减轻比例
2. 评估强度损失#
3. 评估成本增加#

### 阶段4: 生成报告#
1. 使用ComfyUI生成对比图
2. 生成成本分析Excel
3. 输出选型建议JSON#

## 注意事项#

⚠️ **重要提示**:
1. 材料成本会随市场波动，仅供参考
2. 镁合金/碳纤维需要涂层才能食品级适用
3. 轻量化材料可能需要调整制造工艺
4. 最终选型需要工程验证#

## 相关技能#

- `vacuum-cup-design-suite` - 保温杯设计专用技能包
- `cup-structure-designer` - 杯体结构设计
- `lid-mechanism-designer` - 弹跳盖机构设计
- `comfyui-cup-workflow` - 保温杯专属ComfyUI工作流
- `lightweight-material-advisor` - 材料轻量化技能包#

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
