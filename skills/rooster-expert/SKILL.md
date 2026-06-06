---
name: rooster-expert
description: 鸡专家（AI生图评审专家）技能包，负责评审生成图质量、质量守门员。包含生图质量评审、质量守门员、评审标准管理等功能。是十二生肖团的生图质量把关者。
version: 1.3.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-06
tags: [rooster-expert, ai-image-review, quality-gate-keeper, twelve-zodiac-team]
dependencies: [python>=3.8, json, argparse, PIL, matplotlib]
---

# 鸡专家（AI生图评审专家）技能包

## 功能概述

本技能包提供 AI 生图评审功能，包含：

1. **生图质量评审** - 真实感评估、材质感评估、灯光自然度评估、构图合理性评估
2. **质量守门员** - 一票否决权、质量红线管理、评审标准执行
3. **评审标准管理** - 评审标准制定、标准更新、标准执行监督
4. **反馈回路管理** - 反馈回路触发、反馈方式决定、反馈次数限制

鸡专家是十二生肖团的**生图质量把关者**，负责评审生成图质量、质量守门员。在十二生肖团工作流中，鸡专家位于第6阶段（设计评审阶段），接收马专家/羊专家的生成图，进行质量评审，然后决定是否通过，或触发反馈回路。

## 安装 (Installation)

1. 确保已安装 Python 3.8+。
2. 安装依赖库：
   ```bash
   pip install Pillow matplotlib numpy scikit-learn
   ```
3. 本技能包无需额外配置，开箱即用。

## 使用方法 (Usage)

### 命令行使用 (Command Line Usage)

```bash
# 评审生成图质量（真实感评估）
python scripts/image_review_tool.py --image "path/to/image.jpg" --evaluation_dimension "realism"

# 执行质量守门员功能（一票否决权）
python scripts/quality_gatekeeper_tool.py --image "path/to/image.jpg" --standard "high" --veto_power "enabled"

# 管理评审标准（标准更新）
python scripts/review_standard_manager_tool.py --action "update" --standard_file "path/to/standard.json"

# 管理反馈回路（反馈回路触发）
python scripts/feedback_loop_manager_tool.py --action "trigger" --feedback_reason "质量不通过" --feedback_method "return_to_stage_5"
```

### Python 使用 (Python Usage)

```python
from rooster_expert import ImageReviewer, QualityGateKeeper, ReviewStandardManager, FeedbackLoopManager

# 创建生图评审器
reviewer = ImageReviewer()

# 评审生成图质量（真实感评估）
review_result = reviewer.reviewImageQuality(
    image_path="path/to/image.jpg",
    evaluation_criteria=["realism", "material_feel", "lighting_naturalness", "composition_reasonableness"]
)

# 创建质量守门员
gatekeeper = QualityGateKeeper()

# 执行质量守门员功能（一票否决权）
gatekeeping_result = gatekeeper.executeGatekeeping(
    review_result=review_result,
    standard="high",
    veto_power="enabled"
)

# 创建评审标准管理器
standard_manager = ReviewStandardManager()

# 管理评审标准（标准更新）
standard_management_result = standard_manager.manageStandard(
    action="update",
    standard_file="path/to/standard.json"
)

# 创建反馈回路管理器
feedback_manager = FeedbackLoopManager()

# 管理反馈回路（反馈回路触发）
feedback_management_result = feedback_manager.manageFeedbackLoop(
    action="trigger",
    feedback_reason="质量不通过",
    feedback_method="return_to_stage_5"
)
```

## 详细功能说明

### 1. 生图质量评审 (Image Quality Review)

#### 1.1 真实感评估 (Realism Evaluation)

**功能**：评估生成图的真实感，判断是否符合真实产品照片的标准。

**输入**：
- `image_path`：生成图文件路径（PNG/JPG格式）
- `realism_criteria`：真实感评估标准（例如：["texture_realism", "reflection_realism", "shadow_realism"]）

**输出**：
- `realism_evaluation_report.md`：真实感评估报告，包含：
  - 真实感评分（0-100分）
  - 真实感维度分析
  - 真实感问题描述
  - 真实感改进建议

**示例**：
```bash
python scripts/image_review_tool.py --image "path/to/image.jpg" --evaluation_dimension "realism" --realism_criteria "texture_realism,reflection_realism,shadow_realism"
```

