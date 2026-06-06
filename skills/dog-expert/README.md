# Dog Expert (Intelligence Gathering Expert)

Twelve Zodiac Team - Dog Expert (情报收集专家/狗仔)

## Role Definition

**Dog Expert** is the "Intelligence Gathering Expert (Pap
arazzi)" in the Twelve Zodiac Team, responsible for:
- Collecting technical intelligence and market dynamics
- Tracking the latest AI technology and industry trends
- Monitoring competitor dynamics and patent information
- Collecting user feedback and market demand
- Building intelligence database and knowledge graph

## Core Functions

### 1. Technical Intelligence Collection
- AI technology dynamics (large models, Agent, computer vision, NLP)
- New material technology (magnesium alloy, carbon fiber, smart materials)
- Manufacturing process innovation (injection molding, die casting, surface treatment)
- Open source projects and GitHub trends

### 2. Competitor Monitoring
- Competitor product releases and technical updates
- Competitor patent layout and intellectual property
- Competitor marketing strategies and market performance
- Competitor supply chain and cost structure

### 3. Industry Dynamics Tracking
- Electric wheelchair/mobility scooter industry policies
- Market size and growth trends
- Technological innovation and breakthroughs
- Industrial chain changes and supply chain dynamics

### 4. User Demand Collection
- User feedback and pain point analysis
- Market demand and trend prediction
- User behavior and usage scenarios
- User satisfaction and NPS scoring

## Workflow

### Phase 1: Intelligence Requirements Analysis
1. Clarify intelligence collection objectives (technology/competitor/industry/user)
2. Determine intelligence sources and channels
3. Develop intelligence collection plan

### Phase 2: Intelligence Collection Execution
1. Web crawling and data scraping
2. Technical documentation and paper retrieval
3. Social media and forum monitoring
4. Patent database query

### Phase 3: Intelligence Analysis and Organization
1. Data cleaning and structuring
2. Intelligence classification and tagging
3. Trend analysis and prediction
4. Intelligence report generation

### Phase 4: Intelligence Distribution and Application
1. Intelligence storage and knowledge graph update
2. Intelligence report distribution (Twelve Zodiac Team)
3. Intelligence application scenario matching
4. Intelligence value assessment

## Skill Package Structure

```
dog-expert/
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
│   ├── intelligence_sources.json  # Intelligence sources configuration
│   ├── competitor_database.json  # Competitor database
│   ├── tech_trends.json          # Technology trends data
│   └── user_feedback.json        # User feedback data
├── scripts/                      # Scripts directory
│   ├── intelligence_collector.py  # Intelligence collection tool
│   ├── competitor_monitor.py     # Competitor monitoring tool
│   ├── tech_tracker.py           # Technology tracking tool
│   └── report_generator.py       # Report generation tool
└── tests/                        # Tests directory
    ├── test_intelligence_collector.py
    ├── test_competitor_monitor.py
    ├── test_tech_tracker.py
    └── test_report_generator.py
```

## Installation and Usage

### Install Dependencies

```bash
pip install requests beautifulsoup4 selenium pandas numpy matplotlib
```

### Usage Examples

#### Example 1: Collect Technical Intelligence
```python
from scripts.intelligence_collector import IntelligenceCollector

# Initialize collector
collector = IntelligenceCollector()

# Collect AI technology intelligence
tech_intel = collector.collect_tech_intelligence(
    keywords=["large model", "Agent", "computer vision"],
    sources=["arXiv", "GitHub", "tech blog"],
    time_range="2026-01-01 to 2026-06-05"
)

# Output intelligence report
print(tech_intel)
```

#### Example 2: Monitor Competitor Dynamics
```python
from scripts.competitor_monitor import CompetitorMonitor

# Initialize monitor
monitor = CompetitorMonitor()

# Monitor competitor product releases
competitor_updates = monitor.monitor_product_releases(
    competitors=["Competitor A", "Competitor B", "Competitor C"],
    platforms=["official website", "JD.com", "Tmall"]
)

# Output competitor dynamics
print(competitor_updates)
```

## Intelligence Sources

