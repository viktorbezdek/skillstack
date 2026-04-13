# MCP Server

> **v1.2.20** | Development | 23 iterations

> Build production-grade MCP (Model Context Protocol) servers in Python or TypeScript -- tool design, validation, security, evaluation testing, and Claude Code plugin packaging.

## The Problem

MCP (Model Context Protocol) is the standard for connecting AI agents to external tools and data sources, but building a quality MCP server is harder than it looks. The protocol specification covers the wire format but not the design decisions that determine whether an agent can actually use the tools effectively. Developers build servers that technically implement the protocol but produce tools with vague descriptions, inconsistent parameter names, missing validation, unhelpful error messages, and no pagination -- resulting in agents that waste turns trying to understand what the tools do and how to call them.

The gap between "MCP server that compiles" and "MCP server that agents use well" is substantial. Tool descriptions need to be optimized for AI comprehension, not human reading. Parameters need constraints that prevent the agent from constructing invalid requests. Error messages need to tell the agent what to do next, not just what went wrong. Output needs to be truncated to fit context windows, paginated for large result sets, and formatted for agent consumption. These requirements are not documented in the MCP spec -- they are learned through trial and error with real agent workloads.

For Claude Code plugin developers, the challenge extends further. A plugin is not just an MCP server -- it includes skills (SKILL.md files with frontmatter and methodology), hooks (event-driven scripts), references (progressive disclosure depth), evaluations (trigger and output quality tests), and packaging (plugin.json manifest). Building a well-structured plugin requires knowledge that spans protocol implementation, agent-centric design, and the Claude Code extension system.

## The Solution

This plugin provides comprehensive guidance for building MCP servers and Claude Code plugins. It covers the complete development lifecycle: MCP protocol fundamentals (tools, resources, prompts, transports), server implementation in Python (FastMCP) and TypeScript (@modelcontextprotocol/sdk), agent-centric tool design (workflow-oriented tools, AI-optimized descriptions, context-window-aware output), input validation (Pydantic/Zod with constraints), security patterns (path sanitization, destructive operation confirmations), evaluation-driven development (trigger evals and output quality tests), production deployment, and Claude Code plugin packaging.

The plugin ships one SKILL.md with the core methodology, 72 reference files organized across protocol basics, language-specific guides, best practices, architecture patterns, Claude Code documentation, Figma integration, and community practices. It includes 8 project templates (MCP servers in Python and TypeScript, Claude Code skills, plugins, and slash commands), 10+ scripts for plugin initialization, validation, packaging, evaluation, and cost calculation, and an asset file with MCP tool definitions. The reference collection includes the complete Claude Code documentation (36 files covering everything from quickstart to advanced configuration) for building plugins that integrate deeply with the Claude Code ecosystem.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Tool descriptions are human-readable but confusing to agents; agents waste turns guessing what tools do | Agent-centric tool design with descriptions optimized for AI comprehension, including examples and constraints |
| No input validation; agents construct invalid requests and get cryptic errors | Pydantic/Zod validation with Field constraints that guide agents to valid parameter ranges |
| Error messages say "invalid input" with no guidance | Actionable error messages that tell the agent exactly what to fix: "fileId required, use search_files to find it" |
| Large result sets dump everything into context, exceeding window limits | CHARACTER_LIMIT enforcement (25K default) with pagination and truncation indicators |
| Plugin structure is guessed from examples; missing frontmatter, broken eval format, invalid manifest | Templates and validation scripts enforce correct structure for SKILL.md, plugin.json, evals, and references |
| No way to test if the agent actually triggers the right skill or produces quality output | Evaluation framework with trigger evals (does the agent pick the right skill?) and output evals (is the response good?) |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install mcp-server@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention MCP, Model Context Protocol, FastMCP, MCP server, MCP tools, Claude Code plugins, or building agent tools with MCP.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Build an MCP server in Python that exposes a search tool for our product database`
4. Claude produces a FastMCP server with a properly described search tool, Pydantic validation, pagination, and a CHARACTER_LIMIT for output
5. Next, try: `Package this as a Claude Code plugin with trigger evaluations`

---

## System Overview

```
User prompt (build MCP server / create plugin / design tools)
        |
        v
