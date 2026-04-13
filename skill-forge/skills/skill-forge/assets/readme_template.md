# README Template

> Template for creating comprehensive, AI-optimized README files with consistent structure, progressive disclosure, and scannable content.

---

## TEMPLATE USAGE

**When to use this template**:
- Project documentation (root-level README)
- Component/module documentation
- Feature/system documentation
- Skill documentation (supplement to SKILL.md)

**How to use**:
1. Copy the template section below
2. Replace all `[PLACEHOLDER]` markers with actual content
3. Remove sections that don't apply (keep minimum: Overview, Quick Start, Usage)
4. Delete guidance comments (`<!-- ... -->`)
5. Adjust section numbers if you remove sections

**Section requirements by type**:

| Type | Required Sections | Optional Sections |
|------|------------------|-------------------|
| Project | 1-2, 7-9 | 3-6 |
| Component | 1-2, 4, 6-8 | 3, 5, 9 |
| Feature | 1-2, 4, 6-7 | 3, 5, 8-9 |
| Skill | 1-2, 4, 6-8 | 3, 5, 9 |

---

## TEMPLATE

```markdown
# [PROJECT_NAME]

> [One-sentence description of what this is and its primary purpose. Keep under 150 characters.]

---

## TABLE OF CONTENTS

<!-- Link format: #N--section-name (number + double-dash + lowercase-hyphenated) -->

- [1. 📖 OVERVIEW](#1--overview)
- [2. 🚀 QUICK START](#2--quick-start)
- [3. 📁 STRUCTURE](#3--structure)
- [4. ⚡ FEATURES](#4--features)
- [5. ⚙️ CONFIGURATION](#5--configuration)
- [6. 💡 USAGE EXAMPLES](#6--usage-examples)
- [7. 🛠️ TROUBLESHOOTING](#7--troubleshooting)
- [8. ❓ FAQ](#8--faq)
- [9. 📚 RELATED DOCUMENTS](#9--related-documents)

---

## 1. 📖 OVERVIEW

### What is [PROJECT_NAME]?

<!-- 2-3 sentences explaining what this is and why it exists -->

[Brief description of the project/component/feature and its primary purpose.]

### Key Statistics

<!-- Adjust columns based on what's relevant -->

| Category | Count | Details |
|----------|-------|---------|
| [Category 1] | [N] | [Brief detail] |
| [Category 2] | [N] | [Brief detail] |
| [Category 3] | [N] | [Brief detail] |

### Key Features

<!-- List 3-6 primary capabilities -->

| Feature | Description |
|---------|-------------|
| **[Feature 1]** | [What it does and why it matters] |
| **[Feature 2]** | [What it does and why it matters] |
| **[Feature 3]** | [What it does and why it matters] |

### Requirements

<!-- List prerequisites: runtime, dependencies, system requirements -->

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| [Runtime/Tool] | [Version] | [Version] |
| [Dependency] | [Version] | [Version] |

---

## 2. 🚀 QUICK START

<!-- Goal: Working setup in <2 minutes with copy-paste commands -->

### 30-Second Setup

```bash
# 1. [First step description]
[command]

# 2. [Second step description]
[command]

# 3. [Third step description]
[command]
```

### Verify Installation

```bash
# Confirm everything is working
[verification command]

