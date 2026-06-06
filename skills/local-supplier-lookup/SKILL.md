---
name: local-supplier-lookup
description: 本地供应商查询技能 - 查询永康本地保温杯供应商
tags: ["supplier", "lookup", "yongkang", "local", "jinhua"]
---

# 本地供应商查询技能 (local-supplier-lookup)

本技能专门用于查询浙江永康本地的保温杯供应商、制造商、配件商。

## 功能概述#

### 1. 供应商查询#
- 按产品类型查询（杯体/杯盖/配件）
- 按地理位置查询（永康/金华/浙江）
- 按评分筛选（≥4.0）
- 按MOQ筛选#

### 2. 地图可视化#
- 在地图上标注供应商位置
- 计算距离永康市中心的距离
- 规划拜访路线#

### 3. 数据管理#
- 添加新供应商
- 更新供应商信息
- 删除失效供应商#

## 使用方法#

### 基础查询
```bash
python scripts/lookup_supplier.py \
  --product "vacuum cup body" \
  --location "yongkang" \
  --radius 50 \
  --output results/suppliers.json
```

### 高级查询（带评分筛选）
```bash
python scripts/lookup_supplier.py \
  --product "bounce lid assembly" \
  --location "yongkang, jinhua" \
  --min-rating 4.0 \
  --max-moq 5000 \
  --output results/lid_suppliers.json
```

### 地图可视化
```bash
python scripts/visualize_on_map.py \
  --input results/suppliers.json \
  --output results/suppliers_map.html
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
python scripts/local-supplier-lookup.py --help

# 查询杯体供应商
python scripts/local-supplier-lookup.py lookup \
  --product "vacuum cup body, 500ml" \
  --location "yongkang" \
  --radius 50 \
  --min-rating 4.0 \
  --output results/cup_body_suppliers.json

# 查询杯盖供应商#
python scripts/local-supplier-lookup.py lookup \
  --product "bounce lid assembly" \
  --location "yongkang, jinhua" \
  --max-moq 10000 \
  --output results/lid_suppliers.json

# 地图可视化
python scripts/local-supplier-lookup.py visualize \
  --input results/cup_body_suppliers.json \
  --output results/cup_body_suppliers_map.html

# 添加新供应商
python scripts/local-supplier-lookup.py add \
  --name "永康市XX五金厂" \
  --address "浙江省永康市古山镇XX路XX号" \
  --products "vacuum cup body, stainless steel 304" \
  --moq 5000 \
  --contact "138XXXXXXX" \
  --rating 4.5
```

## 示例#

### 示例1: 查询永康本地杯体供应商
```bash
python scripts/local-supplier-lookup.py lookup \
  --product "vacuum cup body, 500ml, stainless steel 304" \
  --location "yongkang" \
  --radius 50 \
  --min-rating 4.0 \
  --max-moq 10000 \
  --output results/cup_body_suppliers.json
```

**输出**: `results/cup_body_suppliers.json` - 供应商列表JSON。

### 示例2: 查询弹跳盖供应商并生成地图#
```bash
# 1. 查询供应商
python scripts/local-supplier-lookup.py lookup \
  --product "bounce lid assembly, stainless steel" \
  --location "yongkang, jinhua" \
  --max-moq 5000 \
  --output results/lid_suppliers.json

# 2. 生成地图可视化
python scripts/local-supplier-lookup.py visualize \
  --input results/lid_suppliers.json \
  --output results/lid_suppliers_map.html
```

**输出**: 
- `results/lid_suppliers.json` - 供应商列表JSON。
- `results/lid_suppliers_map.html` - 交互式地图（可在浏览器中打开）。

### 示例3: 批量查询多个产品#
```bash
# 创建查询配置文件
cat > configs/batch_lookup.json << EOF
[
  {"product": "vacuum cup body, 500ml", "location": "yongkang", "max_moq": 10000},
  {"product": "bounce lid assembly", "location": "yongkang", "max_moq": 5000},
  {"product": "silicone seal ring", "location": "yongkang", "max_moq": 20000}
]
EOF

# 批量查询
python scripts/local-supplier-lookup.py batch-lookup \
  --config configs/batch_lookup.json \
  --output-dir results/batch/
```

**输出**: `results/batch/` 目录下的多个JSON文件。

## 文件结构#

```
local-supplier-lookup/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── local-supplier-lookup.py    # 主程序
│   ├── lookup_supplier.py          # 供应商查询
│   ├── visualize_on_map.py        # 地图可视化
│   ├── download_supplier_db.py   # 下载供应商数据库
│   └── init_db.py                   # 初始化数据库
├── data/                                 # 数据文件
│   ├── supplier_db.json              # 供应商数据库
│   ├── location_db.json             # 地理位置数据库
│   └── rating_db.json                # 评分数据库
├── configs/                              # 配置文件
│   ├── search_radius.json           # 搜索半径配置
│   └── filters.json                  # 筛选条件配置
├── results/                              # 查询结果
│   ├── suppliers.json                # 供应商查询结果
│   ├── suppliers_map.html           # 地图可视化结果
│   └── batch/                       # 批量查询结果
├── examples/                            # 使用示例
│   ├── example_1_basic.py
│   ├── example_2_advanced.py
│   └── example_3_batch.py
└── tests/                               # 测试文件
    ├── test_lookup.py
    └── test_visualize.py
```

## 供应商数据库#

### 数据来源#
- 永康本地供应商目录
- 永康政府公开数据
- 行业展会参展商名单
- 用户提交数据#

### 数据字段#
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
2. 确定地理位置要求
3. 确定MOQ要求#

### 阶段2: 供应商查询#
1. 从供应商数据库中筛选符合条件的供应商
2. 按评分排序
3. 计算距离永康市中心的距離#

### 阶段3: 结果展示#
1. 生成供应商列表JSON
2. 生成地图可视化HTML
3. 输出Excel报告（可选）#

### 阶段4: 数据更新#
1. 添加新发现的供应商
2. 更新供应商信息（价格/MOQ/评分）
3. 删除失效供应商#

## 注意事项#

⚠️ **重要提示**:
1. 供应商数据需要定期更新（建议每月更新）
2. 价格数据会随市场波动，仅供参考
3. MOQ数据需要与供应商确认后才能下单
4. 建议实地拜访供应商后再下单#

## 相关技能#

- `yongkang-supply-chain` - 永康供应链技能包
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
