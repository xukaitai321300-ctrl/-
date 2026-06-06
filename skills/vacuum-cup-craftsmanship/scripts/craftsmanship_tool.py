#!/usr/bin/env python3
"""
保温杯工艺知识工具 (vacuum-cup-craftsmanship)
提供工艺选择、成本计算、质量评估功能
版本: 1.0.0
创建时间: 2026-06-05
"""

import json
import os
from typing import Dict, List, Optional, Tuple

# 加载工艺知识数据库
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
KNOWLEDGE_FILE = os.path.join(DATA_DIR, 'craftsmanship_knowledge.json')

def load_knowledge_database() -> Dict:
    """加载工艺知识数据库"""
    try:
        with open(KNOWLEDGE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：找不到文件 {KNOWLEDGE_FILE}")
        return {}
    except json.JSONDecodeError:
        print(f"错误：解析JSON文件失败 {KNOWLEDGE_FILE}")
        return {}

# 全局数据库
_KNOWLEDGE_DB = load_knowledge_database()

def select_material(material_type: str, requirements: Dict) -> List[Dict]:
    """
    选择合适的材料
    Args:
        material_type: 材料类型（'metals' 或 'plastics'）
        requirements: 需求字典（如 {'cost_max': 80, 'safety_level': '食品级'}）
    Returns:
        推荐材料列表
    """
    if not _KNOWLEDGE_DB:
        return []
    
    materials = _KNOWLEDGE_DB.get('craftsmanship_database', {}).get('materials', {}).get(material_type, {})
    if not materials:
        return []
    
    results = []
    for mid, minfo in materials.items():
        # 检查需求匹配
        match = True
        for key, value in requirements.items():
            if key == 'cost_max' and minfo.get('cost_index', 0) > value:
                match = False
                break
            elif key == 'safety_level' and minfo.get('safety_level') != value:
                match = False
                break
            elif key == 'temperature_resistance_min' and minfo.get('temperature_resistance', 0) < value:
                match = False
                break
        
        if match:
            results.append({'id': mid, 'name': minfo.get('name'), 'info': minfo})
    
    return results

def select_surface_treatment(material_type: str, requirements: Dict) -> List[Dict]:
    """
    选择合适的表面处理工艺
    Args:
        material_type: 材料类型（'metal_surface' 或 'plastic_surface'）
        requirements: 需求字典（如 {'cost_max': 20, 'durability_min': 80}）
    Returns:
        推荐表面处理工艺列表
    """
    if not _KNOWLEDGE_DB:
        return []
    
    surface_treatments = _KNOWLEDGE_DB.get('craftsmanship_database', {}).get('surface_treatments', {}).get(material_type, {})
    if not surface_treatments:
        return []
    
    results = []
    for sid, sinfo in surface_treatments.items():
        # 检查需求匹配
        match = True
        for key, value in requirements.items():
            if key == 'cost_max' and sinfo.get('cost', 0) > value:
                match = False
                break
            elif key == 'durability_min' and sinfo.get('durability', 0) < value:
                match = False
                break
        
        if match:
            results.append({'id': sid, 'name': sinfo.get('name'), 'info': sinfo})
    
    return results

def calculate_craftsmanship_cost(material_id: str, surface_treatment_id: str, assembly_method: str, quantity: int = 1000) -> Dict:
    """
    计算工艺总成本
    Args:
        material_id: 材料ID（如 '304', 'PP'）
        surface_treatment_id: 表面处理工艺ID（如 'spray_painting'）
        assembly_method: 组装方法（如 'ultrasonic_welding'）
        quantity: 生产数量
    Returns:
        成本明细字典
    """
    if not _KNOWLEDGE_DB:
        return {}
    
    db = _KNOWLEDGE_DB.get('craftsmanship_database', {})
    
    # 获取材料成本指数
    material_cost_index = 0
    materials = db.get('materials', {})
    for mtype, mdict in materials.items():
        if material_id in mdict:
            material_cost_index = mdict[material_id].get('cost_index', 0)
            break
    
    # 获取表面处理成本
    surface_cost = 0
    surface_treatments = db.get('surface_treatments', {})
    for stype, sdict in surface_treatments.items():
        if surface_treatment_id in sdict:
            surface_cost = sdict[surface_treatment_id].get('cost', 0)
            break
    
    # 获取组装成本
    assembly_cost = 0
    assembly_process = db.get('assembly_process', {})
    if assembly_method in assembly_process:
        assembly_cost = assembly_process[assembly_method].get('cost', 0)
    
    # 计算总成本（简化公式：成本指数 × 数量 × 0.01 + 表面处理成本 × 数量 + 组装成本 × 数量）
    total_material_cost = material_cost_index * quantity * 0.01
    total_surface_cost = surface_cost * quantity * 0.01
    total_assembly_cost = assembly_cost * quantity * 0.01
    
    total_cost = total_material_cost + total_surface_cost + total_assembly_cost
    
    return {
        'material_cost': round(total_material_cost, 2),
        'surface_treatment_cost': round(total_surface_cost, 2),
        'assembly_cost': round(total_assembly_cost, 2),
        'total_cost': round(total_cost, 2),
        'quantity': quantity,
        'unit_cost': round(total_cost / quantity, 4) if quantity > 0 else 0
    }

def evaluate_craftsmanship_quality(material_id: str, surface_treatment_id: str, assembly_method: str) -> Dict:
    """
    评估工艺质量
    Args:
        material_id: 材料ID
        surface_treatment_id: 表面处理工艺ID
        assembly_method: 组装方法
    Returns:
        质量评估字典
    """
    if not _KNOWLEDGE_DB:
        return {}
    
    db = _KNOWLEDGE_DB.get('craftsmanship_database', {})
    quality_scores = {}
    
    # 评估材料质量（耐腐蚀性 + 安全级别）
    material_score = 0
    materials = db.get('materials', {})
    for mtype, mdict in materials.items():
        if material_id in mdict:
            minfo = mdict[material_id]
            corrosion = minfo.get('corrosion_resistance', 0)
            safety = minfo.get('safety_level', '')
            # 安全级别评分：食品级=80，医疗级=100
            safety_score = 100 if safety == '医疗级' else (80 if safety == '食品级' else 60)
            material_score = (corrosion + safety_score) / 2
            break
    
    # 评估表面处理质量（耐久性）
    surface_score = 0
    surface_treatments = db.get('surface_treatments', {})
    for stype, sdict in surface_treatments.items():
        if surface_treatment_id in sdict:
            surface_score = sdict[surface_treatment_id].get('durability', 0)
            break
    
    # 评估组装质量（强度 + 效率）
    assembly_score = 0
    assembly_process = db.get('assembly_process', {})
    if assembly_method in assembly_process:
        ainfo = assembly_process[assembly_method]
        strength = ainfo.get('strength', 0)
        efficiency = ainfo.get('efficiency', 0)
        assembly_score = (strength + efficiency) / 2
    
    # 综合质量评分
    overall_quality = (material_score + surface_score + assembly_score) / 3
    
    return {
        'material_quality': round(material_score, 2),
        'surface_quality': round(surface_score, 2),
        'assembly_quality': round(assembly_score, 2),
        'overall_quality': round(overall_quality, 2),
        'quality_level': '优秀' if overall_quality >= 85 else ('良好' if overall_quality >= 70 else ('一般' if overall_quality >= 60 else '较差'))
    }

def get_process_details(process_type: str, process_id: str) -> Dict:
    """
    获取工艺详细信息
    Args:
        process_type: 工艺类型（'materials', 'surface_treatments', 'injection_molding', 'assembly_process'）
        process_id: 工艺ID
    Returns:
        工艺详细信息字典
    """
    if not _KNOWLEDGE_DB:
        return {}
    
    db = _KNOWLEDGE_DB.get('craftsmanship_database', {})
    
    # 根据材料类型查找
    if process_type == 'materials':
        for mtype, mdict in db.get('materials', {}).items():
            if process_id in mdict:
                return mdict[process_id]
    elif process_type == 'surface_treatments':
        for stype, sdict in db.get('surface_treatments', {}).items():
            if process_id in sdict:
                return sdict[process_id]
    elif process_type == 'injection_molding':
        if process_id in db.get('injection_molding', {}):
            return db['injection_molding'][process_id]
    elif process_type == 'assembly_process':
        if process_id in db.get('assembly_process', {}):
            return db['assembly_process'][process_id]
    
    return {}

def recommend_injection_molding_parameters(material: str, product_dimensions: Dict) -> Dict:
    """
    推荐注塑工艺参数
    Args:
        material: 材料（'PP', 'TRITAN', 'ABS', 'PC', 'silicone'）
        product_dimensions: 产品尺寸字典（如 {'length': 100, 'width': 80, 'height': 30}）
    Returns:
        推荐注塑工艺参数字典
    """
    if not _KNOWLEDGE_DB:
        return {}
    
    injection_db = _KNOWLEDGE_DB.get('craftsmanship_database', {}).get('injection_molding', {})
    if material not in injection_db:
        return {}
    
    params = injection_db[material].copy()
    
    # 根据产品尺寸调整周期时间（简化逻辑）
    if product_dimensions:
        volume = product_dimensions.get('length', 0) * product_dimensions.get('width', 0) * product_dimensions.get('height', 0)
        if volume > 100000:  # 大尺寸产品
            params['cycle_time'] = '40-60秒'
        elif volume < 1000:  # 小尺寸产品
            params['cycle_time'] = '15-30秒'
    
    return params

def analyze_quality_issues(process_type: str, process_id: str, quality_data: Dict) -> List[str]:
    """
    分析质量问题并提供改进建议
    Args:
        process_type: 工艺类型
        process_id: 工艺ID
        quality_data: 质量数据字典（如 {'defect_rate': 5.0, 'strength': 75}）
    Returns:
        改进建议列表
    """
    suggestions = []
    
    if process_type == 'injection_molding':
        # 注塑工艺质量问题分析
        defect_rate = quality_data.get('defect_rate', 0)
        if defect_rate > 3.0:
            suggestions.append('缺陷率过高，建议调整注塑温度或压力')
        
        strength = quality_data.get('strength', 0)
        if strength < 70:
            suggestions.append('强度不足，建议调整保压压力或冷却时间')
    
    elif process_type == 'surface_treatment':
        # 表面处理工艺质量问题分析
        adhesion = quality_data.get('adhesion', 0)
        if adhesion < 80:
            suggestions.append('附着力不足，建议优化表面预处理或涂料配方')
        
        durability = quality_data.get('durability', 0)
        if durability < 75:
            suggestions.append('耐久性不足，建议增加涂层厚度或改进固化工艺')
    
    return suggestions if suggestions else ['质量状况良好，无需改进']

def main():
    """主函数 - 演示工具使用"""
    print("保温杯工艺知识工具演示")
    print("=" * 50)
    
    # 1. 选择材料
    print("\n1. 选择材料（成本上限80，食品级安全）")
    materials = select_material('metals', {'cost_max': 80, 'safety_level': '食品级'})
    for m in materials[:3]:  # 只显示前3个
        print(f"   - {m['name']} (ID: {m['id']})")
    
    # 2. 选择表面处理工艺
    print("\n2. 选择表面处理工艺（成本上限20，耐久性≥80）")
    surface_treatments = select_surface_treatment('metal_surface', {'cost_max': 20, 'durability_min': 80})
    for st in surface_treatments[:3]:
        print(f"   - {st['name']} (ID: {st['id']})")
    
    # 3. 计算工艺成本
    print("\n3. 计算工艺成本（材料：304，表面处理：激光打标，组装：超声波焊接，数量：1000个）")
    cost = calculate_craftsmanship_cost('304', 'laser_marking', 'ultrasonic_welding', 1000)
    print(f"   材料成本: ¥{cost['material_cost']}")
    print(f"   表面处理成本: ¥{cost['surface_treatment_cost']}")
    print(f"   组装成本: ¥{cost['assembly_cost']}")
    print(f"   总成本: ¥{cost['total_cost']}")
    print(f"   单位成本: ¥{cost['unit_cost']}/个")
    
    # 4. 评估工艺质量
    print("\n4. 评估工艺质量（材料：304，表面处理：激光打标，组装：超声波焊接）")
    quality = evaluate_craftsmanship_quality('304', 'laser_marking', 'ultrasonic_welding')
    print(f"   材料质量: {quality['material_quality']}/100")
    print(f"   表面处理质量: {quality['surface_quality']}/100")
    print(f"   组装质量: {quality['assembly_quality']}/100")
    print(f"   综合质量: {quality['overall_quality']}/100 ({quality['quality_level']})")
    
    print("\n" + "=" * 50)
    print("演示完成！")

if __name__ == '__main__':
    main()
