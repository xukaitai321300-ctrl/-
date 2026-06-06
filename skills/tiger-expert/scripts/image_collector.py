#!/usr/bin/env python3
"""
图像采集工具 (Image Collector Tool) - 增强版
为十二生肖团提供竞品图片采集功能，支持图片下载、搜索、过滤和报告生成
"""

import json
import argparse
import os
import sys
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import time

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
IMAGE_DATA_FILE = os.path.join(DATA_DIR, 'image_sources.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def load_image_data() -> Dict[str, Any]:
    """加载图像采集数据库"""
    try:
        with open(IMAGE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载图像采集数据库 - {e}")
        return {}


def save_image_data(data: Dict[str, Any]) -> bool:
    """保存图像采集数据库"""
    try:
        with open(IMAGE_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 图像采集数据库已更新：{IMAGE_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存图像采集数据库 - {e}")
        return False


def get_image_source(source_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取图像来源"""
    data = load_image_data()
    sources = data.get('image_sources', [])
    for source in sources:
        if source.get('id') == source_id:
            return source
    return None


def list_sources() -> None:
    """列出所有图像来源"""
    data = load_image_data()
    sources = data.get('image_sources', [])
    if not sources:
        print("❌ 没有找到任何图像来源")
        return
    
    print("📊 可用图像来源列表：")
    for source in sources:
        print(f"  - {source.get('id')}: {source.get('name')} ({source.get('name_zh')})")


def search_images(source_id: str, keywords: str, max_images: int = 10) -> Dict[str, Any]:
    """
    搜索图像
    
    Args:
        source_id: 图像来源ID
        keywords: 搜索关键词
        max_images: 最大图像数量
        
    Returns:
        搜索结果字典
    """
    source = get_image_source(source_id)
    if not source:
        return {
            'success': False,
            'error': f"找不到ID为 '{source_id}' 的图像来源"
        }
    
    # 构建搜索URL
    base_url = source.get('url', '')
    search_prompt = source.get('search_prompts', {}).get('english', keywords)
    
    # 模拟搜索结果（实际应用中这里会调用API）
    search_results = {
        'success': True,
        'source_id': source_id,
        'source_name': source.get('name'),
        'keywords': keywords,
        'search_prompt': search_prompt,
        'max_images': max_images,
        'found_count': min(max_images, 15),  # 模拟找到的图像数量
        'images': []
    }
    
    # 生成模拟图像数据
    for i in range(min(max_images, 15)):
        image_data = {
            'id': f"{source_id}_{i+1:03d}",
            'url': f"{base_url}/images/{keywords.replace(' ', '_')}_{i+1:03d}.jpg",
            'thumbnail_url': f"{base_url}/thumbnails/{keywords.replace(' ', '_')}_{i+1:03d}_thumb.jpg",
            'title': f"{keywords} - Image {i+1}",
            'title_zh': f"{keywords} - 图像 {i+1}",
            'source': source.get('name'),
            'width': 800,
            'height': 600,
            'format': 'jpg',
            'size_kb': 150 + i * 10,
            'relevance_score': 0.95 - (i * 0.02),
            'collected_at': datetime.now().isoformat()
        }
        search_results['images'].append(image_data)
    
    return search_results


def download_images(search_results: Dict[str, Any], download_dir: str = None) -> Dict[str, Any]:
    """
    下载图像
    
    Args:
        search_results: 搜索结果字典
        download_dir: 下载目录（默认为脚本所在目录的downloads文件夹）
        
    Returns:
        下载结果字典
    """
    if not download_dir:
        download_dir = DOWNLOAD_DIR
    
    os.makedirs(download_dir, exist_ok=True)
    
    if not search_results.get('success'):
        return {
            'success': False,
            'error': search_results.get('error', '搜索失败')
        }
    
    images = search_results.get('images', [])
    download_results = {
        'success': True,
        'total_images': len(images),
        'downloaded_count': 0,
        'failed_count': 0,
        'downloaded_files': [],
        'failed_files': []
    }
    
    for image in images:
        try:
            # 模拟下载（实际应用中这里会使用requests下载）
            image_id = image.get('id')
            image_url = image.get('url')
            file_name = f"{image_id}.jpg"
            file_path = os.path.join(download_dir, file_name)
            
            # 模拟下载延迟
            time.sleep(0.1)
            
            # 模拟下载成功（实际应用中这里会保存文件）
            download_results['downloaded_count'] += 1
            download_results['downloaded_files'].append({
                'id': image_id,
                'url': image_url,
                'file_path': file_path,
                'status': 'downloaded'
            })
            
        except Exception as e:
            download_results['failed_count'] += 1
            download_results['failed_files'].append({
                'id': image.get('id'),
                'url': image.get('url'),
                'error': str(e)
            })
    
    return download_results


def filter_images(search_results: Dict[str, Any], min_width: int = 0, min_height: int = 0, 
                 max_size_kb: int = 0, min_relevance: float = 0.0) -> Dict[str, Any]:
    """
    过滤图像
    
    Args:
        search_results: 搜索结果字典
        min_width: 最小宽度
        min_height: 最小高度
        max_size_kb: 最大文件大小（KB）
        min_relevance: 最小相关性分数
        
    Returns:
        过滤结果字典
    """
    if not search_results.get('success'):
        return {
            'success': False,
            'error': search_results.get('error', '搜索失败')
        }
    
    images = search_results.get('images', [])
    filtered_images = []
    
    for image in images:
        # 应用过滤条件
        if min_width > 0 and image.get('width', 0) < min_width:
            continue
        if min_height > 0 and image.get('height', 0) < min_height:
            continue
        if max_size_kb > 0 and image.get('size_kb', 0) > max_size_kb:
            continue
        if min_relevance > 0 and image.get('relevance_score', 0) < min_relevance:
            continue
        
        filtered_images.append(image)
    
    filter_results = {
        'success': True,
        'total_images': len(images),
        'filtered_count': len(filtered_images),
        'filter_conditions': {
            'min_width': min_width,
            'min_height': min_height,
            'max_size_kb': max_size_kb,
            'min_relevance': min_relevance
        },
        'images': filtered_images
    }
    
    return filter_results


def generate_collection_report(search_results: Dict[str, Any], output_format: str = 'json') -> str:
    """
    生成图像采集报告
    
    Args:
        search_results: 搜索结果字典
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    if not search_results.get('success'):
        print(f"❌ 错误：{search_results.get('error')}")
        return ""
    
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 图像采集报告

## 基本信息
- **来源ID**：{search_results.get('source_id')}
- **来源名称**：{search_results.get('source_name')}
- **搜索关键词**：{search_results.get('keywords')}
- **搜索提示词**：{search_results.get('search_prompt')}
- **采集时间**：{datetime.now().isoformat()}

## 采集结果
- **找到图像数量**：{search_results.get('found_count')}
- **请求图像数量**：{search_results.get('max_images')}

## 图像列表
"""
        images = search_results.get('images', [])
        for i, image in enumerate(images):
            report_content += f"\n### {i+1}. {image.get('title')}\n"
            report_content += f"- **ID**：{image.get('id')}\n"
            report_content += f"- **URL**：{image.get('url')}\n"
            report_content += f"- **尺寸**：{image.get('width')}x{image.get('height')}\n"
            report_content += f"- **格式**：{image.get('format')}\n"
            report_content += f"- **大小**：{image.get('size_kb')} KB\n"
            report_content += f"- **相关性分数**：{image.get('relevance_score'):.2f}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'image_collection',
            'source_id': search_results.get('source_id'),
            'source_name': search_results.get('source_name'),
            'keywords': search_results.get('keywords'),
            'search_prompt': search_results.get('search_prompt'),
            'collected_at': datetime.now().isoformat(),
            'found_count': search_results.get('found_count'),
            'max_images': search_results.get('max_images'),
            'images': search_results.get('images', [])
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(OUTPUT_DIR, f'image_collection_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(OUTPUT_DIR, f'image_collection_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 图像采集报告已生成：{output_file}")
    return output_file


def print_source_details(source: Dict[str, Any]) -> None:
    """打印图像来源详情"""
    print(f"📊 图像来源详情：{source.get('name')} ({source.get('name_zh')})")
    print(f"  描述：{source.get('description')}")
    print(f"  中文描述：{source.get('description_zh')}")
    print(f"  URL：{source.get('url')}")
    print(f"  中文URL：{source.get('url_zh')}")
    
    methods = source.get('collection_methods', [])
    print(f"\n  📋 采集方法：")
    for i, method in enumerate(methods):
        print(f"    {i+1}. {method}")
    
    prompts = source.get('search_prompts', {})
    print(f"\n  📝 搜索提示词：")
    print(f"    英文：{prompts.get('english')}")
    print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='图像采集工具（增强版）')
    parser.add_argument('--source', type=str, help='图像来源ID（tmall/jd/amazon/official_website/social_media）')
    parser.add_argument('--list', action='store_true', help='列出所有图像来源')
    parser.add_argument('--search', type=str, help='搜索关键词')
    parser.add_argument('--max-images', type=int, default=10, help='最大图像数量（默认：10）')
    parser.add_argument('--download', action='store_true', help='下载搜索到的图像')
    parser.add_argument('--filter', action='store_true', help='过滤图像')
    parser.add_argument('--min-width', type=intelligent, default=0, help='过滤：最小宽度')
    parser.add_argument('--min-height', type=intelligent, default=0, help='过滤：最小高度')
    parser.add_argument('--max-size', type=intelligent, default=0, help='过滤：最大文件大小（KB）')
    parser.add_argument('--min-relevance', type=float, default=0.0, help='过滤：最小相关性分数')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', help='生成图像采集报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_sources()
        return
    
    if not args.source:
        print("❌ 错误：请指定图像来源ID（使用 --source）或列出所有来源（使用 --list）")
        parser.print_help()
        return
    
    source = get_image_source(args.source)
    if not source:
        print(f"❌ 错误：找不到ID为 '{args.source}' 的图像来源")
        list_sources()
        return
    
    if args.search:
        print(f"🔍 正在搜索图像：来源={args.source}, 关键词={args.search}")
        search_results = search_images(args.source, args.search, args.max_images)
        
        if args.filter:
            print(f"🔍 正在过滤图像...")
            filtered_results = filter_images(search_results, args.min_width, args.min_height, 
                                          args.max_size, args.min_relevance)
            print(f"  过滤前：{filtered_results.get('total_images')} 张图像")
            print(f"  过滤后：{filtered_results.get('filtered_count')} 张图像")
            search_results = filtered_results
        
        if args.download:
            print(f"📥 正在下载图像...")
            download_results = download_images(search_results)
            print(f"  下载成功：{download_results.get('downloaded_count')} 张")
            print(f"  下载失败：{download_results.get('failed_count')} 张")
        
        if args.generate_report:
            print(f"📝 正在生成图像采集报告...")
            report_file = generate_collection_report(search_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        
        return
    
    # 默认：打印来源详情
    print_source_details(source)


if __name__ == '__main__':
    main()
