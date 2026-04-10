#!/usr/bin/env python3
"""Generate improved README.md for each plugin using groupon-ai-marketplace template.

Reads SKILL.md frontmatter, plugin.json, and version history to create
documentation with:
- Version badge and metadata
- Pain-first problem framing
- When to use / When NOT to use (from SKILL.md description)
- Usage examples with natural language triggers
- Changelog from git history
"""

import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Category display names and descriptions
CATEGORY_INFO = {
    "development": ("Development", "Core development tools and language-specific expertise"),
    "devops": ("DevOps & Infrastructure", "CI/CD, containers, git workflow, and automation"),
    "quality": ("Quality & Testing", "Code review, testing, edge cases, and standards"),
    "context-engineering": ("Context Engineering", "LLM context management, optimization, and patterns"),
    "agent-architecture": ("Agent Architecture", "Multi-agent systems, memory, tools, and evaluation"),
    "thinking": ("Strategic Thinking", "Problem-solving, analysis, prioritization, and risk"),
    "design": ("Design & UX", "Content models, personas, navigation, and UX writing"),
    "documentation": ("Documentation", "Doc generation, examples, and templates"),
}

# Known acronyms/words that should not be title-cased normally
TITLE_OVERRIDES = {
    "api": "API", "bdi": "BDI", "cicd": "CI/CD", "finops": "FinOps",
    "mcp": "MCP", "nextjs": "Next.js", "tdd": "TDD", "ux": "UX",
    "ui": "UI", "devops": "DevOps", "grpc": "gRPC", "graphql": "GraphQL",
    "okrs": "OKRs", "raci": "RACI",
}


def smart_title(name):
    """Title-case a plugin name with proper acronym handling."""
    words = name.split("-")
    result = []
    for word in words:
        lower = word.lower()
        if lower in TITLE_OVERRIDES:
            result.append(TITLE_OVERRIDES[lower])
        else:
            result.append(word.capitalize())
    return " ".join(result)


def parse_skill_frontmatter(skill_path):
    """Parse YAML frontmatter from SKILL.md."""
    if not skill_path.exists():
        return {}

    text = skill_path.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}

    frontmatter = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            frontmatter[key.strip()] = val.strip()

    # Handle multi-line description (block scalar)
    desc_match = re.search(r"description:\s*>-?\n((?:\s+.*\n)*)", m.group(1))
    if desc_match:
        frontmatter["description"] = " ".join(
            line.strip() for line in desc_match.group(1).strip().split("\n")
        )

    return frontmatter


def read_skill_body(skill_path):
    """Read SKILL.md content after frontmatter."""
    if not skill_path.exists():
        return ""
    text = skill_path.read_text()
    m = re.match(r"^---\n.*?\n---\n*(.*)", text, re.DOTALL)
    return m.group(1).strip() if m else text.strip()


def extract_not_clauses(description):
    """Extract NOT clauses from SKILL.md description for 'When NOT to use'."""
    nots = []
    for m in re.finditer(r"NOT\s+(?:for\s+)?(.+?)(?:\.|$)", description, re.IGNORECASE):
        clause = m.group(1).strip().rstrip(".")
        # Extract the suggested alternative if present
        alt_match = re.search(r"\(use\s+(\S+)\)", clause, re.IGNORECASE)
        if alt_match:
            skill = alt_match.group(1)
            action = clause[:clause.index("(")].strip()
            nots.append(f"{action} -- use [{skill}](../{skill}/) instead")
        else:
            nots.append(clause)
    return nots


def format_version_changelog(history):
    """Format version history as a compact changelog."""
    if not history:
        return ""

    lines = []
    # Show last 10 entries
    recent = history[-10:]
    for entry in reversed(recent):
        bump = entry["bump"]
        version = entry["version"]
        msg = entry["message"]
        sha = entry["hash"]
        if bump == "initial":
            lines.append(f"- `{version}` Initial release ({sha})")
        else:
            lines.append(f"- `{version}` {msg} ({sha})")
    return "\n".join(lines)


def find_related_skills(plugin_name, registry):
    """Find related skills based on category."""
    plugins = registry.get("plugins", [])
    current = next((p for p in plugins if p["id"] == plugin_name), None)
    if not current:
        return []

    same_cat = [p for p in plugins if p["category"] == current["category"] and p["id"] != plugin_name]
    return same_cat[:5]


