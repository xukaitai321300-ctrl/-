#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
市场预测工具 - forecast_tool.py
功能: 生成市场预测、生成市场预警、获取预测详细信息
"""

import json
import os
from datetime import datetime, timedelta

def load_market_forecast():
    """加载市场预测数据"""
    data_path = os.path.join(os.path.dirname(__file__), '../data/market_forecast.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载市场预测数据失败: {e}")
        return None

def generate_forecast(forecast_period='12months'):
    """生成市场预测"""
    data = load_market_forecast()
    if not data:
        return None
    
    # 简化实现：返回预测趋势
    forecast_data = data.get('market_forecast', {})
    
    # 构建预测结果
    result = {
        'forecast_period': f"2026-06 至 2027-06" if forecast_period == '12months' else forecast_period,
        'trends': forecast_data.get('predicted_trends', []),
        'opportunities': forecast_data.get('opportunities', []),
        'risks': forecast_data.get('risks', []),
        'overall_market_forecast': forecast_data.get('overall_market_forecast', {})
    }
    
    return result

def generate_alert():
    """生成市场预警"""
    data = load_market_forecast()
    if not data:
        return []
    
    # 返回预警列表
    alert_system = data.get('alert_system', {})
    alert_log = alert_system.get('alert_log', [])
    
    # 简化实现：返回高紧急度的预警
    high_urgency_alerts = [a for a in alert_log if a.get('urgency') == '高']
    return high_urgency_alerts

def get_forecast_details(forecast_id):
    """获取预测详细信息"""
    data = load_market_forecast()
    if not data:
        return None
    
    # 简化实现：返回整体市场预测
    forecast_data = data.get('market_forecast', {})
    overall = forecast_data.get('overall_market_forecast', {})
    
    if forecast_id == 'overall':
        return overall
    
    # 查找特定趋势
    for trend in forecast_data.get('predicted_trends', []):
        if trend.get('name') == forecast_id or trend.get('name') == forecast_id:
            return trend
    
    return None

def print_forecast_tool_example():
    """打印市场预测工具示例"""
    print("=== 市场预测工具示例 ===")
    print()
    
    # 示例1：预测未来市场趋势
    print("示例1：预测未来市场趋势")
    forecast = generate_forecast('12months')
    if forecast:
        print(f"  预测时间段: {forecast['forecast_period']}")
        print(f"  预测趋势:")
        for trend in forecast.get('trends', [])[:3]:
            print(f"    {trend['name']}: 增长率 +{trend['growth_rate']}%")
    print()
    
    # 示例2：生成市场预警
    print("==================================================")
    print("示例2：生成市场预警")
    alerts = generate_alert()
    print(f"  生成 {len(alerts)} 个高紧急度预警：")
    for i, alert in enumerate(alerts[:3], 1):
        print(f"  {i}. [{alert['alert_type']}] {alert['content']}")
    print()
    
    # 示例3：获取预测详情
    print("==================================================")
    print("示例3：获取预测详情")
    forecast_details = get_forecast_details('overall')
    if forecast_details:
        print(f"  整体市场预测:")
        print(f"    2026年市场规模: {forecast_details.get('total_market_size_2026', 'N/A')}")
        print(f"    2027年预测规模: {forecast_details.get('total_market_size_2027', 'N/A')}")
        print(f"    复合增长率: {forecast_details.get('cagr', 'N/A')}")

if __name__ == '__main__':
    print_forecast_tool_example()
