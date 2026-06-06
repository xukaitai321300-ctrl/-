#!/usr/bin/env python3
"""
产品设计工具 (Product Design Tool) - 增强版
为十二生肖团提供产品设计功能，支持需求分析、概念设计、详细设计、设计验证和报告生成
"""

import json
import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional

# 获取数据文件路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
DESIGN_DATA_FILE = os.path.join(DATA_DIR, 'design_process.json')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
VERSIONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'versions')

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(VERSIONS_DIR, exist_ok=True)


def load_design_data() -> Dict[str, Any]:
    """加载产品设计数据库"""
    try:
        with open(DESIGN_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"❌ 错误：无法加载产品设计数据库 - {e}")
        return {}


def save_design_data(data: Dict[str, Any]) -> bool:
    """保存产品设计数据库"""
    try:
        with open(DESIGN_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 产品设计数据库已更新：{DESIGN_DATA_FILE}")
        return True
    except Exception as e:
        print(f"❌ 错误：无法保存产品设计数据库 - {e}")
        return False


def get_design_stage(stage_id: str) -> Optional[Dict[str, Any]]:
    """根据ID获取设计阶段"""
    data = load_design_data()
    stages = data.get('design_process', [])
    for stage in stages:
        if stage.get('id') == stage_id:
            return stage
    return None


def list_stages() -> None:
    """列出所有设计阶段"""
    data = load_design_data()
    stages = data.get('design_process', [])
    if not stages:
        print("❌ 没有找到任何设计阶段")
        return
    
    print("📊 可用设计阶段列表：")
    for stage in stages:
        print(f"  - {stage.get('id')}: {stage.get('name')} ({stage.get('name_zh')})")


def analyze_requirements(requirements: List[str]) -> Dict[str, Any]:
    """
    分析设计需求
    
    Args:
        requirements: 需求列表
        
    Returns:
        需求分析结果字典
    """
    # 模拟需求分析（实际应用中会调用NLP模型）
    analysis_result = {
        'success': True,
        'requirements_count': len(requirements),
        'analysis_time': datetime.now().isoformat(),
        'requirement_categories': {
            'functional': len([r for r in requirements if '功能' in r or 'function' in r.lower()]),
            'aesthetic': len([r for r in requirements if '外观' in r or 'aesthetic' in r.lower()]),
            'technical': len([r for r in requirements if '技术' in r or 'technical' in r.lower()]),
            'market': len([r for r in requirements if '市场' in r or 'market' in r.lower()])
        },
        'priority_distribution': {
            'high': len([r for r in requirements if '必须' in r or '必须' in r or 'required' in r.lower()]),
            'medium': len([r for r in requirements if '希望' in r or '希望' in r or 'should' in r.lower()]),
            'low': len([r for r in requirements if '可以' in r or '可以' in r or 'could' in r.lower()])
        },
        'feasibility_analysis': {
            'high': len([r for r in requirements if '可行' in r or '可行' in r or 'feasible' in r.lower()]),
            'medium': len([r for r in requirements if '考虑' in r or '考虑' in r or 'consider' in r.lower()]),
            'low': len([r for r in requirements if '困难' in r or '困难' in r or 'difficult' in r.lower()])
        },
        'issues': [],
        'suggestions': []
    }
    
    # 检查需求完整性
    if analysis_result['requirements_count'] < 3:
        analysis_result['issues'].append("需求数量不足，建议补充更多需求")
        analysis_result['suggestions'].append("建议从功能、外观、技术、市场等多个角度补充需求")
    
    # 检查需求分类平衡性
    categories = analysis_result['requirement_categories']
    if max(categories.values()) > sum(categories.values()) * 0.6:
        analysis_result['issues'].append("需求分类不平衡，某一类需求过多")
        analysis_result['suggestions'].append("建议平衡各类需求，确保产品设计全面性")
    
    return analysis_result


def generate_design_concept(requirements_analysis: Dict[str, Any], 
                           style_preferences: List[str] = None) -> Dict[str, Any]:
    """
    生成设计方案
    
    Args:
        requirements_analysis: 需求分析结果
        style_preferences: 风格偏好列表
        
    Returns:
        设计方案字典
    """
    if not style_preferences:
        style_preferences = ['minimalist', 'modern', 'functional']
    
    # 模拟设计方案生成（实际应用中会调用设计生成模型）
    design_concept = {
        'success': True,
        'concept_id': f"concept_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'generation_time': datetime.now().isoformat(),
        'based_on_requirements': requirements_analysis.get('requirements_count', 0),
        'style_preferences': style_preferences,
        'design_elements': {
            'shape': 'cylindrical with ergonomic grip',
            'materials': ['304 stainless steel', 'food-grade PP', 'silicone'],
            'colors': ['silver', 'white', 'black'],
            'finish': 'brushed stainless steel with matte finish',
            'features': ['lightweight', 'push-button lid', 'car cup holder compatible']
        },
        'design_variants': [
            {
                'id': 'variant_a',
                'name': 'Variant A - Minimalist',
                'description': '简约设计，强调功能性',
                'features': ['minimalist shape', 'single color', 'simple branding']
            },
            {
                'id': 'variant_b',
                'name': 'Variant B - Modern',
                'description': '现代设计，强调美学',
                'features': ['modern shape', 'two-tone color', 'premium branding']
            },
            {
                'id': 'variant_c',
                'name': 'Variant C - Functional',
                'description': '功能设计，强调实用性',
                'features': ['functional shape', 'rubber grip', 'additional features']
            }
        ],
        'feasibility_score': 85.5,
        'innovation_score': 78.2,
        'aesthetic_score': 82.0,
        'issues': [],
        'suggestions': []
    }
    
    # 根据可行性分数添加问题和建议
    if design_concept['feasibility_score'] < 70:
        design_concept['issues'].append("设计方案可行性不足")
        design_concept['suggestions'].append("建议简化设计或优化材料和工艺")
    
    if design_concept['innovation_score'] < 70:
        design_concept['issues'].append("设计方案创新性不足")
        design_concept['suggestions'].append("建议增加创新元素或差异化设计")
    
    return design_concept


def create_design_detail(design_concept: Dict[str, Any], 
                         variant_id: str = 'variant_a') -> Dict[str, Any]:
    """
    创建设计详图
    
    Args:
        design_concept: 设计方案
        variant_id: 设计变体ID
        
    Returns:
        设计详图字典
    """
    # 模拟设计详图创建（实际应用中会调用CAD软件）
    design_detail = {
        'success': True,
        'detail_id': f"detail_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'based_on_concept': design_concept.get('concept_id'),
        'variant_id': variant_id,
        'creation_time': datetime.now().isoformat(),
        'technical_drawings': {
            '2d_drawings': ['top_view.dwg', 'side_view.dwg', 'front_view.dwg', 'detail_view.dwg'],
            '3d_model': '3d_model.step',
            'assembly_drawing': 'assembly.dwg',
            'parts_list': 'parts_list.xlsx'
        },
        'dimensions': {
            'height': 220.0,  # mm
            'diameter': 75.0,  # mm
            'weight': 280.0,  # g
            'capacity': 500.0,  # ml
            'wall_thickness': 0.8  # mm
        },
        'material_specs': {
            'body': '304 stainless steel, 0.8mm thickness',
            'lid': 'food-grade PP, injection molded',
            'seal': 'silicone, food-grade',
            'surface_treatment': 'brushed finish with clear coat'
        },
        'manufacturing_specs': {
            'process': 'spinning + vacuum insulation',
            'tolerance': '±0.1mm',
            'surface_roughness': 'Ra 0.8',
            'assembly_method': 'snap-fit + adhesive'
        },
        'cost_estimate': {
            'material_cost': 35.0,  # RMB
            'manufacturing_cost': 15.0,  # RMB
            'assembly_cost': 5.0,  # RMB
            'total_cost': 55.0,  # RMB
            'retail_price': 129.0  # RMB
        },
        'issues': [],
        'suggestions': []
    }
    
    # 检查设计合理性
    if design_detail['dimensions']['weight'] > 350.0:
        design_detail['issues'].append("产品设计重量过大，不符合轻量化要求")
        design_detail['suggestions'].append("建议优化材料厚度或采用更轻的材料")
    
    if design_detail['cost_estimate']['total_cost'] > 60.0:
        design_detail['issues'].append("产品设计成本过高，不符合成本控制要求")
        design_detail['suggestions'].append("建议优化材料或简化制造工艺")
    
    return design_detail


def verify_design(design_detail: Dict[str, Any]) -> Dict[str, Any]:
    """
    验证设计
    
    Args:
        design_detail: 设计详图
        
    Returns:
        设计验证结果字典
    """
    # 模拟设计验证（实际应用中会调用仿真软件）
    verification_result = {
        'success': True,
        'verification_id': f"verification_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'based_on_detail': design_detail.get('detail_id'),
        'verification_time': datetime.now().isoformat(),
        'verification_items': {
            'functional': {
                'insulation_performance': 'passed',  # passed, failed
                'sealing_performance': 'passed',
                'durability': 'passed',
                'safety': 'passed'
            },
            'aesthetic': {
                'visual_appeal': 'passed',
                'color_accuracy': 'passed',
                'surface_quality': 'passed'
            },
            'technical': {
                'dimensional_accuracy': 'passed',
                'material_compliance': 'passed',
                'manufacturability': 'passed'
            },
            'user_experience': {
                'usability': 'passed',
                'comfort': 'passed',
                'safety': 'passed'
            }
        },
        'overall_status': 'passed',  # passed, failed, needs_improvement
        'verification_score': 88.5,
        'issues': [],
        'suggestions': []
    }
    
    # 检查验证结果
    all_items = []
    for category, items in verification_result['verification_items'].items():
        all_items.extend(items.values())
    
    if 'failed' in all_items:
        verification_result['overall_status'] = 'failed'
        verification_result['issues'].append("设计验证未通过，存在失败项目")
        verification_result['suggestions'].append("建议修改设计并通过验证")
    
    if verification_result['verification_score'] < 70:
        verification_result['issues'].append("设计验证分数较低")
        verification_result['suggestions'].append("建议优化设计以提高验证分数")
    
    return verification_result


def manage_design_version(design_id: str, version: str, 
                          design_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    管理设计版本
    
    Args:
        design_id: 设计ID
        version: 版本号
        design_data: 设计数据
        
    Returns:
        版本管理结果字典
    """
    version_file = os.path.join(VERSIONS_DIR, f"{design_id}_v{version}.json")
    
    # 保存设计版本
    try:
        with open(version_file, 'w', encoding='utf-8') as f:
            json.dump({
                'design_id': design_id,
                'version': version,
                'saved_at': datetime.now().isoformat(),
                'design_data': design_data
            }, f, ensure_ascii=False, indent=2)
        
        version_result = {
            'success': True,
            'design_id': design_id,
            'version': version,
            'version_file': version_file,
            'saved_at': datetime.now().isoformat()
        }
        
        print(f"✅ 设计版本已保存：{version_file}")
        return version_result
        
    except Exception as e:
        print(f"❌ 错误：无法保存设计版本 - {e}")
        return {
            'success': False,
            'error': str(e)
        }


def generate_design_report(design_data: Dict[str, Any], 
                          output_format: str = 'json') -> str:
    """
    生成产品设计报告
    
    Args:
        design_data: 设计数据
        output_format: 输出格式 ('json' 或 'markdown')
        
    Returns:
        输出文件路径
    """
    # 生成报告内容
    if output_format == 'markdown':
        report_content = f"""# 产品设计报告

## 基本信息
- **设计ID**：{design_data.get('design_id', '未知设计')}
- **设计方案ID**：{design_data.get('concept_id', '未知方案')}
- **设计详细ID**：{design_data.get('detail_id', '未知详图')}
- **生成时间**：{datetime.now().isoformat()}

## 需求分析摘要
"""
        req_analysis = design_data.get('requirement_analysis', {})
        if req_analysis:
            report_content += f"- **需求数量**：{req_analysis.get('requirements_count', 0)}\n"
            report_content += f"- **需求分类**：功能{req_analysis.get('requirement_categories', {}).get('functional', 0)}个，外观{req_analysis.get('requirement_categories', {}).get('aesthetic', 0)}个，技术{req_analysis.get('requirement_categories', {}).get('technical', 0)}个，市场{req_analysis.get('requirement_categories', {}).get('market', 0)}个\n"
        
        report_content += f"\n## 设计方案摘要\n"
        design_concept = design_data.get('design_concept', {})
        if design_concept:
            report_content += f"- **设计方案ID**：{design_concept.get('concept_id', '未知')}\n"
            report_content += f"- **可行性分数**：{design_concept.get('feasibility_score', 0):.2f}/100\n"
            report_content += f"- **创新性分数**：{design_concept.get('innovation_score', 0):.2f}/100\n"
            report_content += f"- **美学分数**：{design_concept.get('aesthetic_score', 0):.2f}/100\n"
            
            report_content += f"\n### 设计变体\n"
            for variant in design_concept.get('design_variants', []):
                report_content += f"- **{variant.get('name', '未知变体')}**：{variant.get('description', '')}\n"
        
        report_content += f"\n## 设计详图摘要\n"
        design_detail = design_data.get('design_detail', {})
        if design_detail:
            report_content += f"- **详细ID**：{design_detail.get('detail_id', '未知')}\n"
            report_content += f"- **高度**：{design_detail.get('dimensions', {}).get('height', 0):.2f} mm\n"
            report_content += f"- **直径**：{design_detail.get('dimensions', {}).get('diameter', 0):.2f} mm\n"
            report_content += f"- **重量**：{design_detail.get('dimensions', {}).get('weight', 0):.2f} g\n"
            report_content += f"- **容量**：{design_detail.get('dimensions', {}).get('capacity', 0):.2f} ml\n"
            report_content += f"- **总成本**：{design_detail.get('cost_estimate', {}).get('total_cost', 0):.2f} 元\n"
        
        report_content += f"\n## 设计验证摘要\n"
        verification = design_data.get('verification', {})
        if verification:
            report_content += f"- **验证ID**：{verification.get('verification_id', '未知')}\n"
            report_content += f"- **验证状态**：{'✅ 通过' if verification.get('overall_status') == 'passed' else '❌ 未通过'}\n"
            report_content += f"- **验证分数**：{verification.get('verification_score', 0):.2f}/100\n"
        
        report_content += f"\n## 总结\n"
        report_content += f"- **设计完成情况**：需求分析✅，设计方案✅，设计详图✅，设计验证✅\n"
        report_content += f"- **主要问题**：{len(design_data.get('issues', []))}个\n"
        report_content += f"- **改进建议**：{len(design_data.get('suggestions', []))}个\n"
        
    else:  # JSON格式
        report_content = {
            'report_type': 'product_design',
            'generated_at': datetime.now().isoformat(),
            'design_data': design_data,
            'summary': {
                'requirement_count': design_data.get('requirement_analysis', {}).get('requirements_count', 0),
                'feasibility_score': design_data.get('design_concept', {}).get('feasibility_score', 0),
                'verification_score': design_data.get('verification', {}).get('verification_score', 0),
                'total_issues': len(design_data.get('issues', [])),
                'total_suggestions': len(design_data.get('suggestions', []))
            }
        }
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if output_format == 'markdown':
        output_file = os.path.join(OUTPUT_DIR, f'product_design_report_{timestamp}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        output_file = os.path.join(OUTPUT_DIR, f'product_design_report_{timestamp}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 产品设计报告已生成：{output_file}")
    return output_file


def print_stage_details(stage: Dict[str, Any]) -> None:
    """打印设计阶段详情"""
    print(f"📊 设计阶段详情：{stage.get('name')} ({stage.get('name_zh')})")
    print(f"  描述：{stage.get('description')}")
    print(f"  中文描述：{stage.get('description_zh')}")
    
    steps = stage.get('steps', [])
    steps_zh = stage.get('steps_zh', [])
    print(f"\n  🔧 设计步骤：")
    for i, step in enumerate(steps):
        step_zh = steps_zh[i] if i < len(steps_zh) else step
        print(f"    {i+1}. {step}")
        print(f"       {step_zh}")
    
    prompts = stage.get('prompt_keywords', {})
    if prompts:
        print(f"\n  📝 提示词关键词：")
        print(f"    英文：{prompts.get('english')}")
        print(f"    中文：{prompts.get('chinese')}")


def main():
    parser = argparse.ArgumentParser(description='产品设计工具（增强版）')
    parser.add_argument('--stage', type=str, help='设计阶段ID（requirement_analysis/concept_design/detail_design/verification）')
    parser.add_argument('--list', action='store_true', help='列出所有设计阶段')
    parser.add_argument('--analyze-requirements', type=str, help='分析设计需求（指定需求文件路径或JSON字符串）')
    parser.add_argument('--generate-concept', type=str, help='生成设计方案（指定需求分析JSON文件路径）')
    parser.add_argument('--create-detail', type=str, help='创建设计详图（指定设计方案JSON文件路径）')
    parser.add_argument('--verify-design', type=str, help='验证设计（指定设计详图JSON文件路径）')
    parser.add_argument('--manage-version', action='store_true', help='管理设计版本')
    parser.add_argument('--design-id', type=str, help='设计ID（用于版本管理）')
    parser.add_argument('--version', type=str, help='版本号（用于版本管理）')
    parser.add_argument('--generate-report', type=str, choices=['json', 'markdown'], default='json', help='生成产品设计报告（json或markdown格式）')
    
    args = parser.parse_args()
    
    if args.list:
        list_stages()
        return
    
    if args.analyze_requirements:
        print(f"🔍 正在分析设计需求：{args.analyze_requirements}")
        
        # 获取需求数据
        requirements = []
        if os.path.exists(args.analyze_requirements):
            with open(args.analyze_requirements, 'r', encoding='utf-8') as f:
                requirements = json.load(f)
        else:
            try:
                requirements = json.loads(args.analyze_requirements)
            except:
                print(f"❌ 错误：无法解析需求数据 - {args.analyze_requirements}")
                return
        
        if not isinstance(requirements, list):
            requirements = [requirements]
        
        analysis_result = analyze_requirements(requirements)
        print(f"  需求数量：{analysis_result['requirements_count']}")
        print(f"  需求分类：功能{analysis_result['requirement_categories']['functional']}个，外观{analysis_result['requirement_categories']['aesthetic']}个，技术{analysis_result['requirement_categories']['technical']}个，市场{analysis_result['requirement_categories']['market']}个")
        
        if args.generate_report:
            print(f"📝 正在生成产品设计报告...")
            report_file = generate_design_report({
                'requirement_analysis': analysis_result
            }, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.generate_concept:
        print(f"🔍 正在生成设计方案：{args.generate_concept}")
        
        # 获取需求分析结果
        requirement_analysis = {}
        if os.path.exists(args.generate_concept):
            with open(args.generate_concept, 'r', encoding='utf-8') as f:
                requirement_analysis = json.load(f)
        
        design_concept = generate_design_concept(requirement_analysis)
        print(f"  设计方案ID：{design_concept['concept_id']}")
        print(f"  可行性分数：{design_concept['feasibility_score']:.2f}/100")
        print(f"  创新性分数：{design_concept['innovation_score']:.2f}/100")
        
        if args.generate_report:
            print(f"📝 正在生成产品设计报告...")
            report_file = generate_design_report({
                'requirement_analysis': requirement_analysis,
                'design_concept': design_concept
            }, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.create_detail:
        print(f"🔍 正在创建设计详图：{args.create_detail}")
        
        # 获取设计方案
        design_concept = {}
        if os.path.exists(args.create_detail):
            with open(args.create_detail, 'r', encoding='utf-8') as f:
                design_concept = json.load(f)
        
        design_detail = create_design_detail(design_concept)
        print(f"  详细ID：{design_detail['detail_id']}")
        print(f"  高度：{design_detail['dimensions']['height']:.2f} mm")
        print(f"  重量：{design_detail['dimensions']['weight']:.2f} g")
        print(f"  总成本：{design_detail['cost_estimate']['total_cost']:.2f} 元")
        
        if args.generate_report:
            print(f"📝 正在生成产品设计报告...")
            report_file = generate_design_report({
                'design_concept': design_concept,
                'design_detail': design_detail
            }, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.verify_design:
        print(f"🔍 正在验证设计：{args.verify_design}")
        
        # 获取设计详图
        design_detail = {}
        if os.path.exists(args.verify_design):
            with open(args.verify_design, 'r', encoding='utf-8') as f:
                design_detail = json.load(f)
        
        verification_result = verify_design(design_detail)
        print(f"  验证ID：{verification_result['verification_id']}")
        print(f"  验证状态：{'✅ 通过' if verification_result['overall_status'] == 'passed' else '❌ 未通过'}")
        print(f"  验证分数：{verification_result['verification_score']:.2f}/100")
        
        if args.generate_report:
            print(f"📝 正在生成产品设计报告...")
            report_file = generate_design_report({
                'design_detail': design_detail,
                'verification': verification_result
            }, args.generate_report)
            if report_file:
                print(f"✅ 报告已生成：{report_file}")
        return
    
    if args.manage_version:
        if not args.design_id or not args.version:
            print(f"❌ 错误：版本管理需要指定设计ID（--design-id）和版本号（--version）")
            return
        
        print(f"🔍 正在管理设计版本：{args.design_id}, 版本 {args.version}")
        
        # 模拟设计数据
        design_data = {
            'design_id': args.design_id,
            'version': args.version,
            'concept': {},
            'detail': {},
            'verification': {}
        }
        
        version_result = manage_design_version(args.design_id, args.version, design_data)
        if version_result['success']:
            print(f"  版本管理成功：{version_result['version_file']}")
        else:
            print(f"  版本管理失败：{version_result['error']}")
        return
    
    # 默认：列出所有阶段或显示帮助
    if not args.stage:
        print("❌ 错误：请指定设计阶段ID（使用 --stage）或列出所有阶段（使用 --list）")
        parser.print_help()
        return
    
    stage = get_design_stage(args.stage)
    if not stage:
        print(f"❌ 错误：找不到ID为 '{args.stage}' 的设计阶段")
        list_stages()
        return
    
    print_stage_details(stage)


if __name__ == '__main__':
    main()
