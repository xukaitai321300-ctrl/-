#!/usr/bin/env python3
"""
测试脚本：高清细节处理工具 (Test Script: Detail Processor Tool)
测试 detail_processor.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from detail_processor import load_detail_data, get_detail_processing, list_details
except ImportError as e:
    print(f"❌ 无法导入 detail_processor 模块：{e}")
    raise


class TestDetailProcessor(unittest.TestCase):
    """测试高清细节处理工具"""
    
    def test_load_detail_data(self):
        """测试加载高清细节处理数据库"""
        data = load_detail_data()
        self.assertIsInstance(data, list, "加载的数据应该是列表类型")
        self.assertGreater(len(data), 0, "应该至少包含一种细节处理")
    
    def test_get_detail_processing_valid(self):
        """测试获取有效的细节处理"""
        # 测试获取材质表面细节处理
        detail = get_detail_processing('material_surface_detail')
        self.assertIsNotNone(detail, "应该能找到材质表面细节处理")
        self.assertEqual(detail.get('id'), 'material_surface_detail', "ID应该匹配")
        self.assertIn('name', detail, "应该包含name字段")
        self.assertIn('processing_techniques', detail, "应该包含processing_techniques字段")
    
    def test_get_detail_processing_invalid(self):
        """测试获取无效的细节处理"""
        detail = get_detail_processing('invalid_id')
        self.assertIsNone(detail, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()