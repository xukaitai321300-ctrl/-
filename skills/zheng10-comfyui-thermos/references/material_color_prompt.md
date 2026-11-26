# 保温杯材质 × 颜色 英文提示词词表

**来源**：`<本地资源路径>` `<本地资源路径>` `<本地资源路径>` + `<本地资源路径> 提示词知识库.txt`（500mL 石墨黑金标准）
**作者**：猴哥 · 经生肖团 AI 提炼
**用途**：agent 驱动「保温杯变款工作台」生图时，按配色线选词填入 `productPresets[jug].material` / `COLOR_LINES[].desc` 材质层。

> ⚠️ **铁律兼容（必读）**：工作台有「三重蓝锚」——`buildBasePrompt` 最终会强制把正向 prompt 染成 cobalt 蓝（颜色锁）。因此**颜色信号（white/silver/black 等）不能直接进正向 prompt**，否则破坏颜色锁。
> 本词表的用法 = ① 材质/质感/纹理词可进正向 `material` 字段（不含颜色信号）；② 各配色线的防缺陷描述进 `COLOR_LINES[].desc`（工作台原有设计，desc 会进 prompt）；③ 颜色专属负面词进 `NEG_WORDS`（见 negative_prompt_library.md）。

---

## 一、银色（Silver / 不锈钢拉丝）— 治「塑料感」主刀

| 维度 | 英文词 |
|------|--------|
| 主体材质 | `brushed silver`, `brushed stainless steel`, `cold-rolled stainless steel surface` |
| 纹理 | `fine vertical brushed metal texture`, `visible grain texture`, `subtle anisotropic reflections`（各向异性反射，金属感核心） |
| 防缺陷 | `visible surface detail`, `no crushed blacks`, `no mirror reflection`（拉丝≠镜面） |

**jug 默认材质写法（工作台现状）**：
```
brushed stainless steel with fine vertical brushed metal texture and visible grain,
metallic cold-rolled steel surface, subtle anisotropic reflections,
visible surface detail, no crushed blacks
```

---

## 二、白色（White / 哑光/缎面）— 防边缘融背景

| 维度 | 英文词 |
|------|--------|
| 主体材质 | `satin white powder-coated`, `matte white enamel finish` |
| 防融白底 | `light gray edge separation`（浅灰描边，把白杯从白底里切出来，防边缘消失） |
| 灯光 | `soft diffused studio lighting`, `clean white e-commerce background` |

**说明**：白色杯在白底上最易出现「边缘融背景、看不出轮廓」——`light gray edge separation` 是参考库专门为此加的护城河词。

---

## 三、黑色（Black / 哑光粉末涂层）— 治「黑剪影/黑塑料」

| 维度 | 英文词 |
|------|--------|
| 主体材质 | `fine-textured matte black powder coating`, `graphite black finish` |
| 工业精度（石墨黑） | `graphite black #252729`, `8-12 GU low gloss`（光泽度 8-12，哑光不镜面） |
| 防黑剪影 | `visible surface detail`, `no crushed blacks`, `controlled narrow vertical highlights`（细窄纵向高光，不镜面但保留立体感） |

**石墨黑金标准片段（来自 AI 提示词知识库）**：
```
graphite black matte powder-coated body (#252729, 8-12 GU low gloss),
fine narrow vertical highlight band on left edge, no mirror reflection,
visible micro-texture on surface, soft compact contact shadow
```

**E 线（国潮深蓝/黑）desc 写法**：`深色部位哑光粉末涂层质感、细窄纵向高光不镜面`
**G 线（电竞近黑）desc 写法**：`近黑区域哑光粉末涂层、受控窄高光不镜面反射`

---

## 四、补充材质（按品类/风格扩展）

| 品类 | 英文材质词 |
|------|-----------|
| 商务款 | `brushed stainless steel + deep blue panel, matte finish`（拉丝+深蓝拼接，哑光） |
| 时尚款 | `satin finish with localized glossy accent strip`（亮面改哑光+局部亮面装饰条，防刮花） |
| 运动款 | `matte powder-coated, rugged textured grip`（降饱和、磨砂、防滑纹理） |
| 钛内胆 | 仅允许灰度系 hex（钛上色铁律，禁彩色） |

---

## 五、错误写法（对照，避免回潮）

| ❌ 过时/错误 | ✅ 修正 |
|-------------|--------|
| `powder-coated stainless steel`（喷粉≈塑料感） | `brushed stainless steel with visible grain`（拉丝金属） |
| `chrome mirror finish`（镜面塑料） | `subtle anisotropic reflections`（可控各向异性） |
| `outdoor adventure blurred background`（光影不可控） | `clean white studio, softbox key light`（棚拍锐焦） |
| 中文材质词直灌 | 必须英文（CLIP 中文弱） |
