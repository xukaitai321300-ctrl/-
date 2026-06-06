"""
测试效果生成工具 - Test Effect Generator
"""

import unittest
import json
import os
from scripts.effect_generator import EffectGenerator


class TestEffectGenerator(unittest.TestCase):
    """测试效果生成器"""
    
    def setUp(self):
        """测试前准备"""
        self.generator = EffectGenerator()
        self.test_output_dir = "test_output"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.generator)
        self.assertIsNotNone(self.generator.treatments)
        self.assertIsNotNone(self.generator.templates)
        self.assertIsNotNone(self.generator.materials)
    
    def test_generate_painting_effect(self):
        """测试生成喷漆效果"""
        # 生成喷漆效果
        result = self.generator.generate_painting_effect(
            color="红色",
            finish="高光",
            material="镁合金",
            output_path=os.path.join(self.test_output_dir, "test_painting_effect.png")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["treatment_type"], "喷漆")
        self.assertEqual(result["color"], "红色")
        self.assertEqual(result["finish"], "高光")
        self.assertEqual(result["material"], "镁合金")
        self.assertGreater(len(result["effect_description"]), 0)
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_spraying_effect(self):
        """测试生成喷塑效果"""
        # 生成喷塑效果
        result = self.generator.generate_spraying_effect(
            color="蓝色",
            texture="细纹",
            material="铝合金",
            output_path=os.path.join(self.test_output_dir, "test_spraying_effect.png")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["treatment_type"], "喷塑")
        self.assertEqual(result["color"], "蓝色")
        self.assertEqual(result["texture"], "细纹")
        self.assertEqual(result["material"], "铝合金")
        self.assertGreater(len(result["effect_description"]), 0)
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_heat_transfer_effect(self):
        """测试生成热转印效果"""
        # 生成热转印效果
        result = self.generator.generate_heat_transfer_effect(
            pattern="木纹",
            material="PP",
            output_path=os.path.join(self.test_output_dir, "test_heat_transfer_effect.png")
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["treatment_type"], "热转印")
        self.assertEqual(result["pattern"], "木纹")
        self.assertEqual(result["material"], "PP")
        self.assertGreater(len(result["effect_description"]), 0)
        
        # 验证文件是否存在
        if result.get("output_path"):
            self.assertTrue(os.path.exists(result["output_path"]))
    
    def test_generate_effect_report(self):
        """测试生成效果报告"""
        # 生成喷漆效果
        effect_result = self.generator.generate_painting_effect(
            color="红色",
            finish="高光",
            material="镁合金",
            output_path=os.path.join(self.test_output_dir, "test_painting_effect.png")
        )
        
        # 生成报告
        report = self.generator.generate_effect_report(
            effect_result=effect_result,
            output_path=os.path.join(self.test_output_dir, "test_effect_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("treatment_type", report)
        self.assertIn("parameters", report)
        self.assertIn("effect_description", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_effect_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试输出
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
