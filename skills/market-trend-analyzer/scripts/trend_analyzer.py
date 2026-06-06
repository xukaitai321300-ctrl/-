#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
市场趋势分析工具 - trend_analyzer.py
功能: 分析保温杯市场趋势、识别新兴趋势、获取趋势详细信息
"""

import json
import os
from datetime import datetime

def load_market_trends():
    """加载市场趋势数据"""
    data_path = os.path.join(os.path.dirname(__file__), '../data/market_trends.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载市场趋势数据失败: {e}")
        return None

def analyze_market_trend(start_date, end_date):
    """分析指定时间段的市场趋势"""
    data = load_market_trends()
    if not data:
        return None
    
    # 简化实现：返回整体趋势分析
    trend_analysis = {
        'time_period': f"{start_date} 至 {end_date}",
        'direction': data['trend_analysis']['overall_direction'],
        'market_heat': data['trend_analysis']['average_market_heat'],
        'key_drivers': data['trend_analysis']['top_drivers'],
        'emerging_trends_count': data['trend_analysis']['emerging_trends_count'],
        'high_potential_trends': data['trend_analysis']['high_potential_trends']
    }
    
    return trend_analysis

def identify_emerging_trends():
    """识别新兴趋势"""
    data = load_market_trends()
    if not data:
        return []
    
    # 返回趋势列表（按相关度排序）
    trends = data.get('market_trends', [])
    # 按相关度排序
    sorted_trends = sorted(trends, key=lambda x: x.get('relevance', 0), reverse=True)
    return sorted_trends

def get_trend_details(trend_id):
    """获取趋势详细信息"""
    data = load_market_trends()
    if not data:
        return None
    
    # 查找指定ID的趋势
    for trend in data.get('market_trends', []):
        if trend.get('id') == trend_id:
            return trend
    
    return None

def print_market_trend_example():
    """打印市场趋势分析工具示例"""
    print("=== 市场趋势分析工具示例 ===")
    print()
    
    # 示例1：分析保温杯市场趋势（2024-2026）
    print("示例1：分析保温杯市场趋势（2024-2026）")
    trend_data = analyze_market_trend('2024-01', '2026-05')
    if trend_data:
        print(f"  时间段: {trend_data['time_period']}")
        print(f"  趋势方向: {trend_data['direction']}")
        print(f"  市场热度: {trend_data['market_heat']}/10")
        print(f"  主要驱动力: {', '.join(trend_data['key_drivers'])}")
        print()
    
    # 示例2：识别新兴趋势
    print("==================================================")
    print("示例2：识别新兴趋势")
    emerging = identify_emerging_trends()
    print(f"  识别到 {len(emerging)} 个新兴趋势：")
    for i, trend in enumerate(emerging[:3], 1):
        print(f"  {i}. {trend['name']} (相关度: {trend.get('relevance', 'N/A')})")
    print()
    
    # 示例3：获取趋势详情
    print("==================================================")
    print("示例3：获取趋势详情")
    trend_details = get_trend_details('light_weight_design')
    if trend_details:
        print(f"  趋势ID: {trend_details['id']}")
        print(f"  名称: {trend_details['name']}")
        print(f"  相关度: {trend_details.get('relevance', 'N/A')}")
        print(f"  增长潜力: {trend_details.get('growth_potential', 'N/A')}")
        print(f"  关键特征: {', '.join(trend_details.get('key_features', []))}")

if __name__ == '__main__':
    print_market_trend_example()
