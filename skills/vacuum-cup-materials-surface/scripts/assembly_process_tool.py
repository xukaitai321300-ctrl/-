#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
组装工艺工具
提供保温杯组装工艺的选择、成本估算和质量分析功能
"""

import json
import os

def load_assembly_data():
    """加载组装工艺数据库"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'assembly_process.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_assembly_process(assembly_requirements):
    """
    根据需求选择组装工艺
    
    Args:
        assembly_requirements: 组装需求字典，可包含：
            - material_combination: 材料组合（plastic_plastic, plastic_metal, metal_metal）
            - strength_requirement: 强度要求（low, medium, high）
            - sealing_requirement: 密封要求（none, low, medium, high）
            - cost_level: 成本级别（low, medium, high）
            - production_volume: 生产批量（small, medium, large）
            - disassembly_need: 可拆卸需求（yes, no）
    
    Returns:
        推荐组装工艺列表
    """
    data = load_assembly_data()
    processes = data['assembly_processes']
    
    # 根据材料组合筛选
    if 'material_combination' in assembly_requirements:
        mc = assembly_requirements['material_combination']
        # 所有工艺都适用，但某些工艺更适合特定组合
        if mc == 'plastic_plastic':
            # 塑料-塑料：超声波焊接、卡扣装配优先
            processes = sorted(processes, key=lambda x: 0 if x['id'] in ['ultrasonic_welding', 'snap_fit'] else 1)
        elif mc == 'plastic_metal':
            # 塑料-金属：螺丝固定、胶水粘合优先
            processes = sorted(processes, key=lambda x: 0 if x['id'] in ['screw_fixation', 'adhesive_bonding'] else 1)
        elif mc == 'metal_metal':
            # 金属-金属：螺丝固定、卡扣装配优先
            processes = sorted(processes, key=lambda x: 0 if x['id'] in ['screw_fixation', 'snap_fit'] else 1)
    
    # 根据强度要求筛选
    if 'strength_requirement' in assembly_requirements:
        sr = assembly_requirements['strength_requirement']
        strength_map = {
            'low': ['snap_fit', 'adhesive_bonding'],
            'medium': ['screw_fixation', 'hot_plate_welding', 'sealing_ring_assembly'],
            'high': ['ultrasonic_welding', 'screw_fixation', 'spring_lid_assembly']
        }
        if sr in strength_map:
            candidate_ids = strength_map[sr]
            processes = [p for p in processes if p['id'] in candidate_ids] + \
                       [p for p in processes if p['id'] not in candidate_ids]
    
    # 根据密封要求筛选
    if 'sealing_requirement' in assembly_requirements:
        sr = assembly_requirements['sealing_requirement']
        if sr in ['medium', 'high']:
            # 需要密封：密封圈装配、超声波焊接、胶水粘合
            candidate_ids = ['sealing_ring_assembly', 'ultrasonic_welding', 'adhesive_bonding']
            processes = [p for p in processes if p['id'] in candidate_ids] + \
                       [p for p in processes if p['id'] not in candidate_ids]
    
    # 根据成本级别筛选
    if 'cost_level' in assembly_requirements:
        cl = assembly_requirements['cost_level']
        cost_map = {
            'low': ['snap_fit', 'screw_fixation', 'sealing_ring_assembly'],
            'medium': ['ultrasonic_welding', 'hot_plate_welding', 'adhesive_bonding'],
            'high': ['spring_lid_assembly']
        }
        if cl in cost_map:
            candidate_ids = cost_map[cl]
            processes = [p for p in processes if p['id'] in candidate_ids] + \
                       [p for p in processes if p['id'] not in candidate_ids]
    
    # 根据可拆卸需求筛选
    if 'disassembly_need' in assembly_requirements:
        dn = assembly_requirements['disassembly_need']
        if dn == 'yes':
            # 可拆卸：螺丝固定、卡扣装配、密封圈装配
            candidate_ids = ['screw_fixation', 'snap_fit', 'sealing_ring_assembly']
            processes = [p for p in processes if p['id'] in candidate_ids] + \
                       [p for p in processes if p['id'] not in candidate_ids]
        elif dn == 'no':
            # 不可拆卸：超声波焊接、热板焊接、胶水粘合
            candidate_ids = ['ultrasonic_welding', 'hot_plate_welding', 'adhesive_bonding']
            processes = [p for p in processes if p['id'] in candidate_ids] + \
                       [p for p in processes if p['id'] not in candidate_ids]
    
    # 排序：按成本指数升序
    processes.sort(key=lambda x: x['total_cost_index'])
    
    return processes

