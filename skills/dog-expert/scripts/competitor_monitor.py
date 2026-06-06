#!/usr/bin/env python3
"""
竞品监测工具 (Competitor Monitor) - 增强版
为十二生肖团提供竞品监测功能，支持产品发布监测、专利监测、动态追踪和报告生成
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
COMPETITOR_DATA_FILE = os.path.join(DATA_DIR, 'competitor_database.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_competitor_data() -> Dict[str, Any]:
    """加载竞品数据库"""
    try:
        with open(COMPETITOR_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载竞品数据库 - {e}")
        return {}

def save_competitor_data(data: Dict[str, Any]) -> bool:
    """保存竞品数据库"""
    try:
        with open(COMPETITOR_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 竞品数据库已更新：{COMPETITOR_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存竞品数据库 - {e}")
        return False


def get_competitor(competitor_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取竞品信息"""
    data = load_competitor_data()
    competitors = data.get('competitors', [])
    for competitor in competitors:
        if competitor.get('id') == competitor_id:
            return competitor
    return None


def list_competitors() -> None:
    """列出所有竞品"""
    data = load_competitor_data()
    competitors = data.get('competitors', [])
    if not competitors:
        print("❌ 没有找到任何竞品")
        return
    
    print("📊 可用竞品列表：")
    for competitor in competitors:
        print(f"  - {competitor.get('id')}: {competitor.get('name')} ({competitor.get('name_zh')})")


def monitor_product_releases(competitors: List[str], platforms: List[str] = None) -> Dict[str, Any]:
    """
    监测竞品产品发布
    
    Args:
        competitors: 竞品列表
        platforms: 平台列表（官网、京东、天猫等）
        
    Returns:
        监测结果字典
    """
    if not platforms:
        platforms = ['official_website', 'jd', 'tmall', 'amazon']
    
    # 模拟竞品产品发布监测（实际应用中会调用API）
    monitoring_result = {
        'success': True,
        'monitoring_type': 'product_releases',
        'monitoring_time': datetime.now().isoformat(),
        'competitors': competitors,
        'platforms': platforms,
        'updates': [],
        'analysis': '',
        'threat_level': '',
        'recommendations': []
    }
    
    # 生成模拟更新
    for competitor in competitors:
        # 查找竞品信息
        competitor_info = get_competitor(competitor)
        if competitor_info:
            # 获取竞品产品信息
            for product in competitor_info.get('products', []):
                update = {
                    'id': f"COMP-{datetime.now().strftime('%Y%m%d')}-{len(monitoring_result['updates']) + 1:03d}",
                    'type': '产品发布',
                    'title': f"{competitor_info.get('name')}发布{product.get('name')}",
                    'competitor': competitor,
                    'product': product.get('name'),
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'features': product.get('features', []),
                    'price': product.get('price', '未知'),
                    'url': competitor_info.get('website', ''),
                    'detected_at': datetime.now().isoformat()
                }
                monitoring_result['updates'].append(update)
        else:
            # 如果没有找到竞品信息，则使用模拟数据
            update = {
                'id': f"COMP-{datetime.now().strftime('%Y%m%d')}-{len(monitoring_result['updates']) + 1:03d}",
                'type': '产品发布',
                'title': f"{competitor}发布新产品",
                'competitor': competitor,
                'product': f"{competitor}新产品",
                'date': datetime.now().strftime('%Y-%m-%d'),
                'features': ['轻量化设计', '智能导航', '健康监测'],
                'price': '¥3,999',
                'url': f"https://{competitor}.com/new-product",
                'detected_at': datetime.now().isoformat()
            }
            monitoring_result['updates'].append(update)
    
    # 生成模拟分析
    monitoring_result['analysis'] = "竞品在轻量化和智能化方面持续投入"
    monitoring_result['threat_level'] = '中'  # 高、中、低
    
    # 生成模拟建议
    monitoring_result['recommendations'] = ['加强轻量化材料研发', '加快智能导航技术布局']
    
    return monitoring_result


