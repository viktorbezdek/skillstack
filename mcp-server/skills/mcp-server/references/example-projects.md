# FastMCP Example Projects

Real-world MCP server implementations demonstrating best practices and patterns.

## Overview

TRIGGER: The model must reference these patterns when implementing similar functionality

PATTERN_LIBRARY: Open-source MCP implementations demonstrating production architectures

## Ultimate MCP Server (AI Agent OS)

**GitHub**: Dicklesworthstone/ultimate_mcp_server

A comprehensive reference implementation that turns an MCP server into an **AI agent operating system**.

### Features

- **Dozens of integrated tools** for cognitive augmentation:
  - Tool-mediated web browsing
  - Code execution
  - OCR (image text extraction)
  - Vector database queries
  - Excel automation
  - And many more capabilities

### Key Architecture Patterns

**Intelligent Model Delegation:**

Uses powerful but expensive models (Claude 3.7) for complex planning, then offloads subtasks to cheaper models (Gemini Flash 2.0 Lite) to optimize cost vs performance.

**Large-Scale Server Structure:**

- FastMCP's plugin system to manage many tools
- Shared memory across tools
- Robust error handling
- ~140 commits with MIT license

### Why Study This Project

- **Template for industrial-grade agents** - Shows how to structure large-scale servers
- **Multi-service orchestration** - Demonstrates integrating multiple AI services under one MCP endpoint
- **Cost optimization** - Practical model delegation strategies
- **Plugin architecture** - Managing complexity with modular design

**Use as template when**: Building complex agent systems with multiple integrated capabilities.

## Hugging Face MCP Server

**GitHub**: evalstate/hf-mcp-server

Official MCP server from Hugging Face providing access to HF resources via MCP.

### Capabilities

Exposes tools for:

- **Browsing** Hugging Face models, datasets, and Spaces
- **Querying** ML assets on HF infrastructure
- **Running inferences** on HF-hosted models

### What This Demonstrates

- **Third-party SDK integration** - How to configure external SDKs within an MCP server
- **Authentication handling** - Managing API keys and user auth
- **Caching strategies** - Improving performance for repeated queries
- **ML domain patterns** - Specific to AI/ML asset management

### Endorsement Significance

Endorsement from Hugging Face signals trust in MCP's approach as an integration standard for ML platforms.

**Use as reference when**: Integrating ML model hubs or AI asset management into MCP servers.

## Browser Automation Servers

### Browser MCP

**Website**: browsermcp.io

Combines local HTTP MCP server with Chrome extension to enable browser control.

### Capabilities

AI IDEs (Cursor, Claude Code, Windsurf) can:

- Open web pages
- Click elements
- Retrieve text from pages
- Fill forms
- Navigate web interfaces

### Technical Approach

- **FastMCP with async tools** - Controlling headless browser or Chrome DevTools Protocol
- **Performance focus** - Must be responsive to keep up with model
- **Reliability** - Sandboxing actions, ensuring automation doesn't hang
- **UI bridge** - MCP interface to real browser interactions

### Related Project

**Firecrawl MCP** - Similar project for web browsing and searching, often cited in community lists.

**Use as template when**: Building tools that require UI automation or web interaction.

## Data and DevOps Integrations

### BrightData MCP

Provides web data scraping functions:

- Search queries across web
- Page navigation
- Data extraction

### JSON Manipulation Server

Tools for working with JSON files:

- Splitting large JSON files
- Merging JSON structures
- Transforming data formats

### Database MCP Servers

Servers for querying databases:

- **SQLite MCP** - Local database queries
- **Postgres MCP** - PostgreSQL integration
- **MindsDB MCP** - AI database, query multiple databases with SQL via one server

### Infrastructure Management

**Render MCP Server** - Manage Render Cloud infrastructure through Claude or Cursor

**Common Pattern**: Define one class of tools (e.g., all database operations) and use resource templates to expose data (like `data://table/{id}` returning a record).

**Use as template when**: Building MCP servers for existing services or APIs.

## Coding Assistant MCPs

### DeepView MCP

**Purpose**: Analyze large codebases using Google's Gemini model with huge context window.

### Capabilities

AI IDE can ask:

