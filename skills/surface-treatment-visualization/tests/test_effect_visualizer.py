"""
测试效果展示工具 - Test Effect Visualizer
"""

import unittest
import json
import os
from scripts.effect_visualizer import EffectVisualizer


class TestEffectVisualizer(unittest.TestCase):
    """测试效果展示器"""
    
    def setUp(self):
        """测试前准备"""
        self.visualizer = EffectVisualizer(output_dir="test_output")
        self.test_output_dir = "test_output"
        
        # 创建测试图片
        os.makedirs(self.test_output_dir, exist_ok=True)
        with open(os.path.join(self.test_output_dir, "test_effect.png"), 'w') as f:
            f.write("This is a test effect image.")
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.visualizer)
        self.assertEqual(self.visualizer.output_dir, "test_output")
    
    def test_visualize_effect(self):
        """测试展示表面处理效果"""
        # 展示效果
        result = self.visualizer.visualize_effect(
            effect_image_path=os.path.join(self.test_output_dir, "test_effect.png"),
            output_path=os.path.join(self.test_output_dir, "test_effect_visualization.html")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["visualization_type"], "static")
        self.assertIsNotNone(result["view_url"])
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(result["view_url"]))
    
    def test_visualize_effects_comparison(self):
        """测试展示多个表面处理效果对比"""
        # 创建测试图片
        with open(os.path.join(self.test_output_dir, "test_effect2.png"), 'w') as f:
            f.write("This is another test effect image.")
        
        # 展示效果对比
        result = self.visualizer.visualize_effects_comparison(
            effect_images=[
                os.path.join(self.test_output_dir, "test_effect.png"),
                os.path.join(self.test_output_dir, "test_effect2.png")
            ],
            output_path=os.path.join(self.test_output_dir, "test_effects_comparison.html")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["visualization_type"], "comparison")
        self.assertIsNotNone(result["view_url"])
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(result["view_url"]))
    
    def test_generate_visualization_report(self):
        """测试生成可视化报告"""
        # 展示效果
        visualization_result = self.visualizer.visualize_effect(
            effect_image_path=os.path.join(self.test_output_dir, "test_effect.png"),
            output_path=os.path.join(self.test_output_dir, "test_effect_visualization.html")
        )
        
        # 生成报告
        report = self.visualizer.generate_visualization_report(
            visualization_result=visualization_result,
            output_path=os.path.join(self.test_output_dir, "test_visualization_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("visualization_type", report)
        self.assertIn("view_url", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_visualization_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试输出
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
