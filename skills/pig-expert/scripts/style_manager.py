#!/usr/bin/env python3
"""
风格管理工具 (Style Manager) - 增强版
为十二生肖团提供风格参考管理功能，支持风格添加、搜索、更新、删除和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import shutil

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
STYLE_DATA_FILE = os.path.join(DATA_DIR, 'style_references.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')
REFERENCE_IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reference_images')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(REFERENCE_IMAGES_DIR, exist_ok=True)


def load_style_data() -> Dict[str, Any]:
    """加载风格参考数据库"""
    try:
        with open(STYLE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载风格参考数据库 - {e}")
        return {}

def save_style_data(data: Dict[str, Any]) -> bool:
    """保存风格参考数据库"""
    try:
        with open(STYLE_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 风格参考数据库已更新：{STYLE_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存风格参考数据库 - {e}")
        return False


def get_style_by_id(style_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取风格参考"""
    data = load_style_data()
    styles = data.get('style_references', [])
    for style in styles:
        if style.get('id') == style_id:
            return style
    return None


def list_styles() -> None:
    """列出所有风格参考"""
    data = load_style_data()
    styles = data.get('style_references', [])
    if not styles:
        print("❌ 没有找到任何风格参考")
        return
    
    print("📊 可用风格参考列表：")
    for style in styles:
        print(f"  - {style.get('id')}: {style.get('name')} ({style.get('name_zh')})")