+------------------+     +-------------------------------+
|  mcp-server      |---->| Topic routing                  |
|  skill (SKILL.md)|     | (language, component, concern) |
+------------------+     +-------------------------------+
        |                         |
        v                         v
  Core concepts:           72 Reference files:
  - Tools, Resources,      - Protocol basics (3)
    Prompts                 - Python guide (FastMCP)
  - STDIO/HTTP/SSE         - TypeScript guide
    transports              - Best practices (3)
  - Agent-centric design    - Architecture patterns
        |                   - Claude Code docs (36)
        v                   - Figma integration (6)
  Implementation:           - SDK patterns
  - Python (FastMCP)        - Community practices
  - TypeScript (SDK)        - Evaluation guide
  - Plugin packaging        - Production checklist
        |                   - ...and more
        v
  Automation:             8 Project Templates:
  - init_plugin.py         - MCP server (Python)
  - validate_plugin.py     - MCP server (TypeScript)
  - package_plugin.py      - Claude Code skill
  - evaluation scripts     - Full plugin
  - cost-calculator.py     - Slash command
  - mcp-tools CLI          - Figma tokens
```

Single-skill plugin with 72 references, 10+ scripts, 8 templates, and 1 asset file. The largest knowledge base in SkillStack, covering the full MCP and Claude Code plugin ecosystem.

## What's Inside

| Component | Type | Count | What It Provides |
|---|---|---|---|
| **mcp-server** | Skill | 1 | Core methodology, language selection, quick starts, best practices |
| **References** | Reference | 72 | Protocol, implementation guides, best practices, Claude Code docs, Figma integration |
| **Scripts** | Script | 10+ | Plugin init, validation, packaging, evaluation, cost calculation, MCP client tools |
| **Templates** | Template | 8 | Project starters for MCP servers, plugins, skills, and commands |
| **Assets** | Asset | 1 | `tools.json` -- MCP tool definitions reference |
| **trigger-evals** | Eval | 13 | 8 positive, 5 negative trigger eval cases |
| **output-evals** | Eval | 3 | Output quality eval cases |

### Component Spotlights

#### mcp-server (skill)

**What it does:** Activates when you build MCP servers, design agent tools, create Claude Code plugins, or work with the Model Context Protocol. Provides the implementation approach for your chosen language (Python/TypeScript), agent-centric tool design patterns, and the full Claude Code plugin structure.

**Input -> Output:** You describe what you want to build (an MCP server, a tool, a plugin) -> The skill produces production-ready code with proper validation, error handling, security, and plugin packaging.

**When to use:**
- Building new MCP servers from scratch (Python or TypeScript)
- Integrating external APIs or services as MCP tools
- Creating Claude Code plugins (skills, hooks, references, evals)
- Designing tools optimized for AI agent consumption
- Writing evaluations to test MCP server quality
- Implementing security, caching, or production patterns

**When NOT to use:**
- Designing tool interfaces or tool consolidation patterns -> use [tool-design](../tool-design/)
- Prompt engineering or prompt optimization -> use [prompt-engineering](../prompt-engineering/)
- Agent coordination patterns -> use [multi-agent-patterns](../multi-agent-patterns/)

**Try these prompts:**

```
Build a FastMCP server that wraps our REST API with tools for search, create, and update operations
```

```
Create a Claude Code plugin with a skill that helps users design database schemas -- include trigger evals and references
```

```
Design an MCP tool for file management with proper path validation, destructive operation confirmation, and pagination for directory listings
```

```
Convert my existing Python script into an MCP server with proper tool descriptions and Zod/Pydantic validation
```

```
Set up evaluation tests for my MCP server -- I need trigger evals to verify the skill activates correctly and output evals for response quality
```

**Key reference categories:**

| Category | Files | Topics |
|---|---|---|
| Protocol | 3 | Protocol basics, API comparison, using tools |
| Language guides | 3 | Python (FastMCP), TypeScript (SDK), SDK patterns |
| Best practices | 3 | Tool design, MCP-specific, development guidelines |
| Architecture | 2 | Architecture patterns, building servers |
| Claude Code docs | 36 | Complete Claude Code documentation (plugins, hooks, skills, settings, deployment) |
| Figma integration | 6 | Figma MCP tools, token extraction, naming conventions |
| Production | 2 | Production checklist, evaluation guide |
| Community | 2 | Community practices, example projects |
| Prompts/Templates | 2 | Prompt templates, extended patterns |

#### Scripts (automation tools)

| Script | What It Does |
|---|---|
| `init_plugin.py` | Initialize a new Claude Code plugin project with correct structure |
| `validate_plugin.py` | Validate plugin structure, manifest, frontmatter, and eval format |
| `package_plugin.py` | Package a plugin for distribution |
| `cost-calculator.py` | Calculate token costs for MCP tool usage |
| `evaluation/` | Evaluation framework for testing MCP server quality |
| `mcp-tools/` | CLI for connecting to and testing MCP servers |
| `figma-tokens/` | Extract, transform, and validate design tokens from Figma |
| `update_docs.js` | Update documentation from source files |

#### Templates (project starters)

| Template | Language | What It Creates |
|---|---|---|
| `mcp-server-python/` | Python | FastMCP server with tools, resources, and tests |
| `mcp-server-typescript/` | TypeScript | MCP SDK server with Zod validation |
| `mcp-template-python/` | Python | Minimal MCP server template with test scaffolding |
| `mcp-template-typescript/` | TypeScript | Minimal MCP server template |
| `full-plugin/` | -- | Complete Claude Code plugin with skill, references, evals |
| `skill/` | -- | Standalone skill with references and example script |
| `slash-command/` | -- | Slash command template for Claude Code |
| `figma-tokens/` | -- | Design token pipeline templates (CSS, SCSS, TS, JSON) |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Build an MCP server" | "Build a FastMCP server in Python that wraps our PostgreSQL database with search, read, and update tools" |
| "Make a plugin" | "Create a Claude Code plugin with a skill for API design, including 5 trigger evals and 3 references on REST best practices" |
| "Add validation" | "Add Pydantic validation to my search tool -- query (string, 1-500 chars), limit (int, 1-100, default 10), and format (enum: json/markdown)" |
| "Fix my MCP server" | "My MCP tool returns 50K tokens for large queries. Add CHARACTER_LIMIT truncation and pagination with cursor-based navigation." |
| "Make it secure" | "Add path validation to my file_read tool -- restrict to the project directory, reject symlinks outside the sandbox, and require confirmation for destructive operations" |

### Structured Prompt Templates

**For MCP server creation:**
```
Build an MCP server in [Python/TypeScript]. It should wrap [service/API/database] with tools for [operations]. Transport: [STDIO/HTTP]. Key requirements: [validation, pagination, security, caching].
```

**For Claude Code plugin creation:**
```
Create a Claude Code plugin for [domain]. The skill should help users [capability]. Include: [number] references covering [topics], trigger evals for [number] positive and [number] negative cases, and output evals for [quality criteria].
```

**For tool design:**
```
Design MCP tools for [domain]. I have these operations: [list]. For each tool: name it with the service prefix convention, write an agent-optimized description, add input validation with constraints, and handle errors with actionable messages.
```

### Prompt Anti-Patterns

- **Wrapping API endpoints 1:1 as tools:** "Create one tool for each REST endpoint" -- the skill will push back toward workflow-oriented tools that combine multiple endpoints into meaningful agent operations.
- **Skipping validation:** "Just make it work first, we'll add validation later" -- validation is not optional for MCP tools because agents will construct invalid requests and get stuck in retry loops.
- **Ignoring output size:** "Return the full database query result" -- the skill enforces CHARACTER_LIMIT (25K default) and will add truncation and pagination automatically.

## Real-World Walkthrough

You are building an MCP server that gives Claude access to your company's project management tool. The tool has a REST API with endpoints for projects, tasks, comments, and users. You want Claude to be able to search tasks, create tasks, update task status, and add comments.

**Step 1: Language selection.** You ask Claude: **"Build an MCP server for our project management API. We're a Python shop using FastAPI."**

Claude activates the mcp-server skill and selects the Python (FastMCP) path. It produces a server skeleton:

```python
from fastmcp import FastMCP
from pydantic import Field
from typing import Annotated

