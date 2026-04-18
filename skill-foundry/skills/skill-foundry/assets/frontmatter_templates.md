# YAML Frontmatter Templates - Document Type Reference

Templates for adding missing YAML frontmatter to documents. Use these templates when the document-style-fixer needs to add frontmatter to non-compliant files.

---

## 1. 📋 SKILL.MD FRONTMATTER TEMPLATE

**Required Fields**: `name`, `description`, `allowed-tools`

**Template**:
```yaml
---
name: skill-name
description: Brief one-line description of what this skill does and when to use it
allowed-tools: Read, Write, Edit, Bash, Grep
---
```

**Field Guidelines**:

**`name`**:
- Format: `lowercase-with-hyphens`
- Should match directory name
- Example: `document-style-validator`, `git-commit`, `system-memory`

**`description`**:
- One to two sentences maximum
- Explains what the skill does
- Mentions key triggering conditions or use cases
- **MUST be on a single line after the colon** (see warning below)
- Example: "Validates markdown document structure against style guide requirements for SKILL.md, commands, knowledge files, and specs"

> **WARNING: YAML Multiline Strings Are Not Parsed**
>
> The skill parser does not handle YAML multiline block format. Keep your description on a single line after the colon.
>
> ```yaml
> # BAD - Will not be parsed correctly
> description:
>   This is my skill description
>   spanning multiple lines.
>
> # GOOD - Single line after colon
> description: This is my skill description all on one line.
> ```
>
> **Note**: Prettier and other formatters may auto-format long descriptions to multiline. If this happens, manually revert to single-line format.

**`allowed-tools`**:
- Comma-separated list of AI tools the skill can use
- Common tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch
- Order by frequency of use (most common first)
- Example: `Read, Write, Bash` or `Read, Grep, Bash, WebFetch`

**Complete Example**:
```yaml
---
name: code-systematic-debugging
description: Four-phase debugging framework for browser console errors, CSS layout issues, JavaScript animations, and Webflow-specific bugs
allowed-tools: Read, Bash, Grep
---
```

---

## 2. ⚙️ COMMAND FRONTMATTER TEMPLATE

**Required Fields**: `description`, `argument-hint`, `allowed-tools`

**Template**:
```yaml
---
description: Brief description of what this command does
argument-hint: [required_arg] [optional_arg]
allowed-tools: Read, Write, Bash
---
```

**Field Guidelines**:

**`description`**:
- One sentence explaining command purpose
- Focus on what it creates or generates
- Example: "Create new slash commands with standardized structure"

**`argument-hint`**:
- Shows command syntax with placeholders
- Square brackets for required args: `[required_arg]`
- Angle brackets for optional args: `<optional_arg>` OR square brackets with default notation
- Example: `[name] [purpose]` or `[name] <type>`

**`allowed-tools`**:
- Same as SKILL.md
- Common for commands: Read, Write, Bash, Grep
- Include tools needed to fulfill command's purpose

**Complete Example**:
```yaml
---
description: Generate properly structured command files with correct YAML frontmatter
argument-hint: [name] [purpose]
allowed-tools: Read, Write, Bash
---
```

---

## 3. 📚 KNOWLEDGE FILE FRONTMATTER

**Rule**: Knowledge files should **NOT** have YAML frontmatter.

**If present**: The fixer should **remove** frontmatter from knowledge files.

**Rationale**: Knowledge files are pure content documents. Frontmatter is for programmatic interfaces (skills, commands) that need metadata for execution.

**Fix Action**:
```yaml
# BEFORE (incorrect)
---
name: document-style-guide
description: Style guide for documentation
---

# Document Style Guide - Official Standards

Content...

# AFTER (correct)
# Document Style Guide - Official Standards

Content...
```

---

## 4. 📄 SPEC FILE FRONTMATTER

**Rule**: Spec files should **NOT** have YAML frontmatter.

**Alternative Metadata Format**:
Specs use inline metadata at the top (not YAML frontmatter):

```markdown
# Feature Name - Spec

**Date**: 2025-11-10
**Version**: 1.0
**Priority**: HIGH

Brief introduction...
```

**Rationale**: Specs evolve rapidly during planning. YAML frontmatter adds formality that slows iteration. Inline metadata is more flexible.

**If YAML frontmatter present**: Suggest removal (loose enforcement, not required).

---

## 5. 📖 README.MD FRONTMATTER

**Rule**: README files follow universal rules only. No specific frontmatter requirements.

**Common Practice**: README files typically don't use YAML frontmatter unless they're skill/command documentation.

**Exception**: If README.md is in `.opencode/skills/*/` directory and documents the skill, it might use skill-style frontmatter. However, the main SKILL.md should exist separately.

---

## 6. ✅ FRONTMATTER VALIDATION RULES

### Validation Logic

