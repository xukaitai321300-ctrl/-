---
name: zheng10-comfyui-thermos
display_name: ComfyUI 出图与保温杯产品图
display_name_en: "Comfyui Thermos"
name_en: "zheng10-comfyui-thermos"
description_zh: "ComfyUI 出图、生图、批量出图、白底主视图、出保温杯产品图时使用。zheng10-comfyui-thermos skill package — ComfyUI 保温杯/饮具生图信念、LoRA 触发词规范与提示词工程知识库（材质×颜色词表/负向词库/采样参数/场景维度），供 agent 层（羊/猴/猪）驱动工作台时遵循，防品类漂移与塑料感/黑剪影缺陷"
description_en: "Zodiac team execution-layer skill: Comfyui Thermos. (See description_zh for full details.)"
version: "2.4.5"
author: "猴哥（十二生肖团）"
description: >-
  ComfyUI 出图、生图、批量出图、白底主视图、出保温杯产品图时使用。zheng10-comfyui-thermos skill package — ComfyUI 保温杯/饮具生图信念、LoRA
  触发词规范与提示词工程知识库（材质×颜色词表/负向词库/采样参数/场景维度），供 agent
  层（羊/猴/猪）驱动工作台时遵循，防品类漂移与塑料感/黑剪影缺陷
compatibility: WorkBuddy 3.13+
tags:
  - auto-fixed
  - workbuddy-standard
license: MIT
when_to_use: "在涉及「zheng10-comfyui-thermos」职责的任务中调用本技能；ComfyUI 出图、生图、批量出图、白底主视图、出保温杯产品图时使用。"
---

## 配套能力调用（本技能只做主责，其余功能按需点名调用）

> 规则：**不要**把配套能力的能力顺手做在本技能里；需要哪段功能，就点名调谁。
> 配套能力已设为「仅手动调用」（`disable-model-invocation: true`），只能被点名，不会自己冒出来。

| 我需要 | 就调它 | 别自己硬做 |
|---|---|---|
| 要出一张写实的保温杯产品图 | `zheng10-comfyui-thermos`、`(外部写实基座模型)`、`(外部写实基座模型)` | `(外部生图引擎，运行时按需调用)`、`(外部生图运行器)` |
| 要按线稿/参考图/构图精确控制 | `(外部 Lineart 控制)`、`(外部图生图控制)`、`(外部 IPAdapter 控制)` | `(外部扩图工作流)`、`(外部 Refiner 工作流)` |
| 要训练或加载速凡风格 LoRA | `(外部 LoRA 训练资料)`、`(外部 LoRA 工作流)` | `(外部模型合并工具)`、`(外部桥接工具)` |
| 提示词写得不好，画面不对 | `(外部提示词工具)`、`(外部提示词优化)`、`(外部提示词优化)` | `(外部提示词专家)`、`(外部提示词范式)` |
| 图出来了但有瑕疵：文字幻觉、划痕、糊了、要换背景 | `局部精修`、`去背景`、`图像还原` | `(外部高清修复工作流)`、`(外部高清修复工具)` |
| 要把产品做成 3D 看结构 | `(外部图生3D工具)` | `(外部生图引擎)` |
| 要产品动效或演示视频 | `(外部动画工作流)`、`(外部视频工作流)` | — |

完整矩阵见 `references/配套能力调用表.md`（或 `<本地资源路径>`）。
# 一、能力定位

本技能沉淀「ComfyUI 生图 = 可控工业生产」的方法论，并登记保温杯/饮具生图所需的 **LoRA 触发词映射 + 品类闸门**。

适用场景：生肖团中 生图核心/设计调整/风格参考经「保温杯变款工作台」(`<架构根目录>\保温杯变款工作台_MVP.html`) 驱动 ComfyUI 生图时，必须先读本技能，选对 LoRA 与触发词，避免把大容量水壶（jug）误渲染成杯/瓶。

> **加载说明（2026-09 修正）**：本技能 frontmatter 无 `disable` 字段（tag 为 `auto-fixed` / `workbuddy-standard`），编排层调用 `zheng10-*` 执行层时即会加载。使用铁律不变——**驱动工作台生图前必须先 `Read` 本文件**，选对 LoRA + 触发词 + 提示词维度，否则易出现品类漂移 / 塑料感 / 文字幻觉。

# 一·五、实时环境对齐（2026-09 实测基准，所有参数以此为准）

