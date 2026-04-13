# Filesystem Context

> **v1.0.4** | Context Engineering | 5 iterations

> Use the filesystem as unlimited external memory for LLM agents -- scratch pads, plan persistence, sub-agent workspaces, dynamic skill loading, and self-modification patterns.

## The Problem

LLM agents working on long-horizon tasks hit the same wall: the context window fills up. A web search returns 10,000 tokens of raw content. A build produces 50,000 lines of output. A multi-step refactoring task takes 30 turns and the agent loses track of which files have been updated. The standard workarounds -- summarization and truncation -- destroy information. The agent forgets details it needed, repeats work it already did, or loses the plan it was following.

The problem compounds in multi-agent architectures. When sub-agents report findings to a coordinator through message chains, each hop summarizes and loses fidelity. By the time three sub-agents have reported to a coordinator, the original details are gone -- replaced by summaries of summaries. And as agents accumulate more capabilities (tools, skills, instructions), the static system prompt grows until it crowds out space for the actual task.

The deeper issue is architectural. Context windows are treated as the only memory layer, when they should be the working memory -- small, focused, and frequently refreshed from a persistent store. Without a persistent layer, agents carry everything they have ever seen in the conversation, burning tokens on information that was relevant three steps ago but is noise now.

## The Solution

This plugin treats the filesystem as an unlimited external memory layer for LLM agents. Instead of stuffing everything into the context window, agents write large outputs to files and keep only a summary and a file reference in context. Plans are persisted as YAML files and re-read each turn so the agent always knows where it left off. Sub-agents share state through file directories instead of message chains. Skills are loaded dynamically from files rather than crammed into the system prompt.

The six patterns in this plugin address six specific failure modes: context bloat from tool outputs (scratch pad), plan amnesia over long trajectories (plan persistence), information loss in multi-agent communication (sub-agent workspaces), system prompt overload from too many skills (dynamic loading), inaccessible terminal output (log persistence), and inability to learn across sessions (self-modification).

The implementation is concrete: code examples with before/after token counts, a recommended directory structure, and ten operational rules for when and how to apply each pattern. The reference file provides worked examples showing exactly how much context is saved by each technique.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Web search returns 8,000 tokens that stay in context for the entire conversation | Scratch pad writes results to a file, returns a 100-token summary -- agent greps the file when it needs specific details |
| Agent loses track of a 30-step refactoring task after context summarization | YAML plan file is re-read each turn -- the agent always knows which step is next |
| Sub-agents report to a coordinator through message chains, losing detail at each hop | Each sub-agent writes to its own directory; coordinator reads files directly with full fidelity |
| 50 skills stuffed into the system prompt waste tokens and confuse the model | Only skill names and one-line descriptions are static; full SKILL.md files are loaded on demand |
| 50,000-line build output is either dumped into context (too large) or lost (not useful) | Terminal output is synced to dated files; the agent greps for "ERROR" or stack traces |
| Agent cannot remember user preferences or learned patterns across sessions | Self-modification pattern writes learned information to files loaded at session start |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install filesystem-context@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention filesystem context, scratch pads, plan persistence, dynamic skill loading, or file-based agent memory.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Design a scratch pad system for my agent that offloads large tool outputs to files`
4. Claude produces the scratch pad pattern with threshold logic (write to file if > 2,000 tokens), summary extraction, file reference format, and grep-based retrieval
5. Next, try: `How should I persist my agent's plan so it survives context compaction?` to get the YAML plan persistence pattern with re-read-on-each-turn architecture

## What's Inside

Single-skill plugin with one SKILL.md and one reference file, 13 trigger eval cases, and 3 output eval cases.

| Component | What It Provides |
|---|---|
| **Scratch Pad Pattern** | Write large outputs (> 2,000 tokens) to files, return summary + reference, use grep for retrieval |
| **Plan Persistence** | YAML schema for objective, steps, and status; re-read each turn for attention manipulation |
| **Sub-Agent Workspaces** | Per-agent file directories for direct state sharing, bypassing message chains |
| **Dynamic Skill Loading** | Static index of skill names + descriptions; full content loaded on demand |
| **Terminal Log Persistence** | Sync stdout to dated files; agents grep for error patterns |
| **Self-Modification** | Agents write learned preferences/patterns to files loaded at session start |
| **`implementation-patterns.md`** | Reference with worked examples, before/after token counts, directory structure, and ten rules |

### filesystem-context

**What it does:** Activates when you ask about using files for agent context management, offloading tool outputs, persisting plans, coordinating sub-agents through files, loading skills dynamically, or building agents that learn across sessions. Provides six concrete patterns with code examples, token accounting, and a recommended directory structure.

**Try these prompts:**

```
My agent's web search tool returns 10,000+ tokens per query and it's filling up the context window -- how do I offload this to files?
```

