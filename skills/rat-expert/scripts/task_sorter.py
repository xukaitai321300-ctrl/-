#!/usr/bin/env python3
"""
任务分拣工具 (Task Sorter Tool)
为十二生肖团提供任务分拣功能

功能：
1. 根据优先级、依赖关系、专业领域等规则对任务进行排序
2. 生成任务调度计划
3. 输出任务列表（JSON、Markdown格式）
"""

import json
import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import re

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


def get_task_sorting_rule(rule_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取任务分拣规则"""
    data = load_requirement_data()
    rules = data.get('task_sorting_rules', [])
    for rule in rules:
        if rule.get('id') == rule_id:
            return rule
    return None


def list_rules() -> None:
    """列出所有任务分拣规则"""
    data = load_requirement_data()
    rules = data.get('task_sorting_rules', [])
    if not rules:
        print("❌ 没有找到任何任务分拣规则")
        return
    
    print("📊 可用任务分拣规则列表：")
    for rule in rules:
        print(f"  - {rule.get('id')}: {rule.get('name')} ({rule.get('name_zh')})")


def print_rule_details(rule: Dict[str, Any]) -> None:
    """打印任务分拣规则详情"""
    print(f"📊 任务分拣规则详情：{rule.get('name')} ({rule.get('name_zh')})")
    print(f"  描述：{rule.get('description')}")
    print(f"  中文描述：{rule.get('description_zh')}")
    print(f"  规则：{rule.get('rule')}")
    print(f"  中文规则：{rule.get('rule_zh')}")
    
    example = rule.get('example', '')
    if example:
        print(f"  示例：{example}")
        # 尝试获取中文示例
        example_zh = rule.get('example_zh', '')
        if example_zh:
            print(f"  中文示例：{example_zh}")


def sort_tasks_by_priority(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    按优先级排序任务（高 > 中 > 低）
    
    Args:
        tasks: 任务列表
        
    Returns:
        排序后的任务列表
    """
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    return sorted(tasks, key=lambda x: priority_order.get(x.get('priority', 'low'), 2))


def sort_tasks_by_dependency(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    按依赖关系排序任务（无依赖的任务优先）
    
    Args:
        tasks: 任务列表
        
    Returns:
        排序后的任务列表
    """
    # 构建依赖图
    task_ids = {task['id'] for task in tasks}
    dependency_graph = {}
    
    for task in tasks:
        task_id = task['id']
        dependencies = task.get('dependencies', [])
        # 只保留存在于任务列表中的依赖
        valid_deps = [dep for dep in dependencies if dep in task_ids]
        dependency_graph[task_id] = valid_deps
    
    # 拓扑排序
    sorted_tasks = []
    visited = set()
    
    def visit(task_id):
        if task_id in visited:
            return
        visited.add(task_id)
        
        # 先访问依赖
        for dep in dependency_graph.get(task_id, []):
            visit(dep)
        
        # 添加当前任务
        for task in tasks:
            if task['id'] == task_id:
                sorted_tasks.append(task)
                break
    
    # 访问所有任务
    for task in tasks:
        visit(task['id'])
    
    return sorted_tasks


def sort_tasks_by_expertise(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    按专业领域排序任务（相同领域的任务放在一起）
    
    Args:
        tasks: 任务列表
        
    Returns:
        排序后的任务列表
    """
    # 按expertise字段分组
    expertise_groups = {}
    for task in tasks:
        expertise = task.get('expertise', 'other')
        if expertise not in expertise_groups:
            expertise_groups[expertise] = []
        expertise_groups[expertise].append(task)
    
    # 按领域名称排序
    sorted_tasks = []
    for expertise in sorted(expertise_groups.keys()):
        sorted_tasks.extend(expertise_groups[expertise])
    
    return sorted_tasks


def generate_task_schedule(tasks: List[Dict[str, Any]], rule: str) -> Dict[str, Any]:
    """
    生成任务调度计划
    
    Args:
        tasks: 排序后的任务列表
        rule: 排序规则
        
    Returns:
        任务调度计划
    """
    schedule = {
        'rule': rule,
        'total_tasks': len(tasks),
        'schedule_time': datetime.now().isoformat(),
        'tasks': []
    }
    
    # 为每个任务分配预计开始时间和结束时间
    current_time = 0  # 假设从0开始（单位：小时）
    
    for task in tasks:
        duration = task.get('estimated_duration', 1)  # 默认1小时
        
        task_schedule = {
            'id': task['id'],
            'name': task['name'],
            'priority': task.get('priority', 'low'),
            'expertise': task.get('expertise', 'other'),
            'start_time': current_time,
            'end_time': current_time + duration,
            'duration': duration,
            'dependencies': task.get('dependencies', [])
        }
        
        schedule['tasks'].append(task_schedule)
        current_time += duration
    
    # 计算总时长
    schedule['total_duration'] = current_time
    
    return schedule


def generate_schedule_markdown(schedule: Dict[str, Any]) -> str:
    """
    生成Markdown格式的任务调度计划
    
    Args:
        schedule: 任务调度计划
        
    Returns:
        Markdown格式的调度计划
    """
    md = "# 任务调度计划\n\n"
    md += f"**排序规则**: {schedule['rule']}\n"
    md += f"**生成时间**: {schedule['schedule_time']}\n"
    md += f"**总任务数**: {schedule['total_tasks']}\n"
    md += f"**总时长**: {schedule['total_duration']} 小时\n\n"
    
    md += "## 任务列表\n\n"
    md += "| 序号 | 任务ID | 任务名称 | 优先级 | 专业领域 | 开始时间 | 结束时间 | 时长 |\n"
    md += "|------|--------|----------|--------|----------|----------|----------|------|\n"
    
    for i, task in enumerate(schedule['tasks'], 1):
        md += f"| {i} | {task['id']} | {task['name']} | {task['priority']} | {task['expertise']} | {task['start_time']} | {task['end_time']} | {task['duration']} |\n"
    
    return md


def save_schedule(schedule: Dict[str, Any], output_format: str = 'json') -> str:
    """
    保存任务调度计划
    
    Args:
        schedule: 任务调度计划
        output_format: 输出格式（json/markdown）
        
    Returns:
        保存的文件路径
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if output_format == 'markdown':
        filename = f"task_schedule_{timestamp}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        content = generate_schedule_markdown(schedule)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:  # json
        filename = f"task_schedule_{timestamp}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, ensure_ascii=False, indent=2)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(description='任务分拣工具')
    parser.add_argument('--rule', type=str, choices=['by_priority', 'by_dependency', 'by_expertise'], 
                        default='by_priority', help='任务分拣规则')
    parser.add_argument('--list', action='store_true', help='列出所有任务分拣规则')
    parser.add_argument('--tasks', type=str, help='任务列表文件路径（JSON格式）')
    parser.add_argument('--format', type=str, choices=['json', 'markdown'], default='json', help='输出格式（json/markdown）')
    
    args = parser.parse_args()
    
    if args.list:
        list_rules()
        return
    
    if not args.tasks:
        print("❌ 错误：请指定任务列表文件（使用 --tasks）")
        parser.print_help()
        return
    
    # 加载任务列表
    try:
        with open(args.tasks, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
    except Exception as e:
        print(f"❌ 错误：无法加载任务列表文件 - {e}")
        return
    
    # 根据规则排序任务
    if args.rule == 'by_priority':
        sorted_tasks = sort_tasks_by_priority(tasks)
    elif args.rule == 'by_dependency':
        sorted_tasks = sort_tasks_by_dependency(tasks)
    elif args.rule == 'by_expertise':
        sorted_tasks = sort_tasks_by_expertise(tasks)
    else:
        sorted_tasks = tasks
    
    # 生成任务调度计划
    schedule = generate_task_schedule(sorted_tasks, args.rule)
    
    # 保存调度计划
    filepath = save_schedule(schedule, args.format)
    print(f"✅ 任务调度计划已保存至：{filepath}")
    
    # 打印摘要
    print(f"\n📊 任务调度摘要：")
    print(f"  排序规则：{args.rule}")
    print(f"  总任务数：{schedule['total_tasks']}")
    print(f"  总时长：{schedule['total_duration']} 小时")
    
    # 打印前5个任务
    print(f"\n📋 前5个任务：")
    for i, task in enumerate(schedule['tasks'][:5], 1):
        print(f"  {i}. {task['name']} (优先级: {task['priority']}, 专业领域: {task['expertise']})")
    
    if len(schedule['tasks']) > 5:
        print(f"  ... 还有 {len(schedule['tasks']) - 5} 个任务")


if __name__ == '__main__':
    main()