**输出文件示例** (`realism_evaluation_report.md`)：
```markdown
# 真实感评估报告：[项目名称]

## 1. 评估概述
- 项目名称：
- 评估时间：
- 评估维度：真实感

## 2. 真实感评分
- 真实感评分：85/100
- 评级：良好（80-89分）

## 3. 真实感维度分析
- 纹理真实感：90/100（纹理清晰、细腻）
- 反射真实感：80/100（反射较自然，但略有瑕疵）
- 阴影真实感：85/100（阴影较自然，但略有瑕疵）

## 4. 真实感问题描述
- 问题1：反射略有瑕疵（杯身反射不够自然）
- 问题2：阴影略有瑕疵（杯身阴影不够自然）

## 5. 真实感改进建议
- 建议1：优化反射（调整反射参数，使反射更自然）
- 建议2：优化阴影（调整阴影参数，使阴影更自然）
```

#### 1.2 材质感评估 (Material Feel Evaluation)

**功能**：评估生成图的材质感，判断是否符合材料真实质感的标准。

**输入**：
- `image_path`：生成图文件路径（PNG/JPG格式）
- `material_feel_criteria`：材质感评估标准（例如：["metal_feel", "plastic_feel", "silicone_feel"]）

**输出**：
- `material_feel_evaluation_report.md`：材质感评估报告，包含：
  - 材质感评分（0-100分）
  - 材质感维度分析
  - 材质感问题描述
  - 材质感改进建议

**示例**：
```bash
python scripts/image_review_tool.py --image "path/to/image.jpg" --evaluation_dimension "material_feel" --material_feel_criteria "metal_feel,plastic_feel,silicone_feel"
```

#### 1.3 灯光自然度评估 (Lighting Naturalness Evaluation)

**功能**：评估生成图的灯光自然度，判断是否符合自然灯光的标准。

**输入**：
- `image_path`：生成图文件路径（PNG/JPG格式）
- `lighting_naturalness_criteria`：灯光自然度评估标准（例如：["lighting_direction", "lighting_intensity", "lighting_color_temperature"]）

**输出**：
- `lighting_naturalness_evaluation_report.md`：灯光自然度评估报告，包含：
  - 灯光自然度评分（0-100分）
  - 灯光自然度维度分析
  - 灯光自然度问题描述
  - 灯光自然度改进建议

**示例**：
```bash
python scripts/image_review_tool.py --image "path/to/image.jpg" --evaluation_dimension "lighting_naturalness" --lighting_naturalness_criteria "lighting_direction,lighting_intensity,lighting_color_temperature"
```

#### 1.4 构图合理性评估 (Composition Reasonableness Evaluation)

**功能**：评估生成图的构图合理性，判断是否符合产品展示构图的标准。

**输入**：
- `image_path`：生成图文件路径（PNG/JPG格式）
- `composition_reasonableness_criteria`：构图合理性评估标准（例如：["product_position", "product_size", "product_angle"]））

**输出**：
- `composition_reasonableness_evaluation_report.md`：构图合理性评估报告，包含：
  - 构图合理性评分（0-100分）
  - 构图合理性维度分析
  - 构图合理性问题描述
  - 构图合理性改进建议

**示例**：
```bash
python scripts/image_review_tool.py --image "path/to/image.jpg" --evaluation_dimension "composition_reasonableness" --composition_reasonableness_criteria "product_position,product_size,product_angle"
```

### 2. 质量守门员 (Quality Gatekeeper)

#### 2.1 一票否决权 (Veto Power)

**功能**：执行一票否决权，决定是否通过评审。

**输入**：
- `review_result`：评审结果（文件路径）
- `standard`：评审标准（例如："high"，可选："low"、"medium"、"high"）
- `veto_power`：一票否决权（例如："enabled"，可选："enabled"、"disabled"）

**输出**：
- `veto_power_report.md`：一票否决权报告，包含：
  - 否决权执行结果（通过/不通过）
  - 否决原因（如果不通过）
  - 否决建议

**示例**：
```bash
python scripts/quality_gatekeeper_tool.py --image "path/to/image.jpg" --standard "high" --veto_power "enabled"
```

