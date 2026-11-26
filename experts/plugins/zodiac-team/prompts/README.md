# prompts/ · 提示词卡清单

> 提示词**不集中在一处**（集中会产生第二真源 ⇒ 漂移）。此处只列**真源位置**。

| 用途 | 真源位置 | 说明 |
|---|---|---|
| 项目级速查（最高优先） | `H:\架构\.workbuddy\memory\MEMORY.md` | ≤3980 字符硬闸；速查行 + 状态锚点 + 精选纪律 |
| 细则全文 | `H:\架构\.workbuddy\memory\MEMORY_FACTS.md` | 227 KB，不受注入闸约束，靠检索取 |
| 专家角色卡（15 位） | `H:\SXJG\03_专家\zodiac-team\agents\*.md` | 每张卡含角色/目标/边界 |
| 调度总规则 | `settings.json` → `rules`（8 条） | 总调度中心 + 联动规则 |
| 契约四域 | `settings.json` → `workflowDeps` / `observability` / `learnings` / `evolution` | 框架契约 |
| 全局铁律 | `~/.workbuddy/user-.../personal/MEMORY.md` | 跨项目铁律七条 + 禁忌八条 |

## 写提示词纪律

1. **一句话一件事**；禁「不是…而是…」等翻案句（用 `human-writing` skill 的硬规则）。
2. 中文任务 ⇒ 提示词也要有**中文落点**（T95：否则路由恒匹配不到）。
3. 改提示词后**必须跑一次对应判据**（`regress_all.js`）⇒ 别自评自过。
