---
version: "2.0.6"
author: "猴哥（十二生肖团）"
name: zheng10-bus
display_name: 十二生肖团通用互通总线
display_name_en: "Bus"
name_en: "zheng10-bus"
description_zh: "十二生肖团通用互通总线：全17角色共享产出池 + 静态联动映射表 + inbox 事件触发，让联动映射秒级路由、连接反应更迅速"
description_en: "Zodiac team execution-layer skill: Bus. (See description_zh for full details.)"
description: 十二生肖团通用互通总线：全17角色共享产出池 + 静态联动映射表 + inbox 事件触发，让联动映射秒级路由、连接反应更迅速
license: MIT
metadata:
  author: 猴哥
  version: "2.0.6"
  tags:
    - 资料总线
    - interconnection
    - event-bus
    - shared-pool
    - linked-map
  generated_date: 2026-07-29
  classification: P0-core
  merged_from:
    - "1.1（源侧内网）"
    - "2.0.5（分发对外）"
  merged_at: "2026-11-19"
when_to_use: "在涉及「bus」职责的任务中调用本技能；十二生肖团通用互通总线：全17角色共享产出池 + 静态联动映射表 + inbox 事件触发。"
---

# zheng10-bus · 生肖团通用互通总线（单一真相源）

> **定位**：把「视觉互通层」(视觉引擎) 跑通的成功模式从「视觉子域」抽象为
> **全团干线**，覆盖全部 17 职能（12 生肖 + 龙二「产品设计调整」+ 凤「自主进化协调器」+ 鼠/牛/马/羊/猴/狗 职能）。任何职能完成一项产出 → 写共享产出池 → 按静态
> **联动映射表**自动给下游 append 信箱(inbox) → 下游即时读信箱响应。
>
> **目标（用户原话）**：「让联动映射反应更快。连接反应更迅速。」
> - **联动映射反应更快** → 实体是**静态映射表**：把「下一步该谁干」从 LLM 临场推理降级为**查表秒级路由**。
> - **连接反应更迅速** → 实体是**事件触发(inbox 通知)** 替代全局轮询。

## 一、与 vision-core 的层级关系

```
zheng10-bus (通用干线，全17职能)
   ├── 视觉4角(兔/虎/猪/鸡) 的「看图结论」经 视觉引擎 出 → 同时写 bus 池 (ref=image_hash)
   └── 其余10角(鼠/牛/龙/龙二/蛇/马/羊/猴/狗/凤) 的产出 直接写 bus 池 (ref=业务key)
两池并存: vision_evidence.jsonl (视觉细节, 按图hash) + zodiac_bus.jsonl (通用事件, 按role+type+ref)
```

- **vision-core 是总线的「专用视觉通道」**：4 视觉职能依然走 vision_engine.js 看图，但其结论
  除写视觉证据池外，**也写 zodiac_bus.jsonl**（经本脚本 `--emit`，type=`analyze/collect/style/review`），
  让非视觉职能也能按 `ref`(image_hash) 拉到「某图已被分析/采集」事件。
- **本总线是通用骨干**：不替代 vision-core 的看图逻辑，只承载「产出互通 + 联动触发」。

## 二、三件套（总线技术基座）

1. **通用产出池** `<架构根目录>\logs\zodiac_bus.jsonl`（append-only，按 `role + type + ref` 索引，跨职能互通、重复不重复烧 token）。
2. **联动映射表** `<架构根目录>\logs\zodiac_bus_map.json`（静态配置：`emitter(role[.type]) → [下游职能]`；这是「联动映射」实体）。
3. **事件触发 / inbox** `<架构根目录>\logs\inbox/<role>.jsonl`（每职能一个信箱；上游 emit 后自动 append 下游信箱，下游读信箱秒级得通知，**非轮询**）。

## 三、CLI 用法（`zodiac_bus.js`）

