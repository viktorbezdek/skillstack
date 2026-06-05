#!/usr/bin/env python3
"""Generate docs/audit/01-inventory.md from _groundtruth.json."""
import json
from pathlib import Path

# ── Domain assignments (proposed 4-domain taxonomy) ──────────────────────────
# E=Engineering  M=Marketing-Comms  P=Managerial-Product  I=Meta-Infra
DOMAIN = {
    "agent-evaluation":          "I",
    "agent-project-development": "E",
    "api-design":                "E",
    "bdi-mental-states":         "E",
    "brainstorm-swarm":          "P",
    "cicd-pipelines":            "E",
    "cloud-finops":              "P",
    "code-review":               "E",
    "coding-discipline":         "E",
    "communication":             "M",
    "consistency-standards":     "I",
    "content-modelling":         "P",
    "context-compression":       "I",
    "context-degradation":       "I",
    "context-fundamentals":      "I",
    "context-optimization":      "I",
    "creative-problem-solving":  "P",
    "critical-intuition":        "I",
    "debugging":                 "E",
    "deslop":                    "M",
    "docker-containerization":   "E",
    "documentation-generator":   "E",
    "edge-case-coverage":        "E",
    "elicitation":               "I",
    "example-design":            "I",
    "filesystem-context":        "I",
    "frontend-design":           "E",
    "git-workflow":              "E",
    "gws-cli":                   "E",
    "hindsight":                 "I",
    "hosted-agents":             "E",
    "mcp-server":                "E",
    "memory-systems":            "I",
    "multi-agent-patterns":      "E",
    "navigation-design":         "E",
    "nextjs-development":        "E",
    "ontology-design":           "P",
    "osint":                     "I",
    "outcome-orientation":       "P",
    "persona-definition":        "P",
    "persona-mapping":           "P",
    "plugin-dev":                "I",
    "prioritization":            "P",
    "product-thinking":          "P",
    "prompt-engineering":        "I",
    "python-development":        "E",
    "react-development":         "E",
    "risk-management":           "P",
    "skill-foundry":             "I",
    "skillstack-workflows":      "I",
    "storytelling":              "M",
    "systems-thinking":          "P",
    "technical-copywriting":     "M",
    "test-driven-development":   "E",
    "testing-framework":         "E",
    "tool-design":               "E",
    "typescript-development":    "E",
    "user-journey-design":       "P",
    "ux-writing":                "M",
}

DOMAIN_NAMES = {
    "E": "Engineering",
    "M": "Marketing-Comms",
    "P": "Managerial-Product",
    "I": "Meta-Infra",
}

# ── Overlap clusters ──────────────────────────────────────────────────────────
OVERLAP_CLUSTER = {
    "context-compression":       "context-suite",
    "context-degradation":       "context-suite",
    "context-fundamentals":      "context-suite",
    "context-optimization":      "context-suite",
    "memory-systems":            "memory-state",
    "hindsight":                 "memory-state",
    "filesystem-context":        "memory-state",
    "persona-definition":        "persona",
    "persona-mapping":           "persona",
    "outcome-orientation":       "outcome-product",
    "product-thinking":          "outcome-product",
    "agent-evaluation":          "eval-quality",
    "skill-foundry":             "eval-quality",
    "testing-framework":         "eval-quality",
    "deslop":                    "copy-quality",
    "technical-copywriting":     "copy-quality",
    "ux-writing":                "copy-quality",
    "multi-agent-patterns":      "agent-dev",
    "agent-project-development": "agent-dev",
    "brainstorm-swarm":          "agent-dev",
}

# ── Granularity flags ─────────────────────────────────────────────────────────
# nano=1 skill, focused topic; large=10+ skills; suite=2-9 skills, related area
def granularity(p):
    s = p["skills"]
    if s == 1:
        return "nano"
    elif s <= 5:
        return "multi"
    elif s >= 10:
        return "large"
    return "multi"

