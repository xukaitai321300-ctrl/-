---
name: dragon-expert
description: 龙专家（竞品分析专家）技能包，负责深度解构竞品生图方案。包含竞品分析、竞品工艺分析、竞品设计风格分析等功能。是十二生肖团的竞品分析者。
version: 1.2.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-06
tags: [dragon-expert, competitive-analysis, product-deconstruction, twelve-zodiac-team]
dependencies: [python>=3.8, json, argparse, pandas, matplotlib]
---

# 龙专家（竞品分析专家）技能包

## 功能概述

本技能包提供竞品分析功能，包含：

1. **竞品分析** - 竞品产品分析、竞品工艺分析、竞品设计风格分析、竞品材料分析
2. **生图方案解构** - 竞品生图提示词分析、竞品生图工作流分析、竞品生图参数分析
3. **竞品对比分析** - 与竞品的多维度对比分析、差距分析、优势分析
4. **竞品趋势分析** - 竞品技术趋势分析、竞品设计趋势分析、竞品市场趋势分析

龙专家是十二生肖团的**竞品分析者**，负责深度解构竞品生图方案。在十二生肖团工作流中，龙专家位于第2阶段（市场调研阶段），与虎专家、兔专家并行执行，接收鼠专家的需求分析结果，进行竞品分析，然后将竞品分析报告传递给蛇专家（产品设计）、马专家/羊专家（AI生图）。

## 安装 (Installation)

1. 确保已安装 Python 3.8+。
2. 安装依赖库：
   ```bash
   pip install pandas matplotlib seaborn requests beautifulsoup4
   ```
3. 本技能包无需额外配置，开箱即用。

## 使用方法 (Usage)

### 命令行使用 (Command Line Usage)

```bash
# 竞品分析（产品分析）
python scripts/competitive_analyzer.py --product "vacuum cup" --competitor "Thermos"

# 竞品生图方案解构
python scripts/image_solution_deconstructor.py --competitor "Thermos" --image "path/to/competitor_image.jpg"

# 竞品对比分析
python scripts/comparative_analysis_tool.py --our_product "path/to/our_product.json" --competitor_product "path/to/competitor_product.json"

# 竞品趋势分析
python scripts/trend_analysis_tool.py --industry "vacuum cup" --time_range "2020-2026"
```

### Python 使用 (Python Usage)

```python
from dragon_expert import CompetitiveAnalyzer, ImageSolutionDeconstructor, ComparativeAnalyzer

# 创建竞品分析器
analyzer = CompetitiveAnalyzer()

# 执行竞品分析（产品分析）
competitor_analysis = analyzer.analyzeProduct(
    product="vacuum cup",
    competitior="Thermos",
    analysis_dimensions=["design", "material", "craftsmanship", "price"]
)

# 创建生图方案解构器
deconstructor = ImageSolutionDeconstructor()

# 执行生图方案解构
image_solution = deconstructor.deconstructImageSolution(
    competitior="Thermos",
    image_path="path/to/competitor_image.jpg",
    deconstruction_dimensions=["prompt", "workflow", "parameters"]
)

# 创建竞品对比分析器
comparative_analyzer = ComparativeAnalyzer()

# 执行竞品对比分析
comparative_analysis = comparative_analyzer.compare(
    our_product_path="path/to/our_product.json",
    competitior_product_path="path/to/competitor_product.json",
    comparison_dimensions=["design", "material", "craftsmanship", "price", "quality"]
)
```

## 详细功能说明

### 1. 竞品分析 (Competitive Analysis)

#### 1.1 竞品产品分析 (Competitor Product Analysis)

**功能**：分析竞品的产品设计、功能、材料、工艺、价格等。

**输入**：
- `product`：产品类型（例如："vacuum cup"）
- `competitor`：竞品品牌（例如："Thermos"、"Zojirushi"、"Tiger"）
- `analysis_dimensions`：分析维度（例如：["design", "material", "craftsmanship", "price"]）

**输出**：
- `competitor_product_analysis_report.md`：竞品产品分析报告，包含：
  - 竞品概述
  - 产品设计分析
  - 材料分析
  - 工艺分析
  - 价格分析
  - 优势分析
  - 劣势分析

**示例**：
```bash
python scripts/competitive_analyzer.py --product "vacuum cup" --competitor "Thermos" --analysis_dimensions "design,material,craftsmanship,price"
```

**输出文件示例** (`competitor_product_analysis_report.md`)：
```markdown
# 竞品产品分析报告：Thermos 弹跳盖保温杯

## 1. 竞品概述
- 品牌：Thermos（膳魔师）
- 产品：弹跳盖保温杯
- 价格：399元
- 容量：450ml
- 重量：320g

## 2. 产品设计分析
- 设计风格：简约、高端
- 颜色：深空灰、黑色
- 造型：流线型、人体工学

## 3. 材料分析
- 杯身：不锈钢 304
- 杯盖：食品级PP
- 密封圈：硅胶

## 4. 工艺分析
- 杯身：旋薄工艺（厚度 1.2mm）
- 杯盖：压铸工艺
- 表面处理：喷砂 + 电镀

## 5. 价格分析
- 价格带：300-500元
- 性价比：中等

## 6. 优势分析
- 品牌知名度高
- 产品质量稳定
- 设计简约大方

## 7. 劣势分析
- 重量较重（320g）
- 价格较高
- 材料不够先进（不锈钢 304）
```

