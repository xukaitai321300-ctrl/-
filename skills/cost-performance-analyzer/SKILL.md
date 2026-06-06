---
name: cost-performance-analyzer
description: 性价比分析器 - 计算重量减轻比例、成本增加比例、投资回收期
tags: ["cost", "performance", "analysis", "roi"]
---

# 性价比分析器 (cost-performance-analyzer)

本技能用于计算材料轻量化的性价比：重量减轻比例、成本增加比例、投资回收期。

## 功能概述#

### 1. 性价比计算#
- 计算重量减轻比例#
- 计算成本增加比例#
- 计算性能提升比例#
- 计算性价比指数#

### 2. 投资回收期分析#
- 计算投资回收期（月）#
- 分析市场竞争力提升#
- 计算品牌溢价能力#

### 3. 报告生成#
- 生成性价比分析Excel#
- 生成投资回收期图表#
- 生成决策建议报告#

## 使用方法#

### 基础性价比分析#
```bash
python scripts/analyze_cost_performance.py \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --quantity 10000 \
  --output results/cost_performance.xlsx
```

### 投资回收期分析#
```bash
python scripts/analyze_roi.py \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --annual-sales 100000 \
  --price-premium 20 \
  --output results/roi_analysis.xlsx
```

### 批量分析#
```bash
python scripts/batch_analyze.py \
  --config configs/batch_analysis.json \
  --output-dir results/batch/
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
python scripts/cost-performance-analyzer.py --help

# 基础性价比分析
python scripts/cost-performance-analyzer.py analyze \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/cost_performance.xlsx

# 投资回收期分析
python scripts/cost-performance-analyzer.py analyze-roi \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --annual-sales 100000 \
  --price-premium 20 \
  --output results/roi_analysis.xlsx.

# 批量分析
python scripts/cost-performance-analyzer.py batch-analyze \
  --config configs/batch_analysis.json \
  --output-dir results/batch/

# 生成决策建议报告
python scripts/cost-performance-analyzer.py generate-report \
  --input results/cost_performance.xlsx \
  --output results/decision_report.pdf
```

## 示例#

### 示例1: 不锈钢304 → 镁合金AE44性价比分析#
```bash
python scripts/cost-performance-analyzer.py analyze \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/ss304_to_mg_analysis.xlsx
```

**输出**: `results/ss304_to_mg_analysis.xlsx` - 性价比分析Excel。

### 示例2: 投资回收期分析#
```bash
python scripts/cost-performance-analyzer.py analyze-roi \
  --base-material "stainless_steel_304" \
  --target-material "magnesium_alloy_ae44" \
  --annual-sales 100000 \
  --price-premium 20 \
  --cup-weight 280 \
  --output results/roi_analysis.xlsx
```

**输出**: `results/roi_analysis.xlsx` - 投资回收期分析Excel。

### 示例3: 批量分析（多种材料对比）#
```bash
# 创建批量分析配置
cat > configs/batch_analysis.json << EOF
[
  {
    "base_material": "stainless_steel_304",
    "target_materials": ["magnesium_alloy_ae44", "carbon_fiber_t300"],
    "quantity": 10000,
    "cup_weight": 280
  }
]
EOF

# 批量分析
python scripts/cost-performance-analyzer.py batch-analyze \
  --config configs/batch_analysis.json \
  --output-dir results/batch/
```

**输出**: `results/batch/` 目录下的多个Excel文件。

## 文件结构#

```
cost-performance-analyzer/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── cost-performance-analyzer.py    # 主程序
│   ├── analyze_cost_performance.py    # 性价比分析
│   ├── analyze_roi.py                # 投资回收期分析
│   ├── batch_analyze.py               # 批量分析
│   ├── generate_report.py             # 生成决策建议报告
│   └── download_material_db.py       # 下载材料数据库
├── data/                                 # 数据文件
│   ├── material_db.json              # 材料数据库
│   ├── cost_db.json                 # 成本数据库
│   └── market_db.json                # 市场数据库
├── configs/                              # 配置文件
│   ├── batch_analysis.json           # 批量分析配置
│   └── roi_params.json               # 投资回收期参数配置
├── results/                              # 分析结果
│   ├── cost_performance.xlsx        # 性价比分析结果
│   ├── roi_analysis.xlsx            # 投资回收期分析结果
│   └── decision_report.pdf           # 决策建议报告
├── examples/                            # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_roi.py
│   └── example_3_batch.py
└── tests/                               # 测试文件
    ├── test_analyze.py
    └── test_roi.py
```

## 性价比计算公式#

### 1. 重量减轻比例#
```
weight_reduction_ratio = (base_weight - target_weight) / base_weight × 100%
```

### 2. 成本增加比例#
```
cost_increase_ratio = (target_cost - base_cost) / base_cost × 100%
```

### 3. 性价比指数#
```
cost_performance_index = weight_reduction_ratio / cost_increase_ratio
```

### 4. 投资回收期（月）#
```
roi_months = extra_investment / (price_premium × annual_sales / 12)
```

## 决策矩阵#

| 性价比指数 | 投资回收期 | 决策建议 |
|------------|------------|------------|
| >1.5 | <6个月 | ✅ **强烈推荐** - 立即采用 |
| 1.0-1.5 | 6-12个月 | ✅ **推荐** - 可以采用 |
| 0.5-1.0 | 12-24个月 | ⚠️ **谨慎** - 评估市场风险 |
| <0.5 | >24个月 | ❌ **不推荐** - 暂时不采用 |

## 工作流程#

### 阶段1: 需求分析#
1. 确定基础材料（通常是不锈钢304）#
2. 确定目标材料（镁合金/碳纤维）#
3. 确定数量要求#

### 阶段2: 性价比计算#
1. 计算重量减轻比例#
2. 计算成本增加比例#
3. 计算性价比指数#

### 阶段3: 投资回收期分析#
1. 计算额外投资#
2. 计算品牌溢价收入#
3. 计算投资回收期（月）#

### 阶段4: 生成报告#
1. 生成性价比分析Excel#
2. 生成投资回收期图表#
3. 生成决策建议报告#

## 注意事项#

⚠️ **重要提示**:
1. 材料成本会随市场波动，仅供参考#
2. 品牌溢价能力需要市场验证#
3. 投资回收期计算假设销售价格可以提升#
4. 最终决策需要综合考虑市场风险#

## 相关技能#

- `lightweight-material-advisor` - 材料轻量化技能包#
- `magnesium-alloy-guide` - 镁合金应用指南（子技能）#
- `carbon-fiber-guide` - 碳纤维应用指南（子技能）#
- `material-selector` - 材料选型助手#
- `vacuum-cup-design-suite` - 保温杯设计专用技能包#

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
