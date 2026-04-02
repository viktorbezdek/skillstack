# GWS CLI

> **v1.0.0** | Development | 1 iteration

Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace APIs from the command line. Dynamic Discovery-based commands, helper shortcuts, schema introspection, and cross-service workflows.

## What Problem Does This Solve

The `gws` CLI provides a single command-line interface for all Google Workspace APIs, dynamically generated from Google's Discovery Service. This skill teaches Claude Code how to use `gws` effectively -- constructing correct commands, choosing between raw API methods and ergonomic helpers, handling authentication, formatting output, and chaining commands for cross-service workflows. Without this skill, Claude must guess at parameter names, miss helper shortcuts, and cannot leverage pagination, schema introspection, or output formatting.

## When to Use This Skill

Use when working with Google Workspace from the command line: listing Drive files, sending Gmail, reading Sheets data, creating Calendar events, managing Tasks, querying Chat spaces, pushing Apps Script code, or building cross-service automations. Use whenever the user mentions `gws`, Google Workspace CLI, or asks to interact with Google APIs via terminal.

## When NOT to Use This Skill

- Building MCP servers for Google APIs (use mcp-server instead)
- Designing REST APIs in general (use api-design instead)
- Google Cloud Platform infrastructure (use cicd-pipelines instead)
- Browser-based Google Workspace interactions (use the Workspace MCP tools directly)

## How to Use

**Direct invocation:**

```
Use the gws-cli skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `gws`
- `google workspace cli`
- `gws drive`
- `gws gmail`
- `gws sheets`
- `gws calendar`

## What's Inside

- **Complete Service Reference** -- All 18 services with resources and methods
- **Helper Commands** -- Ergonomic `+` prefixed shortcuts for common tasks
- **Schema Introspection** -- How to discover API parameters dynamically
- **Authentication** -- Setup, login, scopes, and credential management
- **Output Formatting** -- JSON, table, YAML, CSV with pagination
- **Cross-Service Workflows** -- Standup reports, meeting prep, email-to-task
- **Real-World Examples** -- Tested command patterns for every service

## Key Capabilities

- **18 Google Workspace APIs** from a single CLI
- **Dynamic Discovery** -- commands auto-update when Google adds endpoints
- **Helper Shortcuts** -- `+send`, `+triage`, `+agenda`, `+upload`, `+append`, `+read`
- **Schema Introspection** -- `gws schema` for parameter discovery
- **Output Formats** -- JSON, table, YAML, CSV with auto-pagination
- **Cross-Service Workflows** -- standup, meeting prep, weekly digest

## Version History

- `1.0.0` feat: initial gws-cli skill with full service reference, helpers, auth, workflows

## Related Skills

- **[API Design](../api-design/)** -- REST, GraphQL, gRPC API design patterns and best practices
- **[Workflow Automation](../workflow-automation/)** -- General workflow orchestration and automation patterns
- **[Documentation Generator](../documentation-generator/)** -- Generate docs for CLI tools and APIs

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