| 项 | 当前实测值 | 避坑点 |
|---|---|---|
| ComfyUI 版本 | 0.17.0（API 端口 127.0.0.1:8188） | VRAM 空闲约 14.6GB（RTX 5080 16GB），叠加 2 个 ControlNet 仍安全 |
| 底模 | `sd_xl_base_1.0` | **不要退回 SD1.5**（`v1-5-pruned-emaonly` 等）——保温杯写实已验证 SDXL 更稳 |
| 采样器 | `DPM++ 2M SDE` / `Karras` | 经 `dpmpp_sde` 验证达 **A 级效果**，优于旧 `DPM++ 2M Karras` |
| 工作台活版本 | **V6.2026.0828.07**（cobalt blue 配色线） | 本技能旧正文引用 V6.2026.0803 / 0814 已过期，改工作台后须同步 §三 / §四 |
| 统一吸收源 | `references/thermos_prompt_assets_v5.md`（v5.0 单源） | 所有 `zheng10-*` 执行层引用同一份资产，避免提示词漂移 |
| 商务配色 | 墨影 / 月白 / 棠色（已确立） | 主图锚定走 **cobalt blue（钴蓝）** 蓝锚，材质词不直接进正向 |

# 二、核心信念（Core Beliefs）

## 信念1：控制 = 可复现

ComfyUI 的控制能力本质是：把"随机试错的创作"变成"可定义、可复现、可批量的工业生产"。

## 信念2：保温杯必须标准化

保温杯是**标准化产品**，必须：

- 每一个环节参数锁死
- AI 只能在定义范围内生成
- 根本没机会乱改

## 信念3：批量生成是目标

最终目标：

- 100 个 SKU × 10 个场景 = 1000 张图
- 全程无人值守
- 2 小时完成

# 三、LoRA 触发词映射 + 品类闸门

> **当前对接工作台版本：V6.2026.0828.07**（cobalt blue 配色线活版本，2026-09 实测）。
> 历史版本参考：V6.2026.0803.0900（新增「生肖团 · 主图智能识别与自动配置」；0840 加固方案模型 JSON 解析容错；0850 同步守卫；**0900 生成闸门**：`任务生成` 按钮默认禁用，必须「先识别后生成」）。下方映射与工作台 `ST.LORA_TRIGGER_MAP` 逐字一致，是本技能最易过期的部分——**改工作台 LoRA 表后须同步此处**（实测 2026-09：目录 `<COMFYUI_ROOT>/models/loras/product/` 已探测到 9 个 `zodiac_*` 权重）。
> 提示词工程维度（材质×颜色/负向词库/采样参数/场景角度）另见 §四，对接工作台 **V6.2026.0814.0002**（材质词表 / 负向词库 / 采样参数已在 0828.07 吸收并校准）。

## 3.1 为什么需要

- **根因**：早期 jug（大容量运动水壶）经纯 prompt 锚定仍被渲染成杯/瓶（2026-08-01 视觉评审发现）。
- **治本**：训练专属 `duntongjug` LoRA，在 jug 品类**主动注入**触发词，把形态拉向矮胖宽体；比单纯 prompt 锚定稳。
- **副作用防控**：THERMOS 系 7 个 cup 类 LoRA 若在 jug/pot 品类注入触发词，会把 jug 拉回杯形——需品类闸门拦截。

## 3.2 触发词映射表

| LoRA 文件名（`product/` 下） | 触发词（trigger） | 品类（category） | 说明 |
|---|---|---|---|
| `zodiac_duntongjug_sdxl_v1.safetensors` | `duntongjug` | `jug` | 大容量运动水壶专 LoRA，jug 品类须注入 |
| `zodiac_zidanbaocup_sdxl_v1.safetensors` | `zidanbaocup` | `cup` | 子弹头保温杯 |
| `zodiac_kafeibei_sdxl_v1.safetensors` | `kafeibei` | `cup` | 咖啡杯 |
| `zodiac_tantiaogai_sdxl_v1.safetensors` | `tantiaogai` | `cup` | 弹跳盖 |
| `zodiac_baowenshuihu_sdxl_v1.safetensors` | `baowenshuihu` | `cup` | 保温水壶 |
| `zodiac_tishoulvxinghu_sdxl_v1.safetensors` | `tishoulvxinghu` | `cup` | 提手旅行壶 |
| `zodiac_tishoubei_sdxl_v1.safetensors` | `tishoubei` | `cup` | 提手杯 |
| `zodiac_wenxianzhibei_sdxl_v1.safetensors` | `wenxianzhibei` | `cup` | 温现直杯 |
| `zodiac_all8_sdxl_v1.safetensors` | （空） | （空） | 8 套合并总 LoRA，无单一触发词，按需手动指定 token |

工作台内联 JS 字面量（权威源，`ST.LORA_TRIGGER_MAP`）：

