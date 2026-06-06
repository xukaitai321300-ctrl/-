#!/usr/bin/env python3
"""
需求分析工具 (Requirement Analyzer Tool)
为十二生肖团提供需求分析功能

功能：
1. 从用户输入中提取需求
2. 需求分类和优先级排序
3. 生成需求分析报告
4. 任务分拣和分配
"""

import json
import argparse
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
REQUIREMENT_DATA_FILE = os.path.join(DATA_DIR, 'requirement_analysis.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_requirement_data() -> Dict[str, Any]:
    """加载需求分析数据库"""
    try:
        with open(REQUIREMENT_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载需求分析数据库 - {e}")
        return {}


def save_requirement_data(data: Dict[str, Any]) -> bool:
    """保存需求分析数据库"""
    try:
        with open(REQUIREMENT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存需求分析数据库 - {e}")
        return False


def get_template(template_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取需求分析模板"""
    data = load_requirement_data()
    templates = data.get('requirement_analysis_templates', [])
    for template in templates:
        if template.get('id') == template_id:
            return template
    return None


def list_templates() -> None:
    """列出所有需求分析模板"""
    data = load_requirement_data()
    templates = data.get('requirement_analysis_templates', [])
    if not templates:
        print("❌ 没有找到任何需求分析模板")
        return
    
    print("📊 可用需求分析模板列表：")
    for template in templates:
        print(f"  - {template.get('id')}: {template.get('name')} ({template.get('name_zh')})")


def print_template_details(template: Dict[str, Any]) -> None:
    """打印需求分析模板详情"""
    print(f"📊 需求分析模板详情：{template.get('name')} ({template.get('name_zh')})")
    print(f"  描述：{template.get('description')}")
    print(f"  中文描述：{template.get('description_zh')}")
    
    fields = template.get('fields', [])
    fields_zh = template.get('fields_zh', [])
    print(f"\n  📋 字段列表：")
    for i, field in enumerate(fields):
        field_zh = fields_zh[i] if i < len(fields_zh) else field
        print(f"    {i+1}. {field} ({field_zh})")
    
    example = template.get('example', {})
    if example:
        print(f"\n  📝 示例数据：")
        for key, value in example.items():
            print(f"    {key}: {value}")


def extract_requirements(text: str) -> List[Dict[str, Any]]:
    """
    从文本中提取需求
    
    Args:
        text: 用户输入的文本
        
    Returns:
        提取的需求列表
    """
    requirements = []
    
    # 改进的需求提取逻辑
    # 1. 首先按中文标点符号分割文本（，。；！？）
    sentences = re.split(r'[，。；！？]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # 2. 查找包含需求关键词的句子
    requirement_keywords = ['需要', '要求', '希望', '想要', '目标', '必须', '应该', '建议']
    
    for sentence in sentences:
        # 检查句子是否包含需求关键词
        if any(keyword in sentence for keyword in requirement_keywords):
            requirements.append({
                'text': sentence,
                'source': text,
                'priority': 'medium',  # 默认优先级
                'category': 'functional',  # 默认分类
                'status': 'extracted',  # 状态：已提取
                'created_at': datetime.now().isoformat()
            })
        elif sentence:  # 如果不包含关键词但也有内容，则作为一般性需求
            requirements.append({
                'text': sentence,
                'source': text,
                'priority': 'low',  # 低优先级
                'category': 'other',  # 其他分类
                'status': 'extracted',
                'created_at': datetime.now().isoformat()
            })
    
    # 3. 如果没有提取到任何需求，则将整个文本作为一个需求
    if not requirements:
        requirements.append({
            'text': text,
            'source': text,
            'priority': 'medium',
            'category': 'functional',
            'status': 'extracted',
            'created_at': datetime.now().isoformat()
        })
    
    return requirements


def categorize_requirement(requirement: Dict[str, Any]) -> str:
    """
    对需求进行分类
    
    Args:
        requirement: 需求字典
        
    Returns:
        分类名称
    """
    text = requirement.get('text', '').lower()
    
    # 简单分类逻辑（可以根据需要扩展）
    if any(keyword in text for keyword in ['设计', '外观', '颜色', '造型', 'design', 'appearance']):
        return 'design'
    elif any(keyword in text for keyword in ['功能', '性能', '参数', 'function', 'performance']):
        return 'functionality'
    elif any(keyword in text for keyword in ['成本', '价格', '预算', 'cost', 'price', 'budget']):
        return 'cost'
    elif any(keyword in text for keyword in ['时间', '周期', '进度', 'time', 'schedule']):
        return 'schedule'
    elif any(keyword in text for keyword in ['质量', '测试', '验证', 'quality', 'test']):
        return 'quality'
    else:
        return 'other'


def prioritize_requirement(requirement: Dict[str, Any]) -> str:
    """
    确定需求优先级
    
    Args:
        requirement: 需求字典
        
    Returns:
        优先级（high/medium/low）
    """
    text = requirement.get('text', '').lower()
    
    # 简单优先级逻辑（可以根据需要扩展）
    if any(keyword in text for keyword in ['必须', '必要', '关键', 'must', 'necessary', 'critical']):
        return 'high'
    elif any(keyword in text for keyword in ['重要', '应该', 'important', 'should']):
        return 'medium'
    else:
        return 'low'


def analyze_requirements(text: str) -> Dict[str, Any]:
    """
    分析需求并生成报告
    
    Args:
        text: 用户输入的文本
        
    Returns:
        需求分析报告
    """
    # 提取需求
    requirements = extract_requirements(text)
    
    # 对每个需求进行分类和优先级排序
    for req in requirements:
        req['category'] = categorize_requirement(req)
        req['priority'] = prioritize_requirement(req)
    
    # 生成报告
    report = {
        'summary': {
            'total_requirements': len(requirements),
            'high_priority': sum(1 for r in requirements if r['priority'] == 'high'),
            'medium_priority': sum(1 for r in requirements if r['priority'] == 'medium'),
            'low_priority': sum(1 for r in requirements if r['priority'] == 'low'),
            'categories': {}
        },
        'requirements': requirements,
        'analysis_time': datetime.now().isoformat()
    }
    
    # 统计各类别需求数量
    categories = {}
    for req in requirements:
        category = req['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += 1
    report['summary']['categories'] = categories
    
    return report


def generate_report_markdown(report: Dict[str, Any]) -> str:
    """
    生成Markdown格式的需求分析报告
    
    Args:
        report: 需求分析报告
        
    Returns:
        Markdown格式的报告
    """
    md = "# 需求分析报告\n\n"
    md += f"**分析时间**: {report['analysis_time']}\n\n"
    
    md += "## 摘要\n\n"
    md += f"- **总需求数量**: {report['summary']['total_requirements']}\n"
    md += f"- **高优先级**: {report['summary']['high_priority']}\n"
    md += f"- **中优先级**: {report['summary']['medium_priority']}\n"
    md += f"- **低优先级**: {report['summary']['low_priority']}\n\n"
    
    md += "### 按类别统计\n\n"
    for category, count in report['summary']['categories'].items():
        md += f"- **{category}**: {count}\n"
    md += "\n"
    
    md += "## 需求列表\n\n"
    for i, req in enumerate(report['requirements'], 1):
        md += f"### {i}. {req['text']}\n\n"
        md += f"- **优先级**: {req['priority']}\n"
        md += f"- **类别**: {req['category']}\n"
        md += f"- **状态**: {req['status']}\n"
        md += f"- **创建时间**: {req['created_at']}\n\n"
    
    return md


def save_report(report: Dict[str, Any], output_format: str = 'json') -> str:
    """
    保存需求分析报告
    
    Args:
        report: 需求分析报告
        output_format: 输出格式（json/markdown）
        
    Returns:
        保存的文件路径
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if output_format == 'markdown':
        filename = f"requirement_analysis_report_{timestamp}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        content = generate_report_markdown(report)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:  # json
        filename = f"requirement_analysis_report_{timestamp}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(description='需求分析工具')
    parser.add_argument('--template', type=str, help='需求分析模板ID（product_design/market_research）')
    parser.add_argument('--list', action='store_true', help='列出所有需求分析模板')
    parser.add_argument('--analyze', type=str, help='分析需求文本（提供文本或文本文件路径）')
    parser.add_argument('--format', type=str, choices=['json', 'markdown'], default='json', help='输出格式（json/markdown）')
    parser.add_argument('--output', type=str, help='输出文件路径（可选）')
    
    args = parser.parse_args()
    
    if args.list:
        list_templates()
        return
    
    if args.analyze:
        # 分析需求
        text = args.analyze
        
        # 如果提供的是文件路径，则读取文件内容
        if os.path.exists(text):
            with open(text, 'r', encoding='utf-8') as f:
                text = f.read()
        
        print(f"📊 开始分析需求...")
        report = analyze_requirements(text)
        
        # 保存报告
        filepath = save_report(report, args.format)
        print(f"✅ 需求分析报告已保存至：{filepath}")
        
        # 打印摘要
        print(f"\n📊 需求分析摘要：")
        print(f"  总需求数量：{report['summary']['total_requirements']}")
        print(f"  高优先级：{report['summary']['high_priority']}")
        print(f"  中优先级：{report['summary']['medium_priority']}")
        print(f"  低优先级：{report['summary']['low_priority']}")
        
        return
    
    if args.template:
        template = get_template(args.template)
        if not template:
            print(f"❌ 错误：找不到ID为 '{args.template}' 的需求分析模板")
            list_templates()
            return
        
        print_template_details(template)
        return
    
    # 如果没有提供任何参数，则显示帮助
    parser.print_help()


if __name__ == '__main__':
    main()
