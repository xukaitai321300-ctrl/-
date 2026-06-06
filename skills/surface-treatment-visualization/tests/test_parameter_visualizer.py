"""
测试参数可视化工具 - Test Parameter Visualizer
"""

import unittest
import json
import os
from scripts.parameter_visualizer import ParameterVisualizer


class TestParameterVisualizer(unittest.TestCase):
    """测试参数可视化器"""
    
    def setUp(self):
        """测试前准备"""
        self.visualizer = ParameterVisualizer()
        self.test_output_dir = "test_output"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.visualizer)
        self.assertIsNotNone(self.visualizer.parameters)
        self.assertGreater(len(self.visualizer.parameters), 0)
    
    def test_visualize_parameter_effect(self):
        """测试可视化工艺参数对效果的影响"""
        # 可视化工艺参数对效果的影响
        result = self.visualizer.visualize_parameter_effect(
            treatment_type="喷漆",
            parameter_name="温度",
            output_path=os.path.join(self.test_output_dir, "test_parameter_effect.png")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["treatment_type"], "喷漆")
        self.assertEqual(result["parameter_name"], "温度")
        self.assertIn("parameter_unit", result)
        self.assertIn("typical_range", result)
        self.assertIn("optimal_value", result)
        self.assertIn("effect_on_quality", result)
        self.assertIn("effect_on_efficiency", result)
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_parameter_optimization_suggestion(self):
        """测试生成参数优化建议"""
        # 生成参数优化建议
        suggestion = self.visualizer.generate_parameter_optimization_suggestion(
            treatment_type="喷漆",
            parameter_name="温度"
        )
        
        # 验证结果
        self.assertIsNotNone(suggestion)
        self.assertEqual(suggestion["treatment_type"], "喷漆")
        self.assertEqual(suggestion["parameter_name"], "温度")
        self.assertIn("optimal_value", suggestion)
        self.assertIn("typical_range", suggestion)
        self.assertIn("control_method", suggestion)
        self.assertIn("optimization_suggestions", suggestion)
        self.assertGreater(len(suggestion["optimization_suggestions"]), 0)
    
    def test_generate_parameter_visualization_report(self):
        """测试生成参数可视化报告"""
        # 可视化工艺参数对效果的影响
        visualization_result = self.visualizer.visualize_parameter_effect(
            treatment_type="喷漆",
            parameter_name="温度",
            output_path=os.path.join(self.test_output_dir, "test_parameter_effect.png")
        )
        
        # 生成报告
        report = self.visualizer.generate_parameter_visualization_report(
            visualization_result=visualization_result,
            output_path=os.path.join(self.test_output_dir, "test_parameter_visualization_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("treatment_type", report)
        self.assertIn("parameter_name", report)
        self.assertIn("optimal_value", report)
        self.assertIn("optimization_suggestions", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_parameter_visualization_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试输出
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