```js
LORA_TRIGGER_MAP: {
  'zodiac_duntongjug_sdxl_v1':     { trigger:'duntongjug',     category:'jug' },
  'zodiac_zidanbaocup_sdxl_v1':    { trigger:'zidanbaocup',    category:'cup' },
  'zodiac_kafeibei_sdxl_v1':       { trigger:'kafeibei',       category:'cup' },
  'zodiac_tantiaogai_sdxl_v1':     { trigger:'tantiaogai',     category:'cup' },
  'zodiac_baowenshuihu_sdxl_v1':   { trigger:'baowenshuihu',   category:'cup' },
  'zodiac_tishoulvxinghu_sdxl_v1': { trigger:'tishoulvxinghu', category:'cup' },
  'zodiac_tishoubei_sdxl_v1':      { trigger:'tishoubei',      category:'cup' },
  'zodiac_wenxianzhibei_sdxl_v1':  { trigger:'wenxianzhibei',  category:'cup' },
  'zodiac_all8_sdxl_v1':           { trigger:'',               category:'' }
}
```

## 3.3 品类闸门规则（agent 必守）

设当前产品品类为 `_trigType`（由 `detectProductType(name)` 判定：`jug`=宽短带侧柄大容量 / `pot`=带柄壶 / `cup`=细长保温杯），选中 LoRA 品类为 `_loraCat`：

1. **注入条件**：仅当 `_loraCat && _trigType && _loraCat === _trigType` 时才把触发词注入 positive prompt。
2. **cup 类 LoRA 在 jug/pot 禁用**：7 个 THERMOS 系 cup LoRA 在 jug/pot 品类**不得注入**触发词（防把 jug 拉回杯形）。
3. **jug 类 LoRA 在 jug 必注入**：`duntongjug` 在 jug 品类**必须注入**，将形态拉向矮胖宽体，根治「jug 被渲染成杯/瓶」。
4. **双向错配拦截**：`_loraCat !== _trigType` 即触发 `🚫 品类错配，已禁用触发词注入` 警告并跳过注入。
5. **提交前最终闸门**（工作台 L~4348）：jug 品类词级清洗 `THERMOS→JUG` / `slim→wide-body` / `500ml→1800ml` / `flask|tumbler|bottle→jug`。

## 3.4 权重位置与探测

- 扫描点（ComfyUI `LoraLoader`）：`<COMFYUI_ROOT>/models/loras/product/`
- 工作台启动经 `/object_info/LoraLoader` 拉 `lora_name[0]` 列表填入下拉框（`product/` 优先置顶）。
- 2026-08-02 复核：该目录 9 个 `zodiac_*` 权重均被探测到（合计 18 个含 epoch5 检查点）。

## 3.5 agent 层使用纪律

- 经工作台生图前，**先读本技能 §3.2 选对 LoRA + 触发词**，再决定品类。
- **严禁**绕过品类闸门手动硬塞 THERMOS 系触发词到 jug/pot 品类——会 reintroduce jug 漂移。
- jug 任务优先用 `duntongjug`；cup 任务用对应杯型 LoRA；要通用融合再用 `all8`（无触发词，手动 token）。
- 触发词均为**拼音专属 token**，刻意避开工作台英文 cup prompt，勿擅自改回英文（会与 `THERMOS` 锚点冲突）。

## 3.6 生肖团 · 主图智能识别与自动配置（V6.2026.0803.0850）

工作台现已内置「🐭 鼠」自动配置：上传主图后，若产品名为空或默认值「保温杯变款」，自动调用 qwen3-vl:8b 识别主图品类，并一键设置产品名、启用 LoRA、选择对应 LoRA、填充触发词、设置 refShape。

> **V6.2026.0803.0840 加固**：`runSchemeAnalysis` 返回的 JSON 若含 trailing comma、模型截断、非标引号或未转义换行，`_parseAnalysisJSON` 会自动修复；即使完全无法解析，也会正则兜底抽取出 `product_type` / `body_structure` / `constraint_prompt` 等关键字段，避免方案分析直接失败导致生图链断裂。

> **V6.2026.0803.0850 同步守卫**：`onUploadMain` 中的自动配置原是 `setTimeout(...,800)` 异步触发，用户上传主图后若立刻点生成，会导致 `generateSchemesData` 仍读到旧产品名「保温杯变款」。0850 在 `startGenerate` 和 `preGenerateCheck`（任务生成入口）增加强制同步守卫：产品名仍为默认值且已上传主图时，先 `await autoConfigureFromMainImage(true)` 完成再生成。

### 自动配置映射（agent 须知）

| 识别品类 | 产品名 | 自动选择 LoRA | 触发词 | refShape |
|---|---|---|---|---|
| `jug` | 大容量运动水壶 | `zodiac_duntongjug_sdxl_v1` | `duntongjug` | `round` |
| `pot` | 保温壶 | `zodiac_baowenshuihu_sdxl_v1` | `baowenshuihu` | `round` |
| `cup` | 商务保温杯 | `zodiac_zidanbaocup_sdxl_v1` | `zidanbaocup` | `tapered` |

### agent 配合纪律

