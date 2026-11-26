# 保温杯生图 角度 / 场景维度库（Scene & Angle Library）

**来源**：`<本地资源路径> 度角主图.txt` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径>` `<本地资源路径> 提示词知识库.txt`（8 场景词典）
**作者**：猴哥 · 经生肖团 AI 提炼

> ⚠️ **当前工作台限制**：jug 默认仅单一 `scene` 字段（白底棚拍），**没有场景选择器 UI**。本库价值已通过两种方式间接吸收（V6.2026.0814.0002）：① 电商白底精确灯光融入 `jug scene`；② 户外/健身/极简海报最在意的防缺陷进 `NEG_WORDS`。若要做独立"场景切换 UI"，属架构级改动，需单独规划。

---

## 一、角度维度

**45° 主图（hero angle）**：
```
three-quarter view, approximately 15° horizontal rotation from front,
hero angle showing both body and cap, professional product photography
```
负面：`extreme angle, top-down, bottom-up, perspective distortion`

**电商主图构图约束**：
- 产品居中、占画面 60-70%
- 主光来自前左（key light front-left）
- 右侧窄轮廓光（narrow rim light on right edge）
- 柔和紧凑接触阴影（soft compact contact shadow）
- 纯白无缝背景（pure white seamless background）

---

## 二、场景维度（8 类词典精选）

| 场景 | 英文关键词 | 灯光/质感要点 |
|------|-----------|--------------|
| 电商白底 | `clean white studio background, softbox key light` | 锐焦、无环境 |
| 高端商务 | `executive desk setting, warm ambient light, shallow depth` | 高级感、弱景深 |
| 户外 | `outdoor adventure, natural daylight, blurred trail background` | 自然光、动感 |
| 家居 | `modern home interior, soft window light` | 生活化 |
| 健身 | `gym setting, sporty mood, dynamic angle` | 机能感 |
| 极简海报 | `minimalist poster, generous negative space` | 大量留白 |
| 车载 | `car cup holder context, dashboard light` | 场景化 |
| 分解图 | `exploded view, components separated, technical layout` | 工程感 |

---

## 三、电商延展构图（多图模板）

**杯盖分离展示**：
```
detached cap shown beside bottle, exploded view,
same product two parts, clean studio background
```
负面：`cap merged with body, floating cap, wrong cap scale`

**杯身与包装盒组合**：
```
product beside its retail box, packaging match, e-commerce set
```

**同款多颜色排列**：
```
five color variants in a row, identical product different colors,
uniform lighting, aligned grid
```
负面：`inconsistent product shape across variants, mismatched proportions`

**透明背景抠图素材（packshot）**：
```
transparent background, orthogonal front view, no shadow,
no reflection, pure product cutout
```
负面：`background, shadow, reflection, environment`

---

## 四、与工作台的集成建议

- 短期：场景价值已间接吸收（灯光进 `jug scene` + 防缺陷进 `NEG_WORDS`）。
- 中期（规划项）：在「调整中心」增加"场景/角度"下拉，映射到 `productPresets[jug].scene` 字段，复用本库词表。
- 长期：多图模板（杯盖分离/多色排列）需扩展工作台多图机制 + UI，风险高，单列规划。
