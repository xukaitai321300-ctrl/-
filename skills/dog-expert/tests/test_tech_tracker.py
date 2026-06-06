"""
测试技术追踪工具 - Test Tech Tracker
"""

import unittest
import json
import os
from scripts.tech_tracker import TechTracker


class TestTechTracker(unittest.TestCase):
    """测试技术追踪器"""
    
    def setUp(self):
        """测试前准备"""
        self.tracker = TechTracker()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.tracker)
        self.assertIsNotNone(self.tracker.trends)
    
    def test_track_tech_trends(self):
        """测试追踪技术趋势"""
        # 追踪技术趋势
        tech_trends = self.tracker.track_tech_trends(
            categories=["AI技术", "材料技术"]
        )
        
        # 验证结果
        self.assertIsNotNone(tech_trends)
        self.assertIn("report_id", tech_trends)
        self.assertIn("title", tech_trends)
        self.assertIn("categories", tech_trends)
        self.assertIn("trends", tech_trends)
        self.assertIn("analysis", tech_trends)
        self.assertIn("recommendations", tech_trends)
        
        # 验证内容
        self.assertEqual(len(tech_trends["categories"]), 2)
        self.assertGreater(len(tech_trends["trends"]), 0)
        self.assertGreater(len(tech_trends["recommendations"]), 0)
    
    def test_track_specific_technology(self):
        """测试追踪特定技术"""
        # 追踪特定技术
        tech_report = self.tracker.track_specific_technology("大模型")
        
        # 验证结果
        self.assertIsNotNone(tech_report)
        self.assertIn("report_id", tech_report)
        self.assertIn("title", tech_report)
        self.assertIn("technology", tech_report)
        self.assertIn("developments", tech_report)
        self.assertIn("key_players", tech_report)
        self.assertIn("future_directions", tech_report)
        self.assertIn("recommendations", tech_report)
        
        # 验证内容
        self.assertEqual(tech_report["technology"], "大模型")
        self.assertGreater(len(tech_report["developments"]), 0)
        self.assertGreater(len(tech_report["key_players"]), 0)
        self.assertGreater(len(tech_report["future_directions"]), 0)
        self.assertGreater(len(tech_report["recommendations"]), 0)
    
    def test_save_report(self):
        """测试保存报告"""
        # 追踪技术趋势
        tech_trends = self.tracker.track_tech_trends(
            categories=["AI技术"]
        )
        
        # 保存报告
        output_path = os.path.join(self.test_output_dir, "test_tech_trends_report.json")
        self.tracker.save_report(tech_trends, output_path)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(output_path))
        
        # 验证文件内容
        with open(output_path, 'r', encoding='utf-8') as f:
            loaded_report = json.load(f)
            self.assertEqual(loaded_report["report_id"], tech_trends["report_id"])
            self.assertEqual(loaded_report["title"], tech_trends["title"])
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
