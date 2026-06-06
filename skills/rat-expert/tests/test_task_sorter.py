#!/usr/bin/env python3
"""
测试脚本：任务分拣工具 (Test Script: Task Sorter Tool)
测试 task_sorter.py 的功能
"""

import unittest
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# 导入要测试的模块
try:
    from task_sorter import load_requirement_data, get_task_sorting_rule, list_rules
except ImportError as e:
    print(f"❌ 无法导入 task_sorter 模块：{e}")
    raise


class TestTaskSorter(unittest.TestCase):
    """测试任务分拣工具"""
    
    def test_load_requirement_data(self):
        """测试加载需求分析数据库"""
        data = load_requirement_data()
        self.assertIsInstance(data, dict, "加载的数据应该是字典类型")
        self.assertIn('task_sorting_rules', data, "应该包含task_sorting_rules键")
    
    def test_get_task_sorting_rule_valid(self):
        """测试获取有效的任务分拣规则"""
        # 测试获取按优先级排序规则
        rule = get_task_sorting_rule('by_priority')
        self.assertIsNotNone(rule, "应该能找到按优先级排序规则")
        self.assertEqual(rule.get('id'), 'by_priority', "ID应该匹配")
        self.assertIn('name', rule, "应该包含name字段")
        self.assertIn('rule', rule, "应该包含rule字段")
    
    def test_get_task_sorting_rule_invalid(self):
        """测试获取无效的任务分拣规则"""
        rule = get_task_sorting_rule('invalid_id')
        self.assertIsNone(rule, "无效ID应该返回None")


if __name__ == '__main__':
    unittest.main()
