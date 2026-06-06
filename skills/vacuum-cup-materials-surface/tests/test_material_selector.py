#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试材料选择工具
"""

import sys
import os

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from material_selector import select_material, compare_materials, get_material_by_id

def test_select_material():
    """测试材料选择功能"""
    print("测试材料选择功能...")
    
    # 测试1：轻量化需求
    print("\n测试1：轻量化需求")
    req1 = {
        'weight_sensitive': True,
        'safety_level': 'medical_grade',
        'cost_sensitive': False
    }
    recommended1 = select_material(req1)
    assert len(recommended1) > 0, "应该返回推荐材料"
    print(f"  推荐材料数量: {len(recommended1)}")
    for mat in recommended1[:3]:
        print(f"    - {mat['name']} (成本指数: {mat['cost_index']})")
    
    # 测试2：成本敏感
    print("\n测试2：成本敏感需求")
    req2 = {
        'weight_sensitive': False,
        'safety_level': 'food_grade',
        'cost_sensitive': True,
        'local_supply_preferred': True
    }
    recommended2 = select_material(req2)
    assert len(recommended2) > 0, "应该返回推荐材料"
    print(f"  推荐材料数量: {len(recommended2)}")
    for mat in recommended2[:3]:
        print(f"    - {mat['name']} (成本指数: {mat['cost_index']}, 本地供应: {mat.get('local_supply', False)})")
    
    # 测试3：材料对比
    print("\n测试3：材料对比")
    comparison = compare_materials(['304_stainless_steel', 'ta2_titanium'])
    assert 'comparison_table' in comparison, "应该返回对比表"
    print(f"  对比维度数量: {len(comparison['comparison_table'])}")
    
    print("材料选择功能测试通过！")
    return True

def test_get_material_by_id():
    """测试根据ID获取材料功能"""
    print("\n测试根据ID获取材料功能...")
    
    # 测试1：存在的材料
    print("\n测试1：存在的材料")
    material = get_material_by_id('304_stainless_steel')
    assert material is not None, "应该找到材料"
    assert material['name'] == '304不锈钢', "材料名称应该正确"
    print(f"  材料名称: {material['name']}")
    print(f"  材料密度: {material['density']} {material['density_unit']}")
    
    # 测试2：不存在的材料
    print("\n测试2：不存在的材料")
    material = get_material_by_id('non_existent')
    assert material is None, "应该返回None"
    print("  正确返回None")
    
    print("根据ID获取材料功能测试通过！")
    return True

if __name__ == '__main__':
    print("=" * 50)
    print("开始测试材料选择工具")
    print("=" * 50)
    
    try:
        test_select_material()
        test_get_material_by_id()
        
        print("\n" + "=" * 50)
        print("所有测试通过！")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n测试出错: {e}")
        sys.exit(1)
