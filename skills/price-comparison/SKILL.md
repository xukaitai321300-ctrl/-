---
name: price-comparison
description: 价格对比分析技能 - 对比不同供应商报价
tags: ["price", "comparison", "analysis", "cost"]
---

# 价格对比分析技能 (price-comparison)

本技能专门用于对比不同供应商的报价，识别价格异常，生成价格对比报告。

## 功能概述#

### 1. 价格对比#
- 对比不同供应商报价
- 分析价格趋势
- 识别价格异常#
- 生成价格对比图表#

### 2. 成本分析#
- 计算总成本（单价×数量+运费）
- 分析MOQ对单价的影响
- 推荐最优采购方案#

### 3. 报告生成#
- 生成价格对比Excel
- 生成价格趋势图#
- 生成采购建议报告#

## 使用方法#

### 基础价格对比
```bash
python scripts/compare_price.py \
  --product "stainless steel 304, 0.8mm" \
  --quantity 10000 \
  --output results/price_comparison.xlsx
```

### 高级成本分析
```bash
python scripts/analyze_cost.py \
  --product "bounce lid assembly" \
  --quantity-range 1000 5000 10000 \
  --output results/cost_analysis.xlsx
```

### 生成可视化报告
```bash
python scripts/generate_report.py \
  --input results/price_comparison.xlsx \
  --output results/price_report.html
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载价格数据库
python scripts/download_price_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/price-comparison.py --help

# 基础价格对比
python scripts/price-comparison.py compare \
  --product "stainless steel 304, coil, 0.8mm" \
  --quantity 10000 \
  --unit "kg" \
  --output results/price_comparison.xlsx

# 成本分析
python scripts/price-comparison.py analyze-cost \
  --product "bounce lid assembly, stainless steel 304" \
  --quantity-range 1000 5000 10000 \
  --output results/cost_analysis.xlsx.

# 生成可视化报告
python scripts/price-comparison.py generate-report \
  --input results/price_comparison.xlsx \
  --output results/price_report.html \
  --charts "price_trend, cost_breakdown"

# 批量对比
python scripts/price-comparison.py batch-compare \
  --products configs/products.json \
  --output-dir results/batch/
```

## 示例#

### 示例1: 对比不锈钢304价格
```bash
python scripts/price-comparison.py compare \
  --product "stainless steel 304, coil, 0.8mm" \
  --quantity 10000 \
  --unit "kg" \
  --min-rating 4.0 \
  --output results/ss304_price_comparison.xlsx
```

**输出**: `results/ss304_price_comparison.xlsx` - 价格对比Excel。

### 示例2: 分析弹跳盖成本
```bash
python scripts/price-comparison.py analyze-cost \
  --product "bounce lid assembly, stainless steel 304" \
  --quantity-range 1000 5000 10000 \
  --include-freight \
  --output results/lid_cost_analysis.xlsx
```

**输出**: `results/lid_cost_analysis.xlsx` - 成本分析Excel。

### 示例3: 生成价格趋势报告
```bash
python scripts/price-comparison.py generate-report \
  --input results/ss304_price_comparison.xlsx \
  --output results/ss304_price_report.html \
  --charts "price_trend, supplier_comparison, cost_breakdown"
```

**输出**: `results/ss304_price_report.html` - 交互式价格报告（可在浏览器中打开）。

## 文件结构#

```
price-comparison/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── price-comparison.py         # 主程序
│   ├── compare_price.py            # 价格对比
│   ├── analyze_cost.py              # 成本分析
│   ├── generate_report.py           # 报告生成
│   └── download_price_db.py       # 下载价格数据库
├── data/                                 # 数据文件
│   ├── price_db.json                # 价格数据库
│   ├── supplier_db.json             # 供应商数据库
│   └── freight_db.json              # 运费数据库
├── configs/                              # 配置文件
│   ├── products.json                 # 产品配置
│   └── analysis_params.json          # 分析参数配置
├── results/                              # 分析结果
│   ├── price_comparison.xlsx        # 价格对比结果
│   ├── cost_analysis.xlsx            # 成本分析结果
│   └── price_report.html            # 可视化报告
├── examples/                            # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_advanced.py
│   └── example_3_batch.py
└── tests/                               # 测试文件
    ├── test_compare.py
    └── test_analysis.py
```

## 价格数据库#

### 数据来源#
- 供应商报价#
- 行业公开数据#
- 用户提交数据#
- 网络爬取数据（合法来源）

### 数据字段#
- **产品**: 产品名称#
- **规格**: 产品规格#
- **供应商**: 供应商名称#
- **报价**: 单价#
- **MOQ**: 最小起订量#
- **交货期**: 交货时间#
- **评分**: 用户评分（1-5）#
- **更新时间**: 数据更新时间#

## 工作流程#

### 阶段1: 数据收集#
1. 从价格数据库中获取报价#
2. 从供应商数据库中获取供应商信息#
3. 从运费数据库中获取运费信息#

### 阶段2: 价格对比#
1. 对比不同供应商报价#
2. 计算总成本（单价×数量+运费）#
3. 识别价格异常（过高/过低）#

### 阶段3: 成本分析#
1. 分析MOQ对单价的影响#
2. 计算不同采购量的成本#
3. 推荐最优采购方案#

### 阶段4: 报告生成#
1. 生成价格对比Excel#
2. 生成价格趋势图#
3. 生成采购建议报告#

## 注意事项#

⚠️ **重要提示**:
1. 价格数据会随市场波动，仅供参考#
2. 总成本计算需要包含运费#
3. 推荐采购方案需要综合考虑价格、MOQ、交货期、评分#
4. 价格异常需要人工核实#

## 相关技能#

- `yongkang-supply-chain` - 永康供应链技能包#
- `local-supplier-lookup` - 本地供应商查询（子技能）#
- `moq-checker` - MOQ查询工具（子技能）#

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
