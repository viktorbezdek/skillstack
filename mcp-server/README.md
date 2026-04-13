# MCP Server

> **v1.2.20** | Development | 23 iterations

> Build production-grade MCP (Model Context Protocol) servers in Python or TypeScript -- tool design, validation, security, evaluation testing, and Claude Code plugin packaging.

## The Problem

Connecting AI agents to external APIs and services requires bridging two fundamentally different worlds. APIs are designed for human developers who read documentation, understand data models, and handle edge cases with conditional logic. AI agents consume tool descriptions from structured metadata, receive inputs as JSON, and make decisions based on natural language descriptions. A direct wrapper around an existing API -- exposing every endpoint as a separate tool with the same parameters -- produces tools that confuse the model, waste context window with verbose descriptions, and return data in formats optimized for machines rather than AI comprehension.

Without a standard protocol, every integration is a custom build. Each developer writes their own tool registration, input validation, error formatting, and transport layer. The result is fragile integrations that break when the API changes, inconsistent tool naming that confuses the model across servers, and security gaps (unsanitized file paths, missing confirmation flags for destructive operations, leaked API keys in tool responses).

The MCP specification provides the standard protocol, but going from "I read the spec" to "I have a production-grade server" requires knowing which SDK to use, how to design tools for AI consumption (not just API wrapping), how to validate inputs with Pydantic or Zod, how to handle pagination and output truncation, how to test with evaluation harnesses, how to deploy securely, and how to package the result as a Claude Code plugin. This knowledge is scattered across the MCP specification, SDK documentation, community examples, and hard-won production experience.

## The Solution

This plugin consolidates everything needed to build production-grade MCP servers into a single skill with 24 reference files. The SKILL.md provides the quick start for both Python (FastMCP with Pydantic validation) and TypeScript (McpServer SDK with Zod schemas), core concepts (tools, resources, prompts, transport types), and best practices for tool design, input/output formatting, validation, and security.

The 24 reference files provide depth across the full development lifecycle: protocol fundamentals, language-specific implementation guides (Python and TypeScript), SDK patterns and code examples, agent-centric tool design, production deployment checklist, security patterns, evaluation-driven development, Claude Code plugin packaging, and community practices from real-world FastMCP deployments.

