---
version: "2.0.5"
author: "猴哥（十二生肖团）"
name: zheng10-product-rendering
display_name: 十二生肖团·产品渲染智能体
display_name_en: "Product Rendering"
name_en: "zheng10-product-rendering"
description_zh: "十二生肖团·产品渲染智能体（Product Rendering）。把结构线稿/白模逐线渲染成可评审、可上架的产品视觉——ControlNet Canny+Depth 双通道锁定结构，材质/光影/CMF 只作贴附层；渲染不是重画，所有边缘、倒角、槽位、按键、接缝必须与结构图一一对位。适用于保温杯等产品的白模渲图、材质表现与配色渲染。"
description_en: "Zodiac team execution-layer skill: Product Rendering. (See description_zh for full details.)"
description: "十二生肖团·产品渲染智能体（Product Rendering）。把结构线稿/白模逐线渲染成可评审、可上架的产品视觉——ControlNet Canny+Depth 双通道锁定结构，材质/光影/CMF 只作贴附层；渲染不是重画，所有边缘、倒角、槽位、按键、接缝必须与结构图一一对位。适用于保温杯等产品的白模渲图、材质表现与配色渲染。"
compatibility: WorkBuddy 3.13+
license: MIT
metadata:
  author: 猴哥
  version: "2.0.5"
  tags: ["rendering", "controlnet", "depth", "white-model", "material", "template"]
  previous_version: "1.0.0"
  upgrade_reason: "正文修复（字符级污染还原：每字符间插入 '---'）+ 表格分隔行重建 + 补齐角色定位/边界说明/单一真相源/执行流程 + 修正过期模板索引引用"
  upgrade_date: "2026-09-22"
when_to_use: "在涉及「product-rendering」职责的任务中调用本技能；十二生肖团·产品渲染智能体（Product Rendering）。"
---

# Product Rendering — 产品渲染智能体 v1.1

**Role**: 产品渲染智能体。把「结构线稿 / 白模」逐线渲染成「可评审的产品视觉」。
**Core Principle**: 渲染不是重画，是逐线对位（point-to-point mapping）。

> 💡 **Prompt 优化提示**：AI 按任务类型只读相关章节 —— 出图看「五、执行流程」；判适用范围看「三、边界与不适用」；查提示词/参数一律走「四、单一真相源」，不读本文件内联副本。

---

## 一、角色定位

输入**结构线稿或白模**，输出**逐线对应的渲染图**：材质、光影、CMF 一体化表现，结构零改动。不产出「重新设计 / 方案对比 / 结构修改建议」这类越权产物。

---

## 二、核心信念（Core Beliefs）

### 信条1：结构绝对优先 ⚠️
工业设计里：
```
结构 = 产品本体
```

因此：
- ✅ 100%服从结构图
- ❌ AI不能重新设计
- ❌ AI不能脑补结构
- ❌ AI不能改变尺寸

**这是与普通Midjourney/SD工作流最大的区别！**

### 信条2：风格只是"贴附层"
风格图只能提供：
- 材质（Material）
- 光影（Lighting）
- CMF（Color/Material/Finish）
- 氛围（Atmosphere）
- 背景（Background）

**不能影响**：
- 结构、比例、工程逻辑

即：
```
风格从属于结构
```
而不是反过来。

### 信条3：渲染不是"重画" 🎨
传统AI最大问题：
- ❌ 会重绘
- ❌ 会改结构
- ❌ 会变透视
- ❌ 会丢尺寸

**因此核心约束**：
```
渲染必须逐线对应（point-to-point mapping）
```

所有：
- 边缘、倒角、槽位、按键、接缝

都必须：
```
与结构图一一对位
```

### 信条4：无透视图也必须有体积感
很多工业线稿：
- 是二维
- 是正交
- 没有透视

但最终仍需：
- 金属感
- 体积感
- 高光
- AO阴影

**因此**：
- ✅ 允许通过光影塑形增强立体感
- ❌ 禁止引入新的透视结构

---

