#!/usr/bin/env python3
"""
素材搜索工具 (Material Searcher) - 增强版
为十二生肖团提供材质素材搜索功能，支持关键词搜索、类型搜索、特征搜索和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import re

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
MATERIAL_DATA_FILE = os.path.join(DATA_DIR, 'material_library.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_material_data() -> Dict[str, Any]:
    """加载材质素材数据库"""
    try:
        with open(MATERIAL_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载材质素材数据库 - {e}")
        return {}

def save_material_data(data: Dict[str, Any]) -> bool:
    """保存材质素材数据库"""
    try:
        with open(MATERIAL_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 材质素材数据库已更新：{MATERIAL_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存材质素材数据库 - {e}")
        return False


def get_material(material_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取材质"""
    data = load_material_data()
    materials = data.get('materials', [])
    for material in materials:
        if material.get('id') == material_id:
            return material
    return None


def list_materials() -> None:
    """列出所有材质素材"""
    data = load_material_data()
    materials = data.get('materials', [])
    if not materials:
        print("❌ 没有找到任何材质素材")
        return
    
    print("📊 可用材质素材列表：")
    for material in materials:
        print(f"  - {material.get('id')}: {material.get('name')} ({material.get('name_zh')})")


def search_materials(keyword: str = None, material_type: str = None, 
                      features: List[str] = None, applications: List[str] = None) -> Dict[str, Any]:
    """
    搜索材质素材
    
    Args:
        keyword: 搜索关键词
        material_type: 材质类型（metal, plastic, silicone, composite）
        features: 特征列表（lightweight, durable, heat_resistant等）
        applications: 应用列表（cup_body, lid, seal, handle等）
        
    Returns:
        搜索结果字典
    """
    # 模拟材质素材搜索（实际应用中会调用搜索算法）
    search_result = {
        'success': True,
        'search_time': datetime.now().isoformat(),
        'search_conditions': {
            'keyword': keyword,
            'material_type': material_type,
            'features': features,
            'applications': applications
        },
        'total_count': 0,
        'found_count': 0,
        'materials': []
    }
    
    # 获取所有材质
    data = load_material_data()
    all_materials = data.get('materials', [])
    
    # 搜索匹配的材质
    for material in all_materials:
        match = True
        
        # 关键词搜索
        if keyword:
            if (keyword.lower() not in material.get('name', '').lower() and
                keyword.lower() not in material.get('description', '').lower() and
                not any(keyword.lower() in kw.lower() for kw in material.get('prompt_keywords', []))):
                match = False
        
        # 类型搜索
        if material_type and match:
            if material.get('type') != material_type:
                match = False
        
        # 特征搜索
        if features and match:
            if not any(feature in material.get('features', []) for feature in features):
                match = False
        
        # 应用搜索
        if applications and match:
            if not any(app in material.get('applications', []) for app in applications):
                match = False
        
        # 如果匹配，添加到结果
        if match:
            search_result['materials'].append(material)
    
    # 更新计数
    search_result['total_count'] = len(all_materials)
    search_result['found_count'] = len(search_result['materials'])
    
    return search_result


def compare_materials(material_id1: str, material_id2: str) -> Dict[str, Any]:
    """
    比较两个材质
    
    Args:
        material_id1: 第一个材质ID
        material_id2: 第二个材质ID
        
    Returns:
        比较结果字典
    """
    material1 = get_material(material_id1)
    material2 = get_material(material_id2)
    
    if not material1:
        return {
            'success': False,
            'error': f"找不到ID为 '{material_id1}' 的材质"
        }
    
    if not material2:
        return {
            'success': False,
            'error': f"找不到ID为 '{material_id2}' 的材质"
        }
    
    # 模拟材质比较（实际应用中会调用比较算法）
    comparison_result = {
        'success': True,
        'material1': material1,
        'material2': material2,
        'comparison_time': datetime.now().isoformat(),
        'comparison_results': {
            'weight': {
                'material1': 280.0,  # 模拟重量（g）
                'material2': 250.0,
                'difference': -30.0,  # 差异（g）
                'percentage': -10.7  # 差异百分比（%）
            },
            'cost': {
                'material1': 35.0,  # 模拟成本（元）
                'material2': 45.0,
                'difference': 10.0,  # 差异（元）
                'percentage': 28.6  # 差异百分比（%）
            },
            'durability': {
                'material1': 85.0,  # 模拟耐久性分数（0-100）
                'material2': 90.0,
                'difference': 5.0,  # 差异（分）
                'percentage': 5.9  # 差异百分比（%）
            },
            'heat_insulation': {
                'material1': 88.0,  # 模拟保温性能分数（0-100）
                'material2': 85.0,
                'difference': -3.0,  # 差异（分）
                'percentage': -3.4  # 差异百分比（%）
            }
        },
        'recommendation': '',
        'issues': [],
        'suggestions': []
    }
    
    # 生成建议
    if comparison_result['comparison_results']['weight']['difference'] < 0:
        comparison_result['recommendation'] = f"建议使用{material2.get('name')}，因为它更轻"
    elif comparison_result['comparison_results']['cost']['difference'] > 0:
        comparison_result['recommendation'] = f"建议使用{material1.get('name')}，因为它更便宜"
    elif comparison_result['comparison_results']['durability']['difference'] > 0:
        comparison_result['recommendation'] = f"建议使用{material2.get('name')}，因为它更耐用"
    else:
        comparison_result['recommendation'] = f"建议使用{material1.get('name')}，综合性能更好"
    
    return comparison_result


