# UX Writing

> **v1.0.10** | Design & UX | 11 iterations

Write effective microcopy, error messages, button labels, and interface text using UX writing principles.

## What Problem Does This Solve

Interface text is often written by engineers as an afterthought -- "Submit", "Error 404", "Click here" -- leaving users confused about what just happened or what to do next. Every label, error message, button, and empty state is a design decision that either guides the user toward success or creates friction. A "Submit" button does not tell the user what they are submitting. "Error 404" does not tell them what to do about it. "Click here" does not tell them why they should.

This skill treats interface copy as a UX discipline, not a fill-in-the-blank exercise. It provides the Clear-Concise-Useful-Human framework, tone guidelines calibrated by context (success, error, warning, empty state), and concrete before/after rewrites for the most common UI text patterns -- buttons, errors, confirmation dialogs, and form labels.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install ux-writing@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

**Direct invocation:**

```
Use the ux-writing skill to improve the error messages in my form
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `ux-writing`
- `microcopy`
- `error-messages`

## What's Inside

This is a **single-skill plugin** with no reference documents and two eval suites.

| Component | Path | Purpose |
|---|---|---|
| Skill | `skills/ux-writing/SKILL.md` | Core principles, tone-by-context guidance, and four UI pattern rewrites |
| Evals | `evals/trigger-evals.json` | Trigger scenarios for activation boundary testing |
| Evals | `evals/evals.json` | Output quality scenarios for copy improvement |

**The four principles:**

| Principle | What it means in practice |
|---|---|
| Clear | Simple words, active voice, no jargon |
| Concise | Front-load the key information, cut filler |
| Useful | Always provide a next step the user can take |
| Human | Empathetic and conversational, not robotic |

**Tone calibrated by context:**

| Context | Tone | Example |
|---|---|---|
| Success | Celebratory | "You're all set!" |
| Error | Helpful | "Let's fix this" |
| Warning | Direct | "This can't be undone" |
| Empty state | Encouraging | "Create your first..." |

## Usage Scenarios

**1. "Write better error messages for my form validation"**
The skill applies the error message pattern: human-readable description of what went wrong plus a specific next step to resolve it. Instead of "Error 404" or "Invalid input", you get "Page not found -- try searching or go to homepage" or "Email address needs an @ symbol".

**2. "The submit button just says 'Submit' -- how do I improve it?"**
The Verb + Object formula replaces generic labels with action-specific ones. "Submit" becomes "Save changes". "Click here" becomes "Download report". "OK" becomes "Confirm deletion". The verb tells the user what will happen; the object tells them what it applies to.

**3. "Users don't know what to do on the empty state screen"**
The empty state copy pattern describes what the feature does and provides a clear first action. Instead of a blank page or "No items found", the user sees "Create your first project to start organizing your work" with a visible action button.

**4. "Write a confirmation dialog for a destructive action"**
The confirmation dialog template uses an action-specific title ("Delete 'Report'?"), an irreversibility warning ("This can't be undone"), and labeled confirm/cancel buttons where the confirm button uses the destructive verb ("[Delete]") rather than a generic "[OK]".

**5. "My error messages are too technical for end users"**
The tone-by-context guidance transforms technical error codes into helpful copy. The error tone is "helpful, not blaming" -- the copy acknowledges what went wrong without jargon and immediately offers the user something they can do about it.

## When to Use / When NOT to Use

**Use when:**
- Writing or rewriting button labels, error messages, or confirmation dialogs
- Improving empty state copy that leaves users confused
- Reviewing interface text for clarity and actionability
- Establishing a tone guide for UI copy across your product
- Training a team on UX writing principles

**Do NOT use when:**
- Generating long-form documentation -- use [documentation-generator](../documentation-generator/) instead
- Designing the visual layout or navigation patterns -- use [frontend-design](../frontend-design/) or [navigation-design](../navigation-design/)
- Creating content models for a CMS -- use [content-modelling](../content-modelling/) instead

## Related Plugins in SkillStack

- **[User Journey Design](../user-journey-design/)** -- Map the journeys where your microcopy appears at each touchpoint
- **[Persona Definition](../persona-definition/)** -- Understand who reads your copy so tone and vocabulary match
- **[Navigation Design](../navigation-design/)** -- Design the navigation labels and wayfinding text
- **[Content Modelling](../content-modelling/)** -- Structure the content types that contain your copy
- **[Frontend Design](../frontend-design/)** -- Design the visual components where your copy lives

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
