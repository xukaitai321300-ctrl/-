# 保温杯材料与表面处理技术数据库

## 简介

本技能包提供保温杯材料和表面处理技术的全面数据支持，帮助速凡团队在产品设计中做出更明智的材料选择和表面处理决策。

## 功能特性

- **材料数据库**：包含不锈钢（304、316）和纯钛（TA1、TA2）的详细技术参数
- **表面处理数据库**：涵盖喷漆、喷塑、热转印、激光打标、3D UV打印、电镀、UV镀等工艺
- **LOGO工艺数据库**：包含激光打标、丝网印刷、热转印、3D UV打印、电镀、UV镀、贴金、气染印等工艺
- **智能工具**：
  - 材料选择工具：根据需求推荐合适材料
  - 成本计算工具：计算材料、表面处理和LOGO工艺的总成本
  - 工艺推荐工具：根据需求推荐合适的表面处理和LOGO工艺

## 安装使用

### 前提条件

- Python 3.8+
- 必要库：`json`, `os`（内置库，无需额外安装）

### 使用方法

#### 1. 材料选择

```python
from scripts.material_selector import select_material, compare_materials

# 选择材料
requirements = {
    'weight_sensitive': True,  # 需要轻量化
    'safety_level': 'medical_grade',  # 安全级别
    'cost_sensitive': False  # 成本不敏感
}

recommended = select_material(requirements)
for mat in recommended:
    print(f"{mat['name']} (成本指数: {mat['cost_index']})")

# 对比材料
comparison = compare_materials(['304_stainless_steel', 'ta2_titanium'])
```

#### 2. 成本计算

```python
from scripts.cost_calculator import calculate_total_cost

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

#### 3. 工艺推荐

```python
from scripts.process_recommender import recommend_surface_treatment, recommend_logo_process

# 推荐表面处理工艺
req = {
    'budget_level': 'low',  # 低成本
    'batch_size': 50,  # 小批量
    'durability_requirement': 'medium'  # 中等耐久性
}

recommended = recommend_surface_treatment(req)
for p in recommended[:3]:
    print(f"{p['name']} (成本指数: {p.get('total_cost_index', 'N/A')})")

# 推荐LOGO工艺
logo_req = {
    'logo_type': 'text',  # 文字LOGO
    'budget_level': 'low',  # 低成本
    'batch_size': 100  # 小批量
}

logo_recommended = recommend_logo_process(logo_req)
for p in logo_recommended[:3]:
    print(f"{p['name']} (单杯成本: {p.get('cost_per_cup', 'N/A')})")
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
