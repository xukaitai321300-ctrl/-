"""
测试Prompt生成工具 - Test Prompt Generator
"""

import unittest
import json
import os
from scripts.prompt_generator import PromptGenerator


class TestPromptGenerator(unittest.TestCase):
    """测试Prompt生成器"""
    
    def setUp(self):
        """测试前准备"""
        self.generator = PromptGenerator()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.generator)
        self.assertIsNotNone(self.generator.styles)
        self.assertIsNotNone(self.generator.templates)
        self.assertIsNotNone(self.generator.materials)
    
    def test_generate_styled_prompt(self):
        """测试生成风格化Prompt"""
        # 生成风格化Prompt
        result = self.generator.generate_styled_prompt(
            product="弹跳盖保温杯",
            style="现代简约",
            features=["轻量化", "防误触", "车载适配"],
            materials=["镁合金", "PP", "硅胶"]
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertIn("product", result)
        self.assertIn("style", result)
        self.assertIn("prompt", result)
        self.assertIn("prompt_variants", result)
        self.assertIn("recommendations", result)
        
        # 验证内容
        self.assertEqual(result["product"], "弹跳盖保温杯")
        self.assertEqual(result["style"], "现代简约")
        self.assertGreater(len(result["prompt"]), 0)
        self.assertGreater(len(result["prompt_variants"]), 0)
        self.assertGreater(len(result["recommendations"]), 0)
    
    def test_generate_prompt_report(self):
        """测试生成Prompt生成报告"""
        # 生成风格化Prompt
        result = self.generator.generate_styled_prompt(
            product="弹跳盖保温杯",
            style="现代简约",
            features=["轻量化"],
            materials=["镁合金"]
        )
        
        # 生成报告
        report = self.generator.generate_prompt_report(
            prompt_result=result,
            output_path=os.path.join(self.test_output_dir, "test_prompt_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("prompt", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_prompt_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