- "Find all references of function X in this repository"
- "Show me all classes implementing interface Y"
- "Analyze the call graph for this module"

### Technical Pattern

**Big data handling** - Server does heavy lifting (code indexing, AST parsing) that would be impractical through LLM context directly.

### Related Projects

- **AmpCode** (Sourcegraph) - Likely uses MCP-like mechanisms for repository-wide context
- **Cline** - Claude-based dev tool with MCP plugin support
- **Roo** - AI IDE with MCP integration

### Common Patterns

**Safety focus**:

- Read-only access for code analysis
- User approval required for code execution
- Permission gating using FastMCP's enabled flags or annotations

**Task splitting**:

- AI decides what to query
- Server does actual file parsing and indexing

**Use as template when**: Building tools for code analysis, repository search, or large-scale text processing.

## Templates and Aggregators

### Data-Everything MCP Server Templates

**GitHub**: Data-Everything/mcp-server-templates

Provides flexible skeleton for MCP servers with:

- **Docker/Kubernetes support** - Production deployment ready
- **CLI tool (mcpt)** - Generate new servers from templates
- **Transport flexibility** - Both HTTP and STDIO
- **Load balancing** - Across multiple server instances
- **YAML configuration** - Centralized config management

**Use when**: Kickstarting a project with best-practice defaults (logging, error masking) already set up.

### mcp-server-templates

"One server, all tools" approach - plug multiple capabilities behind one interface.

### Aggregator Projects

**MCPX** (TheLunarCompany):

- Acts as gateway centralizing tool discovery
- Usage tracking and load balancing
- Combines multiple MCP servers into one endpoint

**Magg** (MetaMCP):

- Lets AI autonomously discover and install new MCP servers as needed
- Enterprise pattern for managing multiple servers

### Architecture Pattern

Instead of AI client juggling 10 server connections:

1. Run aggregator that proxies them as one
2. Centralized discovery and routing
3. Load balancing across servers
4. Usage analytics

**Use when**: Designing modular MCP systems, scaling horizontally, or enterprise deployments.

## Common Patterns Across Examples

### Key Takeaways

1. **Use FastMCP's strengths**:
   - Schema validation
   - Structured I/O
   - Type safety

2. **Optimize where possible**:
   - Cache results
   - Delegate heavy tasks to server
   - Use async for I/O operations

3. **Security patterns**:
   - Don't execute arbitrary code unless necessary
   - Sandbox when you do
   - Respect user-provided scopes (directories, API quotas)
   - Use annotations for permission gating

4. **Follow established patterns**:
   - Tool naming conventions
   - Error message formatting
   - Resource template usage
   - Configuration via environment variables

## Community Resources

### Discovery Lists

- **Awesome MCP Servers** (GitHub: punkpeye/awesome-mcp-servers) - Curated list of MCP servers and frameworks
- **Hugging Face Turing Post** articles - Community practices and trending projects

### Where to Find More

Many projects featured in:

- Anthropic's MCP showcase
- Community Discord channels
- Reddit r/ClaudeAI discussions
- GitHub trending repositories

## Using These Examples

### How to Learn from Examples

1. **Start with simple projects** - Understand basic patterns first
2. **Clone and experiment** - Run servers locally to understand behavior
3. **Read the code** - Look for FastMCP patterns and best practices
4. **Adapt to your needs** - Don't copy blindly, understand and modify
5. **Contribute back** - Many projects accept PRs for improvements

### Common Questions These Projects Answer

- How do I structure a large server with many tools?
- How do I handle authentication for external APIs?
- What's the best way to cache responses?
- How do I implement pagination for large datasets?
- How do I test my MCP server?
- What deployment options work best?

## Summary

These example projects illustrate MCP's use case breadth:

- **Simple calculators** to **multi-functional agent OSes**
- **File manipulation** to **cloud infrastructure management**
- **Local databases** to **distributed AI systems**

Most are built on FastMCP (Python) or TypeScript MCP SDK, demonstrating the frameworks' versatility and power.

Study these projects to:

- Accelerate your development
- Avoid common pitfalls
- Learn production-ready patterns
- Understand real-world architectures

When building your own server, chances are someone has open-sourced a similar one - consulting those repositories can save time and highlight edge cases you might not have considered.
