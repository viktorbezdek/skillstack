# Markdown Optimizer - Quick Reference

One-page cheat sheet for experienced users who need quick command access, quality gates, transformation patterns, and integration points.

---

## 1. 💻 COMMANDS

**Extract Structure** (for AI analysis):
```bash
scripts/extract_structure.py document.md
# Outputs JSON: frontmatter, structure, metrics, checklist, questions
```

**Quick Validation** (skill folders):
```bash
scripts/quick_validate.py .opencode/skills/my-skill
# Fast check for essential requirements
```

**Quick Validation with JSON**:
```bash
scripts/quick_validate.py .opencode/skills/my-skill --json
# Machine-readable output
```

**CLI Wrapper**:
```bash
markdown-document-specialist extract document.md   # Extract structure + DQI score
markdown-document-specialist validate skill-path   # Quick validation
markdown-document-specialist init skill-name       # Initialize new skill
markdown-document-specialist package skill-path    # Package skill
```

---

## 2. 🔒 QUALITY GATES

| Document Type | Target | Checklist | Content |
| --- | --- | --- | --- |
| SKILL.md | Production-ready | Strict (no failures) | High AI-friendliness |
| Command | Acceptable+ | Strict (no failures) | Functional |
| Knowledge | Good | Strict (no failures) | Good AI-friendliness |
| README | Good | Flexible | High AI-friendliness |
| Spec | Acceptable | Loose | N/A |

**Quality Levels**:
- Excellent → Production-ready
- Good → Shareable
- Acceptable → Functional

---

## 3. 🎨 TRANSFORMATION PATTERNS (TOP 8)

| # | Pattern | Impact | Effort |
|---|---------|--------|--------|
| 1 | API → Usage | High | Medium |
| 2 | Import → Complete | Medium | Low |
| 3 | Consolidate | Medium | Medium |
| 4 | Remove Metadata | Low | Low |
| 5 | Theory → Practical | High | High |
| 6 | Error → Handling | Medium | Medium |
| 7 | Complete Examples | Medium | Medium |
| 8 | Deduplicate | Medium | Low |

---

## 4. 📚 DOCUMENT TYPES & ENFORCEMENT

**SKILL.md** (Strict):
- YAML frontmatter required
- H1 with subtitle
- No H3+ headings
- Blocks on violations

**Knowledge** (Moderate):
- NO frontmatter
- H1 with subtitle
- Numbered H2 sections
- Blocks on structural issues

**Spec** (Loose):
- Suggestions only
- Never blocks
- Flexible structure

**README** (Flexible):
- Frontmatter optional
- Safe auto-fixes only
- No blocking

**Command** (Strict):
- YAML frontmatter required (description, argument-hint, allowed-tools)
- H1 without subtitle
- Required sections: Purpose, Contract, Instructions, Example Usage
- Template: `assets/command_template.md`

---

## 5. 🛠️ COMMON ISSUES - QUICK FIXES

**Issue**: Checklist failures in JSON output
**Fix**: Review specific failures, address structural issues first

**Issue**: Low content quality rating from AI
**Fix**: Answer "How do I..." questions, add practical examples

**Issue**: Style compliance issues
**Fix**: All H2 must be ALL CAPS with emoji, --- separators between H2

**Issue**: Frontmatter issues detected
**Fix**: Keep description on single line, use [Tool1, Tool2] array format

---

## 6. 📁 FILE STRUCTURE

```
.opencode/skills/workflows-documentation/
├── SKILL.md (overview + quick guidance)
├── references/
│   ├── core_standards.md (filename conventions, document types, violations)
│   ├── optimization.md (content optimization patterns)
│   ├── validation.md (quality assessment, gates, interpretation)
│   ├── workflows.md (execution modes, validation patterns, troubleshooting)
│   ├── skill_creation.md (skill creation workflow)
│   └── quick_reference.md (this file)
├── assets/
│   ├── frontmatter_templates.md (YAML frontmatter examples)
│   ├── command_template.md (slash command templates)
│   ├── llmstxt_templates.md (llms.txt generation examples)
│   ├── skill_md_template.md (SKILL.md file templates)
│   └── flowcharts/ (ASCII flowchart examples)
└── scripts/
    ├── extract_structure.py (document parsing → JSON for AI)
    ├── quick_validate.py (fast skill validation)
    ├── init_skill.py (skill scaffolding)
    └── package_skill.py (skill packaging)
```

---

## 7. 📊 CONTENT QUALITY QUICK GUIDE

**AI evaluates content for**:
- Clarity and completeness
- Practical usefulness (examples, workflows)
- AI-friendliness (scannable, question-answering format)
- Appropriate level of detail

**Quick Wins for Higher Ratings**:
1. Add complete examples (not just API references)
2. Combine concepts with practical usage
3. Answer "How do I..." questions directly
4. Make content scannable (clear headings, lists)

---

## 8. 🔗 INTEGRATION POINTS

**Validation Workflow**:
```
1. Run extract_structure.py → JSON output
2. AI evaluates checklist results + content quality
3. AI provides recommendations
4. Fix issues and re-extract
```

---

## 9. 🔗 RELATED RESOURCES

### Reference Files
- [core_standards.md](./core_standards.md) - Document type rules and structural requirements
- [validation.md](./validation.md) - Quality scoring and validation workflows
- [optimization.md](./optimization.md) - Content transformation patterns
- [workflows.md](./workflows.md) - Execution modes and workflows

### Templates
- [skill_md_template.md](../assets/skill_md_template.md) - SKILL.md file templates
- [frontmatter_templates.md](../assets/frontmatter_templates.md) - Frontmatter by document type
- [command_template.md](../assets/command_template.md) - Command file templates

### Related Skills
- `git-commit` - Git commit workflows
- `system-memory` - Context preservation
- `system-spec-kit` - Spec folder management

### External Resources
- [llms.txt specification](https://llmstxt.org/) - Official llms.txt spec
- [CommonMark](https://spec.commonmark.org/) - Markdown specification

---

**For complete documentation**: See [SKILL.md](../SKILL.md)