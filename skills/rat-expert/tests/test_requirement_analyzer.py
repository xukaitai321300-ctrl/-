#!/usr/bin/env python3
"""
测试脚本：需求分析工具 (Test Script: Requirement Analyzer Tool)
测试 requirement_analyzer.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from requirement_analyzer import load_requirement_data, get_template, list_templates
except ImportError as e:
    print(f"❌ 无法导入 requirement_analyzer 模块：{e}")
    raise


class TestRequirementAnalyzer(unittest.TestCase):
    """测试需求分析工具"""
    
    def test_load_requirement_data(self):
        """测试加载需求分析数据库"""
        data = load_requirement_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('requirement_analysis_templates', data, "应该包含requirement_analysis_templates键")
    
    def test_get_template_valid(self):
        """测试获取有效的需求分析模板"""
        # 测试获取产品设计需求分析模板
        template = get_template('product_design')
        self.assertIsNotNone(template, "应该能找到产品设计需求分析模板")
        self.assertEqual(template.get('id'), 'product_design', "ID应该匹配")
        self.assertIn('name', template, "应该包含name字段")
        self.assertIn('fields', template, "应该包含fields字段")
    
    def test_get_template_invalid(self):
        """测试获取无效的需求分析模板"""
        template = get_template('invalid_id')
        self.assertIsNone(template, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()
