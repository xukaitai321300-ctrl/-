## Description: <br>
Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and design-focused coding agents use this skill to define visual direction, interface hierarchy, layout strategy, typography, and color choices before implementing web or mini program interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's strict visual-design prohibitions can conflict with an existing brand system or approved design tokens. <br>
Mitigation: Use the artifact's documented brand escape hatch: treat real brand colors, font tokens, and design-system rules as higher-priority constraints, document the override, and keep the override narrow. <br>
Risk: The skill may produce UI code or visual direction before the design intent and target platform are clear. <br>
Mitigation: Follow the included activation checklist by outputting a design specification first, confirming whether the target is web or mini program, and using the appropriate implementation skill after the design spec is fixed. <br>


## Reference(s): <br>
- [Ui Design Guide on ClawHub](https://clawhub.ai/binggg/ui-design-guide) <br>
- [Current skill raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md) <br>
- [CloudBase main entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Web implementation sibling skill](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/web-development/SKILL.md) <br>
- [Mini program implementation sibling skill](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/miniprogram-development/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown guidance with design specifications, optional code, and inline shell audit commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to produce a design specification before interface code and to audit generated UI for color, font, icon, layout, and design-spec compliance.] <br>

## Skill Version(s): <br>
1.16.0 (source: server release metadata; artifact frontmatter reports 2.20.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
