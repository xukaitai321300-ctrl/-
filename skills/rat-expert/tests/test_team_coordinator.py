#!/usr/bin/env python3
"""
测试脚本：团队协调工具 (Test Script: Team Coordinator Tool)
测试 team_coordinator.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from team_coordinator import load_requirement_data, get_workflow, list_workflows
except ImportError as e:
    print(f"❌ 无法导入 team_coordinator 模块：{e}")
    raise


class TestTeamCoordinator(unittest.TestCase):
    """测试团队协调工具"""
    
    def test_load_requirement_data(self):
        """测试加载需求分析数据库"""
        data = load_requirement_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('team_coordination_workflows', data, "应该包含team_coordination_workflows键")
    
    def test_get_workflow_valid(self):
        """测试获取有效的团队协调流程"""
        # 测试获取设计到生产协调流程
        workflow = get_workflow('design_to_production')
        self.assertIsNotNone(workflow, "应该能找到设计到生产协调流程")
        self.assertEqual(workflow.get('id'), 'design_to_production', "ID应该匹配")
        self.assertIn('name', workflow, "应该包含name字段")
        self.assertIn('steps', workflow, "应该包含steps字段")
    
    def test_get_workflow_invalid(self):
        """测试获取无效的团队协调流程"""
        workflow = get_workflow('invalid_id')
        self.assertIsNone(workflow, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()
