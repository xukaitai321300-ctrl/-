"""
测试效果分析工具 - Test Effect Analyzer
"""

import unittest
import json
import os
from scripts.effect_analyzer import EffectAnalyzer


class TestEffectAnalyzer(unittest.TestCase):
    """测试效果分析器"""
    
    def setUp(self):
        """测试前准备"""
        self.analyzer = EffectAnalyzer()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.analyzer)
        self.assertIsNotNone(self.analyzer.styles)
        self.assertIsNotNone(self.analyzer.mappings)
    
    def test_analyze_prompt_style_consistency(self):
        """测试分析Prompt与风格的一致性"""
        # 准备测试数据
        prompt = "现代简约风格的弹跳盖保温杯，采用镁合金杯身和PP内胆，具有轻量化、防误触、车载适配等功能，简洁实用的设计风格"
        
        # 分析一致性
        result = self.analyzer.analyze_prompt_style_consistency(prompt, "现代简约")
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertIn("prompt", result)
        self.assertIn("style", result)
        self.assertIn("consistency_score", result)
        self.assertIn("consistency_level", result)
        self.assertIn("recommendations", result)
        
        # 验证内容
        self.assertEqual(result["style"], "现代简约")
        self.assertGreater(result["consistency_score"], 0)
        self.assertIn(result["consistency_level"], ["高", "中", "低"])
        self.assertGreater(len(result["recommendations"]), 0)
    
    def test_analyze_generation_effect(self):
        """测试分析生图效果"""
        # 准备测试数据
        prompt = "现代简约风格的弹跳盖保温杯"
        
        # 分析生图效果
        result = self.analyzer.analyze_generation_effect(prompt, "generated_image.jpg")
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertIn("prompt", result)
        self.assertIn("image_path", result)
        self.assertIn("effect_analysis", result)
        self.assertIn("prompt_optimization_suggestions", result)
        self.assertIn("style_adjustment_suggestions", result)
        
        # 验证内容
        self.assertEqual(result["prompt"], prompt)
        self.assertEqual(result["image_path"], "generated_image.jpg")
        self.assertIn("clarity", result["effect_analysis"])
        self.assertIn("style_consistency", result["effect_analysis"])
        self.assertIn("detail_richness", result["effect_analysis"])
        self.assertIn("overall_quality", result["effect_analysis"])
    
    def test_generate_analysis_report(self):
        """测试生成效果分析报告"""
        # 分析Prompt与风格的一致性
        prompt = "现代简约风格的弹跳盖保温杯"
        analysis_result = self.analyzer.analyze_prompt_style_consistency(prompt, "现代简约")
        
        # 生成报告
        report = self.analyzer.generate_analysis_report(
            analysis_result=analysis_result,
            output_path=os.path.join(self.test_output_dir, "test_analysis_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("analysis_result", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_analysis_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
