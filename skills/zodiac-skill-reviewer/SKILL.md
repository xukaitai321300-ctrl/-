---
name: zodiac-skill-reviewer
description: "auto-generated: skill package 'zodiac-skill-reviewer' (awaiting human review)"
license: MIT
metadata:
  author: WorkBuddy
  version: "1.0"
  tags: ["core"]
  generated_date: "2026-06-15"
  classification: P1-auto-standardized
---



# 十二生肖团技能完善性专家评审

## 核心定位
**系统性评审十二生肖团所有技能的完善性**，从专家角度检查技能完整性、协作能力、知识质量，输出可操作的改进建议。

## 评审维度（满分10分）

### 1. Frontmatter完整性（2分）
- ✅ 必需字段：`name`, `zodiac`, `role`, `description`
- ✅ 可选字段：`version`, `updated`, `skill_family`, `status`
- ❌ 缺失任字段扣0.5分

### 2. 触发场景章节（2分）
- ✅ 必须包含 `## 触发场景` 或等效章节
- ✅ 章节内容≥50字符（不是只有标题）
- ❌ 缺失章节扣2分，内容过少扣1分

### 3. 融合节格式统一性（1.5分）
- ✅ 标准格式：`## 知识融合补充 (from \`file\`)`
- ✅ 或：`## vX.X 融合更新`
- ❌ 非标准格式每条扣0.5分

### 4. 技能间交叉引用（1.5分）
- ✅ 必须引用至少1个其他生肖技能
- ✅ 在协作接口/集成能力章节中明确标注
- ❌ 无任何交叉引用扣1.5分

### 5. 蒸馏文件质量（1.5分）
- ✅ 必须存在 `SKILL_DISTILLED.md`
- ✅ 字符数≥5000（得分2分）或≥2000（得分1分）
- ✅ 包含基本的Markdown结构（`## `标题）
- ❌ 缺失文件扣1.5分

### 6. 垃圾内容检查（1分）
- ✅ 无Thai字符（\u0e00-\u0e7f）
- ✅ 无Arabic字符（\u0600-\u06ff）
- ✅ 无乱码行（连续特殊字符）
- ❌ 存在垃圾内容扣1分

### 7. 协作接口定义（1.5分）
- ✅ 明确输入定义（Input/输入/参数）
- ✅ 明确输出定义（Output/输出/返回）
- ❌ 两者都缺失扣1.5分，缺失一项扣0.5分

## 使用方法

### 快速评审（推荐）
```bash
PYTHONIOENCODING=utf-8 C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe I:\AI日记\Claw\expert_review_v2.py
```

### 自定义评审
修改 `references/expert_review_v2.py` 中的评审逻辑，调整评分权重或添加新维度。

## 评审脚本说明

`references/expert_review_v2.py` 提供：
- 自动化评分（7个维度，满分10分）
- 问题定位（精确到具体章节）
- 汇总统计（平均分、最高/最低分、分布）
- 详细排名（按评分从高到低）

## 评审结果解读

| 评分范围 | 等级 | 建议 |
|---------|------|------|
| 9-10分 | ✅ 优秀 | 可直接使用，无需修改 |
| 7-8分 | ⚠️ 良好 | 有少量问题，建议优化 |
| <7分 | ❌ 不达标 | 必须修复，否则影响协作 |

## 常见问题和修复方案

### 问题1：缺少触发场景
**修复**：在 `## 触发场景` 章节添加：
```markdown
## 触发场景

### 主动触发
1. "示例指令1"
2. "示例指令2"

### 被动触发
- 其他技能完成后自动触发
```

### 问题2：缺少技能间交叉引用
**修复**：添加 `## 协作接口` 章节（参考 `references/colab_template.md`）

### 问题3：蒸馏文件质量低
**修复**：运行智能蒸馏脚本
```bash
PYTHONIOENCODING=utf-8 C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe I:\AI日记\Claw\smart_distill_v27.py
```

### 问题4：存在垃圾内容
**修复**：运行清理脚本
```bash
PYTHONIOENCODING=utf-8 C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe I:\AI日记\Claw\clean_snake_garbage.py
```

## 输出格式

```
======================================================================
十二生肖团专家级完善性评审 v2
======================================================================

✅ 🐭 鼠 | 评分:9.0/10
    - 缺少技能间交叉引用

...

======================================================================
汇总统计
======================================================================
平均评分: 9.36/10
最高分: 10.0/10
最低分: 8.0/10
≥8分技能: 11个
6-8分技能: 0个
<6分技能: 0个
```

## 更新记录

- **v1.0 (2026-05-29)**: 初始版本，7维度评审框架

## Usage Examples

### Example 1: Basic Usage

```bash
python scripts/example.py
```

### Example 2: Advanced Usage

```python
from src.main import MainClass

obj = MainClass()
result = obj.run()
```

## 注意事项

- 执行前确保依赖工具已安装
- 如遇报错请查看详细日志输出
- 重要步骤需人工确认后再执行


## 语言说明
本文档使用简体中文编写，请确保所有操作输出也为中文。
