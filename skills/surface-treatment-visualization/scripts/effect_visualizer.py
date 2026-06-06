"""
效果展示工具（增强版） - Effect Visualizer
负责展示表面处理效果图片，支持多种展示模式
"""

import json
import os
import base64
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse


class EffectVisualizer:
    """效果展示器（增强版）"""
    
    def __init__(self, output_dir: str = "output"):
        """
        初始化展示器
        
        Args:
            output_dir: 输出目录
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def visualize_effect(self, effect_image_path: str, output_path: str = None, 
                        title: str = None, description: str = None) -> Dict[str, Any]:
        """
        展示单个表面处理效果
        
        Args:
            effect_image_path: 效果图片路径
            output_path: 输出HTML文件路径
            title: 标题
            description: 描述
            
        Returns:
            可视化结果字典
        """
        # 检查图片是否存在
        if not os.path.exists(effect_image_path):
            return {"error": f"效果图片不存在: {effect_image_path}"}
        
        # 创建可视化结果
        result = {
            "success": True,
            "effect_image_path": effect_image_path,
            "visualization_type": "static",
            "view_url": None,
            "interactive_elements": ["zoom", "rotate", "pan"],
            "title": title or "表面处理效果展示",
            "description": description or "",
            "created_at": datetime.now().isoformat()
        }
        
        # 生成可视化HTML
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 读取图片并转换为base64
                with open(effect_image_path, 'rb') as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                # 获取图片格式
                img_format = effect_image_path.split('.')[-1].lower()
                if img_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                    img_format = 'png'
                
                # 创建HTML页面
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{result['title']}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                        h1 {{ color: #333; text-align: center; }}
                        .description {{ text-align: center; color: #666; margin-bottom: 30px; }}
                        .effect-container {{ 
                            max-width: 1000px; 
                            margin: 0 auto; 
                            background-color: white; 
                            padding: 20px; 
                            border-radius: 10px; 
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        }}
                        .effect-image {{ 
                            max-width: 100%; 
                            height: auto; 
                            display: block; 
                            margin: 20px auto; 
                            border: 1px solid #ddd; 
                            border-radius: 5px;
                            cursor: zoom-in;
                        }}
                        .controls {{ 
                            text-align: center; 
                            margin-top: 20px; 
                            padding: 20px;
                            background-color: #f9f9f9;
                            border-radius: 5px;
                        }}
                        button {{ 
                            margin: 5px 10px; 
                            padding: 10px 20px; 
                            background-color: #4CAF50; 
                            color: white; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer; 
                            font-size: 14px;
                        }}
                        button:hover {{ background-color: #45a049; }}
                        button:disabled {{ background-color: #cccccc; cursor: not-allowed; }}
                        .info {{ 
                            margin-top: 20px; 
                            padding: 15px; 
                            background-color: #e8f4fd; 
                            border-left: 4px solid #2196F3; 
                            border-radius: 5px;
                        }}
                        .zoom-info {{ 
                            position: absolute; 
                            top: 10px; 
                            right: 10px; 
                            background-color: rgba(0,0,0,0.7); 
                            color: white; 
                            padding: 5px 10px; 
                            border-radius: 5px; 
                            font-size: 12px;
                        }}
                    </style>
                </head>
                <body>
                    <h1>{result['title']}</h1>
                    {f"<div class='description'>{result['description']}</div>" if result['description'] else ''}
                    
                    <div class="effect-container">
                        <div class="zoom-info" id="zoomInfo">缩放: 100%</div>
                        <img src="data:image/{img_format};base64,{img_data}" alt="表面处理效果" class="effect-image" id="effectImage">
                        
                        <div class="controls">
                            <button onclick="zoomIn()">🔍 放大</button>
                            <button onclick="zoomOut()">🔍 缩小</button>
                            <button onclick="rotate()">🔄 旋转</button>
                            <button onclick="resetView()">↺ 重置</button>
                            <button onclick="panLeft()">⬅ 左移</button>
                            <button onclick="panRight()">➡ 右移</button>
                        </div>
                        
                        <div class="info">
                            <strong>📊 操作说明：</strong><br>
                            - 使用放大/缩小按钮或鼠标滚轮缩放图片<br>
                            - 使用旋转按钮旋转图片<br>
                            - 使用左移/右移按钮或拖拽移动图片<br>
                            - 点击重置按钮恢复初始状态
                        </div>
                    </div>
                    
                    <script>
                        let currentZoom = 1.0;
                        let currentRotation = 0;
                        let currentPanX = 0;
                        let isDragging = false;
                        let startX = 0;
                        
                        const img = document.getElementById('effectImage');
                        const zoomInfo = document.getElementById('zoomInfo');
                        
                        // 放大
                        function zoomIn() {{
                            currentZoom = Math.min(currentZoom * 1.2, 5.0);
                            updateTransform();
                        }}
                        
                        // 缩小
                        function zoomOut() {{
                            currentZoom = Math.max(currentZoom / 1.2, 0.2);
                            updateTransform();
                        }}
                        
                        // 旋转
                        function rotate() {{
                            currentRotation += 90;
                            if (currentRotation >= 360) currentRotation = 0;
                            updateTransform();
                        }}
                        
                        // 重置视图
                        function resetView() {{
                            currentZoom = 1.0;
                            currentRotation = 0;
                            currentPanX = 0;
                            updateTransform();
                        }}
                        
                        // 左移
                        function panLeft() {{
                            currentPanX -= 50;
                            updateTransform();
                        }}
                        
                        // 右移
                        function panRight() {{
                            currentPanX += 50;
                            updateTransform();
                        }}
                        
                        // 更新变换
                        function updateTransform() {{
                            img.style.transform = `scale(${{currentZoom}}) rotate(${{currentRotation}}deg) translateX(${{currentPanX}}px)`;
                            zoomInfo.textContent = `缩放: ${{Math.round(currentZoom * 100)}}%`;
                        }}
                        
                        // 鼠标滚轮缩放
                        img.addEventListener('wheel', function(e) {{
                            e.preventDefault();
                            if (e.deltaY < 0) {{
                                zoomIn();
                            }} else {{
                                zoomOut();
                            }}
                        }});
                        
                        // 拖拽功能
                        img.addEventListener('mousedown', function(e) {{
                            isDragging = true;
                            startX = e.clientX - currentPanX;
                            img.style.cursor = 'grabbing';
                        }});
                        
                        document.addEventListener('mousemove', function(e) {{
                            if (!isDragging) return;
                            currentPanX = e.clientX - startX;
                            updateTransform();
                        }});
                        
                        document.addEventListener('mouseup', function() {{
                            isDragging = false;
                            img.style.cursor = 'zoom-in';
                        }});
                    </script>
                </body>
                </html>
                """
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                result["view_url"] = output_path
                print(f"✅ 效果展示页面已生成: {output_path}")
                
            except Exception as e:
                print(f"❌ 生成效果展示页面失败: {e}")
                result["error"] = str(e)
        
        return result
    
    def visualize_effects_comparison(self, effect_images: List[str], output_path: str = None,
                                     title: str = None, layout: str = "horizontal") -> Dict[str, Any]:
        """
        展示多个表面处理效果对比
        
        Args:
            effect_images: 效果图片路径列表
            output_path: 输出HTML文件路径
            title: 标题
            layout: 布局方式 ('horizontal' 或 'vertical')
            
        Returns:
            可视化结果字典
        """
        # 检查图片是否存在
        for img_path in effect_images:
            if not os.path.exists(img_path):
                return {"error": f"效果图片不存在: {img_path}"}
        
        # 创建可视化结果
        result = {
            "success": True,
            "effect_images": effect_images,
            "visualization_type": "comparison",
            "view_url": None,
            "comparison_mode": "side_by_side",
            "layout": layout,
            "title": title or "表面处理效果对比",
            "created_at": datetime.now().isoformat()
        }
        
        # 生成可视化HTML
        if output_path:
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 创建图片HTML
                images_html = ""
                for i, img_path in enumerate(effect_images):
                    # 读取图片并转换为base64
                    with open(img_path, 'rb') as img_file:
                        img_data = base64.b64encode(img_file.read()).decode('utf-8')
                    
                    # 获取图片格式
                    img_format = img_path.split('.')[-1].lower()
                    if img_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                        img_format = 'png'
                    
                    images_html += f"""
                    <div style="flex: 1; margin: 10px; text-align: center;">
                        <h3>效果 {i+1}</h3>
                        <img src="data:image/{img_format};base64,{img_data}" alt="表面处理效果 {i+1}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;">
                    </div>
                    """
                
                # 根据布局方式设置CSS
                if layout == "vertical":
                    flex_direction = "column"
                else:
                    flex_direction = "row"
                
                # 创建HTML页面
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{result['title']}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                        h1 {{ color: #333; text-align: center; }}
                        .effects-container {{ 
                            display: flex; 
                            flex-direction: {flex_direction}; 
                            justify-content: center; 
                            align-items: center;
                            flex-wrap: wrap;
                            margin-top: 30px;
                            background-color: white;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        }}
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
                    
                    <div class="effects-container">
                        {images_html}
                    </div>
                    
                    <div class="info">
                        <strong>📊 对比说明：</strong><br>
                        - 上方展示了 {len(effect_images)} 个表面处理效果<br>
                        - 鼠标悬停在图片上可以放大查看<br>
                        - 当前布局方式: {layout}
                    </div>
                </body>
                </html>
                """
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                result["view_url"] = output_path
                print(f"✅ 效果对比页面已生成: {output_path}")
                
            except Exception as e:
                print(f"❌ 生成效果对比页面失败: {e}")
                result["error"] = str(e)
        
        return result
    
    def generate_visualization_report(self, visualization_result: Dict[str, Any], 
                                     output_format: str = 'json', 
                                     output_path: str = None) -> str:
        """
        生成可视化报告（增强版）
        
        Args:
            visualization_result: 可视化结果字典
            output_format: 输出格式 ('json' 或 'markdown')
            output_path: 输出文件路径
            
        Returns:
            输出文件路径
        """
        # 创建报告
        report_id = f"VISUAL-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}"
        
        if output_format == 'markdown':
            # 生成Markdown格式报告
            report_content = f"""# 表面处理效果可视化报告

## 基本信息
- **报告ID**：{report_id}
- **标题**：{visualization_result.get('title', '表面处理效果可视化报告')}
- **生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **可视化类型**：{visualization_result.get('visualization_type', '未知')}

## 可视化详情
- **视图URL**：{visualization_result.get('view_url', '无')}
- **交互元素**：{', '.join(visualization_result.get('interactive_elements', []))}
- **布局方式**：{visualization_result.get('layout', '水平')}

## 效果图片
"""
            # 添加效果图片信息
            effect_images = visualization_result.get('effect_images', [visualization_result.get('effect_image_path', '')])
            for i, img_path in enumerate(effect_images):
                if img_path:
                    report_content += f"{i+1}. **图片 {i+1}**：{img_path}\n"
            
            report_content += f"""
## 建议
1. 建议使用高分辨率图片进行展示
2. 建议添加效果描述和参数说明
3. 建议支持交互式操作（放大、缩小、旋转等）
4. 对于对比展示，建议使用一致的拍摄角度和光照条件

## 总结
- **图片数量**：{len([img for img in effect_images if img])}
- **交互功能**：{'支持' if visualization_result.get('interactive_elements') else '不支持'}
- **可视化类型**：{visualization_result.get('visualization_type', '未知')}
"""
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/visualization_report_{report_id}.md"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(report_content)
                print(f"✅ 可视化报告已保存（Markdown）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存可视化报告失败: {e}")
                return None
            
        else:  # JSON格式
            report = {
                "report_id": report_id,
                "title": visualization_result.get("title", "表面处理效果可视化报告"),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "visualization_type": visualization_result.get("visualization_type"),
                "view_url": visualization_result.get("view_url"),
                "effect_images": visualization_result.get("effect_images", []),
                "interactive_elements": visualization_result.get("interactive_elements", []),
                "layout": visualization_result.get("layout", "horizontal"),
                "recommendations": [
                    "建议使用高分辨率图片进行展示",
                    "建议添加效果描述和参数说明",
                    "建议支持交互式操作（放大、缩小、旋转等）",
                    "对于对比展示，建议使用一致的拍摄角度和光照条件"
                ],
                "generated_at": datetime.now().isoformat()
            }
            
            # 保存报告
            if not output_path:
                output_path = f"{self.reports_dir}/visualization_report_{report_id}.json"
            
            try:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(report, f, ensure_ascii=False, indent=2)
                print(f"✅ 可视化报告已保存（JSON）: {output_path}")
                return output_path
            except Exception as e:
                print(f"❌ 保存可视化报告失败: {e}")
                return None
    
    def print_visualization_summary(self, visualization_result: Dict[str, Any]) -> None:
        """
        打印可视化摘要
        
        Args:
            visualization_result: 可视化结果字典
        """
        print(f"\n📊 可视化摘要")
        print(f"  可视化类型: {visualization_result.get('visualization_type', '未知')}")
        print(f"  成功状态: {'✅ 成功' if visualization_result.get('success', False) else '❌ 失败'}")
        print(f"  生成时间: {visualization_result.get('created_at', '未知')}")
        
        # 打印图片信息
        effect_images = visualization_result.get('effect_images', [visualization_result.get('effect_image_path', '')])
        valid_images = [img for img in effect_images if img]
        if valid_images:
            print(f"  图片数量: {len(valid_images)}")
            for i, img_path in enumerate(valid_images):
                print(f"    {i+1}. {img_path}")
        
        # 打印视图URL
        view_url = visualization_result.get("view_url")
        if view_url:
            print(f"  视图URL: {view_url}")
        
        # 打印交互元素
        interactive_elements = visualization_result.get("interactive_elements", [])
        if interactive_elements:
            print(f"  交互元素: {', '.join(interactive_elements)}")


# 使用示例
if __name__ == "__main__":
    # 初始化效果展示器
    visualizer = EffectVisualizer()
    
    # 展示单个表面处理效果
    result = visualizer.visualize_effect(
        effect_image_path="output/painting_effect.png",
        output_path="output/effect_visualization.html",
        title="喷漆效果展示",
        description="红色高光喷漆效果，镁合金材质"
    )
    print(f"效果展示页面: {result.get('view_url')}")
    visualizer.print_visualization_summary(result)
    
    # 展示多个表面处理效果对比
    comparison_result = visualizer.visualize_effects_comparison(
        effect_images=["output/painting_effect.png", "output/spraying_effect.png"],
        output_path="output/effects_comparison.html",
        title="喷漆 vs 喷塑效果对比",
        layout="horizontal"
    )
    print(f"效果对比页面: {comparison_result.get('view_url')}")
    
    # 生成可视化报告
    report_path = visualizer.generate_visualization_report(
        visualization_result=result,
        output_format='markdown',
        output_path="reports/visualization_report.md"
    )
    print(f"生成可视化报告: {report_path}")
