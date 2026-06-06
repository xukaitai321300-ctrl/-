---
name: market-trend-analyzer
description: 保温杯市场趋势分析技能包，包含市场趋势数据、消费者需求分析、竞争对手跟踪、市场预测和预警功能
version: 1.0.0
author: 速凡团队
tags:
  - market-analysis
  - trend-forecast
  - competitor-tracking
  - consumer-insights
  - yongkang
---

# 保温杯市场趋势分析技能包

## 功能概述

本技能包提供保温杯市场趋势分析的全面数据支持，帮助速凡团队把握市场动向、了解消费者需求变化、跟踪竞争对手动态，并做出前瞻性的市场预测和预警。

## Installation

### 前提条件

- **Python版本**: 3.8+
- **必要库**: `json`, `os`, `datetime` (内置库，无需额外安装)
- **可选库**: `requests` (用于API调用，可选)

### 快速安装

```bash
# 方法1：直接下载到技能目录
cd E:\\AI日记\\Claw\\skills\\
git clone <repository_url> market-trend-analyzer

# 方法2：手动下载并解压
# 将下载的文件解压到 E:\\AI日记\\Claw\\skills\\market-trend-analyzer\\

# 验证安装
cd E:\\AI日记\\Claw\\skills\\market-trend-analyzer
python scripts/trend_analyzer.py
```

### 集成到项目

```python
# 方法1：直接导入
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'skills/market-trend-analyzer/scripts'))

from trend_analyzer import analyze_market_trend
from competitor_tracker import track_competitors
from forecast_tool import generate_forecast

# 方法2：作为Python包安装（未来支持）
# pip install market-trend-analyzer
```

## Usage

### 1. 市场趋势分析工具

```bash
# 运行市场趋势分析工具
python scripts/trend_analyzer.py
```

**输出示例：**
```
=== 市场趋势分析工具示例 ===

示例1：分析保温杯市场趋势（2024-2026）
  时间段: 2024-01 至 2026-05
  趋势方向: 上升
  市场热度: 8.5/10
  主要驱动力: 健康意识提升, 户外运动流行, 轻量化需求

==================================================

示例2：识别新兴趋势
  识别到 3 个新兴趋势：
  1. 轻量化设计 (相关度: 0.95)
  2. 智能温控 (相关度: 0.88)
  3. 环保材料 (相关度: 0.82)

==================================================

示例3：获取趋势详情
  趋势ID: light_weight_design
  名称: 轻量化设计
  相关度: 0.95
  增长潜力: 高
  关键特征: 重量减轻, 便携性提升, 材料创新
```

### 2. 竞争对手跟踪工具

```bash
# 运行竞争对手跟踪工具
python scripts/competitor_tracker.py
```

**输出示例：**
```
=== 竞争对手跟踪工具示例 ===

示例1：跟踪竞争对手动态
  竞争对手: 膳魔师 (Thermos)
  最新动态: 推出轻量化系列 (2026-03-15)
  市场份额: 18.5%
  产品策略: 高端化, 轻量化, 智能化

==================================================

示例2：对比竞争对手产品
  对比维度:
    价格定位:
      膳魔师: 高端 (¥300-800)
      虎牌: 高端 (¥250-600)
      国产品牌: 中端 (¥100-300)
    材料使用:
      膳摩师: 304不锈钢 + 纯钛
      虎牌: 316不锈钢 + 玻璃真空层
      国产品牌: 304不锈钢 + 喷漆
```

### 3. 市场预测工具

```bash
# 运行市场预测工具
python scripts/forecast_tool.py
```

**输出示例：**
```
=== 市场预测工具示例 ===

示例1：预测未来市场趋势
  预测时间段: 2026-06 至 2027-06
  预测趋势:
    轻量化保温杯: 增长率 +25%
    智能保温杯: 增长率 +40%
    环保材料保温杯: 增长率 +30%

==================================================

示例2：生成市场预警
  预警类型: 机会预警
  预警内容: 轻量化保温杯需求激增，建议加大研发投入
  紧急程度: 高
  建议行动: 在3个月内推出轻量化新产品线
```