**输出文件示例** (`veto_power_report.md`)：
```markdown
# 一票否决权报告：[项目名称]

## 1. 否决权概述
- 项目名称：
- 评审时间：
- 评审标准：high
- 一票否决权：enabled

## 2. 否决权执行结果
- 执行结果：❌ 不通过（需修改）

## 3. 否决原因
- 原因1：创新性得分率50.0% < 60%，存在严重短板
- 原因2：与竞品差异化不足，缺乏创新功能

## 4. 否决建议
- 建议1：增加差异化功能（如：温度显示、防滑底座等）
- 建议2：优化外观设计（如：增加卡通图案、个性化定制等）
- 建议3：考虑使用新材料（如：镁合金、碳纤维等）
```

#### 2.2 质量红线管理 (Quality Red Line Management)

**功能**：管理质量红线，确保生成图质量不低于红线标准。

**输入**：
- `review_result`：评审结果（文件路径）
- `quality_red_line`：质量红线（例如：{"functionality": 60, "aesthetics": 60, "innovation": 60, "feasibility": 60}）

**输出**：
- `quality_red_line_management_report.md`：质量红线管理报告，包含：
  - 质量红线管理结果（通过/不通过）
  - 质量红线问题（如果不通过）
  - 质量红线改进建议

**示例**：
```bash
python scripts/quality_gatekeeper_tool.py --review_result "path/to/review_result.md" --quality_red_line "functionality:60,aesthetics:60,innovation:60,feasibility:60"
```

#### 2.3 评审标准执行 (Review Standard Execution)

**功能**：执行评审标准，确保评审过程符合标准。

**输入**：
- `review_result`：评审结果（文件路径）
- `review_standard`：评审标准（文件路径）

**输出**：
- `review_standard_execution_report.md`：评审标准执行报告，包含：
  - 评审标准执行结果（通过/不通过）
  - 评审标准执行问题（如果不通过）
  - 评审标准执行改进建议

**示例**：
```bash
python scripts/quality_gatekeeper_tool.py --review_result "path/to/review_result.md" --review_standard "path/to/review_standard.md"
```

### 3. 评审标准管理 (Review Standard Management)

#### 3.1 评审标准制定 (Review Standard Formulation)

**功能**：制定评审标准，确保评审标准全面、准确。

**输入**：
- `review_type`：评审类型（例如："concept_design"，可选："concept_design"、"detailed_design"、"final_design"）
- `review_standard`：评审标准（例如："strict"，可选："lenient"、"normal"、"strict"）

**输出**：
- `review_standard.md`：评审标准文档，包含：
  - 评审维度
  - 评分标准
  - 通过条件

**示例**：
```bash
python scripts/review_standard_manager_tool.py --action "formulate" --review_type "concept_design" --review_standard "strict"
```

#### 3.2 评审标准更新 (Review Standard Update)

**功能**：更新评审标准，确保评审标准与时俱进。

**输入**：
- `standard_file`：标准文件（文件路径）
- `update_content`：更新内容（例如：{"dimension": "innovation", "score": 25}）

**输出**：
- `review_standard_update_report.md`：评审标准更新报告，包含：
  - 更新概述
  - 更新内容
  - 更新建议

**示例**：
```bash
python scripts/review_standard_manager_tool.py --action "update" --standard_file "path/to/standard.json" --update_content "dimension:innovation,score:25"
```

#### 3.3 评审标准执行监督 (Review Standard Execution Supervision)

**功能**：监督评审标准执行，确保评审过程符合标准。

**输入**：
- `review_result`：评审结果（文件路径）
- `review_standard`：评审标准（文件路径）

**输出**：
- `review_standard_execution_supervision_report.md`：评审标准执行监督报告，包含：
  - 监督概述
  - 监督结果
  - 监督建议

**示例**：
```bash
python scripts/review_standard_manager_tool.py --action "supervise" --review_result "path/to/review_result.md" --review_standard "path/to/review_standard.md"
```

### 4. 反馈回路管理 (Feedback Loop Management)

#### 4.1 反馈回路触发 (Feedback Loop Triggering)

**功能**：触发反馈回路，确保不通过的评审结果能够得到及时处理。

**输入**：
- `feedback_reason`：反馈原因（例如："质量不通过"）
- `feedback_method`：反馈方式（例如："return_to_stage_5"，可选："return_to_stage_5"、"return_to_stage_4"、"return_to_stage_3"）