```python
def validate_frontmatter(file_path, doc_type):
    """
    Validate YAML frontmatter against document type requirements.

    Args:
        file_path: Path to markdown file
        doc_type: One of: SKILL, Command, Knowledge, Spec, README

    Returns:
        ValidationResult with errors/warnings
    """
    errors = []
    warnings = []

    # Read file content
    with open(file_path) as f:
        content = f.read()

    # Check frontmatter delimiters
    if not content.startswith('---\n'):
        if doc_type in ['SKILL', 'Command']:
            errors.append("Missing opening frontmatter delimiter (---)")
        else:
            # Knowledge/Spec shouldn't have frontmatter
            return ValidationResult(is_valid=True, errors=[], warnings=[])

    # Extract frontmatter block
    lines = content.split('\n')
    if lines[0] == '---':
        try:
            end_idx = lines[1:21].index('---') + 1  # Find closing within first 20 lines
            frontmatter_lines = lines[1:end_idx]
        except ValueError:
            errors.append("Missing closing frontmatter delimiter (---) within first 20 lines")
            return ValidationResult(is_valid=False, errors=errors, warnings=warnings)

    # Parse frontmatter fields
    frontmatter = {}
    for line in frontmatter_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    # Validate required fields by document type
    required_fields = {
        'SKILL': ['name', 'description', 'allowed-tools'],
        'Command': ['description', 'argument-hint', 'allowed-tools'],
        'Knowledge': [],  # No frontmatter required
        'Spec': [],       # No frontmatter required
        'README': []      # No frontmatter required
    }

    for field in required_fields.get(doc_type, []):
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")

    # Validate field formats
    if 'name' in frontmatter:
        if not re.match(r'^[a-z][a-z0-9-]*$', frontmatter['name']):
            errors.append("Field 'name' must be lowercase-with-hyphens format")

    if 'description' in frontmatter:
        if not frontmatter['description']:
            errors.append("Field 'description' cannot be empty")
        if len(frontmatter['description']) < 10:
            warnings.append("Field 'description' is very short (<10 chars)")

    if 'allowed-tools' in frontmatter:
        if not frontmatter['allowed-tools']:
            errors.append("Field 'allowed-tools' cannot be empty")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings
    )
```

### Validation Rules by Document Type

```yaml
validation_rules:
  SKILL:
    frontmatter_required: true
    required_fields:
      - name
      - description
      - allowed-tools
    optional_fields:
      - tags
      - category
      - version
    field_formats:
      name:
        pattern: "^[a-z][a-z0-9-]*$"
        description: "lowercase-with-hyphens"
        example: "code-systematic-debugging"
      description:
        min_length: 10
        max_length: 200
        description: "One to two sentences"
      allowed-tools:
        type: "comma-separated-list"
        description: "List of AI tools"

  Command:
    frontmatter_required: true
    required_fields:
      - description
      - argument-hint
      - allowed-tools
    optional_fields:
      - example
    field_formats:
      description:
        min_length: 10
        max_length: 100
      argument-hint:
        pattern: "^\\[[^\\]]+\\].*"
        description: "[required] <optional>"

  Knowledge:
    frontmatter_required: false
    action_if_present: "suggest_removal"

  Spec:
    frontmatter_required: false
    action_if_present: "suggest_removal"

  README:
    frontmatter_required: false
    action_if_present: "no_action"
```

---

## 7. 🤖 AUTO-GENERATION GUIDELINES

### Frontmatter Decision Logic

```
Document type detected?
├─> SKILL.md
│   ├─ Has frontmatter? → Validate fields
│   └─ Missing frontmatter? → Auto-generate + ask user to review
│
├─> Command
│   ├─ Has frontmatter? → Validate fields
│   └─ Missing frontmatter? → Auto-generate from H1 and INPUTS section
│
├─> Knowledge
│   ├─ Has frontmatter? → Suggest removal
│   └─ No frontmatter? → Valid (no action needed)
│
├─> Spec
│   ├─ Has frontmatter? → Suggest removal
│   └─ No frontmatter? → Valid (no action needed)
│
└─> README
    ├─ Has skill-style frontmatter? → Valid if in .opencode/skills/
    └─ No frontmatter? → Valid (no action needed)
```

### Field Inference Rules

