#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注塑工艺工具
提供保温杯塑料零件的注塑工艺参数推荐、成本估算和质量分析功能
"""

import json
import os

def load_injection_molding_data():
    """加载注塑工艺数据库"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'injection_molding.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_injection_parameters(material_id):
    """
    获取材料的注塑工艺参数
    
    Args:
        material_id: 材料ID（pp_food_grade, tritan, abs_food_grade, pc_food_grade, silicone_food_grade）
    
    Returns:
        工艺参数字典
    """
    data = load_injection_molding_data()
    
    # 材料ID到工艺参数键的映射
    material_mapping = {
        'pp_food_grade': 'pp',
        'tritan': 'tritan',
        'abs_food_grade': 'abs',
        'pc_food_grade': 'pc',
        'silicone_food_grade': 'silicone'
    }
    
    if material_id not in material_mapping:
        return None
    
    process_key = material_mapping[material_id]
    
    if process_key not in data['injection_molding']['process_parameters']:
        return None
    
    return data['injection_molding']['process_parameters'][process_key]

def recommend_molding_machine(part_size, batch_size):
    """
    推荐注塑机规格
    
    Args:
        part_size: 零件尺寸（小型/中型/大型）
        batch_size: 批量大小（小/中/大）
    
    Returns:
        推荐注塑机规格
    """
    data = load_injection_molding_data()
    recommendations = data['injection_molding']['equipment']['recommended_machine']
    
    if part_size == 'small':
        return recommendations['small_part']
    elif part_size == 'medium':
        return recommendations['medium_part']
    elif part_size == 'large':
        return recommendations['large_part']
    else:
        return "请提供更多零件尺寸信息"

def estimate_injection_cost(material_id, quantity, part_weight):
    """
    估算注塑成本
    
    Args:
        material_id: 材料ID
        quantity: 生产数量
        part_weight: 零件重量（克）
    
    Returns:
        成本估算字典
    """
    data = load_injection_molding_data()
    
    # 获取材料成本
    material_mapping = {
        'pp_food_grade': 'pp',
        'tritan': 'tritan',
        'abs_food_grade': 'abs',
        'pc_food_grade': 'pc',
        'silicone_food_grade': 'silicone'
    }
    
    material_cost_per_kg = {
        'pp': 12.5,  # ¥10-15/kg，取中值
        'tritan': 50,   # ¥40-60/kg，取中值
        'abs': 20,       # ¥15-25/kg，取中值
        'pc': 32.5,      # ¥25-40/kg，取中值
        'silicone': 65    # ¥50-80/kg，取中值
    }
    
    if material_id not in material_mapping:
        return None
    
    mat_key = material_mapping[material_id]
    mat_cost_per_kg = material_cost_per_kg.get(mat_key, 0)
    
    # 计算材料成本
    total_material_weight = (part_weight / 1000) * quantity  # 转换为kg
    material_cost = total_material_weight * mat_cost_per_kg
    
    # 估算机器小时费率（根据机器吨位）
    machine_hour_rate = 150  # 中型机器，¥150/小时
    
    # 估算周期时间（根据工艺参数）
    process_params = get_injection_parameters(material_id)
    if process_params:
        cycle_time = float(process_params['cycle_time'].split('-')[0])  # 取最小值
    else:
        cycle_time = 30  # 默认30秒
    
    # 计算总周期时间（秒）
    total_cycle_time = (cycle_time * quantity) / 3600  # 转换为小时
    
    # 计算机器成本
    machine_cost = total_cycle_time * machine_hour_rate
    
    # 总成本
    total_cost = material_cost + machine_cost
    cost_per_part = total_cost / quantity if quantity > 0 else 0
    
    return {
        'material_cost': round(material_cost, 2),
        'machine_cost': round(machine_cost, 2),
        'total_cost': round(total_cost, 2),
        'cost_per_part': round(cost_per_part, 2),
        'cycle_time': cycle_time,
        'total_cycle_time_hours': round(total_cycle_time, 2)
    }

