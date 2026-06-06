"""
测试情报收集工具 - Test Intelligence Collector
"""

import unittest
import json
import os
from scripts.intelligence_collector import IntelligenceCollector


class TestIntelligenceCollector(unittest.TestCase):
    """测试情报收集器"""
    
    def setUp(self):
        """测试前准备"""
        self.collector = IntelligenceCollector()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.collector)
        self.assertIsNotNone(self.collector.sources)
    
    def test_collect_tech_intelligence(self):
        """测试收集技术情报"""
        # 收集技术情报
        tech_intel = self.collector.collect_tech_intelligence(
            keywords=["大模型", "Agent", "计算机视觉"],
            sources=["arXiv", "GitHub", "技术博客"],
            time_range="2026-01-01 to 2026-06-05"
        )
        
        # 验证结果
        self.assertIsNotNone(tech_intel)
        self.assertIn("report_id", tech_intel)
        self.assertIn("title", tech_intel)
        self.assertIn("keywords", tech_intel)
        self.assertIn("sources", tech_intel)
        self.assertIn("findings", tech_intel)
        self.assertIn("trends", tech_intel)
        self.assertIn("recommendations", tech_intel)
        
        # 验证内容
        self.assertEqual(len(tech_intel["keywords"]), 3)
        self.assertEqual(len(tech_intel["sources"]), 3)
        self.assertGreater(len(tech_intel["findings"]), 0)
        self.assertGreater(len(tech_intel["trends"]), 0)
        self.assertGreater(len(tech_intel["recommendations"]), 0)
    
    def test_collect_competitor_intelligence(self):
        """测试收集竞品情报"""
        # 收集竞品情报
        comp_intel = self.collector.collect_competitor_intelligence(
            competitors=["竞品A", "竞品B", "竞品C"],
            platforms=["官网", "京东", "天猫"]
        )
        
        # 验证结果
        self.assertIsNotNone(comp_intel)
        self.assertIn("report_id", comp_intel)
        self.assertIn("title", comp_intel)
        self.assertIn("competitors", comp_intel)
        self.assertIn("platforms", comp_intel)
        self.assertIn("updates", comp_intel)
        self.assertIn("analysis", comp_intel)
        self.assertIn("threat_level", comp_intel)
        self.assertIn("recommendations", comp_intel)
        
        # 验证内容
        self.assertEqual(len(comp_intel["competitors"]), 3)
        self.assertEqual(len(comp_intel["platforms"]), 3)
        self.assertGreater(len(comp_intel["updates"]), 0)
    
    def test_save_report(self):
        """测试保存报告"""
        # 收集技术情报
        tech_intel = self.collector.collect_tech_intelligence(
            keywords=["大模型"],
            sources=["arXiv"],
            time_range="2026-01-01 to 2026-06-05"
        )
        
        # 保存报告
        output_path = os.path.join(self.test_output_dir, "test_tech_report.json")
        self.collector.save_report(tech_intel, output_path)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(output_path))
        
        # 验证文件内容
        with open(output_path, 'r', encoding='utf-8') as f:
            loaded_report = json.load(f)
            self.assertEqual(loaded_report["report_id"], tech_intel["report_id"])
            self.assertEqual(loaded_report["title"], tech_intel["title"])
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
