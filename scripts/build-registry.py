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

    registry = {
        "name": "skillstack",
        "description": "Battle-tested Claude Code skills for development, DevOps, testing, design, strategy, context engineering, and agent architecture.",
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
                "context": "46 battle-tested Claude Code skills covering development, DevOps, testing, API design, documentation, strategic thinking, context engineering, and agent architecture."
            }
        ],
        "plugins": plugins,
        "collections": [
            {
                "id": "skillstack-full",
                "name": "SkillStack",
                "description": "The complete SkillStack library — 46 expert skills for Claude Code covering the full software development lifecycle.",
                "audience": "technical",
                "auto_inferred_from_repo": REPO_ID,
                "plugin_ids": [p["id"] for p in plugins],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-development",
                "name": "Development Core",
                "description": "Core development skills: Python, TypeScript, React, Next.js, API design, debugging, and frontend design.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "development"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-devops",
                "name": "DevOps & Infrastructure",
                "description": "CI/CD pipelines, Docker containerization, Git workflow management, and workflow automation.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "devops"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-quality",
                "name": "Quality & Testing",
                "description": "Code review, test-driven development, testing frameworks, edge case coverage, and consistency standards.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "quality"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-context-engineering",
                "name": "Context Engineering",
                "description": "Context fundamentals, degradation patterns, compression, optimization, and filesystem-based context management.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "context-engineering"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-agent-architecture",
                "name": "Agent Architecture",
                "description": "Multi-agent patterns, memory systems, tool design, hosted agents, BDI mental states, agent evaluation, and project development.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "agent-architecture"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-thinking",
                "name": "Strategic Thinking",
                "description": "Creative problem-solving, critical intuition, systems thinking, prioritization, risk management, and outcome orientation.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "thinking"],
                "created_at": "2025-01-01T00:00:00Z"
            },
            {
                "id": "skillstack-design",
                "name": "Design & UX",
                "description": "Content modelling, navigation design, ontology design, persona definition/mapping, user journey design, and UX writing.",
                "audience": "technical",
                "plugin_ids": [p["id"] for p in plugins if p["category"] == "design"],
                "created_at": "2025-01-01T00:00:00Z"
            }
        ]
    }

    registry_path = ROOT / ".claude-plugin" / "registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
        f.write("\n")

    print(f"Registry built: {len(plugins)} plugins, {len(registry['collections'])} collections")
    print(f"Written to {registry_path}")


if __name__ == "__main__":
    main()