```bash
# 1) 职能完成产出 → 写池 + 按映射表给下游 append inbox (核心: 事件触发)
node zodiac_bus.js --emit \
  --role rat --type requirement --product 吨吨桶 --ref req_001 \
  --content-file <本地资源路径>
# 或内联: --content '{"summary":"...","tasks":[...]}'

# 2) 查某职能 emit 后会触发哪些下游 (秒级路由, 替代 LLM 临场推理)
node zodiac_bus.js --map --role rat --type requirement

# 3) 读某职能信箱 (下游秒级得通知)
node zodiac_bus.js --inbox --role tiger
node zodiac_bus.js --inbox --role tiger --pending-only

# 4) 列出所有/某职能未处理事件
node zodiac_bus.js --pending
node zodiac_bus.js --pending --role tiger

# 5) 标记某信箱事件已处理
node zodiac_bus.js --mark-done --role tiger --id evt_xxx

# 6) 查某 ref 在池中已有的全部产出 (互通去重)
node zodiac_bus.js --pool --ref req_001
```

参数：
- `--emit`：写入模式（必带 `--role` + `--type`；`--ref`/`--product`/`--content`/`--content-file` 选带）
- `--role`：`rat|ox|tiger|rabbit|dragon|snake|horse|sheep|monkey|rooster|dog|pig`
- `--type`：产出类型（如 `requirement`/`collect`/`analyze`/`swot`/`design`/`standard`/`workflow`/`render`/`param`/`review`/`intel`/`style`）
- `--ref`：互通索引 key（需求=req_id；图=image_hash；产品=product 名）
- `--content` / `--content-file`：产出载荷（JSON 字符串或文件，写入池）
- `--map`：查下游映射
- `--inbox`：读信箱（`--pending-only` 仅未处理）
- `--pending`：列未处理（`--role` 限定）
- `--mark-done`：置已处理（`--id` 事件 id）
- `--pool`：按 ref 查池

## 四、17 职能接线契约（接线铁律）

每个职能的 SKILL.md / agents/*.md **必须**新增「产出写总线」MANDATORY 节，路由到本脚本 `--emit`：
- 视觉4角：保持 vision-core 通道，调用 vision_engine.js 后**额外** `--emit type=analyze/collect/style/review`，`--ref` 传 `image_hash`，`--content` 含结论摘要。
- 其余10角：完成产出后 `--emit`，`--ref` 传业务 key（如 `req_001` / `design_v3` / `render_007`），`--content` 含产出摘要 + 文件路径。
- 任何职能开工前先 `--inbox --pending-only` 看是否有上游通知（秒级感知），避免被动轮询。

## 五、确定性裁决

- 映射表是**静态确定性配置**，路由零歧义；改联动关系只改 `zodiac_bus_map.json`，不碰职能代码。
- inbox 去重：同一 `(from_role, recipient_role, ref, type)` 已存在 pending 则跳过 append，防 emit 重试炸信箱。
- 本脚本不替代业务裁决逻辑，只做「产出互通 + 事件路由」。

---

---

---

---

## 📚 资料总线（H 盘资料入口）

> 本技能可读的 H 盘资料已登记在**资料总线**，开工前先查一遍 —— 避免"重复造轮子"和"翻不到料"。

```bash
python <本地资源路径> --role zheng10-bus
python <本地资源路径> --kw <关键词>      # 元数据层：找「有哪些资料」
python <本地资源路径> --wb             # 工作台可挂载的料
python <本地资源路径> "一句话需求"    # 语义层：在 1.2 万篇业务库正文里找「哪一段」
python <本地资源路径> --role zheng10-bus "..."  # 限定本角色的资料范围内检索
```

**全量索引**：`<本地资源路径>` ｜ **清单**：`<本地资源路径>`

| 资料 | 路径 | 体量 | 用途 |
|---|---|---|---|
| `sys.arch` | `<架构根目录>` | 1.27 GB | 自治/系统 |

**硬数据优先**：凡涉及国标限值、材料参数、专利红线、竞品价格，**必须以本总线登记的真实文件为准**，不得凭记忆作答。

**出图/交付**：32 个标准提示词模板见 `<本地资源路径>`（结构化索引 `prompt_templates.json`，含分类/变量/正文/示例）。

> 两个入口分工：`lookup.py` 查**目录元数据**（有哪些资料、多大、谁能用）；`core_lookup.py` 查**内容语义**（哪份文件的哪一段讲了这件事）。

<!-- 资料总线区块结束 -->
