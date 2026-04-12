#!/usr/bin/env python3
"""
Generate trigger-evals.json and evals.json for every skill that lacks them.

Reads SKILL.md frontmatter (name + description) and produces realistic,
domain-specific eval queries. Skips skills that already have both files.

Usage:
    python3 scripts/generate_evals.py [--dry-run] [--force]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Exclusion patterns — nested SKILL.md files that are not real skills
EXCLUDE_PATTERNS = ["examples/", "templates/", "resources/SKILL.md", "references/SKILL.md"]


def parse_frontmatter(skill_md: Path) -> dict:
    """Extract YAML frontmatter from SKILL.md."""
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    raw = match.group(1)
    # Simple key-value extraction without full YAML parser
    result = {}
    current_key = None
    current_val_lines = []
    for line in raw.split("\n"):
        # New key?
        kv = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if kv:
            if current_key:
                result[current_key] = "\n".join(current_val_lines).strip()
            current_key = kv.group(1)
            val = kv.group(2)
            if val in ("|", ">-", ">"):
                current_val_lines = []
            else:
                current_val_lines = [val.strip().strip("'\"")]
        elif current_key:
            current_val_lines.append(line.strip())
    if current_key:
        result[current_key] = "\n".join(current_val_lines).strip()
    # Clean trailing quotes from description
    if "description" in result:
        result["description"] = result["description"].strip().strip("'\"")
    return result


def extract_trigger_phrases(description: str) -> list[str]:
    """Extract quoted trigger phrases from description."""
    phrases = re.findall(r'"([^"]+)"', description)
    return phrases[:10]  # Cap at 10


def extract_not_for(description: str) -> list[str]:
    """Extract NOT-for clauses from description."""
    nots = re.findall(r"NOT\s+for\s+([^.(]+)", description, re.IGNORECASE)
    return [n.strip() for n in nots[:5]]


def generate_trigger_evals(name: str, description: str) -> list[dict]:
    """Generate trigger eval cases from skill name and description."""
    triggers = extract_trigger_phrases(description)
    not_fors = extract_not_for(description)

    # Build positive cases from trigger phrases
    positives = []
    # Map common skill domains to realistic user queries
    domain_queries = _domain_queries(name, description, triggers)
    for q, note in domain_queries[:10]:
        positives.append({"query": q, "should_trigger": True, "note": note})

    # Pad to at least 8 positives
    if len(positives) < 8:
        generic_positives = _generic_positives(name, description)
        for q, note in generic_positives:
            if len(positives) >= 8:
                break
            if not any(p["query"] == q for p in positives):
                positives.append({"query": q, "should_trigger": True, "note": note})

    # Build negative cases — near-miss + off-topic
    negatives = []
    for nf in not_fors[:3]:
        q = f"help me with {nf.lower().rstrip(',').strip()}"
        negatives.append({
            "query": q,
            "should_trigger": False,
            "note": f"Near-miss — NOT-for clause from description: {nf.strip()}"
        })

    near_miss_negs = _near_miss_negatives(name, description)
    for q, note in near_miss_negs:
        if len(negatives) >= 5:
            break
        if not any(n["query"] == q for n in negatives):
            negatives.append({"query": q, "should_trigger": False, "note": note})

    # Pad negatives to 5
    off_topic = [
        ("write me a haiku about cats", "Off-topic — completely unrelated"),
        ("what's the weather like today", "Off-topic — no relation to this skill"),
        ("help me plan a birthday party", "Off-topic — no software/design context"),
        ("explain quantum entanglement", "Off-topic — physics, not software"),
        ("translate this to French", "Off-topic — translation, not this domain"),
    ]
    for q, note in off_topic:
        if len(negatives) >= 5:
            break
        if not any(n["query"] == q for n in negatives):
            negatives.append({"query": q, "should_trigger": False, "note": note})

    return positives[:10] + negatives[:6]


def _domain_queries(name: str, description: str, triggers: list[str]) -> list[tuple[str, str]]:
    """Generate domain-specific positive queries."""
    results = []

    # From trigger phrases
    for t in triggers[:5]:
        q = f"I need to {t.lower()}"
        results.append((q, f"Maps to trigger phrase: \"{t}\""))

    # From skill name — natural phrasing
    name_words = name.replace("-", " ")
    results.append((
        f"can you help me with {name_words}?",
        f"Direct domain reference using skill topic"
    ))
    results.append((
        f"what's the best approach to {name_words}?",
        f"Advisory query in the skill's domain"
    ))
    results.append((
        f"I'm struggling with {name_words} on my project",
        f"Problem statement in the skill's domain"
    ))

    # Contextual query
    desc_lower = description.lower()
    if "framework" in desc_lower or "methodology" in desc_lower:
        results.append((
            f"what framework should I use for {name_words}?",
            "Framework/methodology selection query"
        ))
    if "pattern" in desc_lower or "architecture" in desc_lower:
        results.append((
            f"show me the patterns for {name_words}",
            "Pattern/architecture query"
        ))
    if "best practice" in desc_lower:
        results.append((
            f"what are the best practices for {name_words}?",
            "Best practices query"
        ))

    return results


def _generic_positives(name: str, description: str) -> list[tuple[str, str]]:
    """Fallback positive queries when domain-specific ones are insufficient."""
    name_words = name.replace("-", " ")
    return [
        (f"help me set up {name_words} for my team's project", "Setup/onboarding query"),
        (f"review my approach to {name_words}", "Review/critique query"),
        (f"I need guidance on {name_words} — where should I start?", "Getting-started query"),
        (f"our {name_words} is a mess — help me improve it", "Improvement/refactoring query"),
        (f"what are common mistakes people make with {name_words}?", "Anti-pattern query"),
        (f"compare different approaches to {name_words}", "Comparison query"),
    ]


def _near_miss_negatives(name: str, description: str) -> list[tuple[str, str]]:
    """Generate near-miss negative queries — sound related but belong elsewhere."""
    name_words = name.replace("-", " ")
    negs = []

    # Generic near-misses based on common confusions
    confusion_map = {
        "testing": ("write me a unit test for this function", "Near-miss — specific test writing, not testing framework/methodology"),
        "design": ("make my button blue", "Near-miss — CSS styling, not design methodology"),
        "api": ("fix the 500 error on my endpoint", "Near-miss — debugging, not API design"),
        "context": ("my React context provider isn't working", "Near-miss — React Context API, not LLM context engineering"),
        "agent": ("install the Chrome extension", "Near-miss — browser agent, not LLM agent"),
        "workflow": ("merge my PR", "Near-miss — git operation, not workflow design"),
        "debug": ("add a console.log here", "Near-miss — quick logging, not systematic debugging"),
        "docker": ("my kubernetes pod keeps crashing", "Near-miss — k8s, not Docker"),
        "git": ("deploy my app to production", "Near-miss — deployment, not git workflow"),
        "prompt": ("write a marketing email", "Near-miss — content writing, not prompt engineering"),
        "memory": ("my computer is running out of RAM", "Near-miss — hardware, not agent memory systems"),
        "navigation": ("add a back button to my app", "Near-miss — UI implementation, not navigation design"),
        "security": ("encrypt this data", "Near-miss — crypto, not security review"),
        "typescript": ("convert my Python script to JavaScript", "Near-miss — language conversion, not TS development"),
        "python": ("my pip install is failing", "Near-miss — package management, not Python development"),
        "react": ("which frontend framework should I use", "Near-miss — framework selection, not React development"),
    }

    for keyword, (q, note) in confusion_map.items():
        if keyword in name.lower() or keyword in description.lower()[:200]:
            negs.append((q, note))

    # Always add a couple of adjacent-domain near-misses
    negs.append((
        f"I want to learn about {name_words} in general — any good books?",
        "Near-miss — learning resources, not actionable skill guidance"
    ))
    negs.append((
        "create a presentation about our quarterly results",
        "Near-miss — content creation, not this skill's domain"
    ))

    return negs


def generate_output_evals(name: str, description: str) -> list[dict]:
    """Generate output eval cases."""
    name_words = name.replace("-", " ")
    triggers = extract_trigger_phrases(description)

    cases = []

    # Case 1: primary use case
    primary_trigger = triggers[0] if triggers else name_words
    cases.append({
        "query": f"I need to {primary_trigger.lower()} — walk me through the approach",
        "files": [],
        "expected_behavior": (
            f"Agent activates the {name} skill and provides a structured, "
            f"actionable response covering the methodology or framework from "
            f"the skill's references. Response includes concrete steps, not "
            f"just abstract advice. If the skill has references, it should "
            f"cite or draw from them."
        )
    })

    # Case 2: review/critique
    cases.append({
        "query": f"review my current approach to {name_words} and suggest improvements",
        "files": [],
        "expected_behavior": (
            f"Agent asks for context about the current approach (or works "
            f"with what's available), then provides specific, actionable "
            f"feedback grounded in the {name} skill's methodology. Feedback "
            f"should be structured (numbered or categorized) and reference "
            f"concrete patterns or anti-patterns from the domain."
        )
    })

    # Case 3: getting started / setup
    cases.append({
        "query": f"we're starting a new project and need to set up {name_words} from scratch — what's the best approach?",
        "files": [],
        "expected_behavior": (
            f"Agent provides a step-by-step getting-started guide for "
            f"{name_words}, appropriate to the project context. Steps are "
            f"concrete and ordered (not a generic list of principles). "
            f"If the skill covers multiple sub-topics, agent focuses on "
            f"the foundational ones first."
        )
    })

    return cases


def discover_skills(repo_root: Path) -> list[Path]:
    """Find all real skill directories that need evals."""
    skills = []
    for skill_md in sorted(repo_root.glob("*/skills/*/SKILL.md")):
        # Skip nested non-skill SKILL.md files
        rel = str(skill_md.relative_to(repo_root))
        if any(p in rel for p in EXCLUDE_PATTERNS):
            continue
        skills.append(skill_md.parent)
    # Also pick up multi-level skills like plugin-dev/skills/X/
    for skill_md in sorted(repo_root.glob("*/skills/*/*/SKILL.md")):
        rel = str(skill_md.relative_to(repo_root))
        if any(p in rel for p in EXCLUDE_PATTERNS):
            continue
        # Only include if parent/parent is "skills" (e.g. plugin-dev/skills/plugin-hooks/)
        if skill_md.parent.parent.name == "skills":
            if skill_md.parent not in skills:
                skills.append(skill_md.parent)
    return sorted(set(skills))


def main():
    parser = argparse.ArgumentParser(description="Generate eval files for all skills")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be generated without writing")
    parser.add_argument("--force", action="store_true", help="Overwrite existing eval files")
    args = parser.parse_args()

    skills = discover_skills(REPO_ROOT)
    print(f"Discovered {len(skills)} skills")

    generated = 0
    skipped = 0
    errors = 0

    for skill_dir in skills:
        evals_dir = skill_dir / "evals"
        trigger_file = evals_dir / "trigger-evals.json"
        output_file = evals_dir / "evals.json"

        # Skip if both exist and not forcing
        if trigger_file.exists() and output_file.exists() and not args.force:
            skipped += 1
            continue

        skill_md = skill_dir / "SKILL.md"
        fm = parse_frontmatter(skill_md)
        name = fm.get("name", skill_dir.name)
        description = fm.get("description", "")

        if not description:
            print(f"  WARNING: {skill_dir.name} has no description, using name only")

        trigger_cases = generate_trigger_evals(name, description)
        output_cases = generate_output_evals(name, description)

        if args.dry_run:
            print(f"  Would generate: {skill_dir.name} — {len([c for c in trigger_cases if c['should_trigger']])} positive, {len([c for c in trigger_cases if not c['should_trigger']])} negative triggers, {len(output_cases)} output cases")
            generated += 1
            continue

        try:
            evals_dir.mkdir(parents=True, exist_ok=True)
            trigger_file.write_text(json.dumps(trigger_cases, indent=2) + "\n", encoding="utf-8")
            output_file.write_text(json.dumps(output_cases, indent=2) + "\n", encoding="utf-8")
            generated += 1
            print(f"  Generated: {skill_dir.name}")
        except Exception as e:
            print(f"  ERROR: {skill_dir.name}: {e}")
            errors += 1

    print(f"\nDone: {generated} generated, {skipped} skipped (already exist), {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
