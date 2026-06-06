#!/usr/bin/env python3
"""
情报收集工具 (Intelligence Collector) - 增强版
为十二生肖团提供情报收集功能，支持技术情报、竞品情报、用户反馈收集和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import requests
from bs4 import BeautifulSoup

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
INTELLIGENCE_DATA_FILE = os.path.join(DATA_DIR, 'intelligence_sources.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_intelligence_data() -> Dict[str, Any]:
    """加载情报来源数据库"""
    try:
        with open(INTELLIGENCE_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载情报来源数据库 - {e}")
        return {}

def save_intelligence_data(data: Dict[str, Any]) -> bool:
    """保存情报来源数据库"""
    try:
        with open(INTELLIGENCE_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 情报来源数据库已更新：{INTELLIGENCE_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存情报来源数据库 - {e}")
        return False


def get_intelligence_source(source_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取情报来源"""
    data = load_intelligence_data()
    sources = data.get('intelligence_sources', [])
    for source in sources:
        if source.get('id') == source_id:
            return source
    return None


def list_sources() -> None:
    """列出所有情报来源"""
    data = load_intelligence_data()
    sources = data.get('intelligence_sources', [])
    if not sources:
        print("❌ 没有找到任何情报来源")
        return
    
    print("📊 可用情报来源列表：")
    for source in sources:
        print(f"  - {source.get('id')}: {source.get('name')} ({source.get('name_zh')})")


def collect_tech_intelligence(keywords: List[str], sources: List[str] = None, 
                            time_range: str = "2026-01-01 to 2026-12-31") -> Dict[str, Any]:
    """
    收集技术情报
    
    Args:
        keywords: 关键词列表
        sources: 来源列表（arXiv, GitHub, 技术博客等）
        time_range: 时间范围
        
    Returns:
        技术情报收集结果字典
    """
    if not sources:
        sources = ['arxiv', 'github', 'tech_blog', 'news']
    
    # 模拟技术情报收集（实际应用中会调用API）
    collection_result = {
        'success': True,
        'collection_type': 'tech_intelligence',
        'collection_time': datetime.now().isoformat(),
        'keywords': keywords,
        'sources': sources,
        'time_range': time_range,
        'findings': [],
        'trends': [],
        'recommendations': []
    }
    
    # 生成模拟发现
    for keyword in keywords:
        finding = {
            'id': f"TECH-{datetime.now().strftime('%Y%m%d')}-{len(collection_result['findings']) + 1:03d}",
            'title': f"{keyword}技术最新进展",
            'source': sources[0] if sources else 'arxiv',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'summary': f"关于{keyword}的最新技术进展和研究成果",
            'impact': '高',  # 高、中、低
            'url': f"https://arxiv.org/search/?query={keyword}",
            'collected_at': datetime.now().isoformat()
        }
        collection_result['findings'].append(finding)
    
    # 生成模拟趋势
    collection_result['trends'] = ['多模态融合', 'Agent自主化', '边缘计算']
    
    # 生成模拟建议
    collection_result['recommendations'] = ['关注多模态技术', '布局Agent应用', '探索边缘计算场景']
    
    return collection_result


def collect_competitor_intelligence(competitors: List[str], platforms: List[str] = None) -> Dict[str, Any]:
    """
    收集竞品情报
    
    Args:
        competitors: 竞品列表
        platforms: 平台列表（官网、京东、天猫等）
        
    Returns:
        竞品情报收集结果字典
    """
    if not platforms:
        platforms = ['official_website', 'jd', 'tmall', 'amazon']
    
    # 模拟竞品情报收集（实际应用中会调用API）
    collection_result = {
        'success': True,
        'collection_type': 'competitor_intelligence',
        'collection_time': datetime.now().isoformat(),
        'competitors': competitors,
        'platforms': platforms,
        'updates': [],
        'analysis': '',
        'threat_level': '',
        'recommendations': []
    }
    
    # 生成模拟更新
    for competitor in competitors:
        update = {
            'id': f"COMP-{datetime.now().strftime('%Y%m%d')}-{len(collection_result['updates']) + 1:03d}",
            'type': '产品发布',
            'title': f"{competitor}发布新产品",
            'competitor': competitor,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'features': ['轻量化设计', '智能导航', '健康监测'],
            'price': '¥3,999',
            'url': f"https://{competitor}.com/new-product",
            'collected_at': datetime.now().isoformat()
        }
        collection_result['updates'].append(update)
    
    # 生成模拟分析
    collection_result['analysis'] = "竞品在轻量化和智能化方面持续投入"
    collection_result['threat_level'] = '中'  # 高、中、低
    
    # 生成模拟建议
    collection_result['recommendations'] = ['加强轻量化材料研发', '加快智能导航技术布局']
    
    return collection_result


