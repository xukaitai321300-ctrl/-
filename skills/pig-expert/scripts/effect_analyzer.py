#!/usr/bin/env python3
"""
效果分析工具 (Effect Analyzer) - 增强版
为十二生肖团提供效果分析功能，支持Prompt与风格一致性分析、生图效果分析和报告生成
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
STYLE_DATA_FILE = os.path.join(DATA_DIR, 'style_references.json')
MAPPING_DATA_FILE = os.path.join(DATA_DIR, 'style_prompt_mapping.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_style_data() -> Dict[str, Any]:
    """加载风格参考数据库"""
    try:
        with open(STYLE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载风格参考数据库 - {e}")
        return {}

def load_mapping_data() -> Dict[str, Any]:
    """加载风格-Prompt映射数据库"""
    try:
        with open(MAPPING_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载风格-Prompt映射数据库 - {e}")
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


def get_style_reference(style_id: str) -> Optional[Dict[str, Any]]:
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


def analyze_prompt_style_consistency(prompt: str, style_id: str) -> Dict[str, Any]:
    """
    分析Prompt与风格的一致性
    
    Args:
        prompt: Prompt字符串
        style_id: 风格ID
        
    Returns:
        分析结果字典
    """
    # 获取风格信息
    style_info = get_style_reference(style_id)
    if not style_info:
        return {
            'success': False,
            'error': f"找不到ID为 '{style_id}' 的风格参考"
        }
    
    # 模拟一致性分析（实际应用中会调用NLP模型）
    analysis_result = {
        'success': True,
        'analysis_type': 'prompt_style_consistency',
        'analysis_time': datetime.now().isoformat(),
        'prompt': prompt,
        'style_id': style_id,
        'style_name': style_info.get('name'),
        'style_name_zh': style_info.get('name_zh'),
        'keyword_matches': [],
        'feature_matches': [],
        'keyword_match_rate': 0.0,
        'feature_match_rate': 0.0,
        'consistency_score': 0.0,
        'consistency_level': '低',  # 高、中、低
        'issues': [],
        'suggestions': []
    }
    
    # 检查关键词匹配
    prompt_lower = prompt.lower()
    keywords = style_info.get('keywords', [])
    
    for keyword in keywords:
        if keyword.lower() in prompt_lower:
            analysis_result['keyword_matches'].append(keyword)
    
    # 检查特征匹配
    key_features = style_info.get('key_features', [])
    
    for feature in key_features:
        if feature.lower() in prompt_lower:
            analysis_result['feature_matches'].append(feature)
    
    # 计算一致性分数
    keyword_score = len(analysis_result['keyword_matches']) / max(len(keywords), 1)
    feature_score = len(analysis_result['feature_matches']) / max(len(key_features), 1)
    
    analysis_result['keyword_match_rate'] = keyword_score
    analysis_result['feature_match_rate'] = feature_score
    analysis_result['consistency_score'] = (keyword_score + feature_score) / 2
    
    # 确定一致性等级
    if analysis_result['consistency_score'] >= 0.8:
        analysis_result['consistency_level'] = '高'
    elif analysis_result['consistency_score'] >= 0.5:
        analysis_result['consistency_level'] = '中'
    else:
        analysis_result['consistency_level'] = '低'
    
    # 根据分析结果添加问题和建议
    if analysis_result['consistency_score'] < 0.7:
        analysis_result['issues'].append("Prompt与风格一致性较低")
        analysis_result['suggestions'].append("建议在Prompt中加入更多风格关键词和特征")
    
    if keyword_score < 0.6:
        analysis_result['issues'].append("Prompt中风格关键词较少")
        analysis_result['suggestions'].append(f"建议在Prompt中加入以下关键词：{', '.join([kw for kw in keywords if kw not in analysis_result['keyword_matches']])}")
    
    if feature_score < 0.6:
        analysis_result['issues'].append("Prompt中风格特征较少")
        analysis_result['suggestions'].append(f"建议在Prompt中强调以下特征：{', '.join([feat for feat in key_features if feat not in analysis_result['feature_matches']])}")
    
    return analysis_result


def analyze_generation_effect(prompt: str, image_path: str = None) -> Dict[str, Any]:
    """
    分析生图效果
    
    Args:
        prompt: Prompt字符串
        image_path: 图像文件路径（可选）
        
    Returns:
        分析结果字典
    """
    # 模拟生图效果分析（实际应用中会调用图像分析算法）
    analysis_result = {
        'success': True,
        'analysis_type': 'generation_effect',
        'analysis_time': datetime.now().isoformat(),
        'prompt': prompt,
        'image_path': image_path,
        'image_name': os.path.basename(image_path) if image_path and os.path.exists(image_path) else '未知图像',
        'effect_analysis': {
            'clarity': 0.85,  # 清晰度（0-1）
            'style_consistency': 0.78,  # 风格一致性（0-1）
            'detail_richness': 0.82,  # 细节丰富度（0-1）
            'overall_quality': 0.82  # 整体质量（0-1）
        },
        'prompt_optimization_suggestions': [
            "增加细节描述",
            "强调材质质感",
            "优化光照描述"
        ],
        'style_adjustment_suggestions': [
            "调整风格权重",
            "增加风格关键词",
            "参考风格示例图片"
        ],
        'issues': [],
        'suggestions': []
    }
    
    # 根据分析结果添加问题和建议
    if analysis_result['effect_analysis']['overall_quality'] < 0.8:
        analysis_result['issues'].append("生图整体质量较低")
        analysis_result['suggestions'].append("建议优化Prompt，或调整生成参数")
    
    if analysis_result['effect_analysis']['style_consistency'] < 0.7:
        analysis_result['issues'].append("生图与风格一致性较低")
        analysis_result['suggestions'].append("建议调整风格权重，或增加风格关键词")
    
    return analysis_result


def compare_effects(effect1: Dict[str, Any], effect2: Dict[str, Any]) -> Dict[str, Any]:
    """
    比较两个生图效果
    
    Args:
        effect1: 第一个生图效果分析结果
        effect2: 第二个生图效果分析结果
        
    Returns:
        比较结果字典
    """
    # 模拟效果比较（实际应用中会调用比较算法）
    comparison_result = {
        'success': True,
        'comparison_type': 'generation_effect',
        'comparison_time': datetime.now().isoformat(),
        'effect1': effect1,
        'effect2': effect2,
        'score_differences': {},
        'better_effect': None,
        'recommendation': None
    }
    
    # 计算分数差异
    effect1_analysis = effect1.get('effect_analysis', {})
    effect2_analysis = effect2.get('effect_analysis', {})
    
    all_metrics = set(list(effect1_analysis.keys()) + list(effect2_analysis.keys()))
    
    for metric in all_metrics:
        score1 = effect1_analysis.get(metric, 0.0)
        score2 = effect2_analysis.get(metric, 0.0)
        difference = score2 - score1
        
        comparison_result['score_differences'][metric] = {
            'effect1_score': score1,
            'effect2_score': score2,
            'difference': difference,
            'percentage_change': (difference / score1 * 100) if score1 > 0 else 0.0
        }
    
    # 确定哪个效果更好的图像
    overall_score1 = effect1_analysis.get('overall_quality', 0.0)
    overall_score2 = effect2_analysis.get('overall_quality', 0.0)
    
    if overall_score1 > overall_score2:
        comparison_result['better_effect'] = effect1.get('image_name', '未知图像')
        comparison_result['recommendation'] = f"建议使用第一张图像（{effect1.get('image_name', '未知图像')}）"
    elif overall_score2 > overall_score1:
        comparison_result['better_effect'] = effect2.get('image_name', '未知图像')
        comparison_result['recommendation'] = f"建议使用第二张图像（{effect2.get('image_name', '未知图像')}）"
    else:
        comparison_result['better_effect'] = '两者相同'
        comparison_result['recommendation'] = '两张图像质量相当，可以任选一张'
    
    return comparison_result


def generate_effect_report(analysis_results: List[Dict[str, Any]], 
                             output_format: str = 'json') -> str:
    """
    生成效果分析报告
    
    Args:
        analysis_results: 分析结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 效果分析报告#

