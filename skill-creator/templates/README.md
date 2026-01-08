# Skill Templates

This directory contains templates for creating new skills following Anthropic skill standards.

## Available Templates

### skill-skeleton (Universal Template - Default)

**Recommended for:** Complex skills needing optional sections (Known Issues, Configuration Files, Advanced Topics, etc.)

**Universal approach benefits:**
- **Eliminates decision fatigue** - Start comprehensive, delete what you don't need
- **Reduces maintenance** - One comprehensive template to update
- **Easier customization** - All sections available, remove as needed
- **Consistent structure** - All skills follow the same pattern

### minimal-skeleton (Simplified Template)

**Recommended for:** Simple skills with straightforward workflows

**Benefits:**
- **Less intimidating** - Core sections only (Quick Start, Critical Rules, Common Patterns)
- **Faster setup** - No optional sections to delete
- **Lower barrier** - Perfect for first-time builders or simple skills

**When to choose:**
- Skill has clear, linear workflow
- No need for scripts/references/assets
- Quick Start section is sufficient
- Want minimal structure to customize

### How It Works

**For skill-skeleton (universal template):**
1. **Initialize from template** using `init_skill.py --template skill-skeleton`
2. **Fill in all [TODO:] markers** with your content
3. **Delete sections you don't need** - Each section is marked as CORE or optional
4. **Customize remaining sections** for your specific skill

**For minimal-skeleton (simplified template):**
1. **Initialize from template** using `init_skill.py --template minimal-skeleton`
2. **Fill in all [TODO:] markers** with your content
3. **Add sections as needed** - Start minimal, expand only if required
4. **Customize for your specific skill**

### Section Markers

The template uses HTML comments to indicate which sections are required vs optional:

- **`<!-- CORE SECTION - Keep for all skills -->`** - Required for all skills
- **`<!-- DELETE if ... -->`** - Optional, delete if condition applies

### Required Sections (CORE)

These sections should be kept for all skills:

- **Quick Start** - How to use the skill in <5 minutes
- **Critical Rules** - Always Do / Never Do patterns
- **Common Patterns** - At least one pattern example

### Optional Sections (DELETE if not needed)

Delete these sections if they don't apply:

- **Known Issues Prevention** - Only if your skill prevents specific documented issues
- **Configuration Files Reference** - Only if your skill uses config files
- **Using Bundled Resources** - Only if you have scripts/, references/, or assets/
- **Advanced Topics** - Only for complex skills needing deep dives
- **Dependencies** - Only if your skill has dependencies
- **Package Versions** - Only if your skill uses packages with versions
- **Production Example** - Only if you have production evidence
- **Troubleshooting** - Only if your skill has common issues
- **Complete Setup Checklist** - Only if your skill needs a setup checklist
- **The X-Step Setup Process** - Only if Quick Start isn't sufficient

## Usage

### Initialize a New Skill

```bash
# Basic initialization
python scripts/init_skill.py my-skill-name --path <path> --template skill-skeleton

# With auto-fill (replaces [TODO: ...] placeholders automatically)
python scripts/init_skill.py my-skill-name --path <path> --template skill-skeleton --auto-fill

# With research log creation
python scripts/init_skill.py my-skill-name --path <path> --template skill-skeleton --create-research-log

# Full workflow: auto-fill + research log
python scripts/init_skill.py my-skill-name --path <path> --template skill-skeleton \
  --auto-fill --create-research-log
```

### Customization Workflow

1. **Fill in [TODO:] markers** - Replace all placeholders with actual content
2. **Delete optional sections** - Remove sections marked with `<!-- DELETE if ... -->`
3. **Customize core sections** - Adjust Quick Start, Critical Rules, and Patterns
4. **Add resources** - Create scripts/, references/, or assets/ as needed
5. **Validate** - Run `python scripts/validate_skill.py --full-check <skill-dir>`

## Examples

### Simple Skill (Instruction-Only)

**Keep:**
- Quick Start
- Critical Rules
- Common Patterns (1-2 patterns)

**Delete:**
- Known Issues Prevention
- Configuration Files Reference
- Using Bundled Resources
- Advanced Topics
- Dependencies
- Package Versions
- Production Example
- Troubleshooting
- Complete Setup Checklist
- The X-Step Setup Process

### Complex Skill (Multi-Phase Workflow)

**Keep:**
- Quick Start
- The X-Step Setup Process
- Critical Rules
- Common Patterns
- Known Issues Prevention (if applicable)
- Configuration Files Reference (if applicable)
- Using Bundled Resources (if applicable)
- Advanced Topics
- Dependencies
- Troubleshooting

**Delete:**
- Production Example (if no evidence)
- Complete Setup Checklist (if not needed)

### Skill with Resources

**Keep:**
- Quick Start
- Critical Rules
- Common Patterns
- Using Bundled Resources (document your scripts/references/assets)

**Delete:**
- Sections that don't apply based on your skill's complexity

## Template Structure

```
skill-skeleton/
├── SKILL.md              # Main skill documentation template
├── README.md             # README template (quick reference)
├── scripts/              # Example scripts directory
│   └── example-script.sh
├── references/           # Example references directory
│   ├── example-reference.md
│   ├── reference-template.md
│   └── BEST_PRACTICES.md
└── templates/            # Example templates directory (if needed)
```

## Customization Tips

### For Simple Skills

1. Delete the "X-Step Setup Process" section (Quick Start is enough)
2. Keep only 1-2 patterns in Common Patterns
3. Delete all optional sections
4. Focus on concise, actionable instructions

### For Complex Skills

1. Keep the "X-Step Setup Process" for detailed workflows
2. Add multiple patterns in Common Patterns
3. Keep Known Issues Prevention if you prevent specific errors
4. Add Advanced Topics for deep dives
5. Document all dependencies and package versions

### For Skills with Resources

1. Keep "Using Bundled Resources" section
2. Document each script, reference, and asset clearly
3. Explain when Claude should load references
4. Provide usage examples for scripts

## Archived Templates

Previous template variants have been archived to `archive/` directory. See `archive/README.md` for details.

The universal `skill-skeleton` template replaces all previous variants and provides a single, comprehensive starting point for all skills.

## Further Reading

- **Main Guide**: [SKILL.md](../SKILL.md) - Complete skill creation process
- **Quick Workflow**: [QUICK_WORKFLOW.md](../QUICK_WORKFLOW.md) - 5-minute workflow
- **Best Practices**: [references/best_practices_checklist.md](../references/best_practices_checklist.md)
- **Core Principles**: [references/core_principles.md](../references/core_principles.md)

---

**Remember**: Start comprehensive, delete what you don't need. It's easier to remove sections than to remember what to add.