def generate_material_report(search_results: List[Dict[str, Any]], 
                              output_format: str = 'json') -> str:
    """
    生成材质素材搜索报告
    
    Args:
        search_results: 搜索结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 材质素材搜索报告

## 基本信息
- **搜索时间**：{datetime.now().isoformat()}
- **搜索条件**：关键词、类型、特征、应用
- **找到材质数量**：{sum([r.get('found_count', 0) for r in search_results])}
- **总材质数量**：{sum([r.get('total_count', 0) for r in search_results])}

## 搜索结果摘要
"""
        for i, result in enumerate(search_results):
            report_content += f"\n### {i+1}. 搜索条件 {i+1}\n"
            report_content += f"- **关键词**：{result.get('search_conditions', {}).get('keyword', '无')}\n"
            report_content += f"- **类型**：{result.get('search_conditions', {}).get('material_type', '无')}\n"
            report_content += f"- **特征**：{', '.join(result.get('search_conditions', {}).get('features', []))}\n"
            report_content += f"- **应用**：{', '.join(result.get('search_conditions', {}).get('applications', []))}\n"
            report_content += f"- **找到数量**：{result.get('found_count', 0)}\n"
            
            if result.get('materials'):
                report_content += "\n**找到的材质**：\n"
                for j, material in enumerate(result.get('materials', [])[:3]):  # 只显示前3个
                    report_content += f"- {material.get('name', '')}（{material.get('name_zh', '')}）：{material.get('description', '')}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总找到材质数量**：{sum([r.get('found_count', 0) for r in search_results])}\n"
        report_content += f"- **总材质数量**：{sum([r.get('total_count', 0) for r in search_results])}\n"
        report_content += f"- **找到率**：{sum([r.get('found_count', 0) for r in search_results]) / sum([r.get('total_count', 0) for r in search_results]) * 100:.2f}%\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'material_search',
            'generated_at': datetime.now().isoformat(),
            'search_count': len(search_results),
            'search_results': search_results,
            'summary': {
                'total_found': sum([r.get('found_count', 0) for r in search_results]),
                'total_materials': sum([r.get('total_count', 0) for r in search_results]),
                'found_rate': sum([r.get('found_count', 0) for r in search_results]) / sum([r.get('total_count', 0) for r in search_results]) * 100 if sum([r.get('total_count', 0) for r in search_results]) > 0 else 0
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'material_search_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'material_search_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 材质素材搜索报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='素材搜索工具（增强版）')
    parser.add_argument('--list', action='store_true', help='列出所有材质素材')
    parser.add_argument('--search', type=str, help='搜索材质素材（指定关键词）')
    parser.add_argument('--type', type=str, choices=['metal', 'plastic', 'silicone', 'composite'], 
                        help='材质类型（metal, plastic, silicone, composite）')
    parser.add_argument('--features', type=str, nargs='+', help='特征列表（lightweight, durable, heat_resistant等）')
    parser.add_argument('--applications', type=str, nargs='+', help='应用列表（cup_body, lid, seal, handle等）')
    parser.add_argument('--compare', type=str, nargs=2, help='比较两个材质（指定两个材质ID）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成材质素材搜索报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_materials()
        return
    
    search_results = []
    
    if args.search or args.type or args.features or args.applications:
        print(f"🔍 正在搜索材质素材...")
        
        keyword = args.search if args.search else None
        material_type = args.type if args.type else None
        features = args.features if args.features else None
        applications = args.applications if args.applications else None
        
        search_result = search_materials(keyword, material_type, features, applications)
        search_results.append(search_result)
        
        print(f"  搜索条件：关键词={keyword}, 类型={material_type}, 特征={features}, 应用={applications}")
        print(f"  找到材质数量：{search_result.get('found_count', 0)}")
        print(f"  总材质数量：{search_result.get('total_count', 0)}")
        
        if args.generate_report:
            print(f"📝 正在生成材质素材搜索报告...")
            report_file = generate_material_report([search_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.compare:
        material_id1, material_id2 = args.compare
        print(f"🔍 正在比较材质：{material_id1} 和 {material_id2}")
        
        comparison_result = compare_materials(material_id1, material_id2)
        
        if comparison_result.get('success'):
            print(f"  比较结果：")
            print(f"  材质1：{comparison_result.get('material1', {}).get('name', '未知')}")
            print(f"  材质2：{comparison_result.get('material2', {}).get('name', '未知')}")
            print(f"  建议：{comparison_result.get('recommendation', '')}")
        else:
            print(f"  比较失败：{comparison_result.get('error', '')}")
        
        if args.generate_report:
            print(f"📝 正在生成材质素材搜索报告...")
            # 创建一个模拟的搜索结果，用于报告生成
            mock_search_result = {
                'found_count': 2,
                'total_count': 10,
                'materials': [comparison_result.get('material1', {}), comparison_result.get('material2', {})]
            }
            report_file = generate_material_report([mock_search_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有材质或显示帮助
    print("❌ 错误：请指定搜索条件（--search, --type, --features, --applications）或比较材质（--compare）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
