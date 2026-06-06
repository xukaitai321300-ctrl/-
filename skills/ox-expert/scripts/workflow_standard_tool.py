#!/usr/bin/env python3
"""
工作流标准工具 (Workflow Standard Tool) - 增强版
为十二生肖团提供 ComfyUI 工作流标准功能，支持工作流验证、标准检查和报告生成
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
WORKFLOW_DATA_FILE = os.path.join(DATA_DIR, 'workflow_standards.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_workflow_data() -> Dict[str, Any]:
    """加载工作流标准数据库"""
    try:
        with open(WORKFLOW_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载工作流标准数据库 - {e}")
        return {}


def save_workflow_data(data: Dict[str, Any]) -> bool:
    """保存工作流标准数据库"""
    try:
        with open(WORKFLOW_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 工作流标准数据库已更新：{WORKFLOW_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存工作流标准数据库 - {e}")
        return False


def get_workflow_standard(workflow_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取工作流标准"""
    data = load_workflow_data()
    workflows = data.get('workflow_standards', [])
    for workflow in workflows:
        if workflow.get('id') == workflow_id:
            return workflow
    return None


def list_workflows() -> None:
    """列出所有工作流标准"""
    data = load_workflow_data()
    workflows = data.get('workflow_standards', [])
    if not workflows:
        print("❌ 没有找到任何工作流标准")
        return
    
    print("📊 可用工作流标准列表：")
    for workflow in workflows:
        print(f"  - {workflow.get('id')}: {workflow.get('name')} ({workflow.get('name_zh')})")


