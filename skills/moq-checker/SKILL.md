---
name: moq-checker
description: MOQ查询工具 - 查询供应商最小起订量
tags: ["moq", "minimum-order", "quantity", "supplier"]
---

# MOQ查询工具 (moq-checker)

本技能专门用于查询保温杯零部件供应商的最小起订量（MOQ）。

## 功能概述#

### 1. MOQ查询#
- 查询单个产品MOQ
- 批量查询多个产品MOQ
- 对比不同供应商MOQ#

### 2. MOQ分析#
- 分析MOQ与单价关系#
- 计算最优起订量#
- 识别MOQ陷阱#

### 3. 采购建议#
- 推荐最优MOQ策略#
- 分析库存压力#
- 生成采购计划#

## 使用方法#

### 基础查询
```bash
python scripts/check_moq.py \
  --product "vacuum cup body, 500ml" \
  --output results/moq_cup_body.json
```

### 批量查询
```bash
python scripts/batch_check_moq.py \
  --products configs/products.json \
  --output-dir results/batch/
```

### 生成采购建议
```bash
python scripts/generate_procurement_plan.py \
  --moq-data results/moq_cup_body.json \
  --sales-forecast 10000 \
  --output results/procurement_plan.xlsx
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载MOQ数据库
python scripts/download_moq_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/moq-checker.py --help

# 查询单个产品MOQ
python scripts/moq-checker.py check \
  --product "vacuum cup body, 500ml, stainless steel 304" \
  --output results/moq_cup_body.json

# 批量查询
python scripts/moq-checker.py batch-check \
  --products configs/products.json \
  --output-dir results/batch/

# 分析MOQ与单价关系
python scripts/moq-checker.py analyze-relationship \
  --product "bounce lid assembly" \
  --output results/lid_moq_analysis.xlsx

# 生成采购建议
python scripts/moq-checker.py generate-procurement-plan \
  --moq-data results/moq_cup_body.json \
  --sales-forecast 10000 \
  --storage-cost 0.5 \
  --output results/procurement_plan.xlsx
```

## 示例#

### 示例1: 查询杯体MOQ
```bash
python scripts/moq-checker.py check \
  --product "vacuum cup body, 500ml, stainless steel 304" \
  --min-quantity 1000 \
  --max-quantity 50000 \
  --output results/moq_cup_body.json
```

**输出**: `results/moq_cup_body.json` - MOQ数据JSON。

### 示例2: 分析MOQ与单价关系
```bash
python scripts/moq-checker.py analyze-relationship \
  --product "bounce lid assembly, stainless steel 304" \
  --quantity-range 1000 5000 10000 50000 \
  --output results/lid_moq_analysis.xlsx
```

**输出**: `results/lid_moq_analysis.xlsx` - MOQ与单价关系Excel。

### 示例3: 生成采购计划
```bash
python scripts/moq-checker.py generate-procurement-plan \
  --moq-data results/moq_cup_body.json \
  --sales-forecast 10000 \
  --storage-cost 0.5 \
  --lead-time 30 \
  --output results/procurement_plan.xlsx
```

**输出**: `results/procurement_plan.xlsx` - 采购计划Excel。

## 文件结构#

```
moq-checker/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── moq-checker.py            # 主程序
│   ├── check_moq.py               # MOQ查询
│   ├── batch_check_moq.py         # 批量查询
│   ├── analyze_relationship.py      # MOQ与单价关系分析
│   ├── generate_procurement_plan.py  # 生成采购计划
│   └── download_moq_db.py        # 下载MOQ数据库
├── data/                                 # 数据文件
│   ├── moq_db.json                   # MOQ数据库
│   ├── price_db.json                 # 价格数据库
│   └── supplier_db.json              # 供应商数据库
├── configs/                              # 配置文件
│   ├── products.json                 # 产品配置
│   └── analysis_params.json          # 分析参数配置
├── results/                              # 查询结果
│   ├── moq_cup_body.json           # MOQ查询结果
│   ├── moq_analysis.xlsx            # MOQ分析结果
│   └── procurement_plan.xlsx        # 采购计划
├── examples/                            # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_batch.py
│   └── example_3_plan.py
└── tests/                               # 测试文件
    ├── test_check.py
    └── test_analysis.py
```

## MOQ数据库#

### 数据来源#
- 供应商公开数据#
- 行业展会资料#
- 用户提交数据#
- 网络爬取数据（合法来源）

### 数据字段#
- **产品**: 产品名称#
- **规格**: 产品规格#
- **供应商**: 供应商名称#
- **MOQ**: 最小起订量#
- **单价**: 单价（按MOQ区间）#
- **交货期**: 交货时间（天）#
- **评分**: 用户评分（1-5）#
- **更新时间**: 数据更新时间#

## 工作流程#

### 阶段1: 需求分析#
1. 确定产品类型（杯体/杯盖/配件）#
2. 确定规格要求#
3. 确定预计采购量#

### 阶段2: MOQ查询#
1. 从MOQ数据库中查询#
2. 获取多家供应商报价#
3. 获取MOQ与单价关系#

### 阶段3: MOQ分析#
1. 分析MOQ与单价关系#
2. 计算最优起订量#
3. 识别MOQ陷阱（如：MOQ 10000，但单价只比MOQ 5000低2%）#

### 阶段4: 采购建议#
1. 根据销售预测计算最优采购量#
2. 分析库存压力（仓储成本）#
3. 生成采购计划Excel#

## 注意事项#

⚠️ **重要提示**:
1. MOQ数据需要与供应商确认后才能下单#
2. 单价会随市场波动，仅供参考#
3. 仓储成本需要按实际计算#
4. 采购计划需要综合考虑现金流#

## 相关技能#

- `yongkang-supply-chain` - 永康供应链技能包#
- `local-supplier-lookup` - 本地供应商查询（子技能）#
- `price-comparison` - 价格对比分析（子技能）#

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
