# Zheng10 AI Image Generator

[中文版本](README_zh.md) | [English Version](README.md)

## Introduction

This skill package provides ComfyUI AI image generation capabilities for the Twelve Zodiac Team's Goat expert (zheng10-ai-image-generator). It includes prompt engineering, ControlNet precise control, LoRA model application, and integrates vacuum cup craftsmanship knowledge.

## Features

- **Prompt Engineering**: Vacuum cup professional prompt templates, material precise descriptions, surface treatment effects, scene matching, photography lighting, composition templates
- **ControlNet Precise Control**: Edge detection control, depth map control, pose control, lineart control
- **LoRA Model Application**: Vacuum cup specialized LoRA, material LoRA, surface treatment LoRA, style LoRA
- **Craftsmanship Integration**: Integrates vacuum cup materials, surface treatment, injection molding, assembly process knowledge into prompt generation

## Installation

### Prerequisites

- **ComfyUI**: Installed and running
- **Python version**: 3.8+
- **Required libraries**: `json`, `os`, `re` (built-in, no installation needed)
- **Optional libraries**: `PIL` (Pillow) for image processing

### Quick Installation

```bash
# Method 1: Clone the repository
cd E:\AI日记\Claw\skills\
git clone <repository_url> zheng10-ai-image-generator

# Method 2: Manual download and extract
# Extract the downloaded files to E:\AI日记\Claw\skills\zheng10-ai-image-generator\

# Verify installation
cd E:\AI日记\Claw\skills\zheng10-ai-image-generator
python scripts\prompt_generator.py
```

### Integration with ComfyUI

```bash
# Copy workflow files to ComfyUI workflows directory
copy workflows\vacuum_cup_rendering.json <ComfyUI installation directory>\workflows\
```

## Usage

### 1. Prompt Generation

```bash
# Run the prompt generation tool
python scripts\prompt_generator.py
```

**Output Example:**
```
=== Vacuum Cup Prompt Generation Tool Examples ===

Example 1: Generate children's vacuum cup prompt (stainless steel 316, matte spray painting, laser marked LOGO)
  Prompt:
    professional product photography of a children's vacuum cup,
    premium 316 stainless steel interior, matte spray painting exterior,
    laser marked LOGO on body, cute cartoon pattern,
    soft lighting, desaturated background, high resolution, 8K

==================================================

Example 2: Generate bounce-lid vacuum cup prompt (pure titanium TA2, brushed surface, car scene)
  Prompt:
    professional product photography of a bounce-lid vacuum cup,
    brushed pure titanium TA2 body, titanium texture,
    car cup holder compatible, sunlight through car window,
    realistic texture, 3-point lighting, 8K resolution

==================================================

Example 3: Generate smart vacuum cup prompt (smart temperature control display, LED indicator, home scene)
  Prompt:
    professional product photography of a smart vacuum cup,
    digital temperature display screen, LED indicator light,
    modern minimalist home background, soft indoor lighting,
    APP control interface visible, high-tech feel, 8K resolution
```

### 2. ControlNet Control

```bash
# Run the ControlNet control tool
python scripts\controlnet_controller.py
```

### 3. LoRA Application

```bash
# Run the LoRA application tool
python scripts\lora_applier.py
```

### 4. Using in ComfyUI

```bash
# Load workflow in ComfyUI
1. Open ComfyUI
2. Click "Load" button
3. Select `workflows\vacuum_cup_rendering.json`
4. Click "Queue Prompt" to run the workflow
```

## Data Files Structure

