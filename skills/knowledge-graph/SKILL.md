---
name: knowledge-graph
description: Maintain Clawdbot's compounding knowledge graph under life/areas/** by adding/superseding atomic facts (items.json), regenerating entity summaries (summary.md), and keeping IDs consistent. Use when you need deterministic updates to the knowledge graph rather than manual JSON edits.
---
tags: ["ai", "agent", "skill"]


# Knowledge Graph (file-based)

Use the bundled Python script to safely update `life/areas/**`.

## Commands

Add a new fact:
```bash
python3 skills/knowledge-graph/scripts/kg.py add \
  --entity people/safa \
  --category status \
  --fact "Runs Clawdbot on a Raspberry Pi" \
  --source conversation
```

Supersede an old fact (mark old as superseded + create new fact):
```bash
python3 skills/knowledge-graph/scripts/kg.py supersede \
  --entity people/safa \
  --old safa-002 \
  --category status \
  --fact "Moved Clawdbot from Pi to a Mac mini"
```

Regenerate an entity summary from active facts:
```bash
python3 skills/knowledge-graph/scripts/kg.py summarize --entity people/safa
```

## Notes
- Entities live under: `life/areas/<kind>/<slug>/`
- Facts live in `items.json` (array). Summaries live in `summary.md`.
- IDs auto-increment per entity: `<slug>-001`, `<slug>-002`, ...
- Never delete facts; supersede them.

## Installation

```bash
# 安装方法
pip install -e .
```

## CLI Usage

```bash
# 命令行使用方法
python scripts/example.py --help
```
