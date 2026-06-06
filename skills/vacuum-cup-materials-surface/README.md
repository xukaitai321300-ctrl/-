# 保温杯材料与表面处理技术数据库

[English Version](README_zh.md) | [中文版本](README_zh.md)

## 简介

本技能包提供保温杯材料和表面处理技术的全面数据支持，帮助速凡团队在产品设计中做出更明智的材料选择和表面处理决策。

## 功能特性

- **材料数据库**：包含不锈钢（304、316、316L）和纯钛（TA1、TA2、TC4）的详细技术参数
- **塑料材料数据库**：包含食品级PP、TRITAN、食品级硅胶、食品级ABS、食品级PC的详细技术参数
- **表面处理数据库**：涵盖喷漆、喷塑、热转印、激光打标、3D UV打印、电镀、UV镀等工艺
- **塑料表面处理数据库**：涵盖塑料喷漆、塑料UV镀、塑料电镀、塑料激光打标、塑料丝网印刷、塑料3D UV打印、IMD等工艺
- **LOGO工艺数据库**：包含激光打标、丝网印刷、热转印、3D UV打印、电镀、UV镀、贴金、气染印等工艺
- **注塑工艺数据库**：包含PP、TRITAN、ABS、PC、硅胶的注塑工艺参数、模具设计、质量控制等
- **组装工艺数据库**：包含超声波焊接、热板焊接、螺丝固定、卡扣装配、胶水粘合、密封圈装配、弹跳盖机构装配等
- **智能工具**：
  - 金属材料选择工具：根据需求推荐合适金属材料
  - 塑料材料选择工具：根据需求推荐合适塑料材料
  - 成本计算工具：计算材料、表面处理和LOGO工艺的总成本
  - 工艺推荐工具：根据需求推荐合适的表面处理和LOGO工艺
  - 注塑工艺工具：获取注塑工艺参数、推荐注塑机、估算注塑成本、模具设计分析、缺陷诊断
  - 组装工艺工具：选择组装工艺、估算组装成本、获取质量检验清单、分析本地供应链

## 安装使用

### 前提条件

- Python 3.8+
- 必要库：`json`, `os`（内置库，无需额外安装）

### 使用方法

#### 1. 命令行使用

```bash
# 进入技能包目录
cd E:\AI日记\Claw\skills\vacuum-cup-materials-surface

# 运行材料选择工具
python scripts/material_selector.py

# 运行成本计算工具
python scripts/cost_calculator.py

# 运行工艺推荐工具
python scripts/process_recommender.py
```

#### 2. Python脚本调用

```python
from scripts.material_selector import select_material, compare_materials
from scripts.cost_calculator import calculate_total_cost
from scripts.process_recommender import recommend_surface_treatment, recommend_logo_process

# 选择材料
requirements = {
    'weight_sensitive': True,  # 需要轻量化
    'safety_level': 'medical_grade',  # 安全级别
    'cost_sensitive': False  # 成本不敏感
}

recommended = select_material(requirements)
for mat in recommended:
    print(f"{mat['name']} (成本指数: {mat['cost_index']})")

# 计算总成本
result = calculate_total_cost(
    material_id='304_stainless_steel',
    surface_process_id='spray_painting',
    logo_process_id='laser_marking',
    quantity=1000
)

print(f"总成本: ¥{result['total_cost']:.2f}")
print(f"单杯成本: ¥{result['cost_per_cup']:.2f}")
```

## 数据结构

### 材料数据 (data/materials.json)

包含以下字段：
- 基本信息：ID、名称、类型、密度、耐腐蚀性、安全级别、成本指数
- 技术参数：抗拉强度、屈服强度、延伸率、硬度、热导率、热膨胀系数
- 应用信息：500ml重量、保温性能、加工难度、本地供应情况

### 表面处理数据 (data/surface_treatment.json)

包含以下字段：
- 工艺参数：涂层厚度、固化温度、附着力等级、耐冲击性、硬度
- 成本信息：材料成本、设备成本、人工成本、总成本指数
- 优缺点分析：优点列表、缺点列表
- 应用信息：适用场景、耐久性、环保等级

### LOGO工艺数据 (data/logo_process.json)

包含以下字段：
- 工艺参数：最小订单量、制版成本、单杯成本、生产周期
- 质量信息：环保等级、耐久性、精度
- 应用信息：适用场景、优缺点

## 数据来源

- 行业调研
- 供应商咨询
- 技术文档
- 实测数据

## 更新记录

- **2026-06-05**: 初始版本创建
- 数据来源：行业调研、供应商咨询、技术文档

## 维护者

- **维护者**：速凡团队
- **位置**：浙江永康
- **更新频率**：每季度更新

## 许可证

MIT License - 详见LICENSE文件

## 联系方式

如有任何问题或建议，请通过以下方式联系我们：

- 创建Issue
- 联系速凡团队

---

**注意**：本技能包的数据仅供参考，实际应用时请结合具体情况进行调整。
