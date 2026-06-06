---
name: horse-expert
description: 马专家（ComfyUI工作流优化专家）技能包，负责工作流设计优化、ControlNet精准控制、节点效率优化。包含工作流优化、ControlNet配置、节点效率分析等功能。是十二生肖团的工作流优化者。
version: 1.2.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-06
tags: [horse-expert, comfyui-workflow-optimization, control-net, node-efficiency, twelve-zodiac-team]
dependencies: [python>=3.8, json, argparse, matplotlib, networkx]
---

# 马专家（ComfyUI工作流优化专家）技能包

## 功能概述

本技能包提供 ComfyUI 工作流优化功能，包含：

1. **工作流优化** - 节点连接优化、工作流结构优化、执行效率优化、内存占用优化
2. **ControlNet 配置** - ControlNet 模型配置、控制强度调整、预处理方法选择、多ControlNet协同
3. **节点效率分析** - 节点执行时间分析、节点资源占用分析、瓶颈节点识别、节点优化建议
4. **工作流调试** - 工作流错误诊断、节点连接检查、参数配置检查、调试报告生成

马专家是十二生肖团的**工作流优化者**，负责工作流设计优化、ControlNet精准控制、节点效率优化。在十二生肖团工作流中，马专家位于第5阶段（AI生图阶段），接收蛇专家的设计方案，搭建渲染工作流，然后将工作流传递给羊专家进行生图。

## 安装 (Installation)

1. 确保已安装 Python 3.8+。
2. 安装依赖库：
   ```bash
   pip install matplotlib networkx numpy pandas
   ```
3. 本技能包无需额外配置，开箱即用。

## 使用方法 (Usage)

### 命令行使用 (Command Line Usage)

```bash
# 工作流优化（节点连接优化）
python scripts/workflow_optimization_tool.py --method node_connection_optimization --workflow "path/to/workflow.json"

# ControlNet 配置（模型配置）
python scripts/control_net_config_tool.py --model "control_v11p_sd15_lineart" --control_weight 1.0

# 节点效率分析（节点执行时间分析）
python scripts/node_efficiency_analysis_tool.py --workflow "path/to/workflow.json" --analysis_type "execution_time"

# 工作流调试（错误诊断）
python scripts/workflow_debugging_tool.py --workflow "path/to/workflow.json" --debug_level "detailed"
```

### Python 使用 (Python Usage)

```python
from horse_expert import WorkflowOptimizer, ControlNetConfigurator, NodeEfficiencyAnalyzer

# 创建工作流优化器
optimizer = WorkflowOptimizer()

# 执行工作流优化（节点连接优化）
optimized_workflow = optimizer.optimizeNodeConnection(
    workflow_path="path/to/workflow.json",
    optimization_goal="speed"
)

# 创建ControlNet配置器
configurator = ControlNetConfigurator()

# 执行ControlNet配置（模型配置）
control_net_config = configurator.configureModel(
    model="control_v11p_sd15_lineart",
    control_weight=1.0,
    guidance_strength=1.0
)

# 创建节点效率分析器
analyzer = NodeEfficiencyAnalyzer()

# 执行节点效率分析（节点执行时间分析）
efficiency_analysis = analyzer.analyzeExecutionTime(
    workflow_path="path/to/workflow.json",
    analysis_level="detailed"
)

# 识别瓶颈节点
bottleneck_nodes = analyzer.identifyBottleneckNodes(efficiency_analysis)
```

## 详细功能说明

### 1. 工作流优化 (Workflow Optimization)

#### 1.1 节点连接优化 (Node Connection Optimization)

**功能**：优化工作流中的节点连接，减少不必要的连接，提升执行效率。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `optimization_goal`：优化目标（例如："speed"，可选："speed"、"quality"、"memory"）

**输出**：
- `optimized_workflow.json`：优化后的工作流文件
- `node_connection_optimization_report.md`：节点连接优化报告