```
Design a plan persistence system so my refactoring agent doesn't lose track of progress when the context compacts
```

```
I have three sub-agents (research, code, test) that need to share findings with a coordinator -- how do I use the filesystem instead of message passing?
```

```
My agent has 40 skills and the system prompt is enormous -- how do I load skills dynamically instead of including them all?
```

```
How should I structure the file system for an agent that needs scratch space, persistent memory, and sub-agent workspaces?
```

**Key references:**

| Reference | Topic |
|---|---|
| `implementation-patterns.md` | Detailed pattern implementations with before/after token counts, directory structure templates, and ten operational rules |

## Real-World Walkthrough

You are building a code review agent that analyzes pull requests across a monorepo. The agent receives a PR diff (often 2,000-5,000 lines), reads the relevant source files for context, checks test coverage, runs linters, and produces a structured review. After three PRs, the agent's context window is full of old diff content, previous review comments, and stale lint output from PRs that are already merged.

You start by asking Claude: **"Design a filesystem-based context architecture for a code review agent that handles multiple PRs in a single session."**

Claude activates the filesystem-context skill and begins with the **scratch pad pattern** for the largest context consumer: PR diffs. Instead of loading a 4,000-line diff directly into context, the agent writes it to `scratch/pr-1234-diff.txt` and returns a summary: "PR #1234: 47 files changed, 1,200 additions, 800 deletions. Key areas: `src/auth/` (12 files), `src/api/` (8 files), `tests/` (27 files). Full diff in `scratch/pr-1234-diff.txt`." This reduces 4,000 lines to 5 lines. When the agent needs to review a specific file's changes, it runs `grep -A 20 "src/auth/token.ts" scratch/pr-1234-diff.txt` to extract just that section.

Next, Claude applies the **plan persistence pattern** to the review workflow itself. The agent creates a YAML plan at the start of each PR review:

```yaml
# scratch/plans/pr-1234-review.yaml
objective: "Review PR #1234 - Auth token refresh"
status: in_progress
steps:
  - id: 1
    description: "Read diff summary and identify high-risk areas"
    status: completed
  - id: 2
    description: "Review auth module changes for security issues"
    status: in_progress
  - id: 3
    description: "Check test coverage for changed functions"
    status: pending
  - id: 4
    description: "Run linter and check for style violations"
    status: pending
  - id: 5
    description: "Produce structured review with findings"
    status: pending
```

The agent re-reads this file at the start of each turn. If context compaction fires between Step 2 and Step 3, the agent does not lose its place -- it reads the plan file and sees exactly where to resume.

Claude then designs the **sub-agent workspace** for the review components. Instead of one agent doing everything sequentially, three sub-agents work in parallel:

```
workspace/
  agents/
    security-reviewer/
      findings.md          # Security issues found
      severity-summary.txt # High/Medium/Low counts
    test-coverage/
      coverage-report.txt  # Coverage analysis output
      gaps.md             # Untested code paths
    style-checker/
      lint-output.txt     # Raw linter output
      violations.md       # Grouped violations with fix suggestions
  coordinator/
    review.md             # Final synthesized review
```

Each sub-agent writes to its own directory. The coordinator reads all three directories and synthesizes a final review without any information passing through message chains. The security reviewer's full analysis is preserved verbatim -- not summarized through a message hop.

For the lint and test output, Claude applies the **terminal log persistence pattern**. The linter produces 500 lines of output; the test runner produces 2,000 lines. Both are written to files in the sub-agent workspace. The style-checker agent greps for warnings and errors rather than processing the full output: `grep -c "warning" lint-output.txt` (count), then `grep -B2 -A5 "error" lint-output.txt` (details for errors only).

Finally, Claude applies **dynamic skill loading** to the review knowledge base. The agent has specialized review checklists for different code areas (auth, API, database, frontend, infrastructure), but loading all of them into context wastes tokens. The static index includes one-line descriptions:

```
Available review checklists:
- auth-review: Token validation, session handling, RBAC checks
- api-review: Input validation, rate limiting, error responses
- database-review: Query optimization, migration safety, index usage
```

When the agent identifies that PR #1234 touches the auth module, it loads `skills/auth-review/SKILL.md` and applies only the relevant checklist.

The result: each PR review uses approximately 3,000 tokens of active context instead of 15,000+. The agent can review 10 PRs in a single session without context degradation. The plan file ensures no review step is skipped even when compaction fires. Sub-agent findings are preserved at full fidelity. And the agent only loads the review checklists it actually needs.

## Usage Scenarios

### Scenario 1: Offloading web search results for a research agent

**Context:** Your research agent runs 5-10 web searches per task, each returning 8,000-12,000 tokens. After three searches, the context window is dominated by search results from the first query.

**You say:** "Design a scratch pad system for my research agent that keeps search results accessible without filling the context window"

