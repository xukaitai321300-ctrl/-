#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工艺推荐工具 - 根据需求推荐合适的表面处理和LOGO工艺
"""

import json
import os

def load_data():
    """加载所有数据"""
    base_path = os.path.join(os.path.dirname(__file__), '../data')
    
    with open(os.path.join(base_path, 'surface_treatment.json'), 'r', encoding='utf-8') as f:
        surface_data = json.load(f)
    
    with open(os.path.join(base_path, 'logo_process.json'), 'r', encoding='utf-8') as f:
        logo_data = json.load(f)
    
    return surface_data, logo_data

def recommend_surface_treatment(requirements):
    """
    推荐表面处理工艺
    
    参数:
        requirements: dict, 需求参数，包含：
            - budget_level: str, 预算水平 ('low', 'medium', 'high')
            - batch_size: int, 订单数量
            - durability_requirement: str, 耐久性要求 ('low', 'medium', 'high')
            - environmental_requirement: str, 环保要求 ('low', 'medium', 'high')
            - application: str, 应用场景
    
    返回:
        list: 推荐工艺列表
    """
    surface_data, _ = load_data()
    processes = surface_data['surface_treatments']
    
    recommended = []
    
    # 根据预算过滤
    if 'budget_level' in requirements:
        budget = requirements['budget_level']
        if budget == 'low':
            # 低成本：成本指数 <= 1.0
            recommended = [p for p in processes if p.get('total_cost_index', 0) <= 1.0]
        elif budget == 'medium':
            # 中成本：成本指数 <= 1.5
            recommended = [p for p in processes if p.get('total_cost_index', 0) <= 1.5]
        else:  # high
            # 高成本：所有工艺
            recommended = processes.copy()
    
    # 根据订单数量过滤
    if 'batch_size' in requirements:
        batch = requirements['batch_size']
        if batch < 100:
            # 小批量：适合任意批量或低MOQ的工艺
            recommended = [p for p in recommended if p.get('suitable_batch', '任意批量') == '任意批量' or 
                         p.get('min_order_quantity', 0) <= batch]
        elif batch < 1000:
            # 中批量
            recommended = [p for p in recommended if p.get('min_order_quantity', 0) <= batch]
    
    # 根据耐久性要求过滤
    if 'durability_requirement' in requirements:
        durability_map = {'low': 1, 'medium': 2, 'high': 3}
        required_level = durability_map.get(requirements['durability_requirement'], 2)
        
        # 简单评估耐久性
        filtered = []
        for p in recommended:
            durability = p.get('durability', '中等')
            if durability == '优秀（永久性标记）' or durability == '优秀（浮雕立体化）' or durability == '优秀':
                level = 3
            elif durability == '中等（高温易起泡）' or durability == '中等':
                level = 2
            else:
                level = 1
            
            if level >= required_level:
                filtered.append(p)
        
        recommended = filtered
    
    # 根据环保要求过滤
    if 'environmental_requirement' in requirements:
        env_map = {'low': 1, 'medium': 2, 'high': 3}
        required_level = env_map.get(requirements['environmental_requirement'], 2)
        
        filtered = []
        for p in recommended:
            env_grade = p.get('environmental_friendliness', '一般')
            if env_grade == '优秀':
                level = 3
            elif env_grade == '良好':
                level = 2
            else:
                level = 1
            
            if level >= required_level:
                filtered.append(p)
        
        recommended = filtered
    
    # 如果推荐结果为空，返回所有工艺
    if not recommended:
        recommended = processes.copy()
    
    # 按成本指数排序
    recommended.sort(key=lambda x: x.get('total_cost_index', 0))
    
    return recommended

def recommend_logo_process(requirements):
    """
    推荐LOGO工艺
    
    参数:
        requirements: dict, 需求参数，包含：
            - logo_type: str, LOGO类型 ('text', 'simple_pattern', 'complex_pattern', '3d')
            - budget_level: str, 预算水平 ('low', 'medium', 'high')
            - batch_size: int, 订单数量
            - durability_requirement: str, 耐久性要求 ('low', 'medium', 'high')
    
    返回:
        list: 推荐工艺列表
    """
    _, logo_data = load_data()
    processes = logo_data['logo_processes']
    
    recommended = []
    
    # 根据LOGO类型推荐
    if 'logo_type' in requirements:
        logo_type = requirements['logo_type']
        type_map = {
            'text': ['laser_marking'],
            'simple_pattern': ['screen_printing', 'laser_marking'],
            'complex_pattern': ['heat_transfer_printing', 'air_dye_printing', '3d_uv_printing'],
            '3d': ['3d_uv_printing', 'electroplating', 'gold_foil_sticking']
        }
        
        preferred_ids = type_map.get(logo_type, [])
        recommended = [p for p in processes if p['id'] in preferred_ids]
    
    # 如果根据LOGO类型没有找到，使用所有工艺
    if not recommended:
        recommended = processes.copy()
    
    # 根据预算过滤
    if 'budget_level' in requirements:
        budget = requirements['budget_level']
        if budget == 'low':
            # 低成本
            recommended = [p for p in recommended if p.get('cost_per_cup', '¥0').replace('¥', '').replace('/杯', '') < '1.0']
        elif budget == 'medium':
            # 中成本
            recommended = [p for p in recommended if p.get('cost_per_cup', '¥0').replace('¥', '').replace('/杯', '') < '3.0']
    
    # 根据订单数量过滤
    if 'batch_size' in requirements:
        batch = requirements['batch_size']
        recommended = [p for p in recommended if p.get('min_order_quantity', 0) <= batch]
    
    # 根据耐久性要求过滤
    if 'durability_requirement' in requirements:
        durability_map = {'low': 1, 'medium': 2, 'high': 3}
        required_level = durability_map.get(requirements['durability_requirement'], 2)
        
        filtered = []
        for p in recommended:
            durability = p.get('durability', '中等')
            if durability == '优秀':
                level = 3
            elif durability == '中等':
                level = 2
            else:
                level = 1
            
            if level >= required_level:
                filtered.append(p)
        
        recommended = filtered
    
    # 如果推荐结果为空，返回所有工艺
    if not recommended:
        recommended = processes.copy()
    
    # 按成本排序
    def extract_cost(process):
        cost_str = process.get('cost_per_cup', '¥0/杯')
        if '¥' in cost_str and '/' in cost_str:
            cost_range = cost_str.replace('¥', '').replace('/杯', '')
            if '-' in cost_range:
                low, high = map(float, cost_range.split('-'))
                return (low + high) / 2
            else:
                return float(cost_range)
        return 0
    
    recommended.sort(key=extract_cost)
    
    return recommended

def get_process_details(process_id, process_type='surface'):
    """
    获取工艺详细信息
    
    参数:
        process_id: str, 工艺ID
        process_type: str, 工艺类型 ('surface' 或 'logo')
    
    返回:
        dict: 工艺详细信息
    """
    surface_data, logo_data = load_data()
    
    if process_type == 'surface':
        for p in surface_data['surface_treatments']:
            if p['id'] == process_id:
                return p
    else:  # logo
        for p in logo_data['logo_processes']:
            if p['id'] == process_id:
                return p
    
    return None

if __name__ == '__main__':
    # 示例用法
    print("=== 工艺推荐工具示例 ===\n")
    
    # 示例1：推荐表面处理工艺
    print("示例1：推荐表面处理工艺")
    print("需求：低成本、小批量、中等耐久性")
    req1 = {
        'budget_level': 'low',
        'batch_size': 50,
        'durability_requirement': 'medium'
    }
    recommended1 = recommend_surface_treatment(req1)
    print(f"推荐工艺（前3个）:")
    for i, p in enumerate(recommended1[:3], 1):
        print(f"  {i}. {p['name']} (成本指数: {p.get('total_cost_index', 'N/A')})")
    
    print("\n" + "="*50 + "\n")
    
    # 示例2：推荐LOGO工艺
    print("示例2：推荐LOGO工艺")
    print("需求：文字LOGO、低成本、小批量、高耐久性")
    req2 = {
        'logo_type': 'text',
        'budget_level': 'low',
        'batch_size': 100,
        'durability_requirement': 'high'
    }
    recommended2 = recommend_logo_process(req2)
    print(f"推荐工艺（前3个）:")
    for i, p in enumerate(recommended2[:3], 1):
        print(f"  {i}. {p['name']} (单杯成本: {p.get('cost_per_cup', 'N/A')})")
    
    print("\n" + "="*50 + "\n")
    
    # 示例3：获取工艺详情
    print("示例3：获取工艺详情")
    print("工艺ID: laser_marking (激光打标)")
    details = get_process_details('laser_marking', 'logo')
    if details:
        print(f"  名称: {details['name']}")
        print(f"  最小订单量: {details['min_order_quantity']}")
        print(f"  单杯成本: {details.get('cost_per_cup', 'N/A')}")
        print(f"  生产周期: {details.get('production_cycle', 'N/A')}")
        print(f"  耐久性: {details.get('durability', 'N/A')}")
        print(f"  优点: {', '.join(details.get('advantages', []))}")
