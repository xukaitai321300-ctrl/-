#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工艺知识查询工具
提供保温杯工艺知识的全面查询功能
"""

import json
import os
import sys

def load_knowledge_data():
    """加载工艺知识数据库"""
    # 尝试从当前技能包加载
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    
    knowledge_data = {
        'materials': [],
        'surface_treatments': [],
        'injection_molding': {},
        'assembly_processes': []
    }
    
    # 加载材料知识
    materials_file = os.path.join(data_dir, 'materials_knowledge.json')
    if os.path.exists(materials_file):
        with open(materials_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            knowledge_data['materials'] = data.get('materials', [])
    else:
        # 如果文件不存在，尝试从 vacuum-cup-materials-surface 技能包加载
        alt_file = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'materials.json')
        if os.path.exists(alt_file):
            with open(alt_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['materials'] = data.get('materials', [])
        
        alt_file2 = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'materials_plastic.json')
        if os.path.exists(alt_file2):
            with open(alt_file2, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['materials'].extend(data.get('plastic_materials', []))
    
    # 加载表面处理知识
    surface_file = os.path.join(data_dir, 'surface_treatment_knowledge.json')
    if os.path.exists(surface_file):
        with open(surface_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            knowledge_data['surface_treatments'] = data.get('surface_treatments', [])
    else:
        # 如果文件不存在，尝试从 vacuum-cup-materials-surface 技能包加载
        alt_file = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'surface_treatment.json')
        if os.path.exists(alt_file):
            with open(alt_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['surface_treatments'] = data.get('surface_treatments', [])
        
        alt_file2 = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'plastic_surface_treatment.json')
        if os.path.exists(alt_file2):
            with open(alt_file2, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['surface_treatments'].extend(data.get('plastic_surface_treatments', []))
    
    # 加载注塑工艺知识
    injection_file = os.path.join(data_dir, 'injection_molding_knowledge.json')
    if os.path.exists(injection_file):
        with open(injection_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            knowledge_data['injection_molding'] = data.get('injection_molding', {})
    else:
        # 如果文件不存在，尝试从 vacuum-cup-materials-surface 技能包加载
        alt_file = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'injection_molding.json')
        if os.path.exists(alt_file):
            with open(alt_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['injection_molding'] = data.get('injection_molding', {})
    
    # 加载组装工艺知识
    assembly_file = os.path.join(data_dir, 'assembly_process_knowledge.json')
    if os.path.exists(assembly_file):
        with open(assembly_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            knowledge_data['assembly_processes'] = data.get('assembly_processes', [])
    else:
        # 如果文件不存在，尝试从 vacuum-cup-materials-surface 技能包加载
        alt_file = os.path.join(os.path.dirname(__file__), '..', '..', 'vacuum-cup-materials-surface', 'data', 'assembly_process.json')
        if os.path.exists(alt_file):
            with open(alt_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                knowledge_data['assembly_processes'] = data.get('assembly_processes', [])
    
    return knowledge_data

def query_material(material_id):
    """
    查询材料知识
    
    Args:
        material_id: 材料ID
    
    Returns:
        材料详情字典
    """
    knowledge_data = load_knowledge_data()
    materials = knowledge_data['materials']
    
    for mat in materials:
        if mat.get('id') == material_id:
            return mat
    
    return None

def query_surface_treatment(process_id):
    """
    查询表面处理知识
    
    Args:
        process_id: 工艺ID
    
    Returns:
        工艺详情字典
    """
    knowledge_data = load_knowledge_data()
    processes = knowledge_data['surface_treatments']
    
    for proc in processes:
        if proc.get('id') == process_id:
            return proc
    
    return None

def query_injection_parameters(material_type):
    """
    查询注塑工艺参数
    
    Args:
        material_type: 材料类型（pp, tritan, abs, pc, silicone）
    
    Returns:
        工艺参数字典
    """
    knowledge_data = load_knowledge_data()
    injection_data = knowledge_data['injection_molding']
    
    if not injection_data:
        return None
    
    process_params = injection_data.get('process_parameters', {})
    
    if material_type in process_params:
        return process_params[material_type]
    
    return None

def query_assembly_process(process_id):
    """
    查询组装工艺知识
    
    Args:
        process_id: 工艺ID
    
    Returns:
        工艺详情字典
    """
    knowledge_data = load_knowledge_data()
    processes = knowledge_data['assembly_processes']
    
    for proc in processes:
        if proc.get('id') == process_id:
            return proc
    
    return None

def list_all_materials():
    """列出所有材料"""
    knowledge_data = load_knowledge_data()
    return knowledge_data['materials']

def list_all_surface_treatments():
    """列出所有表面处理工艺"""
    knowledge_data = load_knowledge_data()
    return knowledge_data['surface_treatments']

def list_all_assembly_processes():
    """列出所有组装工艺"""
    knowledge_data = load_knowledge_data()
    return knowledge_data['assembly_processes']

def main():
    """主函数：演示工具功能"""
    print("=== 工艺知识查询工具示例 ===")
    print()
    
    # 示例1：查询材料知识
    print("示例1：查询材料知识（304不锈钢）")
    mat = query_material('304_stainless_steel')
    if mat:
        print(f"  材料ID: {mat.get('id', 'N/A')}")
        print(f"  名称: {mat.get('name', 'N/A')}")
        print(f"  类型: {mat.get('type', 'N/A')}")
        print(f"  密度: {mat.get('density', 'N/A')} {mat.get('density_unit', '')}")
        print(f"  耐腐蚀性: {mat.get('corrosion_resistance', 'N/A')}")
        print(f"  安全级别: {mat.get('safety_level', 'N/A')}")
        print(f"  成本指数: {mat.get('cost_index', 'N/A')}")
    print()
    print("="*50)
    print()
    
    # 示例2：查询表面处理知识
    print("示例2：查询表面处理知识（喷漆）")
    proc = query_surface_treatment('spray_painting')
    if proc:
        print(f"  工艺ID: {proc.get('id', 'N/A')}")
        print(f"  名称: {proc.get('name', 'N/A')}")
        print(f"  类别: {proc.get('category', 'N/A')}")
        print(f"  涂层厚度: {proc.get('coating_thickness', 'N/A')}")
        print(f"  固化温度: {proc.get('curing_temperature', 'N/A')}")
        print(f"  成本指数: {proc.get('total_cost_index', 'N/A')}")
    print()
    print("="*50)
    print()
    
    # 示例3：查询注塑工艺知识
    print("示例3：查询注塑工艺知识（PP材料）")
    params = query_injection_parameters('pp')
    if params:
        print(f"  材料: PP")
        print(f"  熔体温度: {params.get('melt_temperature', 'N/A')}")
        print(f"  模具温度: {params.get('mold_temperature', 'N/A')}")
        print(f"  注射压力: {params.get('injection_pressure', 'N/A')}")
        print(f"  保压压力: {params.get('holding_pressure', 'N/A')}")
        print(f"  冷却时间: {params.get('cooling_time', 'N/A')}")
        print(f"  周期时间: {params.get('cycle_time', 'N/A')}")
        print(f"  收缩率: {params.get('shrinkage', 'N/A')}")
    print()
    print("="*50)
    print()
    
    # 示例4：查询组装工艺知识
    print("示例4：查询组装工艺知识（超声波焊接）")
    asm = query_assembly_process('ultrasonic_welding')
    if asm:
        print(f"  工艺ID: {asm.get('id', 'N/A')}")
        print(f"  名称: {asm.get('name', 'N/A')}")
        print(f"  适用材料: {', '.join(asm.get('applicable_materials', []))}")
        print(f"  焊接强度: {asm.get('welding_strength', 'N/A')}")
        print(f"  成本指数: {asm.get('total_cost_index', 'N/A')}")
    print()
    print("="*50)
    print()
    
    # 示例5：列出所有材料
    print("示例5：列出所有材料（前5个）")
    all_materials = list_all_materials()
    for i, mat in enumerate(all_materials[:5]):
        print(f"  {i+1}. {mat.get('name', 'N/A')} (ID: {mat.get('id', 'N/A')})")
    print()
    print("="*50)
    print()

if __name__ == '__main__':
    main()
