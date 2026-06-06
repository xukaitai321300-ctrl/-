#!/usr/bin/env python3
"""
测试脚本：工作流标准工具 (Test Script: Workflow Standard Tool)
测试 workflow_standard_tool.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from workflow_standard_tool import load_workflow_data, get_workflow_standard, list_workflows
except ImportError as e:
    print(f"❌ 无法导入 workflow_standard_tool 模块：{e}")
    raise


class TestWorkflowStandardTool(unittest.TestCase):
    """测试工作流标准工具"""
    
    def test_load_workflow_data(self):
        """测试加载工作流标准数据库"""
        data = load_workflow_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('workflow_standards', data, "应该包含workflow_standards键")
    
    def test_get_workflow_standard_valid(self):
        """测试获取有效的工作流标准"""
        # 测试获取文生图工作流标准
        workflow = get_workflow_standard('text_to_image')
        self.assertIsNotNone(workflow, "应该能找到文生图工作流标准")
        self.assertEqual(workflow.get('id'), 'text_to_image', "ID应该匹配")
        self.assertIn('name', workflow, "应该包含name字段")
        self.assertIn('standard_nodes', workflow, "应该包含standard_nodes字段")
    
    def test_get_workflow_standard_invalid(self):
        """测试获取无效的工作流标准"""
        workflow = get_workflow_standard('invalid_id')
        self.assertIsNone(workflow, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()
