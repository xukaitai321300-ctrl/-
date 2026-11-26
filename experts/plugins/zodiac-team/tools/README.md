# tools/ · 工具面清单

> 本目录是**指路牌**，不是空壳 —— 每个工具的真实实现都在别处（单一真源）。
> 纪律：工具**不复制**到本目录，只写「它在哪、怎么调、谁负责」。

| 工具 | 真实位置 | 职责 |
|---|---|---|
| 生肖团总线 | `~/.workbuddy/skills/zheng10-bus/zodiac_bus.js` | emit 事件 / 路由（键格式须 `角色.类型`） |
| MCP 客户端 | `~/.workbuddy/mcp.json` | MCP server 真实配置（**唯一真源**） |
| MCP · 语义搜索 | `tavily`（npx @tavily/mcp） | 通用网页检索 |
| MCP · 联网眼 | `agent-reach`（`python -m agent_reach.integrations.mcp_server`） | 小红书/B站/推特/Reddit/YouTube 等 16 通道 |
| GitHub CLI | `H:\架构\_tools\gh\gh.exe` | 仓库/issue/代码搜索 |
| Agent-Reach CLI | `H:\架构\_envs\agent_reach\Scripts\agent-reach.exe` | doctor / install / 渠道体检 |
| Octop CLI | `~/.octop/venv/Scripts/octop.exe` | 自托管助手（Web 8088） |
| ComfyUI API | `http://127.0.0.1:8188` | 出图 / 判图（整合包根 `<COMFYUI_ROOT>`） |
| 生图质量门禁 | `H:\架构\_inspect\_chk_r1*.cjs` | 多档判据（r170/r172/r176 等） |

## 约定

- 新增工具**先登记到 `H:\架构\_资产台账.json`**（门禁段26 判据④「未登记即红」）。
- 工具若依赖外部程序 ⇒ 必须有**独立路径**（禁依赖会话 PATH）。
- 弹窗类调用必须带 `creationflags=CREATE_NO_WINDOW`（门禁哨兵会抓）。
