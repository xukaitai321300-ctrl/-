#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
材料选择工具 - 根据需求推荐合适的保温杯材料
"""

import json
import os

def load_materials():
    """加载材料数据"""
    data_path = os.path.join(os.path.dirname(__file__), '../data/materials.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_material(requirements):
    """
    根据需求选择材料
    
    参数:
        requirements: dict, 需求参数，包含：
            - weight_sensitive: bool, 是否重量敏感（需要轻量化）
            - safety_level: str, 安全级别要求 ('food_grade', 'medical_grade', 'biocompatible')
            - cost_sensitive: bool, 是否成本敏感
            - local_supply_preferred: bool, 是否优先本地供应
    
    返回:
        list: 推荐材料列表
    """
    materials_data = load_materials()
    materials = materials_data['materials']
    
    recommended = []
    
    # 轻量化需求
    if requirements.get('weight_sensitive', False):
        # 优先推荐纯钛
        for material in materials:
            if material['type'] == 'titanium':
                recommended.append(material)
        # 如果不要求最高安全级别，也可以推荐不锈钢
        if requirements.get('safety_level') != 'biocompatible':
            for material in materials:
                if material['type'] == 'stainless_steel':
                    if material not in recommended:
                        recommended.append(material)
    else:
        # 不要求轻量化，推荐所有材料
        recommended = materials.copy()
    
    # 安全级别过滤
    if 'safety_level' in requirements:
        safety_levels = {'food_grade': 1, 'medical_grade': 2, 'biocompatible': 3}
        required_level = safety_levels.get(requirements['safety_level'], 0)
        
        filtered = []
        for material in recommended:
            material_level = safety_levels.get(material['safety_level'], 0)
            if material_level >= required_level:
                filtered.append(material)
        recommended = filtered
    
    # 成本敏感过滤
    if requirements.get('cost_sensitive', False):
        # 按成本指数排序
        recommended.sort(key=lambda x: x['cost_index'])
    
    # 本地供应优先
    if requirements.get('local_supply_preferred', False):
        # 将本地供应的材料排在前面
        recommended.sort(key=lambda x: not x.get('local_supply', False))
    
    return recommended

def compare_materials(material_ids):
    """
    对比多种材料的性能
    
    参数:
        material_ids: list, 材料ID列表
    
    返回:
        dict: 对比结果
    """
    materials_data = load_materials()
    materials = materials_data['materials']
    
    selected = []
    for material in materials:
        if material['id'] in material_ids:
            selected.append(material)
    
    if not selected:
        return {'error': '未找到指定材料'}
    
    # 构建对比表
    comparison = {
        'materials': selected,
        'comparison_table': {}
    }
    
    # 对比维度
    dimensions = ['density', 'corrosion_resistance', 'safety_level', 'cost_index', 
                 'weight_500ml', 'insulation_performance', 'processing_difficulty']
    
    for dimension in dimensions:
        comparison['comparison_table'][dimension] = {}
        for material in selected:
            comparison['comparison_table'][dimension][material['id']] = material.get(dimension, 'N/A')
    
    return comparison

def get_material_by_id(material_id):
    """
    根据ID获取材料详细信息
    
    参数:
        material_id: str, 材料ID
    
    返回:
        dict: 材料详细信息
    """
    materials_data = load_materials()
    for material in materials_data['materials']:
        if material['id'] == material_id:
            return material
    return None

if __name__ == '__main__':
    # 示例用法
    print("=== 材料选择工具示例 ===\n")
    
    # 示例1：轻量化需求
    print("示例1：轻量化需求")
    req1 = {
        'weight_sensitive': True,
        'safety_level': 'medical_grade',
        'cost_sensitive': False
    }
    recommended1 = select_material(req1)
    for mat in recommended1:
        print(f"  - {mat['name']} (成本指数: {mat['cost_index']})")
    
    print("\n" + "="*50 + "\n")
    
    # 示例2：成本敏感
    print("示例2：成本敏感需求")
    req2 = {
        'weight_sensitive': False,
        'safety_level': 'food_grade',
        'cost_sensitive': True,
        'local_supply_preferred': True
    }
    recommended2 = select_material(req2)
    for mat in recommended2[:3]:  # 只显示前3个
        print(f"  - {mat['name']} (成本指数: {mat['cost_index']}, 本地供应: {mat.get('local_supply', False)})")
    
    print("\n" + "="*50 + "\n")
    
    # 示例3：材料对比
    print("示例3：材料对比 (304不锈钢 vs TA2纯钛)")
    comparison = compare_materials(['304_stainless_steel', 'ta2_titanium'])
    if 'comparison_table' in comparison:
        print("  对比维度:")
        for dimension, values in comparison['comparison_table'].items():
            print(f"    {dimension}:")
            for material_id, value in values.items():
                material = get_material_by_id(material_id)
                print(f"      {material['name']}: {value}")