- **需求/协调**：接收 jug 任务时，先确认用户已上传主图，并检查工作台是否已自动配置为 `duntongjug`；若未自动，提醒用户点击「🐭 鼠·生肖识别」按钮或手动填写「大容量运动水壶」。
- **生图核心/ 设计调整**：出图前必须核对 `ST.loraName` 包含对应 zodiac LoRA、`ST.loraTrigger` 为拼音触发词；禁止在 jug 任务中使用 cup 类 LoRA。
- **风格参考**：为 jug 提供风格参考时，优先给出「户外机能/运动水壶/吨吨桶」风格图，避免给细长保温杯参考图造成形态冲突。
- **评审**：jug 出图验收时，除 rubric 外额外检查形态锁：宽体、侧柄/提手、矮胖轮廓；若仍被渲染成杯/瓶，立即打回并要求确认 LoRA 为 `duntongjug`。

## 3.7 生成闸门：先识别，后生成任务（V6.2026.0803.0900）

工作台 `任务生成` 按钮**默认禁用**，满足以下任一条件才解锁：

- **主图识别完成**：上传主图后，`autoConfigureFromMainImage` 执行完（`ST.mainImageRecognized=true`）。
- **文字确认完成**：在 ✍️文字生图 输入需求后，点「✅ 确认识别」(`confirmText2Img`)，识别完（`ST.textConfirmed=true`）。

配套 UI：`enqueueTasks` 顶部有防御性拦截（按钮 disabled 仍被程序调用时仍拦），页面加载即锁定并提示 `🔒 请先完成识别…`；文本框改动会令「确认」状态失效（需重确认）；「🔆 优化强化提示词」(`optimizeTextPrompt`) 把原始需求润色为精准英文 constraint_prompt 写回文本框（不解锁，需再点确认）。

### agent 配合纪律（新增）
- 经工作台驱动生图前，**必须先完成一次识别**：要么上传主图等「鼠·自动配置完成」，要么在文字生图点「✅ 确认识别」。否则 `任务生成` 被闸门拦截，不应尝试绕过。
- 文字描述 jug 时，点「确认识别」会按 §3.6 映射自动启用 `duntongjug`（与鼠一致），无需手动干预。
- 不得在未识别状态下直接调用 `enqueueTasks`——那是用户铁律「先识别，后生成任务」。

---

# 四、提示词工程（Prompt Engineering for Thermos）

> **新增于 v2.2.0（2026-08-14）**：把猴哥提供的 29 个英文提示词参考文件 + 《AI 提示词知识库》（中文 JSON + 500mL 石墨黑金标准长提示词）提炼固化，解决此前出图「塑料感 / 黑剪影 / 边缘融背景 / 文字幻觉」等质量问题。详细词表/参数见 `references/` 下 6 个素材文件。
>
> 对接工作台版本：**V6.2026.0814.0002**（已精选吸收材质词表 + 负向词库 + 采样参数对齐 + 黑材质精度）。

## 4.1 核心原则（agent 必守）

1. **CLIP 只认英文**：所有提示词必须英文，中文直灌 = 出图失控（见 `prompt_engineering_rules.md` §一）。
2. **颜色锁蓝锚约束**：工作台 `buildBasePrompt` 强制把正向染蓝 cobalt。材质/颜色词**不能直接进正向**——走三条安全通道：
   - 材质/质感/纹理（不含颜色信号）→ 正向 `material` 字段
   - 各配色线防缺陷 → `COLOR_LINES[].desc`
   - 颜色专属负面 → `NEG_WORDS`
3. **SDXL 无否定语义**：软概念放负向并加权 `(concept:1.x)`。
4. **参考图 IPAdapter 必须 CLEAN 无字**（#519 铁律）：带水印=生成图必出字。

## 4.2 材质 × 颜色词表（治塑料感/黑剪影/边缘融白底）

| 配色 | 正向材质词（进 `material`/`desc`） | 专属负面（进 `NEG_WORDS`） |
|------|-----------------------------------|----------------------------|
| 银/不锈钢 | `brushed stainless steel, fine vertical brushed metal texture, subtle anisotropic reflections, no crushed blacks` | `plastic look, rubbery metal, chrome mirror finish` |
| 白 | `satin white powder-coated, light gray edge separation`（防融白底） | `no edge bleed, visible outline required` |
| 黑/石墨黑 | `fine-textured matte black powder coating, graphite black #252729, 8-12 GU low gloss, controlled narrow vertical highlights, no crushed blacks` | `crushed blacks, mirror black finish, uneven coating` |
| **cobalt blue（钴蓝·主图蓝锚）** | `cobalt blue, deep saturated blue, matte powder-coated, premium anodized look` | `navy, cyan, desaturated blue, color bleed, purple shift` |
| **墨影（商务深灰）** | `ink shadow dark grey, matte graphite, subtle vertical highlights, 8-12 GU low gloss` | `crushed blacks, mirror finish, uneven coating` |
| **月白（商务浅色）** | `moon white, soft off-white satin, light gray edge separation` | `no edge bleed, pure white blowout, visible outline required` |
| **棠色（商务暖调/胭脂）** | `tang warm reddish tone, soft warm powder-coated, muted` | `oversaturated red, orange shift, neon` |

