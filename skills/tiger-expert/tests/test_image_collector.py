#!/usr/bin/env python3
"""
测试脚本：图像采集工具 (Test Script: Image Collector Tool)
测试 image_collector.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from image_collector import load_image_data, get_image_source, list_sources
except ImportError as e:
    print(f"❌ 无法导入 image_collector 模块：{e}")
    raise


class TestImageCollector(unittest.TestCase):
    """测试图像采集工具"""
    
    def test_load_image_data(self):
        """测试加载图像采集数据库"""
        data = load_image_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('image_sources', data, "应该包含image_sources键")
    
    def test_get_image_source_valid(self):
        """测试获取有效的图像来源"""
        # 测试获取天猫图像来源
        source = get_image_source('tmall')
        self.assertIsNotNone(source, "应该能找到天猫图像来源")
        self.assertEqual(source.get('id'), 'tmall', "ID应该匹配")
        self.assertIn('name', source, "应该包含name字段")
        self.assertIn('collection_methods', source, "应该包含collection_methods字段")
    
    def test_get_image_source_invalid(self):
        """测试获取无效的图像来源"""
        source = get_image_source('invalid_id')
        self.assertIsNone(source, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()