def add_style_reference(style_name: str, description: str, 
                       reference_images: List[str] = None, 
                       tags: List[str] = None) -> Dict[str, Any]:
    """
    添加风格参考
    
    Args:
        style_name: 风格名称
        description: 风格描述
        reference_images: 参考图像列表
        tags: 标签列表
        
    Returns:
        添加的风格参考字典
    """
    if not reference_images:
        reference_images = []
    
    if not tags:
        tags = []
    
    # 生成风格ID
    data = load_style_data()
    styles = data.get('style_references', [])
    style_id = f"style_{len(styles) + 1:03d}"
    
    # 创建新风格参考
    new_style = {
        'id': style_id,
        'name': style_name,
        'name_zh': style_name,  # 中文名称（默认与英文相同）
        'description': description,
        'description_zh': description,  # 中文描述（默认与英文相同）
        'key_features': [],
        'keywords': [],
        'reference_images': reference_images,
        'application_scenarios': [],
        'prompt_templates': [],
        'tags': tags,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    # 添加到风格列表
    styles.append(new_style)
    data['style_references'] = styles
    
    # 保存到文件
    save_style_data(data)
    
    print(f"✅ 风格参考已添加：{style_id} - {style_name}")
    return new_style


def search_style_references(keyword: str) -> List[Dict[str, Any]]:
    """
    搜索风格参考
    
    Args:
        keyword: 搜索关键词
        
    Returns:
        匹配的风格参考列表
    """
    data = load_style_data()
    styles = data.get('style_references', [])
    results = []
    
    # 搜索匹配的风格
    for style in styles:
        # 检查名称、描述、关键词、标签是否匹配
        if (keyword.lower() in style.get('name', '').lower() or
            keyword.lower() in style.get('description', '').lower() or
            any(keyword.lower() in kw.lower() for kw in style.get('keywords', [])) or
            any(keyword.lower() in tag.lower() for tag in style.get('tags', []))):
            results.append(style)
    
    print(f"🔍 搜索到 {len(results)} 个风格参考（关键词：{keyword}）")
    return results


def update_style_reference(style_id: str, **kwargs) -> Optional[Dict[str, Any]]:
    """
    更新风格参考
    
    Args:
        style_id: 风格ID
        **kwargs: 要更新的字段和值
        
    Returns:
        更新后的风格参考字典
    """
    data = load_style_data()
    styles = data.get('style_references', [])
    
    for i, style in enumerate(styles):
        if style.get('id') == style_id:
            # 更新字段
            for key, value in kwargs.items():
                if key in style:
                    style[key] = value
            
            # 更新更新时间
            style['updated_at'] = datetime.now().isoformat()
            
            # 保存到文件
            data['style_references'] = styles
            save_style_data(data)
            
            print(f"✅ 风格参考已更新：{style_id}")
            return style
    
    print(f"❌ 错误：找不到ID为 '{style_id}' 的风格参考")
    return None


def delete_style_reference(style_id: str) -> bool:
    """
    删除风格参考
    
    Args:
        style_id: 风格ID
        
    Returns:
        是否删除成功
    """
    data = load_style_data()
    styles = data.get('style_references', [])
    
    initial_count = len(styles)
    styles = [style for style in styles if style.get('id') != style_id]
    
    if len(styles) < initial_count:
        # 保存到文件
        data['style_references'] = styles
        save_style_data(data)
        
        print(f"✅ 风格参考已删除：{style_id}")
        return True
    
    print(f"❌ 错误：找不到ID为 '{style_id}' 的风格参考")
    return False


def generate_style_report(style_id: str, output_format: str = 'json') -> str:
    """
    生成风格参考报告
    
    Args:
        style_id: 风格ID
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    style = get_style_by_id(style_id)
    
    if not style:
        print(f"❌ 错误：找不到ID为 '{style_id}' 的风格参考")
        return ""
    
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 风格参考报告：{style.get('name')} ({style.get('name_zh')})

## 基本信息
- **风格ID**：{style.get('id')}
- **英文名称**：{style.get('name')}
- **中文名称**：{style.get('name_zh')}
- **创建时间**：{style.get('created_at')}
- **更新时间**：{style.get('updated_at')}

## 风格描述
- **英文描述**：{style.get('description')}
- **中文描述**：{style.get('description_zh')}

## 关键特征
"""
        for i, feature in enumerate(style.get('key_features', [])):
            report_content += f"{i+1}. {feature}\n"
        
        report_content += f"\n## 关键词\n"
        for i, keyword in enumerate(style.get('keywords', [])):
            report_content += f"- {keyword}\n"
        
        report_content += f"\n## 参考图像\n"
        for i, image in enumerate(style.get('reference_images', [])):
            report_content += f"- {image}\n"
        
        report_content += f"\n## 应用场景\n"
        for i, scenario in enumerate(style.get('application_scenarios', [])):
            report_content += f"- {scenario}\n"
        
        report_content += f"\n## Prompt模板\n"
        for i, template in enumerate(style.get('prompt_templates', [])):
            report_content += f"- {template}\n"
        
        report_content += f"\n## 标签\n"
        for i, tag in enumerate(style.get('tags', [])):
            report_content += f"- {tag}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'style_reference',
            'generated_at': datetime.now().isoformat(),
            'style': style
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'style_reference_report_{style_id}_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'style_reference_report_{style_id}_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 风格参考报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='风格管理工具（增强版）')
    parser.add_argument('--list', action='store_true', help='列出所有风格参考')
    parser.add_argument('--add', type=str, help='添加风格参考（指定风格名称）')
    parser.add_argument('--description', type=str, help='风格描述（用于添加风格参考）')
    parser.add_argument('--reference-images', type=str, nargs='+', help='参考图像列表（用于添加风格参考）')
    parser.add_argument('--tags', type=str, nargs='+', help='标签列表（用于添加风格参考）')
    parser.add_argument('--search', type=str, help='搜索风格参考（指定关键词）')
    parser.add_argument('--update', type=str, help='更新风格参考（指定风格ID）')
    parser.add_argument('--update-fields', type=str, help='要更新的字段JSON字符串或文件路径（用于更新风格参考）')
    parser.add_argument('--delete', type=str, help='删除风格参考（指定风格ID）')
    parser.add_argument('--generate-report', type=str, help='生成风格参考报告（指定风格ID）')
    parser.add_argument('--output-format', type=str, choices=['json', 'markdown'], default='json', 
                        help='输出格式（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_styles()
        return
    
    if args.add:
        if not args.description:
            print("❌ 错误：添加风格参考需要指定风格描述（使用 --description）")
            parser.print_help()
            return
        
        print(f"🔍 正在添加风格参考：{args.add}")
        
        reference_images = args.reference_images if args.reference_images else None
        tags = args.tags if args.tags else None
        
        new_style = add_style_reference(args.add, args.description, reference_images, tags)
        
        if args.generate_report:
            print(f"📝 正在生成风格参考报告...")
            report_file = generate_style_report(new_style.get('id'), args.output_format)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.search:
        print(f"🔍 正在搜索风格参考：{args.search}")
        
        results = search_style_references(args.search)
        
        print(f"  搜索到 {len(results)} 个风格参考")
        
        if results:
            print("  结果：")
            for i, result in enumerate(results):
                print(f"    {i+1}. {result.get('id')}: {result.get('name')} ({result.get('name_zh')})")
        return
    
    if args.update:
        print(f"🔍 正在更新风格参考：{args.update}")
        
        if not args.update_fields:
            print("❌ 错误：更新风格参考需要指定要更新的字段（使用 --update-fields）")
            parser.print_help()
            return
        
        # 获取要更新的字段
        update_fields = {}
        if os.path.exists(args.update_fields):
            with open(args.update_fields, 'r', encoding='utf-8') as f:
                update_fields = json.load(f)
        else:
            try:
                update_fields = json.loads(args.update_fields)
            except:
                print(f"❌ 错误：无法解析更新字段 - {args.update_fields}")
                return
        
        updated_style = update_style_reference(args.update, **update_fields)
        
        if updated_style:
            print(f"  更新后的风格参考：{updated_style.get('name')}")
            
            if args.generate_report:
                print(f"📝 正在生成风格参考报告...")
                report_file = generate_style_report(updated_style.get('id'), args.output_format)
                if report_file:
                    print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.delete:
        print(f"🔍 正在删除风格参考：{args.delete}")
        
        success = delete_style_reference(args.delete)
        
        if success:
            print(f"  删除成功")
        return
    
    if args.generate_report:
        print(f"🔍 正在生成风格参考报告：{args.generate_report}")
        
        report_file = generate_style_report(args.generate_report, args.output_format)
        
        if report_file:
            print(f"  报告已生成：{report_file}")
        return
    
    # 默认：列出所有风格或显示帮助
    print("❌ 错误：请指定操作（--list、--add、--search、--update、--delete、--generate-report）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
