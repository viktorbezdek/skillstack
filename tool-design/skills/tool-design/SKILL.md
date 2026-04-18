---
name: tool-design
description: This skill should be used when the user asks to "design agent tools", "create tool descriptions", "reduce tool complexity", "implement MCP tools", or mentions tool consolidation, architectural reduction, tool naming conventions, or agent-tool interfaces. NOT for building MCP servers or MCP protocol implementation (use mcp-server), NOT for multi-agent coordination or agent handoffs (use multi-agent-patterns), NOT for agent memory or persistence (use memory-systems).
---

# Tool Design for Agents

Tools are the primary mechanism through which agents interact with the world. They define the contract between deterministic systems and non-deterministic agents. Unlike traditional software APIs designed for developers, tool APIs must be designed for language models that reason about intent, infer parameter values, and generate calls from natural language requests. Poor tool design creates failure modes that no amount of prompt engineering can fix.

## When to Use This Skill

Activate this skill when:
- Creating new tools for agent systems from scratch
- Debugging tool-related failures or misuse (wrong tool selected, parameters misused)
- Optimizing existing tool sets for better agent performance
- Designing tool APIs and descriptions for MCP servers
- Evaluating whether to use primitives (bash, SQL) vs specialized wrappers
- Standardizing tool conventions across a codebase
- Consolidating overlapping tools that confuse agents
- Writing error messages that enable agent self-correction

## When NOT to Use This Skill

- **Building MCP servers or implementing MCP protocol** → use `mcp-server` (this skill is about the tool interface design, not the transport layer)
- **Designing multi-agent coordination or agent handoffs** → use `multi-agent-patterns`
- **Implementing agent memory or persistence** → use `memory-systems`
- **Evaluating whether tools work after designing them** → use `agent-evaluation` (rubrics, LLM-as-judge scoring, test harnesses)

## Decision Trees

### Consolidation vs Architectural Reduction

```
You have a tool set. What's the problem?
  │
  ├─ Agent picks wrong tool when multiple have overlapping scopes
  │   └─ CONSOLIDATION (default first move)
  │       Merge overlapping tools (getFoo + searchFoo → lookupFoo)
  │       Test: can a human instantly tell which tool to use?
  │       If not → merge.
  │
  ├─ Tool count is reasonable but agent is still constrained
  │   └─ Ask: are specialized tools enabling or constraining?
  │       │
  │       ├─ Enabling → Keep specialized tools
  │       └─ Constraining → ARCHITECTURAL REDUCTION
  │           Replace with primitives (bash, SQL, file access)
  │           Requires: well-documented data + model reasoning capability
  │
  └─ Not sure which approach
      └─ Start with consolidation. Only reduce if agent still struggles.
```

### Primitives vs Specialized Tools Decision

```
Is your data layer well-documented and consistently structured?
  │
  ├─ Yes → Are there safety constraints limiting what the agent can do?
  │   │       │
  │   │       ├─ No → PRIMITIVES (bash, SQL, file access)
  │   │       │   Model navigates complexity; less maintenance
  │   │       │
  │   │       └─ Yes → SPECIALIZED TOOLS with guardrails
  │   │           Safety trumps flexibility
  │   │
  └─ No → SPECIALIZED TOOLS
      Messy data requires structured interfaces;
      primitives will fail against undocumented/invalid schemas
```

### Error Message Design Decision

```
After reading the error, can the agent construct a corrected call?
  │
  ├─ Yes → Error message is sufficient
  │
  └─ No → Redesign the error message:
      - Include: error code, human message, invalid value provided, correction suggestion
      - For retryable errors: include wait time or backoff guidance
      - For format errors: include accepted format with example
```

## Core Concepts

### The Tool-Agent Interface

Tools are contracts between deterministic systems and non-deterministic agents. When humans call APIs, they understand the contract and make appropriate requests. Agents must infer the contract from descriptions and generate calls that match expected formats. Every ambiguity in tool definitions becomes a potential failure mode.

### Tool Description as Prompt

Tool descriptions are loaded into agent context and collectively steer behavior. The descriptions are not just documentation — they are prompt engineering that shapes how agents reason about tool use. Poor descriptions like "Search the database" with cryptic parameter names force agents to guess.

### The Consolidation Principle

If a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better. Prefer single comprehensive tools over multiple narrow tools with overlapping scopes.

**When NOT to consolidate:**
- Tools serve fundamentally different workflows (not just different use cases of the same workflow)
- Tools are used in completely different contexts
- Tools that might be called independently should not be artificially bundled

### Architectural Reduction

The consolidation principle, taken to its logical extreme: removing most specialized tools in favor of primitive, general-purpose capabilities.

**Reduction works when:**
- Data layer is well-documented and consistently structured
- Model has sufficient reasoning capability to navigate complexity
- Specialized tools were constraining rather than enabling
- You're spending more time maintaining scaffolding than improving outcomes

**Reduction fails when:**
- Data is messy, inconsistent, or poorly documented
- Domain requires specialized knowledge the model lacks
- Safety constraints require limiting what the agent can do
- Operations are truly complex and benefit from structured workflows

See [Architectural Reduction Case Study](./references/architectural_reduction.md) for production evidence.

## Tool Description Engineering

Effective tool descriptions answer four questions:

| Question | What to Include |
|----------|----------------|
| **What does it do?** | Clear, specific functionality. No vague language like "helps with." State exactly what it accomplishes. |
| **When should it be used?** | Specific triggers and contexts. Include negative triggers: "NOT for [X] — use [other_tool] instead." |
| **What inputs does it accept?** | Parameter descriptions with types, constraints, defaults, and format examples. |
| **What does it return?** | Output format and structure. Include examples of successful responses and error conditions. |

