# 保温杯专属ComfyUI工作流使用指南

## 功能描述

本技能提供保温杯设计的专属ComfyUI工作流，支持：
- 文生图（Text-to-Image）
- 图生图（Image-to-Image）
- 产品设计图生成

## 工作流文件

- `workflows/vacuum_cup_design.json` - 保温杯设计工作流
- `workflows/lid_mechanism_design.json` - 弹跳盖机构设计工作流
- `workflows/material_showcase.json` - 材料展示工作流

## 使用方法

### 1. 加载工作流
```bash
# 启动 ComfyUI
cd /path/to/ComfyUI
python main.py

# 在浏览器中打开
# http://127.0.0.1:8188

# 加载工作流
# 点击"Load"按钮，选择 workflows/vacuum_cup_design.json
```

### 2. 文生图提示词示例
```
# 杯体结构设计
"vacuum cup body structure design, technical drawing, magnesium alloy, lightweight, cross-section view"

# 弹跳盖设计
"bounce lid mechanism design, spring hinge, technical drawing, explosion view"

# 材料展示
"material showcase, magnesium alloy AE44, carbon fiber T300, comparison"
```

### 3. 图生图使用方法
```bash
# 上传参考图
# 在 ComfyUI 中，将参考图拖入"Load Image"节点

# 修改提示词
# 在"Positive Prompt"节点中输入修改要求
"modify the cup body to be more ergonomic, keep the magnesium alloy material"
```

## 示例脚本

```bash
# 批量生成产品设计图
python scripts/batch_generate.py --prompt "vacuum cup design" --count 10 --output ./output
```
