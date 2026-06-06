#!/usr/bin/env python3
"""
摄影灯光模拟工具 (Lighting Simulator Tool)
为保温杯产品真实摄影生图提供灯光配置和提示词生成
"""

import json
import argparse
import os
import sys

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
LIGHTING_DATA_FILE = os.path.join(DATA_DIR, 'lighting_setups.json')


def load_lighting_data():
    """加载摄影灯光数据库"""
    try:
        with open(LIGHTING_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('lighting_setups', [])
    except Exception as e:
        print(f"❌ 错误：无法加载灯光数据库 - {e}")
        return []


def get_lighting_setup(setup_id):
    """根据ID获取灯光配置"""
    setups = load_lighting_data()
    for setup in setups:
        if setup.get('id') == setup_id:
            return setup
    return None


def list_setups():
    """列出所有灯光配置"""
    setups = load_lighting_data()
    if not setups:
        print("❌ 没有找到任何灯光配置")
        return
    
    print("📊 可用灯光配置列表：")
    for setup in setups:
        print(f"  - {setup.get('id')}: {setup.get('name')} ({setup.get('name_zh')})")


def print_setup_details(setup):
    """打印灯光配置详情"""
    print(f"📊 灯光配置详情：{setup.get('name')} ({setup.get('name_zh')})")
    print(f"  描述：{setup.get('description')}")
    print(f"  中文描述：{setup.get('description_zh')}")
    print(f"  应用：{setup.get('application')}")
    print(f"  中文应用：{setup.get('application_zh')}")
    
    print("\n  💡 灯光配置：")
    for light in setup.get('lights', []):
        print(f"    - {light.get('type')} ({light.get('type_zh')})")
        print(f"      位置：{light.get('position')}")
        print(f"      中文位置：{light.get('position_zh')}")
        print(f"      强度：{light.get('intensity')}")
        print(f"      中文强度：{light.get('intensity_zh')}")
        if 'softbox' in light:
            print(f"      修饰件：{light.get('softbox')}")
            print(f"      中文修饰件：{light.get('softbox_zh')}")
        if 'modifier' in light:
            print(f"      修饰件：{light.get('modifier')}")
            print(f"      中文修饰件：{light.get('modifier_zh')}")
        print(f"      用途：{light.get('purpose')}")
        print(f"      中文用途：{light.get('purpose_zh')}")
    
    camera = setup.get('camera_settings', {})
    print(f"\n  📷 相机设置：")
    print(f"    光圈：{camera.get('aperture')}")
    print(f"    中文光圈：{camera.get('aperture_zh')}")
    print(f"    快门速度：{camera.get('shutter_speed')}")
    print(f"    中文快门速度：{camera.get('shutter_speed_zh')}")
    print(f"    ISO：{camera.get('iso')}")
    print(f"    中文ISO：{camera.get('iso_zh')}")
    print(f"    白平衡：{camera.get('white_balance')}")
    print(f"    中文白平衡：{camera.get('white_balance_zh')}")
    print(f"    对焦模式：{camera.get('focus_mode')}")
    print(f"    中文对焦模式：{camera.get('focus_mode_zh')}")
    
    bg = setup.get('background', {})
    print(f"\n  🖼️ 背景设置：")
    print(f"    类型：{bg.get('type')}")
    print(f"    中文类型：{bg.get('type_zh')}")
    print(f"    距离：{bg.get('distance')}")
    print(f"    中文距离：{bg.get('distance_zh')}")
    print(f"    灯光：{bg.get('lighting')}")
    print(f"    中文灯光：{bg.get('lighting_zh')}")
    
    prompts = setup.get('prompt_keywords', {})
    print(f"\n  📝 提示词关键词：")
    print(f"    英文：{prompts.get('english')}")
    print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='摄影灯光模拟工具')
    parser.add_argument('--setup', type=str, help='灯光配置ID（three_point/top_light/window_light）')
    parser.add_argument('--list', action='store_true', help='列出所有灯光配置')
    
    args = parser.parse_args()
    
    if args.list:
        list_setups()
        return
    
    if not args.setup:
        print("❌ 错误：请指定灯光配置ID（使用 --setup）或列出所有配置（使用 --list）")
        parser.print_help()
        return
    
    setup = get_lighting_setup(args.setup)
    if not setup:
        print(f"❌ 错误：找不到ID为 '{args.setup}' 的灯光配置")
        list_setups()
        return
    
    print_setup_details(setup)


if __name__ == '__main__':
    main()