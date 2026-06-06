# Market Trend Analyzer

保温杯市场趋势分析技能包，包含市场趋势数据、消费者需求分析、竞争对手跟踪、市场预测和预警功能。

## Features

- **Market Trend Analysis**: Analyze market trends for vacuum cups (2024-2026)
- **Consumer Demand Analysis**: Understand changing consumer demands and pain points
- **Competitor Tracking**: Track competitor dynamics and product strategies
- **Market Forecast**: Generate market forecasts and identify growth opportunities
- **Alert System**: Receive alerts for market opportunities and risks

## Installation

### Prerequisites

- **Python Version**: 3.8+
- **Required Libraries**: `json`, `os`, `datetime` (built-in, no installation needed)
- **Optional Libraries**: `requests` (for API calls, optional)

### Quick Start

```bash
# Method 1: Clone to skills directory
cd E:\\AI日记\\Claw\\skills\\
git clone <repository_url> market-trend-analyzer

# Method 2: Manual download and extract
# Extract downloaded files to E:\\AI日记\\Claw\\skills\\market-trend-analyzer\\

# Verify installation
cd E:\\AI日记\\Claw\\skills\\market-trend-analyzer
python scripts/trend_analyzer.py
```

### Integration into Projects

```python
# Method 1: Direct import
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'skills/market-trend-analyzer/scripts'))

from trend_analyzer import analyze_market_trend
from competitor_tracker import track_competitors
from forecast_tool import generate_forecast

# Method 2: Install as Python package (future support)
# pip install market-trend-analyzer
```

## Usage

### 1. Market Trend Analysis Tool

```bash
# Run market trend analysis tool
python scripts/trend_analyzer.py
```

**Output Example:**
```
=== Market Trend Analysis Tool Example ===

Example 1: Analyze vacuum cup market trend (2024-2026)
  Period: 2024-01 to 2026-05
  Trend Direction: Upward
  Market Heat: 8.5/10
  Key Drivers: Health awareness, Outdoor sports popularity, Lightweight demand

==================================================

Example 2: Identify emerging trends
  Identified 3 emerging trends:
  1. Lightweight design (Relevance: 0.95)
  2. Smart temperature control (Relevance: 0.88)
  3. Eco-friendly materials (Relevance: 0.82)

==================================================

Example 3: Get trend details
  Trend ID: light_weight_design
  Name: Lightweight Design
  Relevance: 0.95
  Growth Potential: High
  Key Features: Weight reduction, Portability improvement, Material innovation
```

### 2. Competitor Tracking Tool

```bash
# Run competitor tracking tool
python scripts/competitor_tracker.py
```

**Output Example:**
```
=== Competitor Tracking Tool Example ===

Example 1: Track competitor dynamics
  Competitor: Thermos
  Latest Activity: Launched lightweight series (2026-03-15)
  Market Share: 18.5%
  Product Strategy: High-end, Lightweight, Smart

==================================================

Example 2: Compare competitor products
  Comparison Dimensions:
    Price Positioning:
      Thermos: High-end (¥300-800)
      Tiger: High-end (¥250-600)
      Domestic brands: Mid-range (¥100-300)
    Material Usage:
      Thermos: 304 stainless steel + Pure titanium
      Tiger: 316 stainless steel + Glass vacuum layer
      Domestic brands: 304 stainless steel + Spray painting
```

### 3. Market Forecast Tool

```bash
# Run market forecast tool
python scripts/forecast_tool.py
```

**Output Example:**
```
=== Market Forecast Tool Example ===

Example 1: Forecast future market trends
  Forecast Period: 2026-06 to 2027-06
  Forecast Trends:
    Lightweight vacuum cups: Growth rate +25%
    Smart vacuum cups: Growth rate +40%
    Eco-friendly material vacuum cups: Growth rate +30%

==================================================

Example 2: Generate market alerts
  Alert Type: Opportunity Alert
  Alert Content: Surge in lightweight vacuum cup demand, recommend increasing R&D investment
  Urgency: High
  Suggested Action: Launch lightweight new product line within 3 months
```

## Data Files

### data/market_trends.json
Contains market trend data, fields include:
- `time_period`: Time period
- `direction`: Trend direction
- `market_heat`: Market heat index
- `key_drivers`: Key drivers
- `emerging_trends`: Emerging trends list

### data/consumer_demand.json
Contains consumer demand data, fields include:
- `demand_trend`: Demand change trends
- `consumer_profile`: Consumer profile
- `demand_forecast`: Demand forecast
- `pain_points`: Pain points analysis

### data/competitors.json
Contains competitor data, fields include:
- `name`: Competitor name
- `market_share`: Market share
- `product_strategy`: Product strategy
- `latest_activity`: Latest activity

### data/market_forecast.json
Contains market forecast data, fields include:
- `forecast_period`: Forecast period
- `predicted_trends`: Predicted trends
- `growth_rate`: Growth rate
- `opportunities`: Opportunity identification
- `risks`: Risk alerts

## Script Files

### scripts/trend_analyzer.py
Market trend analysis tool, functions include:
- `analyze_market_trend(start_date, end_date)`: Analyze market trends for specified period
- `identify_emerging_trends()`: Identify emerging trends
- `get_trend_details(trend_id)`: Get detailed trend information

### scripts/competitor_tracker.py
Competitor tracking tool, functions include:
- `track_competitors(competitor_name)`: Track specified competitor
- `compare_competitors(competitor_list)`: Compare multiple competitors
- `get_competitor_details(competitor_id)`: Get detailed competitor information

### scripts/forecast_tool.py
Market forecast tool, functions include:
- `generate_forecast(forecast_period)`: Generate market forecast
- `generate_alert()`: Generate market alerts
- `get_forecast_details(forecast_id)`: Get detailed forecast information

## Application Scenarios

### 1. Product Planning
- Adjust product direction based on market trends
- Identify emerging demands and plan ahead
- Optimize product features to meet consumer pain points

### 2. Competition Strategy
- Track competitor dynamics and adjust strategies timely
- Analyze competitor strengths and weaknesses to find differentiation opportunities
- Monitor market share changes and evaluate competitive landscape

### 3. Market Prediction
- Predict future market trends and prepare in advance
- Identify market opportunities and seize the initiative
- Alert market risks and formulate response measures

### 4. Marketing Decisions
- Formulate marketing strategies based on consumer demand
- Choose appropriate marketing channels and timing
- Optimize product pricing and promotion strategies

## Notes

1. **Data Timeliness**: Market data needs regular updates (recommended monthly)
2. **Data Sources**: Data comes from industry reports, e-commerce platforms, social media, etc., needs cross-validation
3. **Prediction Accuracy**: Market predictions have uncertainty, need to combine with actual situations for adjustment
4. **Competitor Tracking**: Requires continuous tracking to detect changes timely

## Changelog

### v1.0.0 (2026-06-05)
- Initial version release
- Includes market trend analysis, competitor tracking, market forecast functions
- Provides 3 core script tools
- Provides 4 data files

## Author

速凡团队 (Sufan Team)

## License

MIT License - see LICENSE file for details
