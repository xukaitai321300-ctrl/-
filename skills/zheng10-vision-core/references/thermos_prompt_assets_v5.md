# 生肖团 v5.0 保温杯出图提示词资产（统一源 / Single Source of Truth）

> ## 📌 版本对齐说明（2026-09-22 加注，内容未改动）
>
> **本文件是活文件，内容有效；仅文件名版本号与当下技能版本存在命名落差。**
>
> | 项 | 值 |
> |---|---|
> | 文件名版本 | `v5` |
> | 当前技能本体版本 | `v7.0 ~ v7.4`（2026-09-18 批量刷新） |
> | 引用方 | **21 个文件 / 29 处**（2026-09-30 全树复核实测；含 10+ 个 `zheng10-*` / `zodiac-*` 技能 SKILL.md、多名 CHANGELOG、1 处资产自引用、1 处 `v5.0_upgrade_report.md`）。※ 2026-09-22 注记「12 文件 / 18 行」已过期，以本次实测为准。**核验方式：必须用 Python `os.walk` 全树扫描——`grep -r` 在本 skills 目录会静默漏报（实测仅报 1 处）** |
> | 引用路径 | `references/thermos_prompt_assets_v5.md` |
>
> **为什么不改名**：文件名被 10 个技能 + 2 个附属文件（共 18 行）硬编码引用，重命名会**立即断链**。本文件承载的仍是**唯一有效的提示词真相源**，`v5` 仅为历史命名。
>
> **回写铁律（不变）**：进化闭环发现的提示词 / 负向词 / 配色词改进，**必须回写本文件**，再由各 `zheng10-*` 技能引用，严禁各技能自建词表。
>
> **版本号收敛（2026-09-22 已决）**：采用**方案①** —— 保持文件名 `_v5` 不变，仅以本注声明与技能本体版本（v7.x）的对齐关系；**不新建 `_v7` 文件、不批量改引用**。理由：本文件承载的是**版本无关的提示词真相源**（材质 / 颜色 / 负向 / 采样 / 铁律），与技能本体版本解耦更合理；改名收益为零而断链风险为 **29 处**（2026-09-30 `os.walk` 全树复核；2026-09-22 原估 18 处）。方案② 正式作废。

---

> 固化自 29 个英文提示词参考库 + AI 提示词知识库（2026-08-14 投喂），并经
> 工作台 `V6.2026.0814.0002` 与执行层技能 `zheng10-comfyui-thermos` v2.2.0 实机验证。
> **本文件是生肖团（zodiac / zheng10）各技能吸收提示词知识的单一真相源**——各技能只放角色相关规则 + 链接，避免多份词表漂移。

---

## 一、材质词表（Material · 正向关键词）

| 材质 | 正向关键词（写进 posPrompt） | 备注 / 防缺陷 |
|---|---|---|
| 银拉丝不锈钢 | `brushed stainless steel, fine vertical brushed, anisotropic reflection` | 防塑料感核心词 |
| 白缎面 | `satin white finish, soft sheen, micro texture` | 哑光防刮花 |
| 黑石墨 | `graphite black #252729, matte powder-coated 8-12GU` | 8-12GU 为光泽单位（Gloss Unit） |
| 保温杯(jug) | `brushed stainless steel` / `matte powder-coated 8-12GU` | 替代旧 plastic 感（jug 塑料感根因=材质词误导） |

⚠️ **材质词不得进入正向抢色**：见第三节「颜色锁蓝锚」铁律。

---

## 二、颜色词表（Color）

- **颜色锁蓝锚（铁律）**：所有配色线（A~G）posPrompt **强制染蓝** `cobalt blue`，蓝锚无条件执行；颜色精度靠各线 `getActiveColorDesc()` 对抗。
- 商务三色（撞色 LOGO 精度要求）：墨影 / 月白 / 棠色。
- 黑材质精度：`graphite black #252729`，8-12GU。
- 白材质精度：`satin white`，防灰剪影（jug 黑剪影根因=材质词缺失 + 场景灯不足）。

