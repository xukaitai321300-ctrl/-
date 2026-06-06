#!/usr/bin/env python3
"""
图像评审工具 (Image Review Tool) - 增强版
为十二生肖团提供AI生图评审功能，支持图像质量评审、风格一致性评审、产品特征准确性评审和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import base64
from io import BytesIO

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CRITERIA_DATA_FILE = os.path.join(DATA_DIR, 'review_criteria.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_criteria_data() -> Dict[str, Any]:
    """加载评审标准数据库"""
    try:
        with open(CRITERIA_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载评审标准数据库 - {e}")
        return {}

def save_criteria_data(data: Dict[str, Any]) -> bool:
    """保存评审标准数据库"""
    try:
        with open(CRITERIA_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 评审标准数据库已更新：{CRITERIA_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存评审标准数据库 - {e}")
        return False


def get_review_criterion(criterion_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取评审标准"""
    data = load_criteria_data()
    criteria = data.get('review_criteria', [])
    for criterion in criteria:
        if criterion.get('id') == criterion_id:
            return criterion
    return None


def list_criteria() -> None:
    """列出所有评审标准"""
    data = load_criteria_data()
    criteria = data.get('review_criteria', [])
    if not criteria:
        print("❌ 没有找到任何评审标准")
        return
    
    print("📊 可用评审标准列表：")
    for criterion in criteria:
        print(f"  - {criterion.get('id')}: {criterion.get('name')} ({criterion.get('name_zh')})")


def review_image_quality(image_path: str, prompt: str = None, style: str = None) -> Dict[str, Any]:
    """
    评审图像质量
    
    Args:
        image_path: 图像文件路径
        prompt: 提示词
        style: 风格
        
    Returns:
        评审结果字典
    """
    # 模拟图像质量评审（实际应用中会调用图像质量评估算法）
    review_result = {
        'success': True,
        'image_path': image_path,
        'image_name': os.path.basename(image_path),
        'prompt': prompt,
        'style': style,
        'review_time': datetime.now().isoformat(),
        'scores': {
            '图像质量': 85.5,  # 模拟评分（0-100）
            '风格一致性': 78.2,
            '产品特征准确性': 88.0,
            '提示词遵从度': 82.5,
            '创新性': 75.0
        },
        'details': {
            '图像质量': '图像清晰，细节丰富，真实感强',
            '风格一致性': '风格与参考基本一致的，但某些细节有差异',
            '产品特征准确性': '产品特征准确，符合设计要求',
            '提示词遵从度': '基本遵从提示词要求，但某些细节有差异',
            '创新性': '设计有一定创新性，但不够突出'
        },
        'total_score': 0.0,
        'pass_threshold': 80.0,  # 通过阈值
        'is_passed': False,
        'recommendations': [],
        'issues': [],
        'suggestions': []
    }
    
    # 计算总分（加权平均）
    data = load_criteria_data()
    criteria = data.get('review_criteria', [])
    
    total_weight = 0.0
    weighted_score = 0.0
    
    for criterion in criteria:
        criterion_name = criterion.get('name')
        weight = criterion.get('weight', 0.0)
        
        if criterion_name in review_result['scores']:
            weighted_score += review_result['scores'][criterion_name] * weight
            total_weight += weight
    
    if total_weight > 0:
        review_result['total_score'] = weighted_score / total_weight
    else:
        review_result['total_score'] = 0.0
    
    # 确定是否通过
    review_result['is_passed'] = review_result['total_score'] >= review_result['pass_threshold']
    
    # 生成建议
    for criterion_name, score in review_result['scores'].items():
        if score < 80:
            if criterion_name == '图像质量':
                review_result['recommendations'].append('提高图像清晰度和细节丰富度')
                review_result['issues'].append('图像质量分数较低')
            elif criterion_name == '风格一致性':
                review_result['recommendations'].append('加强风格特征，提高与风格参考的一致性')
                review_result['issues'].append('风格一致性分数较低')
            elif criterion_name == '产品特征准确性':
                review_result['recommendations'].append('确保产品特征准确，符合设计要求')
                review_result['issues'].append('产品特征准确性分数较低')
            elif criterion_name == '提示词遵从度':
                review_result['recommendations'].append('优化提示词，提高遵从度')
                review_result['issues'].append('提示词遵从度分数较低')
            elif criterion_name == '创新性':
                review_result['recommendations'].append('增强设计创新性，突出设计亮点')
                review_result['issues'].append('创新性分数较低')
    
    # 如果没有问题，添加通用建议
    if not review_result['issues']:
        review_result['recommendations'].append('图像质量良好，可以输出')
        review_result['suggestions'].append('建议进行最终检查后输出')
    
    return review_result


