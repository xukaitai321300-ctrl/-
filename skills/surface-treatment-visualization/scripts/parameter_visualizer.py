"""
参数可视化工具（增强版） - Parameter Visualizer
负责可视化表面处理工艺参数对效果的影响
"""

import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse


class ParameterVisualizer:
    """参数可视化器（增强版）"""
    
    def __init__(self, param_path: str = "data/process_parameters.json"):
        """
        初始化可视化器
        
        Args:
            param_path: 工艺参数数据文件路径
        """
        self.param_path = param_path
        self.parameters = self._load_parameters()
        
        # 确保输出目录存在
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def _load_parameters(self) -> List[Dict[str, Any]]:
        """
        加载工艺参数数据
        
        Returns:
            工艺参数列表
        """
        try:
            with open(self.param_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 已加载 {len(data.get('process_parameters', []))} 个工艺参数")
                return data.get('process_parameters', [])
        except FileNotFoundError:
            print(f"⚠️ 工艺参数数据文件不存在: {self.param_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"❌ 工艺参数数据JSON格式错误: {e}")
            return []
        except Exception as e:
            print(f"❌ 加载工艺参数数据失败: {e}")
            return []
    
    def get_parameter_by_id(self, param_id: str) -> Optional[Dict[str, Any]]:
        """
        根据ID获取工艺参数
        
        Args:
            param_id: 工艺参数ID
            
        Returns:
            工艺参数字典，如果未找到则返回None
        """
        for param in self.parameters:
            if param.get("id") == param_id:
                return param
        return None
    
    def get_parameters_by_treatment(self, treatment_type: str) -> List[Dict[str, Any]]:
        """
        根据表面处理类型获取工艺参数
        
        Args:
            treatment_type: 表面处理类型
            
        Returns:
            工艺参数字典列表
        """
        results = []
        for param in self.parameters:
            if param.get("treatment_type") == treatment_type:
                results.append(param)
        return results
    
    def visualize_parameter_effect(self, treatment_type: str, parameter_name: str, 
                                 output_path: str = None, chart_type: str = "line") -> Dict[str, Any]:
        """
        可视化工艺参数对效果的影响（增强版）
        
        Args:
            treatment_type: 表面处理类型
            parameter_name: 参数名称
            output_path: 输出路径
            chart_type: 图表类型 ('line', 'bar', 'scatter')
            
        Returns:
            可视化结果字典
        """
        # 查找工艺参数
        param_info = None
        for param in self.parameters:
            if param.get("treatment_type") == treatment_type and param.get("parameter_name") == parameter_name:
                param_info = param
                break
        
        if not param_info:
            return {"error": f"未找到工艺参数: {treatment_type} - {parameter_name}"}
        
        # 创建可视化结果
        result = {
            "success": True,
            "treatment_type": treatment_type,
            "parameter_name": parameter_name,
            "parameter_unit": param_info.get("parameter_unit"),
            "typical_range": param_info.get("typical_range"),
            "optimal_value": param_info.get("optimal_value"),
            "effect_on_quality": param_info.get("effect_on_quality"),
            "effect_on_efficiency": param_info.get("effect_on_efficiency"),
            "visualization_type": chart_type,
            "output_path": output_path,
            "created_at": datetime.now().isoformat()
        }
        
        # 生成可视化图表
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 创建模拟数据
                import random
                typical_range = param_info.get("typical_range", "0-100")
                optimal_value = param_info.get("optimal_value", 50)
                
                # 解析典型范围
                if "-" in typical_range:
                    min_val, max_val = map(float, typical_range.split("-"))
                else:
                    min_val, max_val = 0.0, 100.0
                
                # 生成参数值
                param_values = []
                current_val = min_val
                step = (max_val - min_val) / 10
                while current_val <= max_val:
                    param_values.append(round(current_val, 2))
                    current_val += step
                
                # 生成质量分数（模拟数据，围绕最优值波动）
                quality_scores = []
                for val in param_values:
                    # 计算与最优值的距离
                    distance = abs(val - optimal_value)
                    range_size = max_val - min_val
                    if range_size == 0:
                        range_size = 1.0
                    
                    # 质量分数：距离越近，分数越高
                    score = 100 - (distance / range_size) * 100
                    # 添加随机波动
                    score += random.uniform(-10, 10)
                    score = max(0, min(100, score))  # 限制在0-100范围内
                    quality_scores.append(round(score, 2))
                
                # 生成效率分数（模拟数据）
                efficiency_scores = []
                for val in param_values:
                    # 模拟效率与参数的关系（这里使用简单线性关系）
                    if param_info.get("effect_on_efficiency") == "正相关":
                        score = 50 + (val / max_val) * 50 if max_val > 0 else 50
                    elif param_info.get("effect_on_efficiency") == "负相关":
                        score = 50 + ((max_val - val) / max_val) * 50 if max_val > 0 else 50
                    else:
                        score = 50 + random.uniform(-10, 10)
                    
                    score = max(0, min(100, score))  # 限制在0-100范围内
                    efficiency_scores.append(round(score, 2))
                
                # 根据图表类型生成不同的HTML
                if chart_type == "line":
                    # 折线图
                    html_content = self._generate_line_chart_html(
                        param_values, quality_scores, efficiency_scores,
                        parameter_name, param_info.get("parameter_unit"),
                        treatment_type
                    )
                elif chart_type == "bar":
                    # 柱状图
                    html_content = self._generate_bar_chart_html(
                        param_values, quality_scores, efficiency_scores,
                        parameter_name, param_info.get("parameter_unit"),
                        treatment_type
                    )
                elif chart_type == "scatter":
                    # 散点图
                    html_content = self._generate_scatter_chart_html(
                        param_values, quality_scores, efficiency_scores,
                        parameter_name, param_info.get("parameter_unit"),
                        treatment_type
                    )
                else:
                    # 默认使用折线图
                    html_content = self._generate_line_chart_html(
                        param_values, quality_scores, efficiency_scores,
                        parameter_name, param_info.get("parameter_unit"),
                        treatment_type
                    )
                
                # 保存HTML文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                result["output_path"] = output_path
                result["param_values"] = param_values
                result["quality_scores"] = quality_scores
                result["efficiency_scores"] = efficiency_scores
                
                print(f"✅ 工艺参数影响图表已生成: {output_path}")
                
            except Exception as e:
                print(f"❌ 生成工艺参数影响图表失败: {e}")
                result["error"] = str(e)
        
        return result
    
    def _generate_line_chart_html(self, param_values: List[float], 
                                quality_scores: List[float],
                                efficiency_scores: List[float],
                                parameter_name: str, parameter_unit: str,
                                treatment_type: str) -> str:
        """
        生成折线图HTML
        
        Args:
            param_values: 参数值列表
            quality_scores: 质量分数列表
            efficiency_scores: 效率分数列表
            parameter_name: 参数名称
            parameter_unit: 参数单位
            treatment_type: 表面处理类型
            
        Returns:
            HTML内容
        """
        # 准备数据
        param_values_str = str(param_values)
        quality_scores_str = str(quality_scores)
        efficiency_scores_str = str(efficiency_scores)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{treatment_type} - {parameter_name} 参数影响</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                h1 {{ color: #333; text-align: center; }}
                .chart-container {{ 
                    max-width: 1000px; 
                    margin: 30px auto; 
                    background-color: white; 
                    padding: 20px; 
                    border-radius: 10px; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .info {{ 
                    margin-top: 30px; 
                    padding: 15px; 
                    background-color: #e8f4fd; 
                    border-left: 4px solid #2196F3; 
                    border-radius: 5px; 
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <h1>{treatment_type} - {parameter_name} 参数影响</h1>
            
            <div class="chart-container">
                <canvas id="parameterChart"></canvas>
            </div>
            
            <div class="info">
                <strong>📊 图表说明：</strong><br>
                - 横轴：{parameter_name} ({parameter_unit})<br>
                - 纵轴：分数 (0-100)<br>
                - 蓝色线条：质量分数<br>
                - 橙色线条：效率分数<br>
                - 标记点为最优值：{self._get_optimal_value(treatment_type, parameter_name)}
            </div>
            
            <script>
                const paramValues = {param_values_str};
                const qualityScores = {quality_scores_str};
                const efficiencyScores = {efficiency_scores_str};
                
                const ctx = document.getElementById('parameterChart').getContext('2d');
                const chart = new Chart(ctx, {{
                    type: 'line',
                    data: {{
                        labels: paramValues,
                        datasets: [{{
                            label: '质量分数',
                            data: qualityScores,
                            borderColor: 'rgb(54, 162, 235)',
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            tension: 0.4,
                            fill: true
                        }}, {{
                            label: '效率分数',
                            data: efficiencyScores,
                            borderColor: 'rgb(255, 159, 64)',
                            backgroundColor: 'rgba(255, 159, 64, 0.2)',
                            tension: 0.4,
                            fill: true
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        plugins: {{
                            title: {{
                                display: true,
                                text: '{parameter_name} 对质量和效率的影响'
                            }},
                            tooltip: {{
                                mode: 'index',
                                intersect: false
                            }}
                        }},
                        scales: {{
                            x: {{
                                title: {{
                                    display: true,
                                    text: '{parameter_name} ({parameter_unit})'
                                }}
                            }},
                            y: {{
                                title: {{
                                    display: true,
                                    text: '分数 (0-100)'
                                }},
                                min: 0,
                                max: 100
                            }}
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """
        
        return html_content
    
    def _generate_bar_chart_html(self, param_values: List[float], 
                               quality_scores: List[float],
                               efficiency_scores: List[float],
                               parameter_name: str, parameter_unit: str,
                               treatment_type: str) -> str:
        """
        生成柱状图HTML
        
        Args:
            param_values: 参数值列表
            quality_scores: 质量分数列表
            efficiency_scores: 效率分数列表
            parameter_name: 参数名称
            parameter_unit: 参数单位
            treatment_type: 表面处理类型
            
        Returns:
            HTML内容
        """
        # 准备数据
        param_values_str = str(param_values)
        quality_scores_str = str(quality_scores)
        efficiency_scores_str = str(efficiency_scores)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{treatment_type} - {parameter_name} 参数影响</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                h1 {{ color: #333; text-align: center; }}
                .chart-container {{ 
                    max-width: 1000px; 
                    margin: 30px auto; 
                    background-color: white; 
                    padding: 20px; 
                    border-radius: 10px; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .info {{ 
                    margin-top: 30px; 
                    padding: 15px; 
                    background-color: #e8f4fd; 
                    border-left: 4px solid #2196F3; 
                    border-radius: 5px; 
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <h1>{treatment_type} - {parameter_name} 参数影响</h1>
            
            <div class="chart-container">
                <canvas id="parameterChart"></canvas>
            </div>
            
            <div class="info">
                <strong>📊 图表说明：</strong><br>
                - 横轴：{parameter_name} ({parameter_unit})<br>
                - 纵轴：分数 (0-100)<br>
                - 蓝色柱状：质量分数<br>
                - 橙色柱状：效率分数<br>
                - 最优值：{self._get_optimal_value(treatment_type, parameter_name)}
            </div>
            
            <script>
                const paramValues = {param_values_str};
                const qualityScores = {quality_scores_str};
                const efficiencyScores = {efficiency_scores_str};
                
                const ctx = document.getElementById('parameterChart').getContext('2d');
                const chart = new Chart(ctx, {{
                    type: 'bar',
                    data: {{
                        labels: paramValues,
                        datasets: [{{
                            label: '质量分数',
                            data: qualityScores,
                            backgroundColor: 'rgba(54, 162, 235, 0.5)',
                            borderColor: 'rgb(54, 162, 235)',
                            borderWidth: 1
                        }}, {{
                            label: '效率分数',
                            data: efficiencyScores,
                            backgroundColor: 'rgba(255, 159, 64, 0.5)',
                            borderColor: 'rgb(255, 159, 64)',
                            borderWidth: 1
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        plugins: {{
                            title: {{
                                display: true,
                                text: '{parameter_name} 对质量和效率的影响'
                            }}
                        }},
                        scales: {{
                            x: {{
                                title: {{
                                    display: true,
                                    text: '{parameter_name} ({parameter_unit})'
                                }}
                            }},
                            y: {{
                                title: {{
                                    display: true,
                                    text: '分数 (0-100)'
                                }},
                                min: 0,
                                max: 100
                            }}
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """
        
        return html_content
    
    def _generate_scatter_chart_html(self, param_values: List[float], 
                                   quality_scores: List[float],
                                   efficiency_scores: List[float],
                                   parameter_name: str, parameter_unit: str,
                                   treatment_type: str) -> str:
        """
        生成散点图HTML
        
        Args:
            param_values: 参数值列表
            quality_scores: 质量分数列表
            efficiency_scores: 效率分数列表
            parameter_name: 参数名称
            parameter_unit: 参数单位
            treatment_type: 表面处理类型
            
        Returns:
            HTML内容
        """
        # 准备数据（散点图需要x,y坐标对）
        scatter_data_quality = []
        scatter_data_efficiency = []
        
        for i in range(len(param_values)):
            scatter_data_quality.append({"x": param_values[i], "y": quality_scores[i]})
            scatter_data_efficiency.append({"x": param_values[i], "y": efficiency_scores[i]})
        
        scatter_data_quality_str = str(scatter_data_quality)
        scatter_data_efficiency_str = str(scatter_data_efficiency)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{treatment_type} - {parameter_name} 参数影响</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                h1 {{ color: #333; text-align: center; }}
                .chart-container {{ 
                    max-width: 1000px; 
                    margin: 30px auto; 
                    background-color: white; 
                    padding: 20px; 
                    border-radius: 10px; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .info {{ 
                    margin-top: 30px; 
                    padding: 15px; 
                    background-color: #e8f4fd; 
                    border-left: 4px solid #2196F3; 
                    border-radius: 5px; 
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <h1>{treatment_type} - {parameter_name} 参数影响</h1>
            
            <div class="chart-container">
                <canvas id="parameterChart"></canvas>
            </div>
            
            <div class="info">
                <strong>📊 图表说明：</strong><br>
                - 横轴：{parameter_name} ({parameter_unit})<br>
                - 纵轴：分数 (0-100)<br>
                - 蓝色散点：质量分数<br>
                - 橙色散点：效率分数<br>
                - 最优值：{self._get_optimal_value(treatment_type, parameter_name)}
            </div>
            
            <script>
                const scatterDataQuality = {scatter_data_quality_str};
                const scatterDataEfficiency = {scatter_data_efficiency_str};
                
                const ctx = document.getElementById('parameterChart').getContext('2d');
                const chart = new Chart(ctx, {{
                    type: 'scatter',
                    data: {{
                        datasets: [{{
                            label: '质量分数',
                            data: scatterDataQuality,
                            backgroundColor: 'rgba(54, 162, 235, 0.5)',
                            borderColor: 'rgb(54, 162, 235)',
                            pointRadius: 6
                        }}, {{
                            label: '效率分数',
                            data: scatterDataEfficiency,
                            backgroundColor: 'rgba(255, 159, 64, 0.5)',
                            borderColor: 'rgb(255, 159, 64)',
                            pointRadius: 6
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        plugins: {{
                            title: {{
                                display: true,
                                text: '{parameter_name} 对质量和效率的影响'
                            }}
                        }},
                        scales: {{
                            x: {{
                                title: {{
                                    display: true,
                                    text: '{parameter_name} ({parameter_unit})'
                                }},
                                type: 'linear',
                                position: 'bottom'
                            }},
                            y: {{
                                title: {{
                                    display: true,
                                    text: '分数 (0-100)'
                                }},
                                min: 0,
                                max: 100
                            }}
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """
        
        return html_content
    
    def _get_optimal_value(self, treatment_type: str, parameter_name: str) -> str:
        """
        获取最优值
        
        Args:
            treatment_type: 表面处理类型
            parameter_name: 参数名称
            
        Returns:
            最优值字符串
        """
        for param in self.parameters:
            if param.get("treatment_type") == treatment_type and param.get("parameter_name") == parameter_name:
                optimal = param.get("optimal_value")
                unit = param.get("parameter_unit")
                if optimal and unit:
                    return f"{optimal} {unit}"
                elif optimal:
                    return str(optimal)
                else:
                    return "未知"
        
        return "未知"
    
    def generate_parameter_optimization_suggestion(self, treatment_type: str, parameter_name: str) -> Dict[str, Any]:
        """
        生成参数优化建议（增强版）
        
        Args:
            treatment_type: 表面处理类型
            parameter_name: 参数名称
            
        Returns:
            优化建议字典
        """
        # 查找工艺参数
        param_info = None
        for param in self.parameters:
            if param.get("treatment_type") == treatment_type and param.get("parameter_name") == parameter_name:
                param_info = param
                break
        
        if not param_info:
            return {"error": f"未找到工艺参数: {treatment_type} - {parameter_name}"}
        
        # 创建优化建议
        suggestion = {
            "success": True,
            "treatment_type": treatment_type,
            "parameter_name": parameter_name,
            "optimal_value": param_info.get("optimal_value"),
            "typical_range": param_info.get("typical_range"),
            "control_method": param_info.get("control_method"),
            "parameter_unit": param_info.get("parameter_unit"),
            "effect_on_quality": param_info.get("effect_on_quality"),
            "effect_on_efficiency": param_info.get("effect_on_efficiency"),
            "optimization_suggestions": [
                f"建议使用最优值: {param_info.get('optimal_value')} {param_info.get('parameter_unit')}",
                f"控制参数在典型范围内: {param_info.get('typical_range')}",
                f"使用{param_info.get('control_method')}控制参数"
            ],
            "created_at": datetime.now().isoformat()
        }
        
        return suggestion
    
    def batch_visualize_parameters(self, param_configs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量可视化工艺参数
        
        Args:
            param_configs: 参数配置列表，每个配置包含：
                - treatment_type: 表面处理类型
                - parameter_name: 参数名称
                - output_path: 输出路径（可选）
                - chart_type: 图表类型（可选，默认'line'）
                
        Returns:
            可视化结果列表
        """
        if not param_configs or not isinstance(param_configs, list):
            return [{"error": "参数配置列表无效"}]
        
        results = []
        
        for i, config in enumerate(param_configs):
            treatment_type = config.get("treatment_type")
            parameter_name = config.get("parameter_name")
            output_path = config.get("output_path")
            chart_type = config.get("chart_type", "line")
            
            # 验证参数
            if not treatment_type or not parameter_name:
                results.append({"error": f"配置 {i+1} 缺少必要参数"})
                continue
            
            # 可视化参数影响
            result = self.visualize_parameter_effect(
                treatment_type=treatment_type,
                parameter_name=parameter_name,
                output_path=output_path or f"{self.output_dir}/batch_param_vis_{i+1:03d}.html",
                chart_type=chart_type
            )
            
            results.append(result)
        
        print(f"✅ 批量可视化完成，共生成 {len(results)} 个图表")
        return results
    
    def generate_parameter_visualization_report(self, visualization_result: Dict[str, Any], 
                                              output_format: str = 'json', 
                                              output_path: str = None) -> str:
        """
        生成参数可视化报告（增强版）
        
        Args:
            visualization_result: 可视化结果字典
            output_format: 输出格式 ('json' 或 'markdown')
            output_path: 输出文件路径
            
        Returns:
            输出文件路径
        """
        # 创建报告
        report_id = f"PARAM-VIS-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}"
        
        if output_format == 'markdown':
            # 生成Markdown格式报告
            report_content = f"""# 表面处理工艺参数可视化报告

## 基本信息
- **报告ID**：{report_id}
- **标题**：{visualization_result.get('treatment_type', '未知')} - {visualization_result.get('parameter_name', '未知')} 参数可视化报告
- **生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **表面处理类型**：{visualization_result.get('treatment_type', '未知')}
- **参数名称**：{visualization_result.get('parameter_name', '未知')}

## 参数信息
- **参数单位**：{visualization_result.get('parameter_unit', '未知')}
- **典型范围**：{visualization_result.get('typical_range', '未知')}
- **最优值**：{visualization_result.get('optimal_value', '未知')}
- **对质量的影响**：{visualization_result.get('effect_on_quality', '未知')}
- **对效率的影响**：{visualization_result.get('effect_on_efficiency', '未知')}

## 可视化信息
- **可视化类型**：{visualization_result.get('visualization_type', '未知')}
- **输出路径**：{visualization_result.get('output_path', '未知')}
- **生成时间**：{visualization_result.get('created_at', '未知')}
- **成功状态**：{'✅ 成功' if visualization_result.get('success', False) else '❌ 失败'}

## 优化建议
"""
            # 添加优化建议
            suggestion = self.generate_parameter_optimization_suggestion(
                visualization_result.get("treatment_type"),
                visualization_result.get("parameter_name")
            )
            
            if "error" not in suggestion:
                for i, rec in enumerate(suggestion.get("optimization_suggestions", []), 1):
                    report_content += f"{i}. {rec}\n"
            else:
                report_content += f"1. {suggestion.get('error')}\n"
            
            report_content += f"""
## 总结
- **表面处理类型**：{visualization_result.get('treatment_type', '未知')}
- **参数名称**：{visualization_result.get('parameter_name', '未知')}
- **最优值**：{visualization_result.get('optimal_value', '未知')}
- **可视化类型**：{visualization_result.get('visualization_type', '未知')}
"""
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/parameter_visualization_report_{report_id}.md"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(report_content)
                print(f"✅ 参数可视化报告已保存（Markdown）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存参数可视化报告失败: {e}")
                return None
            
        else:  # JSON格式
            # 生成优化建议
            suggestion = self.generate_parameter_optimization_suggestion(
                visualization_result.get("treatment_type"),
                visualization_result.get("parameter_name")
            )
            
            report = {
                "report_id": report_id,
                "title": f"{visualization_result.get('treatment_type', '未知')} - {visualization_result.get('parameter_name', '未知')} 参数可视化报告",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "treatment_type": visualization_result.get("treatment_type"),
                "parameter_name": visualization_result.get("parameter_name"),
                "parameter_unit": visualization_result.get("parameter_unit"),
                "typical_range": visualization_result.get("typical_range"),
                "optimal_value": visualization_result.get("optimal_value"),
                "effect_on_quality": visualization_result.get("effect_on_quality"),
                "effect_on_efficiency": visualization_result.get("effect_on_efficiency"),
                "visualization_type": visualization_result.get("visualization_type"),
                "output_path": visualization_result.get("output_path"),
                "created_at": visualization_result.get("created_at"),
                "success": visualization_result.get("success", False),
                "optimization_suggestions": suggestion.get("optimization_suggestions", []) if "error" not in suggestion else [],
                "generated_at": datetime.now().isoformat()
            }
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/parameter_visualization_report_{report_id}.json"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, ensure_ascii=False, indent=2)
                print(f"✅ 参数可视化报告已保存（JSON）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存参数可视化报告失败: {e}")
                return None
    
    def print_visualization_summary(self, visualization_result: Dict[str, Any]) -> None:
        """
        打印可视化摘要
        
        Args:
            visualization_result: 可视化结果字典
        """
        print(f"\n📊 参数可视化摘要")
        print(f"  表面处理类型: {visualization_result.get('treatment_type', '未知')}")
        print(f"  参数名称: {visualization_result.get('parameter_name', '未知')}")
        print(f"  成功状态: {'✅ 成功' if visualization_result.get('success', False) else '❌ 失败'}")
        print(f"  生成时间: {visualization_result.get('created_at', '未知')}")
        
        # 打印参数信息
        param_unit = visualization_result.get("parameter_unit")
        if param_unit:
            print(f"  参数单位: {param_unit}")
        
        typical_range = visualization_result.get("typical_range")
        if typical_range:
            print(f"  典型范围: {typical_range}")
        
        optimal_value = visualization_result.get("optimal_value")
        if optimal_value:
            print(f"  最优值: {optimal_value}")
        
        # 打印输出路径
        output_path = visualization_result.get("output_path")
        if output_path:
            print(f"  输出路径: {output_path}")
    
    def print_optimization_suggestion(self, suggestion: Dict[str, Any]) -> None:
        """
        打印优化建议
        
        Args:
            suggestion: 优化建议字典
        """
        print(f"\n💡 参数优化建议")
        print(f"  表面处理类型: {suggestion.get('treatment_type', '未知')}")
        print(f"  参数名称: {suggestion.get('parameter_name', '未知')}")
        print(f"  最优值: {suggestion.get('optimal_value', '未知')} {suggestion.get('parameter_unit', '')}")
        print(f"  典型范围: {suggestion.get('typical_range', '未知')}")
        print(f"  控制方法: {suggestion.get('control_method', '未知')}")
        
        # 打印优化建议
        optimizations = suggestion.get("optimization_suggestions", [])
        if optimizations:
            print(f"  优化建议:")
            for i, opt in enumerate(optimizations, 1):
                print(f"    {i}. {opt}")


# 使用示例
if __name__ == "__main__":
    # 初始化参数可视化器
    visualizer = ParameterVisualizer()
    
    # 可视化工艺参数对效果的影响（折线图）
    result = visualizer.visualize_parameter_effect(
        treatment_type="喷漆",
        parameter_name="温度",
        output_path="output/parameter_effect_chart.html",
        chart_type="line"
    )
    
    if "error" not in result:
        print(f"生成工艺参数影响图表: {result.get('output_path')}")
        visualizer.print_visualization_summary(result)
    else:
        print(f"❌ 错误: {result.get('error')}")
    
    # 可视化工艺参数对效果的影响（柱状图）
    result2 = visualizer.visualize_parameter_effect(
        treatment_type="喷塑",
        parameter_name="温度",
        output_path="output/parameter_effect_chart_bar.html",
        chart_type="bar"
    )
    
    if "error" not in result2:
        print(f"生成工艺参数影响图表（柱状图）: {result2.get('output_path')}")
    
    # 可视化工艺参数对效果的影响（散点图）
    result3 = visualizer.visualize_parameter_effect(
        treatment_type="热转印",
        parameter_name="温度",
        output_path="output/parameter_effect_chart_scatter.html",
        chart_type="scatter"
    )
    
    if "error" not in result3:
        print(f"生成工艺参数影响图表（散点图）: {result3.get('output_path')}")
    
    # 生成参数优化建议
    suggestion = visualizer.generate_parameter_optimization_suggestion(
        treatment_type="喷漆",
        parameter_name="温度"
    )
    
    if "error" not in suggestion:
        print(f"参数优化建议: ")
        visualizer.print_optimization_suggestion(suggestion)
    else:
        print(f"❌ 错误: {suggestion.get('error')}")
    
    # 批量可视化工艺参数
    batch_configs = [
        {
            "treatment_type": "喷漆",
            "parameter_name": "温度",
            "chart_type": "line"
        },
        {
            "treatment_type": "喷塑",
            "parameter_name": "温度",
            "chart_type": "bar"
        },
        {
            "treatment_type": "热转印",
            "parameter_name": "温度",
            "chart_type": "scatter"
        }
    ]
    
    batch_results = visualizer.batch_visualize_parameters(batch_configs)
    print(f"批量可视化完成，共生成 {len(batch_results)} 个图表")
    
    # 生成参数可视化报告
    if "error" not in result:
        report_path = visualizer.generate_parameter_visualization_report(
            visualization_result=result,
            output_format='markdown',
            output_path="reports/parameter_visualization_report.md"
        )
        print(f"生成参数可视化报告: {report_path}")