## 核心数据类型

本技能包包含以下核心数据：

### 1. 市场趋势数据 (market_trends.json)
- **时间段分析**：2024-2026年保温杯市场趋势
- **趋势方向**：上升/下降/平稳
- **市场热度**：量化指标（0-10）
- **主要驱动力**：健康意识、户外运动、轻量化需求等
- **新兴趋势识别**：轻量化设计、智能温控、环保材料等

### 2. 消费者需求数据 (consumer_demand.json)
- **需求变化趋势**：功能需求、外观需求、价格敏感度
- **消费者画像**：年龄分布、地域分布、购买动机
- **需求预测**：未来1-2年需求变化
- **痛点分析**：现有产品不足之处

### 3. 竞争对手数据 (competitors.json)
- **主要竞争对手**：膳魔师、虎牌、象印、国产品牌等
- **产品策略**：高端化、轻量化、智能化
- **市场份额**：实时更新
- **动态跟踪**：新品发布、营销策略、价格调整

### 4. 市场预测数据 (market_forecast.json)
- **未来趋势预测**：轻量化、智能化、环保化
- **增长率预测**：各细分市场增长率
- **机会识别**：新兴市场、未满足需求
- **风险预警**：市场饱和、价格战、新进入者

## 使用方法

### 1. 命令行使用

#### 1.1 市场趋势分析工具

```bash
# 进入技能包目录
cd E:\\AI日记\\Claw\\skills\\market-trend-analyzer

# 运行市场趋势分析工具
python scripts/trend_analyzer.py
```

**输出示例：**
```
=== 市场趋势分析工具示例 ===

示例1：分析保温杯市场趋势（2024-2026）
  时间段: 2024-01 至 2026-05
  趋势方向: 上升
  市场热度: 8.5/10
  主要驱动力: 健康意识提升, 户外运动流行, 轻量化需求

==================================================

示例2：识别新兴趋势
  识别到 3 个新兴趋势：
  1. 轻量化设计 (相关度: 0.95)
  2. 智能温控 (相关度: 0.88)
  3. 环保材料 (相关度: 0.82)
```

#### 1.2 竞争对手跟踪工具

```bash
# 运行竞争对手跟踪工具
python scripts/competitor_tracker.py
```

**输出示例：**
```
=== 竞争对手跟踪工具示例 ===

示例1：跟踪竞争对手动态
  竞争对手: 膳魔师 (Thermos)
  最新动态: 推出轻量化系列 (2026-03-15)
  市场份额: 18.5%
  产品策略: 高端化, 轻量化, 智能化
```

#### 1.3 市场预测工具

```bash
# 运行市场预测工具
python scripts/forecast_tool.py
```

**输出示例：**
```
=== 市场预测工具示例 ===

示例1：预测未来市场趋势
  预测时间段: 2026-06 至 2027-06
  预测趋势:
    轻量化保温杯: 增长率 +25%
    智能保温杯: 增长率 +40%
    环保材料保温杯: 增长率 +30%
```

### 2. Python脚本调用

#### 2.1 市场趋势分析

```python
from scripts.trend_analyzer import analyze_market_trend, identify_emerging_trends

# 分析市场趋势
trend_data = analyze_market_trend(start_date='2024-01', end_date='2026-05')
print(f"趋势方向: {trend_data['direction']}")
print(f"市场热度: {trend_data['market_heat']}/10")

# 识别新兴趋势
emerging = identify_emerging_trends()
for trend in emerging[:3]:
    print(f"{trend['name']} (相关度: {trend['relevance']})")
```

#### 2.2 竞争对手跟踪