**输出**：
- `feedback_loop_triggering_report.md`：反馈回路触发报告，包含：
  - 触发概述
  - 触发结果
  - 触发建议

**示例**：
```bash
python scripts/feedback_loop_manager_tool.py --action "trigger" --feedback_reason "质量不通过" --feedback_method "return_to_stage_5"
```

**输出文件示例** (`feedback_loop_triggering_report.md`)：
```markdown
# 反馈回路触发报告：[项目名称]

## 1. 触发概述
- 项目名称：
- 触发时间：
- 反馈原因：质量不通过

## 2. 触发结果
- 触发结果：✅ 成功触发反馈回路
- 反馈方式：返回第5阶段（羊专家重新生成，或猴专家重新调优）
- 反馈次数：第1次（最多3次）

## 3. 触发建议
- 建议1：羊专家根据优化后的参数重新生成（优化提示词，增加差异化元素）
- 建议2：猴专家重新调优参数（调整提示词权重、采样参数、VAE参数、ControlNet参数、LoRA权重）
- 建议3：如果3次后仍不通过，终止项目或升级处理
```

#### 4.2 反馈方式决定 (Feedback Method Decision)

**功能**：决定反馈方式，确保反馈方式合理、有效。

**输入**：
- `feedback_reason`：反馈原因（例如："质量不通过"）
- `review_result`：评审结果（文件路径）

**输出**：
- `feedback_method_decision_report.md`：反馈方式决定报告，包含：
  - 决定概述
  - 决定结果
  - 决定建议

**示例**：
```bash
python scripts/feedback_loop_manager_tool.py --action "decide" --feedback_reason "质量不通过" --review_result "path/to/review_result.md"
```

#### 4.3 反馈次数限制 (Feedback Count Limitation)

**功能**：限制反馈次数，避免无限反馈循环。

**输入**：
- `max_feedback_count`：最大反馈次数（默认：3）
- `current_feedback_count`：当前反馈次数（默认：0）

**输出**：
- `feedback_count_limitation_report.md`：反馈次数限制报告，包含：
  - 限制概述
  - 限制结果
  - 限制建议

**示例**：
```bash
python scripts/feedback_loop_manager_tool.py --action "limit" --max_feedback_count 3 --current_feedback_count 1
```

## 输出文件格式

本文档的输出文件格式已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\输出文件格式规范_20260606_v1.0.md`

## 1. 项目信息
- 项目名称：
- 评审专家：鸡专家
- 评审时间：

## 2. 评审结果
- 评审结果：通过/不通过

## 3. 评审维度评分
| 评审维度 | 得分 | 满分 | 得分率 |
|---------|------|------|---------|
| 功能性 |  | 30 |  |
| 美观性 |  | 30 |  |
| 创新性 |  | 20 |  |
| 可行性 |  | 20 |  |

## 4. 总分
- 总分：
- 等级：

## 5. 不通过原因
- 原因1：
- 原因2：

## 6. 改进建议
- 建议1：
- 建议2：

## 7. 反馈回路触发
- 触发反馈回路：是/否
- 反馈方式：
- 反馈次数：
```

### 2. `veto_power_report.md`（一票否决权报告）

```markdown
# 一票否决权报告：[项目名称]

## 1. 否决权概述
- 项目名称：
- 评审时间：
- 评审标准：
- 一票否决权：

## 2. 否决权执行结果
- 执行结果：通过/不通过

## 3. 否决原因
- 原因1：
- 原因2：

## 4. 否决建议
- 建议1：
- 建议2：
```

### 3. `feedback_loop_triggering_report.md`（反馈回路触发报告）

```markdown
# 反馈回路触发报告：[项目名称]

## 1. 触发概述
- 项目名称：
- 触发时间：
- 反馈原因：

## 2. 触发结果
- 触发结果：成功/失败
- 反馈方式：
- 反馈次数：

## 3. 触发建议
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
2. **优化评审算法**（2026-07）：使用机器学习算法，提升评审准确性
3. **增加评审维度**（2026-08）：增加更多评审维度（如：品牌一致性、市场适应性等）

## 版本历史

本文档的版本历史已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\版本历史集_20260606_v1.0.md`

