---
name: lightweight-material-advisor
description: 材料轻量化技能包 - 镁合金/碳纤维应用指南与性价比分析
tags: ["material", "lightweight", "magnesium", "carbon-fiber", "cost-performance"]
---

# 材料轻量化技能包 (lightweight-material-advisor)

本技能包提供镁合金/碳纤维应用指南与性价比分析，用于保温杯轻量化设计。

## 核心功能#

### 1. 镁合金应用指南#
- 镁合金AE44/AZ91性能参数#
- 镁合金成型工艺（压铸/挤压）#
- 镁合金表面处理（微弧氧化/喷涂）#
- 镁合金成本分析#

### 2. 碳纤维应用指南#
- 碳纤维T300/T700性能参数#
- 碳纤维铺层设计#
- 碳纤维成型工艺（热压/缠绕）#
- 碳纤维成本分析#

### 3. 性价比分析器#
- 计算重量减轻比例#
- 计算成本增加比例#
- 计算投资回收期#
- 生成性价比报告#

## 使用方法#

### 基础轻量化分析#
```bash
python scripts/analyze_lightweight.py \
  --base-material "stainless_steel_304" \
  --target-materials "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --quantity 10000 \
  --output results/lightweight_analysis.xlsx
```

### 镁合金应用指南#
```bash
python scripts/magnesium_guide.py \
  --application "vacuum cup body" \
  --output results/magnesium_guide.pdf
```

### 碳纤维应用指南#
```bash
python scripts/carbon_fiber_guide.py \
  --application "vacuum cup body" \
  --output results/carbon_fiber_guide.pdf
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载材料数据库
python scripts/download_material_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/lightweight-material-advisor.py --help

# 基础轻量化分析
python scripts/lightweight-material-advisor.py analyze \
  --base-material "stainless_steel_304" \
  --target-materials "magnesium_alloy_ae44" "carbon_fiber_t300" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/lightweight_analysis.xlsx

# 镁合金应用指南
python scripts/lightweight-material-advisor.py magnesium-guide \
  --application "vacuum cup body, 500ml" \
  --thickness 0.8 \
  --output results/magnesium_guide.pdf

# 碳纤维应用指南
python scripts/lightweight-material-advisor.py carbon-fiber-guide \
  --application "vacuum cup body, 500ml" \
  --thickness 0.5 \
  --output results/carbon_fiber_guide.pdf

# 性价比分析
python scripts/lightweight-material-advisor.py cost-performance \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --quantity 10000 \
  --output results/cost_performance.xlsx
```

## 示例#

### 示例1: 分析不锈钢304 → 镁合金AE44轻量化效果#
```bash
python scripts/lightweight-material-advisor.py analyze \
  --base-material "stainless_steel_304" \
  --target-materials "magnesium_alloy_ae44" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/ss304_to_mg_analysis.xlsx
```

**输出**: `results/ss304_to_mg_analysis.xlsx` - 轻量化分析报告Excel。

### 示例2: 生成镁合金应用指南#
```bash
python scripts/lightweight-material-advisor.py magnesium-guide \
  --application "vacuum cup body, 500ml" \
  --thickness 0.8 \
  --coating "micro-arc oxidation" \
  --output results/magnesium_guide.pdf
```

**输出**: `results/magnesium_guide.pdf` - 镁合金应用指南PDF。

### 示例3: 性价比分析（镁合金AE44 vs 不锈钢304）#
```bash
python scripts/lightweight-material-advisor.py cost-performance \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --quantity 10000 \
  --annual-sales 100000 \
  --output results/cost_performance.xlsx
```

**输出**: `results/cost_performance.xlsx` - 性价比分析报告Excel。

## 文件结构#

```
lightweight-material-advisor/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── lightweight-material-advisor.py    # 主程序
│   ├── analyze_lightweight.py          # 轻量化分析
│   ├── magnesium_guide.py             # 镁合金应用指南
│   ├── carbon_fiber_guide.py         # 碳纤维应用指南
│   ├── cost_performance_analyzer.py  # 性价比分析器
│   └── download_material_db.py       # 下载材料数据库
├── data/                                 # 数据文件
│   ├── material_db.json              # 材料数据库
│   ├── cost_db.json                 # 成本数据库
│   └── manufacturing_db.json        # 可制造性数据库
├── configs/                              # 配置文件
│   ├── magnesium_params.json         # 镁合金参数配置
│   ├── carbon_fiber_params.json     # 碳纤维参数配置
│   └── analysis_params.json         # 分析参数配置
├── results/                              # 分析结果
│   ├── lightweight_analysis.xlsx      # 轻量化分析报告
│   ├── magnesium_guide.pdf          # 镁合金应用指南
│   ├── carbon_fiber_guide.pdf      # 碳纤维应用指南
│   └── cost_performance.xlsx        # 性价比分析报告
├── examples/                            # 使用示例
│   ├── example_1_analyze.py
│   ├── example_2_guide.py
│   └── example_3_cost_performance.py
└── tests/                               # 测试文件
    ├── test_analyze.py
    ├── test_guide.py
    └── test_cost_performance.py
```

## 材料数据库#

### 镁合金AE44#
- **密度**: 1.78 g/cm³（比铝轻35%+）#
- **强度**: 280 MPa#
- **成本**: ~80 CNY/kg#
- **食品级**: ❌（需涂层）#
- **可制造性**: ⭐⭐⭐#

### 碳纤维T300#
- **密度**: 1.76 g/cm³（比钢轻70%+）#
- **强度**: 3530 MPa#
- **成本**: ~200 CNY/kg#
- **食品级**: ❌（需涂层）#
- **可制造性**: ⭐⭐#

### 不锈钢304（对比基准）#
- **密度**: 7.93 g/cm³#
- **强度**: 520 MPa#
- **成本**: ~35 CNY/kg#
- **食品级**: ✅#
- **可制造性**: ⭐⭐⭐⭐⭐#

## 工作流程#

### 阶段1: 需求分析#
1. 确定基础材料（通常为不锈钢304）#
2. 确定目标材料（镁合金/碳纤维）#
3. 确定数量要求#

### 阶段2: 轻量化分析#
1. 计算重量减轻比例#
2. 计算成本增加比例#
3. 评估强度损失#

### 阶段3: 应用指南生成#
1. 生成镁合金应用指南（工艺/表面处理/成本）#
2. 生成碳纤维应用指南（铺层设计/成型工艺/成本）#

### 阶段4: 性价比分析#
1. 计算投资回收期#
2. 分析市场竞争力提升#
3. 生成性价比报告#

## 注意事项#

⚠️ **重要提示**:
1. 镁合金/碳纤维需要涂层才能食品级适用#
2. 材料成本会随市场波动，仅供参考#
3. 轻量化材料可能需要调整制造工艺#
4. 最终选型需要工程验证#

## 相关技能#

- `vacuum-cup-design-suite` - 保温杯设计专用技能包#
- `cup-structure-designer` - 杯体结构设计#
- `material-selector` - 材料选型助手#
- `magnesium-alloy-guide` - 镁合金应用指南（子技能）#
- `carbon-fiber-guide` - 碳纤维应用指南（子技能）#
- `cost-performance-analyzer` - 性价比分析器（子技能）#

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
