# 准确出图实用规则 + 铁律兼容总览（Prompt Engineering Rules）

**来源**：`<本地资源路径>` + 生肖团架构记忆（`<架构根目录>\.workbuddy\memory\MEMORY.md` 八铁律）+ 本次提示词库整合经验
**作者**：猴哥 · 经生肖团 AI 提炼

> 本文件是 agent 驱动工作台生图时的「纪律总纲」。违反任一条都会 reintroduce 已修复的缺陷。

---

## 一、CLIP / 语言铁律

1. **中文喂不进 SDXL**：CLIP 对中文弱，所有正向/负向提示词必须英文。中文词直灌 = 出图失控。
2. **SDXL CLIP 无否定语义**：正向只写肯定描述；软概念（strap / soft band / fabric / 模糊背景）全放负向并加权 `(concept:1.x)`。
3. **标点/格式**：用逗号分隔词，勿用长句；权重用 `(word:1.2)` 而非中文"很/非常"。

---

## 二、颜色锁蓝锚铁律（工作台核心）

4. **三重蓝锚**：`buildBasePrompt` 最终强制把正向 prompt 染成 cobalt 蓝（颜色锁），靠 `main_centered_blue.png` 参考图锚定。
5. **材质/颜色词不直接进正向**：白/银/黑等颜色信号若进正向会破坏颜色锁 → 走三条安全通道：
   - 材质/质感/纹理词 → 正向 `material` 字段（**不含颜色信号**）
   - 各配色线防缺陷 → `COLOR_LINES[].desc`（工作台原有设计，desc 进 prompt）
   - 颜色专属负面 → `NEG_WORDS`
6. **B~G 配色线对抗**：非蓝配色线靠 `getActiveColorDesc()` 对抗蓝锚，agent 改配色线时勿破坏此机制。

---

## 三、文字幻觉铁律（#519 系）

7. **参考图 IPAdapter 必须 CLEAN 无字无水印**：带水印/文字=生成图必出字，负向压不住。
8. **提手曲面固有字母幻觉**：SDXL 在提手高光曲面有固有字母幻觉（非参考图污染）。jug 负向必须追加 6 项 `(text on handle:2.2)` 等加权。
9. **视觉双 QA 闸门**：出图后经 `qwen3-vl:8b` 视觉模型 + CIELAB ΔE76 双检；文字疑似 > 阈值必须返工重绘。视觉模型未启动（Ollama 挂）→ 缺陷图直接放行，必须保 Ollama 在线。

---

## 四、参考图 / 控制铁律

10. **IPAdapter 权重 0.65-0.85**，参考图 CLEAN；ControlNet Canny 0.45-0.70 / Depth 0.40-0.65；denoise 0.30-0.55（变款非复制）。
11. **EmptyLatentImage + denoise<1.0 = 幽灵图**：全图生成用 denoise=1.0；IPAdapter 须 VAEEncode→latent 喂 KSampler。

---

## 五、品类闸门铁律（防 jug 漂移）

12. **LoRA 触发词拼音专属 token**：`duntongjug`/`zidanbaocup` 等，勿改回英文（与 THERMOS 锚点冲突）。
13. **cup 类 LoRA 在 jug/pot 禁用注入**；`duntongjug` 在 jug 必注入。
14. **提交前词级清洗**：jug 品类 `THERMOS→JUG` / `slim→wide-body` / `500ml→1800ml` / `flask|tumbler|bottle→jug`。

---

## 六、参数铁律

15. **采样器 DPM++ 2M SDE Karras**，steps 28-36（现 32），CFG 4.5-6.5（现 6.5）。**勿过度采样**（85 步已证无效且拖时）。
16. **loraStrength 0.52**（jug），勿 >0.75（过拟合）。

---

## 七、变更纪律（猴哥铁律）

17. **别随便动**：ComfyUI 修复后不重启不杀进程不改脚本，除非推进 Step 2 重训且先备份 LoRA。
18. **坏文件只移不删**：错版/弃用图移到 `<本地资源路径>`，不 `rm`。
19. **Windows 含中文路径 .ps1 必须 UTF-8 BOM**，否则 PowerShell 5.1 用 GBK 误读乱码。
20. **长驻进程用 PowerShell Start-Process**，勿用 Bash `&`（shell 退出回收子进程→假重启）。