def collect_user_feedback(products: List[str], sources: List[str] = None) -> Dict[str, Any]:
    """
    收集用户反馈
    
    Args:
        products: 产品列表
        sources: 来源列表（电商平台、社交媒体、客服记录等）
        
    Returns:
        用户反馈收集结果字典
    """
    if not sources:
        sources = ['ecommerce', 'social_media', 'customer_service']
    
    # 模拟用户反馈收集（实际应用中会调用API）
    collection_result = {
        'success': True,
        'collection_type': 'user_feedback',
        'collection_time': datetime.now().isoformat(),
        'products': products,
        'sources': sources,
        'feedback': [],
        'pain_points': [],
        'demands': [],
        'recommendations': []
    }
    
    # 生成模拟反馈
    for product in products:
        feedback = {
            'id': f"USER-{datetime.now().strftime('%Y%m%d')}-{len(collection_result['feedback']) + 1:03d}",
            'product': product,
            'source': sources[0] if sources else 'ecommerce',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'rating': 4.5,  # 模拟评分（1-5）
            'positive_points': ['保温效果好', '开盖方便', '外观时尚'],
            'negative_points': ['重量偏大', '价格偏高'],
            'suggestions': ['希望更轻量化', '希望增加智能功能'],
            'collected_at': datetime.now().isoformat()
        }
        collection_result['feedback'].append(feedback)
    
    # 生成模拟痛点
    collection_result['pain_points'] = ['重量偏大', '价格偏高', '智能功能不足']
    
    # 生成模拟需求
    collection_result['demands'] = ['更轻量化', '更智能', '更便宜']
    
    # 生成模拟建议
    collection_result['recommendations'] = ['优化轻量化设计', '增加智能功能', '降低成本']
    
    return collection_result


