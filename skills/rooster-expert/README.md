# Rooster Expert Skill Package (十二生肖团 - 鸡专家)#

鸡专家（AI生图评审专家）技能包，负责评审生成图质量、质量守门员。包含生图质量评审、质量守门员、评审标准管理等功能。是十二生肖团的生图质量把关者。

## Features#

- **AI Image Review**: Realism evaluation, material texture evaluation, lighting naturalness evaluation#
- **Quality Gatekeeper**: Veto power, quality red line management, review standard execution#
- **Review Standard Management**: Review standard formulation, standard update, standard execution supervision#

## Installation#

1. Ensure Python 3.8+ is installed.#
2. No additional Python dependencies are required (only standard libraries: json, argparse).#

## Usage#

```bash
# Review generated image quality#
python scripts/image_review_tool.py --image "path/to/image.jpg"#

# Execute quality gatekeeper function#
python scripts/quality_gatekeeper_tool.py --image "path/to/image.jpg" --standard "high"#
```

## Skill Package Quality#

This skill package is designed to achieve a quality score of **90+** (target: 100/100)