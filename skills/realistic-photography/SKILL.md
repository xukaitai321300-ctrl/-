---
name: realistic-photography
description: 保温杯产品真实摄影生图技能包，包含摄影灯光模拟、材质纹理增强、产品摄影构图、高清细节处理等功能。专为替代已归档的羊专家（zheng10-ai-image-generator）技能包而创建，是 P0 优先级的核心生图能力技能包。
version: 1.0.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-05
tags: [realistic-photography, product-photography, lighting-setup, material-texture, composition, high-resolution]
dependencies: [python>=3.8, json, argparse]
---

# 保温杯产品真实摄影生图技能包 (Realistic Photography Skill Package)

## 功能概述

本技能包提供保温杯产品的真实摄影生图能力，包含：

1. **摄影灯光模拟** - 三点布光、顶光、窗光等经典布光方案
2. **材质纹理增强** - 不锈钢、纯钛、PP、TRITAN、硅胶等材质的纹理增强
3. **产品摄影构图** - 主视角、侧视角、顶视角、细节特写、场景搭配等构图模板
4. **高清细节处理** - 材质表面细节、LOGO工艺细节、组装缝隙细节、灯光反射细节、颜色准确性细节

本技能包专为 **ComfyUI 图文生图、文生图、产品图片生成** 提供真实摄影级的提示词和参数配置，是十二生肖团（特别是羊专家）的核心技能包。

## 核心数据类型

### 1. 摄影灯光数据库
- **文件**: `data/lighting_setups.json`
- **内容**: 3种经典布光方案（三点布光、顶光、窗光）
- **字段**: 灯光类型、位置、强度、修饰件、用途、相机设置、背景设置、提示词关键词
- **应用**: 为 ComfyUI 生图提供真实摄影灯光配置

### 2. 材质纹理数据库
- **文件**: `data/material_textures.json`
- **内容**: 6种保温杯常用材料（不锈钢304/316、纯钛TA1、PP、TRITAN、硅胶）
- **字段**: 反射率、镜面高光、表面纹理、颜色变化、划痕可见性、防指纹性、摄影技巧、提示词关键词
- **应用**: 为 ComfyUI 生图提供材质纹理增强提示词

### 3. 产品摄影构图模板数据库
- **文件**: `data/composition_templates.json`
- **内容**: 5种产品摄影构图模板（主视角、侧视角、顶视角、细节特写、场景搭配）
- **字段**: 相机角度、相机距离、构图规则、背景选择、灯光配置、景深设置、提示词关键词
- **应用**: 为 ComfyUI 生图提供产品摄影构图模板

### 4. 高清细节处理数据库
- **文件**: `data/high_resolution_details.json`
- **内容**: 5种高清细节处理（材质表面细节、LOGO工艺细节、组装缝隙细节、灯光反射细节、颜色准确性细节）
- **字段**: 处理技巧、提示词关键词
- **应用**: 为 ComfyUI 生图提供高清细节处理提示词

## 数据文件结构

```
realistic-photography/
├── SKILL.md                          # 本文件
├── README.md                         # 英文说明文档
├── README_zh.md                     # 中文说明文档
├── LICENSE                          # 开源协议
├── CONTRIBUTING.md                 # 贡献指南
├── CODE_OF_CONDUCT.md              # 行为准则
├── CHANGELOG.md                   # 更新日志
├── AUTHORS.md                     # 作者信息
├── .gitignore                        # Git忽略文件
├── data/                              # 数据库目录
│   ├── lighting_setups.json        # 摄影灯光数据库
│   ├── material_textures.json      # 材质纹理数据库
│   ├── composition_templates.json  # 产品摄影构图模板数据库
│   └── high_resolution_details.json # 高清细节处理数据库
├── scripts/                           # Python工具目录
│   ├── lighting_simulator.py           # 摄影灯光模拟工具
│   ├── texture_enhancer.py           # 材质纹理增强工具
│   ├── composition_generator.py      # 构图模板生成工具
│   └── detail_processor.py         # 高清细节处理工具
├── tests/                             # 测试文件目录
│   ├── test_lighting_simulator.py
│   ├── test_texture_enhancer.py
│   ├── test_composition_generator.py
│   └── test_detail_processor.py
└── references/                       # 参考文档目录
    ├── photography_guides/            # 摄影指南文档
    ├── lighting_diagrams/             # 灯光示意图
    └── composition_examples/         # 构图示例
```

