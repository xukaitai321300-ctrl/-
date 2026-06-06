#!/usr/bin/env python3
"""
Prompt生成工具 (Prompt Generator) - 增强版
为十二生肖团提供Prompt生成功能，支持风格化Prompt生成、Prompt变体生成和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import itertools

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
PROMPT_DATA_FILE = os.path.join(DATA_DIR, 'prompt_templates.json')
STYLE_DATA_FILE = os.path.join(DATA_DIR, 'style_references.json')
MATERIAL_DATA_FILE = os.path.join(DATA_DIR, 'material_library.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_prompt_data() -> Dict[str, Any]:
    """加载Prompt模板数据库"""
    try:
        with open(PROMPT_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载Prompt模板数据库 - {e}")
        return {}

def load_style_data() -> Dict[str, Any]:
    """加载风格参考数据库"""
    try:
        with open(STYLE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载风格参考数据库 - {e}")
        return {}

def load_material_data() -> Dict[str, Any]:
    """加载材质素材数据库"""
    try:
        with open(MATERIAL_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载材质素材数据库 - {e}")
        return {}

def save_prompt_data(data: Dict[str, Any]) -> bool:
    """保存Prompt模板数据库"""
    try:
        with open(PROMPT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Prompt模板数据库已更新：{PROMPT_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存Prompt模板数据库 - {e}")
        return False


def get_style_reference(style_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取风格参考"""
    data = load_style_data()
    styles = data.get('style_references', [])
    for style in styles:
        if style.get('id') == style_id:
            return style
    return None