```yaml
field_inference:
  name:
    source: "directory_name"
    method: "Extract parent directory name from file path"
    example:
      input: ".opencode/skills/my-skill/SKILL.md"
      output: "my-skill"
    python: |
      name = Path(file_path).parent.name

  description:
    sources:
      - "h1_subtitle"  # Primary
      - "first_paragraph"  # Fallback
    method: "Extract subtitle after ' - ' from H1, or use first paragraph"
    example:
      h1: "# My Skill - Brief Description"
      output: "Brief Description"
    python: |
      # From H1 subtitle
      h1_line = re.search(r'^# [^-]+ - (.+)$', content, re.MULTILINE)
      if h1_line:
          description = h1_line.group(1)
      else:
          # From first paragraph
          lines = content.split('\n')
          h1_idx = next(i for i, line in enumerate(lines) if line.startswith('# '))
          description = lines[h1_idx + 2]  # Skip blank line after H1

  argument_hint:
    source: "inputs_section"
    method: "Extract from Required/Optional Inputs sections"
    example:
      input: |
        ### Required Inputs
        - `name`: Skill name
        - `type`: Skill type
        ### Optional Inputs
        - `version`: Version number
      output: "[name] [type] <version>"
    python: |
      required = re.findall(r'### Required Inputs.*?^- `([^`]+)`', content, re.DOTALL | re.MULTILINE)
      optional = re.findall(r'### Optional Inputs.*?^- `([^`]+)`', content, re.DOTALL | re.MULTILINE)
      argument_hint = ' '.join([f'[{r}]' for r in required] + [f'<{o}>' for o in optional])

  allowed_tools:
    source: "workflow_section"
    method: "Extract tool names from WORKFLOW examples"
    example:
      workflow_content: |
        ```python
        Read("file.md")
        Write("output.md", content)
        Bash("ls -la")
        ```
      output: "Read, Write, Bash"
    python: |
      tool_pattern = r'\b(Read|Write|Edit|Bash|Grep|Glob|WebFetch)\('
      tools = list(set(re.findall(tool_pattern, content)))
      allowed_tools = ', '.join(sorted(tools))
```

---

## 8. 💬 INTERACTIVE FRONTMATTER ADDITION

### Approval Flow

**Step 1: Present Template**
```
STRUCTURAL FIX: Add YAML Frontmatter

File: .opencode/skills/new-skill/SKILL.md
Type: SKILL.md (frontmatter required)

Proposed frontmatter (inferred from document):
---
name: new-skill
description: Brief description inferred from H1 subtitle
allowed-tools: Read, Write, Bash
---

Options:
1. Accept as-is
2. Edit values before applying
3. Skip (leave non-compliant)

Choice:
```

**Step 2: If Edit Selected**
```
Edit frontmatter values:

name [new-skill]: _
description [Brief description...]: _
allowed-tools [Read, Write, Bash]: _

Press Enter to keep default, or type new value.
```

**Step 3: Apply**
```bash
# Insert at beginning of file
{
  echo "---"
  echo "name: $name"
  echo "description: $description"
  echo "allowed-tools: $allowed_tools"
  echo "---"
  echo ""
  cat original_file.md
} > updated_file.md
```

---

## 9. 🔧 FRONTMATTER CORRECTION

### ️ Fixing Incomplete Frontmatter

**Missing Fields**:
```yaml
# BEFORE (missing allowed-tools)
---
name: my-skill
description: My skill description
---

# FIX: Add missing field
---
name: my-skill
description: My skill description
allowed-tools: Read, Write, Bash
---
```

**Incorrect Format**:
```yaml
# BEFORE (wrong format)
---
Name: my-skill  # Should be lowercase
desc: Description  # Should be 'description'
tools: Read  # Should be 'allowed-tools'
---

# FIX: Correct field names
---
name: my-skill
description: Description
allowed-tools: Read
---
```

**Malformed Delimiters**:
```yaml
# BEFORE (missing closing delimiter)
---
name: my-skill
description: Description
allowed-tools: Read

# FIX: Add closing delimiter
---
name: my-skill
description: Description
allowed-tools: Read
---
```

---

## 10. 🎯 QUICK REFERENCE

### Frontmatter Decision Tree

```
Document type?
├─> SKILL.md       → MUST have frontmatter (name, description, allowed-tools)
├─> Command        → MUST have frontmatter (description, argument-hint, allowed-tools)
├─> Knowledge      → MUST NOT have frontmatter (remove if present)
├─> Spec           → SHOULD NOT have frontmatter (suggest removal)
└─> README         → No specific requirement (usually none)
```

### Field Requirements

| Document Type | name        | description | argument-hint | allowed-tools |
| ------------- | ----------- | ----------- | ------------- | ------------- |
| **SKILL.md**  | ✅ Required  | ✅ Required  | ❌ N/A         | ✅ Required    |
| **Command**   | ❌ N/A       | ✅ Required  | ✅ Required    | ✅ Required    |
| **Knowledge** | ❌ Forbidden | ❌ Forbidden | ❌ Forbidden   | ❌ Forbidden   |
| **Spec**      | ❌ Not used  | ❌ Not used  | ❌ Not used    | ❌ Not used    |

### ️ Common Mistakes

1. **Knowledge file with frontmatter** → Remove it
2. **SKILL.md missing `name` field** → Add with directory name
3. **Command missing `argument-hint`** → Infer from INPUTS or ask user
4. **Spec with YAML frontmatter** → Suggest inline metadata instead
5. **Wrong field names** → Correct to standard names (name, description, etc.)

---

## 11. 🔗 RELATED RESOURCES

### Templates
- [skill_md_template.md](./skill_md_template.md) - SKILL.md file templates
- [command_template.md](./command_template.md) - Command file templates

### Standards
- [core-standards.md](../references/core-standards.md) - Document type rules