## 安装 (Installation)

1. 确保已安装 Python 3.8+。
2. 本技能包无需额外 Python 依赖（仅使用标准库：json, argparse）。

## 使用方法 (Usage)

### 命令行使用 (Command Line Usage)

```bash
# 获取摄影灯光配置
python scripts/lighting_simulator.py --setup three_point

# 获取材质纹理增强提示词
python scripts/texture_enhancer.py --material stainless_steel_304

# 获取产品摄影构图模板
python scripts/composition_generator.py --template front_view

# 获取高清细节处理提示词
python scripts/detail_processor.py --detail material_surface_detail
```

### 在 ComfyUI 中使用 (Using in ComfyUI)

1. **生成提示词**: 运行上述命令行工具，获取英文/中文提示词关键词。
2. **输入提示词**: 将提示词复制到 ComfyUI 的 Text Prompt 节点。
3. **调整参数**: 根据灯光配置、相机设置调整 ComfyUI 参数。
4. **生成图像**: 运行 ComfyUI 工作流，生成真实摄影级产品图像。

### 在 AI 生图工作流中使用 (Using in AI Image Generation Workflow)

本技能包生成的提示词可以直接用于：
- **ComfyUI**: 文生图、图生图工作流
- **Stable Diffusion**: Text-to-Image, Image-to-Image
- **Midjourney**: `/imagine` 命令
- **DALL-E**: 文本描述生成图像

## 工具脚本说明 (Tool Scripts Description)

### 1. lighting_simulator.py
- **功能**: 模拟摄影灯光配置，生成提示词
- **输入**: 布光方案ID（three_point/top_light/window_light）
- **输出**: 灯光配置详情、相机设置、背景设置、提示词关键词

### 2. texture_enhancer.py
- **功能**: 增强材质纹理，生成提示词
- **输入**: 材料ID（stainless_steel_304/stainless_steel_316/titanium_ta1/plastic_pp/tritan/silicone）
- **输出**: 材质属性、摄影技巧、提示词关键词

### 3. composition_generator.py
- **功能**: 生成产品摄影构图模板，生成提示词
- **输入**: 构图模板ID（front_view/side_view/top_view/detail_closeup/scene_matching）
- **输出**: 构图规则、相机设置、灯光配置、提示词关键词

### 4. detail_processor.py
- **功能**: 处理高清细节，生成提示词
- **输入**: 细节类型ID（material_surface_detail/logo_process_detail/assembly_seam_detail/lighting_reflection_detail/color_accuracy_detail）
- **输出**: 处理技巧、提示词关键词

## 与其他技能包的关系 (Relationship with Other Skill Packages)

- **依赖**: `vacuum-cup-materials-surface`（材料与表面处理知识）
- **依赖**: `vacuum-cup-craftsmanship`（工艺知识）
- **被依赖**: `zheng10-ai-image-generator`（羊专家技能包，已归档，由本技能包替代）
- **被依赖**: `comfyui-workflow-standard`（牛专家技能包，需要提供工作流规范）

## 质量控制 (Quality Control)

- **数据准确性**: 所有数据基于真实摄影理论和保温杯产品特性
- **提示词质量**: 英文/中文提示词均经过优化，确保生成图像质量
- **工具稳定性**: 所有 Python 工具均经过测试，确保稳定运行

## 更新日志 (Changelog)

详见 `CHANGELOG.md` 文件。

## 贡献指南 (Contributing)

详见 `CONTRIBUTING.md` 文件。

## 许可证 (License)

本技能包采用 MIT 许可证 - 详见 `LICENSE` 文件。

## 联系我们 (Contact Us)

如有任何问题或建议，请联系：速凡团队（浙江永康）