# ── Verdict logic ─────────────────────────────────────────────────────────────
# keep / merge-candidate / split-candidate / rename-candidate / deprecate-candidate
VERDICT = {
    # context suite: complementary, keep all, but consider grouping
    "context-compression":   ("keep",   "Distinct scope: reduce size. Complements others in context-suite."),
    "context-degradation":   ("keep",   "Distinct scope: diagnose failures. No overlap with compression/optimization."),
    "context-fundamentals":  ("keep",   "Theory anchor for suite. Referenced by 10 plugins — high utility."),
    "context-optimization":  ("keep",   "Distinct scope: extend capacity via caching/partitioning."),
    # memory state cluster
    "memory-systems":        ("keep",   "General memory theory. Referenced by 10 plugins."),
    "hindsight":             ("keep",   "Operational memory (session persistence, hooks). Different from theory."),
    "filesystem-context":    ("merge-candidate", "Overlaps with memory-systems (state tracking). Merge into memory-systems or re-scope as 'workspace context'."),
    # persona cluster
    "persona-definition":    ("keep",   "User persona creation (demographics, empathy maps). Distinct output from persona-mapping."),
    "persona-mapping":       ("keep",   "Stakeholder mapping (RACI, Power-Interest). Different audience, different deliverable."),
    # outcome-product cluster
    "outcome-orientation":   ("merge-candidate", "Outcome framing overlaps with product-thinking's goal-alignment skills. Merge or clearly re-scope."),
    "product-thinking":      ("keep",   "5-skill suite with depth (PRDs, roadmaps, metrics, strategy). Primary product anchor."),
    # eval-quality cluster
    "agent-evaluation":      ("keep",   "LLM-as-judge, multi-dim rubrics, bias mitigation — specialist eval."),
    "skill-foundry":         ("keep",   "Plugin/skill authoring quality. Distinct lifecycle from agent evaluation."),
    "testing-framework":     ("keep",   "Code test strategy (TDD, coverage, integration). Different from LLM eval."),
    # copy-quality cluster
    "deslop":                ("keep",   "3 skills: AI-slop removal from editorial/marketing copy. Distinct from technical writing style."),
    "technical-copywriting": ("keep",   "5 skills: long-form technical article structure/distribution. Distinct audience/output."),
    "ux-writing":            ("keep",   "Microcopy/interface text. Different output format from both above."),
    # agent-dev cluster
    "multi-agent-patterns":  ("keep",   "Architecture patterns for multi-agent systems. Referenced by 13 plugins."),
    "agent-project-development": ("keep", "End-to-end agent project lifecycle. Different scope from patterns."),
    "brainstorm-swarm":      ("keep",   "12 agents + 4 skills + 1 cmd — interactive ideation runtime, not a pattern reference."),
}

# Fill in default verdicts
def get_verdict(plugin):
    if plugin in VERDICT:
        return VERDICT[plugin]
    return ("keep", "No overlap cluster. Unique domain and trigger surface.")

# ── Load ground truth ─────────────────────────────────────────────────────────
gt_path = Path("docs/audit/_groundtruth.json")
with open(gt_path) as f:
    data = json.load(f)

plugins = {p["plugin"]: p for p in data}

# ── Build table rows ──────────────────────────────────────────────────────────
DOMAIN_FULL = {
    "E": "Engineering",
    "M": "Marketing-Comms",
    "P": "Mgmt-Product",
    "I": "Meta-Infra",
}