def validate_workflow(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """
    验证工作流是否符合标准
    
    Args:
        workflow: 工作流数据
        
    Returns:
        验证结果字典
    """
    validation_result = {
        'is_valid': True,
        'score': 100,
        'issues': [],
        'suggestions': []
    }
    
    # 检查必需字段
    required_fields = ['id', 'name', 'name_zh', 'description', 'description_zh', 'standard_nodes', 'example_workflow']
    for field in required_fields:
        if field not in workflow:
            validation_result['is_valid'] = False
            validation_result['score'] -= 20
            validation_result['issues'].append(f"缺少必需字段：{field}")
    
    # 检查标准节点
    standard_nodes = workflow.get('standard_nodes', [])
    if not standard_nodes:
        validation_result['is_valid'] = False
        validation_result['score'] -= 15
        validation_result['issues'].append("没有定义标准节点")
    else:
        # 检查每个节点的必需字段
        for i, node in enumerate(standard_nodes):
            if 'node_type' not in node:
                validation_result['score'] -= 5
                validation_result['issues'].append(f"节点 {i+1} 缺少 node_type 字段")
    
    # 检查示例工作流
    example = workflow.get('example_workflow', {})
    if not example:
        validation_result['score'] -= 10
        validation_result['suggestions'].append("建议添加示例工作流")
    else:
        if 'node_count' not in example:
            validation_result['score'] -= 5
            validation_result['suggestions'].append("示例工作流建议包含节点数量信息")
    
    return validation_result


def check_workflow_compliance(workflow_id: str) -> Dict[str, Any]:
    """
    检查工作流是否符合标准
    
    Args:
        workflow_id: 工作流ID
        
    Returns:
        合规性检查结果
    """
    workflow = get_workflow_standard(workflow_id)
    if not workflow:
        return {
            'success': False,
            'error': f"找不到ID为 '{workflow_id}' 的工作流标准"
        }
    
    validation_result = validate_workflow(workflow)
    
    return {
        'success': True,
        'workflow_id': workflow_id,
        'workflow_name': workflow.get('name'),
        'workflow_name_zh': workflow.get('name_zh'),
        'validation_result': validation_result,
        'checked_at': datetime.now().isoformat()
    }


def generate_standard_report(workflow_id: str, output_format: str = 'json') -> str:
    """
    生成工作流标准报告
    
    Args:
        workflow_id: 工作流ID
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    compliance_result = check_workflow_compliance(workflow_id)
    
    if not compliance_result.get('success'):
        print(f"❌ 错误：{compliance_result.get('error')}")
        return ""
    
    # 生成报告内容
    workflow = get_workflow_standard(workflow_id)
    validation = compliance_result['validation_result']
    
    if output_format == 'markdown':
        report_content = f"""# 工作流标准报告：{workflow.get('name')} ({workflow.get('name_zh')})

## 基本信息
- **工作流ID**：{workflow_id}
- **英文名称**：{workflow.get('name')}
- **中文名称**：{workflow.get('name_zh')}
- **检查时间**：{compliance_result['checked_at']}

## 验证结果
- **是否有效**：{'✅ 是' if validation['is_valid'] else '❌ 否'}
- **合规分数**：{validation['score']}/100
- **问题数量**：{len(validation['issues'])}
- **建议数量**：{len(validation['suggestions'])}

## 问题描述
"""
        if validation['issues']:
            for i, issue in enumerate(validation['issues']):
                report_content += f"{i+1}. {issue}\n"
        else:
            report_content += "✅ 没有发现问题\n"
        
        report_content += "\n## 改进建议\n"
        if validation['suggestions']:
            for i, suggestion in enumerate(validation['suggestions']):
                report_content += f"{i+1}. {suggestion}\n"
        else:
            report_content += "✅ 没有改进建议\n"
        
        report_content += f"\n## 标准节点列表\n"
        standard_nodes = workflow.get('standard_nodes', [])
        for i, node in enumerate(standard_nodes):
            report_content += f"{i+1}. {node.get('node_type')} ({node.get('node_type_zh', '')})\n"
        
        report_content += f"\n## 示例工作流\n"
        example = workflow.get('example_workflow', {})
        if example:
            report_content += f"- **名称**：{example.get('name', '')}\n"
            report_content += f"- **中文名称**：{example.get('name_zh', '')}\n"
            report_content += f"- **节点数量**：{example.get('node_count', '')}\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'workflow_standard',
            'workflow_id': workflow_id,
            'workflow_name': workflow.get('name'),
            'workflow_name_zh': workflow.get('name_zh'),
            'checked_at': compliance_result['checked_at'],
            'validation_result': validation,
            'workflow_details': workflow
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(OUTPUT_DIR, f'workflow_standard_report_{workflow_id}_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(OUTPUT_DIR, f'workflow_standard_report_{workflow_id}_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 工作流标准报告已生成：{output_file}")
    return output_file


def print_workflow_details(workflow: Dict[str, Any]) -> None:
    """打印工作流标准详情"""
    print(f"📊 工作流标准详情：{workflow.get('name')} ({workflow.get('name_zh')})")
    print(f"  描述：{workflow.get('description')}")
    print(f"  中文描述：{workflow.get('description_zh')}")
    
    nodes = workflow.get('standard_nodes', [])
    print(f"\n  🔧 标准节点列表：")
    for i, node in enumerate(nodes):
        print(f"    {i+1}. {node.get('node_type')} ({node.get('node_type_zh', '')})")
    
    example = workflow.get('example_workflow', {})
    if example:
        print(f"\n  📝 示例工作流：")
        print(f"    名称：{example.get('name')}")
        print(f"    中文名称：{example.get('name_zh')}")
        print(f"    节点数量：{example.get('node_count')}")


def main():
    parser = argparse.ArgumentParser(description='工作流标准工具（增强版）')
    parser.add_argument('--workflow', type=str, help='工作流标准ID（text_to_image/image_to_image/inpainting）')
    parser.add_argument('--list', action='store_true', help='列出所有工作流标准')
    parser.add_argument('--validate', action='store_true', help='验证工作流是否符合标准')
    parser.add_argument('--check-compliance', action='store_true', help='检查工作流合规性')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', help='生成工作流标准报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_workflows()
        return
    
    if not args.workflow:
        print("❌ 错误：请指定工作流标准ID（使用 --workflow）或列出所有工作流标准（使用 --list）")
        parser.print_help()
        return
    
    workflow = get_workflow_standard(args.workflow)
    if not workflow:
        print(f"❌ 错误：找不到ID为 '{args.workflow}' 的工作流标准")
        list_workflows()
        return
    
    if args.validate:
        print(f"🔍 正在验证工作流：{args.workflow}")
        validation_result = validate_workflow(workflow)
        print(f"  是否有效：{'✅ 是' if validation_result['is_valid'] else '❌ 否'}")
        print(f"  合规分数：{validation_result['score']}/100")
        if validation_result['issues']:
            print("  问题：")
            for issue in validation_result['issues']:
                print(f"    - {issue}")
        if validation_result['suggestions']:
            print("  建议：")
            for suggestion in validation_result['suggestions']:
                print(f"    - {suggestion}")
        return
    
    if args.check_compliance:
        print(f"🔍 正在检查工作流合规性：{args.workflow}")
        report_file = generate_standard_report(args.workflow, args.generate_report)
        if report_file:
            print(f"✅ 合规性检查完成，报告已生成：{report_file}")
        return
    
    # 默认：打印工作流详情
    print_workflow_details(workflow)


if __name__ == '__main__':
    main()
