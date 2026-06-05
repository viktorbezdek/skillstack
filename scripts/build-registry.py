#!/usr/bin/env python3
"""Build .claude-plugin/registry.json from individual plugin.json files and marketplace.json.

This creates a normalized registry (the source of truth) from which all other
artifacts (README, catalog site, marketplace.json) are generated.
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/viktorbezdek/skillstack"
REPO_ID = "viktorbezdek-skillstack"


def get_head_sha():
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True, text=True, cwd=ROOT
    )
    return result.stdout.strip()


def load_marketplace():
    """Load existing marketplace.json for category/tag data."""
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp_path.exists():
        return {}
    with open(mp_path) as f:
        mp = json.load(f)
    return {p["name"]: p for p in mp.get("plugins", [])}


def discover_plugins():
    """Find all plugins by scanning for .claude-plugin/plugin.json."""
    plugins = []
    mp_data = load_marketplace()

    for pj_path in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        with open(pj_path) as f:
            pj = json.load(f)

        name = pj["name"]
        mp_entry = mp_data.get(name, {})

        # Determine plugin type by checking for skills/, agents/, commands/
        plugin_dir = pj_path.parent.parent
        ptype = "skill"
        if list(plugin_dir.glob("agents/*.md")):
            ptype = "agent"
        elif list(plugin_dir.glob("commands/*.md")):
            ptype = "command"

        # Find the skill path
        skill_paths = list(plugin_dir.glob(f"skills/{name}/SKILL.md"))
        path_in_repo = f"{name}/skills/{name}" if skill_paths else name

        # Read SKILL.md description if available
        description = pj.get("description", "")

        plugins.append({
            "id": name,
            "name": name.replace("-", " ").title(),
            "type": ptype,
            "category": mp_entry.get("category", "engineering"),
            "description": description,
            "repo_id": REPO_ID,
            "path_in_repo": path_in_repo,
            "version": pj.get("version", "1.0.0"),
            "tags": mp_entry.get("tags", pj.get("keywords", [])),
            "documentation_path": f"./{name}/README.md",
            "status": "active",
            "platforms": ["claude-code"]
        })

    return plugins


def main():
    sha = get_head_sha()
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    plugins = discover_plugins()

    # 4-domain taxonomy collections
    VALID_DOMAINS = ["Engineering", "Meta-Infra", "Managerial-Product", "Marketing-Comms"]

    def domain_ids(domain: str) -> list[str]:
        return [p["id"] for p in plugins if p["category"] == domain]

    domain_descriptions = {
        "Engineering": (
            "skillstack-engineering",
            "Engineering",
            "Skills for building software: APIs, debugging, testing, DevOps, frontend, "
            "language tooling (Python, TypeScript, React, Next.js), containerization, "
            "MCP servers, multi-agent systems, and documentation generation."
        ),
        "Meta-Infra": (
            "skillstack-meta-infra",
            "Meta-Infra",
            "Skills for improving how Claude Code and LLM agents operate: context engineering "
            "(compression, degradation, fundamentals, optimization), memory systems, plugin "
            "authoring, prompt engineering, skill evaluation, and workflow orchestration."
        ),
        "Managerial-Product": (
            "skillstack-managerial-product",
            "Managerial-Product",
            "Skills for making decisions and shipping products: product thinking, prioritization, "
            "risk management, brainstorm facilitation, personas, user journeys, outcome orientation, "
            "ontology design, content modelling, cloud FinOps, and systems thinking."
        ),
        "Marketing-Comms": (
            "skillstack-marketing-comms",
            "Marketing-Comms",
            "Skills for creating human-facing content: communication craft, AI-slop removal, "
            "technical copywriting, UX writing, and storytelling."
        ),
    }

    collections = [
        {
            "id": "skillstack-full",
            "name": "SkillStack",
            "description": (
                f"The complete SkillStack library - {len(plugins)} expert plugins for Claude Code "
                "spanning Engineering, Meta-Infra, Managerial-Product, and Marketing-Comms."
            ),
            "audience": "technical",
            "auto_inferred_from_repo": REPO_ID,
            "plugin_ids": [p["id"] for p in plugins],
            "created_at": "2025-01-01T00:00:00Z"
        }
    ]
    for domain in VALID_DOMAINS:
        col_id, col_name, col_desc = domain_descriptions[domain]
        ids = domain_ids(domain)
        collections.append({
            "id": col_id,
            "name": col_name,
            "description": col_desc,
            "audience": "technical",
            "plugin_ids": ids,
            "created_at": "2025-01-01T00:00:00Z"
        })

    registry = {
        "name": "skillstack",
        "description": (
            "Battle-tested Claude Code plugins spanning Engineering, Meta-Infra, "
            "Managerial-Product, and Marketing-Comms."
        ),
        "owner": {
            "name": "Viktor Bezdek",
            "url": "https://github.com/viktorbezdek"
        },
        "metadata": {
            "version": "3.0.0",
            "schema_version": 2,
            "last_full_sync": now
        },
        "repositories": [
            {
                "id": REPO_ID,
                "url": REPO_URL,
                "added_by": "viktorbezdek",
                "added_date": "2025-01-01",
                "last_synced_sha": sha,
                "last_synced_at": now,
                "integration_status": "active",
                "context": (
                    f"{len(plugins)} battle-tested Claude Code plugins across 4 domains: "
                    "Engineering, Meta-Infra, Managerial-Product, Marketing-Comms."
                )
            }
        ],
        "plugins": plugins,
        "collections": collections
    }

    registry_path = ROOT / ".claude-plugin" / "registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
        f.write("\n")

    print(f"Registry built: {len(plugins)} plugins, {len(registry['collections'])} collections")
    print(f"Written to {registry_path}")


if __name__ == "__main__":
    main()