def generate_intelligence_report(collection_results: List[Dict[str, Any]], 
                                output_format: str = 'json') -> str:
    """
    生成情报收集报告
    
    Args:
        collection_results: 收集结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 情报收集报告

## 基本信息
- **收集时间**：{datetime.now().isoformat()}
- **收集类型**：{', '.join([r.get('collection_type', '未知') for r in collection_results])}
- **情报数量**：{sum([len(r.get('findings', [])) + len(r.get('updates', [])) + len(r.get('feedback', [])) for r in collection_results])}

## 收集结果摘要
"""
        for i, result in enumerate(collection_results):
            report_content += f"\n### {i+1}. {result.get('collection_type', '未知类型').replace('_', ' ').title()}\n"
            
            if result.get('collection_type') == 'tech_intelligence':
                report_content += f"- **关键词**：{', '.join(result.get('keywords', []))}\n"
                report_content += f"- **来源**：{', '.join(result.get('sources', []))}\n"
                report_content += f"- **时间范围**：{result.get('time_range', '未知')}\n"
                report_content += f"- **发现数量**：{len(result.get('findings', []))}\n"
                report_content += f"- **趋势数量**：{len(result.get('trends', []))}\n"
                
                if result.get('findings'):
                    report_content += "\n**主要发现**：\n"
                    for finding in result.get('findings', [])[:3]:  # 只显示前3个
                        report_content += f"- {finding.get('title', '')}（{finding.get('source', '')}）\n"
                
                if result.get('trends'):
                    report_content += "\n**主要趋势**：\n"
                    for trend in result.get('trends', []):
                        report_content += f"- {trend}\n"
            
            elif result.get('collection_type') == 'competitor_intelligence':
                report_content += f"- **竞品**：{', '.join(result.get('competitors', []))}\n"
                report_content += f"- **平台**：{', '.join(result.get('platforms', []))}\n"
                report_content += f"- **更新数量**：{len(result.get('updates', []))}\n"
                report_content += f"- **威胁等级**：{result.get('threat_level', '未知')}\n"
                
                if result.get('updates'):
                    report_content += "\n**主要更新**：\n"
                    for update in result.get('updates', [])[:3]:  # 只显示前3个
                        report_content += f"- {update.get('title', '')}（{update.get('competitor', '')}）\n"
            
            elif result.get('collection_type') == 'user_feedback':
                report_content += f"- **产品**：{', '.join(result.get('products', []))}\n"
                report_content += f"- **来源**：{', '.join(result.get('sources', []))}\n"
                report_content += f"- **反馈数量**：{len(result.get('feedback', []))}\n"
                report_content += f"- **痛点数量**：{len(result.get('pain_points', []))}\n"
                report_content += f"- **需求数量**：{len(result.get('demands', []))}\n"
                
                if result.get('feedback'):
                    report_content += "\n**主要反馈**：\n"
                    for feedback in result.get('feedback', [])[:3]:  # 只显示前3个
                        report_content += f"- {feedback.get('product', '')}：评分{feedback.get('rating', 0):.2f}/5.0\n"
                
                if result.get('pain_points'):
                    report_content += "\n**主要痛点**：\n"
                    for pain_point in result.get('pain_points', []):
                        report_content += f"- {pain_point}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总发现数量**：{sum([len(r.get('findings', [])) for r in collection_results])}\n"
        report_content += f"- **总更新数量**：{sum([len(r.get('updates', [])) for r in collection_results])}\n"
        report_content += f"- **总反馈数量**：{sum([len(r.get('feedback', [])) for r in collection_results])}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'intelligence_collection',
            'generated_at': datetime.now().isoformat(),
            'collection_count': len(collection_results),
            'collection_results': collection_results,
            'summary': {
                'total_findings': sum([len(r.get('findings', [])) for r in collection_results]),
                'total_updates': sum([len(r.get('updates', [])) for r in collection_results]),
                'total_feedback': sum([len(r.get('feedback', [])) for r in collection_results]),
                'total_pain_points': sum([len(r.get('pain_points', [])) for r in collection_results]),
                'total_demands': sum([len(r.get('demands', [])) for r in collection_results]),
                'total_recommendations': sum([len(r.get('recommendations', [])) for r in collection_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'intelligence_collection_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'intelligence_collection_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 情报收集报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='情报收集工具（增强版）')
    parser.add_argument('--collect-tech', action='store_true', help='收集技术情报')
    parser.add_argument('--keywords', type=str, nargs='+', help='关键词列表（用于技术情报收集）')
    parser.add_argument('--sources', type=str, nargs='+', help='来源列表（用于技术情报收集）')
    parser.add_argument('--time-range', type=str, default='2026-01-01 to 2026-12-31', help='时间范围（用于技术情报收集）')
    parser.add_argument('--collect-competitor', action='store_true', help='收集竞品情报')
    parser.add_argument('--competitors', type=str, nargs='+', help='竞品列表（用于竞品情报收集）')
    parser.add_argument('--platforms', type=str, nargs='+', help='平台列表（用于竞品情报收集）')
    parser.add_argument('--collect-feedback', action='store_true', help='收集用户反馈')
    parser.add_argument('--products', type=str, nargs='+', help='产品列表（用于用户反馈收集）')
    parser.add_argument('--feedback-sources', type=str, nargs='+', help='来源列表（用于用户反馈收集）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成情报收集报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    collection_results = []
    
    if args.collect_tech:
        if not args.keywords:
            print("❌ 错误：收集技术情报需要指定关键词（使用 --keywords）")
            parser.print_help()
            return
        
        print(f"🔍 正在收集技术情报：关键词={args.keywords}")
        tech_intel = collect_tech_intelligence(args.keywords, args.sources, args.time_range)
        collection_results.append(tech_intel)
        
        print(f"  收集类型：{tech_intel['collection_type']}")
        print(f"  发现数量：{len(tech_intel['findings'])}")
        print(f"  趋势数量：{len(tech_intel['trends'])}")
    
    if args.collect_competitor:
        if not args.competitors:
            print("❌ 错误：收集竞品情报需要指定竞品列表（使用 --competitors）")
            parser.print_help()
            return
        
        print(f"🔍 正在收集竞品情报：竞品={args.competitors}")
        comp_intel = collect_competitor_intelligence(args.competitors, args.platforms)
        collection_results.append(comp_intel)
        
        print(f"  收集类型：{comp_intel['collection_type']}")
        print(f"  更新数量：{len(comp_intel['updates'])}")
        print(f"  威胁等级：{comp_intel['threat_level']}")
    
    if args.collect_feedback:
        if not args.products:
            print("❌ 错误：收集用户反馈需要指定产品列表（使用 --products）")
            parser.print_help()
            return
        
        print(f"🔍 正在收集用户反馈：产品={args.products}")
        user_feedback = collect_user_feedback(args.products, args.feedback_sources)
        collection_results.append(user_feedback)
        
        print(f"  收集类型：{user_feedback['collection_type']}")
        print(f"  反馈数量：{len(user_feedback['feedback'])}")
        print(f"  痛点数量：{len(user_feedback['pain_points'])}")
    
    if collection_results:
        if args.generate_report:
            print(f"📝 正在生成情报收集报告...")
            report_file = generate_intelligence_report(collection_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有来源或显示帮助
    if not any([args.collect_tech, args.collect_competitor, args.collect_feedback]):
        print("❌ 错误：请指定收集类型（--collect-tech, --collect-competitor, --collect-feedback）")
        parser.print_help()
        return


if __name__ == '__main__':
    main()