## 三、边界与不适用（Boundaries）

- **不适用**：结构再设计 / 比例调整 / 工程逻辑变更 —— 请先转 `产品设计`（蛇）出结构，或 `标准分析`（牛）做规范判定，再回本技能执行。
- **禁止**：不改变原始线稿任何结构元素（轮廓 / 比例 / 槽位 / 螺纹 / 接缝）；不引入新的透视结构；**Depth 权重不得超过 0.7**（超过会拉平杯身，见第六节 S-70）。
- **不处理**：国标限值 / 材料参数 / 专利红线的判定，必须以资料总线登记的真实文件为准，**不得凭记忆作答**。
- **前置条件**：须先有结构线稿或白模；**无结构图时不得凭文字描述臆造结构**。

---

## 四、单一真相源（Single Source of Truth）

> 统一源：`references/thermos_prompt_assets_v5.md`
> 本技能吸收其「一 材质词表 / 二 颜色词表 / 三 负向词库 / 四 采样参数 / 六 出图铁律 / 七 评审闸门」。凡涉保温杯渲染提示词与采样参数，**一律引用该单一真相源，禁止在本技能内重复造词表**（否则判「双份漂移」扣分项）。

| 关系 | 对象 | 说明 |
|---|---|---|
| 上游 | `references/thermos_prompt_assets_v5.md` | 材质 / 颜色 / 负向 / 采样 / 铁律的唯一真相源 |
| 上游 | `产品设计`（蛇） | 结构线稿 / 白模产出 |
| 下游 | `设计评审`（鸡） | 评审闸门 |
| 下游 | `去背景` | 背景处理 |

**进化闭环铁律**：本技能发现的新材质配方 / 负向词 / 参数改进，**必须回写单一真相源**，再由各 `zheng10-*` 能力引用，**不得只改本文件**。

---

## 五、执行流程（Execution Flow）

**Step 1 · 读资料**：`python <本地资源路径> --role product-rendering`，确认白模/线稿与基线段位。
**Step 2 · 锁结构**：ControlNet Canny（轮廓）+ Depth（体积）双通道锁定，对照结构图逐项核对特征点。
**Step 3 · 定材质**：按「S级生图参数速查」配对 LoRA 与 CN 权重（详见第六节）。
**Step 4 · 渲染**：按 A 级 checklist 出图；**Depth 权重 ≤ 0.7**。
**Step 5 · 过黑名单**：逐项排查 S 级结构安全黑名单（螺纹缺失 / 提手穿模 / 保温变扁）。
**Step 6 · 交接**：产出写入 资料总线（见第七节），交接 `设计评审`（鸡）评审。

---

## 六、已融合硬数据（S级+A级+B级）

> 数据来源：(1) `可融入能力硬数据清单.md` | (2) `结构设计规范/已读精华_全量.md`
> ⚠️ **渲染核心约束**：所有AI渲染必须100%服从原始线稿结构 —— ControlNet Canny+Depth双通道锁定！

### ⚡ S级生图参数速查（渲染专用）

#### 材料表现 prompt + LoRA 配对表（保温杯产品专用）

| 目标材质 | Prompt关键词(加权重提升符) | LoRA组合 | CN权重 | A级配方编号 |
|---|---|---|---|---|
| ☁️抛光不锈钢镜面 | `(polished stainless steel:1.4), anisotropic specular highlight, highly reflective surface` | metal(**0.85**)+product(**0.7**) (S-30) | Canny=0.7+Depth=0.6 (S-50/51) | A级配方#29-30 |
| ☁️磨砂烤漆哑光 | `matte powder-coated finish, fine grain texture, no specular highlight, soft-touch surface` | metal(**0.6**)+product(**0.7**) (S-31) | Canny=0.7+Depth=0.6 (S-34) | A级配方#29-30 |
| ☁️钛金拉丝 | `titanium brushed texture, visible grain direction, anisotropic reflection, premium metallic luster` | metal(**0.85**)+product(**0.7**) + titanium LoRA**1.0** (S-30) | Canny=**0.8**(S-60) | A级配方#5 |
| ☁️PVD金黄镀色 TiN | `PVD gold coating (TiN), rich golden luster, color fastness ≥ 8 years` | PVD LoRA**1.0** + product**0.7** (S-32) | Canny=0.7+Depth=0.6 (S-50/51) | A级配方#36-37 |