The practical outcomes are MCP servers where tools are designed for AI consumption (workflow-oriented, not endpoint wrappers), inputs are validated with type-safe schemas (Pydantic constraints in Python, Zod `.strict()` in TypeScript), outputs are formatted for context window efficiency (character limits, pagination, truncation), security is enforced by default (path validation, confirmation flags, secret management), and the whole thing is testable with evaluation harnesses and deployable as a Claude Code plugin.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Each API endpoint becomes a separate MCP tool -- the model sees 30 tools and picks the wrong one | Workflow-oriented tool design consolidates related operations, reducing tool count and improving model accuracy |
| Tool descriptions copy API documentation verbatim -- verbose, jargon-heavy, optimized for humans | Agent-centric descriptions explain what the tool does in plain language, optimized for model comprehension |
| Input validation is ad-hoc if present at all -- invalid inputs produce cryptic API errors | Pydantic `Field()` constraints (Python) or Zod `.strict()` schemas (TypeScript) validate inputs before they reach the API |
| Tool output dumps raw JSON from the API -- 50,000 characters of nested objects filling the context window | Character limits, pagination, and format selection (JSON or Markdown) keep output context-efficient |
| File path parameters are passed directly to the filesystem -- path traversal vulnerabilities | Path validation against allowed directories, destructive operation confirmation flags, and `readOnlyHint` annotations |
| Testing means "try it and see if it works" -- no systematic quality verification | Evaluation-driven development with trigger evals (does the model pick the tool?) and output evals (does the tool produce correct results?) |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install mcp-server@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention MCP, Model Context Protocol, FastMCP, MCP server, MCP tools, or Claude Code plugin development.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Build an MCP server in Python that exposes my database as searchable tools`
4. Claude produces a FastMCP server with Pydantic-validated tool definitions, resource endpoints for schema introspection, STDIO transport configuration, and the `.claude/settings.json` entry to connect it
5. Next, try: `Write evaluation tests for this MCP server` to get trigger evals and output evals for systematic quality verification

## What's Inside

Large single-skill plugin with one SKILL.md, 24 reference files, 13 trigger eval cases, and 3 output eval cases.

### SKILL.md Structure

| Section | What It Covers |
|---|---|
| **Quick Start** | Minimal working server in Python (FastMCP) and TypeScript (McpServer SDK), language selection guide |
| **Core Concepts** | Tools, Resources, Prompts component table; STDIO, HTTP, SSE transport selection; MCP configuration format |
| **Best Practices** | Tool design rules, input/output formatting, validation patterns, security checklist |

### Reference Files (24 files)

| Domain | References | What They Cover |
|---|---|---|
| **Protocol** | 2 files | MCP specification fundamentals, protocol basics |
| **Python (FastMCP)** | 5 files | Python implementation guide, FastMCP development guidelines, community practices, example projects, prompts and templates |
| **TypeScript** | 2 files | TypeScript MCP server implementation, Node SDK patterns |
| **Tool Design** | 3 files | MCP best practices, agent-centric tool design, SDK patterns and code examples |
| **Building & Architecture** | 3 files | Building servers guide, architecture patterns, API comparison |
| **Production** | 2 files | Production deployment checklist, security and caching patterns |
| **Evaluation** | 1 file | MCP server evaluation guide with trigger and output eval patterns |
| **Claude Code Integration** | 4 files | Skill guide, slash command guide, plugin development best practices, extended patterns |
| **Other** | 2 files | Comprehensive development guide, accessing online resources |

### mcp-server

**What it does:** Activates when you ask about building MCP servers, creating tools for Claude, integrating external APIs with MCP, configuring MCP servers for Claude Desktop or Claude Code, writing MCP evaluations, implementing security patterns, or packaging MCP servers as Claude Code plugins. Routes to the appropriate reference files based on your language choice (Python or TypeScript) and development stage (building, testing, deploying, packaging).

**Try these prompts:**

```
Build an MCP server in Python that wraps our REST API for managing inventory -- I need search, create, update, and delete tools
```

```
Convert this existing TypeScript API client into an MCP server with proper Zod validation and tool annotations
```

```
Review my MCP server's tool descriptions -- are they designed for AI consumption or are they just API doc wrappers?
```

```
Write a production deployment checklist for our MCP server -- security, caching, monitoring, and error handling
```

```
Package this MCP server as a Claude Code plugin with skills, hooks, and proper plugin.json metadata
```

```
How do I test my MCP tools with evaluation harnesses -- trigger evals for activation and output evals for correctness?
```

## Real-World Walkthrough

You are building an internal developer platform and your team uses a custom issue tracker (not Jira, not GitHub Issues -- a homegrown system with a REST API). Developers currently switch between their IDE and the web UI to create issues, update status, and link commits to tickets. You want to expose the issue tracker to Claude so developers can manage issues without leaving their coding session.

You start by asking Claude: **"Build an MCP server in Python that exposes our issue tracker API as tools for Claude."**

Claude activates the mcp-server skill and immediately addresses the most common mistake: do not create a separate tool for every API endpoint. Your REST API has 15 endpoints (list issues, get issue, create issue, update issue, delete issue, list comments, add comment, list labels, add label, remove label, etc.). Wrapping each as a tool would give Claude 15 tools to choose from -- too many for reliable selection.

Instead, Claude designs **workflow-oriented tools** that consolidate related operations:

```python
from fastmcp import FastMCP
from pydantic import Field
from typing import Annotated, Literal

mcp = FastMCP("issue-tracker")

@mcp.tool()
def search_issues(
    query: str,
    status: Annotated[Literal["open", "closed", "all"], Field(description="Filter by status")] = "open",
    assignee: Annotated[str | None, Field(description="Filter by assignee username")] = None,
    limit: Annotated[int, Field(ge=1, le=50, description="Max results")] = 10
) -> dict:
    """Search issues by text query with optional filters.
    Returns issue ID, title, status, assignee, and creation date.
    Use this to find issues before updating or commenting on them."""
    results = api.search(query=query, status=status, assignee=assignee, limit=limit)
    return format_results(results, limit)
```

The tool description is written for Claude, not for a human reading API docs. It explains what the tool returns and when to use it ("Use this to find issues before updating or commenting"). The `Annotated` types with Pydantic `Field()` constraints ensure inputs are validated before they reach the API -- `limit` must be between 1 and 50, `status` must be one of the three allowed values.

Claude consolidates the 15 API endpoints into 5 tools:

1. **`search_issues`** -- find issues by query, status, assignee (replaces list + get + filter)
2. **`manage_issue`** -- create, update status, assign, or close an issue (replaces create + update + delete)
3. **`add_comment`** -- add a comment to an issue (remains separate because it is a distinct workflow step)
4. **`manage_labels`** -- add or remove labels (replaces add_label + remove_label + list_labels)
5. **`link_commit`** -- associate a commit hash with an issue (unique workflow action)

Five tools instead of fifteen. Claude picks the right tool far more reliably.

Next, Claude adds **output formatting** for context window efficiency:

```python
CHARACTER_LIMIT = 25_000

