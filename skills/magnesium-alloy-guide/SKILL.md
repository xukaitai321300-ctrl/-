---
name: magnesium-alloy-guide
description: 镁合金应用指南 - 镁合金AE44/AZ91性能参数与应用指南
tags: ["magnesium", "alloy", "ae44", "az91", "lightweight"]
---

# 镁合金应用指南 (magnesium-alloy-guide)

本技能提供镁合金AE44/AZ91的性能参数、成型工艺、表面处理、成本分析。

## 功能概述#

### 1. 性能参数#
- 镁合金AE44性能参数#
- 镁合金AZ91性能参数#
- 镁合金 vs 铝合金 vs 不锈钢对比#
- 疲劳强度、耐腐蚀性数据#

### 2. 成型工艺#
- 压铸工艺参数#
- 挤压工艺参数#
- 半固态成型工艺#
- 良品率分析#

### 3. 表面处理#
- 微弧氧化（MAO）工艺#
- 喷涂工艺#
- 化学转化膜#
- 食品级认证要求#

### 4. 成本分析#
- 材料成本分析#
- 加工成本分析#
- 表面处理成本分析#
- 总成本对比（vs 不锈钢304）#

## 使用方法#

### 基础查询#
```bash
python scripts/query_magnesium.py \
  --alloy "AE44" \
  --property "density, strength, cost" \
  --output results/ae44_properties.json
```

### 工艺指南#
```bash
python scripts/process_guide.py \
  --alloy "AE44" \
  --process "die-casting" \
  --output results/ae44_die_casting.pdf
```

### 成本分析#
```bash
python scripts/analyze_cost.py \
  --alloy "AE44" \
  --quantity 10000 \
  --output results/ae44_cost_analysis.xlsx
```

## 安装#

```bash
# 安装依赖
pip install -r requirements.txt

# 下载镁合金数据库
python scripts/download_magnesium_db.py
```

## CLI 用法#

```bash
# 查看帮助
python scripts/magnesium-alloy-guide.py --help

# 查询镁合金性能参数
python scripts/magnesium-alloy-guide.py query \
  --alloy "AE44" \
  --properties "density, tensile_strength, yield_strength, fatigue_strength" \
  --output results/ae44_properties.json

# 生成成型工艺指南#
python scripts/magnesium-alloy-guide.py process-guide \
  --alloy "AE44" \
  --process "die-casting" \
  --output results/ae44_die_casting.pdf

# 成本分析#
python scripts/magnesium-alloy-guide.py analyze-cost \
  --alloy "AE44" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/ae44_cost_analysis.xlsx.

# 表面处理指南#
python scripts/magnesium-alloy-guide.py surface-treatment \
  --alloy "AE44" \
  --requirement "food-grade" \
  --output results/ae44_surface_treatment.pdf
```

## 示例#

### 示例1: 查询镁合金AE44性能参数#
```bash
python scripts/magnesium-alloy-guide.py query \
  --alloy "AE44" \
  --properties "density, tensile_strength, yield_strength, fatigue_strength, corrosion_resistance" \
  --output results/ae44_properties.json
```

**输出**: `results/ae44_properties.json` - 镁合金AE44性能参数JSON。

### 示例2: 生成压铸工艺指南#
```bash
python scripts/magnesium-alloy-guide.py process-guide \
  --alloy "AE44" \
  --process "die-casting" \
  --wall-thickness 0.8 \
  --output results/ae44_die_casting.pdf
```

**输出**: `results/ae44_die_casting.pdf` - 压铸工艺指南PDF。

### 示例3: 成本分析（AE44 vs 不锈钢304）#
```bash
python scripts/magnesium-alloy-guide.py analyze-cost \
  --alloy "AE44" \
  --base-material "stainless_steel_304" \
  --quantity 10000 \
  --cup-weight 280 \
  --output results/cost_comparison.xlsx
```

**输出**: `results/cost_comparison.xlsx` - 成本对比Excel。

## 文件结构#

```
magnesium-alloy-guide/
├── SKILL.md                              # 本文件
├── README.md                             # 详细说明文档
├── requirements.txt                      # Python依赖
├── scripts/                             # 可执行脚本
│   ├── magnesium-alloy-guide.py    # 主程序
│   ├── query_magnesium.py          # 性能参数查询
│   ├── process_guide.py            # 成型工艺指南
│   ├── surface_treatment.py        # 表面处理指南
│   ├── analyze_cost.py              # 成本分析
│   └── download_magnesium_db.py   # 下载镁合金数据库
├── data/                                 # 数据文件
│   ├── magnesium_db.json           # 镁合金数据库
│   ├── process_db.json             # 成型工艺数据库
│   └── cost_db.json                 # 成本数据库
├── configs/                              # 配置文件
│   ├── alloys.json                   # 合金配置
│   └── processes.json               # 工艺配置
├── results/                              # 分析结果
│   ├── ae44_properties.json         # AE44性能参数
│   ├── ae44_die_casting.pdf        # AE44压铸指南
│   └── cost_comparison.xlsx        # 成本对比
├── examples/                            # 使用示例
│   ├── example_1_query.py
│   ├── example_2_process.py
│   └── example_3_cost.py
└── tests/                               # 测试文件
    ├── test_query.py
    ├── test_process.py
    └── test_cost.py
```

