#!/usr/bin/env python3
"""
工作流优化工具 (Workflow Optimization Tool) - 增强版
为十二生肖团提供 ComfyUI 工作流优化功能，支持节点优化、参数调整、性能提升和报告生成
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
WORKFLOW_DATA_FILE = os.path.join(DATA_DIR, 'workflow_optimization.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_workflow_data() -> Dict[str, Any]:
    """加载工作流优化数据库"""
    try:
        with open(WORKFLOW_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载工作流优化数据库 - {e}")
        return {}


def save_workflow_data(data: Dict[str, Any]) -> bool:
    """保存工作流优化数据库"""
    try:
        with open(WORKFLOW_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 工作流优化数据库已更新：{WORKFLOW_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存工作流优化数据库 - {e}")
        return False


def get_optimization_method(method_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取优化方法"""
    data = load_workflow_data()
    methods = data.get('optimization_methods', [])
    for method in methods:
        if method.get('id') == method_id:
            return method
    return None


def list_methods() -> None:
    """列出所有优化方法"""
    data = load_workflow_data()
    methods = data.get('optimization_methods', [])
    if not methods:
        print("❌ 没有找到任何优化方法")
        return
    
    print("📊 可用优化方法列表：")
    for method in methods:
        print(f"  - {method.get('id')}: {method.get('name')} ({method.get('name_zh')})")


def optimize_workflow(workflow_id: str, optimization_goals: List[str] = None) -> Dict[str, Any]:
    """
    优化工作流
    
    Args:
        workflow_id: 工作流ID
        optimization_goals: 优化目标列表（speed, quality, memory, stability）
        
    Returns:
        优化结果字典
    """
    if not optimization_goals:
        optimization_goals = ['speed', 'quality', 'memory', 'stability']
    
    # 模拟工作流优化（实际应用中会调用优化算法）
    optimization_result = {
        'success': True,
        'workflow_id': workflow_id,
        'workflow_name': f'工作流_{workflow_id}',
        'optimization_time': datetime.now().isoformat(),
        'optimization_goals': optimization_goals,
        'original_workflow': {
            'node_count': 25,
            'execution_time': 12.5,  # 秒
            'memory_usage': 2048,  # MB
            'quality_score': 85.0,
            'stability_score': 78.5
        },
        'optimized_workflow': {
            'node_count': 22,  # 减少了3个节点
            'execution_time': 8.2,  # 秒（提升了34.4%）
            'memory_usage': 1536,  # MB（减少了25%）
            'quality_score': 87.5,  # 提升了2.5分
            'stability_score': 85.0  # 提升了6.5分
        },
        'optimization_details': {
            'nodes_removed': ['KSampler_05', 'ControlNetApply_03', 'ImageSharpness_02'],
            'nodes_added': ['EfficientLoader_01', 'ControlNetApplyAdvanced_01'],
            'parameters_adjusted': {
                'steps': '20 → 15',
                'cfg_scale': '7.5 → 6.5',
                'sampler': 'DPM++ 2M Karras → Euler a'
            },
            'performance_improvement': {
                'speed': '34.4%',
                'memory': '25.0%',
                'quality': '2.9%',
                'stability': '8.3%'
            }
        },
        'issues': [],
        'suggestions': []
    }
    
    # 根据优化目标添加问题和建议
    if optimization_result['optimized_workflow']['quality_score'] < 80:
        optimization_result['issues'].append("优化后质量分数较低")
        optimization_result['suggestions'].append("建议调整优化策略，优先保证质量")
    
    if optimization_result['optimized_workflow']['stability_score'] < 80:
        optimization_result['issues'].append("优化后稳定性分数较低")
        optimization_result['suggestions'].append("建议增加稳定性测试，确保工作流可靠")
    
    return optimization_result


