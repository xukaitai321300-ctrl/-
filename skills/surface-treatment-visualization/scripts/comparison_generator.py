"""
对比生成工具（增强版） - Comparison Generator
负责生成表面处理前后对比图片，支持多种对比模式
"""

import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import base64
import argparse


class ComparisonGenerator:
    """对比生成器（增强版）"""
    
    def __init__(self, output_dir: str = "output"):
        """
        初始化生成器
        
        Args:
            output_dir: 输出目录
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def generate_before_after_comparison(self, before_image: str, after_image: str = None,
                                        after_effect: str = None, after_params: Dict[str, Any] = None,
                                        output_path: str = None, title: str = None) -> Dict[str, Any]:
        """
        生成表面处理前后对比
        
        Args:
            before_image: 处理前图片路径
            after_image: 处理后图片路径（与after_effect二选一）
            after_effect: 处理后效果描述（与after_image二选一）
            after_params: 处理后参数字典
            output_path: 输出路径
            title: 标题
            
        Returns:
            对比结果字典
        """
        # 检查原始图片是否存在
        if not os.path.exists(before_image):
            return {"error": f"处理前图片不存在: {before_image}"}
        
        # 检查处理后图片或效果描述
        if not after_image and not after_effect:
            return {"error": "必须提供处理后图片路径或效果描述"}
        
        if after_image and not os.path.exists(after_image):
            return {"error": f"处理后图片不存在: {after_image}"}
        
        # 创建对比结果
        result = {
            "success": True,
            "comparison_type": "before_after",
            "before_image": before_image,
            "after_image": after_image,
            "after_effect": after_effect,
            "after_params": after_params or {},
            "output_path": output_path,
            "title": title or "表面处理前后对比",
            "created_at": datetime.now().isoformat()
        }
        
        # 生成对比图片（模拟）
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 读取图片并转换为base64
                with open(before_image, 'rb') as img_file:
                    before_img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                after_img_data = None
                if after_image and os.path.exists(after_image):
                    with open(after_image, 'rb') as img_file:
                        after_img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                # 获取图片格式
                before_format = before_image.split('.')[-1].lower()
                if before_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                    before_format = 'png'
                
                # 创建HTML页面
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{result['title']}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                        h1 {{ color: #333; text-align: center; }}
                        .comparison-container {{ 
                            display: flex; 
                            justify-content: center; 
                            align-items: flex-start;
                            flex-wrap: wrap;
                            margin-top: 30px;
                            background-color: white;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        }}
                        .image-box {{ 
                            flex: 1; 
                            margin: 10px; 
                            text-align: center;
                            padding: 15px;
                            background-color: #f9f9f9;
                            border-radius: 5px;
                        }}
                        .image-box h3 {{ color: #555; }}
                        img {{ 
                            max-width: 100%; 
                            height: auto; 
                            border: 1px solid #ddd; 
                            border-radius: 5px;
                            transition: transform 0.3s;
                        }}
                        img:hover {{ 
                            transform: scale(1.05);
                            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                        }}
                        .params {{ 
                            margin-top: 15px; 
                            text-align: left; 
                            padding: 10px; 
                            background-color: #e8f4fd; 
                            border-left: 4px solid #2196F3; 
                            border-radius: 5px; 
                            font-size: 14px;
                        }}
                        .info {{ 
                            margin-top: 30px; 
                            padding: 15px; 
                            background-color: #e8f4fd; 
                            border-left: 4px solid #2196F3; 
                            border-radius: 5px;
                        }}
                    </style>
                </head>
                <body>
                    <h1>{result['title']}</h1>
                    
                    <div class="comparison-container">
                        <div class="image-box">
                            <h3>🔍 处理前</h3>
                            <img src="data:image/{before_format};base64,{before_img_data}" alt="处理前">
                        </div>
                        
                        <div class="image-box">
                            <h3>✨ 处理后</h3>
                """
                
                # 添加处理后图片或效果描述
                if after_img_data:
                    after_format = after_image.split('.')[-1].lower()
                    if after_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                        after_format = 'png'
                    
                    html_content += f"""
                            <img src="data:image/{after_format};base64,{after_img_data}" alt="处理后">
                    """
                elif after_effect:
                    html_content += f"""
                            <div style="padding: 50px 20px; font-size: 18px; color: #333;">
                                {after_effect}
                            </div>
                    """
                
                html_content += f"""
                        </div>
                    </div>
                """
                
                # 添加参数信息
                if after_params:
                    params_html = "<div class='params'><strong>⚙️ 处理参数：</strong><br>"
                    for key, value in after_params.items():
                        params_html += f"&nbsp;&nbsp;- <strong>{key}</strong>: {value}<br>"
                    params_html += "</div>"
                    html_content += params_html
                
                html_content += f"""
                    <div class="info">
                        <strong>📊 对比说明：</strong><br>
                        - 上方展示了处理前和处理后的效果对比<br>
                        - 鼠标悬停在图片上可以放大查看<br>
                        - 处理时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </div>
                </body>
                </html>
                """
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                result["output_path"] = output_path
                print(f"✅ 前后对比页面已生成: {output_path}")
                
            except Exception as e:
                print(f"❌ 保存前后对比页面失败: {e}")
                result["error"] = str(e)
        
        return result
    
    def generate_slider_comparison(self, before_image: str, after_image: str, 
                                        output_path: str = None, title: str = None) -> Dict[str, Any]:
        """
        生成滑块对比
        
        Args:
            before_image: 处理前图片路径
            after_image: 处理后图片路径
            output_path: 输出路径
            title: 标题
            
        Returns:
            对比结果字典
        """
        # 检查图片是否存在
        if not os.path.exists(before_image):
            return {"error": f"处理前图片不存在: {before_image}"}
        
        if not os.path.exists(after_image):
            return {"error": f"处理后图片不存在: {after_image}"}
        
        # 创建对比结果
        result = {
            "success": True,
            "comparison_type": "slider",
            "before_image": before_image,
            "after_image": after_image,
            "output_path": output_path,
            "title": title or "表面处理前后滑块对比",
            "created_at": datetime.now().isoformat()
        }
        
        # 生成滑块对比HTML
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 读取图片并转换为base64
                with open(before_image, 'rb') as img_file:
                    before_img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                with open(after_image, 'rb') as img_file:
                    after_img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                # 获取图片格式
                before_format = before_image.split('.')[-1].lower()
                if before_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                    before_format = 'png'
                
                after_format = after_image.split('.')[-1].lower()
                if after_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                    after_format = 'png'
                
                # 创建HTML页面
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{result['title']}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                        h1 {{ color: #333; text-align: center; }}
                        .comparison-container {{ 
                            position: relative; 
                            width: 80%; 
                            max-width: 1000px;
                            height: 600px; 
                            margin: 30px auto; 
                            background-color: white;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        }}
                        .before-image, .after-image {{ 
                            position: absolute; 
                            top: 20px; 
                            left: 20px; 
                            width: calc(100% - 40px); 
                            height: calc(100% - 40px); 
                            object-fit: contain; 
                            border-radius: 5px;
                        }}
                        .after-image {{ 
                            clip-path: polygon(0 0, 50% 0, 50% 100%, 0 100%); 
                        }}
                        .slider {{ 
                            position: absolute; 
                            top: 20px; 
                            left: 50%; 
                            width: 4px; 
                            height: calc(100% - 40px); 
                            background-color: #fff; 
                            cursor: ew-resize; 
                            z-index: 10;
                            box-shadow: 0 0 10px rgba(0,0,0,0.5);
                        }}
                        .slider-handle {{ 
                            position: absolute; 
                            top: 50%; 
                            left: -18px; 
                            width: 40px; 
                            height: 40px; 
                            margin-top: -20px;
                            background-color: #2196F3; 
                            color: white;
                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            font-size: 20px;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                        }}
                        .info {{ 
                            margin-top: 30px; 
                            padding: 15px; 
                            background-color: #e8f4fd; 
                            border-left: 4px solid #2196F3; 
                            border-radius: 5px;
                        }}
                    </style>
                </head>
                <body>
                    <h1>{result['title']}</h1>
                    <p style="text-align: center; color: #666;">拖拽中间滑块来对比处理前后的效果</p>
                    
                    <div class="comparison-container">
                        <img src="data:image/{before_format};base64,{before_img_data}" alt="处理前" class="before-image">
                        <img src="data:image/{after_format};base64,{after_img_data}" alt="处理后" class="after-image" id="afterImage">
                        <div class="slider" id="slider">
                            <div class="slider-handle">⇔</div>
                        </div>
                    </div>
                    
                    <script>
                        const slider = document.getElementById('slider');
                        const afterImage = document.getElementById('afterImage');
                        let isDragging = false;
                        
                        slider.addEventListener('mousedown', function(e) {{
                            isDragging = true;
                            e.preventDefault();
                        }});
                        
                        document.addEventListener('mousemove', function(e) {{
                            if (!isDragging) return;
                            
                            const container = document.querySelector('.comparison-container');
                            const rect = container.getBoundingClientRect();
                            let x = e.clientX - rect.left;
                            
                            if (x < 20) x = 20;
                            if (x > rect.width - 20) x = rect.width - 20;
                            
                            const percentage = ((x - 20) / (rect.width - 40)) * 100;
                            
                            slider.style.left = percentage + '%';
                            afterImage.style.clipPath = `polygon(0 0, ${{percentage}}% 0, ${{percentage}}% 100%, 0 100%)`;
                        }});
                        
                        document.addEventListener('mouseup', function() {{
                            isDragging = false;
                        }});
                        
                        // 触摸设备支持
                        slider.addEventListener('touchstart', function(e) {{
                            isDragging = true;
                            e.preventDefault();
                        }});
                        
                        document.addEventListener('touchmove', function(e) {{
                            if (!isDragging) return;
                            
                            const container = document.querySelector('.comparison-container');
                            const rect = container.getBoundingClientRect();
                            let x = e.touches[0].clientX - rect.left;
                            
                            if (x < 20) x = 20;
                            if (x > rect.width - 20) x = rect.width - 20;
                            
                            const percentage = ((x - 20) / (rect.width - 40)) * 100;
                            
                            slider.style.left = percentage + '%';
                            afterImage.style.clipPath = `polygon(0 0, ${{percentage}}% 0, ${{percentage}}% 100%, 0 100%)`;
                        }});
                        
                        document.addEventListener('touchend', function() {{
                            isDragging = false;
                        }});
                    </script>
                    
                    <div class="info">
                        <strong>📊 对比说明：</strong><br>
                        - 拖拽中间滑块来对比处理前后的效果<br>
                        - 支持鼠标和触摸操作<br>
                        - 处理时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </div>
                </body>
                </html>
                """
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                result["output_path"] = output_path
                print(f"✅ 滑块对比页面已生成: {output_path}")
                
            except Exception as e:
                print(f"❌ 保存滑块对比页面失败: {e}")
                result["error"] = str(e)
        
        return result
    
    def generate_batch_comparison(self, comparison_configs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量生成对比
        
        Args:
            comparison_configs: 对比配置列表，每个配置包含：
                - before_image: 处理前图片路径
                - after_image: 处理后图片路径（可选）
                - after_effect: 处理后效果描述（可选）
                - after_params: 处理后参数字典（可选）
                - output_path: 输出路径（可选）
                - title: 标题（可选）
                - comparison_type: 对比类型（'before_after' 或 'slider'）
                
        Returns:
            对比结果列表
        """
        if not comparison_configs or not isinstance(comparison_configs, list):
            return [{"error": "对比配置列表无效"}]
        
        results = []
        
        for i, config in enumerate(comparison_configs):
            comparison_type = config.get("comparison_type", "before_after")
            before_image = config.get("before_image")
            after_image = config.get("after_image")
            after_effect = config.get("after_effect")
            after_params = config.get("after_params")
            output_path = config.get("output_path")
            title = config.get("title")
            
            # 根据对比类型调用相应的生成方法
            if comparison_type == "before_after":
                result = self.generate_before_after_comparison(
                    before_image=before_image,
                    after_image=after_image,
                    after_effect=after_effect,
                    after_params=after_params,
                    output_path=output_path or f"{self.output_dir}/batch_comparison_{i+1:03d}.html",
                    title=title
                )
            elif comparison_type == "slider":
                result = self.generate_slider_comparison(
                    before_image=before_image,
                    after_image=after_image,
                    output_path=output_path or f"{self.output_dir}/batch_slider_{i+1:03d}.html",
                    title=title
                )
            else:
                result = {"error": f"不支持的对比类型: {comparison_type}"}
            
            results.append(result)
        
        print(f"✅ 批量对比生成完成，共生成 {len(results)} 个对比")
        return results
    
    def generate_comparison_report(self, comparison_result: Dict[str, Any], 
                                   output_format: str = 'json', 
                                   output_path: str = None) -> str:
        """
        生成对比报告（增强版）
        
        Args:
            comparison_result: 对比结果字典
            output_format: 输出格式 ('json' 或 'markdown')
            output_path: 输出文件路径
            
        Returns:
            输出文件路径
        """
        # 创建报告
        report_id = f"COMPARISON-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}"
        
        if output_format == 'markdown':
            # 生成Markdown格式报告
            report_content = f"""# 表面处理前后对比报告

## 基本信息
- **报告ID**：{report_id}
- **标题**：{comparison_result.get('title', '表面处理前后对比报告')}
- **生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **对比类型**：{comparison_result.get('comparison_type', '未知')}

## 对比详情
- **处理前图片**：{comparison_result.get('before_image', '无')}
- **处理后图片**：{comparison_result.get('after_image', '无')}
- **处理后效果**：{comparison_result.get('after_effect', '无')}

## 处理参数
"""
            # 添加参数信息
            after_params = comparison_result.get('after_params', {})
            if after_params:
                for key, value in after_params.items():
                    report_content += f"- **{key}**：{value}\n"
            else:
                report_content += "- **参数**：无\n"
            
            report_content += f"""
## 输出信息
- **输出路径**：{comparison_result.get('output_path', '未知')}
- **成功状态**：{'✅ 成功' if comparison_result.get('success', False) else '❌ 失败'}

## 建议
1. 建议使用高分辨率图片进行对比
2. 建议添加对比说明和参数变化
3. 建议使用滑块对比，更直观地展示效果差异
4. 确保处理前后图片的拍摄角度和光照条件一致

## 总结
- **对比类型**：{comparison_result.get('comparison_type', '未知')}
- **参数数量**：{len(after_params)}
- **生成时间**：{comparison_result.get('created_at', '未知')}
"""
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/comparison_report_{report_id}.md"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(report_content)
                print(f"✅ 对比报告已保存（Markdown）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存对比报告失败: {e}")
                return None
            
        else:  # JSON格式
            report = {
                "report_id": report_id,
                "title": comparison_result.get("title", "表面处理前后对比报告"),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "comparison_type": comparison_result.get("comparison_type"),
                "before_image": comparison_result.get("before_image"),
                "after_image": comparison_result.get("after_image"),
                "after_effect": comparison_result.get("after_effect"),
                "after_params": comparison_result.get("after_params", {}),
                "output_path": comparison_result.get("output_path"),
                "created_at": comparison_result.get("created_at"),
                "success": comparison_result.get("success", False),
                "recommendations": [
                    "建议使用高分辨率图片进行对比",
                    "建议添加对比说明和参数变化",
                    "建议使用滑块对比，更直观地展示效果差异",
                    "确保处理前后图片的拍摄角度和光照条件一致"
                ],
                "generated_at": datetime.now().isoformat()
            }
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/comparison_report_{report_id}.json"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, ensure_ascii=False, indent=2)
                print(f"✅ 对比报告已保存（JSON）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存对比报告失败: {e}")
                return None
    
    def print_comparison_summary(self, comparison_result: Dict[str, Any]) -> None:
        """
        打印对比摘要
        
        Args:
            comparison_result: 对比结果字典
        """
        print(f"\n📊 对比生成摘要")
        print(f"  对比类型: {comparison_result.get('comparison_type', '未知')}")
        print(f"  成功状态: {'✅ 成功' if comparison_result.get('success', False) else '❌ 失败'}")
        print(f"  生成时间: {comparison_result.get('created_at', '未知')}")
        
        # 打印图片信息
        before_image = comparison_result.get("before_image")
        if before_image:
            print(f"  处理前图片: {before_image}")
        
        after_image = comparison_result.get("after_image")
        if after_image:
            print(f"  处理后图片: {after_image}")
        
        after_effect = comparison_result.get("after_effect")
        if after_effect:
            print(f"  处理后效果: {after_effect}")
        
        # 打印输出路径
        output_path = comparison_result.get("output_path")
        if output_path:
            print(f"  输出路径: {output_path}")


# 使用示例
if __name__ == "__main__":
    # 初始化对比生成器
    generator = ComparisonGenerator()
    
    # 生成表面处理前后对比（使用图片）
    result = generator.generate_before_after_comparison(
        before_image="input/raw_surface.jpg",
        after_image="output/painting_effect.png",
        after_params={"color": "蓝色", "texture": "细纹"},
        output_path="output/before_after_comparison.html",
        title="喷塑处理前后对比"
    )
    print(f"生成前后对比: {result.get('output_path')}")
    generator.print_comparison_summary(result)
    
    # 生成表面处理前后对比（使用效果描述）
    result2 = generator.generate_before_after_comparison(
        before_image="input/raw_surface.jpg",
        after_effect="蓝色细纹喷塑效果，铝合金材质，表面有细纹纹理，触感舒适",
        after_params={"color": "蓝色", "texture": "细纹", "material": "铝合金"},
        output_path="output/before_after_comparison2.html",
        title="喷塑处理前后对比（效果描述）"
    )
    print(f"生成前后对比（效果描述）: {result2.get('output_path')}")
    
    # 生成滑块对比
    slider_result = generator.generate_slider_comparison(
        before_image="input/raw_surface.jpg",
        after_image="output/spraying_effect.png",
        output_path="output/slider_comparison.html",
        title="喷塑处理前后滑块对比"
    )
    print(f"生成滑块对比: {slider_result.get('output_path')}")
    
    # 批量生成对比
    batch_configs = [
        {
            "comparison_type": "before_after",
            "before_image": "input/raw_surface.jpg",
            "after_image": "output/painting_effect.png",
            "after_params": {"color": "红色", "finish": "高光", "material": "镁合金"},
            "title": "喷漆处理前后对比"
        },
        {
            "comparison_type": "slider",
            "before_image": "input/raw_surface.jpg",
            "after_image": "output/spraying_effect.png",
            "title": "喷塑处理前后滑块对比"
        }
    ]
    
    batch_results = generator.generate_batch_comparison(batch_configs)
    print(f"批量生成了 {len(batch_results)} 个对比")
    
    # 生成对比报告
    report_path = generator.generate_comparison_report(
        comparison_result=result,
        output_format='markdown',
        output_path="reports/comparison_report.md"
    )
    print(f"生成对比报告: {report_path}")
