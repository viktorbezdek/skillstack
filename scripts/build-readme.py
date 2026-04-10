#!/usr/bin/env python3
"""Build README.md from registry.json — the SkillStack plugin catalog."""

import json
import sys
from datetime import date
from pathlib import Path

REPO = "viktorbezdek/skillstack"
PAGES_URL = "https://viktorbezdek.github.io/skillstack/"

TITLE_OVERRIDES = {
    "api": "API", "bdi": "BDI", "cicd": "CI/CD", "finops": "FinOps",
    "mcp": "MCP", "nextjs": "Next.js", "tdd": "TDD", "ux": "UX",
    "ui": "UI", "devops": "DevOps", "grpc": "gRPC", "graphql": "GraphQL",
}


def smart_title(name):
    words = name.split("-")
    return " ".join(TITLE_OVERRIDES.get(w.lower(), w.capitalize()) for w in words)


def main():
    root = Path(__file__).resolve().parent.parent
    registry_path = root / ".claude-plugin" / "registry.json"
    if not registry_path.exists():
        print("Error: .claude-plugin/registry.json not found", file=sys.stderr)
        sys.exit(1)

    with open(registry_path) as f:
        registry = json.load(f)

    plugins = registry.get("plugins", [])
    collections = registry.get("collections", [])

    active_plugins = [p for p in plugins if p.get("status") == "active"]

    # Group plugins by category
    by_cat: dict[str, list] = {}
    for p in active_plugins:
        by_cat.setdefault(p.get("category", "other"), []).append(p)

    cat_order = ["development", "devops", "quality", "context-engineering",
                 "agent-architecture", "thinking", "design", "documentation", "other"]
    cats = sorted(by_cat.keys(), key=lambda c: (cat_order.index(c) if c in cat_order else 100, c))
    emoji = {
        "development": "\U0001f4bb", "devops": "\u2699\ufe0f", "quality": "\u2705",
        "context-engineering": "\U0001f9e0", "agent-architecture": "\U0001f916",
        "thinking": "\U0001f4a1", "design": "\U0001f3a8", "documentation": "\U0001f4da",
        "other": "\U0001f4cc"
    }

    L = []
    w = L.append

    # Hero
    w("# SkillStack")
    w("")
    w("**Battle-tested skills for Claude Code.**")
    w("")
    w(f"**{len(active_plugins)}** expert plugins covering development, DevOps, testing, "
      "design, strategy, context engineering, and agent architecture.")
    w("")
    w(f"**[Browse the catalog]({PAGES_URL})** \u00b7 "
      f"**[Install](#quick-start)** \u00b7 "
      f"**[Contribute](https://github.com/{REPO}/issues)**")
    w("")

    # Stats
    w(f"> **{len(active_plugins)}** plugins \u00b7 **{len(cats)}** categories \u00b7 "
      f"**{len(collections)}** collections \u00b7 MIT License")
    w("")

    # Quick start
    w("---")
    w("")
    w("## Quick Start")
    w("")
    w("```bash")
    w(f"# Install the full SkillStack collection")
    w(f"claude plugin add {REPO}")
    w("")
    w("# Or install individual plugins")
    w(f"claude plugin add {REPO} --plugin api-design")
    w("```")
    w("")

    # Collections
    if collections:
        w("---")
        w("")
        w("## Collections")
        w("")
        for col in collections:
            cn = col.get("name", "")
            cd = col.get("description", "").strip()
            cp = col.get("plugin_ids", [])
            w("<details>")
            w(f"<summary><strong>{cn}</strong> \u2014 {len(cp)} plugins</summary>")
            w("")
            w(f"> {cd}")
            w("")
            w(f"Plugins: {', '.join(f'`{p}`' for p in cp)}")
            w("</details>")
            w("")

    # Plugin Catalog
    w("---")
    w("")
    w("## Plugin Catalog")
    w("")

    for cat in cats:
        cp = sorted(by_cat[cat], key=lambda p: p["id"])
        e = emoji.get(cat, "\U0001f4cc")
        cat_label = cat.replace("-", " ").title()
        w(f"### {e} {cat_label} ({len(cp)})")
        w("")
        w("| Plugin | Version | Description |")
        w("|--------|---------|-------------|")

        for p in cp:
            pname = smart_title(p["id"])
            desc = p.get("description", "")
            version = p.get("version", "1.0.0")
            doc_path = p.get("documentation_path", "")
            if doc_path:
                link = f"[{pname}]({doc_path.lstrip('./')})"
            else:
                link = pname
            w(f"| {link} | `{version}` | {desc} |")

        w("")

    # How it works
    w("---")
    w("")
    w("## How It Works")
    w("")
    w("Each plugin is a self-contained skill that teaches Claude Code domain expertise:")
    w("")
    w("```")
    w("You describe a task        Claude loads the right skill     Expert-level output")
    w("  (natural language)   \u2192   (automatic activation)       \u2192   (guided by SKILL.md)")
    w("```")
    w("")
    w("Skills activate automatically based on your request, or you can invoke them directly:")
    w("")
    w("```")
    w("Use the api-design skill to design a REST API for user management")
    w("```")
    w("")

    # Contributing
    w("---")
    w("")
    w("## Contributing")
    w("")
    w(f"See [CONTRIBUTING.md](CONTRIBUTING.md) or [open an issue](https://github.com/{REPO}/issues).")
    w("")

    # Footer
    w("---")
    w("")
    w(f"*Auto-generated from [registry.json](.claude-plugin/registry.json) \u00b7 "
      f"Last updated: {date.today()}*")
    w("")

    with open(root / "README.md", "w") as f:
        f.write("\n".join(L))

    print(f"README.md generated: {len(active_plugins)} plugins, {len(collections)} collections")


if __name__ == "__main__":
    main()