## 基本信息
- **分析时间**：{datetime.now().isoformat()}
- **分析类型**：Prompt与风格一致性分析、生图效果分析
- **分析结果数量**：{len(analysis_results)}

## 分析结果摘要
"""
        for i, result in enumerate(analysis_results):
            analysis_type = result.get('analysis_type', '未知类型')
            
            if analysis_type == 'prompt_style_consistency':
                report_content += f"\n### {i+1}. Prompt与风格一致性分析\n"
                report_content += f"- **Prompt**：{result.get('prompt', '未知')}\n"
                report_content += f"- **风格名称**：{result.get('style_name', '未知')} ({result.get('style_name_zh', '未知')})\n"
                report_content += f"- **一致性分数**：{result.get('consistency_score', 0.0):.2f}\n"
                report_content += f"- **一致性等级**：{result.get('consistency_level', '未知')}\n"
                report_content += f"- **关键词匹配率**：{result.get('keyword_match_rate', 0.0):.2f}\n"
                report_content += f"- **特征匹配率**：{result.get('feature_match_rate', 0.0):.2f}\n"
                
                if result.get('keyword_matches'):
                    report_content += "\n**匹配的关键词**：\n"
                    for keyword in result.get('keyword_matches', []):
                        report_content += f"- {keyword}\n"
                
                if result.get('feature_matches'):
                    report_content += "\n**匹配的特征**：\n"
                    for feature in result.get('feature_matches', []):
                        report_content += f"- {feature}\n"
            
            elif analysis_type == 'generation_effect':
                report_content += f"\n### {i+1}. 生图效果分析\n"
                report_content += f"- **Prompt**：{result.get('prompt', '未知')}\n"
                report_content += f"- **图像名称**：{result.get('image_name', '未知')}\n"
                
                effect_analysis = result.get('effect_analysis', {})
                if effect_analysis:
                    report_content += f"- **清晰度**：{effect_analysis.get('clarity', 0.0):.2f}\n"
                    report_content += f"- **风格一致性**：{effect_analysis.get('style_consistency', 0.0):.2f}\n"
                    report_content += f"- **细节丰富度**：{effect_analysis.get('detail_richness', 0.0):.2f}\n"
                    report_content += f"- **整体质量**：{effect_analysis.get('overall_quality', 0.0):.2f}\n"
                
                if result.get('prompt_optimization_suggestions'):
                    report_content += "\n**Prompt优化建议**：\n"
                    for suggestion in result.get('prompt_optimization_suggestions', []):
                        report_content += f"- {suggestion}\n"
                
                if result.get('style_adjustment_suggestions'):
                    report_content += "\n**风格调整建议**：\n"
                    for suggestion in result.get('style_adjustment_suggestions', []):
                        report_content += f"- {suggestion}\n"
            
            if result.get('issues'):
                report_content += "\n**问题**：\n"
                for issue in result.get('issues'):
                    report_content += f"- {issue}\n"
            
            if result.get('suggestions'):
                report_content += "\n**建议**：\n"
                for suggestion in result.get('suggestions'):
                    report_content += f"- {suggestion}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **平均一致性分数**：{sum([r.get('consistency_score', 0.0) for r in analysis_results if r.get('analysis_type') == 'prompt_style_consistency']) / len([r for r in analysis_results if r.get('analysis_type') == 'prompt_style_consistency']) if any(r.get('analysis_type') == 'prompt_style_consistency' for r in analysis_results) else 0.0:.2f}\n"
        report_content += f"- **平均整体质量**：{sum([r.get('effect_analysis', {}).get('overall_quality', 0.0) for r in analysis_results if r.get('analysis_type') == 'generation_effect']) / len([r for r in analysis_results if r.get('analysis_type') == 'generation_effect']) if any(r.get('analysis_type') == 'generation_effect' for r in analysis_results) else 0.0:.2f}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'effect_analysis',
            'generated_at': datetime.now().isoformat(),
            'analysis_count': len(analysis_results),
            'analysis_results': analysis_results,
            'summary': {
                'avg_consistency_score': sum([r.get('consistency_score', 0.0) for r in analysis_results if r.get('analysis_type') == 'prompt_style_consistency']) / len([r for r in analysis_results if r.get('analysis_type') == 'prompt_style_consistency']) if any(r.get('analysis_type') == 'prompt_style_consistency' for r in analysis_results) else 0.0,
                'avg_overall_quality': sum([r.get('effect_analysis', {}).get('overall_quality', 0.0) for r in analysis_results if r.get('analysis_type') == 'generation_effect']) / len([r for r in analysis_results if r.get('analysis_type') == 'generation_effect']) if any(r.get('analysis_type') == 'generation_effect' for r in analysis_results) else 0.0,
                'total_issues': sum([len(r.get('issues', [])) for r in analysis_results]),
                'total_suggestions': sum([len(r.get('suggestions', [])) for r in analysis_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'effect_analysis_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'effect_analysis_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 效果分析报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='效果分析工具（增强版）')
    parser.add_argument('--analyze-prompt', type=str, help='分析Prompt与风格的一致性（指定Prompt字符串）')
    parser.add_argument('--style', type=str, help='风格ID（用于分析Prompt与风格的一致性）')
    parser.add_argument('--analyze-effect', type=str, help='分析生图效果（指定Prompt字符串）')
    parser.add_argument('--image', type=str, help='图像文件路径（用于分析生图效果）')
    parser.add_argument('--compare-effects', type=str, nargs=2, help='比较两个生图效果（指定两个分析结果JSON文件）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成效果分析报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    analysis_results = []
    
    if args.analyze_prompt:
        if not args.style:
            print("❌ 错误：分析Prompt与风格的一致性需要指定风格ID（使用 --style）")
            parser.print_help()
            return
        
        print(f"🔍 正在分析Prompt与风格的一致性：{args.analyze_prompt}")
        print(f"  风格ID：{args.style}")
        
        analysis_result = analyze_prompt_style_consistency(args.analyze_prompt, args.style)
        
        if analysis_result.get('success'):
            print(f"  一致性分数：{analysis_result.get('consistency_score', 0.0):.2f}")
            print(f"  一致性等级：{analysis_result.get('consistency_level', '未知')}")
            print(f"  关键词匹配率：{analysis_result.get('keyword_match_rate', 0.0):.2f}")
            print(f"  特征匹配率：{analysis_result.get('feature_match_rate', 0.0):.2f}")
            
            analysis_results.append(analysis_result)
        else:
            print(f"  分析失败：{analysis_result.get('error', '未知错误')}")
        
        if args.generate_report:
            print(f"📝 正在生成效果分析报告...")
            report_file = generate_effect_report(analysis_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.analyze_effect:
        print(f"🔍 正在分析生图效果：{args.analyze_effect}")
        
        image_path = args.image if args.image else None
        if image_path:
            print(f"  图像路径：{image_path}")
            if not os.path.exists(image_path):
                print(f"❌ 错误：图像文件不存在 - {image_path}")
                return
        
        analysis_result = analyze_generation_effect(args.analyze_effect, image_path)
        
        if analysis_result.get('success'):
            print(f"  清晰度：{analysis_result.get('effect_analysis', {}).get('clarity', 0.0):.2f}")
            print(f"  风格一致性：{analysis_result.get('effect_analysis', {}).get('style_consistency', 0.0):.2f}")
            print(f"  细节丰富度：{analysis_result.get('effect_analysis', {}).get('detail_richness', 0.0):.2f}")
            print(f"  整体质量：{analysis_result.get('effect_analysis', {}).get('overall_quality', 0.0):.2f}")
            
            analysis_results.append(analysis_result)
        else:
            print(f"  分析失败：{analysis_result.get('error', '未知错误')}")
        
        if args.generate_report:
            print(f"📝 正在生成效果分析报告...")
            report_file = generate_effect_report(analysis_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.compare_effects:
        effect1_file, effect2_file = args.compare_effects
        print(f"🔍 正在比较两个生图效果：{effect1_file} 和 {effect2_file}")
        
        if not os.path.exists(effect1_file):
            print(f"❌ 错误：第一个分析结果文件不存在 - {effect1_file}")
            return
        
        if not os.path.exists(effect2_file):
            print(f"❌ 错误：第二个分析结果文件不存在 - {effect2_file}")
            return
        
        with open(effect1_file, 'r', encoding='utf-8') as f:
            effect1 = json.load(f)
        
        with open(effect2_file, 'r', encoding='utf-8') as f:
            effect2 = json.load(f)
        
        comparison_result = compare_effects(effect1, effect2)
        
        print(f"  比较完成")
        print(f"  更好的图像：{comparison_result.get('better_effect', '未知')}")
        print(f"  建议：{comparison_result.get('recommendation', '未知')}")
        
        if args.generate_report:
            print(f"📝 正在生成效果分析报告...")
            # 创建模拟分析结果列表（用于报告生成）
            mock_analysis_results = [effect1, effect2]
            report_file = generate_effect_report(mock_analysis_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有风格或显示帮助
    if not any([args.analyze_prompt, args.analyze_effect, args.compare_effects]):
        print("❌ 错误：请指定分析类型（--analyze-prompt, --analyze-effect, --compare-effects）")
        parser.print_help()
        return


if __name__ == '__main__':
    main()
