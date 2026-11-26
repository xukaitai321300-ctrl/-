# 金标准长提示词参考：500mL 石墨黑真空保温杯

**来源**：`<本地资源路径> 提示词知识库.txt`（JSON 末尾 500mL 石墨黑真空保温杯精确工业规格 + 3 套完整长提示词）
**作者**：猴哥 · 经生肖团 AI 提炼
**用途**：作为保温杯生图 prompt 的「金标准」模板。 cup 类（商务/时尚/运动款）可参照结构改写；jug 类注意形态与颜色锁蓝锚铁律。

> ⚠️ 本文件是**参考模板**，不是工作台运行时源。工作台是配方式拼装（productPresets + COLOR_LINES + NEG_WORDS），不直接消费整段长提示词。agent 升级工作台默认 prompt 时，以本文件为"质感上限"对照。

---

## 一、工业规格（用于约束 prompt 真实性）

| 参数 | 值 |
|------|----|
| 容量 | 500mL |
| 颜色 | 石墨黑 `#252729` |
| 表面处理 | 哑光粉末涂层，光泽度 8-12 GU |
| 材质 | 316 不锈钢内胆 + 外胆哑光涂层 |
| 结构 | 螺纹旋盖 + 宽口 + 细窄纵向高光带（不镜面） |
| 摄影 | 电商白底、柔光箱主光前左、右侧窄轮廓光、柔和接触阴影 |

---

## 二、金标准长提示词 · 主图（Hero）

```
product photography of a 500ml vacuum insulated bottle in graphite black (#252729),
matte powder-coated body with 8-12 GU low gloss, fine narrow vertical highlight band on left edge,
no mirror reflection, visible micro-texture on surface,
threaded screw cap with subtle knurling, wide mouth,
clean white seamless studio background, large softbox key light from front-left,
narrow rim light on right edge, soft compact contact shadow beneath,
sharp product focus, professional e-commerce hero shot, 1024x1024,
centered composition, 60% frame coverage
```

---

## 三、金标准长提示词 · 杯盖分离（Cap Separated）

```
e-commerce set of a 500ml graphite black vacuum bottle with its cap detached and placed beside the body,
exploded two-part view, identical material and finish on both parts,
matte powder-coated (#252729), fine vertical highlight, no mirror reflection,
clean white studio background, soft diffused lighting, sharp focus,
both parts same scale and aligned, professional product photography
```

---

## 四、金标准长提示词 · 分解图（Exploded / Technical）

```
technical exploded view of a 500ml vacuum insulated bottle,
components separated vertically: cap, collar, body shell, vacuum layer, 316 inner wall, base,
graphite black matte finish (#252729), labeled-free clean layout,
neutral light gray technical background, soft even lighting,
engineering product illustration style, high detail, no text
```

---

## 五、对照工作台现状的差距（治本参考）

| 维度 | 金标准 | 工作台 jug 现状（V6.2026.0814.0002） | 缺口 |
|------|--------|--------------------------------------|------|
| 黑材质精度 | `#252729, 8-12 GU, 细窄纵向高光` | `matte powder-coated...controlled narrow vertical highlights` | 已吸收 ✅ |
| 灯光 | 柔光箱前左 + 右窄轮廓 + 接触阴影 | `large softbox key light from front-left, narrow rim light on right edge` | 已吸收 ✅ |
| 场景 | 仅白底 | 仅白底 | 一致 |
| 多图模板 | 杯盖分离/分解图 | 无 | 待规划 UI |

> 结论：主图质量维度工作台已对齐金标准；杯盖分离/分解图需工作台多图机制扩展（规划项）。