def generate_readme(plugin_name, plugin_json, skill_fm, skill_body, version_data, registry):
    """Generate a README for a plugin."""
    mp_plugin = next((p for p in registry.get("plugins", []) if p["id"] == plugin_name), {})
    category = mp_plugin.get("category", "development")
    cat_label = CATEGORY_INFO.get(category, (category.title(), ""))[0]
    version = version_data.get("version", "1.0.0")
    commit_count = version_data.get("commit_count", 0)
    description = plugin_json.get("description", "")
    display_name = smart_title(plugin_name)
    tags = mp_plugin.get("tags", plugin_json.get("keywords", []))

    # Parse NOT clauses from SKILL.md description
    skill_desc = skill_fm.get("description", description)
    not_clauses = extract_not_clauses(skill_desc)

    # Build the when-to-use from SKILL.md description (remove NOT clauses)
    when_to_use = re.sub(r"\s*NOT\s+(?:for\s+)?[^.]+\.?", "", skill_desc).strip()
    # Clean up trailing punctuation artifacts
    when_to_use = re.sub(r"[,;]\s*$", "", when_to_use)
    when_to_use = when_to_use.rstrip(".")

    L = []
    w = L.append

    # Header with version
    w(f"# {display_name}")
    w("")
    w(f"> **v{version}** | {cat_label} | {commit_count} iterations")
    w("")
    w(f"{description}")
    w("")

    # What problem does this solve
    w("## What Problem Does This Solve")
    w("")
    # Extract first paragraph from SKILL.md body as the problem statement
    body_paragraphs = [p.strip() for p in skill_body.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    if body_paragraphs:
        # Use first non-heading paragraph
        problem = body_paragraphs[0]
        if problem.startswith("- ") or problem.startswith("* "):
            # It's a list, use the description instead
            w(f"{description}")
        else:
            w(problem)
    else:
        w(f"{description}")
    w("")

    # When to use
    w("## When to Use This Skill")
    w("")
    w(f"{when_to_use}.")
    w("")

    # When NOT to use
    if not_clauses:
        w("## When NOT to Use This Skill")
        w("")
        for clause in not_clauses:
            w(f"- {clause}")
        w("")

    # How to use
    w("## How to Use")
    w("")
    w(f"**Direct invocation:**")
    w("")
    w("```")
    w(f"Use the {plugin_name} skill to ...")
    w("```")
    w("")
    w("**Natural language triggers** -- Claude activates this skill automatically when you mention:")
    w("")
    # Extract key terms from tags and description
    trigger_terms = tags[:6] if tags else [plugin_name]
    for term in trigger_terms:
        w(f"- `{term}`")
    w("")

    # What's included -- parse from SKILL.md body
    sections = re.findall(r"^##\s+(.+?)$", skill_body, re.MULTILINE)
    if sections:
        w("## What's Inside")
        w("")
        for section in sections[:8]:
            w(f"- **{section}**")
        w("")

    # Key features from existing README or SKILL.md
    features_match = re.search(r"## Key Features\n\n((?:- .+\n)+)", skill_body)
    if not features_match:
        # Try to extract bullet points from body
        bullets = re.findall(r"^- \*\*(.+?)\*\*", skill_body, re.MULTILINE)
        if bullets:
            w("## Key Capabilities")
            w("")
            for b in bullets[:6]:
                w(f"- **{b}**")
            w("")

    # Version history
    history = version_data.get("history", [])
    if history:
        w("## Version History")
        w("")
        changelog = format_version_changelog(history)
        w(changelog)
        w("")

    # Related skills
    related = find_related_skills(plugin_name, registry)
    if related:
        w("## Related Skills")
        w("")
        for r in related:
            rname = r["id"]
            rdesc = r.get("description", "")[:120]
            if len(r.get("description", "")) > 120:
                rdesc += "..."
            w(f"- **[{rname.replace('-', ' ').title()}](../{rname}/)** -- {rdesc}")
        w("")

    # Footer
    w("---")
    w("")
    w(f"Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- "
      f"{len(registry.get('plugins', []))} production-grade plugins for Claude Code.")
    w("")

    return "\n".join(L)


def main():
    # Load version map
    version_map_path = ROOT / "scripts" / "version-map.json"
    with open(version_map_path) as f:
        version_map = json.load(f)

    # Load or build registry
    registry_path = ROOT / ".claude-plugin" / "registry.json"
    if registry_path.exists():
        with open(registry_path) as f:
            registry = json.load(f)
    else:
        print("Warning: registry.json not found, run build-registry.py first")
        registry = {"plugins": [], "collections": []}

    generated = 0
    for plugin_dir in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        plugin_root = plugin_dir.parent.parent
        plugin_name = plugin_root.name

        # Load plugin.json
        with open(plugin_dir) as f:
            plugin_json = json.load(f)

        # Find SKILL.md
        skill_path = plugin_root / "skills" / plugin_name / "SKILL.md"
        if not skill_path.exists():
            # Try alternative locations
            alt_paths = list(plugin_root.glob("**/SKILL.md"))
            skill_path = alt_paths[0] if alt_paths else skill_path

        skill_fm = parse_skill_frontmatter(skill_path)
        skill_body = read_skill_body(skill_path)

        version_data = version_map.get(plugin_name, {"version": "1.0.0", "commit_count": 0, "history": []})

        readme_content = generate_readme(
            plugin_name, plugin_json, skill_fm, skill_body, version_data, registry
        )

        readme_path = plugin_root / "README.md"
        readme_path.write_text(readme_content)
        generated += 1
        print(f"  {plugin_name}/README.md (v{version_data['version']})")

    print(f"\nGenerated {generated} README files")


if __name__ == "__main__":
    main()
