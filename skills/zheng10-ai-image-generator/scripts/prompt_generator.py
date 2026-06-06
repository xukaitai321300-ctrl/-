#!/usr/bin/env python3
"""
保温杯提示词生成工具 (prompt_generator.py)
为羊专家（zheng10-ai-image-generator）提供提示词生成功能
版本: 4.0.0
创建时间: 2026-06-05
"""

import json
import os
from typing import Dict, List, Optional

# 加载提示词模板数据库
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
PROMPT_TEMPLATES_FILE = os.path.join(DATA_DIR, 'prompt_templates.json')

def load_prompt_templates() -> Dict:
    """加载提示词模板数据库"""
    try:
        with open(PROMPT_TEMPLATES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：找不到文件 {PROMPT_TEMPLATES_FILE}")
        return {}
    except json.JSONDecodeError:
        print(f"错误：解析JSON文件失败 {PROMPT_TEMPLATES_FILE}")
        return {}

# 全局数据库
_PROMPT_TEMPLATES_DB = load_prompt_templates()

def generate_prompt(product_type: str, material: str, surface_treatment: str, 
                  scene: Optional[str] = None, style: Optional[str] = None) -> Dict:
    """
    生成保温杯产品提示词
    Args:
        product_type: 产品类型（'children_cup', 'bounce_lid_cup', 'smart_cup'）
        material: 材料（'304_stainless_steel', '316_stainless_steel', 'TA2_pure_titanium', 'PP_plastic', 'TRITAN_plastic'）
        surface_treatment: 表面处理（'matte_spray_painting', 'brushed_finish', 'laser_marked_LOGO'）
        scene: 场景（可选，如 'kids_room', 'car_cup_holder', 'modern_home'）
        style: 风格（可选，如 'cute_cartoon', 'modern_minimalist', 'high-tech'）
    Returns:
        提示词字典（包含正面提示词、负面提示词、摄影参数）
    """
    if not _PROMPT_TEMPLATES_DB:
        return {}
    
    templates = _PROMPT_TEMPLATES_DB.get('prompt_templates', {})
    if product_type not in templates:
        print(f"错误：找不到产品类型 '{product_type}' 的模板")
        return {}
    
    template = templates[product_type]
    
    # 构建正面提示词
    positive_prompt = template.get('base', '')
    
    # 添加材料描述
    materials = template.get('materials', {})
    if material in materials:
        positive_prompt += f", {materials[material]}"
    
    # 添加表面处理描述
    surface_treatments = template.get('surface_treatments', {})
    if surface_treatment in surface_treatments:
        positive_prompt += f", {surface_treatments[surface_treatment]}"
    
    # 添加场景描述
    if scene:
        positive_prompt += f", {scene}"
    elif 'scene' in template:
        positive_prompt += f", {template['scene']}"
    
    # 添加风格描述
    if style:
        positive_prompt += f", {style} style"
    
    # 添加摄影灯光
    if 'lighting' in template:
        positive_prompt += f", {template['lighting']}"
    
    # 添加构图模板
    if 'composition' in template:
        positive_prompt += f", {template['composition']}"
    
    # 添加质量标准
    positive_prompt += ", professional product photography, high resolution, 8K, realistic texture, high quality"
    
    # 构建负面提示词
    negative_prompt = "low quality, blurry, distorted, deformed, ugly, bad anatomy, extra limbs, missing limbs, floating limbs, (bad proportions:1.4), (poorly drawn hands:1.2), (poorly drawn face:1.2), missing legs, missing arms, poorly drawn face, poorly drawn hands, fused fingers, malformed limbs, out of frame, extra legs, extra arms, extra fingers, (worst quality:1.4), (low quality:1.4), (normal quality:1.4), jpeg artifacts, signature, watermark, username, blurry, artist name"
    
    # 摄影参数
    photography_params = {
        "camera": "professional product photography camera",
        "lens": "macro lens, 100mm, f/8, ISO 100",
        "lighting": template.get('lighting', 'soft lighting'),
        "composition": template.get('composition', 'main view'),
        "resolution": "8K (7680x4320)",
        "color_mode": "RGB, 16-bit"
    }
    
    return {
        'positive_prompt': positive_prompt,
        'negative_prompt': negative_prompt,
        'photography_params': photography_params,
        'product_type': product_type,
        'material': material,
        'surface_treatment': surface_treatment,
        'scene': scene if scene else template.get('scene', ''),
        'style': style
    }

def generate_craftsmanship_integrated_prompt(product_type: str, material: str, 
                                   surface_treatment: str, craftsmanship_type: str) -> Dict:
    """
    生成融合工艺知识的保温杯产品提示词
    Args:
        product_type: 产品类型
        material: 材料
        surface_treatment: 表面处理
        craftsmanship_type: 工艺类型（'materials_knowledge', 'surface_treatment_effects', 'injection_molding_quality', 'assembly_quality'）
    Returns:
        提示词字典（包含正面提示词、负面提示词、工艺知识描述）
    """
    if not _PROMPT_TEMPLATES_DB:
        return {}
    
    # 生成基础提示词
    base_prompt = generate_prompt(product_type, material, surface_treatment)
    if not base_prompt:
        return {}
    
    # 获取工艺知识融合数据库
    craftsmanship_integration = _PROMPT_TEMPLATES_DB.get('craftsmanship_integration', {})
    if craftsmanship_type not in craftsmanship_integration:
        print(f"警告：找不到工艺类型 '{craftsmanship_type}' 的知识")
        return base_prompt
    
    # 添加工艺知识描述
    craftsmanship_desc = craftsmanship_integration[craftsmanship_type]
    
    # 根据材料类型添加工艺知识
    material_key = material.split('_')[0]  # 提取材料关键词（如 '304', 'TA2', 'PP'）
    if material_key in ['304', '316', '316L']:
        if 'stainless_steel' in craftsmanship_desc:
            base_prompt['positive_prompt'] += f", {craftsmanship_desc['stainless_steel']}"
    elif material_key in ['TA1', 'TA2', 'TC4']:
        if 'pure_titanium' in craftsmanship_desc:
            base_prompt['positive_prompt'] += f", {craftsmanship_desc['pure_titanium']}"
    elif material_key in ['PP', 'TRITAN', 'silicone', 'ABS', 'PC']:
        if 'plastics' in craftsmanship_desc:
            base_prompt['positive_prompt'] += f", {craftsmanship_desc['plastics']}"
    
    # 添加表面处理工艺知识
    surface_key = surface_treatment.split('_')[0]  # 提取表面处理关键词
    if surface_key in ['spray', 'brushed', 'laser', 'heat', '3D', 'electro', 'UV']:
        if 'surface_treatment_effects' in craftsmanship_integration:
            surface_desc = craftsmanship_integration['surface_treatment_effects']
            if surface_key in surface_desc:
                base_prompt['positive_prompt'] += f", {surface_desc[surface_key]}"
    
    # 添加注塑工艺知识（针对塑料部件）
    if material_key in ['PP', 'TRITAN', 'ABS', 'PC']:
        if 'injection_molding_quality' in craftsmanship_integration:
            injection_desc = craftsmanship_integration['injection_molding_quality']
            if material_key in injection_desc:
                base_prompt['positive_prompt'] += f", {injection_desc[material_key]}"
    
    # 添加组装工艺知识
    if 'assembly_quality' in craftsmanship_integration:
        assembly_desc = craftsmanship_integration['assembly_quality']
        # 根据产品类型添加组装工艺知识
        if product_type == 'bounce_lid_cup' and 'buckle_assembly' in assembly_desc:
            base_prompt['positive_prompt'] += f", {assembly_desc['buckle_assembly']}"
        elif product_type == 'smart_cup' and 'screw_fixation' in assembly_desc:
            base_prompt['positive_prompt'] += f", {assembly_desc['screw_fixation']}"
    
    return base_prompt

def optimize_prompt(prompt: Dict, optimization_target: str) -> Dict:
    """
    优化提示词
    Args:
        prompt: 提示词字典
        optimization_target: 优化目标（'realism', 'material_texture', 'lighting', 'composition'）
    Returns:
        优化后的提示词字典
    """
    if not prompt:
        return {}
    
    optimized_prompt = prompt.copy()
    
    if optimization_target == 'realism':
        optimized_prompt['positive_prompt'] += ", photorealistic, hyperrealistic, 8K resolution, RAW photo, DSLR, high quality, masterpiece"
    elif optimization_target == 'material_texture':
        optimized_prompt['positive_prompt'] += ", detailed material texture, metallic luster, precise surface treatment, realistic texture"
    elif optimization_target == 'lighting':
        optimized_prompt['positive_prompt'] += ", professional lighting, 3-point lighting, softbox lighting, precise shadow, natural lighting"
    elif optimization_target == 'composition':
        optimized_prompt['positive_prompt'] += ", professional composition, rule of thirds, perfect framing, clean background"
    
    return optimized_prompt

def main():
    """主函数 - 演示工具使用"""
    print("保温杯提示词生成工具演示")
    print("=" * 50)
    
    # 1. 生成儿童保温杯提示词
    print("\n1. 生成儿童保温杯提示词（不锈钢316、喷漆哑光、激光打标LOGO）")
    prompt1 = generate_prompt('children_cup', '316_stainless_steel', 'matte_spray_painting')
    if prompt1:
        print(f"   正面提示词: {prompt1['positive_prompt'][:100]}...")
        print(f"   负面提示词: {prompt1['negative_prompt'][:100]}...")
    
    # 2. 生成弹跳盖保温杯提示词（融合工艺知识）
    print("\n2. 生成弹跳盖保温杯提示词（纯钛TA2、拉丝表面、融合工艺知识）")
    prompt2 = generate_craftsmanship_integrated_prompt('bounce_lid_cup', 'TA2_pure_titanium', 'brushed_finish', 'materials_knowledge')
    if prompt2:
        print(f"   正面提示词: {prompt2['positive_prompt'][:100]}...")
    
    # 3. 优化提示词
    print("\n3. 优化提示词（目标：真实感）")
    if prompt1:
        optimized_prompt = optimize_prompt(prompt1, 'realism')
        print(f"   优化后正面提示词: {optimized_prompt['positive_prompt'][-100:]}")
    
    print("\n" + "=" * 50)
    print("演示完成！")

if __name__ == '__main__':
    main()