def batch_review(image_paths: List[str], prompt: str = None, style: str = None) -> Dict[str, Any]:
    """
    批量评审图像
    
    Args:
        image_paths: 图像文件路径列表
        prompt: 提示词
        style: 风格
        
    Returns:
        批量评审结果字典
    """
    batch_result = {
        'success': True,
        'total_images': len(image_paths),
        'reviewed_count': 0,
        'passed_count': 0,
        'failed_count': 0,
        'review_results': [],
        'batch_review_time': datetime.now().isoformat()
    }
    
    for image_path in image_paths:
        review_result = review_image_quality(image_path, prompt, style)
        batch_result['review_results'].append(review_result)
        batch_result['reviewed_count'] += 1
        
        if review_result.get('is_passed'):
            batch_result['passed_count'] += 1
        else:
            batch_result['failed_count'] += 1
    
    return batch_result


def compare_reviews(review1: Dict[str, Any], review2: Dict[str, Any]) -> Dict[str, Any]:
    """
    比较两个评审结果
    
    Args:
        review1: 第一个评审结果
        review2: 第二个评审结果
        
    Returns:
        比较结果字典
    """
    comparison_result = {
        'success': True,
        'review1_image': review1.get('image_name', '未知图像'),
        'review2_image': review2.get('image_name', '未知图像'),
        'comparison_time': datetime.now().isoformat(),
        'score_differences': {},
        'better_image': None,
        'recommendation': None
    }
    
    # 计算分数差异
    scores1 = review1.get('scores', {})
    scores2 = review2.get('scores', {})
    
    all_criteria = set(list(scores1.keys()) + list(scores2.keys()))
    
    for criterion in all_criteria:
        score1 = scores1.get(criterion, 0.0)
        score2 = scores2.get(criterion, 0.0)
        difference = score2 - score1
        
        comparison_result['score_differences'][criterion] = {
            'review1_score': score1,
            'review2_score': score2,
            'difference': difference,
            'percentage_change': (difference / score1 * 100) if score1 > 0 else 0.0
        }
    
    # 确定哪个图像更好
    total_score1 = review1.get('total_score', 0.0)
    total_score2 = review2.get('total_score', 0.0)
    
    if total_score1 > total_score2:
        comparison_result['better_image'] = review1.get('image_name', '未知图像')
        comparison_result['recommendation'] = f"建议使用第一张图像（{review1.get('image_name', '未知图像')}）"
    elif total_score2 > total_score1:
        comparison_result['better_image'] = review2.get('image_name', '未知图像')
        comparison_result['recommendation'] = f"建议使用第二张图像（{review2.get('image_name', '未知图像')}）"
    else:
        comparison_result['better_image'] = '两者相同'
        comparison_result['recommendation'] = '两张图像质量相当，可以任选一张'
    
    return comparison_result