> **配色线对齐（2026-09 修正）**：`cobalt blue` 是主图蓝锚，所有单品主色锁定钴蓝；`墨影 / 月白 / 棠色` 为已确立的三款商务配色，出图时按订单选配色线，材质词经 `material`/`desc` 安全通道注入，**严禁把颜色信号直灌正向**（会破坏蓝锚）。完整词表见 `references/material_color_prompt.md`，单源见 `references/thermos_prompt_assets_v5.md`。

> 完整词表见 `references/material_color_prompt.md`；石墨黑金标准长提示词见 `references/golden_prompt_graphite_black.md`。

## 4.3 结构维度防缺陷（提手/吸管/杯把）

- 提手：`missing handle, broken handle, floating handle, asymmetric handle` + **#519 加权** `(text on handle:2.2)`、`(text on handle:2.0)`、`(letters on handle:1.8)`、`(words on handle:1.8)`、`(watermark on handle:1.5)`、`(logo text on handle:1.5)` 共 6 项（提手高光曲面固有字母幻觉）。
  > **#519 避坑（2026-09 实测）**：6 项负向加权后 SDXL 仍有 **10-20% 复发**率，属未根治项。根治依赖 **v5.0 统一吸收策略**——所有提示词经单源 `references/thermos_prompt_assets_v5.md` 生成，鸡职能评审命中文字即打回并回写该单源，避免各执行层漂移。不要只在单能力里改负向词。
- 吸管：`missing straw, detached straw, wrong straw position`。
- 杯把：`missing ear handle, deformed ear handle, handle not connected`。
> 完整库见 `references/negative_prompt_library.md`（含 9 类系统负向 + #519 铁律）。

## 4.4 角度 / 场景维度

- 45° 主图：`three-quarter view, ~15° horizontal rotation, hero angle`。
- 电商白底：柔光箱主光前左 + 右窄轮廓光 + 柔和接触阴影（已融入 `jug scene`）。
- 杯盖分离 / 多色排列 / 透明抠图：属多图模板，需工作台 UI 扩展（规划项）。
> 完整库见 `references/scene_angle_library.md`。

## 4.5 采样参数（SDXL 写实）

| 参数 | 值 |
|------|----|
| Sampler / Scheduler | `DPM++ 2M SDE` / `Karras`（工作台已一致） |
| Steps | **28-36**（现 32；勿过度采样 85） |
| CFG | **4.5-6.5**（现 6.5） |
| Base | `sd_xl_base_1.0` |
| IPAdapter / Canny / Depth | 0.65-0.85 / 0.45-0.70 / 0.40-0.65 |
| loraStrength（jug） | **0.52**（勿 >0.75） |

> 完整表见 `references/sampling_params.md`。

## 4.6 agent 使用纪律（提示词维度）

- 经工作台生图前，按 §4.2 选材质词、按 §4.3 叠加结构负面词、按 §4.5 确认采样参数。
- **严禁**把中文提示词直灌、把颜色信号进正向破坏蓝锚、过度采样 steps>40。
- 升级工作台默认 prompt 时，以 `golden_prompt_graphite_black.md` 为质感上限对照，以 `prompt_engineering_rules.md` 为纪律总纲。
- 本技能 references/ 是**权威参考源**，改工作台提示词相关代码后须同步此处（与 §三 LoRA 表同理，易过期）。

---

# 五、⚡ S级硬数据速查（2026-09-09 融合 · 110条提纯）

> **来源**：`<本地资源路径>`（从 ~308 篇文档 + 344 结构设计规范文件提纯）。
> **用法**：agent（羊/猴/猪/鸡）驱动工作台生图前，**必须按材质/场景查本表取值**，不得凭记忆猜参数。
> **冲突仲裁**：本章数值与 §4.5 不一致时，**以 §4.5 为准**（§4.5 是猴哥实测校准值，本章是文档提炼值）。

## 5.1 ControlNet 权重速查（S-01~S-05, S-50~S-57）

| 控制类型 | 杯盖 | 杯身 | 通用推荐 | 致命红线 |
|---|---|---|---|---|
| **Canny**（轮廓） | **0.8** | **0.7** | 0.7-1.0 | 低阈值100-150 / 高阈值200-300 |
| **Depth**（3D结构） | — | **0.6** | 0.5-1.0 | **必须 ≤0.7**！>0.7 必致「杯身变扁」(S-70) |
| **Normal**（法线） | — | **0.5** | 0.5 | 材质纹理法线方向 |
| **Softedge**（软边） | — | **0.5** | 0.5 | 材质边缘软化 |
| **Lineart**（线稿） | — | — | 0.6-0.8 | 替代 Canny 做细腻线稿/Logo |
| **Tile**（平铺放大） | — | — | — | 高清 Upscale 专用 |
| **IP-Adapter**（参考图锁定） | — | — | **0.8** | 产品特征/背景分离锁定 |

