#!/usr/bin/env python3
"""
团队协调工具 (Team Coordinator Tool)
为十二生肖团提供团队协调功能
"""

import json
import argparse
import os
import sys

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
REQUIREMENT_DATA_FILE = os.path.join(DATA_DIR, 'requirement_analysis.json')


def load_requirement_data():
    """加载需求分析数据库"""
    try:
        with open(REQUIREMENT_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载需求分析数据库 - {e}")
        return {}


def get_workflow(workflow_id):
    """根据ID获取团队协调流程"""
    data = load_requirement_data()
    workflows = data.get('team_coordination_workflows', [])
    for workflow in workflows:
        if workflow.get('id') == workflow_id:
            return workflow
    return None


def list_workflows():
    """列出所有团队协调流程"""
    data = load_requirement_data()
    workflows = data.get('team_coordination_workflows', [])
    if not workflows:
        print("❌ 没有找到任何团队协调流程")
        return
    
    print("📊 可用团队协调流程列表：")
    for workflow in workflows:
        print(f"  - {workflow.get('id')}: {workflow.get('name')} ({workflow.get('name_zh')})")


def print_workflow_details(workflow):
    """打印团队协调流程详情"""
    print(f"📊 团队协调流程详情：{workflow.get('name')} ({workflow.get('name_zh')})")
    print(f"  描述：{workflow.get('description')}")
    print(f"  中文描述：{workflow.get('description_zh')}")
    
    steps = workflow.get('steps', [])
    steps_zh = workflow.get('steps_zh', [])
    print(f"\n  🔄 流程步骤：")
    for i, step in enumerate(steps):
        step_zh = steps_zh[i] if i < len(steps_zh) else step
        print(f"    {i+1}. {step}")
        print(f"       {step_zh}")


def main():
    parser = argparse.ArgumentParser(description='团队协调工具')
    parser.add_argument('--workflow', type=str, help='团队协调流程ID（design_to_production/market_research_to_design）')
    parser.add_argument('--list', action='store_true', help='列出所有团队协调流程')
    
    args = parser.parse_args()
    
    if args.list:
        list_workflows()
        return
    
    if not args.workflow:
        print("❌ 错误：请指定团队协调流程ID（使用 --workflow）或列出所有流程（使用 --list）")
        parser.print_help()
        return
    
    workflow = get_workflow(args.workflow)
    if not workflow:
        print(f"❌ 错误：找不到ID为 '{args.workflow}' 的团队协调流程")
        list_workflows()
        return
    
    print_workflow_details(workflow)


if __name__ == '__main__':
    main()
