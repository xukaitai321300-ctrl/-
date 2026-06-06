# 兔专家技能包 (十二生肖团 - 兔专家)#

兔专家（图像分析专家）技能包，负责分析生成图质量、特征提取。包含生成图质量分析、特征提取、图像对比分析等功能。是十二生肖团的图像分析者。

## 功能特性#

- **生成图质量分析** - 清晰度、色彩准确性、构图合理性
- **特征提取** - 边缘检测、纹理分析、颜色直方图
- **图像对比分析** - 与竞品图像对比、与参考图像对比#

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。
2. 安装依赖：`pip install pillow opencv-python`#

## 使用方法 (Usage)#

```bash
# 分析生成图质量
python scripts/image_quality_analyzer.py --image "path/to/image.jpg"

# 提取图像特征
python scripts/feature_extractor.py --image "path/to/image.jpg"
```

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）