def estimate_assembly_cost(assembly_process_id, quantity, assembly_method='manual'):
    """
    估算组装成本
    
    Args:
        assembly_process_id: 组装工艺ID
        quantity: 生产数量
        assembly_method: 组装方法（manual, semi_auto, full_auto）
    
    Returns:
        成本估算字典
    """
    data = load_assembly_data()
    processes = data['assembly_processes']
    
    # 查找组装工艺
    process = next((p for p in processes if p['id'] == assembly_process_id), None)
    if not process:
        return None
    
    # 获取人工成本
    labor_cost_map = data['assembly_cost_estimation']['labor_cost']
    if assembly_method in labor_cost_map:
        labor_cost_range = labor_cost_map[assembly_method]
        # 解析成本范围
        cost_parts = labor_cost_range.replace('¥', '').replace('/杯', '').split('-')
        labor_cost_per_unit = (float(cost_parts[0]) + float(cost_parts[1])) / 2  # 取中值
    else:
        labor_cost_per_unit = 1.0  # 默认¥1.0/杯
    
    # 获取设备折旧
    equipment_cost_map = data['assembly_cost_estimation']['equipment_depreciation']
    equipment_cost_per_unit = 0.2  # 默认¥0.2/杯
    
    for key, value in equipment_cost_map.items():
        if key in process['name']:
            cost_parts = value.replace('¥', '').replace('/杯', '').split('-')
            equipment_cost_per_unit = (float(cost_parts[0]) + float(cost_parts[1])) / 2
            break
    
    # 计算总成本
    total_labor_cost = labor_cost_per_unit * quantity
    total_equipment_cost = equipment_cost_per_unit * quantity
    total_cost = total_labor_cost + total_equipment_cost
    cost_per_unit = total_cost / quantity if quantity > 0 else 0
    
    # 获取良品率
    yield_rate_map = data['assembly_cost_estimation']['yield_rate']
    if assembly_method in yield_rate_map:
        yield_rate_str = yield_rate_map[assembly_method]
        # 解析良品率范围
        rate_parts = yield_rate_str.replace('%', '').split('-')
        yield_rate = (float(rate_parts[0]) + float(rate_parts[1])) / 2 / 100  # 转换为小数
    else:
        yield_rate = 0.95  # 默认95%
    
    # 计算不良品成本
    defective_quantity = quantity * (1 - yield_rate)
    defective_cost = defective_quantity * cost_per_unit
    
    return {
        'process_name': process['name'],
        'assembly_method': assembly_method,
        'quantity': quantity,
        'labor_cost_per_unit': round(labor_cost_per_unit, 2),
        'equipment_cost_per_unit': round(equipment_cost_per_unit, 2),
        'total_labor_cost': round(total_labor_cost, 2),
        'total_equipment_cost': round(total_equipment_cost, 2),
        'total_cost': round(total_cost, 2),
        'cost_per_unit': round(cost_per_unit, 2),
        'yield_rate': yield_rate,
        'defective_quantity': round(defective_quantity, 1),
        'defective_cost': round(defective_cost, 2)
    }

