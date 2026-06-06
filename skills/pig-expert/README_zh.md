# 猪专家（风格参考与Prompt素材专家）

十二生肖团 - 猪专家（风格参考与Prompt素材专家）

## 角色定位

**猪专家**是十二生肖团中的"风格参考与Prompt素材专家"，负责：
- 管理和维护风格参考库
- 整理和优化Prompt素材库
- 生成风格化的Prompt模板
- 优化AI生图效果和风格一致性
- 建立风格-素材-Prompt的关联体系

## 核心职能

### 1. 风格参考管理
- 收集和产品设计风格参考（现代简约、工业风、科技风等）
- 整理和分类风格参考图片和描述
- 建立风格标签体系和检索机制
- 更新和维护风格参考库

### 2. Prompt素材库整理
- 收集和整理Prompt关键词库
- 分类和标签化Prompt素材（材质、功能、场景、风格等）
- 优化Prompt表达和描述精度
- 建立Prompt素材检索和使用机制

### 3. 风格化Prompt生成
- 根据设计需求生成风格化Prompt
- 结合风格参考和Prompt素材生成高质量Prompt
- 优化Prompt以提升AI生图效果
- 生成Prompt变体和优化建议

### 4. AI生图效果优化
- 分析AI生图效果和风格一致性
- 优化Prompt以提升生图质量
- 调整风格参数和权重
- 建立生图效果评估和反馈机制

## 工作流程

### 阶段1：风格需求分析
1. 明确设计需求和风格定位
2. 确定风格参考类型和数量
3. 制定Prompt生成策略

### 阶段2：风格参考收集
1. 从风格参考库检索相关风格
2. 收集和整理风格参考图片和描述
3. 分析和提取风格关键特征
4. 建立风格特征向量表示

### 阶段3：Prompt素材整理
1. 从Prompt素材库检索相关素材
2. 整理和分类Prompt关键词
3. 优化Prompt表达和描述
4. 生成Prompt模板和变体

### 阶段4：风格化Prompt生成
1. 结合风格参考和Prompt素材
2. 生成风格化Prompt
3. 优化Prompt以提升生图效果
4. 生成Prompt变体和优化建议

### 阶段5：效果评估和优化
1. 使用Prompt生成AI图片
2. 评估生图效果和风格一致性
3. 优化Prompt和风格参数
4. 更新风格参考库和Prompt素材库

## 技能包结构

```
pig-expert/
├── SKILL.md                      # 技能包主文档
├── README.md                     # 英文说明文档
├── README_zh.md                  # 中文说明文档
├── LICENSE                       # 许可证
├── CONTRIBUTING.md               # 贡献指南
├── CODE_OF_CONDUCT.md            # 行为准则
├── CHANGELOG.md                  # 变更日志
├── AUTHORS.md                    # 作者信息
├── .gitignore                    # Git忽略文件
├── data/                         # 数据目录
│   ├── style_references.json     # 风格参考库
│   ├── prompt_templates.json     # Prompt模板库
│   ├── material_library.json     # 材质素材库
│   └── style_prompt_mapping.json # 风格-Prompt映射
├── scripts/                      # 脚本目录
│   ├── style_manager.py          # 风格管理工具
│   ├── prompt_generator.py       # Prompt生成工具
│   ├── material_searcher.py      # 素材搜索工具
│   └── effect_analyzer.py        # 效果分析工具
└── tests/                        # 测试目录
    ├── test_style_manager.py
    ├── test_prompt_generator.py
    ├── test_material_searcher.py
    └── test_effect_analyzer.py
```

## 安装和使用

### 安装依赖

```bash
pip install requests pandas numpy matplotlib Pillow
```

### 使用示例

#### 示例1：管理风格参考
```python
from scripts.style_manager import StyleManager

# 初始化风格管理器
manager = StyleManager()

# 添加风格参考
style_ref = manager.add_style_reference(
    style_name="现代简约",
    description="简洁、实用、功能性强",
    reference_images=["image1.jpg", "image2.jpg"],
    tags=["现代", "简约", "实用"]
)

# 搜索风格参考
results = manager.search_style_references(keyword="现代简约")
print(results)
```

#### 示例2：生成风格化Prompt
```python
from scripts.prompt_generator import PromptGenerator

# 初始化Prompt生成器
generator = PromptGenerator()

# 生成风格化Prompt
prompt = generator.generate_styled_prompt(
    product="弹跳盖保温杯",
    style="现代简约",
    features=["轻量化", "防误触", "车载适配"],
    materials=["镁合金", "PP", "硅胶"]
)

# 输出Prompt
print(prompt)
```

## 风格参考库

### 风格分类

