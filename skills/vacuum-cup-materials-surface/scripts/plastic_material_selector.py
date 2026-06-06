#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
塑料材料选择工具
提供保温杯塑料盖材料的选择、对比和推荐功能
"""

import json
import os

def load_plastic_materials():
    """加载塑料材料数据库"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'materials_plastic.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_plastic_material(requirements):
    """
    根据需求选择塑料材料
    
    Args:
        requirements: 需求字典，可包含：
            - application: 应用场景（cup_lid, sealing_ring, outer_shell, decoration）
            - temperature_range: 温度范围（high_temp, medium_temp, low_temp）
            - cost_level: 成本级别（low, medium, high）
            - safety_requirement: 安全要求（bpa_free_required, high_transparency, soft_touch）
            - process_method: 加工方法（injection, compression）
    
    Returns:
        推荐材料列表
    """
    data = load_plastic_materials()
    materials = data['plastic_materials']
    
    # 根据应用场景筛选
    if 'application' in requirements:
        app = requirements['application']
        if app in data['material_selection_guide']['by_application']:
            candidate_ids = data['material_selection_guide']['by_application'][app]
            materials = [m for m in materials if m['id'] in candidate_ids]
    
    # 根据温度范围筛选
    if 'temperature_range' in requirements:
        temp = requirements['temperature_range']
        if temp in data['material_selection_guide']['by_temperature']:
            candidate_ids = data['material_selection_guide']['by_temperature'][temp]
            materials = [m for m in materials if m['id'] in candidate_ids]
    
    # 根据成本级别筛选
    if 'cost_level' in requirements:
        cost = requirements['cost_level']
        if cost in data['material_selection_guide']['by_cost']:
            candidate_ids = data['material_selection_guide']['by_cost'][cost]
            materials = [m for m in materials if m['id'] in candidate_ids]
    
    # 根据安全要求筛选
    if 'safety_requirement' in requirements:
        safety = requirements['safety_requirement']
        if safety in data['material_selection_guide']['by_safety']:
            candidate_ids = data['material_selection_guide']['by_safety'][safety]
            materials = [m for m in materials if m['id'] in candidate_ids]
    
    # 排序：按成本指数升序
    materials.sort(key=lambda x: x['cost_index'])
    
    return materials

def compare_plastic_materials(material_ids):
    """
    对比多个塑料材料的性能
    
    Args:
        material_ids: 材料ID列表
    
    Returns:
        对比结果字典
    """
    data = load_plastic_materials()
    materials = data['plastic_materials']
    
    selected = [m for m in materials if m['id'] in material_ids]
    
    if not selected:
        return None
    
    # 对比维度
    dimensions = ['density', 'temperature_resistance', 'safety_level', 'cost_index', 
                  'tensile_strength', 'impact_strength', 'hardness']
    
    comparison = {}
    for dim in dimensions:
        comparison[dim] = {}
        for mat in selected:
            if dim in mat:
                comparison[dim][mat['id']] = mat[dim]
    
    return {
        'materials': selected,
        'comparison': comparison
    }

def get_plastic_material_by_id(material_id):
    """
    根据ID获取塑料材料详情
    
    Args:
        material_id: 材料ID
    
    Returns:
        材料详情字典
    """
    data = load_plastic_materials()
    materials = data['plastic_materials']
    
    for mat in materials:
        if mat['id'] == material_id:
            return mat
    
    return None

def recommend_plastic_surface_treatment(material_id, requirements):
    """
    根据塑料材料推荐表面处理工艺
    
    Args:
        material_id: 塑料材料ID
        requirements: 需求字典，可包含：
            - effect: 效果要求（metallic, high_gloss, matte, 3d_relief, permanent_marking）
            - batch_size: 批量大小（small, medium, large）
            - cost_level: 成本级别（low, medium, high）
    
    Returns:
        推荐工艺列表
    """
    # 加载塑料表面处理数据库
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'plastic_surface_treatment.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        surface_data = json.load(f)
    
    # 获取适用工艺
    if material_id in surface_data['process_selection_matrix']['by_material']:
        candidate_ids = surface_data['process_selection_matrix']['by_material'][material_id]
    else:
        # 如果材料ID不在矩阵中，返回所有工艺
        candidate_ids = [p['id'] for p in surface_data['plastic_surface_treatments']]
    
    processes = [p for p in surface_data['plastic_surface_treatments'] if p['id'] in candidate_ids]
    
    # 根据效果筛选
    if 'effect' in requirements:
        effect = requirements['effect']
        if effect in surface_data['process_selection_matrix']['by_effect']:
            effect_ids = surface_data['process_selection_matrix']['by_effect'][effect]
            processes = [p for p in processes if p['id'] in effect_ids]
    
    # 根据批量筛选
    if 'batch_size' in requirements:
        batch = requirements['batch_size']
        if batch in surface_data['process_selection_matrix']['by_batch']:
            batch_ids = surface_data['process_selection_matrix']['by_batch'][batch]
            processes = [p for p in processes if p['id'] in batch_ids]
    
    # 根据成本筛选
    if 'cost_level' in requirements:
        cost = requirements['cost_level']
        if cost in surface_data['process_selection_matrix']['by_cost']:
            cost_ids = surface_data['process_selection_matrix']['by_cost'][cost]
            processes = [p for p in processes if p['id'] in cost_ids]
    
    # 排序：按成本指数升序
    processes.sort(key=lambda x: x['total_cost_index'])
    
    return processes

def main():
    """主函数：演示工具功能"""
    print("=== 塑料材料选择工具示例 ===")
    print()
    
    # 示例1：选择塑料盖材料
    print("示例1：选择塑料盖材料（应用：杯盖）")
    req1 = {'application': 'cup_lid', 'safety_requirement': 'bpa_free_required'}
    recommended1 = select_plastic_material(req1)
    for mat in recommended1[:3]:
        print(f"  - {mat['name']} (成本指数: {mat['cost_index']})")
    print()
    print("="*50)
    print()
    
    # 示例2：选择密封圈材料
    print("示例2：选择密封圈材料（应用：密封圈，耐高低温）")
    req2 = {'application': 'sealing_ring', 'temperature_range': 'high_temp'}
    recommended2 = select_plastic_material(req2)
    for mat in recommended2:
        print(f"  - {mat['name']} (耐温性: {mat['temperature_resistance']})")
    print()
    print("="*50)
    print()
    
    # 示例3：对比塑料材料
    print("示例3：对比塑料材料 (PP, TRITAN, 食品级硅胶)")
    comparison = compare_plastic_materials(['pp_food_grade', 'tritan', 'silicone_food_grade'])
    if comparison:
        print("对比维度:")
        for dim, values in comparison['comparison'].items():
            print(f"  {dim}:")
            for mat_id, value in values.items():
                mat = next((m for m in comparison['materials'] if m['id'] == mat_id), None)
                mat_name = mat['name'] if mat else mat_id
                print(f"    {mat_name}: {value}")
    print()
    print("="*50)
    print()
    
    # 示例4：推荐塑料表面处理工艺
    print("示例4：推荐塑料表面处理工艺（材料：ABS，效果：高光泽）")
    req4 = {'effect': 'high_gloss', 'cost_level': 'medium'}
    recommended4 = recommend_plastic_surface_treatment('abs_food_grade', req4)
    for p in recommended4[:3]:
        print(f"  - {p['name']} (成本指数: {p.get('total_cost_index', 'N/A')})")
    print()
    print("="*50)
    print()

if __name__ == '__main__':
    main()
