# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Planning new features for next release

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [4.0.0] - 2026-06-05

### Added
- Recovered from archived state (previous version 3.0, score 62.70)
- Integrated vacuum cup craftsmanship knowledge (materials, surface treatment, injection molding, assembly process)
- Added prompt engineering with craftsmanship integration
- Added ControlNet precise control with craftsmanship integration
- Added LoRA model application with craftsmanship integration
- Added data files:
  - `prompt_templates.json` (prompt templates database)
  - `controlnet_rules.json` (ControlNet control rules database)
  - `lora_rules.json` (LoRA application rules database)
  - `craftsmanship_integration.json` (craftsmanship integration database)
- Added Python tools:
  - `prompt_generator.py` (prompt generation tool)
  - `controlnet_controller.py` (ControlNet control tool)
  - `lora_applier.py` (LoRA application tool)
- Added ComfyUI workflows:
  - `vacuum_cup_rendering.json` (vacuum cup rendering workflow)
  - `material_showcase.json` (material showcase workflow)
  - `scene_matching.json` (scene matching workflow)
- Added documentation:
  - `SKILL.md` (skill definition)
  - `README.md` (English documentation)
  - `README_zh.md` (Chinese documentation)
- Added standard files:
  - `LICENSE` (MIT License)
  - `CONTRIBUTING.md` (contribution guidelines)
  - `CODE_OF_CONDUCT.md` (Code of Conduct)
  - `CHANGELOG.md` (this file)
  - `.gitignore`

### Changed
- Upgraded from version 3.0 to version 4.0
- Improved prompt engineering with craftsmanship knowledge integration
- Improved ControlNet control with craftsmanship knowledge integration
- Improved LoRA application with craftsmanship knowledge integration

### Deprecated
- Nothing yet

### Removed
- Removed archived version (version 3.0)

### Fixed
- Fixed low score issue (from 62.70 to target 90+)
- Fixed missing craftsmanship knowledge integration

### Security
- Nothing yet

---

## Release Notes

### [4.0.0] - 2026-06-05

**Recovered from Archived State**

This release recovers the Goat expert (zheng10-ai-image-generator) skill package from archived state (previous version 3.0, score 62.70) and integrates vacuum cup craftsmanship knowledge.

**Key Features:**
- ✅ Recovered from archived state (version 4.0)
- ✅ Integrated vacuum cup craftsmanship knowledge:
  - Material knowledge (stainless steel, pure titanium, plastics)
  - Surface treatment knowledge (spray painting, spray coating, laser marking, heat transfer, 3D UV printing, electroplating, UV coating)
  - Injection molding knowledge (PP, TRITAN, ABS, PC, silicone)
  - Assembly process knowledge (ultrasonic welding, hot plate welding, screw fixation, buckle assembly, glue bonding, sealing ring assembly)
- ✅ Prompt engineering with craftsmanship integration:
  - Vacuum cup professional prompt templates
  - Material precise descriptions (stainless steel, pure titanium, plastics)
  - Surface treatment effects (spray painting, spray coating, laser marking, etc.)
  - Scene matching (home, office, car, outdoor, gift)
  - Photography lighting (3-point lighting, top lighting, window lighting)
  - Composition templates (main view, detail showcase, scene matching, usage scene, packaging showcase)
- ✅ ControlNet precise control with craftsmanship integration:
  - Edge detection control (precise shape control)
  - Depth map control (spatial depth, 3D effect)
  - Lineart control (from sketch to realistic rendering)
- ✅ LoRA model application with craftsmanship integration:
  - Vacuum cup specialized LoRA (improve generation accuracy)
  - Material LoRA (stainless steel, pure titanium, plastics)
  - Surface treatment LoRA (spray painting, spray coating, laser marking, etc.)
  - Style LoRA (modern minimalist, light luxury, high-tech, cute cartoon)
- ✅ Complete documentation in both English and Chinese
- ✅ Standard open-source files (LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, .gitignore)

**Target Users:**
- Twelve Zodiac Team members (especially Goat expert)
- ComfyUI users
- AI image generation enthusiasts
- Vacuum cup product designers

**Next Steps:**
- Add more prompt templates
- Add more ControlNet control examples
- Add more LoRA application examples
- Add tests for all Python tools
- Improve documentation with more examples

---

## Links

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