## 镁合金性能参数#

### 镁合金AE44#
- **密度**: 1.78 g/cm³（比铝轻35%+）#
- **抗拉强度**: 280 MPa#
- **屈服强度**: 180 MPa#
- **疲劳强度**: 120 MPa#
- **耐腐蚀性**: 差（需表面处理）#
- **成本**: ~80 CNY/kg#
- **可制造性**: ⭐⭐⭐#

### 镁合金AZ91#
- **密度**: 1.81 g/cm³#
- **抗拉强度**: 230 MPa#
- **屈服强度**: 150 MPa#
- **疲劳强度**: 100 MPa#
- **耐腐蚀性**: 一般（需表面处理）#
- **成本**: ~70 CNY/kg#
- **可制造性**: ⭐⭐⭐⭐#

### 不锈钢304（对比基准）#
- **密度**: 7.93 g/cm³#
- **抗拉强度**: 520 MPa#
- **屈服强度**: 215 MPa#
- **疲劳强度**: 240 MPa#
- **耐腐蚀性**: 优秀#
- **成本**: ~35 CNY/kg#
- **可制造性**: ⭐⭐⭐⭐⭐#

## 成型工艺#

### 压铸（Die Casting）#
- **适用合金**: AE44, AZ91#
- **壁厚范围**: 0.6-3.0 mm#
- **公差**: ±0.1 mm#
- **表面粗糙度**: Ra 1.6-3.2 μm#
- **良品率**: 95%+#
- **周期时间**: 30-60 秒/件#

### 挤压（Extrusion）#
- **适用合金**: AE44#
- **壁厚范围**: 0.8-5.0 mm#
- **公差**: ±0.05 mm#
- **表面粗糙度**: Ra 0.8-1.6 μm#
- **良品率**: 98%+#
- **周期时间**: 1-3 分钟/件#

## 表面处理#

### 微弧氧化（MAO）#
- **膜厚**: 10-30 μm#
- **硬度**: 300-500 HV#
- **耐腐蚀性**: 优秀#
- **食品级**: ✅（需符合FDA标准）#
- **成本**: ~15 CNY/dm²#
- **适用**: 保温杯内壁处理#

### 喷涂#
- **膜厚**: 20-50 μm#
- **硬度**: 2H-3H#
- **耐腐蚀性**: 良好#
- **食品级**: ✅（需使用食品级涂料）#
- **成本**: ~8 CNY/dm²#
- **适用**: 保温杯外壁处理#

## 成本分析#

### 10000个保温杯杯体（500ml，壁厚0.8mm）#

| 材料 | 单价 | 单件重量 | 材料成本/件 | 加工成本/件 | 表面处理/件 | 总成本/件 |
|------|------|---------|---------------|
| 不锈钢304 | 35 CNY/kg | 280g | 9.8 CNY | 5.0 CNY | 3.0 CNY | 17.8 CNY |
| 镁合金AE44 | 80 CNY/kg | 95g | 7.6 CNY | 12.0 CNY | 8.0 CNY | 27.6 CNY |
| **对比** | - | **-66%** | **-22%** | **+140%** | **+167%** | **+55%** |

**结论**: 镁合金AE44虽然材料成本更低（重量减轻66%），但加工成本和表面处理成本大幅增加，总成本比不锈钢304高55%。

## 工作流程#

### 阶段1: 需求分析#
1. 确定应用场景（杯体/杯盖/配件）#
2. 确定性能要求（强度/重量/耐腐蚀性）#
3. 确定成本预算#

### 阶段2: 材料选型#
1. 从镁合金数据库中筛选候选合金#
2. 对比性能参数#
3. 评估可制造性#

### 阶段3: 工艺设计#
1. 选择成型工艺（压铸/挤压）#
2. 设计模具#
3. 确定工艺参数#

### 阶段4: 表面处理#
1. 选择表面处理方式（MAO/喷涂）#
2. 确保食品级认证#
3. 计算表面处理成本#

### 阶段5: 成本分析#
1. 计算材料成本#
2. 计算加工成本#
3. 计算表面处理成本#
4. 生成成本对比报告#

## 注意事项#

⚠️ **重要提示**:
1. 镁合金需要涂层才能食品级适用#
2. 镁合金耐腐蚀性差，必须做表面处理#
3. 镁合金加工需要特殊设备（压铸机/挤压机）#
4. 镁合金废料可回收，回收率>95%#
5. 成本数据会随市场波动，仅供参考#

## 相关技能#

- `lightweight-material-advisor` - 材料轻量化技能包#
- `carbon-fiber-guide` - 碳纤维应用指南（子技能）#
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
