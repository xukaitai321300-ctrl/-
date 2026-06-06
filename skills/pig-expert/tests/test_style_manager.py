"""
测试风格管理工具 - Test Style Manager
"""

import unittest
import json
import os
from scripts.style_manager import StyleManager


class TestStyleManager(unittest.TestCase):
    """测试风格管理器"""
    
    def setUp(self):
        """测试前准备"""
        self.manager = StyleManager()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.manager)
        self.assertIsNotNone(self.manager.styles)
        self.assertGreater(len(self.manager.styles), 0)
    
    def test_add_style_reference(self):
        """测试添加风格参考"""
        # 添加风格参考
        new_style = self.manager.add_style_reference(
            style_name="测试风格",
            description="测试描述",
            reference_images=["test1.jpg", "test2.jpg"],
            tags=["测试", "风格"]
        )
        
        # 验证结果
        self.assertIsNotNone(new_style)
        self.assertIn("id", new_style)
        self.assertEqual(new_style["name"], "测试风格")
        self.assertEqual(new_style["description"], "测试描述")
        self.assertEqual(len(new_style["reference_images"]), 2)
        self.assertEqual(len(new_style["tags"]), 2)
    
    def test_search_style_references(self):
        """测试搜索风格参考"""
        # 搜索风格参考
        results = self.manager.search_style_references(keyword="现代")
        
        # 验证结果
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        
        # 验证搜索结果
        for result in results:
            self.assertTrue(
                "现代" in result.get("name", "") or
                "现代" in result.get("description", "") or
                any("现代" in kw for kw in result.get("keywords", [])) or
                any("现代" in tag for tag in result.get("tags", []))
            )
    
    def test_get_style_by_id(self):
        """测试根据ID获取风格参考"""
        # 获取风格参考
        style = self.manager.get_style_by_id("style_001")
        
        # 验证结果
        self.assertIsNotNone(style)
        self.assertEqual(style["id"], "style_001")
        self.assertEqual(style["name"], "现代简约")
    
    def test_update_style_reference(self):
        """测试更新风格参考"""
        # 更新风格参考
        updated_style = self.manager.update_style_reference(
            style_id="style_001",
            description="更新后的描述"
        )
        
        # 验证结果
        self.assertIsNotNone(updated_style)
        self.assertEqual(updated_style["description"], "更新后的描述")
        
        # 验证更新时间
        self.assertEqual(updated_style["updated_at"], os.popen("date +%Y-%m-%d").read().strip())
    
    def test_generate_style_report(self):
        """测试生成风格参考报告"""
        # 生成风格参考报告
        report = self.manager.generate_style_report(
            style_id="style_001",
            output_path=os.path.join(self.test_output_dir, "test_style_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("style_name", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_style_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