def get_quality_control_checklist(assembly_process_id):
    """
    获取组装工艺的质量检验清单
    
    Args:
        assembly_process_id: 组装工艺ID
    
    Returns:
        质量检验清单字典
    """
    data = load_assembly_data()
    
    # 基础检验清单
    base_checklist = {
        'leak_test': data['assembly_quality_control']['leak_test'],
        'drop_test': data['assembly_quality_control']['drop_test'],
        'temperature_cycle_test': data['assembly_quality_control']['temperature_cycle_test']
    }
    
    # 根据组装工艺添加专项检验
    process_specific = {
        'ultrasonic_welding': {
            'welding_strength_test': '焊接强度测试（拉伸强度 ≥20 MPa）',
            'appearance_inspection': '外观检查（无溢料、无烧焦）'
        },
        'screw_fixation': {
            'torque_test': '扭矩测试（按规格要求）',
            'screw_tightness_check': '螺丝紧固度检查（100%全检）'
        },
        'snap_fit': {
            'snap_strength_test': '卡扣强度测试（插入力 20-80 N，拔出力 10-50 N）',
            'assembly_disassembly_test': '拆装测试（5次拆装无断裂）'
        },
        'sealing_ring_assembly': {
            'sealing_performance_test': '密封性能测试（0.3-0.5 MPa保压30秒，无气泡）',
            'durability_test': '耐久性测试（500-1000次开合，功能正常）'
        },
        'spring_lid_assembly': {
            'mechanical_performance_test': '机械性能测试（5000-10000次开合，功能正常）',
            'spring_fatigue_test': '弹簧疲劳测试（10000+次，无断裂）'
        }
    }
    
    if assembly_process_id in process_specific:
        base_checklist.update(process_specific[assembly_process_id])
    
    return base_checklist

def analyze_local_supply_chain():
    """
    分析本地供应链信息
    
    Returns:
        本地供应链信息字典
    """
    data = load_assembly_data()
    
    if 'local_supply_chain' in data and 'yongkang' in data['local_supply_chain']:
        return data['local_supply_chain']['yongkang']
    
    return None

def main():
    """主函数：演示工具功能"""
    print("=== 组装工艺工具示例 ===")
    print()
    
    # 示例1：选择组装工艺
    print("示例1：选择组装工艺（塑料-塑料，中等强度，需要密封）")
    req1 = {
        'material_combination': 'plastic_plastic',
        'strength_requirement': 'medium',
        'sealing_requirement': 'high',
        'cost_level': 'medium',
        'production_volume': 'medium',
        'disassembly_need': 'yes'
    }
    recommended1 = select_assembly_process(req1)
    for p in recommended1[:3]:
        print(f"  - {p['name']} (成本指数: {p.get('total_cost_index', 'N/A')})")
    print()
    print("="*50)
    print()
    
    # 示例2：估算组装成本
    print("示例2：估算组装成本（超声波焊接，1000个，手工组装）")
    cost_est = estimate_assembly_cost('ultrasonic_welding', 1000, 'manual')
    if cost_est:
        print(f"  工艺名称: {cost_est['process_name']}")
        print(f"  组装方法: {cost_est['assembly_method']}")
        print(f"  生产数量: {cost_est['quantity']}个")
        print(f"  人工成本: ¥{cost_est['total_labor_cost']:.2f} (¥{cost_est['labor_cost_per_unit']:.2f}/杯)")
        print(f"  设备成本: ¥{cost_est['total_equipment_cost']:.2f} (¥{cost_est['equipment_cost_per_unit']:.2f}/杯)")
        print(f"  总成本: ¥{cost_est['total_cost']:.2f}")
        print(f"  单杯成本: ¥{cost_est['cost_per_unit']:.2f}")
        print(f"  良品率: {cost_est['yield_rate']*100:.1f}%")
        print(f"  不良品数量: {cost_est['defective_quantity']}个")
        print(f"  不良品成本: ¥{cost_est['defective_cost']:.2f}")
    print()
    print("="*50)
    print()
    
    # 示例3：获取质量检验清单
    print("示例3：获取质量检验清单（超声波焊接）")
    checklist = get_quality_control_checklist('ultrasonic_welding')
    for key, value in checklist.items():
        print(f"  {key}: {value}")
    print()
    print("="*50)
    print()
    
    # 示例4：分析本地供应链
    print("示例4：分析本地供应链（永康）")
    supply_chain = analyze_local_supply_chain()
    if supply_chain:
        for key, value in supply_chain.items():
            print(f"  {key}: {value}")
    print()
    print("="*50)
    print()

if __name__ == '__main__':
    main()