```
zheng10-ai-image-generator/
├── SKILL.md                          # Core documentation
├── README.md                         # English README
├── README_zh.md                     # Chinese README
├── LICENSE                          # License
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md              # Code of conduct
├── CHANGELOG.md                   # Changelog
├── AUTHORS.md                     # Authors information
├── .gitignore                        # Git ignore file
├── data/                              # Database directory
│   ├── prompt_templates.json        # Prompt templates database
│   ├── controlnet_rules.json       # ControlNet control rules database
│   ├── lora_rules.json            # LoRA application rules database
│   └── craftsmanship_integration.json # Craftsmanship integration database
├── rules/                             # Rules directory
│   ├── prompt_engineering_rules.json  # Prompt engineering rules
│   ├── controlnet_control_rules.json # ControlNet control rules
│   └── lora_application_rules.json  # LoRA application rules
├── scripts/                           # Python tools directory
│   ├── prompt_generator.py             # Prompt generation tool
│   ├── controlnet_controller.py       # ControlNet control tool
│   └── lora_applier.py             # LoRA application tool
├── workflows/                         # ComfyUI workflows directory
│   ├── vacuum_cup_rendering.json    # Vacuum cup rendering workflow
│   ├── material_showcase.json        # Material showcase workflow
│   └── scene_matching.json         # Scene matching workflow
├── tests/                             # Tests directory
│   ├── test_prompt_generator.py
│   ├── test_controlnet_controller.py
│   └── test_lora_applier.py
└── references/                       # References directory
    ├── prompt_engineering_guide/      # Prompt engineering guide
    ├── controlnet_guide/             # ControlNet guide
    └── lora_guide/                 # LoRA application guide
```

## Craftsmanship Integration

This skill package integrates vacuum cup craftsmanship knowledge into prompt generation:

### 1. Material Knowledge Integration

- **Metal materials**: 304/316/316L stainless steel, TA1/TA2/TC4 titanium - integrated into material precise description prompts
- **Plastic materials**: Food-grade PP, TRITAN, silicone, ABS, PC - integrated into plastic lid prompt generation

### 2. Surface Treatment Knowledge Integration

- **Metal surface treatment**: Spray painting, spray coating, laser marking, heat transfer, 3D UV printing, electroplating, UV coating - integrated into surface treatment effect prompts
- **Plastic surface treatment**: Plastic spray painting, plastic UV coating, plastic electroplating, IMD - integrated into plastic surface treatment effect prompts

### 3. Injection Molding Knowledge Integration

- **Injection molding parameters**: PP, TRITAN, ABS, PC, silicone - integrated into plastic part prompt generation
- **Defect diagnosis**: Short shot, flash, sink mark, warpage, burn marks - integrated into quality issue analysis prompts

### 4. Assembly Process Knowledge Integration

- **Assembly processes**: Ultrasonic welding, hot plate welding, screw fixation, buckle assembly, glue bonding, sealing ring assembly - integrated into assembly effect prompt generation

## Workflow Example

### Generating a Vacuum Cup Product Image

```
1. Receive requirement: Generate a bounce-lid vacuum cup product image
   - Product type: Bounce-lid vacuum cup
   - Material: Pure titanium TA2
   - Surface treatment: Brushed finish
   - Scene: Car cup holder
   - Style: Modern minimalist

2. Generate prompt:
   - Run prompt_generator.py
   - Input: Product type, material, surface treatment, scene, style
   - Output: Precise prompt (positive prompt + negative prompt)

3. Add ControlNet control (optional):
   - Run controlnet_controller.py
   - Input: Edge detection image, depth map, lineart
   - Output: ControlNet control prompt

4. Apply LoRA model (optional):
   - Run lora_applier.py
   - Input: Vacuum cup specialized LoRA, material LoRA, style LoRA
   - Output: LoRA application prompt

5. Run ComfyUI workflow:
   - Load vacuum_cup_rendering.json
   - Input: Prompt, ControlNet control image, LoRA model
   - Output: Generated image

6. Quality review:
   - Call Rooster expert (design reviewer) for quality review
   - Input: Generated image
   - Output: Review report, improvement suggestions

7. Parameter tuning:
   - According to review feedback, call Monkey expert (design adjuster) for parameter tuning
   - Input: Review report, improvement suggestions
   - Output: Tuned generated image

8. Final delivery:
   - Deliver final generated image to Rat expert (product researcher)
   - Input: Tuned generated image
   - Output: Final deliverable
```

## License

MIT License - See LICENSE file for details.

## Maintainers

- **Maintainer**: Sufan Team
- **Location**: Yongkang, Zhejiang
- **Update Frequency**: Weekly

## Contact

If you have any questions or suggestions, please contact us via:
- Create an Issue
- Contact Sufan Team

---

**Note**: The prompt templates, ControlNet control rules, and LoRA application rules in this skill package are for reference only. Please adjust according to specific requirements.
