#!/usr/bin/env python3
"""
测试脚本：摄影灯光模拟工具 (Test Script: Lighting Simulator Tool)
测试 lighting_simulator.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from lighting_simulator import load_lighting_data, get_lighting_setup, list_setups
except ImportError as e:
    print(f"❌ 无法导入 lighting_simulator 模块：{e}")
    raise


class TestLightingSimulator(unittest.TestCase):
    """测试摄影灯光模拟工具"""
    
    def test_load_lighting_data(self):
        """测试加载灯光数据库"""
        data = load_lighting_data()
        self.assertIsInstance(data, list, "加载的数据应该是列表类型")
        self.assertGreater(len(data), 0, "应该至少包含一种灯光配置")
    
    def test_get_lighting_setup_valid(self):
        """测试获取有效的灯光配置"""
        # 测试获取三点布光配置
        setup = get_lighting_setup('three_point')
        self.assertIsNotNone(setup, "应该能找到三点布光配置")
        self.assertEqual(setup.get('id'), 'three_point', "ID应该匹配")
        self.assertIn('name', setup, "应该包含name字段")
        self.assertIn('lights', setup, "应该包含lights字段")
    
    def test_get_lighting_setup_invalid(self):
        """测试获取无效的灯光配置"""
        setup = get_lighting_setup('invalid_id')
        self.assertIsNone(setup, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()