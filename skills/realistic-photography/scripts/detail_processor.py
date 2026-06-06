#!/usr/bin/env python3
"""
高清细节处理工具 (Detail Processor Tool)
为保温杯产品真实摄影生图提供高清细节处理提示词生成
"""

import json
import argparse
import os
import sys

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
DETAIL_DATA_FILE = os.path.join(DATA_DIR, 'high_resolution_details.json')


def load_detail_data():
    """加载高清细节处理数据库"""
    try:
        with open(DETAIL_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('high_resolution_details', [])
    except Exception as e:
        print(f"❌ 错误：无法加载高清细节处理数据库 - {e}")
        return []


def get_detail_processing(detail_id):
    """根据ID获取细节处理"""
    details = load_detail_data()
    for detail in details:
        if detail.get('id') == detail_id:
            return detail
    return None


def list_details():
    """列出所有细节处理"""
    details = load_detail_data()
    if not details:
        print("❌ 没有找到任何细节处理")
        return
    
    print("📊 可用细节处理列表：")
    for detail in details:
        print(f"  - {detail.get('id')}: {detail.get('name')} ({detail.get('name_zh')})")


def print_detail_details(detail):
    """打印细节处理详情"""
    print(f"📊 细节处理详情：{detail.get('name')} ({detail.get('name_zh')})")
    print(f"  描述：{detail.get('description')}")
    print(f"  中文描述：{detail.get('description_zh')}")
    print(f"  应用：{detail.get('application')}")
    print(f"  中文应用：{detail.get('application_zh')}")
    
    techniques = detail.get('processing_techniques', {})
    print(f"\n  🔧 处理技巧：")
    for key, value in techniques.items():
        # 转换键名格式（下划线转空格，首字母大写）
        key_display = key.replace('_', ' ').title()
        print(f"    {key_display}: {value}")
    
    prompts = detail.get('prompt_keywords', {})
    print(f"\n  📝 提示词关键词：")
    print(f"    英文：{prompts.get('english')}")
    print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='高清细节处理工具')
    parser.add_argument('--detail', type=str, help='细节处理ID（material_surface_detail/logo_process_detail/assembly_seam_detail/lighting_reflection_detail/color_accuracy_detail）')
    parser.add_argument('--list', action='store_true', help='列出所有细节处理')
    
    args = parser.parse_args()
    
    if args.list:
        list_details()
        return
    
    if not args.detail:
        print("❌ 错误：请指定细节处理ID（使用 --detail）或列出所有细节处理（使用 --list）")
        parser.print_help()
        return
    
    detail = get_detail_processing(args.detail)
    if not detail:
        print(f"❌ 错误：找不到ID为 '{args.detail}' 的细节处理")
        list_details()
        return
    
    print_detail_details(detail)


if __name__ == '__main__':
    main()