def generate_review_report(review_results: List[Dict[str, Any]], 
                            output_format: str = 'json') -> str:
    """
    生成图像评审报告
    
    Args:
        review_results: 评审结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 图像评审报告

## 基本信息
- **评审时间**：{datetime.now().isoformat()}
- **评审图像数量**：{len(review_results)}
- **通过数量**：{sum([1 for r in review_results if r.get('is_passed')])}
- **未通过数量**：{sum([1 for r in review_results if not r.get('is_passed')])}

## 评审结果摘要
"""
        for i, result in enumerate(review_results):
            report_content += f"\n### {i+1}. {result.get('image_name', '未知图像')}\n"
            report_content += f"- **总分**：{result.get('total_score', 0):.2f}/100\n"
            report_content += f"- **是否通过**：{'✅ 是' if result.get('is_passed') else '❌ 否'}\n"
            report_content += f"- **通过阈值**：{result.get('pass_threshold', 0):.2f}/100\n"
            
            report_content += "\n**各项分数**：\n"
            for criterion, score in result.get('scores', {}).items():
                report_content += f"- **{criterion}**：{score:.2f}/100\n"
            
            if result.get('issues'):
                report_content += "\n**问题**：\n"
                for issue in result.get('issues'):
                    report_content += f"- {issue}\n"
            
            if result.get('recommendations'):
                report_content += "\n**建议**：\n"
                for recommendation in result.get('recommendations'):
                    report_content += f"- {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **平均总分**：{sum([r.get('total_score', 0) for r in review_results]) / len(review_results):.2f}/100\n"
        report_content += f"- **通过率**：{sum([1 for r in review_results if r.get('is_passed')]) / len(review_results) * 100:.2f}%\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'image_review',
            'generated_at': datetime.now().isoformat(),
            'image_count': len(review_results),
            'passed_count': sum([1 for r in review_results if r.get('is_passed')]),
            'failed_count': sum([1 for r in review_results if not r.get('is_passed')]),
            'avg_score': sum([r.get('total_score', 0) for r in review_results]) / len(review_results),
            'pass_rate': sum([1 for r in review_results if r.get('is_passed')]) / len(review_results) * 100,
            'review_results': review_results,
            'summary': {
                'total_issues': sum([len(r.get('issues', [])) for r in review_results]),
                'total_recommendations': sum([len(r.get('recommendations', [])) for r in review_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'image_review_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'image_review_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 图像评审报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='图像评审工具（增强版）')
    parser.add_argument('--image', type=str, help='评审单个图像（指定图像文件路径）')
    parser.add_argument('--prompt', type=str, help='提示词（用于评审）')
    parser.add_argument('--style', type=str, help='风格（用于评审）')
    parser.add_argument('--batch-review', type=str, help='批量评审图像（指定图像目录或文件列表JSON）')
    parser.add_argument('--compare', type=str, nargs=2, help='比较两个评审结果（指定两个评审结果JSON文件）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成图像评审报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.image:
        print(f"🔍 正在评审图像：{args.image}")
        
        if not os.path.exists(args.image):
            print(f"❌ 错误：图像文件不存在 - {args.image}")
            return
        
        review_result = review_image_quality(args.image, args.prompt, args.style)
        
        print(f"  总分：{review_result['total_score']:.2f}/100")
        print(f"  是否通过：{'✅ 是' if review_result['is_passed'] else '❌ 否'}")
        print(f"  通过阈值：{review_result['pass_threshold']:.2f}/100")
        
        if review_result.get('issues'):
            print("  问题：")
            for issue in review_result['issues']:
                print(f"    - {issue}")
        
        if review_result.get('recommendations'):
            print("  建议：")
            for recommendation in review_result['recommendations']:
                print(f"    - {recommendation}")
        
        if args.generate_report:
            print(f"📝 正在生成图像评审报告...")
            report_file = generate_review_report([review_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.batch_review:
        print(f"🔍 正在批量评审图像：{args.batch_review}")
        
        image_paths = []
        
        if os.path.isdir(args.batch_review):
            # 如果是目录，获取目录下所有图像文件
            image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
            for file in os.listdir(args.batch_review):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    image_paths.append(os.path.join(args.batch_review, file))
        elif os.path.exists(args.batch_review):
            # 如果是文件，尝试读取JSON文件列表
            try:
                with open(args.batch_review, 'r', encoding='utf-8') as f:
                    image_paths = json.load(f)
            except:
                print(f"❌ 错误：无法解析图像列表 - {args.batch_review}")
                return
        else:
            print(f"❌ 错误：图像目录或文件不存在 - {args.batch_review}")
            return
        
        if not image_paths:
            print(f"❌ 错误：没有找到任何图像文件")
            return
        
        batch_result = batch_review(image_paths, args.prompt, args.style)
        
        print(f"  批量评审完成，共评审 {batch_result['reviewed_count']} 张图像")
        print(f"  通过：{batch_result['passed_count']} 张")
        print(f"  未通过：{batch_result['failed_count']} 张")
        
        if args.generate_report:
            print(f"📝 正在生成图像评审报告...")
            report_file = generate_review_report(batch_result['review_results'], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.compare:
        review1_file, review2_file = args.compare
        print(f"🔍 正在比较两个评审结果：{review1_file} 和 {review2_file}")
        
        if not os.path.exists(review1_file):
            print(f"❌ 错误：第一个评审结果文件不存在 - {review1_file}")
            return
        
        if not os.path.exists(review2_file):
            print(f"❌ 错误：第二个评审结果文件不存在 - {review2_file}")
            return
        
        with open(review1_file, 'r', encoding='utf-8') as f:
            review1 = json.load(f)
        
        with open(review2_file, 'r', encoding='utf-8') as f:
            review2 = json.load(f)
        
        comparison_result = compare_reviews(review1, review2)
        
        print(f"  比较完成")
        print(f"  更好的图像：{comparison_result['better_image']}")
        print(f"  建议：{comparison_result['recommendation']}")
        
        if args.generate_report:
            print(f"📝 正在生成图像评审报告...")
            # 创建模拟评审结果列表用于报告生成
            mock_review_results = [review1, review2]
            report_file = generate_review_report(mock_review_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有评审标准或显示帮助
    print("❌ 错误：请指定评审图像（使用 --image）、批量评审（使用 --batch-review）或比较评审结果（使用 --compare）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