---

## 三、负向词库（Negative · 加权）

**通用底词（必带）**：
`plastic texture, low quality, blurry, deformed, asymmetry, extra handle, watermark, text artifact, jpeg artifacts, oversaturated`

**#519 提手文字幻觉铁律（根因=SDXL 在提手高光曲面固有字母幻觉，非参考图污染）**：
负向加权 `(text on handle:2.2)` 共 6 项，且软概念 `strap / soft band / fabric` 全放 negative 加权。

**SDXL CLIP 无否定语义铁律**：正向**只写肯定描述**；soft concept（strap/soft band/fabric）放 negative 加权，不可在正向用否定句式（CLIP 不识别 "no xxx"）。

**防塑料感专项（V6.2026.0822 网络调研升级）**：
- 用写实 SDXL 底座（majicMIX realistic / OnlyRealistic / Realism Engine 系，商用安全·不在 FORBIDDEN_CKPT）替代 sd_xl_base_1.0 的干净塑料先验——**治塑料感最大杠杆**
- 负向加权专打廉价/玩具/亮面塑料：`(glossy cheap plastic toy:2.0),(vinyl doll plastic texture:1.8),(airbrushed waxy finish:1.8),(doll-like plastic sheen:1.8),(overpolished toy plastic:1.7),(overexposed plastic:1.5)`；**硬表面保留 smooth，不误伤哑光拉丝金属**
- CFG ≤ 6.5（>7 过平滑=塑料感主因，调研铁证）；steps 28–36（SDE 采样器需步数收敛保材质）

---

## 四、采样参数（Sampling）

| 参数 | 推荐值 | 反例（曾踩坑） |
|---|---|---|
| 采样器 | `DPM++ 2M SDE Karras` | 非 `Euler a` |
| Steps | **28–36** | 非 85（过度采样无收益） |
| CFG | **4.5–6.5** | 非 8.0 |
| IPAdapter 权重 | 0.5–0.7 | — |
| ControlNet(Canny/Depth) | 0.6–0.8 | — |

**v7 补充（2026-10-13 回流 · 来源：批次 5/7 学习记录）**：
- **ControlNet 引导时机**：不必全程生效——strength 0.6-0.7 / start 0.0 / end 0.8，前 80% 步控结构、后段放手让模型自由细化（strength≈1.0 刚性锁几何但易出描图感/僵硬，严格构图才用高值）。
- **IPAdapter 节点顺序**：`Checkpoint → LoRA → FreeU → IP-Adapter → KSampler`——去噪后期早期交接给 LoRA，参考不全程压满，外观与风格双控不打架。
- **三层身份保持法**：结构 ControlNet（锁杯型轮廓与透视）+ 外观 IPAdapter（锁白底参考图材质）+ 风格 LoRA——三层各管一件事，互不干扰，各自调强度。

⚠️ **IPAdapter 参考图必须 CLEAN 无字无水印**：带水印=生成图必出字，负向压不住。

---

## 五、场景与角度（Scene / Angle）

- **主图**：45° 产品主视图 + 纯白背景（商业棚拍）。
- **8 场景**：纯白棚拍 / 生活方式 / 户外 / 手持 / 杯盖分离 / 多色排列 / 透明抠图 / 细节特写。
- **一款一图**，主视图优先；多色排列用于配色对比；透明抠图用于电商。

---

## 六、出图铁律（Rules · 不可违反）

