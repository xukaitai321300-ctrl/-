"""
测试竞品监测工具 - Test Competitor Monitor
"""

import unittest
import json
import os
from scripts.competitor_monitor import CompetitorMonitor


class TestCompetitorMonitor(unittest.TestCase):
    """测试竞品监测器"""
    
    def setUp(self):
        """测试前准备"""
        self.monitor = CompetitorMonitor()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.monitor)
        self.assertIsNotNone(self.monitor.competitors)
    
    def test_monitor_product_releases(self):
        """测试监测竞品产品发布"""
        # 监测竞品产品发布
        product_updates = self.monitor.monitor_product_releases(
            competitors=["竞品A", "竞品B"],
            platforms=["官网", "京东", "天猫"]
        )
        
        # 验证结果
        self.assertIsNotNone(product_updates)
        self.assertIn("report_id", product_updates)
        self.assertIn("title", product_updates)
        self.assertIn("competitors", product_updates)
        self.assertIn("platforms", product_updates)
        self.assertIn("updates", product_updates)
        self.assertIn("analysis", product_updates)
        self.assertIn("threat_level", product_updates)
        self.assertIn("recommendations", product_updates)
        
        # 验证内容
        self.assertEqual(len(product_updates["competitors"]), 2)
        self.assertEqual(len(product_updates["platforms"]), 3)
        self.assertGreater(len(product_updates["updates"]), 0)
    
    def test_monitor_patent_filings(self):
        """测试监测竞品专利申请"""
        # 监测竞品专利申请
        patent_updates = self.monitor.monitor_patent_filings(
            competitors=["竞品A", "竞品B"]
        )
        
        # 验证结果
        self.assertIsNotNone(patent_updates)
        self.assertIn("report_id", patent_updates)
        self.assertIn("title", patent_updates)
        self.assertIn("competitors", patent_updates)
        self.assertIn("patents", patent_updates)
        self.assertIn("analysis", patent_updates)
        self.assertIn("recommendations", patent_updates)
        
        # 验证内容
        self.assertEqual(len(patent_updates["competitors"]), 2)
        self.assertGreaterEqual(len(patent_updates["patents"]), 0)
    
    def test_save_report(self):
        """测试保存报告"""
        # 监测竞品产品发布
        product_updates = self.monitor.monitor_product_releases(
            competitors=["竞品A"],
            platforms=["官网"]
        )
        
        # 保存报告
        output_path = os.path.join(self.test_output_dir, "test_competitor_report.json")
        self.monitor.save_report(product_updates, output_path)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(output_path))
        
        # 验证文件内容
        with open(output_path, 'r', encoding='utf-8') as f:
            loaded_report = json.load(f)
            self.assertEqual(loaded_report["report_id"], product_updates["report_id"])
            self.assertEqual(loaded_report["title"], product_updates["title"])
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
