#!/usr/bin/env python3
"""
测试脚本：竞品分析工具 (Test Script: Competitive Analysis Tool)
测试 competitive_analyzer.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from competitive_analyzer import load_competitive_data, get_analysis_method, list_methods
except ImportError as e:
    print(f"❌ 无法导入 competitive_analyzer 模块：{e}")
    raise


class TestCompetitiveAnalyzer(unittest.TestCase):
    """测试竞品分析工具"""
    
    def test_load_competitive_data(self):
        """测试加载竞品分析数据库"""
        data = load_competitive_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('analysis_methods', data, "应该包含analysis_methods键")
    
    def test_get_analysis_method_valid(self):
        """测试获取有效的分析方法"""
        # 测试获取产品分析方法
        method = get_analysis_method('product_analysis')
        self.assertIsNotNone(method, "应该能找到产品分析方法")
        self.assertEqual(method.get('id'), 'product_analysis', "ID应该匹配")
        self.assertIn('name', method, "应该包含name字段")
        self.assertIn('steps', method, "应该包含steps字段")
    
    def test_get_analysis_method_invalid(self):
        """测试获取无效的分析方法"""
        method = get_analysis_method('invalid_id')
        self.assertIsNone(method, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()