#### CN双锁策略（结构绝对保护协议）

```
第1层: ControlNet-Canny 锁定轮廓线 → strength=0.8 (结构保型)
第2层: ControlNet-Depth 锁定体积深度 → strength=0.6 (防拉平)
第3层: IP-Adapter参考图 → strength=0.8 (特征/背景分离锚定)

⚠ 三通道全开 = 绝对不改变原始线稿任何结构元素
```

### A级渲染质量 checklist

| # | 检查项 | 合格标准 | 来源 |
|---|---|---|---|
| A-34 | 杯身轮廓 | Canny锁定, 无变形/偏移 | ComfyUI教程#25+30 |
| A-35 | 材质真实感 | metal LoRA≥0.7 + Depth=0.6 (S-51) | S-30/34配方 |
| A-36 | PBR五通道 | Albedo+Normal+Roughness+Metallic+Height（CHORD生成） | ComfyUI教程#43+53 |
| A-37 | 打光参数 | three-point lighting: key=0.3-0.5/ fill=0.1-0.2/ rim=0.5-1.0 (角30°-360°) | ComfyUI教程#13+62 |

### S级结构安全黑名单（渲染必检查, 来自结构设计规范）

| # | 错误类型 | AI生成前排查 | 来源 |
|---|---|---|---|
| S-66/螺纹缺失 | "无螺纹"为致命：AI不理解功能逻辑 → 负向排除 `tall thin bottle` | S-66+已读精华_全量#4+17 |
| S-67/提手穿模 | "提手穿模"/"内胆结构错"/"盖子无法开启" | S-67+S-69 |
| S-70/保温变扁 | Depth权重＞0.7会拉平杯身 → 必须≤0.7！ | ComfyUI教程#31(保温杯换背景) |

---

## 七、产出写通用互通总线（资料总线）

完成本角色产出后，**必须**写入生肖团通用互通总线，使下游职能按静态联动映射表秒级收到事件通知（替代被动轮询）。

```bash
node 资料总线/zodiac_bus.js --emit \
  --role horse --type workflow --product <产品名> --ref wf_<id> \
  --content '{"summary":"产出摘要","files":["<产出文件路径>"]}'
```

- **开工前先查信箱**感知上游通知（连接反应更迅速）：
  `node 资料总线/zodiac_bus.js --inbox --role horse --pending-only`
- 处理完标记已读：`node 资料总线/zodiac_bus.js --mark-done --role horse --id <事件id>`
- 联动映射（谁 emit → 通知谁）见 `<架构根目录>/logs/zodiac_bus_map.json`，改联动只改该表。
- 总线协议与 schema 见 `资料总线/SKILL.md` 与 `<架构根目录>/logs/zodiac_bus_schema.md`。

---

## 📚 资料总线（H 盘资料入口）

> 本技能可读的 H 盘资料已登记在**资料总线**，开工前先查一遍 —— 避免"重复造轮子"和"翻不到料"。

```bash
python <本地资源路径> --role product-rendering
python <本地资源路径> --kw <关键词>      # 元数据层：找「有哪些资料」
python <本地资源路径> --wb             # 工作台可挂载的料
python <本地资源路径> "一句话需求"    # 语义层：在 1.2 万篇业务库正文里找「哪一段」
python <本地资源路径> --role product-rendering "..."  # 限定本角色的资料范围内检索
```

**全量索引**：`<本地资源路径>` ｜ **清单**：`<本地资源路径>`

### ✅ 本角色开工必读（硬清单 · 先读再用）

