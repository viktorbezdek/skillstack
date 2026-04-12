# Build vs Fork vs Contribute vs Skip

> The decision tree for what to do once you've completed the marketplace survey. Four outcomes, specific criteria for each.

---

## The decision tree

```
Did the marketplace survey find ANY plugin that covers your use case?
│
├── NO ──────────────────────────────────────→ BUILD
│
└── YES
     │
     ├── Does it fully cover your requirements?
     │    ├── YES → INSTALL IT AND SKIP (ship is cheaper than build)
     │    └── NO (gaps exist) ↓
     │
     ├── Is the existing plugin actively maintained?
     │    (commits in last 6 months + issues being answered)
     │    │
     │    ├── NO (abandoned) ────────────────→ FORK
     │    │
     │    └── YES
     │         │
     │         ├── Does the maintainer welcome contributions?
     │         │    (CONTRIBUTING.md present, recent merged PRs)
     │         │    │
     │         │    ├── YES → Is your change on their roadmap or acceptable scope?
     │         │    │    ├── YES → CONTRIBUTE
     │         │    │    └── NO → FORK (different vision)
     │         │    │
     │         │    └── NO (cold to PRs) → FORK
     │         │
     │         └── License compatible with your intended use?
     │              ├── YES → (see branches above)
     │              └── NO → BUILD from scratch to avoid contamination
```

---

## Detailed criteria

### BUILD from scratch when

1. **Nothing equivalent exists** — survey found 0 relevant plugins
2. **Existing plugins are stale** — no commits in 12+ months, no response to issues
3. **Existing plugins are wrong-fit** — they cover adjacent but not overlapping ground
4. **License incompatible** — existing plugin is GPL, you need MIT; or vice versa
5. **You need control over the roadmap** — you expect to extend rapidly and don't want to wait on upstream

**Checklist before building**:
- [ ] Survey complete, results documented
- [ ] `plugin-ideation` 7-criteria checklist passed (≥5/7)
- [ ] Authoritative sources read (the relevant ones from `authoritative-sources.md`)
- [ ] You can name the existing plugins you're NOT using, and why

### FORK when

1. **Existing plugin is close but has gaps** that would require significant rework upstream
2. **Upstream is abandoned or inactive** (no response to PRs/issues in 3+ months)
3. **Your vision differs enough** that merging back doesn't make sense
4. **You're willing to maintain the fork** — don't fork and abandon

**Checklist before forking**:
- [ ] You've tried filing an issue or PR upstream (and gotten no response OR a "not interested" reply)
- [ ] Your fork will be credited to the original author in the new plugin's manifest and README
- [ ] The license permits forking (most do; double-check)
- [ ] You have a plan for keeping the fork's core improvements visible to upstream users

### CONTRIBUTE when

1. **Existing plugin is close and actively maintained**
2. **Your change fits the upstream roadmap** — maintainer would accept it
3. **You want long-term shared maintenance** — smaller surface area for you to own
4. **The upstream project has a healthy PR process** (CONTRIBUTING.md, CI, review culture)

**Checklist before contributing**:
- [ ] Read CONTRIBUTING.md (if present)
- [ ] Open an issue first to align on scope before writing code
- [ ] Fork, branch, PR — don't push to main
- [ ] Write tests; respect existing code style

### SKIP when

1. **Existing plugin fully covers the use case** — install it and move on
2. **Your idea scored <10/21 on `plugin-ideation`'s 7-criteria test** — it's not plugin-shaped
3. **Maintenance cost exceeds value** — you'd be supporting it alone forever
4. **You'd be rebuilding just to rebuild** — engineering exercise disguised as a project

**Skipping is a success.** The plugin you didn't build is the plugin that doesn't have bugs, doesn't need updates, and doesn't steal time from higher-leverage work.

---

## Worked examples

### Example 1: BUILD (clear gap)

**Idea**: "A plugin that teaches the AI-slop-cleaner methodology."

**Survey result**: Nothing in Anthropic's bundled plugins, nothing in skillstack, nothing on GitHub with matching description.

**Decision**: BUILD — no prior art, methodology is proprietary to the team that wrote it.

### Example 2: SKIP (already solved)

**Idea**: "A plugin for authoring new skills with frontmatter templates."

**Survey result**: Anthropic ships `skill-creator` as a bundled plugin. It already does this.

**Decision**: SKIP — install `skill-creator`, use it directly. Document it in your team's onboarding instead of building a duplicate.

### Example 3: FORK (abandoned upstream)

**Idea**: "A hook-based secret scanner that blocks commits containing credentials."

**Survey result**: Found `secret-scanner-hooks` by someone on GitHub. Last commit: 2024. Issues unanswered since 2025. Uses outdated matcher syntax.

**Decision**: FORK — upstream is dead, codebase is close, fork lets you modernize the matcher syntax and keep shipping.

### Example 4: CONTRIBUTE (active upstream, small change)

**Idea**: "Add a `--strict` flag to a popular validator plugin."

**Survey result**: Found the validator, it's actively maintained, CONTRIBUTING.md exists, maintainer answers PRs within days.

**Decision**: CONTRIBUTE — open an issue describing the `--strict` behavior, get alignment, then PR it.

### Example 5: BUILD despite existing (license mismatch)

**Idea**: "A plugin to enforce our company's internal commit format."

**Survey result**: A similar plugin exists but is GPL-licensed. Your company's policy requires MIT.

**Decision**: BUILD — cannot use GPL, cannot link, cannot fork. Start fresh with MIT.

---

## Common wrong decisions

### "I'll fork because forking is easy"

Forking is easy to start and expensive to maintain. You now own everything upstream fixed — every bug, every compatibility issue. Only fork when you can commit to long-term maintenance.

### "I'll build from scratch because I don't trust other people's code"

Unless the existing plugin has a real problem (abandoned, license, incompatibility), building from scratch multiplies your own maintenance burden without solving anything.

### "I'll contribute but fork if they reject it"

If you know upstream won't accept the change, don't open a PR just to confirm it. Fork from the start and cite the decision.

### "I'll skip because the existing plugin is slightly wrong"

Measure "slightly wrong" carefully. 5 minutes of adaptation beats 5 days of fresh build. If the adaptation fits inside your own CLAUDE.md or settings, skip and adapt.

### "I'll build because I want to understand how plugins work"

Then build, but don't publish — build it as a learning exercise in a private repo. Don't add a learning-project plugin to the marketplace — it dilutes signal for everyone else searching for real plugins.

---

## After the decision

- **BUILD** → hand off to `plugin-architecture` for component design
- **FORK** → clone upstream, create new manifest, document the fork relationship in README
- **CONTRIBUTE** → file issue, wait for alignment, PR
- **SKIP** → install the existing plugin, document the decision in your notes (future-you will encounter the same idea again)