> **多组叠加总权重 ≤2.0**（S-51），超过必崩。
> **分阶段介入**：StartAtStep=0.05 / EndAtStep=0.8（S-19）。

## 5.2 采样参数速查（S-06~S-19）

| 参数 | 标准值 | 高精度/金属 | 电商快出 | 备注 |
|---|---|---|---|---|
| **Steps** | **25** | **35-40**（金属细节） | 20-30 | 勿 >40（过采样崩） |
| **CFG** | **7.0** | — | SDXL: **3.5-7.5** | 动态衰减 7→5 降饱和(S-11) |
| **Sampler** | DPM++ 2M Karras | **DPM++ SDE Karras**（金属高光最佳） | — | 产品摄影首选 |
| **分辨率 SDXL** | **1024×1024** | — | — | SD1.5 安全域 768×768 |
| **Hires Fix** | 0.4-0.55 | — | — | 高清修复重绘幅度 |
| **CLIP Skip** | **1** | — | — | 真实感产品专用 |
| **VAE** | vae-ft-mse-840000 | SD3.5 用专属 VAE 防偏黄 | — | 默认优化 |

## 5.3 材质渲染配方（S-33~S-37）★ 保温杯核心

| 材质 | ControlNet | LoRA 权重 | 正向提示词关键词 |
|---|---|---|---|
| **抛光不锈钢** | Canny=0.7 + Depth=0.6 | metal=**0.85** + product=**0.7** | `(polished stainless steel:1.4),anisotropic specular highlight,highly reflective` |
| **磨砂烤漆** | Canny=0.7 + Depth=0.6 | metal=**0.6** + product=**0.7** | `matte powder-coated,fine texture,no glare,soft-touch` |
| **拉丝金属** | Canny=**0.8** | — | `directional satin finish,320-grit brushed pattern` |

> **PBR 五通道贴图**（S-36）：Albedo + Normal + Roughness + Metallic + Height（CHORD 模型生成）。
> **三光源打光**（S-37）：光源角 30-360° / 强度 0.1-5.0 / 阴影 1-10 级分层。

## 5.4 图生图 / 换场景 denoise 速查（S-38~S-42）

| 场景 | denoise / strength |
|---|---|
| 轻微调整 | **0.3** |
| 中等调整 | **0.5** |
| 风格大转换 | **0.6-0.8** |
| **换场景保产品形态** | Strength **0.45**（改背景不变产品） |
| 局部重绘（FaceDetailer） | 0.6-0.8 |

## 5.5 ⛔ 出图前必查：致命错误黑名单（S-66~S-70）★ 鸡职能硬性否决项

| # | 缺陷 | 判定 | 防控手段 |
|---|---|---|---|
| **S-66** | **螺纹缺失** | 🔴 致命 | 负向排除 `((tall thin bottle))`；AI 不理解功能逻辑 |
| **S-67** | **提手穿模 / 内胆结构错 / 盖子无法开启** | 🔴 致命 | 结构性错误，必须打回 |
| **S-68** | **文字/Logo 乱码** | 🔴★★★★★最难避免 | 用 **AnyText + ByT5 编码节点**规避 |
| **S-69** | **材质交界模糊 / 涂层过度完美 / 反射虚假** | 🟠 严重 | ControlNet + 具体提示词修正 |
| **S-70** | **杯身变扁** | 🟠 严重 | **Depth 权重必须 ≤0.7** |

> **鸡职能评审纪律**：出图验收时逐条对照此表，命中任一 🔴 项 = **硬性不合格，直接打回**，不得放行。

## 5.6 LoRA 训练参数速查（S-43~S-49）

| 参数 | 值 | 说明 |
|---|---|---|
| 训练数据量 | **98 张多角度实拍**（2026-09 已备） / 文档建议 20-40 张起 | 1024×1024+，干净白背景；图少则提高 epoch、加 augmentation |
| **学习率 lr** | **1e-4**（SD 系列）/ **1e-6**（Flux） | 模型不同不可混用；SDXL 用 1e-4 |
| **rank** | **8**（轻量）/ **16-32**（风格强） | 低秩分解维度；保温杯风格 rank 8 已够 |
| **alpha** | **16**（= 2×rank） | 缩放因子，rank:alpha ≈ 1:2 |
| **max_train_steps** | **1000 步 / 50 轮**（按图量缩放） | 98 图建议 2000-3000 步 + 高 epoch |
| **batch_size** | **2-4 + gradient accumulation**（非 64） | ⚠️ 原表 `64` 对 16GB 卡必 OOM；RTX 5080 16GB 实测安全 batch=2-4，靠累加逼近大 batch 效果 |

