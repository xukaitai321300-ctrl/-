# 市场趋势分析技能包

保温杯市场趋势分析技能包，包含市场趋势数据、消费者需求分析、竞争对手跟踪、市场预测和预警功能。

## 功能特性

- **市场趋势分析**: 分析保温杯市场趋势（2024-2026）
- **消费者需求分析**: 了解消费者需求变化和痛点
- **竞争对手跟踪**: 跟踪竞争对手动态和产品策略
- **市场预测**: 生成市场预测，识别增长机会
- **预警系统**: 接收市场机会和风险预警

## 安装使用

### 前提条件

- **Python版本**: 3.8+
- **必要库**: `json`, `os`, `datetime` (内置库，无需额外安装)
- **可选库**: `requests` (用于API调用，可选)

### 快速开始

```bash
# 方法1：克隆到技能目录
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

## 使用方法

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

## 作者

速凡团队 (Sufan Team)

## 许可证

MIT License - 详见 LICENSE 文件
