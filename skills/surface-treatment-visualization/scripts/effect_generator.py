"""
效果生成工具（增强版） - Effect Generator
负责生成各种表面处理效果的图片，支持多种表面处理技术和材质
"""

import json
import os
import sys
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse


class EffectGenerator:
    """效果生成器（增强版）"""
    
    def __init__(self, treatment_path: str = "data/surface_treatments.json",
                 template_path: str = "data/effect_templates.json",
                 material_path: str = "data/material_effects.json"):
        """
        初始化生成器
        
        Args:
            treatment_path: 表面处理技术数据文件路径
            template_path: 效果模板数据文件路径
            material_path: 材质效果数据文件路径
        """
        self.treatment_path = treatment_path
        self.template_path = template_path
        self.material_path = material_path
        
        # 加载数据
        self.treatments = self._load_treatments()
        self.templates = self._load_templates()
        self.materials = self._load_materials()
        
        # 确保输出目录存在
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def _load_treatments(self) -> List[Dict[str, Any]]:
        """
        加载表面处理技术数据
        
        Returns:
            表面处理技术列表
        """
        try:
            with open(self.treatment_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 已加载 {len(data.get('surface_treatments', []))} 个表面处理技术")
                return data.get('surface_treatments', [])
        except FileNotFoundError:
            print(f"⚠️ 表面处理技术数据文件不存在: {self.treatment_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"❌ 表面处理技术数据JSON格式错误: {e}")
            return []
        except Exception as e:
            print(f"❌ 加载表面处理技术数据失败: {e}")
            return []
    
    def _load_templates(self) -> List[Dict[str, Any]]:
        """
        加载效果模板数据
        
        Returns:
            效果模板列表
        """
        try:
            with open(self.template_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 已加载 {len(data.get('effect_templates', []))} 个效果模板")
                return data.get('effect_templates', [])
        except FileNotFoundError:
            print(f"⚠️ 效果模板数据文件不存在: {self.template_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"❌ 效果模板数据JSON格式错误: {e}")
            return []
        except Exception as e:
            print(f"❌ 加载效果模板数据失败: {e}")
            return []
    
    def _load_materials(self) -> List[Dict[str, Any]]:
        """
        加载材质效果数据
        
        Returns:
            材质效果列表
        """
        try:
            with open(self.material_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 已加载 {len(data.get('material_effects', []))} 个材质效果")
                return data.get('material_effects', [])
        except FileNotFoundError:
            print(f"⚠️ 材质效果数据文件不存在: {self.material_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"❌ 材质效果数据JSON格式错误: {e}")
            return []
        except Exception as e:
            print(f"❌ 加载材质效果数据失败: {e}")
            return []
    
    def get_treatment_by_id(self, treatment_id: str) -> Optional[Dict[str, Any]]:
        """
        根据ID获取表面处理技术
        
        Args:
            treatment_id: 表面处理技术ID
            
        Returns:
            表面处理技术字典，如果未找到则返回None
        """
        for treatment in self.treatments:
            if treatment.get("id") == treatment_id:
                return treatment
        return None
    
    def get_treatment_by_name(self, treatment_name: str) -> Optional[Dict[str, Any]]:
        """
        根据名称获取表面处理技术
        
        Args:
            treatment_name: 表面处理技术名称（支持中英文）
            
        Returns:
            表面处理技术字典，如果未找到则返回None
        """
        for treatment in self.treatments:
            if treatment.get("name") == treatment_name or treatment.get("name_zh") == treatment_name:
                return treatment
        return None
    
    def get_template_by_id(self, template_id: str) -> Optional[Dict[str, Any]]:
        """
        根据ID获取效果模板
        
        Args:
            template_id: 效果模板ID
            
        Returns:
            效果模板字典，如果未找到则返回None
        """
        for template in self.templates:
            if template.get("id") == template_id:
                return template
        return None
    
    def get_material_by_id(self, material_id: str) -> Optional[Dict[str, Any]]:
        """
        根据ID获取材质效果
        
        Args:
            material_id: 材质效果ID
            
        Returns:
            材质效果字典，如果未找到则返回None
        """
        for material in self.materials:
            if material.get("id") == material_id:
                return material
        return None
    
    def generate_painting_effect(self, color: str, finish: str, material: str, 
                                output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成喷漆效果
        
        Args:
            color: 颜色
            finish: 表面处理（高光、哑光等）
            material: 材质
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not color or not isinstance(color, str):
            return {"error": "颜色参数无效"}
        
        if not finish or not isinstance(finish, str):
            return {"error": "表面处理参数无效"}
        
        if not material or not isinstance(material, str):
            return {"error": "材质参数无效"}
        
        # 创建效果描述
        effect_description = f"{finish}{color}喷漆效果，{material}材质，表面光滑，金属质感强"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "喷漆",
            "treatment_type_zh": "喷漆",
            "color": color,
            "finish": finish,
            "material": material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "color": color,
                "finish": finish,
                "material": material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the painting effect image.")
                print(f"✅ 喷漆效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存喷漆效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def generate_spraying_effect(self, color: str, texture: str, material: str,
                                output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成喷塑效果
        
        Args:
            color: 颜色
            texture: 纹理（细纹、粗纹等）
            material: 材质
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not color or not isinstance(color, str):
            return {"error": "颜色参数无效"}
        
        if not texture or not isinstance(texture, str):
            return {"error": "纹理参数无效"}
        
        if not material or not isinstance(material, str):
            return {"error": "材质参数无效"}
        
        # 创建效果描述
        effect_description = f"{color}{texture}喷塑效果，{material}材质，表面有{texture}纹理，触感舒适"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "喷塑",
            "treatment_type_zh": "喷塑",
            "color": color,
            "texture": texture,
            "material": material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "color": color,
                "texture": texture,
                "material": material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the spraying effect image.")
                print(f"✅ 喷塑效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存喷塑效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def generate_heat_transfer_effect(self, pattern: str, material: str,
                                      output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成热转印效果
        
        Args:
            pattern: 图案
            material: 材质
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not pattern or not isinstance(pattern, str):
            return {"error": "图案参数无效"}
        
        if not material or not isinstance(material, str):
            return {"error": "材质参数无效"}
        
        # 创建效果描述
        effect_description = f"{pattern}热转印效果，{material}材质，图案逼真，纹理清晰"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "热转印",
            "treatment_type_zh": "热转印",
            "pattern": pattern,
            "material": material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "pattern": pattern,
                "material": material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the heat transfer effect image.")
                print(f"✅ 热转印效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存热转印效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def generate_laser_engraving_effect(self, pattern: str, depth: str, material: str,
                                          output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成激光雕刻效果
        
        Args:
            pattern: 图案或文字
            depth: 雕刻深度（浅、中、深）
            material: 材质
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not pattern or not isinstance(pattern, str):
            return {"error": "图案参数无效"}
        
        if not depth or not isinstance(depth, str):
            return {"error": "雕刻深度参数无效"}
        
        if not material or not isinstance(material, str):
            return {"error": "材质参数无效"}
        
        # 创建效果描述
        effect_description = f"{pattern}激光雕刻效果，深度{depth}，{material}材质，图案精细，质感独特"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "激光雕刻",
            "treatment_type_zh": "激光雕刻",
            "pattern": pattern,
            "depth": depth,
            "material": material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "pattern": pattern,
                "depth": depth,
                "material": material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the laser engraving effect image.")
                print(f"✅ 激光雕刻效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存激光雕刻效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def generate_plating_effect(self, plating_type: str, base_material: str,
                                output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成电镀效果
        
        Args:
            plating_type: 电镀类型（镀铬、镀镍、镀锌等）
            base_material: 基材
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not plating_type or not isinstance(plating_type, str):
            return {"error": "电镀类型参数无效"}
        
        if not base_material or not isinstance(base_material, str):
            return {"error": "基材参数无效"}
        
        # 创建效果描述
        effect_description = f"{plating_type}电镀效果，{base_material}基材，表面光亮，耐腐蚀性强"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "电镀",
            "treatment_type_zh": "电镀",
            "plating_type": plating_type,
            "base_material": base_material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "plating_type": plating_type,
                "base_material": base_material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the plating effect image.")
                print(f"✅ 电镀效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存电镀效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def generate_anodizing_effect(self, color: str, material: str,
                                  output_path: str = None, extra_params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        生成阳极氧化效果
        
        Args:
            color: 颜色
            material: 材质（通常是铝合金）
            output_path: 输出路径
            extra_params: 额外参数
            
        Returns:
            效果结果字典
        """
        # 验证参数
        if not color or not isinstance(color, str):
            return {"error": "颜色参数无效"}
        
        if not material or not isinstance(material, str):
            return {"error": "材质参数无效"}
        
        # 创建效果描述
        effect_description = f"{color}阳极氧化效果，{material}材质，表面氧化膜均匀，色彩持久"
        
        # 创建效果结果
        result = {
            "success": True,
            "treatment_type": "阳极氧化",
            "treatment_type_zh": "阳极氧化",
            "color": color,
            "material": material,
            "effect_description": effect_description,
            "effect_description_zh": effect_description,
            "parameters": {
                "color": color,
                "material": material
            },
            "output_path": output_path,
            "generated_at": datetime.now().isoformat(),
            "extra_params": extra_params or {}
        }
        
        # 添加额外参数
        if extra_params:
            result["parameters"].update(extra_params)
        
        # 保存效果图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                # 这里应该是实际生成图片的代码
                # 由于没有实际的图像生成库，这里只是创建一个占位文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("This is a placeholder for the anodizing effect image.")
                print(f"✅ 阳极氧化效果图片已生成: {output_path}")
            except Exception as e:
                print(f"❌ 保存阳极氧化效果图片失败: {e}")
                result["save_error"] = str(e)
        
        return result
    
    def batch_generate_effects(self, effect_configs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量生成表面处理效果
        
        Args:
            effect_configs: 效果配置列表，每个配置包含：
                - treatment_type: 表面处理类型
                - parameters: 参数字典
                - output_path: 输出路径（可选）
                
        Returns:
            效果结果列表
        """
        if not effect_configs or not isinstance(effect_configs, list):
            return [{"error": "效果配置列表无效"}]
        
        results = []
        
        for i, config in enumerate(effect_configs):
            treatment_type = config.get("treatment_type")
            parameters = config.get("parameters", {})
            output_path = config.get("output_path")
            
            # 根据表面处理类型调用相应的生成方法
            if treatment_type == "喷漆":
                result = self.generate_painting_effect(
                    color=parameters.get("color", "红色"),
                    finish=parameters.get("finish", "高光"),
                    material=parameters.get("material", "镁合金"),
                    output_path=output_path or f"{self.output_dir}/batch_painting_{i+1:03d}.png"
                )
            elif treatment_type == "喷塑":
                result = self.generate_spraying_effect(
                    color=parameters.get("color", "蓝色"),
                    texture=parameters.get("texture", "细纹"),
                    material=parameters.get("material", "铝合金"),
                    output_path=output_path or f"{self.output_dir}/batch_spraying_{i+1:03d}.png"
                )
            elif treatment_type == "热转印":
                result = self.generate_heat_transfer_effect(
                    pattern=parameters.get("pattern", "木纹"),
                    material=parameters.get("material", "塑料"),
                    output_path=output_path or f"{self.output_dir}/batch_heat_transfer_{i+1:03d}.png"
                )
            elif treatment_type == "激光雕刻":
                result = self.generate_laser_engraving_effect(
                    pattern=parameters.get("pattern", "Logo"),
                    depth=parameters.get("depth", "中"),
                    material=parameters.get("material", "不锈钢"),
                    output_path=output_path or f"{self.output_dir}/batch_laser_engraving_{i+1:03d}.png"
                )
            elif treatment_type == "电镀":
                result = self.generate_plating_effect(
                    plating_type=parameters.get("plating_type", "镀铬"),
                    base_material=parameters.get("base_material", "钢铁"),
                    output_path=output_path or f"{self.output_dir}/batch_plating_{i+1:03d}.png"
                )
            elif treatment_type == "阳极氧化":
                result = self.generate_anodizing_effect(
                    color=parameters.get("color", "黑色"),
                    material=parameters.get("material", "铝合金"),
                    output_path=output_path or f"{self.output_dir}/batch_anodizing_{i+1:03d}.png"
                )
            else:
                result = {"error": f"不支持的表面处理类型: {treatment_type}"}
            
            results.append(result)
        
        print(f"✅ 批量生成完成，共生成 {len(results)} 个效果")
        return results
    
    def generate_effect_report(self, effect_result: Dict[str, Any], 
                              output_format: str = 'json', 
                              output_path: str = None) -> str:
        """
        生成效果报告（增强版）
        
        Args:
            effect_result: 效果结果字典
            output_format: 输出格式 ('json' 或 'markdown')
            output_path: 输出文件路径
            
        Returns:
            输出文件路径
        """
        # 创建报告
        report_id = f"EFFECT-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}"
        
        if output_format == 'markdown':
            # 生成Markdown格式报告
            report_content = f"""# 表面处理效果报告

## 基本信息
- **报告ID**：{report_id}
- **标题**：{effect_result.get('treatment_type_zh', effect_result.get('treatment_type', '未知效果'))}效果报告
- **生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **表面处理类型**：{effect_result.get('treatment_type_zh', effect_result.get('treatment_type', '未知'))}

## 效果参数
"""
            # 添加参数信息
            parameters = effect_result.get('parameters', {})
            for key, value in parameters.items():
                report_content += f"- **{key}**：{value}\n"
            
            report_content += f"""
## 效果描述
{effect_result.get('effect_description_zh', effect_result.get('effect_description', '无描述'))}

## 生成信息
- **生成时间**：{effect_result.get('generated_at', '未知')}
- **输出路径**：{effect_result.get('output_path', '未知')}
- **成功状态**：{'✅ 成功' if effect_result.get('success', False) else '❌ 失败'}

## 优化建议
"""
            # 添加优化建议
            recommendations = self._generate_recommendations(effect_result)
            for i, rec in enumerate(recommendations, 1):
                report_content += f"{i}. {rec}\n"
            
            report_content += f"""
## 总结
- **表面处理类型**：{effect_result.get('treatment_type_zh', effect_result.get('treatment_type', '未知'))}
- **参数数量**：{len(parameters)}
- **优化建议数量**：{len(recommendations)}
"""
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/effect_report_{report_id}.md"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(report_content)
                print(f"✅ 效果报告已保存（Markdown）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存效果报告失败: {e}")
                return None
            
        else:  # JSON格式
            report = {
                "report_id": report_id,
                "title": f"{effect_result.get('treatment_type', '未知效果')}效果报告",
                "title_zh": f"{effect_result.get('treatment_type_zh', effect_result.get('treatment_type', '未知效果'))}效果报告",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "treatment_type": effect_result.get("treatment_type"),
                "treatment_type_zh": effect_result.get("treatment_type_zh"),
                "parameters": effect_result.get("parameters", {}),
                "effect_description": effect_result.get("effect_description"),
                "effect_description_zh": effect_result.get("effect_description_zh"),
                "output_path": effect_result.get("output_path"),
                "generated_at": effect_result.get("generated_at"),
                "success": effect_result.get("success", False),
                "recommendations": self._generate_recommendations(effect_result),
                "generated_at_report": datetime.now().isoformat()
            }
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/effect_report_{report_id}.json"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, ensure_ascii=False, indent=2)
                print(f"✅ 效果报告已保存（JSON）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存效果报告失败: {e}")
                return None
    
    def _generate_recommendations(self, effect_result: Dict[str, Any]) -> List[str]:
        """
        生成优化建议（增强版）
        
        Args:
            effect_result: 效果结果字典
            
        Returns:
            优化建议列表
        """
        recommendations = []
        
        # 基于表面处理类型的建议
        treatment_type = effect_result.get("treatment_type")
        if treatment_type == "喷漆":
            recommendations.append("确保表面清洁，无油污和灰尘")
            recommendations.append("控制喷涂环境温度和湿度")
            recommendations.append("选择合适的底漆和面漆")
            recommendations.append("掌握正确的喷涂距离和速度")
        elif treatment_type == "喷塑":
            recommendations.append("确保粉末涂料干燥，无结块")
            recommendations.append("控制固化温度和时间")
            recommendations.append("选择合适的纹理类型")
            recommendations.append("确保喷枪压力稳定")
        elif treatment_type == "热转印":
            recommendations.append("确保转印纸图案清晰")
            recommendations.append("控制转印温度、压力和时间")
            recommendations.append("选择合适的转印图案")
            recommendations.append("确保转印表面平整")
        elif treatment_type == "激光雕刻":
            recommendations.append("确保激光参数设置正确")
            recommendations.append("控制雕刻深度和精度")
            recommendations.append("选择合适的图案和文字")
            recommendations.append("定期清洁激光头部")
        elif treatment_type == "电镀":
            recommendations.append("确保电镀液成分和浓度正确")
            recommendations.append("控制电镀温度和时间")
            recommendations.append("选择合适的电镀类型")
            recommendations.append("确保基材表面预处理充分")
        elif treatment_type == "阳极氧化":
            recommendations.append("确保阳极氧化液成分和浓度正确")
            recommendations.append("控制阳极氧化电压和时间")
            recommendations.append("选择合适的颜色")
            recommendations.append("确保铝合金表面预处理充分")
        
        # 基于成功状态的建议
        if not effect_result.get("success", False):
            recommendations.append("检查参数设置是否正确")
            recommendations.append("查看错误日志以获取更多信息")
        
        return recommendations
    
    def print_effect_summary(self, effect_result: Dict[str, Any]) -> None:
        """
        打印效果摘要
        
        Args:
            effect_result: 效果结果字典
        """
        print(f"\n📊 效果生成摘要")
        print(f"  表面处理类型: {effect_result.get('treatment_type_zh', effect_result.get('treatment_type', '未知'))}")
        print(f"  成功状态: {'✅ 成功' if effect_result.get('success', False) else '❌ 失败'}")
        print(f"  生成时间: {effect_result.get('generated_at', '未知')}")
        
        # 打印参数
        parameters = effect_result.get("parameters", {})
        if parameters:
            print(f"  参数:")
            for key, value in parameters.items():
                print(f"    - {key}: {value}")
        
        # 打印效果描述
        effect_desc = effect_result.get("effect_description_zh", effect_result.get("effect_description", ""))
        if effect_desc:
            print(f"  效果描述: {effect_desc}")
        
        # 打印输出路径
        output_path = effect_result.get("output_path")
        if output_path:
            print(f"  输出路径: {output_path}")
    
    def validate_parameters(self, treatment_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证参数
        
        Args:
            treatment_type: 表面处理类型
            parameters: 参数字典
            
        Returns:
            验证结果字典
        """
        validation_result = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }
        
        # 根据表面处理类型验证参数
        if treatment_type == "喷漆":
            if "color" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少颜色参数")
            
            if "finish" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少表面处理参数")
            
            if "material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少材质参数")
            
        elif treatment_type == "喷塑":
            if "color" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少颜色参数")
            
            if "texture" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少纹理参数")
            
            if "material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少材质参数")
            
        elif treatment_type == "热转印":
            if "pattern" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少图案参数")
            
            if "material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少材质参数")
            
        elif treatment_type == "激光雕刻":
            if "pattern" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少图案参数")
            
            if "depth" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少深度参数")
            
            if "material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少材质参数")
            
        elif treatment_type == "电镀":
            if "plating_type" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少电镀类型参数")
            
            if "base_material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少基材参数")
            
        elif treatment_type == "阳极氧化":
            if "color" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少颜色参数")
            
            if "material" not in parameters:
                validation_result["is_valid"] = False
                validation_result["errors"].append("缺少材质参数")
            
        else:
            validation_result["is_valid"] = False
            validation_result["errors"].append(f"不支持的表面处理类型: {treatment_type}")
        
        return validation_result


# 使用示例
if __name__ == "__main__":
    # 初始化效果生成器
    generator = EffectGenerator()
    
    # 生成喷漆效果
    painting_effect = generator.generate_painting_effect(
        color="红色",
        finish="高光",
        material="镁合金",
        output_path="output/painting_effect.png"
    )
    print(f"生成喷漆效果: {painting_effect['effect_description']}")
    generator.print_effect_summary(painting_effect)
    
    # 生成喷塑效果
    spraying_effect = generator.generate_spraying_effect(
        color="蓝色",
        texture="细纹",
        material="铝合金",
        output_path="output/spraying_effect.png"
    )
    print(f"生成喷塑效果: {spraying_effect['effect_description']}")
    
    # 生成热转印效果
    heat_transfer_effect = generator.generate_heat_transfer_effect(
        pattern="木纹",
        material="塑料",
        output_path="output/heat_transfer_effect.png"
    )
    print(f"生成热转印效果: {heat_transfer_effect['effect_description']}")
    
    # 生成激光雕刻效果
    laser_engraving_effect = generator.generate_laser_engraving_effect(
        pattern="Logo",
        depth="中",
        material="不锈钢",
        output_path="output/laser_engraving_effect.png"
    )
    print(f"生成激光雕刻效果: {laser_engraving_effect['effect_description']}")
    
    # 生成电镀效果
    plating_effect = generator.generate_plating_effect(
        plating_type="镀铬",
        base_material="钢铁",
        output_path="output/plating_effect.png"
    )
    print(f"生成电镀效果: {plating_effect['effect_description']}")
    
    # 生成阳极氧化效果
    anodizing_effect = generator.generate_anodizing_effect(
        color="黑色",
        material="铝合金",
        output_path="output/anodizing_effect.png"
    )
    print(f"生成阳极氧化效果: {anodizing_effect['effect_description']}")
    
    # 生成效果报告
    report_path = generator.generate_effect_report(
        effect_result=painting_effect,
        output_format='markdown',
        output_path="reports/painting_effect_report.md"
    )
    print(f"生成效果报告: {report_path}")
    
    # 批量生成效果
    batch_configs = [
        {
            "treatment_type": "喷漆",
            "parameters": {"color": "红色", "finish": "高光", "material": "镁合金"}
        },
        {
            "treatment_type": "喷塑",
            "parameters": {"color": "蓝色", "texture": "细纹", "material": "铝合金"}
        },
        {
            "treatment_type": "热转印",
            "parameters": {"pattern": "木纹", "material": "塑料"}
        }
    ]
    
    batch_results = generator.batch_generate_effects(batch_configs)
    print(f"批量生成了 {len(batch_results)} 个效果")
