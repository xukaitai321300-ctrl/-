---
name: carbon-fiber-guide
description: 碳纤维应用指南 - 碳纤维T300/T700性能参数与应用指南
tags: ["carbon", "fiber", "t300", "t700", "lightweight"]
---

# 碳纤维应用指南 (carbon-fiber-guide)

本技能提供碳纤维T300/T700的性能参数、铺层设计、成型工艺、成本分析。

## 功能概述#

### 1. 性能参数#
- 碳纤维T300性能参数#
- 碳纤维T700性能参数#
- 碳纤维 vs 镁合金 vs 不锈钢对比#
- 疲劳强度、耐腐蚀性数据#

### 2. 铺层设计#
- 铺层顺序设计#
- 纤维方向设计#
- 铺层厚度计算#
- 强度仿真#

### 3. 成型工艺#
- 热压罐工艺（Autoclave）#
- 树脂传递模塑（RTM）#
- 预浸料成型#
- 良品率分析#

### 4. 成本分析#
- 材料成本分析#
- 加工成本分析#
- 成型工艺成本分析#
- 总成本对比（vs 不锈钢304）#

## 使用方法#

### 基础查询#
```bash
python scripts/query_carbon.py \
  --fiber "T300" \
  --property "density, strength, cost" \
  --output results/t300_properties.json
```

### 铺层设计#
```bash
python scripts/laminate_design.py \
  --fiber "T300" \
  --layers 8 \
  --thickness 0.5 \
  --output results/laminate_design.json
```

### 成本分析#
```bash
python scripts/analyze_cost.py \
  --fiber "T300" \
  --quantity 10000 \
  --output results/t300_cost_analysis.xlsx
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载碳纤维数据库
python scripts/download_carbon_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/carbon-fiber-guide.py --help

# 查询碳纤维性能参数
python scripts/carbon-fiber-guide.py query \
  --fiber "T300" \
  --properties "density, tensile_strength, yield_strength, fatigue_strength" \
  --output results/t300_properties.json

# 铺层设计
python scripts/carbon-fiber-guide.py laminate-design \
  --fiber "T300" \
  --layers 8 \
  --thickness 0.5 \
  --fiber-direction "[0, 45, -45, 90, 90, -45, 45, 0]" \
  --output results/laminate_design.json

# 成本分析
python scripts/carbon-fiber-guide.py analyze-cost \
  --fiber "T300" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/t300_cost_analysis.xlsx.

# 生成应用指南PDF
python scripts/carbon-fiber-guide.py generate-guide \
  --application "vacuum cup body" \
  --output results/carbon_fiber_guide.pdf
```

## 示例#

### 示例1: 查询碳纤维T300性能参数#
```bash
python scripts/carbon-fiber-guide.py query \
  --fiber "T300" \
  --properties "density, tensile_strength, yield_strength, fatigue_strength, corrosion_resistance" \
  --output results/t300_properties.json
```

**输出**: `results/t300_properties.json` - 碳纤维T300性能参数JSON。

### 示例2: 铺层设计（8层，总厚0.5mm）#
```bash
python scripts/carbon-fiber-guide.py laminate-design \
  --fiber "T300" \
  --layers 8 \
  --thickness 0.5 \
  --fiber-direction "[0, 45, -45, 90, 90, -45, 45, 0]" \
  --output results/laminate_design.json
```

**输出**: `results/laminate_design.json` - 铺层设计方案JSON。

### 示例3: 成本分析（T300 vs 不锈钢304）#
```bash
python scripts/carbon-fiber-guide.py analyze-cost \
  --fiber "T300" \
  --base-material "stainless_steel_304" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/cost_comparison.xlsx
```

**输出**: `results/cost_comparison.xlsx` - 成本对比Excel。

## 文件结构#

```
carbon-fiber-guide/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── carbon-fiber-guide.py     # 主程序
│   ├── query_carbon.py            # 性能参数查询
│   ├── laminate_design.py        # 铺层设计
│   ├── analyze_cost.py              # 成本分析
│   ├── generate_guide.py           # 生成应用指南PDF
│   └── download_carbon_db.py       # 下载碳纤维数据库
├── data/                                 # 数据文件
│   ├── carbon_db.json               # 碳纤维数据库
│   ├── process_db.json             # 成型工艺数据库
│   └── cost_db.json                 # 成本数据库
├── configs/                              # 配置文件
│   ├── fibers.json                   # 碳纤维配置
│   └── processes.json               # 成型工艺配置
├── results/                              # 分析结果
│   ├── t300_properties.json         # T300性能参数
│   ├── t700_properties.json         # T700性能参数
│   ├── laminate_design.json         # 铺层设计方案
│   └── cost_comparison.xlsx        # 成本对比
├── examples/                            # 使用示例
│   ├── example_1_query.py
│   ├── example_2_laminate.py
│   └── example_3_cost.py
└── tests/                               # 测试文件
    ├── test_query.py
    ├── test_laminate.py
    └── test_cost.py
```

## 碳纤维性能参数#

