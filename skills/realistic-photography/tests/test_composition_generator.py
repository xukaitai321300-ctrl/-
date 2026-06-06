#!/usr/bin/env python3
"""
测试脚本：构图模板生成工具 (Test Script: Composition Generator Tool)
测试 composition_generator.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from composition_generator import load_composition_data, get_composition_template, list_templates
except ImportError as e:
    print(f"❌ 无法导入 composition_generator 模块：{e}")
    raise


class TestCompositionGenerator(unittest.TestCase):
    """测试构图模板生成工具"""
    
    def test_load_composition_data(self):
        """测试加载构图模板数据库"""
        data = load_composition_data()
        self.assertIsInstance(data, list, "加载的数据应该是列表类型")
        self.assertGreater(len(data), 0, "应该至少包含一种构图模板")
    
    def test_get_composition_template_valid(self):
        """测试获取有效的构图模板"""
        # 测试获取主视角构图模板
        template = get_composition_template('front_view')
        self.assertIsNotNone(template, "应该能找到主视角构图模板")
        self.assertEqual(template.get('id'), 'front_view', "ID应该匹配")
        self.assertIn('name', template, "应该包含name字段")
        self.assertIn('composition_rules', template, "应该包含composition_rules字段")
    
    def test_get_composition_template_invalid(self):
        """测试获取无效的构图模板"""
        template = get_composition_template('invalid_id')
        self.assertIsNone(template, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()