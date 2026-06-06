# Vacuum Cup Craftsmanship

[中文版本](README_zh.md) | [English Version](README.md)

## Introduction

This skill package provides comprehensive knowledge of vacuum cup (thermos) craftsmanship, including material processing, surface treatment, injection molding, and assembly processes. It includes Python tools for process selection, cost calculation, quality evaluation, injection molding parameter recommendation, and quality issue analysis.

## Features

- **Complete Craftsmanship Knowledge Base**: Covers materials, surface treatments, injection molding, and assembly processes
- **Material Database**: Detailed parameters for stainless steel, pure titanium, and plastics (PP, TRITAN, Silicone, ABS, PC)
- **Surface Treatment Database**: Parameters, costs, and advantages/disadvantages of spraying, printing, and advanced manufacturing processes
- **Injection Molding Database**: Injection machine parameters, mold design, process parameters, defect diagnosis
- **Assembly Process Database**: Parameters, costs, and quality control for welding, fixing, and assembly processes
- **Process Selection Tool**: Select suitable materials and surface treatments based on requirements
- **Cost Calculation Tool**: Calculate total cost for materials, surface treatments, and assembly
- **Quality Evaluation Tool**: Evaluate process quality (material, surface treatment, assembly)
- **Injection Molding Parameter Recommendation**: Recommend injection molding parameters based on material and product dimensions
- **Quality Issue Analysis**: Analyze quality issues and provide improvement suggestions

## Installation

### Prerequisites

- Python 3.8+
- Required libraries: `json`, `os`, `typing` (built-in, no installation needed)

### Quick Installation

```bash
# Method 1: Clone the repository
cd E:\AI日记\Claw\skills\
git clone <repository_url> vacuum-cup-craftsmanship

# Method 2: Manual download and extract
# Extract the downloaded files to E:\AI日记\Claw\skills\vacuum-cup-craftsmanship\

# Verify installation
cd E:\AI日记\Claw\skills\vacuum-cup-craftsmanship
python scripts\craftsmanship_tool.py
```

## Usage

### 1. Process Selection

```python
from scripts.craftsmanship_tool import select_material, select_surface_treatment

# Select material (cost max 80, food-grade safety)
materials = select_material('metals', {'cost_max': 80, 'safety_level': '食品级'})
for m in materials[:3]:
    print(f"Material: {m['name']} (ID: {m['id']})")

# Select surface treatment (cost max 20, durability ≥ 80)
surface_treatments = select_surface_treatment('metal_surface', {'cost_max': 20, 'durability_min': 80})
for st in surface_treatments[:3]:
    print(f"Surface Treatment: {st['name']} (ID: {st['id']})")
```

### 2. Cost Calculation

```python
from scripts.craftsmanship_tool import calculate_craftsmanship_cost

# Calculate process cost (material: 304, surface treatment: laser marking,
# assembly: ultrasonic welding, quantity: 1000)
cost = calculate_craftsmanship_cost('304', 'laser_marking', 'ultrasonic_welding', 1000)
print(f"Material Cost: ¥{cost['material_cost']}")
print(f"Surface Treatment Cost: ¥{cost['surface_treatment_cost']}")
print(f"Assembly Cost: ¥{cost['assembly_cost']}")
print(f"Total Cost: ¥{cost['total_cost']}")
print(f"Unit Cost: ¥{cost['unit_cost']}/pc")
```

### 3. Quality Evaluation

```python
from scripts.craftsmanship_tool import evaluate_craftsmanship_quality

# Evaluate process quality (material: 304, surface treatment: laser marking,
# assembly: ultrasonic welding)
quality = evaluate_craftsmanship_quality('304', 'laser_marking', 'ultrasonic_welding')
print(f"Material Quality: {quality['material_quality']}/100")
print(f"Surface Treatment Quality: {quality['surface_quality']}/100")
print(f"Assembly Quality: {quality['assembly_quality']}/100")
print(f"Overall Quality: {quality['overall_quality']}/100 ({quality['quality_level']})")
```

### 4. Injection Molding Parameter Recommendation

```python
from scripts.craftsmanship_tool import recommend_injection_molding_parameters

# Recommend injection molding parameters (material: PP, product dimensions: 100x80x30mm)
params = recommend_injection_molding_parameters('PP', {'length': 100, 'width': 80, 'height': 30})
print(f"Mold Temperature: {params['mold_temperature']}")
print(f"Melt Temperature: {params['melt_temperature']}")
print(f"Injection Pressure: {params['injection_pressure']}")
print(f"Cycle Time: {params['cycle_time']}")
print(f"Shrinkage Rate: {params['shrinkage_rate']}")
```

### 5. Quality Issue Analysis

```python
from scripts.craftsmanship_tool import analyze_quality_issues

# Analyze injection molding quality issues (defect rate 5.0%, strength 75)
quality_data = {'defect_rate': 5.0, 'strength': 75}
suggestions = analyze_quality_issues('injection_molding', 'PP', quality_data)
for s in suggestions:
    print(f"uggestion: {s}")
```