def analyze_mold_design(part_geometry):
    """
    分析模具设计要点
    
    Args:
        part_geometry: 零件几何特征字典，包含：
            - wall_thickness: 壁厚（mm）
            - parting_line: 分型面位置
            - undercuts: 倒扣数量
            - surface_finish: 表面光洁度要求
    
    Returns:
        模具设计建议
    """
    data = load_injection_molding_data()
    mold_design = data['injection_molding']['mold_design']
    
    suggestions = {
        'gate_type': '',
        'cooling_system': '',
        'venting': '',
        'shrinkage_control': ''
    }
    
    # 浇口类型建议
    if part_geometry.get('wall_thickness', 0) < 2:
        suggestions['gate_type'] = mold_design['gate_types']['pin_point_gate']
    elif part_geometry.get('wall_thickness', 0) > 4:
        suggestions['gate_type'] = mold_design['gate_types']['fan_gate']
    else:
        suggestions['gate_type'] = mold_design['gate_types']['submarine_gate']
    
    # 冷却系统建议
    suggestions['cooling_system'] = f"冷却通道直径 {mold_design['cooling_system']['channel_diameter']}，间距 {mold_design['cooling_system']['channel_spacing']}"
    
    # 排气系统建议
    suggestions['venting'] = f"排气槽深度 {mold_design['venting']['vent_depth']}，宽度 {mold_design['venting']['vent_width']}"
    
    # 收缩率控制
    shrinkage_map = {
        'pp_food_grade': '1.0-2.5%',
        'tritan': '0.5-0.7%',
        'abs_food_grade': '0.4-0.7%',
        'pc_food_grade': '0.5-0.7%',
        'silicone_food_grade': '2.0-3.5%'
    }
    
    material_id = part_geometry.get('material_id', '')
    suggestions['shrinkage_control'] = f"收缩率: {shrinkage_map.get(material_id, '未知')}，需预留修正余量"
    
    return suggestions

def troubleshoot_defect(defect_type):
    """
    注塑缺陷诊断与解决方案
    
    Args:
        defect_type: 缺陷类型（short_shot, flash, sink_mark, warpage, burn_mark）
    
    Returns:
        缺陷原因和解决方案
    """
    data = load_injection_molding_data()
    
    defect_mapping = {
        'short_shot': 'short_shot',
        'flash': 'flash',
        'sink_mark': 'sink_mark',
        'warpage': 'warpage',
        'burn_mark': 'burn_mark'
    }
    
    if defect_type not in defect_mapping:
        return None
    
    defect_key = defect_mapping[defect_type]
    
    if defect_key not in data['injection_molding']['quality_control']['common_defects']:
        return None
    
    defect_info = data['injection_molding']['quality_control']['common_defects'][defect_key]
    
    return {
        'defect_type': defect_type,
        'cause': defect_info['cause'],
        'solution': defect_info['solution']
    }

def main():
    """主函数：演示工具功能"""
    print("=== 注塑工艺工具示例 ===")
    print()
    
    # 示例1：获取PP材料的注塑工艺参数
    print("示例1：获取PP材料的注塑工艺参数")
    params1 = get_injection_parameters('pp_food_grade')
    if params1:
        print(f"  熔体温度: {params1['melt_temperature']}")
        print(f"  模具温度: {params1['mold_temperature']}")
        print(f"  注射压力: {params1['injection_pressure']}")
        print(f"  保压压力: {params1['holding_pressure']}")
        print(f"  冷却时间: {params1['cooling_time']}")
        print(f"  周期时间: {params1['cycle_time']}")
        print(f"  收缩率: {params1['shrinkage']}")
    print()
    print("="*50)
    print()
    
    # 示例2：推荐注塑机规格
    print("示例2：推荐注塑机规格（小型零件）")
    machine_rec = recommend_molding_machine('small', 1000)
    print(f"  推荐: {machine_rec}")
    print()
    print("="*50)
    print()
    
    # 示例3：估算注塑成本
    print("示例3：估算注塑成本（PP材料，1000个，重量20g）")
    cost_est = estimate_injection_cost('pp_food_grade', 1000, 20)
    if cost_est:
        print(f"  材料成本: ¥{cost_est['material_cost']:.2f}")
        print(f"  机器成本: ¥{cost_est['machine_cost']:.2f}")
        print(f"  总成本: ¥{cost_est['total_cost']:.2f}")
        print(f"  单件成本: ¥{cost_est['cost_per_part']:.2f}")
        print(f"  周期时间: {cost_est['cycle_time']}秒")
    print()
    print("="*50)
    print()
    
    # 示例4：模具设计建议
    print("示例4：模具设计建议（PP材料，壁厚2.5mm）")
    part_geo = {
        'material_id': 'pp_food_grade',
        'wall_thickness': 2.5,
        'parting_line': 'middle',
        'undercuts': 0,
        'surface_finish': 'high'
    }
    mold_suggestions = analyze_mold_design(part_geo)
    for key, value in mold_suggestions.items():
        print(f"  {key}: {value}")
    print()
    print("="*50)
    print()
    
    # 示例5：注塑缺陷诊断
    print("示例5：注塑缺陷诊断（短射）")
    defect_analysis = troubleshoot_defect('short_shot')
    if defect_analysis:
        print(f"  缺陷类型: {defect_analysis['defect_type']}")
        print(f"  原因: {defect_analysis['cause']}")
        print(f"  解决方案: {defect_analysis['solution']}")
    print()
    print("="*50)
    print()

if __name__ == '__main__':
    main()
