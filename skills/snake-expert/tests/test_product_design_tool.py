#!/usr/bin/env python3
"""
测试脚本：产品设计工具 (Test Script: Product Design Tool)
测试 product_design_tool.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from product_design_tool import load_design_data, get_design_stage, list_stages
except ImportError as e:
    print(f"❌ 无法导入 product_design_tool 模块：{e}")
    raise


class TestProductDesignTool(unittest.TestCase):
    """测试产品设计工具"""
    
    def test_load_design_data(self):
        """测试加载产品设计数据库"""
        data = load_design_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('design_process', data, "应该包含design_process键")
    
    def test_get_design_stage_valid(self):
        """测试获取有效的设计阶段"""
        # 测试获取概念设计阶段
        stage = get_design_stage('concept_design')
        self.assertIsNotNone(stage, "应该能找到概念设计阶段")
        self.assertEqual(stage.get('id'), 'concept_design', "ID应该匹配")
        self.assertIn('name', stage, "应该包含name字段")
        self.assertIn('steps', stage, "应该包含steps字段")
    
    def test_get_design_stage_invalid(self):
        """测试获取无效的设计阶段"""
        stage = get_design_stage('invalid_id')
        self.assertIsNone(stage, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()