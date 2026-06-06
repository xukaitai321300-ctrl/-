#!/usr/bin/env python3
"""
测试脚本：图像分析工具 (Test Script: Image Analysis Tool)
测试 image_analysis_tool.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from image_analysis_tool import load_image_data, get_analysis_method, list_methods
except ImportError as e:
    print(f"❌ 无法导入 image_analysis_tool 模块：{e}")
    raise


class TestImageAnalysisTool(unittest.TestCase):
    """测试图像分析工具"""
    
    def test_load_image_data(self):
        """测试加载图像分析数据库"""
        data = load_image_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('analysis_methods', data, "应该包含analysis_methods键")
    
    def test_get_analysis_method_valid(self):
        """测试获取有效的图像分析方法"""
        # 测试获取质量分析方法
        method = get_analysis_method('quality_analysis')
        self.assertIsNotNone(method, "应该能找到质量分析方法")
        self.assertEqual(method.get('id'), 'quality_analysis', "ID应该匹配")
        self.assertIn('name', method, "应该包含name字段")
        self.assertIn('steps', method, "应该包含steps字段")
    
    def test_get_analysis_method_invalid(self):
        """测试获取无效的图像分析方法"""
        method = get_analysis_method('invalid_id')
        self.assertIsNone(method, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()
