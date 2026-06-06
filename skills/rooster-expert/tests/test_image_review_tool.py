"""
测试图像评审工具 - Test Image Review Tool
"""

import unittest
import json
import os
from scripts.image_review_tool import ImageReviewTool


class TestImageReviewTool(unittest.TestCase):
    """测试图像评审工具"""
    
    def setUp(self):
        """测试前准备"""
        self.reviewer = ImageReviewTool()
        self.test_output_dir = "test_output"
        
        # 创建测试图片
        os.makedirs(self.test_output_dir, exist_ok=True)
        with open(os.path.join(self.test_output_dir, "test_image.png"), 'w') as f:
            f.write("This is a test image.")
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.reviewer)
        self.assertIsNotNone(self.reviewer.criteria)
        self.assertGreater(len(self.reviewer.criteria), 0)
    
    def test_review_image_quality(self):
        """测试评审图像质量"""
        # 评审图像质量
        result = self.reviewer.review_image_quality(
            image_path=os.path.join(self.test_output_dir, "test_image.png"),
            prompt="现代简约风格的弹跳盖保温杯",
            style="现代简约"
        )
        
        # 验证结果
        self.assertIsNotNone(result)
        self.assertEqual(result["image_path"], os.path.join(self.test_output_dir, "test_image.png"))
        self.assertEqual(result["prompt"], "现代简约风格的弹跳盖保温杯")
        self.assertEqual(result["style"], "现代简约")
        self.assertIn("scores", result)
        self.assertIn("details", result)
        self.assertIn("total_score", result)
        self.assertIn("is_passed", result)
        self.assertIn("recommendations", result)
        
        # 验证评分
        self.assertIn("图像质量", result["scores"])
        self.assertIn("风格一致性", result["scores"])
        self.assertIn("产品特征准确性", result["scores"])
        self.assertIn("提示词遵从度", result["scores"])
        self.assertIn("创新性", result["scores"])
        
        # 验证总分
        self.assertGreater(result["total_score"], 0)
        self.assertLessEqual(result["total_score"], 100)
    
    def test_generate_review_report(self):
        """测试生成评审报告"""
        # 评审图像质量
        review_result = self.reviewer.review_image_quality(
            image_path=os.path.join(self.test_output_dir, "test_image.png"),
            prompt="现代简约风格的弹跳盖保温杯",
            style="现代简约"
        )
        
        # 生成报告
        report = self.reviewer.generate_review_report(
            review_result=review_result,
            output_path=os.path.join(self.test_output_dir, "test_review_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("image_path", report)
        self.assertIn("total_score", report)
        self.assertIn("is_passed", report)
        self.assertIn("recommendations", report)
        self.assertIn("conclusion", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_review_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试输出
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
