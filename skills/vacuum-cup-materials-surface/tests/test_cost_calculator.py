#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试成本计算工具
"""

import sys
import os

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from cost_calculator import calculate_material_cost, calculate_surface_treatment_cost, calculate_total_cost

def test_calculate_material_cost():
    """测试材料成本计算功能"""
    print("测试材料成本计算功能...")
    
    # 测试1：计算304不锈钢成本
    print("\n测试1：计算304不锈钢成本 (1000个)")
    result = calculate_material_cost('304_stainless_steel', 1000)
    assert 'error' not in result, f"不应该返回错误: {result.get('error', '')}"
    assert result['quantity'] == 1000, "数量应该正确"
    assert result['total_material_cost'] > 0, "总成本应该大于0"
    print(f"  材料: {result['material']}")
    print(f"  总成本: ¥{result['total_material_cost']:.2f}")
    print(f"  单杯成本: ¥{result['cost_per_cup']:.2f}")
    
    # 测试2：计算纯钛成本
    print("\n测试2：计算TA2纯钛成本 (500个)")
    result = calculate_material_cost('ta2_titanium', 500)
    assert 'error' not in result, f"不应该返回错误: {result.get('error', '')}"
    assert result['quantity'] == 500, "数量应该正确"
    print(f"  材料: {result['material']}")
    print(f"  总成本: ¥{result['total_material_cost']:.2f}")
    print(f"  单杯成本: ¥{result['cost_per_cup']:.2f}")
    
    # 测试3：不存在的材料
    print("\n测试3：不存在的材料")
    result = calculate_material_cost('non_existent', 100)
    assert 'error' in result, "应该返回错误"
    print(f"  正确返回错误: {result['error']}")
    
    print("材料成本计算功能测试通过！")
    return True

def test_calculate_total_cost():
    """测试总成本计算功能"""
    print("\n测试总成本计算功能...")
    
    # 测试1：计算总成本
    print("\n测试1：计算总成本 (304不锈钢 + 喷漆 + 激光打标, 1000个)")
    result = calculate_total_cost(
        material_id='304_stainless_steel',
        surface_process_id='spray_painting',
        logo_process_id='laser_marking',
        quantity=1000
    )
    assert 'error' not in result, f"不应该返回错误: {result.get('error', '')}"
    assert result['quantity'] == 1000, "数量应该正确"
    assert result['total_cost'] > 0, "总成本应该大于0"
    print(f"  数量: {result['quantity']}个")
    print(f"  材料成本: ¥{result['material']['total_material_cost']:.2f}")
    print(f"  表面处理成本: ¥{result['surface_treatment']['total_cost']:.2f}")
    print(f"  LOGO工艺成本: ¥{result['logo_process']['total_with_plate']:.2f}")
    print(f"  总成本: ¥{result['total_cost']:.2f}")
    print(f"  单杯成本: ¥{result['cost_per_cup']:.2f}")
    
    print("总成本计算功能测试通过！")
    return True

if __name__ == '__main__':
    print("=" * 50)
    print("开始测试成本计算工具")
    print("=" * 50)
    
    try:
        test_calculate_material_cost()
        test_calculate_total_cost()
        
        print("\n" + "=" * 50)
        print("所有测试通过！")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n测试出错: {e}")
        sys.exit(1)
