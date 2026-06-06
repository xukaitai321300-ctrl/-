# 保温杯设计专用技能包使用指南

## 功能描述

本技能包专门用于保温杯设计，包含以下子技能：

1. **cup-structure-designer** - 杯体结构设计
2. **lid-mechanism-designer** - 弹跳盖机构设计
3. **material-selector** - 材料选型助手
4. **comfyui-cup-workflow** - 保温杯专属ComfyUI工作流

## 安装方法

```bash
# 安装方法
pip install -e .
```

## 命令行使用

```bash
# 命令行使用方法
python scripts/example.py --help

# 示例命令
python scripts/example.py --input input.jpg --output output.jpg
```

## ComfyUI 工作流使用

1. 启动 ComfyUI
2. 加载 `workflows/vacuum_cup_design.json`
3. 输入提示词：
   - 杯体结构设计：`"vacuum cup body structure design, technical drawing"`
   - 弹跳盖设计：`"bounce lid mechanism design, spring hinge"`
   - 材料选型：`"material selection for vacuum cup, magnesium alloy vs carbon fiber"`

## 示例

### 杯体结构设计
```bash
python cup-structure-designer/scripts/example.py --type body --material magnesium
```

### 弹跳盖机构设计
```bash
python lid-mechanism-designer/scripts/example.py --type bounce --spring double
```

### 材料选型助手
```bash
python material-selector/scripts/example.py --weight 300g --budget 50CNY
```
