"""
测试素材搜索工具 - Test Material Searcher
"""

import unittest
import json
import os
from scripts.material_searcher import MaterialSearcher


class TestMaterialSearcher(unittest.TestCase):
    """测试素材搜索器"""
    
    def setUp(self):
        """测试前准备"""
        self.searcher = MaterialSearcher()
        self.test_output_dir = "test_reports"
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.searcher)
        self.assertIsNotNone(self.searcher.materials)
        self.assertGreater(len(self.searcher.materials), 0)
    
    def test_search_materials_by_keyword(self):
        """测试根据关键词搜索材质"""
        # 搜索材质
        results = self.searcher.search_materials(keyword="镁合金")
        
        # 验证结果
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        
        # 验证搜索结果
        for result in results:
            self.assertTrue(
                "镁合金" in result.get("name", "") or
                "镁合金" in result.get("description", "") or
                any("镁合金" in kw for kw in result.get("prompt_keywords", []))
            )
    
    def test_search_materials_by_type(self):
        """测试根据类型搜索材质"""
        # 搜索材质
        results = self.searcher.search_materials(material_type="金属")
        
        # 验证结果
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        
        # 验证搜索结果
        for result in results:
            self.assertEqual(result.get("type"), "金属")
    
    def test_search_materials_by_features(self):
        """测试根据特征搜索材质"""
        # 搜索材质
        results = self.searcher.search_materials(features=["轻量化"])
        
        # 验证结果
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        
        # 验证搜索结果
        for result in results:
            self.assertTrue("轻量化" in result.get("features", []))
    
    def test_get_material_by_id(self):
        """测试根据ID获取材质"""
        # 获取材质
        material = self.searcher.get_material_by_id("material_001")
        
        # 验证结果
        self.assertIsNotNone(material)
        self.assertEqual(material["id"], "material_001")
        self.assertEqual(material["name"], "镁合金 AE44")
    
    def test_generate_material_report(self):
        """测试生成材质素材报告"""
        # 搜索材质
        results = self.searcher.search_materials(keyword="镁合金")
        
        # 生成报告
        report = self.searcher.generate_material_report(
            materials=results,
            output_path=os.path.join(self.test_output_dir, "test_material_report.json")
        )
        
        # 验证结果
        self.assertIsNotNone(report)
        self.assertIn("report_id", report)
        self.assertIn("title", report)
        self.assertIn("materials", report)
        
        # 验证文件是否存在
        self.assertTrue(os.path.exists(os.path.join(self.test_output_dir, "test_material_report.json")))
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试报告
        if os.path.exists(self.test_output_dir):
            import shutil
            shutil.rmtree(self.test_output_dir)


if __name__ == "__main__":
    unittest.main()