# Expected output:
# [example output]
```

### First Use

<!-- Show the simplest possible usage example -->

```bash
# Basic usage
[minimal usage command or code]
```

---

## 3. 📁 STRUCTURE

<!-- ASCII tree showing directory/file organization -->

```
[root-directory]/
├── [dir-or-file-1]/          # [Purpose]
│   ├── [subitem-1]           # [Purpose]
│   └── [subitem-2]           # [Purpose]
├── [dir-or-file-2]/          # [Purpose]
│   ├── [subitem-1]           # [Purpose]
│   └── [subitem-2]           # [Purpose]
└── [dir-or-file-3]           # [Purpose]
```

### Key Files

| File | Purpose |
|------|---------|
| `[filename-1]` | [What it does] |
| `[filename-2]` | [What it does] |
| `[filename-3]` | [What it does] |

---

## 4. ⚡ FEATURES

### [Feature Category 1]

<!-- Group related features -->

**[Feature Name]**: [Description of what it does]

| Aspect | Details |
|--------|---------|
| **Purpose** | [Why this feature exists] |
| **Usage** | [How to use it] |
| **Options** | [Available options/flags] |

### [Feature Category 2]

**[Feature Name]**: [Description of what it does]

```bash
# Example usage
[command or code example]
```

### Feature Comparison

<!-- Optional: Compare options or approaches -->

| Feature | Option A | Option B | Option C |
|---------|----------|----------|----------|
| [Aspect 1] | [Value] | [Value] | [Value] |
| [Aspect 2] | [Value] | [Value] | [Value] |

---

## 5. ⚙️ CONFIGURATION

### Configuration File

<!-- Show config file location and format -->

**Location**: `[path/to/config.file]`

```[format]
# Example configuration
[key]: [value]
[key]: [value]
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `[option-1]` | [type] | `[default]` | [What it controls] |
| `[option-2]` | [type] | `[default]` | [What it controls] |
| `[option-3]` | [type] | `[default]` | [What it controls] |

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `[VAR_NAME]` | [Yes/No] | [What it controls] |
| `[VAR_NAME]` | [Yes/No] | [What it controls] |

---

## 6. 💡 USAGE EXAMPLES

### Example 1: [Use Case Name]

<!-- Start with the most common use case -->

```bash
# [Description of what this example does]
[command or code]
```

**Result**: [What happens / expected output]

### Example 2: [Use Case Name]

```bash
# [Description of what this example does]
[command or code]
```

### Example 3: [Advanced Use Case]

```bash
# [Description of what this example does]
[command or code]
```

### Common Patterns

| Pattern | Command/Code | When to Use |
|---------|--------------|-------------|
| [Pattern 1] | `[code]` | [Scenario] |
| [Pattern 2] | `[code]` | [Scenario] |

---

## 7. 🛠️ TROUBLESHOOTING

### Common Issues

#### [Issue 1: Descriptive Name]

**Symptom**: [What the user sees/experiences]

**Cause**: [Why this happens]

**Solution**:
```bash
# Fix command
[command]
```

#### [Issue 2: Descriptive Name]

**Symptom**: [What the user sees/experiences]

**Cause**: [Why this happens]

**Solution**: [Step-by-step fix instructions]

### Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| [Problem 1] | `[command or action]` |
| [Problem 2] | `[command or action]` |
| [Problem 3] | `[command or action]` |

### Diagnostic Commands

```bash
# Check status
[diagnostic command 1]

# View logs
[diagnostic command 2]

# Test connectivity/functionality
[diagnostic command 3]
```

---

## 8. ❓ FAQ

### General Questions

**Q: [Common question about what this is or does]?**

A: [Clear, concise answer. 2-3 sentences max.]

---

**Q: [Common question about usage]?**

A: [Clear, concise answer with example if helpful.]

---

**Q: [Common question about limitations or alternatives]?**

A: [Clear, concise answer.]

### Technical Questions

**Q: [Technical question about implementation]?**

A: [Answer with code example if applicable.]

```bash
# Example
[code]
```

---

**Q: [Technical question about integration]?**

A: [Answer explaining integration approach.]

---

## 9. 📚 RELATED DOCUMENTS

### Internal Documentation

| Document | Purpose |
|----------|---------|
| [Document Name](./path/to/doc.md) | [What it covers] |
| [Document Name](./path/to/doc.md) | [What it covers] |

### External Resources