rows = []
for p in data:
    name = p["plugin"]
    d = DOMAIN.get(name, "?")
    domain_str = DOMAIN_FULL.get(d, "?")

    # component string
    parts = []
    if p["skills"] > 0: parts.append(f"{p['skills']}sk")
    if p["agents"] > 0: parts.append(f"{p['agents']}ag")
    if p["cmds"] > 0:   parts.append(f"{p['cmds']}cmd")
    if p["hooks"]:       parts.append("hook")
    if p["scripts"]:     parts.append("scripts")
    comp = "+".join(parts) if parts else "-"

    # trigger quote (first 80 chars of first skill desc)
    trigger = ""
    if p["skill_detail"]:
        raw = p["skill_detail"][0]["desc"]
        # take up to first "NOT for" or first 100 chars
        idx = raw.find("NOT for")
        snippet = raw[:idx].strip() if idx > 0 else raw
        # trim to 90 chars
        snippet = snippet[:90].rstrip(",. ")
        trigger = f'"{snippet}…"'

    # deps (referenced_by top 3)
    refs = p.get("referenced_by", [])
    deps_str = ", ".join(refs[:3]) + ("…" if len(refs) > 3 else "") if refs else "—"

    # eval coverage
    has_ev = p.get("evals", 0) > 0
    has_tr = p.get("trig", 0) > 0
    has_bm = bool(p.get("bench", []))
    ev_parts = []
    if has_ev: ev_parts.append("E")
    if has_tr: ev_parts.append("T")
    if has_bm: ev_parts.append("B")
    ev_str = "+".join(ev_parts) if ev_parts else "—"

    gran = granularity(p)
    cluster = OVERLAP_CLUSTER.get(name, "—")
    verdict, rationale = get_verdict(name)

    rows.append({
        "plugin": name,
        "domain": domain_str,
        "domain_code": d,
        "comp": comp,
        "trigger": trigger,
        "refs_by": len(refs),
        "deps_str": deps_str,
        "ev": ev_str,
        "gran": gran,
        "cluster": cluster,
        "verdict": verdict,
        "rationale": rationale,
    })

# ── Counts ────────────────────────────────────────────────────────────────────
from collections import Counter
domain_counts = Counter(r["domain_code"] for r in rows)
verdict_counts = Counter(r["verdict"] for r in rows)
cluster_counts = Counter(r["cluster"] for r in rows if r["cluster"] != "—")

# ── Render markdown ───────────────────────────────────────────────────────────
lines = []
lines.append("# Phase 1: Plugin Inventory")
lines.append("")
lines.append("**Date:** 2026-06-05  **Status:** PENDING APPROVAL  **Source:** `docs/audit/_groundtruth.json`")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append(f"- **Total plugins:** {len(rows)}")
lines.append(f"- **Total skills:** {sum(p['skills'] for p in data)}")
lines.append(f"- **Total agents:** {sum(p['agents'] for p in data)}")
lines.append(f"- **Total commands:** {sum(p['cmds'] for p in data)}")
lines.append("")
lines.append("### Domain Distribution (proposed)")
lines.append("")
lines.append("| Domain | Count |")
lines.append("|--------|-------|")
for code in ["E", "I", "P", "M"]:
    lines.append(f"| {DOMAIN_NAMES[code]} ({code}) | {domain_counts[code]} |")
lines.append("")
lines.append("### Verdict Distribution")
lines.append("")
lines.append("| Verdict | Count |")
lines.append("|---------|-------|")
for v, c in sorted(verdict_counts.items()):
    lines.append(f"| {v} | {c} |")
lines.append("")
lines.append("## Overlap Clusters (evidence)")
lines.append("")

cluster_plugins = {}
for r in rows:
    c = r["cluster"]
    if c != "—":
        cluster_plugins.setdefault(c, []).append(r)