**示例**：
```bash
python scripts/workflow_optimization_tool.py --method node_connection_optimization --workflow "path/to/workflow.json" --optimization_goal "speed"
```

**输出文件示例** (`node_connection_optimization_report.md`)：
```markdown
# 节点连接优化报告

## 1. 优化概述
- 工作流文件：workflow.json
- 优化目标：speed
- 优化前节点数：25
- 优化后节点数：22
- 优化前连接数：40
- 优化后连接数：35

## 2. 优化操作
- 移除冗余节点：3个（节点A、节点B、节点C）
- 简化连接：5条（连接1、连接2、连接3、连接4、连接5）
- 重塑工作流结构：是

## 3. 优化效果
- 预计执行时间减少：15%
- 预计内存占用减少：10%
- 预计生成质量影响：无（或极小）

## 4. 优化后工作流
- 文件路径：optimized_workflow.json
- 节点数：22
- 连接数：35
```

#### 1.2 工作流结构优化 (Workflow Structure Optimization)

**功能**：优化工作流的整体结构，提升可读性和可维护性。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `structure_type`：结构类型（例如："linear"，可选："linear"、"tree"、"graph"）

**输出**：
- `optimized_workflow.json`：优化后的工作流文件
- `workflow_structure_optimization_report.md`：工作流结构优化报告

**示例**：
```bash
python scripts/workflow_optimization_tool.py --method workflow_structure_optimization --workflow "path/to/workflow.json" --structure_type "linear"
```

#### 1.3 执行效率优化 (Execution Efficiency Optimization)

**功能**：优化工作流的执行效率，减少执行时间。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `efficiency_metrics`：效率指标（例如：["execution_time", "memory_usage"]）

**输出**：
- `optimized_workflow.json`：优化后的工作流文件
- `execution_efficiency_optimization_report.md`：执行效率优化报告

**示例**：
```bash
python scripts/workflow_optimization_tool.py --method execution_efficiency_optimization --workflow "path/to/workflow.json" --efficiency_metrics "execution_time,memory_usage"
```

#### 1.4 内存占用优化 (Memory Usage Optimization)

**功能**：优化工作流的内存占用，减少显存占用。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `memory_optimization_level`：内存优化级别（例如："aggressive"，可选："mild"、"moderate"、"aggressive"）

**输出**：
- `optimized_workflow.json`：优化后的工作流文件
- `memory_usage_optimization_report.md`：内存占用优化报告

**示例**：
```bash
python scripts/workflow_optimization_tool.py --method memory_usage_optimization --workflow "path/to/workflow.json" --memory_optimization_level "aggressive"
```

### 2. ControlNet 配置 (ControlNet Configuration)

#### 2.1 ControlNet 模型配置 (ControlNet Model Configuration)

**功能**：配置ControlNet模型，选择合适的ControlNet模型。

**输入**：
- `model`：ControlNet模型（例如："control_v11p_sd15_lineart"）
- `control_weight`：控制权重（默认：1.0）
- `guidance_strength`：引导强度（默认：1.0）

**输出**：
- `control_net_config.json`：ControlNet配置参数

**示例**：
```bash
python scripts/control_net_config_tool.py --model "control_v11p_sd15_lineart" --control_weight 1.0 --guidance_strength 1.0
```

**输出文件示例** (`control_net_config.json`)：
```json
{
  "model": "control_v11p_sd15_lineart",
  "control_weight": 1.0,
  "guidance_strength": 1.0,
  "preprocessing_method": "lineart",
  "resolution": 512,
  "threshold_a": 1.0,
  "threshold_b": 1.0
}
```

#### 2.2 控制强度调整 (Control Weight Adjustment)

**功能**：调整ControlNet的控制强度，平衡控制精度和生成多样性。

**输入**：
- `control_weight`：控制权重（默认：1.0，范围：0.0-2.0）
- `adjustment_strategy`：调整策略（例如："dynamic"，可选："static"、"dynamic"）