def format_results(results: list, limit: int) -> dict:
    formatted = []
    for issue in results[:limit]:
        formatted.append(f"#{issue['id']} [{issue['status']}] {issue['title']} (@{issue['assignee']})")
    output = "\n".join(formatted)
    if len(output) > CHARACTER_LIMIT:
        output = output[:CHARACTER_LIMIT] + f"\n... truncated ({len(results)} total results)"
    return {"results": output, "count": len(results)}
```

The output is a compact string, not a nested JSON object. Each issue is one line with the most relevant fields. If the result exceeds 25,000 characters, it truncates with a count of total results.

Claude then adds **security patterns**. The `manage_issue` tool has a `destructiveHint` annotation because it can delete issues:

```python
@mcp.tool(annotations={"destructiveHint": True})
def manage_issue(
    action: Literal["create", "update", "close", "delete"],
    issue_id: Annotated[int | None, Field(description="Required for update/close/delete")] = None,
    # ...
) -> dict:
    """Create, update, close, or delete an issue. DELETE is permanent."""
```

The `destructiveHint` annotation tells Claude to confirm with the user before calling this tool with `action="delete"`. API keys are stored in environment variables and loaded at server startup, never exposed in tool responses.

Claude also generates the **MCP configuration** for Claude Code:

```json
{
  "mcpServers": {
    "issue-tracker": {
      "command": "python",
      "args": ["-m", "issue_tracker_server"],
      "env": {"TRACKER_API_KEY": "${TRACKER_API_KEY}", "TRACKER_URL": "${TRACKER_URL}"}
    }
  }
}
```

Finally, Claude writes **evaluation tests** following the evaluation-driven development workflow:

- **Trigger evals**: "Create a bug report for the login page", "What issues are assigned to me?", "Close issue #42" -- verifying that Claude picks the correct tool for each natural language request
- **Output evals**: Given a specific search query, does the tool return results in the expected format? Does the character limit truncation work correctly? Does the destructive hint trigger user confirmation?

You install the MCP server, add the configuration to `.claude/settings.json`, and test with: "What open issues are assigned to me?" Claude calls `search_issues(query="", status="open", assignee="your-username")` and returns a clean list. You then say "Close issue #342 -- the bug is fixed in the latest commit" and Claude calls `manage_issue(action="close", issue_id=342)` after confirming the destructive action. The entire workflow happens in the coding session without opening the browser.

## Usage Scenarios

### Scenario 1: Building an MCP server from a REST API

**Context:** You have an internal API with 20 endpoints and want Claude to be able to use it as tools.

**You say:** "Build an MCP server that wraps our inventory API -- I need to search products, manage stock levels, and generate reports"

**The skill provides:**
- Workflow-oriented tool design that consolidates 20 endpoints into 5-7 tools
- Pydantic/Zod input validation with proper constraints and descriptions
- Output formatting with character limits and pagination
- Security patterns for API key management and destructive operations
- Claude Code configuration for connecting the server

**You end up with:** A production-ready MCP server with validated tools, efficient output, and secure configuration.

### Scenario 2: Reviewing tool descriptions for AI consumption

**Context:** You built an MCP server but Claude keeps picking the wrong tool. You suspect the descriptions are the problem.

**You say:** "Review my MCP server's tool descriptions -- Claude keeps calling search when it should call list"

**The skill provides:**
- Agent-centric description audit: are descriptions written for the model or for human API docs?
- Naming convention check: `{service}_{action}_{resource}` format
- Tool consolidation recommendations (too many similar tools confuse the model)
- Annotation review: `readOnlyHint`, `destructiveHint`, `idempotentHint`

**You end up with:** Rewritten descriptions that improve Claude's tool selection accuracy.

### Scenario 3: Adding evaluation testing

**Context:** You have a working MCP server but no systematic way to verify it works correctly after changes.

**You say:** "Write evaluation tests for my MCP server -- I want to verify both tool selection and output quality"

**The skill provides:**
- Trigger eval patterns: natural language queries that should activate each tool
- Output eval patterns: expected response format, truncation behavior, error handling
- Evaluation-driven development workflow for ongoing quality assurance
- Integration with CI for automated eval runs

**You end up with:** A test suite that catches regressions in both tool activation and output quality.

### Scenario 4: Packaging as a Claude Code plugin

**Context:** Your MCP server works locally and you want to distribute it to your team as a Claude Code plugin.

**You say:** "Package my MCP server as a Claude Code plugin with proper skills, hooks, and metadata"

**The skill provides:**
- `plugin.json` manifest with correct fields (name, version, description, author)
- SKILL.md authoring for the skill that teaches Claude how to use your tools
- `.claude/settings.json` configuration for the MCP server
- Hook setup for event-driven behaviors (optional)
- Evaluation files for plugin quality testing

**You end up with:** A distributable Claude Code plugin that installs with `/plugin install` and activates automatically from natural language.

### Scenario 5: Securing an MCP server for production

**Context:** Your MCP server handles sensitive data (customer records, financial transactions) and needs security hardening before production deployment.

**You say:** "Write a security checklist for our MCP server that handles customer data"

**The skill provides:**
- Path validation against allowed directories
- Destructive operation confirmation flags with `destructiveHint` annotations
- Secret management via environment variables (never in tool responses)
- Input sanitization for external identifiers (SQL injection, path traversal)
- Production deployment checklist covering auth, logging, rate limiting, and monitoring

**You end up with:** A hardened MCP server with defense-in-depth security and a deployment checklist.

## Ideal For

- **Developers building AI-integrated internal tools** -- the workflow-oriented tool design and agent-centric descriptions produce tools that the model uses reliably, not just tools that exist
- **Teams standardizing on MCP for agent integrations** -- the protocol fundamentals, SDK patterns, and best practices provide a complete adoption path for both Python and TypeScript
- **Claude Code plugin authors** -- the plugin packaging references cover the full journey from MCP server to distributable plugin with skills, evals, and metadata
- **Security-conscious teams exposing tools to AI** -- the security patterns (path validation, confirmation flags, secret management) address the specific risks of AI-callable tools
- **Quality-focused teams** -- evaluation-driven development with trigger and output evals provides systematic verification that tools work correctly

## Not For

- **Designing tool interfaces or consolidation patterns for agents** -- this plugin covers how to build MCP servers, not the theory of tool design for AI agents. Use [tool-design](../tool-design/) for tool description optimization, parameter design, and agent-tool interaction patterns
- **Prompt engineering or optimization** -- use [prompt-engineering](../prompt-engineering/) for systematic prompt design, evaluation, and refinement
- **General API design** -- use [api-design](../api-design/) for REST, GraphQL, and gRPC design patterns that are not specific to MCP

## How It Works Under the Hood

The plugin is a large single-skill architecture with 24 reference files organized across the full MCP development lifecycle:

1. **Protocol Layer** -- MCP specification fundamentals, protocol basics, transport types (STDIO, HTTP, SSE)
2. **Language-Specific Guides** -- Detailed implementation guides for Python (FastMCP with Pydantic) and TypeScript (McpServer SDK with Zod), plus SDK patterns and code examples
3. **Tool Design** -- Agent-centric tool design principles, naming conventions, description optimization, input/output formatting
4. **Production** -- Deployment checklist, security patterns, caching, monitoring, error handling
5. **Evaluation** -- Trigger evals (tool selection accuracy) and output evals (response quality) with CI integration
6. **Claude Code Integration** -- Skill authoring, slash command development, plugin architecture, plugin best practices

The SKILL.md provides the quick start and best practices summary, while the reference files provide depth on demand. Claude loads only the references relevant to the current query -- a Python quick-start question loads `python-guide.md` and `development-guidelines.md`, while a security question loads `production-checklist.md` and `best-practices.md`.

## Related Plugins

- **[Tool Design](../tool-design/)** -- Agent-centric tool interface design, description optimization, and tool consolidation patterns -- the design theory that this plugin implements
- **[API Design](../api-design/)** -- REST, GraphQL, and gRPC design patterns for the APIs that MCP servers wrap
- **[GWS CLI](../gws-cli/)** -- Google Workspace CLI -- an example of a well-designed tool interface for multiple services
- **[Next.js Development](../nextjs-development/)** -- App Router and Server Components for web frontends that pair with MCP-powered backends
- **[Debugging](../debugging/)** -- Systematic debugging methodology for troubleshooting MCP server issues

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