1. **颜色锁蓝锚**：posPrompt 强制染蓝 `cobalt blue`，材质词不进正向（防色偏）。
2. **#519 提手文字幻觉**：负向加权 `(text on handle:2.2)` ×6，软概念进 negative。
3. **采样器**：`dpmpp_sde` + `karras`，steps 28–36，CFG 4.5–6.5。
4. **IPAdapter 参考图 CLEAN** 无字无水印。
5. **SDXL CLIP 正向只肯定**，软概念进 negative 加权。
6. **双 QA 闸门**：CIELAB ΔE76 + 视觉模型 `qwen3-vl:8b`，缺一不可。
7. **编辑指令动词铁律**（v7 新增）：图生图/编辑一律用 `Change [对象] to [新状态], keep [内容] unchanged` 句式，动词用 change/replace，**禁 transform / redesign / place on**（FLUX Kontext 官方四原则：具体明确 / 分步编辑一次只改一个 / 显式保留不变项 / 动词 change·replace）。
8. **局部修改必须走 Inpaint Crop**（v7 新增）：遮罩外像素 byte-for-byte 不变——整图编辑会重画未被指定的区域，换背景/改局部禁整图重绘（详见第十四节）。

---

## 七、评审闸门（Rubric · 对齐鸡评审）

- 幻觉 / A1 / D2 < 10 分 → **返工**。
- 综合 ≥ **B(70)** 且 D4 ≥ 12 → **通过**。
- 视觉模型结论须带 `vision_model: "qwen3-vl:8b (OLLAMA)"`，缺则产物无效重做。
- **主体还原度 ≥95%**（v7 新增）：白底图以实拍参照生成 3 张选 1 对比，防 AI 私自改款——还原度不达标不出场景图。
- **白底机审两项量化检查**（v7 新增）：200% 缩放查四角 `#FFFFFF` + 色温防偏暖（偏暖/带浅阴影会被平台机审判「背景非纯白」，肉眼见白不算数）。

---

## 八、各技能吸收映射（v5.0 统一吸收落点）

| 技能 | 吸收本资产哪部分 |
|---|---|
| `zodiac-content-analysis` | 全部（提示词增强统一入口） |
| `zheng10-style-migration` | 一/二/三/六（CMF 材质·颜色·负向·铁律） |
| `zheng10-vision-core` | 二/三/七（颜色锁视觉校验·防文字幻觉·评审计闸） |
| `zheng10-standards-analyst` | 六/七（出图质量标准 rubric） |
| `zheng10-skill-optimizer` | 四（生图参数推荐 DPM++2M SDE Karras 28-36 / 4.5-6.5） |
| `zheng10-comfyui-thermos`（执行层） | 全部（v2.2.0 已落 references，本文件为其 zodiac 层镜像源） |

---

## 九、LoRA v2 资产清单（重训根治 · 2026-08-19）

> 旧 v1 根因 = 训练 caption 仅写触发词、小样本过拟合 → 出图细节崩（"喷漆塑料球"）。
> **v2 根治 = 富字幕（captions 写品类+材质+纹理+形态）+ 自动数图重训。**

### 9.1 训练与部署事实
- **训练日期**：2026-08-19（lora-scripts v1.10.0，底座 `sd_xl_base_1.0`，AdamW/bf16/dim32·alpha16）
- **训练结果**：9/9 成功，avr_loss 区间 `0.012–0.023`
- **部署路径**：`<COMFYUI_ROOT>\models\loras\product\zodiac_*_sdxl_v2.safetensors`（9 × ~170MB）
- **激活方式**：工作台 `LORA_TRIGGER_MAP` 引用同名 `_v2` 文件，零改生图代码即吃到新权重
- **ComfyUI 状态**：已重启，0.17.0 就绪，CUDA 正常（`pytorch 2.7.0+cu128`）

