---
name: research-synthesis
description: >-
  Structured research and evidence synthesis for knowledge-intensive tasks. Use for multi-source research coordination, evidence triangulation across conflicting sources, competing-hypothesis analysis, literature/documentation sweeps, claim verification, and synthesis reports. Trigger phrases: "research this topic", "synthesise findings from", "compare sources on", "what does the evidence say about", "triangulate these claims". NOT for primary data collection (interviews, surveys) — this skill synthesises existing sources. NOT for code research or codebase exploration — use CodeGraph and Semble for that. NOT for creative content generation — synthesis produces structured analysis, not narrative content.
allowed-tools: Read,Write,Edit,Bash
---

# research-synthesis

Multi-source research coordination, evidence triangulation, competing-hypothesis analysis, and structured synthesis for knowledge-intensive tasks.

## When to use

- Research the tradeoffs between gRPC and REST for internal microservice communication
- Synthesise what the evidence says about daily standups harming deep work
- Compare three sources on the effectiveness of TDD — what do they agree and disagree on?
- I have 5 conflicting reports on LLM inference costs — triangulate the actual picture
- Do a literature sweep on context window utilisation patterns in production LLMs
- Research prompt injection attack vectors and summarise defensive patterns
- What competing hypotheses exist for why the attention mechanism scales so well?
- Synthesise our internal incident post-mortems to find common root-cause patterns

## When NOT to use

- Run a customer survey to validate our product hypothesis — Primary data collection — not synthesis
- Explore this codebase and find where authentication happens — Code research — use CodeGraph/Semble
- Write a blog post about distributed systems — Creative content generation — not evidence synthesis
- What is the capital of France? — Single-fact lookup — no synthesis needed

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
