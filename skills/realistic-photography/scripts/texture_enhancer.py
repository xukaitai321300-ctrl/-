#!/usr/bin/env python3
"""
材质纹理增强工具 (Texture Enhancer Tool)
为保温杯产品真实摄影生图提供材质纹理增强提示词生成
"""

import json
import argparse
import os
import sys

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
MATERIAL_DATA_FILE = os.path.join(DATA_DIR, 'material_textures.json')


def load_material_data():
    """加载材质纹理数据库"""
    try:
        with open(MATERIAL_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('material_textures', [])
    except Exception as e:
        print(f"❌ 错误：无法加载材质纹理数据库 - {e}")
        return []


def get_material(material_id):
    """根据ID获取材质"""
    materials = load_material_data()
    for material in materials:
        if material.get('id') == material_id:
            return material
    return None


def list_materials():
    """列出所有材质"""
    materials = load_material_data()
    if not materials:
        print("❌ 没有找到任何材质")
        return
    
    print("📊 可用材质列表：")
    for material in materials:
        print(f"  - {material.get('id')}: {material.get('name')} ({material.get('name_zh')})")


def print_material_details(material):
    """打印材质详情"""
    print(f"📊 材质详情：{material.get('name')} ({material.get('name_zh')})")
    print(f"  类型：{material.get('type')}")
    print(f"  中文类型：{material.get('type_zh')}")
    
    props = material.get('texture_properties', {})
    print(f"\n  🔬 纹理属性：")
    print(f"    反射率：{props.get('reflectivity')}")
    print(f"    中文反射率：{props.get('reflectivity_zh')}")
    print(f"    镜面高光：{props.get('specular_highlight')}")
    print(f"    中文镜面高光：{props.get('specular_highlight_zh')}")
    print(f"    表面纹理：{props.get('surface_pattern')}")
    print(f"    中文表面纹理：{props.get('surface_pattern_zh')}")
    print(f"    颜色变化：{props.get('color_variation')}")
    print(f"    中文颜色变化：{props.get('color_variation_zh')}")
    print(f"    划痕可见性：{props.get('scratch_visibility')}")
    print(f"    中文划痕可见性：{props.get('scratch_visibility_zh')}")
    print(f"    防指纹性：{props.get('fingerprint_resistance')}")
    print(f"    中文防指纹性：{props.get('fingerprint_resistance_zh')}")
    
    tips = material.get('photography_tips', {})
    print(f"\n  📷 摄影技巧：")
    print(f"    灯光：{tips.get('lighting')}")
    print(f"    中文灯光：{tips.get('lighting_zh')}")
    print(f"    相机角度：{tips.get('camera_angle')}")
    print(f"    中文相机角度：{tips.get('camera_angle_zh')}")
    print(f"    后期处理：{tips.get('post_processing')}")
    print(f"    中文后期处理：{tips.get('post_processing_zh')}")
    
    prompts = material.get('prompt_keywords', {})
    print(f"\n  📝 提示词关键词：")
    print(f"    英文：{prompts.get('english')}")
    print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='材质纹理增强工具')
    parser.add_argument('--material', type=str, help='材质ID（stainless_steel_304/stainless_steel_316/titanium_ta1/plastic_pp/tritan/silicone）')
    parser.add_argument('--list', action='store_true', help='列出所有材质')
    
    args = parser.parse_args()
    
    if args.list:
        list_materials()
        return
    
    if not args.material:
        print("❌ 错误：请指定材质ID（使用 --material）或列出所有材质（使用 --list）")
        parser.print_help()
        return
    
    material = get_material(args.material)
    if not material:
        print(f"❌ 错误：找不到ID为 '{args.material}' 的材质")
        list_materials()
        return
    
    print_material_details(material)


if __name__ == '__main__':
    main()