> **训练环境对齐（2026-09 实测，避坑）**：本机 **RTX 5080 16GB（ASUS ProArt，Blackwell sm_120）**，匹配 **CUDA 130 / PyTorch 2.10+**，工具链 **OneTrainer v1.10 + SDXL Base 1.0**（kohya_ss 经 ZIP 下载安装、非 Git 仓库）。`batch_size=64` 系文档提炼值，在 16GB 卡上会直接 OOM——实际用 2-4 + gradient accumulation。 abstinence：Flux 底模走 `lr=1e-6` 且需 T5 编码器，勿与 SDXL 混用。

## 5.7 推荐模型选型（S-20~S-26）

| 层级 | 模型 | 适用场景 |
|---|---|---|
| **Tier1** | Absolute Reality v1.6 | 金属纹理优秀，首推 |
| **Tier1** | epiC Realism xL | 高精度真实感产品图 |
| **Tier1** | MajicMix Realistic v6 | 通用优质写实 |
| **Tier2** | SDXL Juggernaut XL v9 | SDXL 生态通用底座 |
| **产品首选** | realisticVisionV60B1_v51HyperVAE (4GB) | 4GB 显存 / 产品摄影 |
| **低显存** | SD3.5 FP8 | 量化模型 |
| **Flux** | Flux T5（**非 CLIP** 编码器） | Flux 底模专用 |

## 5.8 电商主图批量 SOP（S-58~S-62）

| 环节 | 参数 / 工具 |
|---|---|
| SKU 遍历 | Batch Input 节点 + CSV 模板；每 SKU 多 seed 出 **3-5 张备选** |
| 文件归类 | `filename_prefix = {sku}_seed{N}` 分类保存 |
| 去背工具 | RMBG（通用）/ **BIRefNet（商用首选）** |
| API 调用 | `POST http://127.0.0.1:8188/prompt`（JSON 含 class_type + inputs） |
| **效率基准** | AI **3分钟/张** vs 人工 25分钟/张；返修率降低 **72%**；单张成本 **<1元** |

## 5.9 低显存优化（S-63~S-65）

| 策略 | 参数 | 代价 |
|---|---|---|
| `--lowvram` 启动 | 显存降 **50-70%** | 速度降 20-30% |
| Tiled VAE | `tile_size=256` | 避免 OOM |
| GGUF 量化 | **4bit**（体积 1/4） | 质量损失 <5%，肉眼难辨；显存 ≥4GB 可跑 |

## 5.10 A级方法论索引（详见原清单）

- **提示词结构模板**（A-09）：`[质量前缀] → [主体描述] → [细节描述] → [场景/光线] → [风格后缀]`
- **括号权重语法**（A-10）：`(keyword:1.3)` 显式提权；`((keyword:1.5))` 双重提权
- **终极负向词库**（A-11）：`worst quality,low quality,blurry,deformed,bad proportions,extra limbs,((tall thin bottle)),small lid,plastic toy,fingerprint marks,watermark,text,logo`
- **自动评估筛选**（A-23）：OpenCV 杯身圆度 >0.95 + CLIP 语义匹配 >0.9 + **CIE Lab 色差 ΔE<2**，不符合自动生成
- **工具选型结论**（A-02）：ControlNet+RealisticVision（准确 **95%**）> Img2Img（85%）> Text2Img（60%）

## 5.11 B级资源索引（详见原清单）

- 模型社区：Civitai / HuggingFace / Liblib.ai（中文）
- 工作流库：comfyworkflows.com / github.com/comfyanonymous/ComfyUI_examples
- 结构设计规范：344 文件（12 大领域：塑胶模具/螺丝/钣金/按键/材料/安规/检验等）
- 巨型手册待精读：6 本 >50MB（机械设计大典 98.5M / 化工设备手册 98.2M / 产品设计教程 91.7M）

### [HD-R2] CN选型·最佳参数组·材质光影（2026-09-09 补零覆盖 A-18 + 新增 S-71~S-79）

**A-18 ComfyUI 三大核心 ControlNet 对比**
| 类型 | 保什么 | 适用 |
|------|--------|------|
| Depth | 空间/3D 透视 | 构图保持、杯身立体感 |
| Canny | 轮廓/线条结构 | 杯型边缘锁定（**主力**） |
| OpenPose | 姿态/朝向 | 人体或产品朝向控制 |

⚠️ **多组叠加总权重 ≤ 2.0**，超出会导致结构崩坏或画面糊化。

**S-71 最佳 ControlNet 参数组（来自 AI渲染优化成果索引，已实测验证）**
```
模型:      realisticVisionV60B1_v51HyperVAE
ControlNet: canny, weight 0.75
降噪:      0.5
Steps:     28-36
CFG:       4.5-6.5
采样器:    DPM++ 2M Karras
```

