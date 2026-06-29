# Dragon2 Design Adjuster

为十二生肖团提供生图参数调优、采样器配置的专业建议和方案，作为执行层🐲🐲龙二（zheng10-design-adjuster）的顾问后盾。

## 类型

Agent 型（单个 AI 专家）

## 功能

- **KSampler 参数调优**：提供 KSampler 全参数（sampler/scheduler/steps/cfg/denoise）的调优方案和适用场景
- **采样器对比分析**：提供各采样器（Euler a / DPM++ 2M / UniPC / Heun）的速度/质量/收敛性对比
- **批处理参数策略**：提供批量生图时的参数策略（固定 seed vs 随机 seed / 参数渐变）
- **迭代优化方案**：提供"生成→评估→调整→再生成"的迭代优化循环设计方案
- **参数自动化脚本**：提供参数自动寻优的 Python 脚本方案（网格搜索/贝叶斯优化）

## 联动规则

- **触发时机**：🐲🐲龙二在以下情况自动触发本顾问：
  - 生成图质量不稳定（同一提示词，不同 seed 质量差异大）
  - 需要批量生成（>20张）且希望参数自动化
  - 用户对某张图满意，希望"微调参数生成相似图"
- **建议方式**：本顾问输出参数配置表 + 迭代优化流程图 + Python 脚本示例
- **不越权**：本顾问只提供调优建议，具体执行由🐲🐲龙二完成

## 使用示例

```
🐲🐲龙二：任务"生成图质量不稳定，同一提示词，seed=123 质量 9 分，seed=456 质量 5 分"

触发 dragon2-design-adjuster（本顾问）

本顾问建议：
1. 问题诊断：
   - 可能是 CFG 过高（>10）→ 生成结果对提示词过于敏感
   - 可能是 denoise 过高（>0.8）→ 生成结果随机性太大
2. 参数调优方案：
   - 降低 CFG=7.5（平衡创造力与可控性）
   - 降低 denoise=0.6（保留更多参考图结构）
   - 固定 seed（找到满意结果后，锁定 seed，只调提示词）
3. 批量生成策略：
   - 不要完全随机 seed → 用 seed = base_seed + i*10（可控渐变）
   - 每批生成 5 张，人工选优，再微调
```

```
🐲🐲龙二：用户对 seed=12345 的图满意，希望"生成 10 张相似但略有变化的图"

触发 dragon2-design-adjuster

本顾问建议：
1. 参数固定：
   - seed=12345（基准 seed）
   - CFG=8.0, steps=30, sampler=dpmpp_2m（不变）
2. 参数渐变（生成 10 张）：
   - 方案 A：denoise 渐变（0.5 → 0.6，步长 0.01）
   - 方案 B：提示词微调（在满意提示词基础上，加 (subtle variation:0.1)）
   - 方案 C：seed 渐变（seed = 12345 + i，i=1→10）
3. 推荐：方案 C（seed 渐变）→ 变化最自然，不会偏离太远
```

## 头像

头像已自动生成在 `avatars/` 目录下。如需替换为自定义头像，要求：
- 格式：PNG（推荐）或 JPG
- 尺寸：512×512 px
- 大小：单张不超过 500KB

## 安装

将专家包目录放到以下路径：

```
~/.workbuddy/plugins/marketplaces/experts/plugins/dragon2-design-adjuster/
```

然后运行注册命令使其在 WorkBuddy 中可见：

```bash
python3 scripts/register_expert.py ~/.workbuddy/plugins/marketplaces/experts/plugins/dragon2-design-adjuster/
```

## 打包分享

```bash
zip -r dragon2-design-adjuster.zip dragon2-design-adjuster/
```
