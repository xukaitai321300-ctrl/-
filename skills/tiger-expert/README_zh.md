# 虎专家技能包 (十二生肖团 - 虎专家)#

虎专家（图像采集专家）技能包，负责采集竞品图片、跨模态搜索。包含竞品图片采集、跨模态搜索、图像预处理等功能。是十二生肖团的图像数据采集者。

## 功能特性#

- **竞品图片采集**: 从电商平台、官网、社交媒体采集竞品图片
- **跨模态搜索**: 以图搜图、以文搜图
- **图像预处理**: 图像清洗、格式转换、尺寸标准化

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。
2. 安装依赖：`pip install requests pillow`

## 使用方法 (Usage)#

```bash
# 采集竞品图片
python scripts/image_collector.py --product "保温杯" --source "天猫"

# 跨模态搜索
python scripts/cross_modal_searcher.py --query "保温杯 弹跳盖" --mode "text2image"
```

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）