def monitor_patent_filings(competitors: List[str]) -> Dict[str, Any]:
    """
    监测竞品专利申请
    
    Args:
        competitors: 竞品列表
        
    Returns:
        监测结果字典
    """
    # 模拟竞品专利申请监测（实际应用中会调用专利数据库API）
    monitoring_result = {
        'success': True,
        'monitoring_type': 'patent_filings',
        'monitoring_time': datetime.now().isoformat(),
        'competitors': competitors,
        'patents': [],
        'analysis': '',
        'recommendations': []
    }
    
    # 生成模拟专利信息
    for competitor in competitors:
        # 查找竞品信息
        competitor_info = get_competitor(competitor)
        if competitor_info:
            # 获取竞品专利信息
            for patent in competitor_info.get('patents', []):
                patent_info = {
                    'id': f"PATENT-{datetime.now().strftime('%Y%m%d')}-{len(monitoring_result['patents']) + 1:03d}",
                    'competitor': competitor,
                    'title': patent.get('title', ''),
                    'patent_number': patent.get('patent_number', ''),
                    'filing_date': patent.get('filing_date', ''),
                    'status': patent.get('status', ''),
                    'url': f"https://www.cnipa.gov.cn/patent/{patent.get('patent_number', '')}",
                    'detected_at': datetime.now().isoformat()
                }
                monitoring_result['patents'].append(patent_info)
        else:
            # 如果没有找到竞品信息，则使用模拟数据
            patent_info = {
                'id': f"PATENT-{datetime.now().strftime('%Y%m%d')}-{len(monitoring_result['patents']) + 1:03d}",
                'competitor': competitor,
                'title': f"{competitor}新专利申请",
                'patent_number': f"CN{datetime.now().year}{len(monitoring_result['patents']) + 1:04d}XXXA",
                'filing_date': datetime.now().strftime('%Y-%m-%d'),
                'status': '审查中',
                'url': f"https://www.cnipa.gov.cn/patent/CN{datetime.now().year}{len(monitoring_result['patents']) + 1:04d}XXXA",
                'detected_at': datetime.now().isoformat()
            }
            monitoring_result['patents'].append(patent_info)
    
    # 生成模拟分析
    monitoring_result['analysis'] = "竞品在轻量化材料和智能控制方面加强专利布局"
    
    # 生成模拟建议
    monitoring_result['recommendations'] = ['加强专利布局', '规避专利风险']
    
    return monitoring_result


def track_competitor_dynamics(competitor: str, time_range: str = "2026-01-01 to 2026-12-31") -> Dict[str, Any]:
    """
    追踪竞品动态
    
    Args:
        competitor: 竞品名称
        time_range: 时间范围
        
    Returns:
        追踪结果字典
    """
    # 模拟竞品动态追踪（实际应用中会调用API）
    tracking_result = {
        'success': True,
        'tracking_type': 'competitor_dynamics',
        'tracking_time': datetime.now().isoformat(),
        'competitor': competitor,
        'time_range': time_range,
        'dynamics': [],
        'analysis': '',
        'recommendations': []
    }
    
    # 生成模拟动态
    dynamics_types = ['产品发布', '专利申请', '市场活动', '技术突破', '合作动态']
    
    for i in range(3):  # 模拟3条动态
        dynamic = {
            'id': f"DYNAMIC-{datetime.now().strftime('%Y%m%d')}-{i + 1:03d}",
            'type': dynamics_types[i % len(dynamics_types)],
            'title': f"{competitor}{dynamics_types[i % len(dynamics_types)]}动态",
            'date': datetime.now().strftime('%Y-%m-%d'),
            'description': f"{competitor}在{dynamics_types[i % len(dynamics_types)]}方面有新的进展",
            'impact': '中',  # 高、中、低
            'url': f"https://{competitor}.com/news/{i + 1}",
            'detected_at': datetime.now().isoformat()
        }
        tracking_result['dynamics'].append(dynamic)
    
    # 生成模拟分析
    tracking_result['analysis'] = f"竞品{competitor}在多个方面有持续投入"
    
    # 生成模拟建议
    tracking_result['recommendations'] = [f"关注{competitor}动态", '及时调整策略']
    
    return tracking_result


