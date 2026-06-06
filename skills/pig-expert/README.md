# Pig Expert (Style Reference and Prompt Asset Expert)

Twelve Zodiac Team - Pig Expert (风格参考与Prompt素材专家)

## Role Definition

**Pig Expert** is the "Style Reference and Prompt Asset Expert" in the Twelve Zodiac Team, responsible for:
- Managing and maintaining style reference library
- Organizing and optimizing Prompt asset library
- Generating styled Prompt templates
- Optimizing AI image generation effects and style consistency
- Building association system between style-asset-prompt

## Core Functions

### 1. Style Reference Management
- Collecting and organizing product design style references (modern minimalist, industrial, tech, etc.)
- Classifying and tagging style reference images and descriptions
- Building style tag system and retrieval mechanism
- Updating and maintaining style reference library

### 2. Prompt Asset Organization
- Collecting and organizing Prompt keyword library
- Classifying and tagging Prompt assets (material, function, scenario, style, etc.)
- Optimizing Prompt expression and description precision
- Building Prompt asset retrieval and usage mechanism

### 3. Styled Prompt Generation
- Generating styled Prompts according to design requirements
- Combining style references and Prompt assets to generate high-quality Prompts
- Optimizing Prompts to improve AI image generation effects
- Generating Prompt variants and optimization suggestions

### 4. AI Image Generation Effect Optimization
- Analyzing AI image generation effects and style consistency
- Optimizing Prompts to improve generation quality
- Adjusting style parameters and weights
- Building generation effect evaluation and feedback mechanism

## Workflow

### Phase 1: Style Requirements Analysis
1. Clarify design requirements and style positioning
2. Determine style reference types and quantities
3. Develop Prompt generation strategy

### Phase 2: Style Reference Collection
1. Retrieve relevant styles from style reference library
2. Collect and organize style reference images and descriptions
3. Analyze and extract key style features
4. Build style feature vector representation

### Phase 3: Prompt Asset Organization
1. Retrieve relevant assets from Prompt asset library
2. Organize and classify Prompt keywords
3. Optimize Prompt expression and description
4. Generate Prompt templates and variants

### Phase 4: Styled Prompt Generation
1. Combine style references and Prompt assets
2. Generate styled Prompts
3. Optimize Prompts to improve generation effects
4. Generate Prompt variants and optimization suggestions

### Phase 5: Effect Evaluation and Optimization
1. Use Prompts to generate AI images
2. Evaluate generation effects and style consistency
3. Optimize Prompts and style parameters
4. Update style reference library and Prompt asset library

## Skill Package Structure

```
pig-expert/
├── SKILL.md                      # Skill package main document
├── README.md                     # English documentation
├── README_zh.md                  # Chinese documentation
├── LICENSE                       # License
├── CONTRIBUTING.md               # Contribution guidelines
├── CODE_OF_CONDUCT.md            # Code of conduct
├── CHANGELOG.md                  # Change log
├── AUTHORS.md                    # Author information
├── .gitignore                    # Git ignore file
├── data/                         # Data directory
│   ├── style_references.json     # Style reference library
│   ├── prompt_templates.json     # Prompt template library
│   ├── material_library.json     # Material asset library
│   └── style_prompt_mapping.json # Style-Prompt mapping
├── scripts/                      # Scripts directory
│   ├── style_manager.py          # Style management tool
│   ├── prompt_generator.py       # Prompt generation tool
│   ├── material_searcher.py      # Asset search tool
│   └── effect_analyzer.py        # Effect analysis tool
└── tests/                        # Tests directory
    ├── test_style_manager.py
    ├── test_prompt_generator.py
    ├── test_material_searcher.py
    └── test_effect_analyzer.py
```

## Installation and Usage

### Install Dependencies

```bash
pip install requests pandas numpy matplotlib Pillow
```

### Usage Examples

#### Example 1: Manage Style References
```python
from scripts.style_manager import StyleManager

# Initialize style manager
manager = StyleManager()

# Add style reference
style_ref = manager.add_style_reference(
    style_name="Modern Minimalist",
    description="Simple, practical, functional",
    reference_images=["image1.jpg", "image2.jpg"],
    tags=["modern", "minimalist", "practical"]
)

# Search style references
results = manager.search_style_references(keyword="Modern Minimalist")
print(results)
```

#### Example 2: Generate Styled Prompt
```python
from scripts.prompt_generator import PromptGenerator

# Initialize Prompt generator
generator = PromptGenerator()

# Generate styled Prompt
prompt = generator.generate_styled_prompt(
    product="Spring Lid Thermos",
    style="Modern Minimalist",
    features=["lightweight", "anti-misoperation", "car-compatible"],
    materials=["magnesium alloy", "PP", "silicone"]
)

# Output Prompt
print(prompt)
```

## Style Reference Library

### Style Classification

#### 1. Modern Minimalist
- **Features**: Simple, practical, functional
- **Keywords**: modern, minimalist, practical, functional, simple
- **Application Scenarios**: Electric wheelchair, thermos, home products