#### 1. 现代简约风
- **特征**: 简洁、实用、功能性强
- **关键词**: 现代、简约、实用、功能、简洁
- **应用场景**: 电动轮椅、保温杯、家居产品

#### 2. 工业风
- **特征**: 硬朗、机械感、金属质感
- **关键词**: 工业、硬朗、机械、金属、质感
- **应用场景**: 电动轮椅车架、金属配件

#### 3. 科技风
- **特征**: 未来感、智能、科技感
- **关键词**: 科技、未来、智能、创新、数字
- **应用场景**: 智能电动轮椅、智能保温杯

#### 4. 自然风
- **特征**: 环保、自然、有机
- **关键词**: 自然、环保、有机、生态、绿色
- **应用场景**: 环保材料产品、有机食品容器

## Prompt素材库

### Prompt分类

#### 1. 材质类
- **金属材质**: 镁合金、铝合金、不锈钢、钛合金
- **塑料材质**: PP、ABS、PC、TRITAN、硅胶
- **其他材质**: 碳纤维、木材、玻璃、陶瓷

#### 2. 功能类
- **电动轮椅**: 轻量化、折叠便携、智能导航、健康监测
- **保温杯**: 弹跳盖、防误触、车载适配、USB加热

#### 3. 场景类
- **室内场景**: 家居、办公室、医院
- **室外场景**: 公园、街道、旅行
- **车载场景**: 汽车杯架、USB充电、磁吸固定

#### 4. 风格类
- **现代简约**: 简洁、实用、功能性强
- **工业风**: 硬朗、机械感、金属质感
- **科技风**: 未来感、智能、科技感

## 输出格式

### 1. 风格参考报告
```json
{
  "report_id": "STYLE-20260605-001",
  "title": "现代简约风格参考报告",
  "date": "2026-06-05",
  "style_name": "现代简约",
  "description": "简洁、实用、功能性强",
  "reference_images": ["image1.jpg", "image2.jpg"],
  "key_features": ["简洁", "实用", "功能性"],
  "keywords": ["现代", "简约", "实用", "功能", "简洁"],
  "application_scenarios": ["电动轮椅", "保温杯", "家居产品"],
  "prompt_templates": ["现代简约风格的{产品}", "简洁实用的{产品}设计"]
}
```

### 2. Prompt生成报告
```json
{
  "report_id": "PROMPT-20260605-001",
  "title": "弹跳盖保温杯Prompt生成报告",
  "date": "2026-06-05",
  "product": "弹跳盖保温杯",
  "style": "现代简约",
  "prompt": "现代简约风格的弹跳盖保温杯，采用镁合金杯身和PP内胆，具有轻量化、防误触、车载适配等功能，简洁实用的设计风格",
  "prompt_variants": [
    "现代简约风格的弹跳盖保温杯，镁合金杯身，轻量化设计",
    "简洁实用的弹跳盖保温杯，PP内胆，防误触设计",
    "功能性弹跳盖保温杯，车载适配，现代简约风格"
  ],
  "recommendations": ["加强轻量化设计", "优化防误触机制", "提升车载适配性"]
}
```

## 质量标准

### 风格参考质量
- **完整性**: 风格参考的完整性和代表性
- **准确性**: 风格特征描述的准确性
- **可检索性**: 风格参考的检索效率和精度
- **时效性**: 风格参考的更新频率

### Prompt生成质量
- **相关性**: Prompt与产品需求的相关性
- **准确性**: Prompt描述的准确性
- **风格一致性**: Prompt与风格参考的一致性
- **可生成性**: Prompt的可生成性和效果

## 与其他专家协作

### 协作流程
1. **鼠专家**（需求分析专家）: 明确风格需求
2. **猪专家**（风格参考与Prompt素材专家）: 提供风格参考和Prompt素材
3. **羊专家**（ComfyUI生图核心专家）: 使用Prompt生成AI图片
4. **鸡专家**（AI生图评审专家）: 评审生图效果和风格一致性
5. **猪专家**（风格参考与Prompt素材专家）: 优化Prompt和风格参考

### 协作输出
- **风格需求清单**: 鼠专家 → 猪专家
- **风格参考和Prompt素材**: 猪专家 → 羊专家
- **AI生图效果评估**: 鸡专家 → 猪专家
- **优化后Prompt和风格参考**: 猪专家 → 羊专家

## 版本历史

### v1.0.0 (2026-06-05)
- 初始版本
- 实现核心风格参考管理和Prompt生成功能
- 支持风格参考库和Prompt素材库管理
- 提供风格化Prompt生成和效果优化功能

## 许可证

MIT License

## 联系方式

- **作者**: 速凡团队（浙江永康）
- **邮箱**: contact@sufan-team.com
- **官网**: https://www.sufan-team.com

---

**最后更新**: 2026-06-05  
**文档版本**: v1.0.0