### Response Format Optimization

Tool response size significantly impacts context usage. Implement response format options:

- **Concise**: Essential fields only, for confirmation or basic information
- **Detailed**: Complete objects, for when full context is needed for decisions

Include guidance in tool descriptions about when to use each format.

### Error Message Design

Error messages serve two audiences: developers debugging issues and agents recovering from failures. For agents, error messages must be **actionable** — they must tell the agent what went wrong and how to correct it.

```python
# Bad: Agent retries with same bad input
{"error": "ValidationError", "message": "Invalid date"}

# Good: Agent self-corrects on next call
{
    "error": "INVALID_DATE_FORMAT",
    "message": "Date must be in ISO 8601 format (YYYY-MM-DD)",
    "provided": "12/31/2025",
    "suggestion": "Did you mean '2025-12-31'? Use YYYY-MM-DD format."
}
```

### MCP Tool Naming Requirements

When using MCP tools, always use fully qualified tool names to avoid "tool not found" errors.

Format: `ServerName:tool_name`

```python
# Correct: Fully qualified names
"Use the BigQuery:bigquery_schema tool to retrieve table schemas."
"Use the GitHub:create_issue tool to create issues."

# Incorrect: Unqualified names
"Use the bigquery_schema tool..."  # May fail with multiple servers
```

### Tool Collection Sizing

- Target **10-20 tools** for most applications
- If more are needed, use namespacing to create logical groupings
- Each tool adds description tokens that consume context budget
- More tools = more selection ambiguity = more wrong-tool calls

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Vague descriptions** | "Search the database for customer information" — agent cannot determine when to use this tool vs another | Answer all four questions: what, when, inputs, returns. Include "NOT for..." negative triggers. |
| **Cryptic parameter names** | `x`, `val`, `param1`, `query` — agent must guess meaning and format | Use descriptive names with type, format constraint, and example: `customer_id: Format "CUST-######"` |
| **Missing error handling** | Generic `{"error": "Invalid input"}` — agent retries same bad input 3-5 times, then gives up | Include error code, human message, provided value, and correction suggestion. See Error Message Design above. |
| **Inconsistent naming** | `id` in one tool, `identifier` in another, `customer_id` in a third — agent cannot infer correct parameter | Establish naming conventions: verb-noun for tool names, consistent parameter names across all tools |
| **getFoo + searchFoo overlap** | Agent cannot distinguish "I have an ID" from "I have a search term" in natural language | Consolidate into `lookupFoo` that accepts both ID and search terms with unambiguous routing |
| **Swiss army knife tools** | Over-consolidation merges fundamentally different workflows; description becomes so long it confuses the model | Split back along workflow boundaries. Consolidate overlapping scopes, not different workflows. |
| **Overly long descriptions** | Description exceeds attention agent allocates to tool selection; descriptions collectively consume too much context | One sentence for "what," one for "when," parameter list, return format. Move extended guidance to system prompts or reference docs. |
| **Missing negative triggers** | Agent calls tool for adjacent use cases it was not designed for | Add explicit "NOT for..." clauses to descriptions. Reference the correct tool by name. |
| **Protective wrapper tools** | Tools built to "protect" the model from complexity — pre-filtering, constraining options, wrapping in validation | Ask: does this tool enable a new capability, or constrain reasoning the model could handle? Build minimal architectures that benefit from model improvements. |

## Using Agents to Optimize Tools

Claude can optimize its own tools. When given a tool and observed failure modes, it diagnoses issues and suggests improvements. Production testing shows this achieves 40% reduction in task completion time.

**The Tool-Testing Agent Pattern:**
1. Agent attempts to use tool across diverse tasks
2. Collect failure modes and friction points
3. Agent analyzes failures and proposes improvements
4. Test improved descriptions against same tasks

This creates a feedback loop: agents using tools generate failure data, which agents then use to improve tool descriptions, which reduces future failures.

## Examples

**Well-Designed Tool:**
```python
def get_customer(customer_id: str, format: str = "concise"):
    """
    Retrieve customer information by ID.

    Use when:
    - User asks about specific customer details
    - Need customer context for decision-making
    - Verifying customer identity
    NOT for: searching customers by name (use search_customers)

    Args:
        customer_id: Format "CUST-######" (e.g., "CUST-000001")
        format: "concise" for key fields, "detailed" for complete record

    Returns:
        Customer object with requested fields

    Errors:
        NOT_FOUND: Customer ID not found
        INVALID_FORMAT: ID must match CUST-###### pattern
    """
```

**Poor Tool Design:**
```python
def search(query):
    """Search the database."""
    pass
```
Problems: vague name, missing parameters, no return description, no usage context, no error handling.

## Guidelines

1. Write descriptions that answer what, when, inputs, and returns
2. Add "NOT for..." negative triggers referencing the correct tool
3. Use consolidation to reduce ambiguity between overlapping tools
4. Implement response format options for token efficiency
5. Design error messages for agent recovery (not just developer debugging)
6. Establish and follow consistent naming conventions
7. Limit tool count to 10-20; use namespacing for logical grouping
8. Test tool designs with actual agent interactions
9. Iterate based on observed failure modes
10. Question whether each tool enables or constrains the model
11. Prefer primitive, general-purpose tools over specialized wrappers (when data is well-documented)
12. Build minimal architectures that benefit from model improvements

## References

Internal references:
- [Best Practices Reference](./references/best_practices.md) - Detailed tool design guidelines
- [Architectural Reduction Case Study](./references/architectural_reduction.md) - Production evidence for tool minimalism

Related skills:
- `context-fundamentals` - Tool context interactions
- `multi-agent-patterns` - Specialized tools per agent
- `agent-evaluation` - Tool effectiveness testing
