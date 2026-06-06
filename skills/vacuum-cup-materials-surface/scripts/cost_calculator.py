#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
成本计算工具 - 计算保温杯材料和表面处理的总成本
"""

import json
import os

def load_data():
    """加载所有数据"""
    base_path = os.path.join(os.path.dirname(__file__), '../data')
    
    with open(os.path.join(base_path, 'materials.json'), 'r', encoding='utf-8') as f:
        materials_data = json.load(f)
    
    with open(os.path.join(base_path, 'surface_treatment.json'), 'r', encoding='utf-8') as f:
        surface_data = json.load(f)
    
    with open(os.path.join(base_path, 'logo_process.json'), 'r', encoding='utf-8') as f:
        logo_data = json.load(f)
    
    return materials_data, surface_data, logo_data

def calculate_material_cost(material_id, quantity):
    """
    计算材料成本
    
    参数:
        material_id: str, 材料ID
        quantity: int, 数量（个）
    
    返回:
        dict: 成本明细
    """
    materials_data, _, _ = load_data()
    
    # 找到材料
    material = None
    for m in materials_data['materials']:
        if m['id'] == material_id:
            material = m
            break
    
    if not material:
        return {'error': f'未找到材料: {material_id}'}
    
    # 计算材料成本（估算）
    # 假设500ml保温杯需要200g材料
    weight_per_cup = 0.2  # kg
    total_weight = weight_per_cup * quantity
    
    # 根据材料类型估算价格
    price_per_kg = {
        '304_stainless_steel': 20,  # 元/kg
        '316_stainless_steel': 30,
        'ta1_titanium': 200,
        'ta2_titanium': 150
    }
    
    unit_price = price_per_kg.get(material_id, 50)
    total_cost = total_weight * unit_price
    
    return {
        'material': material['name'],
        'quantity': quantity,
        'weight_per_cup_kg': weight_per_cup,
        'total_weight_kg': total_weight,
        'unit_price_yuan_per_kg': unit_price,
        'total_material_cost': total_cost,
        'cost_per_cup': total_cost / quantity if quantity > 0 else 0
    }

def calculate_surface_treatment_cost(process_id, quantity):
    """
    计算表面处理成本
    
    参数:
        process_id: str, 工艺ID
        quantity: int, 数量（个）
    
    返回:
        dict: 成本明细
    """
    _, surface_data, _ = load_data()
    
    # 找到工艺
    process = None
    for p in surface_data['surface_treatments']:
        if p['id'] == process_id:
            process = p
            break
    
    if not process:
        return {'error': f'未找到表面处理工艺: {process_id}'}
    
    # 解析成本范围
    cost_str = process.get('material_cost', '¥0/杯')
    # 简单解析，实际应该更复杂
    if '¥' in cost_str and '/' in cost_str:
        cost_range = cost_str.replace('¥', '').replace('/杯', '')
        if '-' in cost_range:
            low, high = map(float, cost_range.split('-'))
            avg_cost = (low + high) / 2
        else:
            avg_cost = float(cost_range)
    else:
        avg_cost = 1.0  # 默认值
    
    total_cost = avg_cost * quantity
    
    # 制版成本（如果有）
    plate_cost = 0
    if 'plate_cost' in process:
        plate_str = str(process['plate_cost'])
        if '¥' in plate_str:
            plate_cost = float(plate_str.replace('¥', '').replace(',', ''))
    
    total_with_plate = total_cost + plate_cost
    
    return {
        'process': process['name'],
        'quantity': quantity,
        'material_cost_per_cup': avg_cost,
        'total_material_cost': total_cost,
        'plate_cost': plate_cost,
        'total_cost': total_with_plate,
        'cost_per_cup': total_with_plate / quantity if quantity > 0 else 0
    }

def calculate_total_cost(material_id, surface_process_id, logo_process_id, quantity):
    """
    计算总成本（材料 + 表面处理 + LOGO工艺）
    
    参数:
        material_id: str, 材料ID
        surface_process_id: str, 表面处理工艺ID
        logo_process_id: str, LOGO工艺ID
        quantity: int, 数量（个）
    
    返回:
        dict: 总成本明细
    """
    # 计算材料成本
    material_cost = calculate_material_cost(material_id, quantity)
    
    # 计算表面处理成本
    surface_cost = calculate_surface_treatment_cost(surface_process_id, quantity)
    
    # 计算LOGO工艺成本
    _, _, logo_data = load_data()
    logo_process = None
    for p in logo_data['logo_processes']:
        if p['id'] == logo_process_id:
            logo_process = p
            break
    
    if logo_process:
        logo_cost_str = logo_process.get('cost_per_cup', '¥0/杯')
        if '¥' in logo_cost_str and '/' in logo_cost_str:
            logo_cost_range = logo_cost_str.replace('¥', '').replace('/杯', '')
            if '-' in logo_cost_range:
                low, high = map(float, logo_cost_range.split('-'))
                logo_avg_cost = (low + high) / 2
            else:
                logo_avg_cost = float(logo_cost_range)
        else:
            logo_avg_cost = 0.5  # 默认值
        
        logo_total = logo_avg_cost * quantity
        
        # 制版成本
        logo_plate_cost = 0
        if 'plate_cost' in logo_process and isinstance(logo_process['plate_cost'], (int, float)):
            logo_plate_cost = logo_process['plate_cost']
        
        logo_total_with_plate = logo_total + logo_plate_cost
    else:
        logo_avg_cost = 0
        logo_total = 0
        logo_plate_cost = 0
        logo_total_with_plate = 0
    
    # 计算总成本
    if 'error' not in material_cost and 'error' not in surface_cost:
        total = (material_cost['total_material_cost'] + 
                 surface_cost['total_cost'] + 
                 logo_total_with_plate)
        
        cost_per_cup = total / quantity if quantity > 0 else 0
        
        return {
            'quantity': quantity,
            'material': material_cost,
            'surface_treatment': surface_cost,
            'logo_process': {
                'process': logo_process['name'] if logo_process else '无',
                'cost_per_cup': logo_avg_cost,
                'total_cost': logo_total,
                'plate_cost': logo_plate_cost,
                'total_with_plate': logo_total_with_plate
            },
            'total_cost': total,
            'cost_per_cup': cost_per_cup
        }
    else:
        return {'error': '计算失败，请检查输入参数'}

if __name__ == '__main__':
    # 示例用法
    print("=== 成本计算工具示例 ===\n")
    
    # 示例：计算304不锈钢 + 喷漆 + 激光打标的成本
    result = calculate_total_cost(
        material_id='304_stainless_steel',
        surface_process_id='spray_painting',
        logo_process_id='laser_marking',
        quantity=1000
    )
    
    if 'error' in result:
        print(f"错误: {result['error']}")
    else:
        print(f"数量: {result['quantity']}个")
        print(f"\n材料成本:")
        print(f"  材料: {result['material']['material']}")
        print(f"  总成本: ¥{result['material']['total_material_cost']:.2f}")
        print(f"  单杯成本: ¥{result['material']['cost_per_cup']:.2f}")
        
        print(f"\n表面处理成本:")
        print(f"  工艺: {result['surface_treatment']['process']}")
        print(f"  总成本: ¥{result['surface_treatment']['total_cost']:.2f}")
        print(f"  单杯成本: ¥{result['surface_treatment']['cost_per_cup']:.2f}")
        
        print(f"\nLOGO工艺成本:")
        print(f"  工艺: {result['logo_process']['process']}")
        print(f"  总成本: ¥{result['logo_process']['total_with_plate']:.2f}")
        print(f"  单杯成本: ¥{result['logo_process']['cost_per_cup']:.2f}")
        
        print(f"\n=== 总成本 ===")
        print(f"总成本: ¥{result['total_cost']:.2f}")
        print(f"单杯成本: ¥{result['cost_per_cup']:.2f}")