### 9.2 9 类触发词 → _v2 文件映射（与工作台 LORA_TRIGGER_MAP 严格对齐）
| LoRA 文件（`product/`） | 触发词 | 品类 | 富字幕材质要点 |
|---|---|---|---|
| `zodiac_duntongjug_sdxl_v2` | `duntongjug`（吨吨桶） | jug | matte powder-coated body, brushed steel collar, wide-body |
| `zodiac_zidanbaocup_sdxl_v2` | `zidanbaocup`（子弹头） | cup | **真拉丝不锈钢** brushed stainless, tapered bullet shape |
| `zodiac_kafeibei_sdxl_v2` | `kafeibei`（咖啡杯） | cup | ceramic-feel matte, handle, double-wall |
| `zodiac_tantiaogai_sdxl_v2` | `tantiaogai`（弹跳盖） | cup | push-button cap, textured chevron grip |
| `zodiac_baowenshuihu_sdxl_v2` | `baowenshuihu`（保温水壶） | pot | large vacuum flask, matte coat, pour spout |
| `zodiac_tishoulvxinghu_sdxl_v2` | `tishoulvxinghu`（提手旅行壶） | pot | travel flask, side strap loop, soft band |
| `zodiac_tishoubei_sdxl_v2` | `tishoubei`（提手杯） | cup | cup with top handle, brushed steel |
| `zodiac_wenxianzhibei_sdxl_v2` | `wenxianzhibei`（温现直杯） | cup | straight wall, digital temp display window |
| `zodiac_all8_sdxl_v2` | （合集，无触发词） | — | 8 类融合 |

### 9.3 工作台引用落点（改名同步已完成 · 2026-08-19）
- `LORA_TRIGGER_MAP`（9 key）→ 全部 `_sdxl_v2`
- 两处品类 map：`jug→zodiac_duntongjug_sdxl_v2` / `pot→zodiac_baowenshuihu_sdxl_v2` / `cup→zodiac_zidanbaocup_sdxl_v2`
- `localStorage` 旧 `_v1` 名自动迁移为 `_v2`（防浏览器缓存失配）
- 工作台版本号：`V6.2026.0815.0024` → 注明 v2 改名后继续保持（活文件 `保温杯变款工作台_MVP.html`）

