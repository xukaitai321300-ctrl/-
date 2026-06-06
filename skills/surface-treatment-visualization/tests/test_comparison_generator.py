"""
测试对比生成工具 - Test Comparison Generator
"""

import unittest
import json
import os
from scripts.comparison_generator import ComparisonGenerator


class TestComparisonGenerator(unittest.TestCase):
    """测试对比生成器"""
    
    def setUp(self):
        """测试前准备"""
        self.generator = ComparisonGenerator(output_dir="test_output")
        self.test_output_dir = "test_output"
        
        # 创建测试图片
        os.makedirs(self.test_output_dir, exist_ok=True)
        with open(os.path.join(self.test_output_dir, "test_before.jpg"), 'w') as f:
            f.write("This is a test before image.")
        with open(os.path.join(self.test_output_dir, "test_after.png"), 'w') as f:
            f.write("This is a test after image.")
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.output_dir, "test_output")
    
    def test_generate_before_after_comparison(self):
        """测试生成表面处理前后对比"""
        # 生成前后对比
        result = self.generator.generate_before_after_comparison(
            before_image=os.path.join(self.test_output_dir, "test_before.jpg"),
            after_effect="喷塑",
            after_params={"color": "蓝色", "texture": "细纹"},
            output_path=os.path.join(self.test_output_dir, "test_comparison.png")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["before_image"], os.path.join(self.test_output_dir, "test_before.jpg"))
        self.assertEqual(result["after_effect"], "喷塑")
        self.assertEqual(result["after_params"]["color"], "蓝色")
        self.assertEqual(result["comparison_type"], "side_by_side")
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_slider_comparison(self):
        """测试生成滑块对比"""
        # 生成滑块对比
        result = self.generator.generate_slider_comparison(
            before_image=os.path.join(self.test_output_dir, "test_before.jpg"),
            after_image=os.path.join(self.test_output_dir, "test_after.png"),
            output_path=os.path.join(self.test_output_dir, "test_slider_comparison.html")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["before_image"], os.path.join(self.test_output_dir, "test_before.jpg"))
        self.assertEqual(result["after_image"], os.path.join(self.test_output_dir, "test_after.png"))
        self.assertEqual(result["comparison_type"], "slider")
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_comparison_report(self):
        """测试生成对比报告"""
        # 生成前后对比
        comparison_result = self.generator.generate_before_after_comparison(
            before_image=os.path.join(self.test_output_dir, "test_before.jpg"),
            after_effect="喷塑",
            after_params={"color": "蓝色", "texture": "细纹"},
            output_path=os.path.join(self.test_output_dir, "test_comparison.png")
        )
        
        # 生成报告
        report = self.generator.generate_comparison_report(
            comparison_result=comparison_result,
            output_path=os.path.join(self.test_output_dir, "test_comparison_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("before_image", report)
        self.assertIn("after_effect", report)
        self.assertIn("comparison_type", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_comparison_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试输出
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