### 碳纤维T300#
- **密度**: 1.76 g/cm³（比钢轻70%+）#
- **抗拉强度**: 3530 MPa#
- **屈服强度**: 不适用（脆性材料）#
- **疲劳强度**: 不适用（脆性材料）#
- **耐腐蚀性**: 优秀#
- **成本**: ~200 CNY/kg#
- **可制造性**: ⭐⭐#

### 碳纤维T700#
- **密度**: 1.78 g/cm³（比钢轻70%+）#
- **抗拉强度**: 4900 MPa#
- **屈服强度**: 不适用（脆性材料）#
- **疲劳强度**: 不适用（脆性材料）#
- **耐腐蚀性**: 优秀#
- **成本**: ~300 CNY/kg#
- **可制造性**: ⭐⭐#

### 不锈钢304（对比基准）#
- **密度**: 7.93 g/cm³#
- **抗拉强度**: 520 MPa#
- **屈服强度**: 215 MPa#
- **疲劳强度**: 240 MPa#
- **耐腐蚀性**: 优秀#
- **成本**: ~35 CNY/kg#
- **可制造性**: ⭐⭐⭐⭐⭐#

## 铺层设计#

### 铺层顺序示例（8层，总厚0.5mm）#
| 层号 | 纤维方向 | 厚度 (mm) | 作用 |
|------|------------|--------------|------|
| 1 | 0° | 0.0625 | 纵向强度 |
| 2 | 45° | 0.0625 | 剪切强度 |
| 3 | -45° | 0.0625 | 剪切强度 |
| 4 | 90° | 0.0625 | 横向强度 |
| 5 | 90° | 0.0625 | 横向强度 |
| 6 | -45° | 0.0625 | 剪切强度 |
| 7 | 45° | 0.0625 | 剪切强度 |
| 8 | 0° | 0.0625 | 纵向强度 |

### 铺层参数#
- **单层厚度**: 0.0625 mm（标准）#
- **纤维体积含量**: 50%-60%#
- **树脂体积含量**: 40%-50%#
- **孔隙率**: <1%#

## 成型工艺#

### 热压罐工艺（Autoclave）#
- **适用产品**: 航空级保温杯（高端）#
- **温度**: 120-180°C#
- **压力**: 2-5 bar#
- **固化时间**: 1-2 小时#
- **良品率**: 90%+#
- **成本**: 高（~50 CNY/kg）#

### 树脂传递模塑（RTM）#
- **适用产品**: 中高端保温杯#
- **温度**: 80-120°C#
- **压力**: 1-3 bar#
- **固化时间**: 0.5-1 小时#
- **良品率**: 95%+#
- **成本**: 中（~30 CNY/kg）#

### 预浸料成型#
- **适用产品**: 中高端保温杯#
- **温度**: 120-150°C#
- **压力**: 1-2 bar#
- **固化时间**: 0.5-1 小时#
- **良品率**: 92%+#
- **成本**: 中高（~40 CNY/kg）#

## 成本分析#

### 10000个保温杯杯体（500ml，壁厚0.5mm）#

| 材料 | 单价 | 单件重量 | 材料成本/件 | 加工成本/件 | 成型成本/件 | 总成本/件 |
|------|------|---------|---------------|
| 不锈钢304 | 35 CNY/kg | 280g | 9.8 CNY | 5.0 CNY | 不适用 | 14.8 CNY |
| 碳纤维T300 | 200 CNY/kg | 62g | 12.4 CNY | 20.0 CNY | 30.0 CNY | 62.4 CNY |
| **对比** | - | **-78%** | **+26%** | **+300%** | **+INF%** | **+322%** |

**结论**: 碳纤维T300虽然重量减轻78%，但成本是不锈钢304的4.2倍（+322%），不适合大众市场保温杯。

## 工作流程#

### 阶段1: 需求分析#
1. 确定应用场景（杯体/杯盖/配件）#
2. 确定性能要求（强度/重量/成本）#
3. 确定预算限制#

### 阶段2: 材料选型#
1. 从碳纤维数据库中筛选候选纤维#
2. 对比性能参数#
3. 评估可制造性#

### 阶段3: 铺层设计#
1. 设计铺层顺序#
2. 确定纤维方向#
3. 计算铺层厚度#

### 阶段4: 成型工艺设计#
1. 选择成型工艺（Autoclave/RTM/预浸料）#
2. 设计模具#
3. 确定工艺参数#

### 阶段5: 成本分析#
1. 计算材料成本#
2. 计算加工成本#
3. 计算成型成本#
4. 生成成本对比报告#

## 注意事项#

⚠️ **重要提示**:
1. 碳纤维需要涂层才能食品级适用#
2. 碳纤维是脆性材料，抗冲击性差#
3. 碳纤维加工需要特殊设备（热压罐/RTM机）#
4. 碳纤维废料不可回收#
5. 成本数据会随市场波动，仅供参考#

## 相关技能#

- `lightweight-material-advisor` - 材料轻量化技能包#
- `magnesium-alloy-guide` - 镁合金应用指南（子技能）#
- `cost-performance-analyzer` - 性价比分析器（子技能）#
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
