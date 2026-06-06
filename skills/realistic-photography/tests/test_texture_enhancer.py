#!/usr/bin/env python3
"""
测试脚本：材质纹理增强工具 (Test Script: Texture Enhancer Tool)
测试 texture_enhancer.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from texture_enhancer import load_material_data, get_material, list_materials
except ImportError as e:
    print(f"❌ 无法导入 texture_enhancer 模块：{e}")
    raise


class TestTextureEnhancer(unittest.TestCase):
    """测试材质纹理增强工具"""
    
    def test_load_material_data(self):
        """测试加载材质数据库"""
        data = load_material_data()
        self.assertIsInstance(data, list, "加载的数据应该是列表类型")
        self.assertGreater(len(data), 0, "应该至少包含一种材质")
    
    def test_get_material_valid(self):
        """测试获取有效的材质"""
        # 测试获取不锈钢304材质
        material = get_material('stainless_steel_304')
        self.assertIsNotNone(material, "应该能找到不锈钢304材质")
        self.assertEqual(material.get('id'), 'stainless_steel_304', "ID应该匹配")
        self.assertIn('name', material, "应该包含name字段")
        self.assertIn('texture_properties', material, "应该包含texture_properties字段")
    
    def test_get_material_invalid(self):
        """测试获取无效的材质"""
        material = get_material('invalid_id')
        self.assertIsNone(material, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()