### 9.4 已知待补（非阻断）
- ⚠️ 小样本类仍需补图重训：`提手杯`(4张) / `温现直杯`(5张) 距 ≥25 张目标差距大
- ⚠️ 出图对拍：v2 部署后首批 4 张 jug 出图仍偏光滑蓝塑、v03 右侧文字伪影(#519)复发 → 细节回升与 #519 抑制仍需用户实拍对拍验证
- Ollama `qwen3-vl:8b` 仅作出图后 QA，不参与 LoRA 加载（串行两段，非协作）

---

## 十、结构化替换词表（Fill-in Vocabulary）

> **吸收来源**：网盘「智能体」目录 → `常用替换词.txt`（猴哥自有资产），2026-09-30 吸收。
> **用途**：模板化拼装 posPrompt 的可替换槽位，替代自由文本描述，降低跑偏率。
> **实证**：吸收前工作台 / 本 SSOT 均为 0 命中（五组槽位全缺失）。

| 槽位 | 可选项（逐条可替换） |
|---|---|
| `[PRODUCT TYPE]` | insulated stainless steel bottle ／ vacuum flask ／ insulated travel tumbler ／ handled thermal mug ／ sports insulated water bottle |
| `[BODY SHAPE]` | slim cylindrical body ／ straight-sided cylindrical body ／ slightly tapered cylindrical body ／ wide-base travel tumbler ／ compact cylindrical body |
| `[SURFACE FINISH]` | fine matte powder-coated finish ／ smooth satin finish ／ fine brushed metal texture ／ subtle textured coating ／ glossy ceramic-like coating |
| `[LID TYPE]` | precision screw lid ／ flush-fitting screw cap ／ flip-top drinking lid ／ integrated straw lid ／ leak-proof push-button lid ／ wide-mouth screw cap |
| `[COLOR]` | matte black ／ ivory white ／ brushed silver ／ forest green ／ navy blue ／ muted red ／ soft pink ／ charcoal gray ／ champagne gold ／ deep wine red（棠色，2026-11-11 商务直杯回写登记，主理人裁决） |

⚠️ **`[COLOR]` 槽位约束**：仅用于非蓝锚线 / 调试场景。正式配色线出图仍受第二节「颜色锁蓝锚」铁律约束（posPrompt 强制染蓝 `cobalt blue`），颜色槽位不得抢占材质词位置。

**v7 补充（2026-10-13 回流）· 母版五固定字段**：每个提示词母版固定 `aspect ratio / style anchor / lighting / mood / brand constraint` 五字段，占位符用 `[BRACKETED]` 或 ALL-CAPS（不用花括号）；母版按类型分册（白底主图 / 场景图 / 促销图 / 详情细节 / 海报），标注适用模型与验证效果，好变体回流入库、每季度淘汰失效词条——与第十一/十二节场景库、构图规范共同构成「可比较、可复用、可淘汰」的模板体系。

---

## 十一、场景 Prompt 库（Scene Library · 白底电商向）

> **吸收来源**：网盘「智能体」目录 6 个场景 txt，2026-09-30 吸收（工作台与 SSOT 均 0 命中）。
> **共同骨架**：`single [product] … isolated on a seamless pure white background … soft diffused studio lighting … soft contact shadow directly below … photorealistic … no props, no text`。
> **统一负向**：沿用第三节 NEG 全套 + 本文件第十三节结构专属负向词。

### 11.1 正视主图（`银色不锈钢保温杯.txt`）
```
single premium stainless steel vacuum flask, front-facing e-commerce product photo, upright and centered,
complete product visible, precise cylindrical geometry, brushed silver stainless steel body,
fine vertical brushed metal texture, accurately fitted metallic screw lid, realistic controlled reflections,
clean highlight strips following the cylindrical shape, isolated on a seamless pure white background,
professional large softbox lighting, balanced front fill light, subtle side rim lighting,
soft natural contact shadow below, neutral color balance, no surrounding objects reflected on the metal,
crisp clean contour, photorealistic commercial product photography, 100mm macro lens look,
deep depth of field, ultra-detailed material, high resolution, no props, no text, no logo
```

### 11.2 45°（3/4 角）主图（`45度角主图.txt`）
```
single insulated stainless steel bottle photographed at a subtle three-quarter front angle,
approximately 15-degree horizontal rotation, camera at product mid-height, upright and centered,
full product visible, accurate cylindrical proportions, matte charcoal gray finish,
lid structure clearly visible without looking down into the bottle, premium realistic materials,
isolated on a seamless pure white background, soft diffused studio lighting, controlled highlight strips,
subtle rim lighting, natural soft contact shadow directly beneath, crisp edges,
high-end e-commerce product photography, 85mm lens, minimal perspective distortion,
deep depth of field, photorealistic, highly detailed, no props, no text
```

### 11.3 杯盖分离展示图（`杯盖分离展示图.txt`）
```
professional e-commerce product photograph of one insulated stainless steel bottle with its matching screw lid
placed neatly beside it, bottle standing upright on the left, lid positioned on the right with its functional
structure clearly visible, exactly two components only, accurate scale and geometry,
matte white powder-coated bottle, clean stainless steel bottle opening, realistic threading details,
isolated on a seamless pure white background, balanced soft studio lighting, subtle contact shadows beneath
both components, clean organized composition, crisp edges, accurate materials, commercial catalog photography,
photorealistic, deep focus, no additional accessories, no text
```

### 11.4 杯身与包装盒组合（`杯身与包装盒组合.txt`）
```
professional e-commerce catalog image of one insulated stainless steel bottle and one matching retail packaging box,
bottle upright in the foreground on the left, packaging box upright slightly behind on the right, both fully visible,
balanced composition, accurate relative scale, matte black bottle with a precision screw lid,
clean unprinted neutral packaging box, isolated on a seamless pure white background, soft diffused studio lighting,
realistic compact contact shadows, crisp edges, true-to-life materials, clean commercial photography,
high resolution, deep focus, no props, no printed text, no logo
```

### 11.5 带杯把保温杯（`带杯把保温杯.txt`）
```
professional white-background e-commerce photograph of one handled insulated travel mug,
direct front view with the handle clearly visible on the right side, upright centered product,
complete mug fully inside the frame, accurate cylindrical stainless steel body,
correctly attached ergonomic handle, proportional lid, matte beige finish, realistic material texture,
clean functional construction, isolated on a seamless pure white background, soft diffused studio light,
gentle rim lighting, natural compact contact shadow underneath, crisp contour, accurate product proportions,
high-end commercial catalog photography, deep focus, photorealistic, no props, no text
```

### 11.6 带提手杯盖（`带提手杯盖.txt`）
```
professional e-commerce product image of a single insulated water bottle with an integrated carry handle lid,
exact front view, bottle upright and centered, full product and complete handle visible,
accurate functional lid construction, handle correctly attached at two connection points, symmetrical body,
matte dark green powder-coated stainless steel, clean manufacturing details,
isolated on a seamless pure white background, soft diffused studio lighting,
subtle rim light defining the dark green silhouette, realistic controlled highlights,
compact soft contact shadow beneath the bottle, crisp product boundaries, accurate proportions,
commercial catalog photography, photorealistic, high resolution, deep focus, no props, no text, no logo
```

### 11.7 带吸管杯盖（`带吸管杯盖.txt`）
```
single insulated tumbler with a flip-up drinking straw lid, front-facing studio product photograph,
standing upright in the center, entire product visible, accurately constructed flip straw mechanism,
straw aligned with the lid, slim cylindrical stainless steel body, matte navy blue finish,
realistic functional seams, isolated on a seamless pure white background, soft commercial studio lighting,
balanced highlights, subtle side rim light, realistic soft contact shadow directly below, clean silhouette,
precise geometry, sharp focus across the whole product, premium e-commerce catalog photography,
photorealistic, highly detailed, no props, no text
```

### 11.8 白底三段断言强化（v7 新增 · 2026-10-13 回流）

> 单句「白色背景」只有一条断言，防不住「灰底 / 背景阴影 / 环境反射」多重漂移。**堆叠 ≥3 条背景断言**，每条针对不同失败模式：

| # | 断言 | 针对失败模式 |
|---|---|---|
| ① | `isolated on a seamless pure white background` | 灰底/环境色渗入 |
| ② | `no shadow on the background` | 背景投影 |
| ③ | `no cast shadows, no reflections on background` | 投射影+地面/台面反射 |

**反光产品特例**：把金属反射写成「产品定义特征」而非缺陷——`linear specular highlight along the curved front edge`（窄长条高光沿杯身曲面边缘），避免模型把不锈钢反光抹成灰蒙或消除。
**机审坑**：平台机审对「看起来白其实不够白」敏感——偏暖、带浅阴影会被判「背景非纯白」；出图后 200% 缩放查四角 `#FFFFFF` + 色温（已并入第七节评审闸门）。

### 11.9 不锈钢保温杯白底示例模板（v7 新增 · Jeff Bullas 实测模板回流）

```
single stainless steel travel flask, centered in the frame,
softbox front lighting with subtle rim light, three-quarter eye-level angle,
seamless white background on a matte white plinth,
crisp metal texture with soft specular highlights and subtle reflections,
photorealistic, high-resolution, realistic soft shadows, minimal artifacts
```

> 与 11.1（正视主图）并存作变体：11.1 偏正面电商构图，本模板偏 3/4 视角 + 展台（plinth）质感，A/B 选用。

---

## 十二、构图硬规范（Composition Spec · 电商主图）

> **吸收来源**：`电商主图构图约束.txt`，2026-09-30 吸收（工作台 / SSOT 均 0 命中）。

| 项 | 规范 |
|---|---|
| 画布 | `1024 × 1024` |
| 产品高度 | 画面高度约 **72% – 82%** |
| 左右留白 | 基本一致 |
| 顶部留白 | > 杯盖高度的 8% |
| 底部 | 保留接触阴影空间 |
| 背景 | 最终后期校正为 `#FFFFFF` |

**正向约束词**（可直接并入 posPrompt）：
`single product only, exact front view, product centered, upright vertical orientation, complete product visible, generous white margin around the product, product occupying approximately 75 percent of the image height, camera aligned with the vertical center of the product, minimal perspective distortion`

---

## 十三、结构专属负向词（Structure-specific Negative）

> **吸收来源**：网盘「智能体」目录 4 个结构负向 txt，2026-09-30 吸收（工作台实测 0 命中）。
> **说明**：均为**结构缺陷描述**（非颜色信号），不触碰「颜色锁蓝锚」；按杯型/场景**选择性追加**到 NEG_WORDS 尾部。

| 分组 | 负向词（逐条） |
|---|---|
| **杯盖分离场景** | extra lids, duplicate bottle, multiple components, exploded view, floating components, cap attached and detached simultaneously, impossible thread, liquid spilling, dirty bottle interior, sharp dangerous edges, random accessories |
| **杯把结构** | two handles, extra handle, handle on both sides, broken handle, floating handle, handle disconnected from body, handle intersecting body, twisted handle, malformed grip, tiny handle, oversized handle, mug without handle |
| **提手结构** | extra handle, double handle, twisted handle, broken handle, floating handle, detached handle, one-sided handle, asymmetrical handle, handle fused into lid, handle intersecting cap, deformed hinge, impossible hinge, oversized handle, tiny handle, missing handle attachment |
| **角度控制** | extreme angle, rear view, side view, top-down view, bird's-eye view, low angle, dramatic perspective, fisheye, wide-angle distortion, excessive rotation, tilted horizon, looking inside bottle |

---

## 十四、编辑 / 图生图保真指令（Edit Fidelity · 2026-10-13 回流）

> **场景**：已有一张产品图，要换背景 / 换色 / 改局部 / 转场景，硬约束「材质零变化、不改款、不重绘」。
> **来源**：FLUX Kontext 官方提示词最佳实践（ComfyUI 官方教程 2026-10-04）+ QuestStudio / MarketPrompter 产品保真模板交叉验证 + Runflow Inpaint Crop 实战（批次 7/8/12/14/16 学习记录）。

### 14.1 Kontext 官方句式（动词铁律）

```
Change [object] to [new state], keep [content] unchanged
Change the background to [new background], keep the subject in the exact same position and pose
```

- ✅ 动词用 **change / replace**；❌ 禁 **transform / redesign / place on**（第三方配方的 "Transform this photo into..." 写法会产品漂移，已按官方句式校正）。
- 四原则：**具体明确 / 分步编辑（一次只改一个）/ 显式保留（明确写「保持哪些不变」）/ 动词 change·replace**。

### 14.2 产品保真指令模板（编辑类模型通用）

```
Keep the original silhouette, proportions, material, color, label wording and logo;
replace only the surrounding background;
do not redraw packaging, invent text, add accessories or change the product
```

### 14.3 局部重绘纪律

- 只写**修改部位**的细节要求 / 结构规范 / 材质光影 + 匹配全局光影；**不重复整体构图 / 氛围 / 场景词**（重复全局词会引发指令冲突）。
- 局部修改必须 **Mask Editor + Inpaint Crop**：遮罩外像素 byte-for-byte 不变；整图编辑会重画未被指定的区域（换背景/改局部禁整图重绘）。
- Seedream 系等效路径：Painter 遮罩 / 框选编辑 / 单图拆 16 图层逐层编辑（换背景/换色不动主体）。
- 编辑时显式 **PRESERVE 声明**：姿势/材质/配色/光线方向逐项列「保持不变」，drift（漂移）是编辑头号失败模式。

---

## 十五、商业合规红线（Compliance · 2026-10-13 回流）

> 出图资产的商业使用边界——上架多渠道前按渠道政策分流素材（批次 10 学习记录）。

1. **国内标识义务**：《人工智能生成合成内容标识办法》（2025-09-01 实施）——AI 图片须**显式标识 + 隐式标识**，商业使用须显著标识；元数据层嵌入不可篡改标识（工具/模型版本/时间/水印）。
2. **版权三条件**：人类主导创作 + 独创性 + 可固定留存。纯「一键出图」**零版权**——提示词、修改记录、时间戳必须留存（维权凭证；本资产配套的定时学习记录 / 判图归档即凭证链）。
3. **亚马逊主图（2026-04 更新）**：主图必须**纯白背景实拍图**，AI 生成内容仅可用于 A+ 页面及副图；详情页保留 1-2 张实拍图；严禁过度美化、图实不符。
4. **欧盟 AI Act（2026-08-02 生效）**：AI 产品图须带技术标记（C2PA 凭证/平台水印）+ 平实语言披露；AI 增强图（换背景/加特征）同样在范围内。
5. **平台协议核查**：免费工具可能规定生成图版权归平台，商用前必须核查《用户协议》；不要移除供应商水印后当可用图。

---

> **v6 增量说明（2026-09-30）**：本文件内容版本从「v5 语义」推进到**含十~十三章的吸收态**；文件名仍保持 `_v5`（回写铁律：**21 文件 / 29 处**硬编码引用，不改名）。
> 吸收源：网盘「智能体」目录（558 条 → 下载 65 个高价值资产 → 对拍工作台/SSOT → 只吸真增量 10 项）。
> 详细稽核过程见 `<架构根目录>\_智能体目录稽核吸收报告.md`。

---

> **v7 增量说明（2026-10-13 · 自进化学习记录回流）**：内容推进到**含十四/十五章 + 四/六/七/十/十一节增量**；文件名仍保持 `_v5`（回写铁律：**46 处硬编码引用指向 C 盘路径**，2026-10-13 os.walk 全树复核，不改名）。
>
> **回流源**：`<本地资源路径>`（16 批 → 去重后只收「可直接用」级）。
>
> **本批落地清单**：
> - 新增第十四节「编辑/图生图保真指令」：Kontext 官方句式（change/replace，禁 transform）+ 产品保真指令模板 + 局部重绘纪律（Inpaint Crop / PRESERVE 声明）
> - 新增第十五节「商业合规红线」：国内 AI 标识 / 版权三条件（提示词与时间戳留存=维权凭证）/ 亚马逊主图实拍 / 欧盟 AI Act
> - 第四节补：ControlNet 引导时机（end 0.8）/ IPAdapter 节点序 / 三层身份保持法
> - 第六节铁律 6→8 条（编辑动词铁律 + Inpaint Crop 铁律）
> - 第七节补：主体还原度 ≥95% / 白底机审两项量化检查（四角 #FFFFFF + 色温）
> - 第十节补：母版五固定字段
> - 第十一节补：11.8 白底三段断言 / 11.9 不锈钢白底示例模板（Jeff Bullas）
>
> **⚠️ 待拍板冲突（未擅改现值）**：
> ① **产品占比**——本文件第十二节现值 **72–82%** vs 学习记录两源 **≥85% / 85–90%**，建议后续拍板统一为 ≥85%（双源一致），改前维持现值；
> ② **文字渲染**——产品主图「无文字」铁律不变；海报/详情页文字场景（<40-45 字符）另册处理，不进主铁律。
>
> **未并入（诚实分级）**：模型/工具动态类（FLUX 3 Image、混元 3.0、NB2.1 定价、ComfyUI 节点更新、Smart ComfyUI Gallery、GPU Optimizer、VRAMCleanup 等）属**模型情报**而非提示词真相源内容，不并入本单源（防单源污染），留学习记录备查。
>
> **双路径实锤（2026-10-13 cp 报 same file + fsutil hardlink list 验证）**：H 盘档案路径与 C 盘运行时路径（46 处引用指向）是**同一物理文件的 hardlink 双路径**（非 junction、非独立副本）——改一处即两处同改，md5 天然一致（回流后双路径 md5 `5a42bc1f…`；回流前基线 `83c5cdd1…`，原件已备份至 `<技能根目录>\06_备份\_pre回流_20261013\`）。