| Resource | Description |
|----------|-------------|
| [Resource Name](https://url) | [What it provides] |
| [Resource Name](https://url) | [What it provides] |

---

*[Optional: Single-line footer with project tagline or maintainer info]*
```

---

## SECTION GUIDELINES

### Overview Section (1)

**Purpose**: Establish what this is, why it exists, and key metrics at a glance.

**Must include**:
- Brief description (2-3 sentences)
- Key statistics table (if metrics exist)
- Key features table (3-6 items)
- Requirements/prerequisites

**Writing tips**:
- Lead with value proposition
- Use tables for scannable data
- Keep descriptions action-oriented

### Quick Start Section (2)

**Purpose**: Get users to a working state in under 2 minutes.

**Must include**:
- Numbered setup steps with copy-paste commands
- Verification command to confirm success
- Simplest possible first use example

**Writing tips**:
- Test every command before documenting
- Show expected output for verification
- Assume nothing is installed

### Structure Section (3)

**Purpose**: Help users navigate the project/component.

**Must include**:
- ASCII directory tree
- Purpose annotations for key directories/files
- Key files table

**Writing tips**:
- Only show relevant structure (not every file)
- Annotate with `# Purpose` comments
- Group related items

### Features Section (4)

**Purpose**: Comprehensive feature documentation with examples.

**Must include**:
- Feature groupings by category
- Usage examples for each feature
- Options/flags tables where applicable

**Writing tips**:
- Group related features
- Show before/after or input/output
- Include comparison tables for alternatives

### Configuration Section (5)

**Purpose**: Complete configuration reference.

**Must include**:
- Config file location and format
- All options with types, defaults, descriptions
- Environment variables

**Writing tips**:
- Show complete example config
- Document all defaults
- Group related options

### Usage Examples Section (6)

**Purpose**: Real-world usage patterns users can copy.

**Must include**:
- 3+ examples from simple to advanced
- Common patterns table
- Expected results for each example

**Writing tips**:
- Start with most common use case
- Build complexity progressively
- Include output/results

### Troubleshooting Section (7)

**Purpose**: Self-service problem resolution.

**Must include**:
- Common issues with symptom/cause/solution
- Quick fixes table
- Diagnostic commands

**Writing tips**:
- Lead with user-visible symptoms
- Provide copy-paste solutions
- Include diagnostic commands

### FAQ Section (8)

**Purpose**: Answer frequently asked questions.

**Must include**:
- General questions (what/why)
- Technical questions (how)
- Bold Q: with A: format

**Writing tips**:
- Keep answers concise (2-3 sentences)
- Include code examples where helpful
- Use horizontal rules between Q&A pairs

### Related Documents Section (9)

**Purpose**: Guide users to additional resources.

**Must include**:
- Internal documentation links
- External resource links
- Purpose description for each

**Writing tips**:
- Use relative paths for internal docs
- Verify all links work
- Describe what each resource provides

---

## STYLE REFERENCE

### Emoji Usage

| Element | Rule | Example |
|---------|------|---------|
| H1 | Never | `# Project Name` |
| H2 | Always (numbered) | `## 1. 📖 OVERVIEW` |
| H3 | Never | `### Configuration` |
| H4+ | Never | `#### Options` |

### Formatting Conventions

| Element | Format |
|---------|--------|
| File paths | Backticks: \`path/to/file.md\` |
| Commands | Fenced code blocks with language |
| Options/flags | Backticks: \`--flag\` |
| Key terms | Bold: **term** |
| Variables | Backticks + caps: \`VAR_NAME\` |

### Section Numbering

- Always use `N. ` prefix before emoji
- Maintain sequential numbering
- Update TOC links when removing sections
- Link format: `#n--section-name`

---

## QUALITY CHECKLIST

Before finalizing README:

- [ ] All `[PLACEHOLDER]` markers replaced
- [ ] All commands tested and working
- [ ] All internal links verified
- [ ] TOC links match section headers
- [ ] No empty sections (remove if unused)
- [ ] Quick Start achievable in <2 minutes
- [ ] Code examples have language specified
- [ ] Tables are properly formatted
- [ ] Emoji only on H2 headings
