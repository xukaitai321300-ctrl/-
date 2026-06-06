#!/usr/bin/env python3
"""
构图模板生成工具 (Composition Generator Tool)
为保温杯产品真实摄影生图提供产品摄影构图模板和提示词生成
"""

import json
import argparse
import os
import sys

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
COMPOSITION_DATA_FILE = os.path.join(DATA_DIR, 'composition_templates.json')


def load_composition_data():
    """加载产品摄影构图模板数据库"""
    try:
        with open(COMPOSITION_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('composition_templates', [])
    except Exception as e:
        print(f"❌ 错误：无法加载构图模板数据库 - {e}")
        return []


def get_composition_template(template_id):
    """根据ID获取构图模板"""
    templates = load_composition_data()
    for template in templates:
        if template.get('id') == template_id:
            return template
    return None


def list_templates():
    """列出所有构图模板"""
    templates = load_composition_data()
    if not templates:
        print("❌ 没有找到任何构图模板")
        return
    
    print("📊 可用构图模板列表：")
    for template in templates:
        print(f"  - {template.get('id')}: {template.get('name')} ({template.get('name_zh')})")


def print_template_details(template):
    """打印构图模板详情"""
    print(f"📊 构图模板详情：{template.get('name')} ({template.get('name_zh')})")
    print(f"  描述：{template.get('description')}")
    print(f"  中文描述：{template.get('description_zh')}")
    print(f"  应用：{template.get('application')}")
    print(f"  中文应用：{template.get('application_zh')}")
    
    rules = template.get('composition_rules', {})
    print(f"\n  📐 构图规则：")
    print(f"    相机角度：{rules.get('camera_angle')}")
    print(f"    中文相机角度：{rules.get('camera_angle_zh')}")
    print(f"    相机距离：{rules.get('camera_distance')}")
    print(f"    中文相机距离：{rules.get('camera_distance_zh')}")
    print(f"    构图：{rules.get('framing')}")
    print(f"    中文构图：{rules.get('framing_zh')}")
    print(f"    背景：{rules.get('background')}")
    print(f"    中文背景：{rules.get('background_zh')}")
    print(f"    灯光：{rules.get('lighting')}")
    print(f"    中文灯光：{rules.get('lighting_zh')}")
    print(f"    景深：{rules.get('depth_of_field')}")
    print(f"    中文景深：{rules.get('depth_of_field_zh')}")
    
    prompts = template.get('prompt_keywords', {})
    print(f"\n  📝 提示词关键词：")
    print(f"    英文：{prompts.get('english')}")
    print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='构图模板生成工具')
    parser.add_argument('--template', type=str, help='构图模板ID（front_view/side_view/top_view/detail_closeup/scene_matching）')
    parser.add_argument('--list', action='store_true', help='列出所有构图模板')
    
    args = parser.parse_args()
    
    if args.list:
        list_templates()
        return
    
    if not args.template:
        print("❌ 错误：请指定构图模板ID（使用 --template）或列出所有模板（使用 --list）")
        parser.print_help()
        return
    
    template = get_composition_template(args.template)
    if not template:
        print(f"❌ 错误：找不到ID为 '{args.template}' 的构图模板")
        list_templates()
        return
    
    print_template_details(template)


if __name__ == '__main__':
    main()