cluster_notes = {
    "context-suite": "4 plugins share 'context' namespace. Trigger surfaces are **distinct** (reduce / diagnose / theory / extend). Suite design, not duplication.",
    "memory-state":  "3 plugins handle agent state. `memory-systems` = theory, `hindsight` = session ops + hook, `filesystem-context` = workspace indexing. Partial overlap on 'track state' trigger — verify.",
    "persona":       "2 plugins: user-facing personas vs stakeholder mapping. Output artifacts differ (empathy map vs RACI). Low merge risk.",
    "outcome-product": "2 plugins: `outcome-orientation` trigger (goal framing, success metrics) overlaps `product-thinking` skill triggers. Merge-candidate if triggers confirm near-identity.",
    "eval-quality":  "3 plugins span: LLM eval (agent-evaluation), plugin authoring quality (skill-foundry), code test strategy (testing-framework). Different targets — same 'quality' concern.",
    "copy-quality":  "3 plugins: editorial slop removal (deslop), technical article structure (technical-copywriting), interface microcopy (ux-writing). Trigger surfaces distinct.",
    "agent-dev":     "3 plugins: architecture patterns (multi-agent-patterns), project lifecycle (agent-project-development), interactive ideation runtime (brainstorm-swarm). Low overlap.",
}

for cluster, crows in sorted(cluster_plugins.items()):
    lines.append(f"### `{cluster}`")
    lines.append("")
    note = cluster_notes.get(cluster, "")
    if note:
        lines.append(f"> {note}")
        lines.append("")
    lines.append("| Plugin | Trigger (excerpt) |")
    lines.append("|--------|-------------------|")
    for r in crows:
        lines.append(f"| `{r['plugin']}` | {r['trigger']} |")
    lines.append("")

lines.append("## Plugin Inventory Table")
lines.append("")
lines.append("**Column key:** Domain (E/I/P/M) · Components (sk=skills ag=agents cmd=commands) · Eval (E=evals T=trigger-evals B=benchmark) · Gran (nano=1sk multi=2-9 large=10+) · Cluster · Verdict")
lines.append("")

# Column widths look fine in raw markdown
lines.append("| Plugin | Domain | Comp | Trigger (excerpt) | Ref-by | Eval | Gran | Cluster | Verdict | Rationale |")
lines.append("|--------|--------|------|-------------------|--------|------|------|---------|---------|-----------|")
for r in rows:
    lines.append(
        f"| `{r['plugin']}` | {r['domain']} | {r['comp']} | {r['trigger']} | {r['refs_by']} | {r['ev']} | {r['gran']} | {r['cluster']} | **{r['verdict']}** | {r['rationale']} |"
    )

lines.append("")
lines.append("## Findings Requiring Phase 2 Decision")
lines.append("")
lines.append("1. **`filesystem-context` merge candidate** — trigger surface overlaps with `memory-systems` on 'workspace state tracking'. Need trigger-level comparison in Phase 2 to confirm.")
lines.append("2. **`outcome-orientation` merge candidate** — trigger phrases (goal framing, success metrics) likely duplicate `product-thinking/outcome-alignment`. Confirm with full trigger-evals read.")
lines.append("3. **Context suite category** — 4 plugins should share a `context-engineering` sub-domain tag to aid discoverability, even if kept as-is.")
lines.append("4. **`gws-cli` domain ambiguity** — Google Workspace CLI sits at E/P boundary (IT admin vs productivity). Assigned Engineering; revisit if P domain grows a 'workspace-productivity' cluster.")
lines.append("5. **`osint` domain** — currently Meta-Infra (information gathering as a meta-capability). Could be P (competitive intelligence). Low ref-count (0) suggests low usage — flag for deprecation review.")
lines.append("6. **`cloud-finops` isolation** — no overlap cluster, P domain, 0 inbound refs from plugins. Useful standalone but may need a 'infrastructure-management' peer to be discoverable.")
lines.append("7. **`plugin-dev` size** — 8 skills, largest after skillstack-workflows (20). Consider splitting: authoring skills vs publishing/eval skills.")
lines.append("")
lines.append("---")
lines.append("*Generated by `docs/audit/_gen_inventory.py` · All domain assignments and verdicts are proposals pending Phase 2 approval*")

out = "\n".join(lines)
Path("docs/audit/01-inventory.md").write_text(out)
print(f"Written: docs/audit/01-inventory.md ({len(lines)} lines)")
print(f"Plugins: {len(rows)}  Domains: {dict(domain_counts)}  Verdicts: {dict(verdict_counts)}")