def generate_monitoring_report(monitoring_results: List[Dict[str, Any]], 
                                output_format: str = 'json') -> str:
    """
    生成竞品监测报告
    
    Args:
        monitoring_results: 监测结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 竞品监测报告

## 基本信息
- **监测时间**：{datetime.now().isoformat()}
- **监测竞品数量**：{len(monitoring_results)}
- **监测类型**：产品发布监测、专利申请监测、动态追踪

## 监测结果摘要
"""
        for i, result in enumerate(monitoring_results):
            report_content += f"\n### {i+1}. {result.get('monitoring_type', result.get('tracking_type', '未知类型')).replace('_', ' ').title()}\n"
            
            if result.get('monitoring_type') == 'product_releases':
                report_content += f"- **监测竞品**：{', '.join(result.get('competitors', []))}\n"
                report_content += f"- **监测平台**：{', '.join(result.get('platforms', []))}\n"
                report_content += f"- **更新数量**：{len(result.get('updates', []))}\n"
                report_content += f"- **威胁等级**：{result.get('threat_level', '未知')}\n"
                
                if result.get('updates'):
                    report_content += "\n**主要更新**：\n"
                    for update in result.get('updates', [])[:3]:  # 只显示前3个
                        report_content += f"- {update.get('title', '')}（{update.get('date', '')}）\n"
            
            elif result.get('monitoring_type') == 'patent_filings':
                report_content += f"- **监测竞品**：{', '.join(result.get('competitors', []))}\n"
                report_content += f"- **专利数量**：{len(result.get('patents', []))}\n"
                
                if result.get('patents'):
                    report_content += "\n**主要专利**：\n"
                    for patent in result.get('patents', [])[:3]:  # 只显示前3个
                        report_content += f"- {patent.get('title', '')}（{patent.get('patent_number', '')}）\n"
            
            elif result.get('tracking_type') == 'competitor_dynamics':
                report_content += f"- **追踪竞品**：{result.get('competitor', '未知')}\n"
                report_content += f"- **时间范围**：{result.get('time_range', '未知')}\n"
                report_content += f"- **动态数量**：{len(result.get('dynamics', []))}\n"
                
                if result.get('dynamics'):
                    report_content += "\n**主要动态**：\n"
                    for dynamic in result.get('dynamics', [])[:3]:  # 只显示前3个
                        report_content += f"- {dynamic.get('title', '')}（{dynamic.get('type', '')}）\n"
            
            if result.get('analysis'):
                report_content += f"\n**分析**：{result.get('analysis', '')}\n"
            
            if result.get('recommendations'):
                report_content += "\n**建议**：\n"
                for recommendation in result.get('recommendations', []):
                    report_content += f"- {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总更新数量**：{sum([len(r.get('updates', [])) for r in monitoring_results if r.get('monitoring_type') == 'product_releases'])}\n"
        report_content += f"- **总专利数量**：{sum([len(r.get('patents', [])) for r in monitoring_results if r.get('monitoring_type') == 'patent_filings'])}\n"
        report_content += f"- **总动态数量**：{sum([len(r.get('dynamics', [])) for r in monitoring_results if r.get('tracking_type') == 'competitor_dynamics'])}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'competitor_monitoring',
            'generated_at': datetime.now().isoformat(),
            'monitoring_count': len(monitoring_results),
            'monitoring_results': monitoring_results,
            'summary': {
                'total_updates': sum([len(r.get('updates', [])) for r in monitoring_results if r.get('monitoring_type') == 'product_releases']),
                'total_patents': sum([len(r.get('patents', [])) for r in monitoring_results if r.get('monitoring_type') == 'patent_filings']),
                'total_dynamics': sum([len(r.get('dynamics', [])) for r in monitoring_results if r.get('tracking_type') == 'competitor_dynamics']),
                'total_recommendations': sum([len(r.get('recommendations', [])) for r in monitoring_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'competitor_monitoring_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'competitor_monitoring_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 竞品监测报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='竞品监测工具（增强版）')
    parser.add_argument('--monitor-product', action='store_true', help='监测竞品产品发布')
    parser.add_argument('--competitors', type=str, nargs='+', help='竞品列表（用于产品发布监测）')
    parser.add_argument('--platforms', type=str, nargs='+', help='平台列表（用于产品发布监测）')
    parser.add_argument('--monitor-patent', action='store_true', help='监测竞品专利申请')
    parser.add_argument('--track-dynamics', type=str, help='追踪竞品动态（指定竞品名称）')
    parser.add_argument('--time-range', type=str, default='2026-01-01 to 2026-12-31', help='时间范围（用于动态追踪）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成竞品监测报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    monitoring_results = []
    
    if args.monitor_product:
        if not args.competitors:
            print("❌ 错误：监测竞品产品发布需要指定竞品列表（使用 --competitors）")
            parser.print_help()
            return
        
        print(f"🔍 正在监测竞品产品发布：{args.competitors}")
        
        platforms = args.platforms if args.platforms else None
        monitoring_result = monitor_product_releases(args.competitors, platforms)
        monitoring_results.append(monitoring_result)
        
        print(f"  监测类型：{monitoring_result['monitoring_type']}")
        print(f"  更新数量：{len(monitoring_result['updates'])}")
        print(f"  威胁等级：{monitoring_result['threat_level']}")
    
    if args.monitor_patent:
        if not args.competitors:
            print("❌ 错误：监测竞品专利申请需要指定竞品列表（使用 --competitors）")
            parser.print_help()
            return
        
        print(f"🔍 正在监测竞品专利申请：{args.competitors}")
        
        monitoring_result = monitor_patent_filings(args.competitors)
        monitoring_results.append(monitoring_result)
        
        print(f"  监测类型：{monitoring_result['monitoring_type']}")
        print(f"  专利数量：{len(monitoring_result['patents'])}")
    
    if args.track_dynamics:
        print(f"🔍 正在追踪竞品动态：{args.track_dynamics}")
        
        tracking_result = track_competitor_dynamics(args.track_dynamics, args.time_range)
        monitoring_results.append(tracking_result)
        
        print(f"  追踪类型：{tracking_result['tracking_type']}")
        print(f"  动态数量：{len(tracking_result['dynamics'])}")
    
    if monitoring_results:
        if args.generate_report:
            print(f"📝 正在生成竞品监测报告...")
            report_file = generate_monitoring_report(monitoring_results, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有竞品或显示帮助
    print("❌ 错误：请指定监测类型（--monitor-product, --monitor-patent, --track-dynamics）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