> ⚠️ **参数以《生图工程参数速查表》为准**（中央真源），以上为基础参考值。

**S-74 三种生图方法效果对比基准（重要：方法选型的量化依据）**
| 方法 | 准确率 | 结构 | 色彩 | Logo |
|------|--------|------|------|------|
| Text2Img | **60%** | ⚠️ 有错误 | 75% | ❌ 乱码 |
| Img2Img | 85% | ✅ 基本正确 | 80% | ⚠️ 部分 |
| **ControlNet** | **95%** | ✅ 正确 | **90%** | ✅ 清晰 |

→ 结论：**出货图一律走 ControlNet**，纯 T2I 只用于探索草稿。

**S-75 金属材质三分关键词**
| 材质 | 关键词 |
|------|--------|
| 不锈钢 | `stainless steel, chrome finish, mirror polish, metal texture, reflections, soft highlights` |
| 铝合金 | `anodized aluminum, matte finish, color anodized, subtle texture, premium look` |
| 铜 | `copper material, brushed copper, patina effect, warm tones, metallic reflections` |

**S-76 塑料材质三分关键词**
| 材质 | 关键词 |
|------|--------|
| 磨砂塑料 | `matte plastic, frosted texture, soft touch coating, subtle reflections, premium feel` |
| 透明塑料 | `clear plastic, transparent material, refraction, glass-like, crystal clear, high transparency` |
| 软胶塑料 | `soft touch TPU, rubber coating, grip texture, fingerprint resistant, matte finish` |

**S-77 三点布光**
```
Key light:  主光源，45度角
Fill light: 补光，减少阴影
Rim light:  轮廓光，分离主体
```

**S-79 结构保持配方**：ControlNet Canny + **重绘幅度 0.3-0.4**（保持产品结构不变的标准解）

---

---

---

---

## 📚 资料总线（H 盘资料入口）

> 本技能可读的 H 盘资料已登记在**资料总线**，开工前先查一遍 —— 避免"重复造轮子"和"翻不到料"。

```bash
python <本地资源路径> --role comfyui-thermos
python <本地资源路径> --kw <关键词>      # 元数据层：找「有哪些资料」
python <本地资源路径> --wb             # 工作台可挂载的料
python <本地资源路径> "一句话需求"    # 语义层：在 1.2 万篇业务库正文里找「哪一段」
python <本地资源路径> --role comfyui-thermos "..."  # 限定本角色的资料范围内检索
```

**全量索引**：`<本地资源路径>` ｜ **清单**：`<本地资源路径>`

### ✅ 本角色开工必读（硬清单 · 先读再用）

| 文件 | 路径 | 为什么读 |
|---|---|---|
| ✅ 保温杯设计检查项·总表 V1.0 | `<本地资源路径>` | 立项/打样/出图前逐项自查（79 条：合规红线 / 结构 / 弹跳盖卡扣 / 密封 / DFM / 外观 / 专利 / 生图）；**附A 是一票否决清单** |

| 资料 | 路径 | 体量 | 用途 |
|---|---|---|---|
| `asset.cfwf` | `<本地资源路径>` | 1 MB | ✅ 工作流调用 |
| `asset.lora` | `<本地资源路径>` | 1.19 GB | ✅ LoRA 挂载 |
| `prompt.tpl` | `<本地资源路径>` | 61 KB | ✅ 出图提示词直接调用 / 锁定约束条件 |

**硬数据优先**：凡涉及国标限值、材料参数、专利红线、竞品价格，**必须以本总线登记的真实文件为准**，不得凭记忆作答。

**出图/交付**：32 个标准提示词模板见 `<本地资源路径>`（结构化索引 `prompt_templates.json`，含分类/变量/正文/示例）。

> 两个入口分工：`lookup.py` 查**目录元数据**（有哪些资料、多大、谁能用）；`core_lookup.py` 查**内容语义**（哪份文件的哪一段讲了这件事）。

<!-- 资料总线区块结束 -->

## 杯类专用词汇库（A-13）

> 来源：《可融入能力硬数据清单.md》A-13（`已读精华_全量.md` #2,5 比例提示词）。补齐 `_audit_harddata.cjs` 零覆盖。

| 词条 | 用途 |
|------|------|
| `squat` | 短胖杯型 |
| `compact squat design, height:width=1:1` | 紧凑矮胖造型，高宽比 1:1 |
| `lid diameter 1.3× body` | 杯盖直径 = 杯身 1.3 倍（盖宽于身） |
| `large push-button flip lid` | 大按键弹跳盖 |
| `vacuum insulated double-wall` | 真空双层不锈钢结构 |

> ⚠️ 本表只描述**形状与结构**，不含触发词黑名单（marble / veins / museum / vintage / 数量词 / 道具 / 结构触发词）；与工作台「比例提示词」段落配合使用。
