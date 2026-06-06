#!/usr/bin/env python3
"""
报告生成工具 (Report Generator) - 增强版
为十二生肖团提供报告生成功能，支持情报报告、竞品监测报告、技术追踪报告和综合报告生成
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
REPORT_CONFIG_FILE = os.path.join(DATA_DIR, 'report_config.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_report_config() -> Dict[str, Any]:
    """加载报告配置数据库"""
    try:
        with open(REPORT_CONFIG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载报告配置数据库 - {e}")
        return {}

def save_report_config(data: Dict[str, Any]) -> bool:
    """保存报告配置数据库"""
    try:
        with open(REPORT_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 报告配置数据库已更新：{REPORT_CONFIG_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存报告配置数据库 - {e}")
        return False


def get_report_template(template_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取报告模板"""
    data = load_report_config()
    templates = data.get('report_templates', [])
    for template in templates:
        if template.get('id') == template_id:
            return template
    return None


def list_templates() -> None:
    """列出所有报告模板"""
    data = load_report_config()
    templates = data.get('report_templates', [])
    if not templates:
        print("❌ 没有找到任何报告模板")
        return
    
    print("📊 可用报告模板列表：")
    for template in templates:
        print(f"  - {template.get('id')}: {template.get('name')} ({template.get('name_zh')})")


