#!/usr/bin/env python3
"""
测试保温杯工艺知识工具 (test_craftsmanship_tool.py)
测试 craftsmanship_tool.py 中的功能
版本: 1.0.0
创建时间: 2026-06-05
"""

import sys
import os
import json
import unittest

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from craftsmanship_tool import (
    load_knowledge_database,
    select_material,
    select_surface_treatment,
    calculate_craftsmanship_cost,
    evaluate_craftsmanship_quality,
    get_process_details,
    recommend_injection_molding_parameters,
    analyze_quality_issues
)

class TestCraftsmanshipTool(unittest.TestCase):
    """测试保温杯工艺知识工具"""
    
    def setUp(self):
        """测试前准备"""
        self.knowledge_db = load_knowledge_database()
        self.assertIsNotNone(self.knowledge_db, "知识数据库加载失败")
    
    def test_load_knowledge_database(self):
        """测试加载知识数据库"""
        db = load_knowledge_database()
        self.assertIsNotNone(db, "数据库不应为None")
        self.assertIn('craftsmanship_database', db, "数据库应包含craftsmanship_database键")
    
    def test_select_material(self):
        """测试选择材料功能"""
        # 测试选择金属材料（成本上限80，食品级安全）
        results = select_material('metals', {'cost_max': 80, 'safety_level': '食品级'})
        self.assertIsInstance(results, list, "结果应为列表")
        if results:
            self.assertIn('id', results[0], "结果应包含id键")
            self.assertIn('name', results[0], "结果应包含name键")
            self.assertIn('info', results[0], "结果应包含info键")
    
    def test_select_surface_treatment(self):
        """测试选择表面处理工艺功能"""
        # 测试选择金属表面处理（成本上限20，耐久性≥80）
        results = select_surface_treatment('metal_surface', {'cost_max': 20, 'durability_min': 80})
        self.assertIsInstance(results, list, "结果应为列表")
        if results:
            self.assertIn('id', results[0], "结果应包含id键")
            self.assertIn('name', results[0], "结果应包含name键")
    
    def test_calculate_craftsmanship_cost(self):
        """测试计算工艺成本功能"""
        # 测试计算工艺成本（材料：304，表面处理：激光打标，组装：超声波焊接，数量：1000个）
        cost = calculate_craftsmanship_cost('304', 'laser_marking', 'ultrasonic_welding', 1000)
        self.assertIsInstance(cost, dict, "成本应为字典")
        self.assertIn('material_cost', cost, "成本应包含material_cost键")
        self.assertIn('surface_treatment_cost', cost, "成本应包含surface_treatment_cost键")
        self.assertIn('assembly_cost', cost, "成本应包含assembly_cost键")
        self.assertIn('total_cost', cost, "成本应包含total_cost键")
        self.assertIn('quantity', cost, "成本应包含quantity键")
        self.assertIn('unit_cost', cost, "成本应包含unit_cost键")
    
    def test_evaluate_craftsmanship_quality(self):
        """测试评估工艺质量功能"""
        # 测试评估工艺质量（材料：304，表面处理：激光打标，组装：超声波焊接）
        quality = evaluate_craftsmanship_quality('304', 'laser_marking', 'ultrasonic_welding')
        self.assertIsInstance(quality, dict, "质量应为字典")
        self.assertIn('material_quality', quality, "质量应包含material_quality键")
        self.assertIn('surface_quality', quality, "质量应包含surface_quality键")
        self.assertIn('assembly_quality', quality, "质量应包含assembly_quality键")
        self.assertIn('overall_quality', quality, "质量应包含overall_quality键")
        self.assertIn('quality_level', quality, "质量应包含quality_level键")
    
    def test_get_process_details(self):
        """测试获取工艺详细信息功能"""
        # 测试获取材料详细信息
        material_detail = get_process_details('materials', '304')
        self.assertIsInstance(material_detail, dict, "材料详细信息应为字典")
        if material_detail:
            self.assertIn('name', material_detail, "材料详细信息应包含name键")
        
        # 测试获取表面处理详细信息
        surface_detail = get_process_details('surface_treatments', 'laser_marking')
        self.assertIsInstance(surface_detail, dict, "表面处理详细信息应为字典")
        
        # 测试获取注塑工艺详细信息
        injection_detail = get_process_details('injection_molding', 'PP')
        self.assertIsInstance(injection_detail, dict, "注塑工艺详细信息应为字典")
        
        # 测试获取组装工艺详细信息
        assembly_detail = get_process_details('assembly_process', 'ultrasonic_welding')
        self.assertIsInstance(assembly_detail, dict, "组装工艺详细信息应为字典")
    
    def test_recommend_injection_molding_parameters(self):
        """测试推荐注塑工艺参数功能"""
        # 测试推荐PP材料的注塑工艺参数
        params = recommend_injection_molding_parameters('PP', {'length': 100, 'width': 80, 'height': 30})
        self.assertIsInstance(params, dict, "注塑工艺参数应为字典")
        if params:
            self.assertIn('mold_temperature', params, "参数应包含mold_temperature键")
            self.assertIn('melt_temperature', params, "参数应包含melt_temperature键")
            self.assertIn('injection_pressure', params, "参数应包含injection_pressure键")
            self.assertIn('cycle_time', params, "参数应包含cycle_time键")
            self.assertIn('shrinkage_rate', params, "参数应包含shrinkage_rate键")
    
    def test_analyze_quality_issues(self):
        """测试分析质量问题功能"""
        # 测试分析注塑工艺质量问题
        quality_data = {'defect_rate': 5.0, 'strength': 75}
        suggestions = analyze_quality_issues('injection_molding', 'PP', quality_data)
        self.assertIsInstance(suggestions, list, "改进建议应为列表")
        
        # 测试分析表面处理工艺质量问题
        quality_data = {'adhesion': 70, 'durability': 70}
        suggestions = analyze_quality_issues('surface_treatment', 'spray_painting', quality_data)
        self.assertIsInstance(suggestions, list, "改进建议应为列表")

def main():
    """主函数 - 运行所有测试"""
    print("运行保温杯工艺知识工具测试...")
    print("=" * 50)
    
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCraftsmanshipTool)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 输出测试结果
    print("\n" + "=" * 50)
    print(f"测试完成！")
    print(f"运行测试数: {result.testsRun}")
    print(f"失败测试数: {len(result.failures)}")
    print(f"错误测试数: {len(result.errors)}")
    
    # 返回退出码
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(main())