**输出**：
- `control_weight_adjustment_report.md`：控制强度调整报告

**示例**：
```bash
python scripts/control_net_config_tool.py --control_weight 1.0 --adjustment_strategy "dynamic"
```

#### 2.3 预处理方法选择 (Preprocessing Method Selection)

**功能**：选择合适的预处理方法，提升ControlNet的控制效果。

**输入**：
- `model`：ControlNet模型（例如："control_v11p_sd15_lineart"）
- `preprocessing_method`：预处理方法（例如："lineart"，可选取决于模型）

**输出**：
- `preprocessing_method_selection_report.md`：预处理方法选择报告

**示例**：
```bash
python scripts/control_net_config_tool.py --model "control_v11p_sd15_lineart" --preprocessing_method "lineart"
```

#### 2.4 多ControlNet协同 (Multi-ControlNet Collaboration)

**功能**：配置多个ControlNet协同工作，实现更精准的控制。

**输入**：
- `models`：ControlNet模型列表（例如：["control_v11p_sd15_lineart", "control_v11f1e_sd15_depth"]）
- `control_weights`：控制权重列表（例如：[1.0, 0.8]）

**输出**：
- `multi_control_net_config.json`：多ControlNet配置参数

**示例**：
```bash
python scripts/control_net_config_tool.py --multi_control_net --models "control_v11p_sd15_lineart,control_v11f1e_sd15_depth" --control_weights "1.0,0.8"
```

### 3. 节点效率分析 (Node Efficiency Analysis)

#### 3.1 节点执行时间分析 (Node Execution Time Analysis)

**功能**：分析每个节点的执行时间，找出执行时间最长的节点。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `analysis_level`：分析级别（例如："detailed"，可选："simple"、"detailed"）

**输出**：
- `node_execution_time_analysis_report.md`：节点执行时间分析报告

**示例**：
```bash
python scripts/node_efficiency_analysis_tool.py --workflow "path/to/workflow.json" --analysis_type "execution_time" --analysis_level "detailed"
```

**输出文件示例** (`node_execution_time_analysis_report.md`)：
```markdown
# 节点执行时间分析报告

## 1. 分析概述
- 工作流文件：workflow.json
- 分析级别：detailed
- 总执行时间：5.2秒

## 2. 节点执行时间排序
1. 节点A（KSampler）：2.5秒（48.1%）
2. 节点B（VAEDecode）：1.2秒（23.1%）
3. 节点C（ControlNetApply）：0.8秒（15.4%）
4. 节点D（LoadCheckpoint）：0.4秒（7.7%）
5. 节点E（CLIPTextEncode）：0.3秒（5.8%）

## 3. 瓶颈节点识别
- 瓶颈节点：节点A（KSampler）
- 瓶颈原因：采样步数较多（steps=50）
- 优化建议：减少采样步数（steps=30），或使用更快的采样器（"Euler a"）

## 4. 优化效果预测
- 预计执行时间减少：20-30%
- 预计生成质量影响：极小（或可接受）
```

#### 3.2 节点资源占用分析 (Node Resource Usage Analysis)

**功能**：分析每个节点的资源占用（显存、内存、CPU），找出资源占用最高的节点。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `resource_type`：资源类型（例如："memory"，可选："memory"、"cpu"、"all"）

**输出**：
- `node_resource_usage_analysis_report.md`：节点资源占用分析报告

**示例**：
```bash
python scripts/node_efficiency_analysis_tool.py --workflow "path/to/workflow.json" --analysis_type "resource_usage" --resource_type "memory"
```

#### 3.3 瓶颈节点识别 (Bottleneck Node Identification)

**功能**：识别工作流中的瓶颈节点，给出优化建议。

**输入**：
- `node_execution_time_analysis_report`：节点执行时间分析报告（文件路径）
- `node_resource_usage_analysis_report`：节点资源占用分析报告（文件路径）

**输出**：
- `bottleneck_node_identification_report.md`：瓶颈节点识别报告

