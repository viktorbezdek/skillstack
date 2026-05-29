# deslop

Remove AI slop from UI copy, marketing text, and product content.

Three focused skills that cover the full cleanup pipeline: detecting and removing AI patterns from interface text, humanizing marketing and editorial prose, and preventing AI content detector flags.

## Skills

### `deslop-ui`
Audits and rewrites UI copy — button labels, error messages, empty states, tooltips, onboarding text, and success messages. Removes the AI fingerprint from interface text: overlong labels, hedging error messages, gratuitous politeness, corporate superlatives, passive voice, and verbose empty states.

### `deslop-copy`
Removes AI clichés from marketing copy, blog posts, product descriptions, emails, and editorial content — and humanizes the result. Includes a 40+ word blacklist (leverage, delve, comprehensive, cutting-edge, etc.), 10 humanization techniques, and a 5-pass rewriting workflow.

### `deslop-detect`
Rewrites AI-generated content to evade AI content detectors by increasing perplexity, burstiness, and lexical entropy. Covers GPTZero, Originality.ai, Turnitin, Copyleaks, ZeroGPT, and Sapling. Explains the signals each detector uses and provides targeted rewriting strategies.

## Installation

```
/plugin install deslop@skillstack
```

## Quick Start

```
# UI copy audit
deslop this UI copy: [paste buttons, errors, empty states]

# Marketing copy cleanup
deslop this landing page / humanize this blog post

# Detection evasion
make this pass GPTZero / reduce the AI score on this piece
```

## Trigger Keywords

- `deslop` — routes to the right skill based on context (UI text → deslop-ui, prose → deslop-copy)
- `anti-slop` — same routing logic
- `humanize` — triggers deslop-copy for prose, deslop-ui for interface text
- `AI slop`, `AI-generated` + cleanup intent — triggers the domain-appropriate skill
- `GPTZero`, `Originality.ai`, `Turnitin`, `AI detection` — triggers deslop-detect

## What This Plugin Is NOT

- Not a code cleanup tool — use `ai-slop-cleaner` for code
- Not a UX writing guide — use `ux-writing` for writing new microcopy from scratch
- Not an academic fraud tool — `deslop-detect` is for legitimate content creators

## Related Plugins

- [`ai-slop-cleaner`](https://github.com/viktorbezdek/oh-my-claudecode) — code-focused AI slop removal (oh-my-claudecode)
- [`ux-writing`](../ux-writing) — writing new UI microcopy from scratch
- [`storytelling`](../storytelling) — writing new marketing and narrative copy