mcp = FastMCP("project-manager")
```

**Step 2: Tool design.** Instead of wrapping each REST endpoint as a separate tool, Claude designs workflow-oriented tools. Rather than `list_tasks` + `get_task` + `list_comments` (three tools for one workflow), it creates:

- `search_tasks` -- Search by query, assignee, status, or project. Returns paginated results with CHARACTER_LIMIT truncation.
- `manage_task` -- Create or update a task. Uses a `confirm` flag for destructive operations (status changes, deletion).
- `add_comment` -- Add a comment to a task with the user's identity.

Each tool has an agent-optimized description that includes examples:

```python
@mcp.tool()
def search_tasks(
    query: Annotated[str, Field(description="Search terms or task ID. Example: 'auth bug' or 'PROJ-142'")],
    status: Annotated[str | None, Field(description="Filter: open, in_progress, done, blocked")] = None,
    assignee: Annotated[str | None, Field(description="Email of the assigned user")] = None,
    limit: Annotated[int, Field(ge=1, le=50, description="Max results")] = 10,
) -> dict:
    """Search tasks across all projects. Returns title, status, assignee, and last update.
    Use this to find tasks before calling manage_task or add_comment."""
```

**Step 3: Validation and error handling.** Claude adds Pydantic validation with constraints (limit between 1-50, status must be one of the enum values) and actionable error messages:

```python
# Instead of: "Invalid status"
# Returns: "Invalid status 'pending'. Valid values: open, in_progress, done, blocked"
```

**Step 4: Plugin packaging.** You then ask: **"Package this as a Claude Code plugin."**

Claude creates the full plugin structure:
- `.claude-plugin/plugin.json` -- Manifest with name, version, description, keywords
- `skills/project-manager/SKILL.md` -- Skill with frontmatter trigger description, methodology, when to use/not use
- `skills/project-manager/references/api-patterns.md` -- Reference for project management API patterns
- `skills/project-manager/evals/trigger-evals.json` -- 8 positive, 5 negative trigger eval cases
- `skills/project-manager/evals/evals.json` -- 3 output quality eval cases

**Step 5: Evaluation.** Claude runs `validate_plugin.py` to check the structure, verifies the trigger evals cover the activation keywords, and confirms the output evals test for the key quality criteria (correct tool selection, parameter validation, response format).

You now have a production-ready MCP server wrapped in a Claude Code plugin, with proper tool design, validation, error handling, and evaluation tests.

## Usage Scenarios

### Scenario 1: Building an MCP server for a database

**Context:** You have a PostgreSQL database with customer data. You want Claude to be able to search customers, view order history, and generate reports.

**You say:** "Build a FastMCP server that connects to our PostgreSQL database. Tools for: search customers, get order history, and generate monthly revenue report."

**The skill provides:**
- FastMCP server with three workflow-oriented tools
- Pydantic validation for all inputs (search query, customer ID, date ranges)
- SQL injection prevention through parameterized queries
- CHARACTER_LIMIT on output with pagination for order history
- Connection pooling setup for production

**You end up with:** A production-ready MCP server that Claude can use to query your database safely, with proper validation preventing harmful queries.

### Scenario 2: Creating a Claude Code plugin for a domain specialty

**Context:** You have deep expertise in GraphQL API design and want to package it as a Claude Code plugin that other developers can install.

**You say:** "Create a Claude Code plugin for GraphQL API design. It should cover schema design, resolver patterns, error handling, and N+1 query prevention."

**The skill provides:**
- Plugin structure with `plugin.json` manifest
- SKILL.md with frontmatter triggers for GraphQL-related queries
- 4 reference files covering each topic with methodology and examples
- Trigger evals testing activation on GraphQL prompts
- Output evals testing quality of schema design advice

**You end up with:** A distributable Claude Code plugin that any developer can install to get GraphQL expertise in their Claude Code sessions.

### Scenario 3: Converting an existing script to an MCP server

**Context:** You have a Python script that interacts with Jira. You want to make it available to Claude as MCP tools.

**You say:** "Convert my Jira integration script into an MCP server. The script has functions for: search issues, create issue, transition issue, and add comment."

**The skill provides:**
- FastMCP wrapper around existing functions with proper type hints
- Agent-optimized tool descriptions (not just the function docstrings)
- Input validation added to each function (issue key format, required fields)
- Configuration for Claude Desktop's `.mcp.json`
- Error handling that converts Jira API errors into actionable agent messages

**You end up with:** An MCP server that exposes your existing Jira integration as agent-ready tools, with minimal code changes to the original script.

---

## Decision Logic

The skill routes your request based on what you are building:

| You are building... | Primary guidance | Key references |
|---|---|---|
| MCP server in Python | FastMCP implementation | python-guide, best-practices, protocol-basics |
| MCP server in TypeScript | SDK implementation | typescript-guide, sdk-patterns, typescript-mcp-server |
| Claude Code plugin | Plugin structure and packaging | claude-code-docs/plugins, skill_guide, slash_command_guide |
| Agent-optimized tools | Tool design patterns | best_practices, architecture_patterns, using-tools |
| Evaluations for a plugin | Eval framework | evaluation-guide, claude-code-docs/plugins-reference |
| Figma-to-code integration | Token pipeline | figma-integration/* (6 files) |

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Tool descriptions too vague for agents | Agent calls the wrong tool or passes wrong parameters | Rewrite descriptions with the agent as the audience: include examples, constraints, and "use this when..." guidance |
| No CHARACTER_LIMIT on output | Large results flood the agent's context window, degrading subsequent responses | Add `CHARACTER_LIMIT = 25000` with truncation indicator: "Results truncated. Use offset/limit to page through." |
| Plugin.json manifest invalid | Plugin fails to install with cryptic error | Run `validate_plugin.py` before packaging; check required fields (name, version, description) |
| Trigger evals too narrow | Skill activates on exact phrases but misses natural language variations | Write evals that cover natural language: "help me build an MCP server" not just "create MCP server" |
| MCP server crashes on invalid input | Agent retries the same invalid request in a loop | Add validation with Pydantic/Zod that returns the valid range/format in the error message |

## Ideal For

- **Backend developers** building MCP servers that connect AI agents to internal tools, databases, and APIs
- **Plugin authors** creating Claude Code plugins for distribution (skills, references, hooks, evals)
- **Tool designers** who need to make existing APIs or scripts agent-friendly through proper MCP wrapping
- **Platform teams** establishing MCP server standards and templates for their organization
- **Full-stack developers** who need to build both the MCP server and the Claude Code plugin that packages it

## Not For

- **Designing tool interfaces abstractly** (consolidation patterns, tool naming theory) -- use [tool-design](../tool-design/)
- **Prompt engineering** for the tools themselves -- use [prompt-engineering](../prompt-engineering/)
- **Agent coordination** (how multiple agents use MCP tools together) -- use [multi-agent-patterns](../multi-agent-patterns/)

## Related Plugins

- **[Tool Design](../tool-design/)** -- Design principles for agent tool interfaces (this plugin implements them for MCP specifically)
- **[API Design](../api-design/)** -- Design the REST/GraphQL/gRPC APIs that MCP servers wrap
- **[Testing Framework](../testing-framework/)** -- Test infrastructure for MCP server unit and integration tests
- **[TypeScript Development](../typescript-development/)** -- TypeScript patterns used in MCP server implementation
- **[Python Development](../python-development/)** -- Python patterns used in FastMCP server implementation

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