#### 2. Industrial
- **Features**: Rugged, mechanical, metallic texture
- **Keywords**: industrial, rugged, mechanical, metal, texture
- **Application Scenarios**: Electric wheelchair frame, metal accessories

#### 3. Tech
- **Features**: Futuristic, intelligent, tech-savvy
- **Keywords**: tech, future, intelligent, innovative, digital
- **Application Scenarios**: Smart electric wheelchair, smart thermos

#### 4. Natural
- **Features**: Eco-friendly, natural, organic
- **Keywords**: natural, eco-friendly, organic, ecological, green
- **Application Scenarios**: Eco-friendly material products, organic food containers

## Prompt Asset Library

### Prompt Classification

#### 1. Material
- **Metal Materials**: Magnesium alloy, aluminum alloy, stainless steel, titanium alloy
- **Plastic Materials**: PP, ABS, PC, TRITAN, silicone
- **Other Materials**: Carbon fiber, wood, glass, ceramic

#### 2. Function
- **Electric Wheelchair**: Lightweight, foldable, smart navigation, health monitoring
- **Thermos**: Spring lid, anti-misoperation, car-compatible, USB heating

#### 3. Scenario
- **Indoor Scenarios**: Home, office, hospital
- **Outdoor Scenarios**: Park, street, travel
- **Car Scenarios**: Car cup holder, USB charging, magnetic fixation

#### 4. Style
- **Modern Minimalist**: Simple, practical, functional
- **Industrial**: Rugged, mechanical, metallic texture
- **Tech**: Futuristic, intelligent, tech-savvy

## Output Format

### 1. Style Reference Report
```json
{
  "report_id": "STYLE-20260605-001",
  "title": "Modern Minimalist Style Reference Report",
  "date": "2026-06-05",
  "style_name": "Modern Minimalist",
  "description": "Simple, practical, functional",
  "reference_images": ["image1.jpg", "image2.jpg"],
  "key_features": ["simple", "practical", "functional"],
  "keywords": ["modern", "minimalist", "practical", "functional", "simple"],
  "application_scenarios": ["electric wheelchair", "thermos", "home products"],
  "prompt_templates": ["{product} in modern minimalist style", "Simple and practical {product} design"]
}
```

### 2. Prompt Generation Report
```json
{
  "report_id": "PROMPT-20260605-001",
  "title": "Spring Lid Thermos Prompt Generation Report",
  "date": "2026-06-05",
  "product": "Spring Lid Thermos",
  "style": "Modern Minimalist",
  "prompt": "Spring lid thermos in modern minimalist style, using magnesium alloy cup body and PP inner liner, with lightweight, anti-misoperation, car-compatible and other functions, simple and practical design style",
  "prompt_variants": [
    "Spring lid thermos in modern minimalist style, magnesium alloy cup body, lightweight design",
    "Simple and practical spring lid thermos, PP inner liner, anti-misoperation design",
    "Functional spring lid thermos, car-compatible, modern minimalist style"
  ],
  "recommendations": ["strengthen lightweight design", "optimize anti-misoperation mechanism", "improve car compatibility"]
}
```

## Quality Standards

### Style Reference Quality
- **Completeness**: Completeness and representativeness of style references
- **Accuracy**: Accuracy of style feature descriptions
- **Retrievability**: Retrieval efficiency and precision of style references
- **Timeliness**: Update frequency of style references

### Prompt Generation Quality
- **Relevance**: Relevance of Prompt to product requirements
- **Accuracy**: Accuracy of Prompt descriptions
- **Style Consistency**: Consistency between Prompt and style references
- **Generatability**: Generatability and effect of Prompt

## Collaboration with Other Experts

### Collaboration Process
1. **Rat Expert** (Requirements Analysis Expert): Clarify style requirements
2. **Pig Expert** (Style Reference and Prompt Asset Expert): Provide style references and Prompt assets
3. **Goat Expert** (ComfyUI Image Generation Core Expert): Use Prompts to generate AI images
4. **Rooster Expert** (AI Image Generation Review Expert): Review generation effects and style consistency
5. **Pig Expert** (Style Reference and Prompt Asset Expert): Optimize Prompts and style references

### Collaboration Output
- **Style Requirements List**: Rat Expert → Pig Expert
- **Style References and Prompt Assets**: Pig Expert → Goat Expert
- **AI Image Generation Effect Evaluation**: Rooster Expert → Pig Expert
- **Optimized Prompts and Style References**: Pig Expert → Goat Expert

## Version History

### v1.0.0 (2026-06-05)
- Initial version
- Implement core style reference management and Prompt generation functionality
- Support style reference library and Prompt asset library management
- Provide styled Prompt generation and effect optimization functionality

## License

MIT License

## Contact

- **Author**: Sufan Team (Yongkang, Zhejiang)
- **Email**: contact@sufan-team.com
- **Website**: https://www.sufan-team.com

---

**Last Updated**: 2026-06-05  
**Document Version**: v1.0.0