```python
from scripts.competitor_tracker import track_competitors, compare_competitors

# 跟踪竞争对手
competitor_data = track_competitors(competitor_name='膳魔师')
print(f"最新动态: {competitor_data['latest_activity']}")
print(f"市场份额: {competitor_data['market_share']}%")

# 对比竞争对手
comparison = compare_competitors(['膳魔师', '虎牌', '象印'])
```

#### 2.3 市场预测

```python
from scripts.forecast_tool import generate_forecast, generate_alert

# 生成市场预测
forecast = generate_forecast(forecast_period='12months')
for trend in forecast['trends']:
    print(f"{trend['name']}: 增长率 +{trend['growth_rate']}%")

# 生成市场预警
alerts = generate_alert()
for alert in alerts[:3]:
    print(f"预警: {alert['content']}")
```

## 数据文件说明

### data/market_trends.json
包含市场趋势数据，字段包括：
- `time_period`: 时间段
- `direction`: 趋势方向
- `market_heat`: 市场热度
- `key_drivers`: 主要驱动力
- `emerging_trends`: 新兴趋势列表

### data/consumer_demand.json
包含消费者需求数据，字段包括：
- `demand_trend`: 需求变化趋势
- `consumer_profile`: 消费者画像
- `demand_forecast`: 需求预测
- `pain_points`: 痛点分析

### data/competitors.json
包含竞争对手数据，字段包括：
- `name`: 竞争对手名称
- `market_share`: 市场份额
- `product_strategy`: 产品策略
- `latest_activity`: 最新动态

### data/market_forecast.json
包含市场预测数据，字段包括：
- `forecast_period`: 预测时间段
- `predicted_trends`: 预测趋势
- `growth_rate`: 增长率
- `opportunities`: 机会识别
- `risks`: 风险预警

## 脚本文件说明

### scripts/trend_analyzer.py
市场趋势分析工具，功能包括：
- `analyze_market_trend(start_date, end_date)`: 分析指定时间段的市场趋势
- `identify_emerging_trends()`: 识别新兴趋势
- `get_trend_details(trend_id)`: 获取趋势详细信息

### scripts/competitor_tracker.py
竞争对手跟踪工具，功能包括：
- `track_competitors(competitor_name)`: 跟踪指定竞争对手
- `compare_competitors(competitor_list)`: 对比多个竞争对手
- `get_competitor_details(competitor_id)`: 获取竞争对手详细信息

### scripts/forecast_tool.py
市场预测工具，功能包括：
- `generate_forecast(forecast_period)`: 生成市场预测
- `generate_alert()`: 生成市场预警
- `get_forecast_details(forecast_id)`: 获取预测详细信息

## 应用场景

### 1. 产品规划
- 根据市场趋势调整产品方向
- 识别新兴需求，提前布局
- 优化产品功能，满足消费者痛点

### 2. 竞争策略
- 跟踪竞争对手动态，及时调整策略
- 分析竞争对手优劣势，找到差异化机会
- 监控市场份额变化，评估竞争态势

### 3. 市场预测
- 预测未来市场趋势，提前准备
- 识别市场机会，抢占先机
- 预警市场风险，制定应对措施

### 4. 营销决策
- 根据消费者需求制定营销策略
- 选择合适的营销渠道和时机
- 优化产品定价和促销策略

## 注意事项

1. **数据时效性**：市场数据需要定期更新（建议每月更新一次）
2. **数据来源**：数据来源于行业报告、电商平台、社交媒体等，需要交叉验证
3. **预测准确性**：市场预测存在不确定性，需要结合实际情况调整
4. **竞争对手跟踪**：需要持续跟踪，及时发现变化

## 更新日志

### v1.0.0 (2026-06-05)
- 初始版本发布
- 包含市场趋势分析、竞争对手跟踪、市场预测功能
- 提供3个核心脚本工具
- 提供4个数据文件

---

**技能包位置**: `E:\\AI日记\\Claw\\skills\\market-trend-analyzer\\`
**适用场景**: 保温杯市场分析、产品规划、竞争策略、营销决策
**目标用户**: 速凡团队（浙江永康），保温杯制造商