def get_material(material_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取材质"""
    data = load_material_data()
    materials = data.get('materials', [])
    for material in materials:
        if material.get('id') == material_id:
            return material
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


def generate_styled_prompt(product: str, style_id: str, 
                              features: List[str] = None, 
                              materials: List[str] = None) -> Dict[str, Any]:
    """
    生成风格化Prompt
    
    Args:
        product: 产品名称
        style_id: 风格ID
        features: 功能特性列表
        materials: 材质列表
        
    Returns:
        生成结果字典
    """
    if not features:
        features = []
    
    if not materials:
        materials = []
    
    # 获取风格信息
    style_info = get_style_reference(style_id)
    if not style_info:
        return {
            'success': False,
            'error': f"找不到ID为 '{style_id}' 的风格参考"
        }
    
    # 获取材质描述
    material_descriptions = []
    for material_name in materials:
        material = get_material(material_name)
        if material:
            material_descriptions.append(f"{material.get('name')}（{material.get('description', '')}）")
    
    # 生成Prompt
    prompt = f"{style_info.get('name')}风格的{product}，"
    
    if material_descriptions:
        prompt += f"采用{', '.join(material_descriptions)}，"
    
    if features:
        prompt += f"具有{', '.join(features)}等功能，"
    
    prompt += f"{style_info.get('description', '')}的设计风格"
    
    # 生成Prompt变体
    prompt_variants = []
    
    # 变体1：强调材质
    if material_descriptions:
        variant1 = f"{product}，{', '.join(materials)}材质，{style_info.get('name')}风格"
        prompt_variants.append(variant1)
    
    # 变体2：强调功能
    if features:
        variant2 = f"{product}，{', '.join(features)}，{style_info.get('name')}风格"
        prompt_variants.append(variant2)
    
    # 变体3：强调风格
    variant3 = f"{style_info.get('name')}风格的{product}，{style_info.get('description', '')}"
    prompt_variants.append(variant3)
    
    # 创建结果
    result = {
        'success': True,
        'product': product,
        'style_id': style_id,
        'style_name': style_info.get('name'),
        'style_name_zh': style_info.get('name_zh'),
        'features': features,
        'materials': materials,
        'prompt': prompt,
        'prompt_variants': prompt_variants,
        'style_keywords': style_info.get('keywords', []),
        'recommendations': _generate_recommendations(style_info, features, materials),
        'generated_at': datetime.now().isoformat()
    }
    
    return result


def _generate_recommendations(style_info: Dict[str, Any], 
                            features: List[str], materials: List[str]) -> List[str]:
    """生成优化建议"""
    recommendations = []
    
    # 基于风格的建议
    style_name = style_info.get('name')
    if style_name == 'minimalist':
        recommendations.append("强调功能性和实用性")
        recommendations.append("减少装饰元素")
    elif style_name == 'industrial':
        recommendations.append("强调金属质感")
        recommendations.append("突出机械感")
    elif style_name == 'technological':
        recommendations.append("强调智能和未来感")
        recommendations.append("加入科技元素")
    elif style_name == 'natural':
        recommendations.append("强调环保和有机")
        recommendations.append("使用自然材质")
    
    # 基于功能的建议
    if 'lightweight' in features:
        recommendations.append("突出轻量化设计")
    if 'anti-mistouch' in features:
        recommendations.append("强调安全设计")
    if 'car-compatible' in features:
        recommendations.append("强调车载场景适配性")
    
    # 基于材质的建议
    if 'magnesium-alloy' in materials:
        recommendations.append("突出镁合金的轻量化和强度")
    if 'carbon-fiber' in materials:
        recommendations.append("突出碳纤维的高端和科技感")
    if 'PP' in materials:
        recommendations.append("强调PP的食品级安全性")
    
    return recommendations


def generate_prompt_variants(base_prompt: str, num_variants: int = 3) -> Dict[str, Any]:
    """
    生成Prompt变体
    
    Args:
        base_prompt: 基础Prompt
        num_variants: 变体数量
        
    Returns:
        生成结果字典
    """
    # 模拟生成Prompt变体（实际应用中会调用Prompt工程算法）
    variants_result = {
        'success': True,
        'base_prompt': base_prompt,
        'num_variants': num_variants,
        'generation_time': datetime.now().isoformat(),
        'variants': [],
        'recommendation': ''
    }
    
    # 生成变体
    for i in range(num_variants):
        variant = {
            'id': f"variant_{i+1:03d}",
            'prompt': f"{base_prompt} - 变体{i+1}",
            'description': f"这是第{i+1}个变体，强调了不同的方面",
            'focus': ['材质', '功能', '风格'][i % 3]
        }
        variants_result['variants'].append(variant)
    
    # 生成建议
    variants_result['recommendation'] = "建议使用变体1，因为它最平衡"
    
    return variants_result


def optimize_prompt(prompt: str, target_score: float = 85.0) -> Dict[str, Any]:
    """
    优化Prompt
    
    Args:
        prompt: 原始Prompt
        target_score: 目标分数
        
    Returns:
        优化结果字典
    """
    # 模拟优化Prompt（实际应用中会调用优化算法）
    optimization_result = {
        'success': True,
        'original_prompt': prompt,
        'optimized_prompt': f"{prompt} - 优化版",
        'optimization_time': datetime.now().isoformat(),
        'original_score': 78.5,
        'optimized_score': 87.2,
        'improvement': 8.7,  # 分数提升
        'changes': [
            {'type': 'add_keyword', 'keyword': '高清', 'reason': '提高图像清晰度'},
            {'type': 'add_keyword', 'keyword': '细节丰富', 'reason': '提高图像细节丰富度'},
            {'type': 'modify_keyword', 'original': '现代', 'modified': '现代简约', 'reason': '更精准地描述风格'}
        ],
        'issues': [],
        'suggestions': []
    }
    
    # 根据优化结果添加问题和建议
    if optimization_result['optimized_score'] < target_score:
        optimization_result['issues'].append("优化后分数仍低于目标分数")
        optimization_result['suggestions'].append("建议继续优化Prompt，或调整生成参数")
    
    return optimization_result


def generate_prompt_report(prompt_results: List[Dict[str, Any]], 
                             output_format: str = 'json') -> str:
    """
    生成Prompt生成报告
    
    Args:
        prompt_results: 生成结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# Prompt生成报告

## 基本信息
- **生成时间**：{datetime.now().isoformat()}
- **生成Prompt数量**：{len(prompt_results)}
- **生成类型**：风格化Prompt生成、Prompt变体生成、Prompt优化

## 生成结果摘要
"""
        for i, result in enumerate(prompt_results):
            report_content += f"\n### {i+1}. {result.get('product', '未知产品')}\n"
            report_content += f"- **风格**：{result.get('style_name', '未知')} ({result.get('style_name_zh', '未知')})\n"
            report_content += f"- **Prompt**：{result.get('prompt', '未知')}\n"
            report_content += f"- **Prompt变体数量**：{len(result.get('prompt_variants', []))}\n"
            
            if result.get('issues'):
                report_content += "\n**问题**：\n"
                for issue in result.get('issues'):
                    report_content += f"- {issue}\n"
            
            if result.get('recommendations'):
                report_content += "\n**建议**：\n"
                for recommendation in result.get('recommendations'):
                    report_content += f"- {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **平均Prompt长度**：{sum([len(r.get('prompt', '')) for r in prompt_results]) / len(prompt_results):.2f} 字符\n"
        report_content += f"- **平均变体数量**：{sum([len(r.get('prompt_variants', [])) for r in prompt_results]) / len(prompt_results):.2f} 个\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'prompt_generation',
            'generated_at': datetime.now().isoformat(),
            'prompt_count': len(prompt_results),
            'prompt_results': prompt_results,
            'summary': {
                'avg_prompt_length': sum([len(r.get('prompt', '')) for r in prompt_results]) / len(prompt_results),
                'avg_variant_count': sum([len(r.get('prompt_variants', [])) for r in prompt_results]) / len(prompt_results),
                'total_issues': sum([len(r.get('issues', [])) for r in prompt_results]),
                'total_recommendations': sum([len(r.get('recommendations', [])) for r in prompt_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'prompt_generation_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'prompt_generation_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Prompt生成报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Prompt生成工具（增强版）')
    parser.add_argument('--product', type=str, help='产品名称（用于生成风格化Prompt）')
    parser.add_argument('--style', type=str, help='风格ID（用于生成风格化Prompt）')
    parser.add_argument('--features', type=str, nargs='+', help='功能特性列表（用于生成风格化Prompt）')
    parser.add_argument('--materials', type=str, nargs='+', help='材质列表（用于生成风格化Prompt）')
    parser.add_argument('--list-styles', action='store_true', help='列出所有风格参考')
    parser.add_argument('--generate-variants', type=str, help='生成Prompt变体（指定基础Prompt）')
    parser.add_argument('--num-variants', type=int, default=3, help='变体数量（默认：3）')
    parser.add_argument('--optimize', type=str, help='优化Prompt（指定原始Prompt）')
    parser.add_argument('--target-score', type=float, default=85.0, help='目标分数（默认：85.0）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成Prompt生成报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    prompt_results = []
    
    if args.list_styles:
        list_styles()
        return
    
    if args.product and args.style:
        print(f"🔍 正在生成风格化Prompt：产品={args.product}, 风格={args.style}")
        
        features = args.features if args.features else None
        materials = args.materials if args.materials else None
        
        result = generate_styled_prompt(args.product, args.style, features, materials)
        
        if result.get('success'):
            print(f"  生成Prompt：{result.get('prompt')}")
            print(f"  生成Prompt变体数量：{len(result.get('prompt_variants', []))}")
            print(f"  风格关键词数量：{len(result.get('style_keywords', []))}")
            
            if args.generate_report:
                print(f"📝 正在生成Prompt生成报告...")
                report_file = generate_prompt_report([result], args.generate_report)
                if report_file:
                    print(f"✅ 报告已生成：{report_file}")
        else:
            print(f"  生成失败：{result.get('error')}")
        
        return
    
    if args.generate_variants:
        print(f"🔍 正在生成Prompt变体：{args.generate_variants}")
        
        variants_result = generate_prompt_variants(args.generate_variants, args.num_variants)
        
        print(f"  基础Prompt：{variants_result.get('base_prompt')}")
        print(f"  变体数量：{variants_result.get('num_variants')}")
        print(f"  建议：{variants_result.get('recommendation')}")
        
        if args.generate_report:
            print(f"📝 正在生成Prompt生成报告...")
            # 创建一个模拟的生成结果，用于报告生成
            mock_result = {
                'product': '未知产品',
                'style_name': '未知风格',
                'style_name_zh': '未知风格',
                'prompt': variants_result.get('base_prompt'),
                'prompt_variants': [v.get('prompt') for v in variants_result.get('variants', [])],
                'issues': [],
                'recommendations': [variants_result.get('recommendation')]
            }
            report_file = generate_prompt_report([mock_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.optimize:
        print(f"🔍 正在优化Prompt：{args.optimize}")
        
        optimization_result = optimize_prompt(args.optimize, args.target_score)
        
        print(f"  原始Prompt：{optimization_result.get('original_prompt')}")
        print(f"  优化后Prompt：{optimization_result.get('optimized_prompt')}")
        print(f"  原始分数：{optimization_result.get('original_score'):.2f}")
        print(f"  优化后分数：{optimization_result.get('optimized_score'):.2f}")
        print(f"  提升：{optimization_result.get('improvement'):.2f} 分")
        
        if args.generate_report:
            print(f"📝 正在生成Prompt生成报告...")
            # 创建一个模拟的生成结果，用于报告生成
            mock_result = {
                'product': '未知产品',
                'style_name': '未知风格',
                'style_name_zh': '未知风格',
                'prompt': optimization_result.get('optimized_prompt'),
                'prompt_variants': [optimization_result.get('optimized_prompt')],
                'issues': optimization_result.get('issues', []),
                'recommendations': optimization_result.get('suggestions', [])
            }
            report_file = generate_prompt_report([mock_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有风格或显示帮助
    print("❌ 错误：请指定操作（--product 和 --style，或 --generate-variants，或 --optimize）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
