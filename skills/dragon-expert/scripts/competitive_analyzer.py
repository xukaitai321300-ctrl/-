#!/usr/bin/env python3
"""
竞品分析工具 (Competitive Analysis Tool) - 增强版
为十二生肖团提供竞品分析功能，支持产品分析、工艺分析、设计风格分析和报告生成
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
COMPETITIVE_DATA_FILE = os.path.join(DATA_DIR, 'competitive_analysis.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_competitive_data() -> Dict[str, Any]:
    """加载竞品分析数据库"""
    try:
        with open(COMPETITIVE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载竞品分析数据库 - {e}")
        return {}


def save_competitive_data(data: Dict[str, Any]) -> bool:
    """保存竞品分析数据库"""
    try:
        with open(COMPETITIVE_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 竞品分析数据库已更新：{COMPETITIVE_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存竞品分析数据库 - {e}")
        return False


def get_analysis_method(method_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取分析方法"""
    data = load_competitive_data()
    methods = data.get('analysis_methods', [])
    for method in methods:
        if method.get('id') == method_id:
            return method
    return None


def list_methods() -> None:
    """列出所有分析方法"""
    data = load_competitive_data()
    methods = data.get('analysis_methods', [])
    if not methods:
        print("❌ 没有找到任何分析方法")
        return
    
    print("📊 可用分析方法列表：")
    for method in methods:
        print(f"  - {method.get('id')}: {method.get('name')} ({method.get('name_zh')})")


