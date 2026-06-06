---
name: yongkang-supply-chain
description: 永康本地供应链技能包 - 查询供应商、价格对比、MOQ查询
tags: ["yongkang", "supply-chain", "local", "jinhua", "zhejiang"]
---

# 永康供应链技能包 (yongkang-supply-chain)

本技能包专门用于查询浙江永康本地保温杯供应链，包括供应商查询、价格对比、MOQ查询。

## 核心功能#

### 1. 本地供应商查询
- 查询永康本地保温杯制造商
- 查询永康本地材料供应商
- 查询永康本地配件供应商
- 地图可视化展示#

### 2. 价格对比分析#
- 对比不同供应商报价
- 分析价格趋势
- 识别价格异常#
- 生成价格对比报告#

### 3. MOQ查询工具#
- 查询供应商最小起订量
- 分析MOQ与单价关系
- 推荐最优MOQ策略#

## 使用方法#

### 基础供应商查询
```bash
python scripts/lookup_supplier.py \
  --product "vacuum cup body" \
  --location "yongkang" \
  --output results/suppliers.json
```

### 价格对比分析
```bash
python scripts/compare_price.py \
  --product "stainless steel 304, 0.8mm" \
  --quantity 10000 \
  --output results/price_comparison.xlsx
```

### MOQ查询
```bash
python scripts/check_moq.py \
  --product "bounce lid assembly" \
  --output results/moq_report.xlsx
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载永康供应商数据库
python scripts/download_supplier_db.py

# 初始化数据库
python scripts/init_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/yongkang-supply-chain.py --help

# 查询本地供应商
python scripts/yongkang-supply-chain.py lookup \
  --product "vacuum cup body, 500ml" \
  --location "yongkang, jinhua" \
  --radius 50 \
  --output results/suppliers.json

# 价格对比
python scripts/yongkang-supply-chain.py compare-price \
  --product "stainless steel 304, 0.8mm" \
  --quantity 10000 \
  --output results/price_comparison.xlsx

# MOQ查询
python scripts/yongkang-supply-chain.py check-moq \
  --product "bounce lid assembly" \
  --output results/moq_report.xlsx

# 生成供应链报告
python scripts/yongkang-supply-chain.py generate-report \
  --products configs/products.json \
  --output results/supply_chain_report.xlsx
```

## 示例#

### 示例1: 查询永康本地保温杯体供应商
```bash
python scripts/yongkang-supply-chain.py lookup \
  --product "vacuum cup body, 500ml, stainless steel 304" \
  --location "yongkang" \
  --radius 50 \
  --min-rating 4.0 \
  --output results/cup_body_suppliers.json
```

**输出**: `results/cup_body_suppliers.json` - 供应商列表JSON。

### 示例2: 对比不锈钢304价格
```bash
python scripts/yongkang-supply-chain.py compare-price \
  --product "stainless steel 304, coil, 0.8mm" \
  --quantity 10000 \
  --unit "kg" \
  --output results/ss304_price_comparison.xlsx
```

**输出**: `results/ss304_price_comparison.xlsx` - 价格对比Excel。

### 示例3: 查询弹跳盖MOQ
```bash
python scripts/yongkang-supply-chain.py check-moq \
  --product "bounce lid assembly, stainless steel" \
  --quantity-range 1000 5000 10000 \
  --output results/lid_moq_analysis.xlsx
```

**输出**: `results/lid_moq_analysis.xlsx` - MOQ分析Excel。

## 文件结构#

```
yongkang-supply-chain/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── yongkang-supply-chain.py    # 主程序
│   ├── lookup_supplier.py          # 供应商查询
│   ├── compare_price.py             # 价格对比
│   ├── check_moq.py                # MOQ查询
│   ├── download_supplier_db.py     # 下载供应商数据库
│   └── init_db.py                   # 初始化数据库
├── data/                                 # 数据文件
│   ├── supplier_db.json              # 供应商数据库
│   ├── price_db.json                 # 价格数据库
│   └── moq_db.json                   # MOQ数据库
├── configs/                              # 配置文件
│   ├── products.json                 # 产品配置
│   └── search_radius.json           # 搜索半径配置
├── results/                              # 查询结果
│   ├── suppliers.json                # 供应商查询结果
│   ├── price_comparison.xlsx        # 价格对比结果
│   └── moq_report.xlsx              # MOQ报告
├── examples/                            # 使用示例
│   ├── example_1_lookup.py
│   ├── example_2_price.py
│   └── example_3_moq.py
└── tests/                               # 测试文件
    ├── test_lookup.py
    ├── test_price.py
    └── test_moq.py
```

## 供应商数据库#

### 数据来源
- 永康本地供应商目录
- 永康政府公开数据
- 行业展会参展商名单
- 用户提交数据#

### 数据字段
- **名称**: 供应商名称
- **地址**: 详细地址
- **坐标**: 经纬度
- **产品**: 主营产品
- **MOQ**: 最小起订量
- **价格**: 参考价格
- **评分**: 用户评分（1-5）
- **联系方式**: 电话/微信/邮箱#

## 工作流程#

### 阶段1: 需求分析#
1. 确定产品类型（杯体/杯盖/配件）
2. 确定材料要求
3. 确定数量要求#

### 阶段2: 供应商查询#
1. 根据产品类型筛选供应商
2. 根据地理位置筛选（永康本地）
3. 根据评分筛选（≥4.0）#

### 阶段3: 价格对比#
1. 获取多家报价
2. 分析价格趋势
3. 识别价格异常#

### 阶段4: MOQ分析#
1. 查询各供应商MOQ
2. 分析MOQ与单价关系
3. 推荐最优MOQ策略#

### 阶段5: 生成报告#
1. 汇总查询结果
2. 生成对比图表
3. 输出Excel报告#

## 注意事项#

⚠️ **重要提示**:
1. 供应商数据需要定期更新（建议每月更新）
2. 价格数据会随市场波动，仅供参考
3. MOQ数据需要与供应商确认后才能下单
4. 建议实地拜访供应商后再下单#

## 相关技能#

- `vacuum-cup-design-suite` - 保温杯设计专用技能包
- `lightweight-material-advisor` - 材料轻量化技能包
- `local-supplier-lookup` - 本地供应商查询（子技能）
- `price-comparison` - 价格对比分析（子技能）
- `moq-checker` - MOQ查询工具（子技能）

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