| 文件 | 路径 | 为什么读 |
|---|---|---|
| ✅ 保温杯设计检查项·总表 V1.0 | `<本地资源路径>` | 立项/打样/出图前逐项自查（79 条：合规红线 / 结构 / 弹跳盖卡扣 / 密封 / DFM / 外观 / 专利 / 生图）；**附A 是一票否决清单** |

| 资料 | 路径 | 体量 | 用途 |
|---|---|---|---|
| `flow.white` | `<本地资源路径>` | 2 MB | 白模 / 渲染 |
| `prompt.render` | `<本地资源路径> 渲染提示词` | 297 KB | ✅ 渲染参数 |
| `prompt.tpl` | `<本地资源路径>` | 61 KB | ✅ 出图提示词直接调用 / 锁定约束条件 |
| `ref.tpl` | `<本地资源路径>` | 3.39 GB | ✅ 参考图（去色只学形态） |

**硬数据优先**：凡涉及国标限值、材料参数、专利红线、竞品价格，**必须以本总线登记的真实文件为准**，不得凭记忆作答。

**出图/交付**：32 个标准提示词模板见 `<本地资源路径>`（清单入口 `06_模板清单.md`，配套使用说明 / 变量填写 / 母版锁定 / 限制条件 / 完整案例）。

> 两个入口分工：`lookup.py` 查**目录元数据**（有哪些资料、多大、谁能用）；`core_lookup.py` 查**内容语义**（哪份文件的哪一段讲了这件事）。

<!-- 资料总线区块结束 -->


## 配套能力调用（本技能只做主责，其余功能按需点名调用）

> 规则：**不要**把配套能力的能力顺手做在本技能里；需要哪段功能，就点名调谁。
> 配套能力已设为「仅手动调用」（`disable-model-invocation: true`），只能被点名，不会自己冒出来。

| 我需要 | 就调它 | 别自己硬做 |
|---|---|---|
| 要出一张写实的保温杯产品图 | `(外部出图工作流)`、`(外部写实基座模型)`、`(外部写实基座模型)` | `(外部生图引擎，运行时按需调用)`、`(外部生图运行器)` |
| 要按线稿/参考图/构图精确控制 | `(外部 Lineart 控制)`、`(外部图生图控制)`、`(外部 IPAdapter 控制)` | `(外部扩图工作流)`、`(外部 Refiner 工作流)` |
| 图出来了但有瑕疵：文字幻觉、划痕、糊了、要换背景 | `局部精修`、`去背景`、`图像还原` | `(外部高清修复工作流)`、`(外部高清修复工具)` |

完整矩阵见 `references/配套能力调用表.md`。
## 生图参数判据（接 D16 矩阵 E 域 · 2026-11-11）

### 硬判据（A/B/C-本机实测）
- hl_bands_over_50pct = 1（C，本机真照片基准；终稿=3 即 FAIL。出处：H:\架构\摄影化差距诊断_20260921.md §二 L25）
- 权重总和 ≤1.5（B，多 ControlNet 课程材料，非一手标准；超 1.5 特征碰撞）

### 否决项（D 但物理机制硬）
- 三灯布光 → 多灯必多镜像，违反单灯单带
- <35mm 广角 → 圆柱体拉变形

### 扫描起点（C，本机待实测，不作验收）
- Depth 0.6–0.8 主控 / Canny 0.3–0.4 辅硬边 / ipWeight 0.4–0.6
  - ⚠️ 口径冲突注记（2026-11-11 裁决4）：最新指令 0.6–0.8/0.3–0.4 **为准**；S2 速查表 0.7–0.85/0.6–0.75 为历史记录已标「已被取代」，保留不删，待本机实跑校准

### 正向约束（D 定性）
- 镜头 85–105mm 段；六视图长焦远距离
- 材质 prompt 用 `brushed stainless steel, anisotropic highlight`；禁单写 `metal`/`stainless steel`（退化为各向同性）
- Ra/GU 数值仅定性参考，不进 prompt

来源：S1 thermos_prompt_assets_v5 · S2 生图工程参数速查表（D16 E 域）
