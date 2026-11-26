# 保温杯生图 负向提示词库（Negative Prompt Library）

**来源**：`<本地资源路径> 负面提示词.txt` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径> 提示词知识库.txt`（9 类系统负向词）
**作者**：猴哥 · 经生肖团 AI 提炼

> ⚠️ **铁律兼容**：本库是工作台 `NEG_WORDS` 数组 + 各颜色/结构专属负面词的**权威参考源**。SDXL CLIP **无否定语义**——正向只写肯定描述，软概念（strap / soft band / fabric 等）必须放负向并加权。

---

## 一、精简版（日常默认，覆盖 80% 问题）

```
low quality, lowres, blurry, soft, out of focus, deformed, distorted,
extra handles, missing handle, wrong proportions, asymmetry,
text, logo, watermark, signature, letters, numbers,
plastic look, rubbery metal, toy-like,
chrome mirror finish, room reflection,
crushed blacks, invisible product edge,
mutated fingers, extra limbs
```

---

## 二、结构专属负面词（按出图结构叠加）

**提手（side handle / loop）**：
```
missing handle, broken handle, deformed handle, floating handle,
handle not attached, asymmetric handle, handle too small, handle too large
```

**吸管（straw）**：
```
missing straw, detached straw, wrong straw position,
straw through lid incorrectly, floating straw, bent straw
```

**杯把（ear handle）**：
```
missing ear handle, deformed ear handle, floating ear handle,
handle not connected, broken ear handle
```

> 🔴 **#519 铁律（提手文字幻觉根因）**：SDXL 在提手高光曲面有固有字母幻觉（非参考图污染）。jug 负向必须追加加权：
> `(text on handle:2.2) (letters on handle:2.2) (words on handle:2.2) (typography on handle:2.2) (numbers on handle:2.2) (signature on handle:2.2)`
> 参考图 IPAdapter 必须 **CLEAN 无字无水印**（带水印=生成图必出字，负向压不住）。

---

## 三、颜色专属负面词（按配色线叠加）

**白色线（B）防融白底**：
```
no edge bleed, no white-on-white消失, visible outline required
```
（对应正向 `light gray edge separation` 的互补防护）

**黑色线（E/G）防黑剪影**：
```
crushed blacks, black silhouette, no detail in shadow,
mirror black finish, uneven coating, noisy dark surface
```

**银色线防塑料感**：
```
plastic look, rubbery metal, toy material, chrome mirror finish
```

---

## 四、角度/场景专属负面词

**45° 主图**：`extreme angle, top-down view, bottom-up view, perspective distortion`
**杯盖分离**：`cap merged with body, floating cap, wrong cap scale`
**多色排列**：`inconsistent product shape across variants, mismatched proportions`
**透明抠图**：`background, shadow, reflection, environment`

---

## 五、9 类系统负向词（来自 AI 提示词知识库，中文→英文精选）

| 类 | 英文负面词 |
|----|-----------|
| 结构类 | `deformed body, extra parts, missing parts, floating components` |
| 比例类 | `wrong aspect ratio, too thin, too fat, disproportional` |
| 材质类 | `plastic look, rubbery, toy material, cheap texture` |
| 光影类 | `harsh shadow, overexposed, underexposed, flat lighting` |
| 背景类 | `cluttered background, distracting environment, messy` |
| 人物类 | `person, hand, fingers, face, human` |
| 画质类 | `blurry, lowres, jpeg artifacts, noise, pixelated` |
| 文字类 | `text, logo, watermark, typography, letters, numbers, signature` |
| 颜色类 | `wrong color tint, color cast, oversaturated, faded color` |

---

## 六、工作台集成点（agent 须知）

- 全局负向 → `NEG_WORDS` 数组（工作台内联 JS 字面量），含上述精简版 + #519 提手加权 + 颜色/材质专项。
- 颜色专属负面词 → 已并入 `NEG_WORDS`（V6.2026.0814.0002 精选吸收）。
- **勿**把中文负面词直灌——必须英文（CLIP 中文弱）。
