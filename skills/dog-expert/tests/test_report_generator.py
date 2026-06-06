"""
测试报告生成工具 - Test Report Generator
"""

import unittest
import json
import os
from scripts.report_generator import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    """测试报告生成器"""
    
    def setUp(self):
        """测试前准备"""
        self.generator = ReportGenerator(output_dir="test_reports")
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.output_dir, "test_reports")
        self.assertTrue(os.path.exists("test_reports"))
    
    def test_generate_tech_report(self):
        """测试生成技术情报报告"""
        # 准备测试数据
        tech_data = {
            "report_id": "TECH-20260605-001",
            "title": "2026年6月AI技术动态",
            "date": "2026-06-05",
            "keywords": ["大模型", "Agent", "计算机视觉"],
            "sources": ["arXiv", "GitHub", "技术博客"],
            "findings": [
                {
                    "title": "GPT-5发布",
                    "source": "OpenAI官方博客",
                    "date": "2026-06-01",
                    "summary": "OpenAI发布GPT-5，性能提升30%",
                    "impact": "高",
                    "url": "https://openai.com/blog/gpt-5"
                }
            ],
            "trends": ["多模态融合", "Agent自主化", "边缘计算"],
            "recommendations": ["关注多模态技术", "布局Agent应用", "探索边缘计算场景"]
        }
        
        # 生成报告
        report_path = self.generator.generate_intelligence_report(tech_data, "tech")
        
        # 验证结果
        self.assertIsNotNone(report_path)
        self.assertTrue(os.path.exists(report_path))
        
        # 验证文件内容
        with open(report_path, 'r', encoding='utf-8') as f:
            loaded_report = json.load(f)
            self.assertEqual(loaded_report["report_id"], tech_data["report_id"])
            self.assertEqual(loaded_report["title"], tech_data["title"])
            self.assertEqual(len(loaded_report["keywords"]), len(tech_data["keywords"]))
            self.assertEqual(len(loaded_report["findings"]), len(tech_data["findings"]))
    
    def test_generate_competitor_report(self):
        """测试生成竞品监测报告"""
        # 准备测试数据
        comp_data = {
            "report_id": "COMP-20260605-001",
            "title": "竞品A产品更新监测",
            "date": "2026-06-05",
            "competitors": ["竞品A"],
            "platforms": ["官网", "京东", "天猫"],
            "updates": [
                {
                    "type": "产品发布",
                    "title": "竞品A发布新款电动轮椅",
                    "date": "2026-06-03",
                    "features": ["轻量化设计", "智能导航", "健康监测"],
                    "price": "¥3,999",
                    "url": "https:// competitor-a.com/new-product"
                }
            ],
            "analysis": "竞品A在轻量化和智能化方面持续投入",
            "threat_level": "中",
            "recommendations": ["加强轻量化材料研发", "加快智能导航技术布局"]
        }
        
        # 生成报告
        report_path = self.generator.generate_intelligence_report(comp_data, "competitor")
        
        # 验证结果
        self.assertIsNotNone(report_path)
        self.assertTrue(os.path.exists(report_path))
        
        # 验证文件内容
        with open(report_path, 'r', encoding='utf-8') as f:
            loaded_report = json.load(f)
            self.assertEqual(loaded_report["report_id"], comp_data["report_id"])
            self.assertEqual(loaded_report["title"], comp_data["title"])
            self.assertEqual(len(loaded_report["competitors"]), len(comp_data["competitors"]))
            self.assertEqual(len(loaded_report["updates"]), len(comp_data["updates"]))
    
    def test_generate_summary_report(self):
        """测试生成综合报告"""
        # 准备测试数据
        reports = [
            {
                "report_id": "TECH-20260605-001",
                "title": "2026年6月AI技术动态",
                "type": "tech"
            },
            {
                "report_id": "COMP-20260605-001",
                "title": "竞品A产品更新监测",
                "type": "competitor"
            }
        ]
        
        # 生成综合报告
        summary_path = self.generator.generate_summary_report(reports)
        
        # 验证结果
        self.assertIsNotNone(summary_path)
        self.assertTrue(os.path.exists(summary_path))
        
        # 验证文件内容
        with open(summary_path, 'r', encoding='utf-8') as f:
            loaded_summary = json.load(f)
            self.assertIn("report_id", loaded_summary)
            self.assertIn("title", loaded_summary)
            self.assertIn("executive_summary", loaded_summary)
            self.assertIn("key_findings", loaded_summary)
            self.assertIn("strategic_recommendations", loaded_summary)
            self.assertIn("reports", loaded_summary)
            self.assertEqual(len(loaded_summary["reports"]), len(reports))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists("test_reports"):
            import shutil
            shutil.rmtree("test_reports")


if __name__ == "__main__":
    unittest.main()
