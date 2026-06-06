---
name: tiger-expert
description: 虎专家（图像采集专家）技能包，负责采集竞品图片、跨模态搜索。包含竞品图片采集、跨模态搜索、图像预处理等功能。是十二生肖团的图像数据采集者。
version: 1.3.0
author: 速凡团队（浙江永康）
last_updated: 2026-06-06
tags: [tiger-expert, image-collection, cross-modal-search, image-preprocessing, twelve-zodiac-team]
dependencies: [python>=3.8, json, argparse, requests, pillow]
---

# 虎专家（图像采集专家）技能包

## 功能概述#

本技能包提供图像采集功能，包含：

1. **竞品图片采集** - 从电商平台、官网、社交媒体采集竞品图片
2. **跨模态搜索** - 以图搜图、以文搜图
3. **图像预处理** - 图像清洗、格式转换、尺寸标准化

虎专家是十二生肖团的**图像数据采集者**，负责为生成提供高质量参考素材。

## 详细功能说明#

### 1. 竞品图片采集
从以下平台采集竞品图片：
- **电商平台**：天猫、淘宝、京东、拼多多
- **官网**：品牌官方网站
- **社交媒体**：小红书、抖音、微博

**采集内容**：
- 产品主图（白底图）
- 产品详情图（细节图）
- 产品使用场景图
- 用户评价图

### 2. 跨模态搜索
- **以文搜图**：输入文字描述，搜索相关图片
- **以图搜图**：输入参考图片，搜索相似图片

**使用场景**：
- 寻找竞品图片（输入："保温杯 弹跳盖"）
- 寻找风格参考（输入："简约风格 保温杯"）
- 寻找材质参考（输入："镁合金 保温杯"）

### 3. 图像预处理
- **图像清洗**：去除重复图片、低质量图片
- **格式转换**：统一转换为JPG/PNG格式
- **尺寸标准化**：统一调整为标准尺寸（如：800x800像素）

## 安装 (Installation)#

1. 确保已安装 Python 3.8+。
2. 安装依赖：`pip install requests pillow`

## 使用方法 (Usage)#

### 命令行使用 (Command Line Usage)#

```bash
# 采集竞品图片（从天猫）
python scripts/image_collector.py --product "vacuum cup" --source "tmall" --output "data/tmall_images/"

# 跨模态搜索（以文搜图）
python scripts/cross_modal_searcher.py --query "保温杯 弹跳盖" --mode "text2image" --output "data/reference_images/"

# 跨模态搜索（以图搜图）
python scripts/cross_modal_searcher.py --image "data/reference_images/cup_001.jpg" --mode "image2image" --output "data/similar_images/"

# 图像预处理（清洗、格式转换、尺寸标准化）
python scripts/image_preprocessor.py --input "data/raw_images/" --output "data/processed_images/" --size "800x800"
```

### 输出文件格式#

#### 1. 竞品图片采集输出
**目录结构**：
```
data/tmall_images/
├─ product_001/
│   ├─ main.jpg           # 产品主图
│   ├─ detail_001.jpg    # 产品详情图
│   ├─ detail_002.jpg
│   ├─ scene_001.jpg     # 产品使用场景图
│   └─ review_001.jpg    # 用户评价图
├─ product_002/
│   └─ ...
└─ metadata.json          # 元数据文件（产品信息、图片信息）
```

**元数据文件格式**（metadata.json）：
```json
{
  "product_id": "product_001",
  "product_name": "弹跳盖保温杯",
  "brand": "膳魔师",
  "price": "199元",
  "source": "tmall",
  "images": [
    {
      "file_name": "main.jpg",
      "image_type": "main",
      "width": 800,
      "height": 800,
      "format": "jpg"
    },
    ...
  ]
}
```

#### 2. 跨模态搜索输出
**目录结构**：
```
data/reference_images/
├─ query_001/
│   ├─ result_001.jpg
│   ├─ result_002.jpg
│   └─ ...
└─ metadata.json          # 元数据文件（搜索条件、结果信息）
```

#### 3. 图像预处理输出
**目录结构**：
```
data/processed_images/
├─ product_001/
│   ├─ main_800x800.jpg
│   ├─ detail_001_800x800.jpg
│   └─ ...
└─ metadata.json          # 元数据文件（预处理信息）
```

## 与其他技能包的数据传输#

### 输入（接收其他技能包的数据）
- **鼠专家**：接收需求分析报告（含竞品列表）
- **龙专家**：接收竞品分析结果（含重点竞品图片URL）

### 输出（向其他技能包传输数据）
- **兔专家**：输出竞品图片集（供图像分析）
- **蛇专家**：输出竞品图片集（供产品设计参考）
- **羊专家**：输出参考图片集（供提示词工程参考）

### 数据传输格式
- **文件传输**：图片文件（JPG/PNG格式）
- **元数据传输**：JSON文件（metadata.json）

## 案例分析

本文档的案例分析已合并到通用文档中，详见：`E:\AI日记\Claw\技能包通用文档\案例分析集_20260606_v1.0.md`

## 常见问题解答 (FAQ)#

### Q1：图片采集失败怎么办？
**A**：检查网络连接、平台访问权限、产品关键词是否正确。可以尝试更换平台（如：从天猫更换为京东）。

### Q2：跨模态搜索结果不准确怎么办？
**A**：优化搜索关键词（增加描述词、更换同义词）。可以尝试使用以图搜图模式（提供更准确的参考图片）。

### Q3：图像预处理后图片质量下降怎么办？
**A**：调整预处理参数（如：降低尺寸压缩率、使用更高质量的格式）。可以保留原始图片备份。

## 技能包质量#

本技能包设计目标质量分数：**90+**（目标：100/100）

### 质量改进记录
| 版本 | 日期 | 改进内容 |
|------|------|---------|
| v1.0.0 | 2026-06-05 | 初始版本 |
| v1.1.0 | 2026-06-06 | 增加详细功能说明、使用示例、输出文件格式、数据传输说明、案例分析、FAQ |

---

**技能包结束**

*本技能包是十二生肖团的图像数据采集者，负责为生成提供高质量参考素材。*
