#!/usr/bin/env python3
"""
测试保温杯提示词生成工具 (test_prompt_generator.py)
测试 prompt_generator.py 中的功能
版本: 4.0.0
创建时间: 2026-06-05
"""

import sys
import os
import json
import unittest

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from prompt_generator import (
    load_prompt_templates,
    generate_prompt,
    generate_craftsmanship_integrated_prompt,
    optimize_prompt
)

class TestPromptGenerator(unittest.TestCase):
    """测试保温杯提示词生成工具"""
    
    def setUp(self):
        """测试前准备"""
        self.prompt_templates_db = load_prompt_templates()
        self.assertIsNotNone(self.prompt_templates_db, "提示词模板数据库加载失败")
    
    def test_load_prompt_templates(self):
        """测试加载提示词模板数据库"""
        db = load_prompt_templates()
        self.assertIsNotNone(db, "数据库不应为None")
        self.assertIn('prompt_templates', db, "数据库应包含prompt_templates键")
    
    def test_generate_prompt(self):
        """测试生成提示词功能"""
        # 测试生成儿童保温杯提示词
        prompt = generate_prompt('children_cup', '316_stainless_steel', 'matte_spray_painting')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
        if prompt:
            self.assertIn('positive_prompt', prompt, "提示词应包含positive_prompt键")
            self.assertIn('negative_prompt', prompt, "提示词应包含negative_prompt键")
            self.assertIn('photography_params', prompt, "提示词应包含photography_params键")
        
        # 测试生成弹跳盖保温杯提示词
        prompt = generate_prompt('bounce_lid_cup', 'TA2_pure_titanium', 'brushed_finish')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
        
        # 测试生成智能保温杯提示词
        prompt = generate_prompt('smart_cup', '316L_stainless_steel', 'LED_indicator_light')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
    
    def test_generate_craftsmanship_integrated_prompt(self):
        """测试生成融合工艺知识的提示词功能"""
        # 测试融合材料知识
        prompt = generate_craftsmanship_integrated_prompt('bounce_lid_cup', 'TA2_pure_titanium', 'brushed_finish', 'materials_knowledge')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
        if prompt:
            self.assertIn('positive_prompt', prompt, "提示词应包含positive_prompt键")
            # 检查是否包含工艺知识描述
            self.assertIn('craftsmanship_integration', prompt.get('positive_prompt', ''), "提示词应包含工艺知识描述")
        
        # 测试融合表面处理知识
        prompt = generate_craftsmanship_integrated_prompt('children_cup', '304_stainless_steel', 'matte_spray_painting', 'surface_treatment_effects')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
        
        # 测试融合注塑工艺知识
        prompt = generate_craftsmanship_integrated_prompt('children_cup', 'PP_plastic', 'matte_spray_painting', 'injection_molding_quality')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
    
    def test_optimize_prompt(self):
        """测试优化提示词功能"""
        # 先生成一个提示词
        prompt = generate_prompt('children_cup', '316_stainless_steel', 'matte_spray_painting')
        self.assertIsInstance(prompt, dict, "提示词应为字典")
        
        if prompt:
            # 测试优化真实感
            optimized_prompt = optimize_prompt(prompt, 'realism')
            self.assertIsInstance(optimized_prompt, dict, "优化后的提示词应为字典")
            self.assertIn('positive_prompt', optimized_prompt, "优化后的提示词应包含positive_prompt键")
            self.assertIn('photorealism', optimized_prompt.get('positive_prompt', ''), "优化后的提示词应包含真实感关键词")
            
            # 测试优化材质感
            optimized_prompt = optimize_prompt(prompt, 'material_texture')
            self.assertIsInstance(optimized_prompt, dict, "优化后的提示词应为字典")
            
            # 测试优化灯光
            optimized_prompt = optimize_prompt(prompt, 'lighting')
            self.assertIsInstance(optimized_prompt, dict, "优化后的提示词应为字典")
            
            # 测试优化构图
            optimized_prompt = optimize_prompt(prompt, 'composition')
            self.assertIsInstance(optimized_prompt, dict, "优化后的提示词应为字典")

def main():
    """主函数 - 运行所有测试"""
    print("运行保温杯提示词生成工具测试...")
    print("=" * 50)
    
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPromptGenerator)
    
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