def generate_intelligence_report(intelligence_data: Dict[str, Any], 
                              output_format: str = 'json') -> str:
    """
    生成情报收集报告
    
    Args:
        intelligence_data: 情报收集数据
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 情报收集报告

## 基本信息
- **报告ID**：{intelligence_data.get('report_id', '未知报告')}
- **报告标题**：{intelligence_data.get('title', '未知标题')}
- **生成时间**：{datetime.now().isoformat()}
- **收集类型**：{intelligence_data.get('collection_type', '未知类型')}

## 收集结果摘要
"""
        findings = intelligence_data.get('findings', [])
        trends = intelligence_data.get('trends', [])
        recommendations = intelligence_data.get('recommendations', [])
        
        if findings:
            report_content += f"\n### 主要发现\n"
            for i, finding in enumerate(findings[:5]):  # 只显示前5个
                report_content += f"{i+1}. **{finding.get('title', '未知发现')}**\n"
                report_content += f"   - 来源：{finding.get('source', '未知来源')}\n"
                report_content += f"   - 日期：{finding.get('date', '未知日期')}\n"
                report_content += f"   - 摘要：{finding.get('summary', '无摘要')}\n"
        
        if trends:
            report_content += f"\n### 技术趋势\n"
            for i, trend in enumerate(trends[:5]):  # 只显示前5个
                report_content += f"{i+1}. {trend}\n"
        
        if recommendations:
            report_content += f"\n### 建议\n"
            for i, recommendation in enumerate(recommendations[:5]):  # 只显示前5个
                report_content += f"{i+1}. {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总发现数量**：{len(findings)}\n"
        report_content += f"- **总趋势数量**：{len(trends)}\n"
        report_content += f"- **总建议数量**：{len(recommendations)}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'intelligence_collection',
            'generated_at': datetime.now().isoformat(),
            'intelligence_data': intelligence_data,
            'summary': {
                'total_findings': len(intelligence_data.get('findings', [])),
                'total_trends': len(intelligence_data.get('trends', [])),
                'total_recommendations': len(intelligence_data.get('recommendations', []))
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'intelligence_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'intelligence_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 情报收集报告已生成：{output_file}")
    return output_file


def generate_competitor_report(competitor_data: Dict[str, Any], 
                            output_format: str = 'json') -> str:
    """
    生成竞品监测报告
    
    Args:
        competitordata: 竞品监测数据
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 竞品监测报告

## 基本信息
- **报告ID**：{competitor_data.get('report_id', '未知报告')}
- **报告标题**：{competitor_data.get('title', '未知标题')}
- **生成时间**：{datetime.now().isoformat()}
- **监测类型**：{competitor_data.get('monitoring_type', '未知类型')}

## 监测结果摘要
"""
        updates = competitordata.get('updates', [])
        analysis = competitordata.get('analysis', '')
        threat_level = competitordata.get('threat_level', '')
        recommendations = competitordata.get('recommendations', [])
        
        if updates:
            report_content += f"\n### 主要更新\n"
            for i, update in enumerate(updates[:5]):  # 只显示前5个
                report_content += f"{i+1}. **{update.get('title', '未知更新')}**\n"
                report_content += f"   - 类型：{update.get('type', '未知类型')}\n"
                report_content += f"   - 日期：{update.get('date', '未知日期')}\n"
                report_content += f"   - 功能：{', '.join(update.get('features', []))}\n"
        
        if analysis:
            report_content += f"\n### 分析\n"
            report_content += f"{analysis}\n"
        
        if threat_level:
            report_content += f"\n### 威胁等级\n"
            report_content += f"{threat_level}\n"
        
        if recommendations:
            report_content += f"\n### 建议\n"
            for i, recommendation in enumerate(recommendations[:5]):  # 只显示前5个
                report_content += f"{i+1}. {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总更新数量**：{len(updates)}\n"
        report_content += f"- **威胁等级**：{threat_level}\n"
        report_content += f"- **总建议数量**：{len(recommendations)}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'competitor_monitoring',
            'generated_at': datetime.now().isoformat(),
            'competitor_data': competitordata,
            'summary': {
                'total_updates': len(competitordata.get('updates', [])),
                'threat_level': competitordata.get('threat_level', ''),
                'total_recommendations': len(competitordata.get('recommendations', []))
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'competitor_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'competitor_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 竞品监测报告已生成：{output_file}")
    return output_file


def generate_tech_tracking_report(tracking_data: Dict[str, Any], 
                                output_format: str = 'json') -> str:
    """
    生成技术追踪报告
    
    Args:
        tracking_data: 技术追踪数据
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 技术追踪报告

## 基本信息
- **报告ID**：{tracking_data.get('report_id', '未知报告')}
- **报告标题**：{tracking_data.get('title', '未知标题')}
- **生成时间**：{datetime.now().isoformat()}
- **追踪类型**：{tracking_data.get('tracking_type', '未知类型')}

## 追踪结果摘要
"""
        trends = tracking_data.get('trends', [])
        analysis = tracking_data.get('analysis', '')
        recommendations = tracking_data.get('recommendations', [])
        
        if trends:
            report_content += f"\n### 主要趋势\n"
            for i, trend in enumerate(trends[:5]):  # 只显示前5个
                if isinstance(trend, dict):
                    report_content += f"{i+1}. **{trend.get('title', '未知趋势')}**\n"
                    report_content += f"   - 类别：{trend.get('category', '未知类别')}\n"
                    report_content += f"   - 描述：{trend.get('description', '无描述')}\n"
                else:
                    report_content += f"{i+1}. {trend}\n"
        
        if analysis:
            report_content += f"\n### 分析\n"
            report_content += f"{analysis}\n"
        
        if recommendations:
            report_content += f"\n### 建议\n"
            for i, recommendation in enumerate(recommendations[:5]):  # 只显示前5个
                report_content += f"{i+1}. {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总趋势数量**：{len(trends)}\n"
        report_content += f"- **总建议数量**：{len(recommendations)}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'tech_tracking',
            'generated_at': datetime.now().isoformat(),
            'tracking_data': tracking_data,
            'summary': {
                'total_trends': len(tracking_data.get('trends', [])),
                'total_recommendations': len(tracking_data.get('recommendations', []))
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'tech_tracking_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'tech_tracking_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 技术追踪报告已生成：{output_file}")
    return output_file


def generate_summary_report(reports: List[Dict[str, Any]], 
                          output_format: str = 'json') -> str:
    """
    生成综合报告
    
    Args:
        reports: 报告列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 综合报告

## 基本信息
- **报告ID**：SUMMARY-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}
- **报告标题**：情报综合报告
- **生成时间**：{datetime.now().isoformat()}
- **包含报告数量**：{len(reports)}

## 综合结果摘要
"""
        # 汇总所有报告的数据
        all_findings = []
        all_trends = []
        all_updates = []
        all_recommendations = []
        
        for report in reports:
            if 'findings' in report:
                all_findings.extend(report.get('findings', []))
            if 'trends' in report:
                all_trends.extend(report.get('trends', []))
            if 'updates' in report:
                all_updates.extend(report.get('updates', []))
            if 'recommendations' in report:
                all_recommendations.extend(report.get('recommendations', []))
        
        if all_findings:
            report_content += f"\n### 主要发现\n"
            for i, finding in enumerate(all_findings[:5]):  # 只显示前5个
                report_content += f"{i+1}. **{finding.get('title', '未知发现')}**\n"
                report_content += f"   - 来源：{finding.get('source', '未知来源')}\n"
        
        if all_trends:
            report_content += f"\n### 技术趋势\n"
            for i, trend in enumerate(all_trends[:5]):  # 只显示前5个
                if isinstance(trend, dict):
                    report_content += f"{i+1}. **{trend.get('title', '未知趋势')}**\n"
                else:
                    report_content += f"{i+1}. {trend}\n"
        
        if all_updates:
            report_content += f"\n### 主要更新\n"
            for i, update in enumerate(all_updates[:5]):  # 只显示前5个
                report_content += f"{i+1}. **{update.get('title', '未知更新')}**\n"
                report_content += f"   - 类型：{update.get('type', '未知类型')}\n"
        
        if all_recommendations:
            report_content += f"\n### 建议\n"
            for i, recommendation in enumerate(all_recommendations[:5]):  # 只显示前5个
                report_content += f"{i+1}. {recommendation}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **总发现数量**：{len(all_findings)}\n"
        report_content += f"- **总趋势数量**：{len(all_trends)}\n"
        report_content += f"- **总更新数量**：{len(all_updates)}\n"
        report_content += f"- **总建议数量**：{len(all_recommendations)}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'summary',
            'generated_at': datetime.now().isoformat(),
            'reports': reports,
            'summary': {
                'total_reports': len(reports),
                'total_findings': sum([len(r.get('findings', [])) for r in reports]),
                'total_trends': sum([len(r.get('trends', [])) for r in reports]),
                'total_updates': sum([len(r.get('updates', [])) for r in reports]),
                'total_recommendations': sum([len(r.get('recommendations', [])) for r in reports])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(REPORTS_DIR, f'summary_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(REPORTS_DIR, f'summary_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 综合报告已生成：{output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='报告生成工具（增强版）')
    parser.add_argument('--generate-intelligence', type=str, help='生成情报收集报告（指定情报数据JSON文件路径）')
    parser.add_argument('--generate-competitor', type=str, help='生成竞品监测报告（指定竞品数据JSON文件路径）')
    parser.add_argument('--generate-tech', type=str, help='生成技术追踪报告（指定追踪数据JSON文件路径）')
    parser.add_argument('--generate-summary', type=str, help='生成综合报告（指定报告列表JSON文件路径）')
    parser.add_argument('--output-format', type=str, choices=['json', 'markdown'], default='json', 
                        help='输出格式（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.generate_intelligence:
        print(f"🔍 正在生成情报收集报告：{args.generate_intelligence}")
        
        # 获取情报数据
        intelligence_data = {}
        if os.path.exists(args.generate_intelligence):
            with open(args.generate_intelligence, 'r', encoding='utf-8') as f:
                intelligence_data = json.load(f)
        else:
            print(f"❌ 错误：情报数据文件不存在 - {args.generate_intelligence}")
            return
        
        report_file = generate_intelligence_report(intelligence_data, args.output_format)
        if report_file:
            print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.generate_competitor:
        print(f"🔍 正在生成竞品监测报告：{args.generate_competitor}")
        
        # 获取竞品数据
        competitordata = {}
        if os.path.exists(args.generate_competitor):
            with open(args.generate_competitor, 'r', encoding='utf-8') as f:
                competitordata = json.load(f)
        else:
            print(f"❌ 错误：竞品数据文件不存在 - {args.generate_competitor}")
            return
        
        report_file = generate_competitor_report(competitordata, args.output_format)
        if report_file:
            print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.generate_tech:
        print(f"🔍 正在生成技术追踪报告：{args.generate_tech}")
        
        # 获取追踪数据
        tracking_data = {}
        if os.path.exists(args.generate_tech):
            with open(args.generate_tech, 'r', encoding='utf-8') as f:
                tracking_data = json.load(f)
        else:
            print(f"❌ 错误：追踪数据文件不存在 - {args.generate_tech}")
            return
        
        report_file = generate_tech_tracking_report(tracking_data, args.output_format)
        if report_file:
            print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.generate_summary:
        print(f"🔍 正在生成综合报告：{args.generate_summary}")
        
        # 获取报告列表
        reports = []
        if os.path.exists(args.generate_summary):
            with open(args.generate_summary, 'r', encoding='utf-8') as f:
                reports = json.load(f)
        else:
            print(f"❌ 错误：报告列表文件不存在 - {args.generate_summary}")
            return
        
        report_file = generate_summary_report(reports, args.output_format)
        if report_file:
            print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有模板或显示帮助
    print("❌ 错误：请指定报告生成类型（--generate-intelligence, --generate-competitor, --generate-tech, --generate-summary）")
    parser.print_help()
    return


if __name__ == '__main__':
    main()