def analyze_product(competitor_id: str, product_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    分析竞品产品
    
    Args:
        competitor_id: 竞品ID
        product_data: 产品数据
        
    Returns:
        产品分析结果字典
    """
    # 模拟产品分析（实际应用中会调用分析算法）
    analysis_result = {
        'success': True,
        'competitor_id': competitor_id,
        'analysis_type': 'product_analysis',
        'analysis_time': datetime.now().isoformat(),
        'product_data': product_data,
        'analysis_results': {
            'design_features': {
                'score': 85.5,
                'features': ['轻量化设计', '弹跳盖结构', '车载杯架适配'],
                'strengths': ['重量轻', '开盖方便', '车载适用'],
                'weaknesses': ['保温性能一般', '价格较高']
            },
            'material_usage': {
                'score': 78.2,
                'materials': ['304不锈钢', '食品级PP', '硅胶密封圈'],
                'cost_effectiveness': '中等',
                'environmental_friendly': True
            },
            'craftsmanship': {
                'score': 82.0,
                'techniques': ['旋薄工艺', '无尾真空', '激光焊接'],
                'precision_level': '高',
                'durability': '良好'
            },
            'user_experience': {
                'score': 88.7,
                'usability': '优秀',
                'comfort': '良好',
                'safety': '高'
            }
        },
        'overall_score': 83.6,
        'competitive_level': '高',  # 高、中、低
        'issues': [],
        'suggestions': []
    }
    
    # 根据分数添加问题和建议
    if analysis_result['overall_score'] < 70:
        analysis_result['issues'].append("产品竞争力不足")
        analysis_result['suggestions'].append("建议重新设计或优化产品")
    
    return analysis_result


def compare_products(products: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    比较多个竞品
    
    Args:
        products: 产品数据列表
        
    Returns:
        产品比较结果字典
    """
    # 模拟产品比较（实际应用中会调用比较算法）
    comparison_result = {
        'success': True,
        'products_count': len(products),
        'comparison_time': datetime.now().isoformat(),
        'products': products,
        'comparison_results': {
            'design_comparison': {
                'best_design': products[0].get('name', '未知产品') if products else '无',
                'design_differences': ['重量差异', '开盖方式差异', '外观设计差异']
            },
            'material_comparison': {
                'best_material': products[0].get('name', '未知产品') if products else '无',
                'material_differences': ['材料类型差异', '成本差异', '环保性差异']
            },
            'craftsmanship_comparison': {
                'best_craftsmanship': products[0].get('name', '未知产品') if products else '无',
                'craftsmanship_differences': ['工艺精度差异', '耐用性差异', '生产效率差异']
            },
            'price_comparison': {
                'lowest_price': min([p.get('price', 0) for p in products]) if products else 0,
                'highest_price': max([p.get('price', 0) for p in products]) if products else 0,
                'avg_price': sum([p.get('price', 0) for p in products]) / len(products) if products else 0
            }
        },
        'ranking': []
    }
    
    # 生成排名（按综合分数排序）
    for i, product in enumerate(products):
        comparison_result['ranking'].append({
            'rank': i + 1,
            'product_name': product.get('name', f'产品{i+1}'),
            'overall_score': 90 - i * 5.2,  # 模拟分数
            'competitive_level': '高' if i == 0 else ('中' if i == 1 else '低')
        })
    
    return comparison_result


def generate_competitive_report(analysis_results: List[Dict[str, Any]], 
                              output_format: str = 'json') -> str:
    """
    生成竞品分析报告
    
    Args:
        analysis_results: 分析结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 竞品分析报告

## 基本信息
- **分析时间**：{datetime.now().isoformat()}
- **分析产品数量**：{len(analysis_results)}
- **分析类型**：产品分析/工艺分析/设计风格分析

## 分析结果摘要
"""
        for i, result in enumerate(analysis_results):
            report_content += f"\n### {i+1}. {result.get('competitor_id', '未知竞品')}\n"
            report_content += f"- **分析类型**：{result.get('analysis_type', '未知')}\n"
            report_content += f"- **综合分数**：{result.get('overall_score', 0):.2f}/100\n"
            report_content += f"- **竞争力水平**：{result.get('competitive_level', '未知')}\n"
            
            if result.get('issues'):
                report_content += "\n**问题**：\n"
                for issue in result.get('issues'):
                    report_content += f"- {issue}\n"
            
            if result.get('suggestions'):
                report_content += "\n**建议**：\n"
                for suggestion in result.get('suggestions'):
                    report_content += f"- {suggestion}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **平均综合分数**：{sum([r.get('overall_score', 0) for r in analysis_results]) / len(analysis_results):.2f}/100\n"
        report_content += f"- **最高综合分数**：{max([r.get('overall_score', 0) for r in analysis_results]):.2f}/100\n"
        report_content += f"- **最低综合分数**：{min([r.get('overall_score', 0) for r in analysis_results]):.2f}/100\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'competitive_analysis',
            'generated_at': datetime.now().isoformat(),
            'products_count': len(analysis_results),
            'analysis_results': analysis_results,
            'summary': {
                'avg_overall_score': sum([r.get('overall_score', 0) for r in analysis_results]) / len(analysis_results),
                'max_overall_score': max([r.get('overall_score', 0) for r in analysis_results]),
                'min_overall_score': min([r.get('overall_score', 0) for r in analysis_results]),
                'total_issues': sum([len(r.get('issues', [])) for r in analysis_results]),
                'total_suggestions': sum([len(r.get('suggestions', [])) for r in analysis_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(OUTPUT_DIR, f'competitive_analysis_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(OUTPUT_DIR, f'competitive_analysis_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 竞品分析报告已生成：{output_file}")
    return output_file


def print_method_details(method: Dict[str, Any]) -> None:
    """打印分析方法详情"""
    print(f"📊 分析方法详情：{method.get('name')} ({method.get('name_zh')})")
    print(f"  描述：{method.get('description')}")
    print(f"  中文描述：{method.get('description_zh')}")
    
    steps = method.get('steps', [])
    steps_zh = method.get('steps_zh', [])
    print(f"\n  🔧 分析步骤：")
    for i, step in enumerate(steps):
        step_zh = steps_zh[i] if i < len(steps_zh) else step
        print(f"    {i+1}. {step}")
        print(f"       {step_zh}")
    
    prompts = method.get('prompt_keywords', {})
    if prompts:
        print(f"\n  📝 提示词关键词：")
        print(f"    英文：{prompts.get('english')}")
        print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='竞品分析工具（增强版）')
    parser.add_argument('--method', type=str, help='分析方法ID（product_analysis/craftsmanship_analysis/design_style_analysis）')
    parser.add_argument('--list', action='store_true', help='列出所有分析方法')
    parser.add_argument('--analyze-product', type=str, help='分析竞品产品（指定竞品ID）')
    parser.add_argument('--product-data', type=str, help='产品数据JSON字符串或文件路径')
    parser.add_argument('--compare-products', type=str, help='比较多个竞品（指定产品数据JSON文件路径）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', help='生成竞品分析报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_methods()
        return
    
    if args.analyze_product:
        print(f"🔍 正在分析竞品产品：{args.analyze_product}")
        
        # 获取产品数据
        product_data = {}
        if args.product_data:
            if os.path.exists(args.product_data):
                with open(args.product_data, 'r', encoding='utf-8') as f:
                    product_data = json.load(f)
            else:
                try:
                    product_data = json.loads(args.product_data)
                except:
                    print(f"❌ 错误：无法解析产品数据 - {args.product_data}")
                    return
        else:
            # 使用模拟数据
            product_data = {
                'name': '竞品保温杯',
                'price': 129.0,
                'weight': 280.0,
                'capacity': 500,
                'material': '304不锈钢',
                'features': ['轻量化', '弹跳盖', '车载适用']
            }
        
        analysis_result = analyze_product(args.analyze_product, product_data)
        print(f"  综合分数：{analysis_result['overall_score']:.2f}/100")
        print(f"  竞争力水平：{analysis_result['competitive_level']}")
        
        if args.generate_report:
            print(f"📝 正在生成竞品分析报告...")
            report_file = generate_competitive_report([analysis_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.compare_products:
        print(f"🔍 正在比较竞品：{args.compare_products}")
        
        # 获取产品数据列表
        products = []
        if os.path.exists(args.compare_products):
            with open(args.compare_products, 'r', encoding='utf-8') as f:
                products = json.load(f)
        else:
            # 使用模拟数据
            products = [
                {'name': '竞品A保温杯', 'price': 129.0, 'weight': 280.0, 'capacity': 500},
                {'name': '竞品B保温杯', 'price': 99.0, 'weight': 320.0, 'capacity': 450},
                {'name': '竞品C保温杯', 'price': 159.0, 'weight': 250.0, 'capacity': 550}
            ]
        
        comparison_result = compare_products(products)
        print(f"  比较产品数量：{comparison_result['products_count']}")
        print(f"  最低价格：{comparison_result['comparison_results']['price_comparison']['lowest_price']:.2f}元")
        print(f"  最高价格：{comparison_result['comparison_results']['price_comparison']['highest_price']:.2f}元")
        
        if args.generate_report:
            print(f"📝 正在生成竞品分析报告...")
            # 将比较结果转换为分析结果列表（用于报告生成）
            analysis_results = [{
                'competitor_id': product.get('name', '未知产品'),
                'analysis_type': 'product_comparison',
                'overall_score': 90 - i * 5.2,
                'competitive_level': '高' if i == 0 else ('中' if i == 1 else '低')
            } for i, product in enumerate(products)]
            
            report_file = generate_competitive_report(analysis_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有方法或显示帮助
    if not args.method:
        print("❌ 错误：请指定分析方法ID（使用 --method）或列出所有方法（使用 --list）")
        parser.print_help()
        return
    
    method = get_analysis_method(args.method)
    if not method:
        print(f"❌ 错误：找不到ID为 '{args.method}' 的分析方法")
        list_methods()
        return
    
    print_method_details(method)


if __name__ == '__main__':
    main()
