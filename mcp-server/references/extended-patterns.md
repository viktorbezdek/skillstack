# MCP Server Development - Extended Patterns & Examples

Detailed development workflow, Claude Code integration patterns, and complete reference listings extracted from the core skill.

## Development Workflow

### Phase 1: Research and Planning

1. **Study Agent-Centric Design Principles**
   - Design tools for AI agents, not just API wrappers
   - Build workflow-oriented tools that enable complete tasks
   - Optimize for limited context windows
   - Provide actionable error messages

2. **Study API Documentation**
   - Read all available API documentation for target service
   - Document authentication, rate limiting, pagination patterns
   - Identify most valuable endpoints to implement

3. **Create Implementation Plan**
   - List tools to implement (prioritize high-value workflows)
   - Plan shared utilities and helpers
   - Design input validation (Pydantic/Zod schemas)
   - Define response formats (JSON, Markdown options)

### Phase 2: Implementation

**Key Patterns:**
- Use service-prefixed tool names: `github_search_repos`, `slack_send_message`
- Support both JSON and Markdown response formats
- Implement pagination with `limit`, `offset`, `has_more`
- Set CHARACTER_LIMIT constant (typically 25,000 tokens)
- Provide actionable, LLM-friendly error messages
- Use async/await for all I/O operations
- Full type coverage (Python type hints, TypeScript types)

### Phase 3: Review and Testing

**Code Quality Checklist:**
- [ ] DRY Principle: No duplicated code between tools
- [ ] Composability: Shared logic extracted into functions
- [ ] Consistency: Similar operations return similar formats
- [ ] Error Handling: All external calls have error handling
- [ ] Type Safety: Full type coverage
- [ ] Documentation: Comprehensive docstrings/descriptions

**Important:** MCP servers are long-running processes. Never run directly - use:
- Evaluation harness (see Phase 4)
- tmux to keep outside main process
- `timeout 5s python server.py` for quick tests

### Phase 4: Create Evaluations

Evaluations test whether LLMs can effectively use your MCP server.

**Question Requirements:**
- Independent (not dependent on other questions)
- Read-only (only non-destructive operations)
- Complex (requiring multiple tool calls)
- Realistic (based on real use cases)
- Verifiable (single, clear answer)
- Stable (answer won't change over time)

**Run Evaluations:**
```bash
pip install -r scripts/evaluation/requirements.txt
export ANTHROPIC_API_KEY=your_api_key

python scripts/evaluation/evaluation.py \
  -t stdio \
  -c python \
  -a my_mcp_server.py \
  evaluation.xml
```

---

## Claude Code Integration

### Plugin Architecture

| Component | When to Use |
|-----------|-------------|
| **MCP Server** | External tool/service integration, stateful operations |
| **Skill** | Procedural workflows, domain knowledge, multi-step processes |
| **Slash Command** | Quick actions, command shortcuts |
| **Combination** | Complex plugins needing multiple interaction patterns |

### Creating Plugins

```bash
# Initialize Plugin
python scripts/init_plugin.py <plugin-name> --type <mcp|skill|command|full>

# Validate Plugin
python scripts/validate_plugin.py <plugin-path>

# Package Plugin
python scripts/package_plugin.py <plugin-path> [output-dir]
```

### Plugin Templates

Templates are available in `templates/`:
- `mcp-server-python/` - Python FastMCP server
- `mcp-server-typescript/` - TypeScript MCP server
- `mcp-template-python/` - Alternative Python template with tests
- `mcp-template-typescript/` - Alternative TypeScript template
- `skill/` - Skill template with references and scripts
- `slash-command/` - Slash command template
- `full-plugin/` - Complete plugin combining all components

---

## Using MCP Tools

### Gemini CLI (Primary Method)

```bash
# CRITICAL: Use stdin piping, NOT -p flag
echo "Search GitHub for MCP servers" | gemini -y -m gemini-2.5-flash
```

### Direct Script Execution

```bash
npx tsx scripts/mcp-tools/cli.ts call-tool memory create_entities '{"entities":[...]}'
npx tsx scripts/mcp-tools/cli.ts list-tools
```

---

## Complete Reference Files

### Core MCP Development

| File | Purpose |
|------|---------|
| `references/mcp-best-practices.md` | Universal MCP guidelines |
| `references/development-guidelines.md` | FastMCP Python patterns |
| `references/typescript-mcp-server.md` | TypeScript implementation |
| `references/building-servers.md` | Complete server development guide |
| `references/protocol-basics.md` | MCP protocol fundamentals |

### Python Specific

| File | Purpose |
|------|---------|
| `references/python-guide.md` | Complete Python/FastMCP guide |
| `references/mcp-development.md` | FastMCP development patterns |

### TypeScript Specific

| File | Purpose |
|------|---------|
| `references/typescript-guide.md` | Complete TypeScript guide |
| `references/sdk-patterns.md` | SDK usage patterns and examples |

### Production and Operations

| File | Purpose |
|------|---------|
| `references/production-checklist.md` | Pre-deployment validation |
| `references/community-practices.md` | Mid-2025+ patterns, .mcpb packaging |
| `references/api-comparison.md` | LLM provider comparison |
| `references/evaluation-guide.md` | Creating effective evaluations |

### Claude Code Integration

| File | Purpose |
|------|---------|
| `references/mcp_server_guide.md` | MCP server guide for plugins |
| `references/skill_guide.md` | Skill creation guide |
| `references/slash_command_guide.md` | Slash command guide |
| `references/architecture_patterns.md` | Plugin architecture patterns |
| `references/best_practices.md` | Plugin best practices |

### Claude Code Official Documentation

Complete Claude Code documentation is in `references/claude-code-docs/`:
- `mcp.md` - MCP integration guide
- `plugins.md`, `plugins-reference.md` - Plugin development
- `skills.md` - Skill authoring
- `hooks.md`, `hooks-guide.md` - Hooks implementation
- `settings.md` - Configuration reference
- And 35+ more official documentation files

### Figma Integration (Specialized)

For Figma MCP server development, see `references/figma-integration/`:
- `figma-mcp-tools.md` - Figma MCP server tools
- `w3c-dtcg-spec.md` - Design tokens specification
- `token-naming-conventions.md` - Token naming patterns

---

## Scripts

### Plugin Development

| Script | Purpose |
|--------|---------|
| `scripts/init_plugin.py` | Initialize new plugin scaffolding |
| `scripts/validate_plugin.py` | Validate plugin structure and quality |
| `scripts/package_plugin.py` | Create distributable plugin package |

### MCP Tools

| Script | Purpose |
|--------|---------|
| `scripts/mcp-tools/cli.ts` | CLI for calling MCP tools |
| `scripts/mcp-tools/mcp-client.ts` | MCP client implementation |

### Evaluation

| Script | Purpose |
|--------|---------|
| `scripts/evaluation/evaluation.py` | Evaluation harness |
| `scripts/evaluation/connections.py` | MCP connection utilities |
| `scripts/evaluation/example_evaluation.xml` | Example evaluation file |

### Utilities

| Script | Purpose |
|--------|---------|
| `scripts/update_docs.js` | Update Claude Code documentation |
| `scripts/cost-calculator.py` | Calculate LLM API costs |

### Figma Token Scripts

| Script | Purpose |
|--------|---------|
| `scripts/figma-tokens/extract_tokens.py` | Extract tokens from Figma |
| `scripts/figma-tokens/transform_tokens.py` | Transform to CSS/SCSS/JSON |
| `scripts/figma-tokens/validate_tokens.py` | Validate W3C compliance |