### 6. Run Demo

```bash
# Run the demonstration
python scripts/craftsmanship_tool.py
```

## Data Files Structure

```
vacuum-cup-craftsmanship/
├── SKILL.md                          # Core documentation
├── README.md                         # English README
├── README_zh.md                     # Chinese README
├── LICENSE                          # License
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md              # Code of conduct
├── CHANGELOG.md                   # Changelog
├── AUTHORS.md                     # Authors information
├── .gitignore                        # Git ignore file
├── data/                              # Knowledge base directory
│   └── craftsmanship_knowledge.json # Complete craftsmanship knowledge database
├── scripts/                           # Python tools directory
│   ├── knowledge_query.py             # Knowledge query tool (basic)
│   └── craftsmanship_tool.py       # Complete craftsmanship tool (process selection, cost calculation, quality evaluation, parameter recommendation, issue analysis)
├── tests/                             # Tests directory
│   └── test_craftsmanship_tool.py   # Test file for craftsmanship_tool.py
└── references/                       # References directory
    ├── material_specs/                # Material specifications
    ├── process_guides/                # Process guides
    ├── injection_molding_guide/      # Injection molding guide
    └── assembly_guide/              # Assembly guide
```

## Knowledge Base Overview

### 1. Material Knowledge

#### 1.1 Metal Materials

| Material | Density (g/cm³) | Corrosion Resistance | Safety | Cost Index | Application |
|----------|---------------|---------------------|--------|---------|------------|
| 304 SS | 7.93 | 85/100 | Food Grade | 60 | Regular vacuum cup |
| 316 SS | 7.98 | 95/100 | Medical Grade | 85 | High-end cup, children's cup |
| TA2 Ti | 4.51 | 99/100 | Medical Grade | 90 | Lightweight cup |

#### 1.2 Plastic Materials

| Material | Density (g/cm³) | Temp. Resistance | Safety | Cost Index | Application |
|----------|---------------|-------------------|--------|---------|------------|
| Food-grade PP | 0.90 | 120°C | Food Grade | 40 | Cup lid, sealing ring |
| TRITAN | 1.05 | 109°C | BPA-free | 70 | High-end lid, children's cup |
| Silicone | 1.10 | 200°C | Food Grade | 50 | Sealing ring, anti-leak pad |

### 2. Surface Treatment Knowledge

#### 2.1 Metal Surface Treatment

| Process | Cost | Durability | Applications |
|---------|------|------------|-------------|
| Spray Painting | 15 | 70/100 | Cup shell, lid |
| Laser Marking | 8 | 95/100 | LOGO marking, pattern engraving |
| 3D UV Printing | 25 | 90/100 | 3D pattern, emboss effect |

#### 2.2 Plastic Surface Treatment

| Process | Cost | Durability | Applications |
|---------|------|------------|-------------|
| Plastic Spray Painting | 12 | 65/100 | Plastic lid, button |
| Plastic UV Coating | 18 | 85/100 | Plastic lid, decoration |
| IMD | 15 | 88/100 | Plastic lid, pattern decoration |

### 3. Injection Molding Knowledge

#### 3.1 Process Parameters

| Material | Melt Temp. | Mold Temp. | Injection Pressure | Cycle Time | Shrinkage |
|----------|------------|------------|-------------------|------------|-----------|
| PP | 200-280°C | 40-80°C | 70-120 MPa | 20-40s | 1.0-2.5% |
| TRITAN | 260-290°C | 50-80°C | 80-130 MPa | 25-45s | 0.5-0.7% |
| ABS | 200-240°C | 50-80°C | 70-120 MPa | 20-40s | 0.4-0.9% |

#### 3.2 Common Defects

| Defect | Cause | Solution |
|--------|-------|----------|
| Short Shot | Insufficient injection pressure, low mold temperature, poor venting | Increase injection pressure, increase mold temperature, add venting slots |
| Flash | Insufficient clamping force, poor mold fitting, excessive injection pressure | Increase clamping force, repair mold, reduce injection pressure |
| Sink Mark | Insufficient holding pressure, uneven cooling, excessive wall thickness | Extend holding time, optimize cooling system, optimize wall thickness design |

### 4. Assembly Process Knowledge

#### 4.1 Process Comparison

| Process | Strength | Efficiency | Cost | Application |
|---------|----------|------------|------|------------|
| Ultrasonic Welding | 85/100 | 90/100 | 60 | Plastic lid welding |
| Screw Fixation | 90/100 | 60/100 | 70 | Lid fixation, handle fixation |
| Buckle Assembly | 70/100 | 95/100 | 30 | Buckle lid, quick assembly |

## License

MIT License - See LICENSE file for details

## Maintainers

- **Maintainer**: Sufan Team
- **Location**: Yongkang, Zhejiang
- **Update Frequency**: Quarterly

## Contact

If you have any questions or suggestions, please contact us via:
- Create an Issue
- Contact Sufan Team

---

**Note**: The data in this skill package is for reference only. Please adjust according to specific circumstances when applying.