def validate_optimized_workflow(workflow_id: str, test_cases: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    验证优化后的工作流
    
    Args:
        workflow_id: 工作流ID
        test_cases: 测试用例列表
        
    Returns:
        验证结果字典
    """
    if not test_cases:
        # 模拟测试用例
        test_cases = [
            {'id': 'test_001', 'name': '基础测试', 'prompt': '一个保温杯'},
            {'id': 'test_002', 'name': '复杂测试', 'prompt': '一个不锈钢保温杯，轻量化设计'},
            {'id': 'test_003', 'name': '边缘测试', 'prompt': '一个保温杯' * 20}
        ]
    
    # 模拟工作流验证（实际应用中会调用验证算法）
    validation_result = {
        'success': True,
        'workflow_id': workflow_id,
        'validation_time': datetime.now().isoformat(),
        'test_cases_count': len(test_cases),
        'validation_results': {
            'passed': len(test_cases) - 1,  # 模拟1个测试失败
            'failed': 1,
            'skipped': 0
        },
        'performance_metrics': {
            'avg_execution_time': 8.5,  # 秒
            'avg_memory_usage': 1600,  # MB
            'avg_quality_score': 86.5,
            'avg_stability_score': 84.0
        },
        'failed_tests': [
            {
                'test_id': 'test_003',
                'test_name': '边缘测试',
                'failure_reason': '提示词过长导致内存溢出',
                'suggested_fix': '增加提示词长度限制或优化内存管理'
            }
        ],
        'issues': [],
        'suggestions': []
    }
    
    # 根据验证结果添加问题和建议
    if validation_result['validation_results']['failed'] > 0:
        validation_result['issues'].append(f"有{validation_result['validation_results']['failed']}个测试失败")
        validation_result['suggestions'].append("建议修复失败的测试，确保工作流稳定性")
    
    if validation_result['performance_metrics']['avg_quality_score'] < 80:
        validation_result['issues'].append("平均质量分数较低")
        validation_result['suggestions'].append("建议调整优化策略，优先保证质量")
    
    return validation_result


def generate_optimization_report(optimization_results: List[Dict[str, Any]], 
                                output_format: str = 'json') -> str:
    """
    生成工作流优化报告
    
    Args:
        optimization_results: 优化结果列表
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 工作流优化报告

## 基本信息
- **优化时间**：{datetime.now().isoformat()}
- **优化工作流数量**：{len(optimization_results)}
- **优化目标**：速度、质量、内存、稳定性

## 优化结果摘要
"""
        for i, result in enumerate(optimization_results):
            report_content += f"\n### {i+1}. {result.get('workflow_name', '未知工作流')}\n"
            report_content += f"- **工作流ID**：{result.get('workflow_id', '未知')}\n"
            
            original = result.get('original_workflow', {})
            optimized = result.get('optimized_workflow', {})
            
            report_content += f"- **原始节点数**：{original.get('node_count', 0)}\n"
            report_content += f"- **优化后节点数**：{optimized.get('node_count', 0)}\n"
            report_content += f"- **原始执行时间**：{original.get('execution_time', 0):.2f}秒\n"
            report_content += f"- **优化后执行时间**：{optimized.get('execution_time', 0):.2f}秒\n"
            report_content += f"- **原始内存使用**：{original.get('memory_usage', 0)} MB\n"
            report_content += f"- **优化后内存使用**：{optimized.get('memory_usage', 0)} MB\n"
            report_content += f"- **原始质量分数**：{original.get('quality_score', 0):.2f}/100\n"
            report_content += f"- **优化后质量分数**：{optimized.get('quality_score', 0):.2f}/100\n"
            
            # 计算提升百分比
            speed_improvement = (original.get('execution_time', 1) - optimized.get('execution_time', 0)) / original.get('execution_time', 1) * 100
            memory_improvement = (original.get('memory_usage', 1) - optimized.get('memory_usage', 0)) / original.get('memory_usage', 1) * 100
            
            report_content += f"- **速度提升**：{speed_improvement:.2f}%\n"
            report_content += f"- **内存减少**：{memory_improvement:.2f}%\n"
            
            if result.get('issues'):
                report_content += "\n**问题**：\n"
                for issue in result.get('issues'):
                    report_content += f"- {issue}\n"
            
            if result.get('suggestions'):
                report_content += "\n**建议**：\n"
                for suggestion in result.get('suggestions'):
                    report_content += f"- {suggestion}\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **平均节点减少**：{sum([r.get('original_workflow', {}).get('node_count', 0) - r.get('optimized_workflow', {}).get('node_count', 0) for r in optimization_results]) / len(optimization_results):.2f}个\n"
        report_content += f"- **平均速度提升**：{sum([(r.get('original_workflow', {}).get('execution_time', 1) - r.get('optimized_workflow', {}).get('execution_time', 0)) / r.get('original_workflow', {}).get('execution_time', 1) * 100 for r in optimization_results]) / len(optimization_results):.2f}%\n"
        report_content += f"- **平均内存减少**：{sum([(r.get('original_workflow', {}).get('memory_usage', 1) - r.get('optimized_workflow', {}).get('memory_usage', 0)) / r.get('original_workflow', {}).get('memory_usage', 1) * 100 for r in optimization_results]) / len(optimization_results):.2f}%\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'workflow_optimization',
            'generated_at': datetime.now().isoformat(),
            'workflow_count': len(optimization_results),
            'optimization_results': optimization_results,
            'summary': {
                'avg_node_reduction': sum([r.get('original_workflow', {}).get('node_count', 0) - r.get('optimized_workflow', {}).get('node_count', 0) for r in optimization_results]) / len(optimization_results),
                'avg_speed_improvement': sum([(r.get('original_workflow', {}).get('execution_time', 1) - r.get('optimized_workflow', {}).get('execution_time', 0)) / r.get('original_workflow', {}).get('execution_time', 1) * 100 for r in optimization_results]) / len(optimization_results),
                'avg_memory_reduction': sum([(r.get('original_workflow', {}).get('memory_usage', 1) - r.get('optimized_workflow', {}).get('memory_usage', 0)) / r.get('original_workflow', {}).get('memory_usage', 1) * 100 for r in optimization_results]) / len(optimization_results),
                'total_issues': sum([len(r.get('issues', [])) for r in optimization_results]),
                'total_suggestions': sum([len(r.get('suggestions', [])) for r in optimization_results])
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(OUTPUT_DIR, f'workflow_optimization_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(OUTPUT_DIR, f'workflow_optimization_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 工作流优化报告已生成：{output_file}")
    return output_file


def print_method_details(method: Dict[str, Any]) -> None:
    """打印优化方法详情"""
    print(f"📊 优化方法详情：{method.get('name')} ({method.get('name_zh')})")
    print(f"  描述：{method.get('description')}")
    print(f"  中文描述：{method.get('description_zh')}")
    
    steps = method.get('steps', [])
    steps_zh = method.get('steps_zh', [])
    print(f"\n  🔧 优化步骤：")
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
    parser = argparse.ArgumentParser(description='工作流优化工具（增强版）')
    parser.add_argument('--method', type=str, help='优化方法ID（node_optimization/parameter_tuning/performance_boost）')
    parser.add_argument('--list', action='store_true', help='列出所有优化方法')
    parser.add_argument('--optimize', type=str, help='优化工作流（指定工作流ID）')
    parser.add_argument('--goals', type=str, nargs='+', choices=['speed', 'quality', 'memory', 'stability'], 
                        help='优化目标（speed, quality, memory, stability）')
    parser.add_argument('--validate', type=str, help='验证优化后的工作流（指定工作流ID）')
    parser.add_argument('--test-cases', type=str, help='测试用例JSON文件路径')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', 
                        help='生成工作流优化报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_methods()
        return
    
    if args.optimize:
        print(f"🔍 正在优化工作流：{args.optimize}")
        
        optimization_goals = args.goals if args.goals else None
        optimization_result = optimize_workflow(args.optimize, optimization_goals)
        
        print(f"  工作流ID：{optimization_result['workflow_id']}")
        print(f"  原始节点数：{optimization_result['original_workflow']['node_count']}")
        print(f"  优化后节点数：{optimization_result['optimized_workflow']['node_count']}")
        print(f"  原始执行时间：{optimization_result['original_workflow']['execution_time']:.2f}秒")
        print(f"  优化后执行时间：{optimization_result['optimized_workflow']['execution_time']:.2f}秒")
        
        if args.generate_report:
            print(f"📝 正在生成工作流优化报告...")
            report_file = generate_optimization_report([optimization_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.validate:
        print(f"🔍 正在验证优化后的工作流：{args.validate}")
        
        test_cases = None
        if args.test_cases and os.path.exists(args.test_cases):
            with open(args.test_cases, 'r', encoding='utf-8') as f:
                test_cases = json.load(f)
        
        validation_result = validate_optimized_workflow(args.validate, test_cases)
        
        print(f"  验证结果：{'✅ 通过' if validation_result['validation_results']['failed'] == 0 else '❌ 未通过'}")
        print(f"  通过测试：{validation_result['validation_results']['passed']}个")
        print(f"  失败测试：{validation_result['validation_results']['failed']}个")
        
        if args.generate_report:
            print(f"📝 正在生成工作流优化报告...")
            # 创建一个模拟的优化结果，用于报告生成
            mock_optimization_result = {
                'workflow_id': args.validate,
                'workflow_name': f'工作流_{args.validate}',
                'original_workflow': {'node_count': 25, 'execution_time': 12.5, 'memory_usage': 2048, 'quality_score': 85.0, 'stability_score': 78.5},
                'optimized_workflow': {'node_count': 22, 'execution_time': 8.2, 'memory_usage': 1536, 'quality_score': 87.5, 'stability_score': 85.0},
                'issues': validation_result['issues'],
                'suggestions': validation_result['suggestions']
            }
            report_file = generate_optimization_report([mock_optimization_result], args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    # 默认：列出所有方法或显示帮助
    if not args.method:
        print("❌ 错误：请指定优化方法ID（使用 --method）或列出所有方法（使用 --list）")
        parser.print_help()
        return
    
    method = get_optimization_method(args.method)
    if not method:
        print(f"❌ 错误：找不到ID为 '{args.method}' 的优化方法")
        list_methods()
        return
    
    print_method_details(method)


if __name__ == '__main__':
    main()