#### 1.2 竞品工艺分析 (Competitor Craftsmanship Analysis)

**功能**：分析竞品的生产工艺、工艺流程、工艺成本等。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `craftsmanship_types`：工艺类型（例如：["spinning", "die-casting", "micro-arc-oxidation"]）

**输出**：
- `competitor_craftsmanship_analysis_report.md`：竞品工艺分析报告，包含：
  - 工艺概述
  - 工艺流程分析
  - 工艺成本分析
  - 工艺质量分析

**示例**：
```bash
python scripts/competitive_analyzer.py --craftsmanship --competitor "Thermos" --craftsmanship_types "spinning,die-casting,micro-arc-oxidation"
```

#### 1.3 竞品设计风格分析 (Competitor Design Style Analysis)

**功能**：分析竞品的设计风格、颜色搭配、造型特征等。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `design_elements`：设计元素（例如：["color", "shape", "texture"]）

**输出**：
- `competitor_design_style_analysis_report.md`：竞品设计风格分析报告，包含：
  - 设计风格概述
  - 颜色搭配分析
  - 造型特征分析
  - 纹理分析

**示例**：
```bash
python scripts/competitive_analyzer.py --design_style --competitor "Thermos" --design_elements "color,shape,texture"
```

#### 1.4 竞品材料分析 (Competitor Material Analysis)

**功能**：分析竞品的材料选择、材料性能、材料成本等。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `material_types`：材料类型（例如：["stainless_steel", "PP", "silicone"]）

**输出**：
- `competitor_material_analysis_report.md`：竞品材料分析报告，包含：
  - 材料概述
  - 材料性能分析
  - 材料成本分析
  - 材料趋势分析

**示例**：
```bash
python scripts/competitive_analyzer.py --material --competitor "Thermos" --material_types "stainless_steel,PP,silicone"
```

### 2. 生图方案解构 (Image Solution Deconstruction)

#### 2.1 竞品生图提示词分析 (Competitor Image Generation Prompt Analysis)

**功能**：分析竞品的生图提示词，找出其生图策略。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `image_path`：竞品图片路径

**输出**：
- `competitor_prompt_analysis_report.md`：竞品提示词分析报告，包含：
  - 提示词概述
  - 关键词分析
  - 权重分析
  - 风格分析

**示例**：
```bash
python scripts/image_solution_deconstructor.py --prompt --competitor "Thermos" --image "path/to/competitor_image.jpg"
```

#### 2.2 竞品生图工作流分析 (Competitor Image Generation Workflow Analysis)

**功能**：分析竞品的生图工作流，找出其生图流程。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `workflow_type`：工作流类型（例如："ComfyUI"、"Stable Diffusion WebUI"）

**输出**：
- `competitor_workflow_analysis_report.md`：竞品工作流分析报告，包含：
  - 工作流概述
  - 节点分析
  - 参数分析
  - 优化建议

**示例**：
```bash
python scripts/image_solution_deconstructor.py --workflow --competitor "Thermos" --workflow_type "ComfyUI"
```

#### 2.3 竞品生图参数分析 (Competitor Image Generation Parameter Analysis)

**功能**：分析竞品的生图参数，找出其参数设置策略。

**输入**：
- `competitor`：竞品品牌（例如："Thermos"）
- `parameter_types`：参数类型（例如：["steps", "cfg_scale", "sampler"]）

**输出**：
- `competitor_parameter_analysis_report.md`：竞品参数分析报告，包含：
  - 参数概述
  - 参数设置分析
  - 参数优化建议

**示例**：
```bash
python scripts/image_solution_deconstructor.py --parameters --competitor "Thermos" --parameter_types "steps,cfg_scale,sampler"
```

### 3. 竞品对比分析 (Comparative Analysis)

#### 3.1 多维度对比分析 (Multi-dimensional Comparative Analysis)

**功能**：与我方产品进行多维度对比分析，找出差距和优势。

**输入**：
- `our_product_path`：我方产品数据文件路径（JSON格式）
- `competitor_product_path`：竞品产品数据文件路径（JSON格式）
- `comparison_dimensions`：对比维度（例如：["design", "material", "craftsmanship", "price", "quality"]）

**输出**：
- `comparative_analysis_report.md`：对比分析报告，包含：
  - 对比概述
  - 各维度对比结果
  - 差距分析
  - 优势分析
  - 改进建议

**示例**：
```bash
python scripts/comparative_analysis_tool.py --our_product "path/to/our_product.json" --competitor_product "path/to/competitor_product.json" --comparison_dimensions "design,material,craftsmanship,price,quality"
```

#### 3.2 差距分析 (Gap Analysis)

**功能**：分析我方产品与竞品的差距，找出改进方向。

**输入**：
- `comparative_analysis_report`：对比分析报告（文件路径）
- `gap_threshold`：差距阈值（默认：10%，即差距超过10%才认为有显著差距）

