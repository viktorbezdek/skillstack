# Commands Reference Library

This directory contains **reference material for creating and organizing Claude Code slash commands**. These are NOT deployed commands themselves, but rather templates, patterns, and procedural guides for command development.

## Purpose

The `commands/` directory serves as a knowledge base for:

- **Command Templates**: Standardized structures for creating new slash commands
- **Command Patterns**: Configuration defining command categories, workflows, and integration
- **Meta-Commands**: Guides for generating other commands using established patterns
- **Specialized Workflows**: Domain-specific command procedures (testing, development)

## Directory Structure

```text
commands/
├── development/                  # Development workflow commands
│   ├── config/
│   │   └── command-patterns.yml # Command categories, workflows, risk levels
│   ├── templates/
│   │   └── command-template.md  # Base template for new commands
│   ├── use-command-template.md  # Meta-command: generate commands from template
│   └── create-feature-task.md   # Structured feature development workflow
│
└── testing/                      # Testing workflow commands
    ├── analyze-test-failures.md  # Investigate test failures (bug vs test issue)
    ├── comprehensive-test-review.md
    └── test-failure-mindset.md
```

## Key Files

### Configuration

**[command-patterns.yml](./development/config/command-patterns.yml)**

Defines the organizational structure for commands:

- **Command Categories**: Analysis, Development, Quality, Documentation, Operations
- **Workflow Chains**: Multi-step processes (Feature Development, Bug Fix, Code Review)
- **Context Sharing**: What information flows between commands
- **Cache Patterns**: TTL and invalidation rules for different command types
- **Risk Assessment**: Classification of commands by risk level and required safeguards

### Templates

**[command-template.md](./development/templates/command-template.md)**

Standard structure for creating new commands:

- Purpose statement (single sentence)
- Task description with `$ARGUMENTS` placeholder
- Phased execution steps (Analysis → Implementation → Validation)
- Context preservation rules
- Expected output format
- Integration points (prerequisites, follow-ups, related commands)

### Meta-Commands

**[use-command-template.md](./development/use-command-template.md)**

Procedural guide for generating new commands:

1. Parse command purpose from `$ARGUMENTS`
2. Select appropriate category and naming convention
3. Apply template structure with customizations
4. Configure integration with workflow chains
5. Create command file in appropriate location

### Specialized Workflows

**[analyze-test-failures.md](./testing/analyze-test-failures.md)**

Critical thinking framework for test failure analysis:

- Balanced investigation approach (test bug vs implementation bug)
- Structured analysis steps
- Classification criteria (Test Bug | Implementation Bug | Ambiguous)
- Examples demonstrating reasoning patterns
- Output format for clear communication

**[create-feature-task.md](./development/create-feature-task.md)**

Structured approach to feature development:

- Requirement parsing and scope determination
- Task structure generation with phases
- Documentation creation and tracking setup
- Integration with development workflows

## Usage Patterns

### Creating a New Command

When you need to create a new slash command for Claude Code:

1. **Consult the patterns**: Review [command-patterns.yml](./development/config/command-patterns.yml) to understand:
   - Which category your command belongs to
   - Whether it fits into existing workflow chains
   - What risk level it represents

2. **Use the template**: Start with [command-template.md](./development/templates/command-template.md)
   - Replace placeholders with command-specific content
   - Customize execution steps for your use case
   - Define clear integration points

3. **Follow naming conventions**: Use verb-noun format
   - Analysis: `analyze-*`, `scan-*`, `validate-*`
   - Development: `create-*`, `implement-*`, `fix-*`
   - Operations: `deploy`, `migrate`, `cleanup-*`

4. **Deploy to proper location**: Actual slash commands live in:
   - User commands: `~/.claude/commands/`
   - Project commands: `.claude/commands/` (in project root)
   - NOT in this `references/commands/` directory

### Integrating Commands into Workflows

Commands are designed to chain together:

```yaml
Feature_Development:
  steps:
    - create-feature-task # Initialize structured task
    - study-current-repo # Understand codebase
    - implement-feature # Write code
    - create-test-plan # Design tests
    - comprehensive-test-review # Validate quality
    - gh-create-pr # Submit for review
```

Each command produces context that subsequent commands can use.

## Relationship to Skill Structure

This directory is part of the **python3-development** skill's reference material:

```text
python3-development/
├── SKILL.md                    # Skill entry point
├── references/
│   ├── commands/               # THIS DIRECTORY (reference material)
│   ├── modern-modules/         # Python library guides
│   └── ...
└── scripts/                    # Executable tools
```

**Important Distinctions**:

- **This directory** (`references/commands/`): Templates and patterns for creating commands
- **Deployed commands** (`~/.claude/commands/`): Actual slash commands that Claude Code executes
- **Skill scripts** (`scripts/`): Python tools that may be called by commands

## Best Practices

### When Creating Commands

1. **Single Responsibility**: Each command should focus on one clear task
2. **Clear Naming**: Use descriptive verb-noun pairs (`analyze-dependencies`, `create-component`)
3. **Example Usage**: Include at least 3 concrete examples
4. **Context Definition**: Specify what gets cached for reuse by later commands
5. **Integration Points**: Define prerequisites and natural follow-up commands

### When Organizing Commands

1. **Category Alignment**: Place commands in appropriate category subdirectories
2. **Workflow Awareness**: Consider how commands chain together
3. **Risk Classification**: Mark high-risk commands with appropriate safeguards
4. **Documentation**: Keep command patterns file updated with new additions

## Integration with Python Development Skill

Commands in this directory support the orchestration patterns described in:

- [python-development-orchestration.md](../references/python-development-orchestration.md)
- [reference-document-architecture.md](../planning/reference-document-architecture.md) (historical proposal, not implemented)

They complement the agent-based workflows:

```text
User Request
    ↓
Orchestrator (uses skill + commands)
    ↓
├─→ @agent-python-cli-architect (implementation)
├─→ @agent-python-pytest-architect (testing)
└─→ @agent-python-code-reviewer (review)
    ↓
Apply standards: /modernpython, /shebangpython (from commands)
```

## Common Workflows

### Feature Development

```bash
# 1. Create structured task
/development:create-feature-task Add user authentication with OAuth

# 2. Implement with appropriate agent
# (Orchestrator delegates to @agent-python-cli-architect)

# 3. Validate with standards
/modernpython src/auth/oauth.py
/shebangpython scripts/migrate-users.py
```

### Test Failure Investigation

```bash
# Analyze failures with critical thinking
/testing:analyze-test-failures test_authentication.py::test_oauth_flow
```

### Command Creation

```bash
# Generate new command from template
/development:use-command-template validate API endpoints for rate limiting
```

## Further Reading

- [Command Template](./development/templates/command-template.md) - Base structure for all commands
- [Command Patterns](./development/config/command-patterns.yml) - Organizational taxonomy
- [Python Development Orchestration](../references/python-development-orchestration.md) - How commands fit into workflows