### Technical Intelligence Sources
- **Academic Databases**: arXiv, IEEE Xplore, ACM Digital Library
- **Open Source Platforms**: GitHub, GitLab, Bitbucket
- **Technology Communities**: Stack Overflow, Reddit, Hacker News
- **Technology Blogs**: Medium, Dev.to, personal tech blogs

### Competitor Intelligence Sources
- **Official Websites**: Product releases, technical updates, news dynamics
- **E-commerce Platforms**: JD.com, Tmall, Amazon product information and reviews
- **Patent Databases**: CNIPA, USPTO, EPO
- **Social Media**: Weibo, WeChat official accounts, LinkedIn

### Industry Intelligence Sources
- **Industry Reports**: IDC, Gartner, Forrester
- **Government Websites**: MIIT, NHC, NMPA
- **Industry Associations**: China Medical Device Industry Association
- **News Media**: Xinhua News Agency, People's Daily, industry media

## Output Format

### 1. Technical Intelligence Report
```json
{
  "report_id": "TECH-20260605-001",
  "title": "AI Technology Dynamics in June 2026",
  "date": "2026-06-05",
  "keywords": ["large model", "Agent", "computer vision"],
  "sources": ["arXiv", "GitHub", "tech blog"],
  "findings": [
    {
      "title": "GPT-5 Released",
      "source": "OpenAI Official Blog",
      "date": "2026-06-01",
      "summary": "OpenAI releases GPT-5 with 30% performance improvement",
      "impact": "high",
      "url": "https://openai.com/blog/gpt-5"
    }
  ],
  "trends": ["multimodal fusion", "Agent autonomy", "edge computing"],
  "recommendations": ["focus on multimodal technology", "layout Agent applications", "explore edge computing scenarios"]
}
```

### 2. Competitor Monitoring Report
```json
{
  "report_id": "COMP-20260605-001",
  "title": "Competitor A Product Update Monitoring",
  "date": "2026-06-05",
  "competitor": "Competitor A",
  "updates": [
    {
      "type": "product release",
      "title": "Competitor A releases new electric wheelchair",
      "date": "2026-06-03",
      "features": ["lightweight design", "smart navigation", "health monitoring"],
      "price": "¥3,999",
      "url": "https:// competitor-a.com/new-product"
    }
  ],
  "analysis": "Competitor A continues to invest in lightweight and intelligent features",
  "threat_level": "medium",
  "recommendations": ["strengthen lightweight material R&D", "accelerate smart navigation technology layout"]
}
```

## Quality Standards

### Intelligence Collection Quality
- **Timeliness**: Intelligence update frequency (real-time/daily/weekly)
- **Accuracy**: Intelligence source reliability and verification mechanism
- **Completeness**: Intelligence coverage and depth
- **Relevance**: Intelligence relevance to objectives

### Intelligence Analysis Quality
- **Logicality**: Logical analysis process and conclusions
- **Objectivity**: Avoid subjective bias and emotionalization
- **Foresight**: Trend prediction and forward-looking analysis
- **Actionability**: Intelligence actionable insights

## Collaboration with Other Experts

### Collaboration Process
1. **Rat Expert** (Requirements Analysis Expert): Clarify intelligence requirements
2. **Dog Expert** (Intelligence Gathering Expert): Collect and analyze intelligence
3. **Dragon Expert** (Competitive Analysis Expert): Deep analysis of competitor intelligence
4. **Snake Expert** (Product Design Expert): Apply intelligence to product design
5. **Rat Expert** (Requirements Analysis Expert): Review intelligence application effect

### Collaboration Output
- **Intelligence Requirements List**: Rat Expert → Dog Expert
- **Intelligence Collection Report**: Dog Expert → Dragon Expert, Snake Expert
- **Competitor Analysis Report**: Dragon Expert → Snake Expert, Rat Expert
- **Product Design Suggestions**: Snake Expert → Rat Expert

## Version History

### v1.0.0 (2026-06-05)
- Initial version
- Implement core intelligence collection functionality
- Support technical intelligence, competitor monitoring, industry dynamics tracking
- Provide intelligence analysis and report generation functionality

## License

MIT License

## Contact

- **Author**: Sufan Team (Yongkang, Zhejiang)
- **Email**: contact@sufan-team.com
- **Website**: https://www.sufan-team.com

---

**Last Updated**: 2026-06-05  
**Document Version**: v1.0.0
