#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
竞争对手跟踪工具 - competitor_tracker.py
功能: 跟踪竞争对手动态、对比竞争对手、获取竞争对手详细信息
"""

import json
import os

def load_competitors():
    """加载竞争对手数据"""
    data_path = os.path.join(os.path.dirname(__file__), '../data/competitors.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载竞争对手数据失败: {e}")
        return None

def track_competitors(competitor_name):
    """跟踪指定竞争对手"""
    data = load_competitors()
    if not data:
        return None
    
    # 查找指定竞争对手
    for comp in data.get('competitors', []):
        if comp.get('name') == competitor_name or comp.get('english_name') == competitor_name:
            return comp
    
    return None

def compare_competitors(competitor_list):
    """对比多个竞争对手"""
    data = load_competitors()
    if not data:
        return []
    
    results = []
    for comp in data.get('competitors', []):
        if comp.get('name') in competitor_list or comp.get('english_name') in competitor_list:
            results.append(comp)
    
    return results

def get_competitor_details(competitor_id):
    """获取竞争对手详细信息"""
    data = load_competitors()
    if not data:
        return None
    
    # 查找指定ID的竞争对手
    for comp in data.get('competitors', []):
        if comp.get('id') == competitor_id:
            return comp
    
    return None

def print_competitor_tracker_example():
    """打印竞争对手跟踪工具示例"""
    print("=== 竞争对手跟踪工具示例 ===")
    print()
    
    # 示例1：跟踪竞争对手动态
    print("示例1：跟踪竞争对手动态")
    comp_data = track_competitors('膳魔师')
    if comp_data:
        print(f"  竞争对手: {comp_data['name']} ({comp_data.get('english_name', 'N/A')})")
        print(f"  最新动态: {comp_data.get('latest_activity', 'N/A')}")
        print(f"  市场份额: {comp_data.get('market_share', 'N/A')}%")
        print(f"  产品策略: {', '.join(comp_data.get('product_strategy', []))}")
    print()
    
    # 示例2：对比竞争对手产品
    print("==================================================")
    print("示例2：对比竞争对手产品")
    comparison = compare_competitors(['膳魔师', '虎牌', '象印'])
    if comparison:
        print(f"  对比维度:")
        print(f"    价格定位:")
        for comp in comparison:
            print(f"      {comp['name']}: {comp.get('price_positioning', 'N/A')} ({comp.get('price_range', 'N/A')})")
        print(f"    材料使用:")
        for comp in comparison:
            print(f"      {comp['name']}: {', '.join(comp.get('materials_used', []))}")
    print()
    
    # 示例3：获取竞争对手详情
    print("==================================================")
    print("示例3：获取竞争对手详情")
    comp_details = get_competitor_details('thermos')
    if comp_details:
        print(f"  竞争对手ID: {comp_details['id']}")
        print(f"  名称: {comp_details['name']}")
        print(f"  市场份额: {comp_details.get('market_share', 'N/A')}%")
        print(f"  优势: {', '.join(comp_details.get('strengths', []))}")
        print(f"  劣势: {', '.join(comp_details.get('weaknesses', []))}")

if __name__ == '__main__':
    print_competitor_tracker_example()