**示例**：
```bash
python scripts/node_efficiency_analysis_tool.py --identify_bottleneck --node_execution_time_analysis "node_execution_time_analysis_report.md" --node_resource_usage_analysis "node_resource_usage_analysis_report.md"
```

#### 3.4 节点优化建议 (Node Optimization Suggestions)

**功能**：根据瓶颈节点识别结果，给出节点优化建议。

**输入**：
- `bottleneck_node_identification_report`：瓶颈节点识别报告（文件路径）
- `optimization_goal`：优化目标（例如："speed"，可选："speed"、"quality"、"memory"）

**输出**：
- `node_optimization_suggestions_report.md`：节点优化建议报告

**示例**：
```bash
python scripts/node_efficiency_analysis_tool.py --optimization_suggestions --bottleneck_node_identification "bottleneck_node_identification_report.md" --optimization_goal "speed"
```

### 4. 工作流调试 (Workflow Debugging)

#### 4.1 工作流错误诊断 (Workflow Error Diagnosis)

**功能**：诊断工作流中的错误，找出错误原因。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `error_log_path`：错误日志文件路径（可选）

**输出**：
- `workflow_error_diagnosis_report.md`：工作流错误诊断报告

**示例**：
```bash
python scripts/workflow_debugging_tool.py --workflow "path/to/workflow.json" --diagnose_error --error_log "path/to/error_log.txt"
```

#### 4.2 节点连接检查 (Node Connection Check)

**功能**：检查工作流中的节点连接是否正确。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `check_level`：检查级别（例如："strict"，可选："lenient"、"normal"、"strict"）

**输出**：
- `node_connection_check_report.md`：节点连接检查报告

**示例**：
```bash
python scripts/workflow_debugging_tool.py --workflow "path/to/workflow.json" --check_node_connection --check_level "strict"
```

#### 4.3 参数配置检查 (Parameter Configuration Check)

**功能**：检查工作流中的参数配置是否正确。

**输入**：
- `workflow_path`：工作流文件路径（JSON格式）
- `check_level`：检查级别（例如："strict"，可选："lenient"、"normal"、"strict"）

**输出**：
- `parameter_configuration_check_report.md`：参数配置检查报告

**示例**：
```bash
python scripts/workflow_debugging_tool.py --workflow "path/to/workflow.json" --check_parameter_configuration --check_level "strict"
```

#### 4.4 调试报告生成 (Debug Report Generation)

**功能**：生成调试报告，汇总所有检查结果。

**输入**：
- `workflow_error_diagnosis_report`：工作流错误诊断报告（文件路径）
- `node_connection_check_report`：节点连接检查报告（文件路径）
- `parameter_configuration_check_report`：参数配置检查报告（文件路径）

**输出**：
- `workflow_debug_report.md`：工作流调试报告

**示例**：
```bash
python scripts/workflow_debugging_tool.py --generate_debug_report --workflow_error_diagnosis "workflow_error_diagnosis_report.md" --node_connection_check "node_connection_check_report.md" --parameter_configuration_check "parameter_configuration_check_report.md"
```

## 输出文件格式

本文档的输出文件格式已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\输出文件格式规范_20260606_v1.0.md`

## 1. 分析概述
- 工作流文件：
- 分析级别：
- 总执行时间：

## 2. 节点执行时间排序
1. 节点A：执行时间（百分比）
2. 节点B：执行时间（百分比）
...

## 3. 瓶颈节点识别
- 瓶颈节点：
- 瓶颈原因：
- 优化建议：

## 4. 优化效果预测
- 预计执行时间减少：
- 预计生成质量影响：
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
2. **优化工作流优化算法**（2026-07）：使用机器学习算法，提升优化效率
3. **增加ControlNet模型库**（2026-08）：增加更多ControlNet模型配置示例

## 版本历史

本文档的版本历史已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\版本历史集_20260606_v1.0.md`