**输出**：
- `gap_analysis_report.md`：差距分析报告，包含：
  - 差距概述
  - 各维度差距分析
  - 显著差距列表
  - 改进建议

**示例**：
```bash
python scripts/comparative_analysis_tool.py --gap --comparative_analysis "comparative_analysis_report.md" --gap_threshold 10
```

#### 3.3 优势分析 (Advantage Analysis)

**功能**：分析我方产品与竞品相比的优势，找出差异化点。

**输入**：
- `comparative_analysis_report`：对比分析报告（文件路径）
- `advantage_threshold`：优势阈值（默认：10%，即优势超过10%才认为有显著优势）

**输出**：
- `advantage_analysis_report.md`：优势分析报告，包含：
  - 优势概述
  - 各维度优势分析
  - 显著优势列表
  - 差异化建议

**示例**：
```bash
python scripts/comparative_analysis_tool.py --advantage --comparative_analysis "comparative_analysis_report.md" --advantage_threshold 10
```

### 4. 竞品趋势分析 (Competitor Trend Analysis)

#### 4.1 竞品技术趋势分析 (Competitor Technology Trend Analysis)

**功能**：分析竞品的技术趋势，预测未来技术方向。

**输入**：
- `industry`：行业（例如："vacuum cup"）
- `time_range`：时间范围（例如："2020-2026"）

**输出**：
- `technology_trend_analysis_report.md`：技术趋势分析报告，包含：
  - 技术趋势概述
  - 关键技术分析
  - 技术发展方向预测
  - 技术建议

**示例**：
```bash
python scripts/trend_analysis_tool.py --technology --industry "vacuum cup" --time_range "2020-2026"
```

#### 4.2 竞品设计趋势分析 (Competitor Design Trend Analysis)

**功能**：分析竞品的设计趋势，预测未来设计方向。

**输入**：
- `industry`：行业（例如："vacuum cup"）
- `time_range`：时间范围（例如："2020-2026"）

**输出**：
- `design_trend_analysis_report.md`：设计趋势分析报告，包含：
  - 设计趋势概述
  - 关键设计元素分析
  - 设计发展方向预测
  - 设计建议

**示例**：
```bash
python scripts/trend_analysis_tool.py --design --industry "vacuum cup" --time_range "2020-2026"
```

#### 4.3 竞品市场趋势分析 (Competitor Market Trend Analysis)

**功能**：分析竞品的市场趋势，预测未来市场方向。

**输入**：
- `industry`：行业（例如："vacuum cup"）
- `time_range`：时间范围（例如："2020-2026"）

**输出**：
- `market_trend_analysis_report.md`：市场趋势分析报告，包含：
  - 市场趋势概述
  - 关键市场数据分析
  - 市场发展方向预测
  - 市场建议

**示例**：
```bash
python scripts/trend_analysis_tool.py --market --industry "vacuum cup" --time_range "2020-2026"
```

## 输出文件格式

本文档的输出文件格式已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\输出文件格式规范_20260606_v1.0.md`

## 1. 竞品概述
- 品牌：
- 产品：
- 价格：
- 容量：
- 重量：

## 2. 产品设计分析
- 设计风格：
- 颜色：
- 造型：

## 3. 材料分析
- 杯身：
- 杯盖：
- 密封圈：

## 4. 工艺分析
- 杯身：
- 杯盖：
- 表面处理：

## 5. 价格分析
- 价格带：
- 性价比：

## 6. 优势分析
- 优势1：
- 优势2：

## 7. 劣势分析
- 劣势1：
- 劣势2：
```

### 2. `comparative_analysis_report.md`（对比分析报告）

```markdown
# 对比分析报告：[我方产品] vs [竞品]

## 1. 对比概述
- 我方产品：
- 竞品：
- 对比维度：

## 2. 各维度对比结果
- 设计：我方得分 vs 竞品得分
- 材料：我方得分 vs 竞品得分
- 工艺：我方得分 vs 竞品得分
- 价格：我方得分 vs 竞品得分
- 质量：我方得分 vs 竞品得分

## 3. 差距分析
- 差距1：
- 差距2：

## 4. 优势分析
- 优势1：
- 优势2：

## 5. 改进建议
- 建议1：
- 建议2：
```

## 数据传输说明

本文档的数据传输说明已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\数据传输说明规范_20260606_v1.0.md`

## 案例分析

本文档的案例分析已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\案例分析集_20260606_v1.0.md`

## FAQ

本文档的FAQ已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\FAQ集_20260606_v1.0.md`

## 技能包质量

本技能包设计目标质量分数：**95+**（目标：100/100）

**当前质量分数**：92/100

**质量改进计划**：
1. **补充更多案例**（2026-06）：增加3个实际案例（车载保温杯、智能保温杯、儿童保温杯）
2. **优化趋势分析算法**（2026-07）：使用时间序列分析算法，提升趋势预测准确性
3. **增加竞品数据数据库**（2026-08）：建立竞品数据数据库，方便快速查询和对比

## 版本历史

本文档的版本历史已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\版本历史集_20260606_v1.0.md`