**The skill provides:**
- Scratch pad implementation with 2,000-token threshold
- Summary extraction function that produces key findings in 200 tokens
- File reference format that the agent can grep for specific claims
- Cleanup strategy for removing stale scratch files after the task completes

**You end up with:** A working pattern where each search adds 200 tokens to context (not 10,000) while the full results remain accessible via grep.

### Scenario 2: Keeping a multi-step migration on track

**Context:** Your agent is running a 25-step database migration and keeps losing track after context compaction. It re-runs steps it already completed.

**You say:** "How do I persist my agent's migration plan so it always knows which step is next?"

**The skill provides:**
- YAML plan schema with step IDs, descriptions, and status fields
- Re-read-on-each-turn architecture that refreshes the plan at the start of every turn
- Status update pattern that marks steps completed immediately after execution
- Recovery strategy for when the agent is mid-step during compaction

**You end up with:** A plan persistence system where the agent never repeats a completed step and always resumes from the correct position.

### Scenario 3: Coordinating parallel sub-agents without information loss

**Context:** You have a frontend agent, a backend agent, and a database agent working on a feature. The coordinator agent gets summarized results from each, losing implementation details.

**You say:** "Set up file workspaces so my sub-agents share results with the coordinator without message chains"

**The skill provides:**
- Directory structure with per-agent workspaces
- File naming conventions for findings, outputs, and status
- Coordinator read pattern that processes all agent outputs directly
- Conflict resolution for when agents need to reference each other's work

**You end up with:** A workspace layout where the coordinator reads full-fidelity results from each agent without any summarization loss.

### Scenario 4: Scaling from 5 skills to 50 without degrading agent performance

**Context:** Your agent started with 5 skills in the system prompt and worked well. Now it has 50 skills, the system prompt is 30,000 tokens, and the model frequently picks the wrong skill.

**You say:** "How do I load skills dynamically so the system prompt stays small but all 50 skills are available?"

**The skill provides:**
- Static index format: skill name + one-line description (50 lines instead of 30,000 tokens)
- On-demand loading pattern: agent reads full SKILL.md only when a query matches
- Matching logic for determining which skill to load based on the query
- Cache-and-evict strategy for skills loaded in the same session

**You end up with:** A system prompt under 2,000 tokens with all 50 skills accessible on demand.

## Ideal For

- **Agent builders working on long-horizon tasks** -- plan persistence and scratch pads keep agents on track across 30+ turn conversations
- **Multi-agent system architects** -- sub-agent workspaces eliminate the information loss inherent in message-chain coordination
- **Teams scaling agent capabilities** -- dynamic skill loading lets you add skills without proportionally growing the system prompt
- **Developers building research or analysis agents** -- scratch pad offloading prevents tool outputs from dominating the context window
- **Context engineers optimizing token budgets** -- the before/after token accounting in the reference file provides concrete savings measurements

## Not For

- **In-context optimization** (KV-cache tuning, observation masking, attention manipulation) -- use [context-optimization](../context-optimization/) for techniques that work within the context window rather than offloading from it
- **Summarization and compression techniques** -- use [context-compression](../context-compression/) for anchored iterative summarization and tokens-per-task optimization
- **Understanding context theory** -- use [context-fundamentals](../context-fundamentals/) for the foundational theory of how attention works and why context engineering matters

## How It Works Under the Hood

The plugin uses a single SKILL.md with one reference file. The SKILL.md covers six patterns, each with a problem statement, solution, implementation code example, and benefits:

1. **Scratch Pad** -- threshold-based offloading with summary extraction and file references
2. **Plan Persistence** -- YAML plan schema with re-read-on-each-turn architecture
3. **Sub-Agent Workspaces** -- per-agent directories with coordinator read patterns
4. **Dynamic Skill Loading** -- static index + on-demand file reads
5. **Terminal Log Persistence** -- stdout sync to dated files with grep-based querying
6. **Self-Modification** -- learned preferences written to files loaded at session start

The reference file (`implementation-patterns.md`) provides detailed worked examples with before/after token counts and a recommended directory structure for organizing agent files.

The skill connects to four related plugins: context-optimization (filesystem offloading as a form of observation masking), memory-systems (filesystem-as-memory as a simple memory layer), multi-agent-patterns (sub-agent workspaces enable agent isolation), and context-compression (file references as lossless compression).

## Related Plugins

- **[Context Optimization](../context-optimization/)** -- KV-cache optimization, observation masking, and retrieval strategies for extending effective context capacity
- **[Context Compression](../context-compression/)** -- Anchored iterative summarization and tokens-per-task optimization
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory of context engineering for AI agent systems
- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, and confusion patterns
- **[Memory Systems](../memory-systems/)** -- Production memory frameworks (Mem0, Zep, Letta) for persistent agent memory
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, swarm, and pipeline architectures for multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
