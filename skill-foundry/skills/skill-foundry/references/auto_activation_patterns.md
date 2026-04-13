# Auto-Activation Patterns from skill-developer

Synthesized patterns, wisdom, and insights extracted from the production skill-developer implementation for creating skills with auto-activation systems.

## Table of Contents

- [Overview](#overview)
- [Core Patterns](#core-patterns)
- [Trigger System Design](#trigger-system-design)
- [Enforcement Strategies](#enforcement-strategies)
- [Session Management](#session-management)
- [Performance Optimization](#performance-optimization)
- [Key Insights](#key-insights)
- [Implementation Wisdom](#implementation-wisdom)
- [Best Practices](#best-practices)
- [Testing Commands Quick Reference](#testing-commands-quick-reference)
- [Auto-Activation Validation Checklist](#auto-activation-validation-checklist)
- [Future Enhancements](#future-enhancements)
- [Summary](#summary)

---

## Overview

The skill-developer system demonstrates a sophisticated two-hook auto-activation framework that balances proactive skill discovery with reactive guardrail enforcement. This document captures the proven patterns for implementing similar systems.

**Key Achievement:** Skills activate contextually based on keywords, intent patterns, file paths, and content - transforming passive documentation into active assistance.

---

## Core Patterns

### Two-Hook Architecture

**Pattern:** Separate proactive suggestions from reactive enforcement.

**Implementation:**
1. **UserPromptSubmit Hook** - Suggests relevant skills BEFORE Claude processes prompt
2. **PreToolUse Hook** - Blocks file edits until critical guardrails satisfied

**Why it works:**
- Proactive suggestions make skills visible early in conversation
- Blocking enforcement prevents critical errors without constant nagging
- Separation of concerns keeps each hook focused and performant

**Example:**
```typescript
// UserPromptSubmit: Inject suggestion
if (matchesKeywords(prompt, skill.keywords)) {
  console.log(`📚 RECOMMENDED SKILL: ${skill.name}`);
}

// PreToolUse: Block if critical
if (matchesGuardrail(filePath, content)) {
  console.error(`⚠️ BLOCKED - Use skill: ${skill.name}`);
  process.exit(2); // Critical: Exit code 2 sends message to Claude
}
```

### Progressive Disclosure Through Reference Files

**Pattern:** Keep main skill file under 500 lines, organize detailed information in reference files.

**Implementation:**
- `SKILL.md` - High-level overview, navigation, quick reference (< 500 lines)
- `references/*.md` - Deep dives on specific topics (< 500 lines each)
- Table of contents for reference files > 100 lines

**Why it works:**
- Prevents context bloat - Claude only loads what's needed
- Maintains comprehensive documentation without overwhelming
- Enables focused updates without touching entire skill

**Example Structure:**
```
skill-developer/
├── SKILL.md (423 lines)
└── resources/
    ├── TRIGGER_TYPES.md (306 lines)
    ├── HOOK_MECHANISMS.md (307 lines)
    ├── TROUBLESHOOTING.md (515 lines)
    └── PATTERNS_LIBRARY.md (153 lines)
```

### Multi-Layer Trigger System

**Pattern:** Combine explicit (keywords) and implicit (intent) triggers with context (file paths, content).

**Four Trigger Types:**
1. **Keywords** - Explicit topic mentions (case-insensitive substring)
2. **Intent Patterns** - Implicit action detection (regex)
3. **File Path Patterns** - Location-based activation (glob)
4. **Content Patterns** - Technology detection in code (regex)

**Why it works:**
- Keywords catch explicit mentions: "how does layout work?"
- Intent patterns catch implicit actions: "add user tracking"
- File paths provide context: editing `services/user.ts`
- Content patterns detect actual usage: `import { PrismaService }`

**Example Configuration:**
```json
{
  "database-verification": {
    "promptTriggers": {
      "keywords": ["prisma", "database", "query"],
      "intentPatterns": ["(add|create).*?(user|feature)"]
    },
    "fileTriggers": {
      "pathPatterns": ["**/services/**/*.ts"],
      "contentPatterns": ["import.*[Pp]risma", "prisma\\."]
    }
  }
}
```

---

## Trigger System Design

### Keyword Triggers - Explicit Topic Matching

**Best Practices:**
- Include common variations: "layout", "layout system", "grid layout"
- Avoid overly generic words: "system", "work", "create"
- Use specific, unambiguous terms
- Test with real user prompts

**Anti-Patterns:**
```json
// ❌ Too generic
"keywords": ["user", "system", "create"]

// ✅ Specific variations
"keywords": [
  "user authentication",
  "user tracking",
  "prisma queries"
]
```

### Intent Patterns - Implicit Action Detection

**Regex Pattern Library:**
```regex
# Feature creation
(add|create|implement|build).*?(feature|endpoint|route)

# Component work
(create|add|make).*?(component|UI|page|modal)

# Database operations
(add|create|modify).*?(table|column|schema)

# Error handling
(fix|handle|catch|debug).*?(error|exception|bug)

# Explanations
(how does|explain|what is|describe).*?
```

**Critical Techniques:**
- Use non-greedy matching: `.*?` not `.*`
- Escape special characters: `\\.findMany\\(` not `.findMany(`
- Test on https://regex101.com/
- Balance specificity vs sensitivity

**Anti-Patterns:**
```regex
# ❌ Too broad - matches everything
(create)

# ✅ Context-aware
(create|add).*?(database|table|feature)
```

### File Path Triggers - Location-Based Activation

**Glob Pattern Strategies:**
```glob
# ✅ Specific directories
frontend/src/components/**/*.tsx
form/src/services/**/*.ts

# ❌ Too broad
form/**
**/*.ts

# ✅ Wildcard for any location
**/schema.prisma
**/migrations/**/*.sql

# ✅ Exclusions for tests
**/*.test.ts
**/*.spec.ts
```

**Performance Impact:**
- Narrow patterns = fewer files checked = faster
- `form/src/services/**` better than `form/**`
- Use exclusions to skip test files

### Content Patterns - Technology Detection

**Proven Patterns:**
```regex
# Prisma/Database
import.*[Pp]risma              # Prisma imports
PrismaService                  # Service usage
prisma\.                       # prisma.something
\.findMany\(                   # Query methods

# React/Components
export.*React\.FC              # Functional components
useState|useEffect             # React hooks

# Controllers/Routes
export class.*Controller       # Controller classes
router\.                       # Express router
```

**Critical Rules:**
- Escape special regex characters
- Match imports and actual usage
- Use case-insensitive where needed: `[Pp]risma`
- Test against real file content

---

## Enforcement Strategies

### Enforcement Levels - Graduated Guardrails

**Three Levels:**

1. **BLOCK (Critical)** - Exit code 2, prevents file edit
   - Use for: Data integrity, security, critical errors
   - Example: Database column verification

2. **SUGGEST (Recommended)** - Context injection, advisory
   - Use for: Best practices, domain guidance
   - Example: Frontend development patterns

3. **WARN (Optional)** - Low priority, informational
   - Rarely used - most skills are BLOCK or SUGGEST

**Decision Matrix:**
```
Mistake causes runtime error? → BLOCK
Data integrity at risk? → BLOCK
Security vulnerability? → BLOCK
Best practice guidance? → SUGGEST
Nice-to-have optimization? → WARN
```

### Block Messages - Actionable Communication

**Template:**
```
⚠️ BLOCKED - [Clear Problem Statement]

📋 REQUIRED ACTION:
1. [Specific step with Skill tool name]
2. [What to verify/check]
3. [How to proceed after]

Reason: [Why this matters]
File: {file_path}

💡 TIP: [Escape hatch like file markers]
```

**Critical Requirements:**
- Clear actionable steps (numbered)
- Include skill name for Skill tool
- Use `{file_path}` placeholder
- Explain WHY (prevents frustration)
- Provide escape hatches

### Exit Code 2 - The Critical Mechanism

**Why Exit Code 2 Matters:**
- **ONLY way** to send message from PreToolUse to Claude
- stderr content "fed back to Claude automatically"
- Tool execution is BLOCKED until resolved
- This is THE enforcement mechanism

**Implementation:**
```typescript
// PreToolUse hook
if (shouldBlock) {
  console.error(blockMessage); // stderr → Claude
  process.exit(2);             // CRITICAL: Exit code 2
}

// Allow
process.exit(0);
```

**Exit Code Reference:**
| Code | stdout | stderr | Tool Execution | Claude Sees |
|------|--------|--------|----------------|-------------|
| 0    | User   | User   | **Proceeds**   | Nothing     |
| 2    | User   | **CLAUDE** | **BLOCKED** | stderr content |

---

## Session Management

### Session Tracking - Preventing Repeated Nagging

**Pattern:** Remember which skills used in current conversation.

**State File:** `.claude/hooks/state/skills-used-{session_id}.json`

**Behavior:**
1. First edit → Hook blocks, adds skill to `skills_used`
2. Second edit (same session) → Hook allows
3. Different session → Blocks again

**Why it works:**
- Balances protective guardrails with user experience
- Prevents repeated blocks in same conversation
- Resets between conversations (different sessions)

**Limitation:** Cannot detect actual Skill tool usage - trusts Claude follows instructions.

### Skip Conditions - User Control

**Three Escape Hatches:**

1. **Session Tracking** - Automatic, prevents repeat nags
   ```typescript
   if (sessionState.skills_used.includes(skillName)) {
     process.exit(0); // Allow
   }
   ```

2. **File Markers** - Permanent skip for verified files
   ```typescript
   // In file: // @skip-validation
   if (fileContent.includes('@skip-validation')) {
     process.exit(0); // Allow
   }
   ```

3. **Environment Variables** - Emergency disable
   ```bash
   export SKIP_DB_VERIFICATION=true
   export SKIP_SKILL_GUARDRAILS=true  # Disables ALL
   ```

**Philosophy:** Rules need escape hatches for edge cases and user autonomy.

---

## Performance Optimization

### Target Metrics

**Performance Targets:**
- UserPromptSubmit: < 100ms
- PreToolUse: < 200ms

**Why:** Prevent noticeable workflow delays.

### Optimization Strategies

**1. Pattern Specificity**
```json
// ❌ Checks too many files
"pathPatterns": ["**/*.ts"]

// ✅ Narrow scope
"pathPatterns": ["form/src/services/**/*.ts"]
```

**2. Combine Similar Patterns**
```regex
// ❌ Multiple patterns
\\.findMany\\(
\\.findUnique\\(
\\.findFirst\\(

// ✅ Combined
\\.(findMany|findUnique|findFirst)\\(
```

**3. Content Pattern Efficiency**
- Only use when necessary (reads entire file)
- Simpler regex = faster matching
- Test performance with `time` command

**4. Regex Optimization**
```regex
// ❌ Long alternation (slow)
(create|add|modify|update|implement|build).*?(feature|endpoint|route|service)

// ✅ Simplified
(create|add).*?(feature|endpoint)
```

### Performance Measurement

```bash
# Measure UserPromptSubmit
time echo '{"prompt":"test"}' | npx tsx skill-activation-prompt.ts

# Measure PreToolUse
time cat <<'EOF' | npx tsx skill-verification-guard.ts
{"tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

---

## Key Insights

### Systems That Anticipate Needs

**Insight:** Proactive skill suggestions prevent problems before they occur.

**Application:** UserPromptSubmit hook activates BEFORE Claude processes prompt, making relevant skills contextually aware from the start.

### Gentle Reminders vs Blocking Friction

**Insight:** Gentle reminders maintain quality awareness without blocking workflow.

**Application:** Philosophy change (2025-10-27) moved from blocking PreToolUse for error handling to gentle post-response reminders.

### Patterns Reveal Intent

**Insight:** Regex patterns detect user intent more reliably than explicit statements.

**Application:** Intent patterns like `(create|add).*?(feature)` catch implicit actions when users don't mention specific technologies.

### Specificity Reduces False Positives

**Insight:** Specific patterns improve relevance dramatically while reducing noise.

**Application:** `form/src/services/**` catches relevant files while excluding tests, configs, and unrelated code.

### Progressive Disclosure Scales Documentation

**Insight:** Reference files respect cognitive load while maintaining comprehensive accessibility.

**Application:** 500-line main skill file with five focused reference files provides complete documentation without overwhelming context.

### Configuration-Driven Evolution

**Insight:** Configuration files enable teams to evolve practices without code changes.

**Application:** skill-rules.json allows pattern updates, new triggers, and enforcement changes without touching hook implementation.

### Exit Codes Bridge Systems

**Insight:** Simple conventions enable sophisticated bidirectional communication.

**Application:** Exit code 2 creates feedback loop from hook to Claude, enabling automated enforcement.

### Test-First Documentation

**Insight:** Skills should solve real problems before extensive documentation investment.

**Application:** Build 3+ evaluations BEFORE documenting - ensures skill addresses actual gaps.

---

## Implementation Wisdom

### From skill-developer Production Usage

**Philosophy Change (2025-10-27):**
> "We moved away from blocking PreToolUse for Sentry/error handling. Instead, use gentle post-response reminders that don't block workflow but maintain code quality awareness."

**Lesson:** Not everything needs blocking enforcement. Sometimes gentle awareness is more effective than friction.

**On Session Tracking:**
> "Trust that Claude follows the instruction"

**Lesson:** Perfect detection isn't always necessary. Session tracking prevents nagging while trusting Claude's judgment.

**On Pattern Testing:**
> "Test with 3+ real scenarios before documenting"

**Lesson:** Real usage reveals gaps that theoretical planning misses.

**On Performance:**
> "More specific patterns (fewer to check)"

**Lesson:** Specificity improves both relevance AND performance.

**On Escape Hatches:**
> "Fail open: On errors, allows operation (don't break workflow)"

**Lesson:** Robustness means degrading gracefully, not breaking on edge cases.

---

## Best Practices

### Trigger Configuration

**DO:**
- ✅ Use specific, unambiguous keywords
- ✅ Test all patterns with real examples
- ✅ Include common variations
- ✅ Use non-greedy regex: `.*?`
- ✅ Escape special characters in content patterns
- ✅ Add exclusions for test files
- ✅ Make file path patterns narrow and specific

**DON'T:**
- ❌ Use overly generic keywords ("system", "work")
- ❌ Make intent patterns too broad (false positives)
- ❌ Make patterns too specific (false negatives)
- ❌ Forget to test with regex tester
- ❌ Use greedy regex: `.*` instead of `.*?`
- ❌ Match too broadly in file paths

### Testing Workflow

**Manual Hook Testing:**
```bash
# UserPromptSubmit
echo '{"prompt":"your test"}' | npx tsx skill-activation-prompt.ts

# PreToolUse
cat <<'EOF' | npx tsx skill-verification-guard.ts
{"tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

**Validation:**
```bash
# JSON syntax
cat skill-rules.json | jq .

# Common errors: trailing commas, missing quotes, single quotes
```

**Testing Checklist:**
- [ ] Keywords tested with real prompts
- [ ] Intent patterns tested with variations
- [ ] File paths tested with actual files
- [ ] Content patterns tested against file contents
- [ ] Performance measured (< 100ms / < 200ms)
- [ ] JSON syntax validated
- [ ] No false positives in testing
- [ ] No false negatives in testing

### Skill Quality Standards

**From skill-developer:**
- ✅ SKILL.md under 500 lines
- ✅ Progressive disclosure with reference files
- ✅ Table of contents for files > 100 lines
- ✅ One-level-deep reference structure
- ✅ Rich descriptions with trigger keywords (< 1024 chars)
- ✅ Test first: 3+ evaluations before documentation
- ✅ Gerund naming: prefer verb-ing forms

### Documentation Pattern

**Main SKILL.md Structure:**
1. Purpose & When to Use
2. Quick Start
3. Key Concepts (high-level)
4. Reference File Links
5. Quick Reference Summary

**Reference File Structure:**
1. Table of Contents (if > 100 lines)
2. Detailed Topic Coverage
3. Examples
4. Related Files Links

---

## Testing Commands Quick Reference

### Manual Hook Testing

**UserPromptSubmit Hook:**
```bash
# Test if hook triggers on specific prompt
echo '{"session_id":"debug","prompt":"your test prompt here"}' | \
  npx tsx .claude/hooks/skill-activation-prompt.ts

# Expected: Skill suggestions in stdout if patterns match
```

**PreToolUse Hook:**
```bash
# Test if hook blocks on specific file edit
cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts 2>&1
{
  "session_id": "debug",
  "tool_name": "Edit",
  "tool_input": {"file_path": "/path/to/test/file.ts"}
}
EOF
echo "Exit code: $?"

# Expected:
# - Exit code 2 + stderr message if should block
# - Exit code 0 + no output if should allow
```

### Session State Debugging

**Check session state:**
```bash
# List session state files
ls .claude/hooks/state/

# View skills used in session
cat .claude/hooks/state/skills-used-{session-id}.json

# Example output:
# {
#   "skills_used": ["database-verification", "error-tracking"],
#   "files_verified": []
# }
```

**Reset session state:**
```bash
# Delete state file to reset for current session
rm .claude/hooks/state/skills-used-{session-id}.json
```

### File Marker Checking

**Check for skip markers:**
```bash
# Search for @skip-validation marker in file
grep "@skip-validation" path/to/file.ts

# If found, file is permanently skipped
```

### Environment Variable Debugging

**Check override variables:**
```bash
# Check skill-specific override
echo $SKIP_DB_VERIFICATION

# Check global override
echo $SKIP_SKILL_GUARDRAILS

# Unset to re-enable
unset SKIP_DB_VERIFICATION
unset SKIP_SKILL_GUARDRAILS
```

### JSON Validation

**Validate skill-rules.json syntax:**
```bash
# Check JSON syntax (pretty-prints if valid, shows error if invalid)
cat .claude/skills/skill-rules.json | jq .

# Common errors to look for:
# - Trailing commas: {"keywords": ["one", "two",]} ❌
# - Missing quotes: {type: "guardrail"} ❌
# - Single quotes: {'type': 'guardrail'} ❌ (must use double quotes)
```

### Performance Measurement

**Measure hook execution time:**
```bash
# UserPromptSubmit (target: < 100ms)
time echo '{"prompt":"test"}' | npx tsx .claude/hooks/skill-activation-prompt.ts

# PreToolUse (target: < 200ms)
time cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts
{"tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

**Target Metrics:**
- UserPromptSubmit: < 100ms
- PreToolUse: < 200ms

**If slower:** Reduce pattern count, simplify regex, narrow file path patterns

### Hook Execution Debugging

**Verify hook registration:**
```bash
# Check if hooks registered in settings
cat .claude/settings.json | jq '.hooks.UserPromptSubmit'
cat .claude/settings.json | jq '.hooks.PreToolUse'
```

**Check hook file permissions:**
```bash
# Verify hooks are executable
ls -l .claude/hooks/*.sh
# Expected: -rwxr-xr-x (executable bit set)

# Make executable if needed
chmod +x .claude/hooks/*.sh
```

**Test TypeScript compilation:**
```bash
# Check for TypeScript errors in hooks
cd .claude/hooks
npx tsc --noEmit skill-activation-prompt.ts
npx tsc --noEmit skill-verification-guard.ts
# Expected: No output (no errors)
```

---

## Auto-Activation Validation Checklist

When creating or modifying auto-activation systems, verify:

### Configuration Validation
- [ ] skill-rules.json syntax valid (`cat skill-rules.json | jq .`)
- [ ] All skill names match SKILL.md filenames exactly
- [ ] Guardrails have `blockMessage` configured
- [ ] Block messages use `{file_path}` placeholder
- [ ] Priority level matches enforcement level
- [ ] No duplicate skill names

### Trigger Pattern Validation
- [ ] Keywords tested with real prompts (3+ examples)
- [ ] Intent patterns tested with variations (use regex101.com)
- [ ] File path patterns tested with actual file paths
- [ ] Content patterns tested against real file contents
- [ ] Intent patterns escape special regex characters
- [ ] File path patterns use correct glob syntax
- [ ] No overly generic keywords ("system", "work", "create")
- [ ] Patterns use non-greedy matching (`.*?` not `.*`)

### Hook Validation
- [ ] Hooks registered in `.claude/settings.json`
- [ ] Hook files executable (`chmod +x .claude/hooks/*.sh`)
- [ ] Correct shebang (`#!/bin/bash`) in shell scripts
- [ ] npx/tsx available (`npx tsx --version`)
- [ ] TypeScript compiles without errors
- [ ] UserPromptSubmit returns exit code 0
- [ ] PreToolUse returns exit code 0 (allow) or 2 (block)

### Performance Validation
- [ ] UserPromptSubmit executes < 100ms
- [ ] PreToolUse executes < 200ms
- [ ] Pattern count is reasonable (< 20 per skill)
- [ ] File path patterns are specific (not `**/*`)
- [ ] Regex patterns are optimized (combined where possible)

### Behavioral Validation
- [ ] No false positives in testing (10+ test prompts)
- [ ] No false negatives in testing (10+ test prompts)
- [ ] Session tracking prevents repeated blocks
- [ ] File markers work (`@skip-validation`)
- [ ] Environment overrides work (`SKIP_*`)
- [ ] Block messages are clear and actionable

### Testing Coverage
- [ ] Manual hook testing completed
- [ ] Session state behavior verified
- [ ] File marker behavior verified
- [ ] Environment override behavior verified
- [ ] Edge cases tested (empty files, missing files, etc.)
- [ ] Performance measured and acceptable

---

## Future Enhancements

Ideas and concepts for evolving auto-activation systems, drawn from skill-developer's ADVANCED.md vision.

### Dynamic Rule Updates

**Current Limitation:** Requires Claude Code restart to pick up changes to skill-rules.json

**Future Enhancement:** Hot-reload configuration without restart

**Implementation Ideas:**
- Watch skill-rules.json for changes
- Reload on file modification
- Invalidate cached compiled regexes
- Notify user of reload

**Benefits:**
- Faster iteration during skill development
- No need to restart Claude Code
- Better developer experience

### Skill Dependencies

**Current Limitation:** Skills are independent

**Future Enhancement:** Specify skill dependencies and load order

**Configuration Idea:**
```json
{
  "my-advanced-skill": {
    "dependsOn": ["prerequisite-skill", "base-skill"],
    "type": "domain",
    ...
  }
}
```

**Use Cases:**
- Advanced skill builds on base skill knowledge
- Ensure foundational skills loaded first
- Chain skills for complex workflows

**Benefits:**
- Better skill composition
- Clearer skill relationships
- Progressive disclosure of complexity

### Conditional Enforcement

**Current Limitation:** Enforcement level is static

**Future Enhancement:** Enforce based on context or environment

**Configuration Idea:**
```json
{
  "enforcement": {
    "default": "suggest",
    "when": {
      "production": "block",
      "development": "suggest",
      "ci": "block"
    }
  }
}
```

**Use Cases:**
- Stricter enforcement in production
- Relaxed rules during development
- CI/CD pipeline requirements

**Benefits:**
- Environment-appropriate enforcement
- Flexible rule application
- Context-aware guardrails

### Skill Analytics

**Current Limitation:** No usage tracking

**Future Enhancement:** Track skill usage patterns and effectiveness

**Metrics to Collect:**
- Skill trigger frequency
- False positive rate
- False negative rate
- Time to skill usage after suggestion
- User override rate (skip markers, env vars)
- Performance metrics (execution time)

**Dashboard Ideas:**
- Most/least used skills
- Skills with highest false positive rate
- Performance bottlenecks
- Skill effectiveness scores

**Benefits:**
- Data-driven skill improvement
- Identify problems early
- Optimize patterns based on real usage

### Skill Versioning

**Current Limitation:** No version tracking

**Future Enhancement:** Version skills and track compatibility

**Configuration Idea:**
```json
{
  "my-skill": {
    "version": "2.1.0",
    "minClaudeVersion": "1.5.0",
    "changelog": "Added support for new workflow patterns",
    ...
  }
}
```

**Benefits:**
- Track skill evolution
- Ensure compatibility
- Document changes
- Support migration paths

### Skill Testing Framework

**Current Limitation:** Manual testing with npx tsx commands

**Future Enhancement:** Automated skill testing

**Features:**
- Test cases for trigger patterns
- Assertion framework
- CI/CD integration
- Coverage reports

**Example Test:**
```typescript
describe('database-verification', () => {
  it('triggers on Prisma imports', () => {
    const result = testSkill({
      prompt: "add user tracking",
      file: "services/user.ts",
      content: "import { PrismaService } from './prisma'"
    });

    expect(result.triggered).toBe(true);
    expect(result.skill).toBe('database-verification');
  });

  it('blocks on Prisma query without verification', () => {
    const result = testPreToolUse({
      file: "services/user.ts",
      content: "prisma.user.findMany()",
      sessionState: { skills_used: [] }
    });

    expect(result.blocked).toBe(true);
    expect(result.exitCode).toBe(2);
  });
});
```

**Benefits:**
- Prevent regressions
- Validate patterns before deployment
- Confidence in changes
- Documentation through tests

### Multi-Language Support

**Current Limitation:** English only

**Future Enhancement:** Support multiple languages for skill content

**Implementation Ideas:**
- Language-specific SKILL.md variants (`SKILL.es.md`, `SKILL.fr.md`)
- Automatic language detection from user locale
- Fallback to English if translation unavailable

**Use Cases:**
- International teams
- Localized documentation
- Multi-language projects

### Actual Skill Usage Detection

**Current Limitation:** Session tracking updates on first block, not on actual Skill tool usage

**Future Enhancement:** Detect when Claude actually uses the Skill tool

**Implementation Ideas:**
- Hook into Skill tool execution
- Track actual skill usage vs. enforcement
- Update session state only after verified usage

**Benefits:**
- More accurate session tracking
- Ensures guardrails aren't bypassed
- Better analytics

---

## Summary

The skill-developer system demonstrates that effective auto-activation requires:

1. **Two-hook architecture** separating proactive suggestions from reactive enforcement
2. **Multi-layer triggers** combining keywords, intent, file paths, and content
3. **Session-aware state** preventing repeated nagging while maintaining guardrails
4. **Progressive disclosure** keeping content focused and context efficient
5. **Performance optimization** through pattern specificity and efficient regex
6. **User control** via session tracking, file markers, and environment variables
7. **Test-first approach** ensuring skills solve real problems before documentation

**Core Philosophy:** Balance protective guardrails with user experience through graduated enforcement, escape hatches, and performance-conscious pattern design.

**Key Takeaway:** Systems that anticipate needs, detect patterns, and communicate clearly create assistance that feels intelligent rather than intrusive.
