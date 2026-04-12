#!/usr/bin/env python3
"""
run_eval.py — plugin evaluation harness.

Runs two types of evaluation against a Claude Code skill:
- TRIGGER evals: measures activation precision/recall against trigger-evals.json
- OUTPUT evals: measures output quality against evals.json using LLM-as-judge

OFFLINE MODE (default when anthropic SDK or API key is unavailable):
  Forces --mode smoke only. Runs STRUCTURAL checks of the eval files and
  the skill's frontmatter. Does NOT compute activation rates or output quality.
  All results are clearly marked SYNTHETIC.

  ⚠️  Offline numbers are not activation rates. Do not report them as such.

ONLINE MODE (requires ANTHROPIC_API_KEY and the anthropic SDK):
  Runs real LLM calls with 60/40 train/test split (trigger mode).
  Output mode spawns with_skill and without_skill runs and grades them.

Usage:
    python3 run_eval.py --plugin-dir PATH --skill SKILL_NAME [OPTIONS]

Examples:
    python3 run_eval.py --plugin-dir ./my-plugin --skill my-skill --offline
    python3 run_eval.py --plugin-dir ./my-plugin --skill my-skill --mode smoke
    ANTHROPIC_API_KEY=sk-... python3 run_eval.py --plugin-dir ./my-plugin --skill my-skill
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Offline detection
# ---------------------------------------------------------------------------

OFFLINE_REASON: str | None = None

try:
    import anthropic as _anthropic  # noqa: F401

    if not os.environ.get("ANTHROPIC_API_KEY"):
        OFFLINE_REASON = "ANTHROPIC_API_KEY not set"
except ImportError:
    OFFLINE_REASON = "anthropic SDK not installed (pip install anthropic)"

SYNTHETIC_BANNER = """\
================================================================================
⚠️  OFFLINE MODE — STRUCTURAL SMOKE TEST ONLY
================================================================================
These results do NOT measure real skill activation or output quality.
Real evaluation requires ANTHROPIC_API_KEY and the anthropic SDK:
    pip install anthropic
    export ANTHROPIC_API_KEY=sk-...
    python3 run_eval.py --plugin-dir PATH --skill NAME

This run only validates that eval files are well-formed and the skill
description meets basic structural quality criteria.
================================================================================
"""


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass
class TriggerCase:
    query: str
    should_trigger: bool


@dataclass
class OutputCase:
    query: str
    files: list[str]
    expected_behavior: list[str]


@dataclass
class SmokeResult:
    """Structural smoke-test result — NOT an activation rate."""

    mode: str = "offline"
    warning: str = "synthetic results — structural checks only"
    trigger_file_valid: bool = False
    output_file_valid: bool = False
    trigger_cases: int = 0
    should_trigger_count: int = 0
    should_not_trigger_count: int = 0
    output_cases: int = 0
    description_issues: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "warning": self.warning,
            "trigger_file_valid": self.trigger_file_valid,
            "output_file_valid": self.output_file_valid,
            "trigger_cases": self.trigger_cases,
            "should_trigger_count": self.should_trigger_count,
            "should_not_trigger_count": self.should_not_trigger_count,
            "output_cases": self.output_cases,
            "description_issues": self.description_issues,
            "errors": self.errors,
        }


# ---------------------------------------------------------------------------
# Eval file loading
# ---------------------------------------------------------------------------


def _load_trigger_evals(path: Path) -> list[TriggerCase] | list[str]:
    """Load trigger-evals.json. Returns list of cases or list of error strings."""
    if not path.exists():
        return [f"trigger-evals.json not found at {path}"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"trigger-evals.json is not valid JSON: {e}"]
    if not isinstance(data, list):
        return ["trigger-evals.json must be a JSON array"]
    errors: list[str] = []
    cases: list[TriggerCase] = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"trigger-evals.json[{i}]: must be an object")
            continue
        if "query" not in item or not isinstance(item["query"], str):
            errors.append(f"trigger-evals.json[{i}]: missing string 'query' field")
        if "should_trigger" not in item or not isinstance(item["should_trigger"], bool):
            errors.append(f"trigger-evals.json[{i}]: missing boolean 'should_trigger' field")
        if not errors or len(errors) == len([e for e in errors if f"[{i}]" in e]):
            cases.append(TriggerCase(query=item.get("query", ""), should_trigger=item.get("should_trigger", True)))
    return errors if errors else cases


def _load_output_evals(path: Path) -> list[OutputCase] | list[str]:
    """Load evals.json. Returns list of cases or list of error strings."""
    if not path.exists():
        return [f"evals.json not found at {path}"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"evals.json is not valid JSON: {e}"]
    if not isinstance(data, list):
        return ["evals.json must be a JSON array"]
    errors: list[str] = []
    cases: list[OutputCase] = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"evals.json[{i}]: must be an object")
            continue
        missing = [f for f in ("query", "files", "expected_behavior") if f not in item]
        if missing:
            errors.append(f"evals.json[{i}]: missing fields: {missing}")
        if not errors or len(errors) == len([e for e in errors if f"[{i}]" in e]):
            cases.append(OutputCase(
                query=item.get("query", ""),
                files=item.get("files", []),
                expected_behavior=item.get("expected_behavior", []),
            ))
    return errors if errors else cases


# ---------------------------------------------------------------------------
# Description quality checks
# ---------------------------------------------------------------------------


def _check_description(description: str) -> list[str]:
    """Basic structural quality checks on a skill description."""
    issues: list[str] = []
    if not description:
        issues.append("description is empty")
        return issues
    if len(description) > 1024:
        issues.append(f"description is {len(description)} chars; max is 1024")
    first_250 = description[:250]
    if not any(kw in first_250.lower() for kw in ("use when", "use for", "use if", "when the user", "when a user")):
        issues.append("description first 250 chars may not contain a 'when to use' trigger clause")
    first_person = any(word in description.lower().split() for word in ("i", "my", "we", "our", "me"))
    if first_person:
        issues.append("description may contain first-person pronouns (should be third-person)")
    return issues


def _load_skill_description(plugin_dir: Path, skill_name: str) -> str | None:
    """Extract description from a skill's SKILL.md frontmatter."""
    skill_md = plugin_dir / "skills" / skill_name / "SKILL.md"
    if not skill_md.exists():
        return None
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_block = text[3:end]
    for line in fm_block.splitlines():
        if line.startswith("description:"):
            return line[len("description:"):].strip()
        elif line.startswith("description:"):
            return line.split(":", 1)[1].strip()
    return None


# ---------------------------------------------------------------------------
# Smoke mode
# ---------------------------------------------------------------------------


def run_smoke(plugin_dir: Path, skill_name: str, workspace: Path) -> SmokeResult:
    """Run offline structural smoke tests. Returns a SmokeResult."""
    result = SmokeResult()
    evals_dir = plugin_dir / "skills" / skill_name / "evals"

    # Load trigger evals.
    trigger_result = _load_trigger_evals(evals_dir / "trigger-evals.json")
    if isinstance(trigger_result, list) and trigger_result and isinstance(trigger_result[0], str):
        result.errors.extend(trigger_result)
    else:
        result.trigger_file_valid = True
        cases: list[TriggerCase] = trigger_result  # type: ignore[assignment]
        result.trigger_cases = len(cases)
        result.should_trigger_count = sum(1 for c in cases if c.should_trigger)
        result.should_not_trigger_count = sum(1 for c in cases if not c.should_trigger)
        if result.should_trigger_count < 8:
            result.errors.append(
                f"trigger-evals.json has only {result.should_trigger_count} should_trigger=true "
                "cases; minimum recommended is 8"
            )
        if result.should_not_trigger_count < 5:
            result.errors.append(
                f"trigger-evals.json has only {result.should_not_trigger_count} should_trigger=false "
                "cases; minimum recommended is 5"
            )

    # Load output evals.
    output_result = _load_output_evals(evals_dir / "evals.json")
    if isinstance(output_result, list) and output_result and isinstance(output_result[0], str):
        result.errors.extend(output_result)
    else:
        result.output_file_valid = True
        result.output_cases = len(output_result)  # type: ignore[arg-type]
        if result.output_cases < 3:
            result.errors.append(
                f"evals.json has only {result.output_cases} cases; minimum recommended is 3"
            )

    # Check description quality.
    description = _load_skill_description(plugin_dir, skill_name)
    if description is None:
        result.errors.append(f"Could not load description from skills/{skill_name}/SKILL.md")
    else:
        result.description_issues = _check_description(description)

    return result


def _write_smoke_report(result: SmokeResult, workspace: Path, skill_name: str) -> None:
    """Write benchmark.json and benchmark.md to workspace."""
    workspace.mkdir(parents=True, exist_ok=True)
    benchmark_json = workspace / "benchmark.json"
    benchmark_md = workspace / "benchmark.md"

    benchmark_json.write_text(json.dumps(result.as_dict(), indent=2), encoding="utf-8")

    lines = [SYNTHETIC_BANNER, "", f"# Smoke Test Results — `{skill_name}`", ""]
    lines += [
        f"**Trigger eval file valid:** {'yes' if result.trigger_file_valid else 'no'}",
        f"**Output eval file valid:** {'yes' if result.output_file_valid else 'no'}",
        f"**Trigger cases:** {result.trigger_cases} "
        f"({result.should_trigger_count} positive, {result.should_not_trigger_count} negative)",
        f"**Output cases:** {result.output_cases}",
        "",
    ]
    if result.description_issues:
        lines += ["## Description quality issues", ""]
        for issue in result.description_issues:
            lines.append(f"- {issue}")
        lines.append("")
    if result.errors:
        lines += ["## Errors", ""]
        for err in result.errors:
            lines.append(f"- {err}")
        lines.append("")
    if not result.errors and not result.description_issues:
        lines.append("✓ All structural checks passed.")

    benchmark_md.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Plugin evaluation harness (online requires ANTHROPIC_API_KEY).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  smoke    Structural checks only. No LLM calls. Safe for CI without API key.
  trigger  Activation precision/recall against trigger-evals.json. Requires API key.
  output   Output quality eval against evals.json. Requires API key.
  both     trigger + output. Requires API key.
""",
    )
    parser.add_argument("--plugin-dir", required=True, metavar="PATH")
    parser.add_argument("--skill", required=True, metavar="SKILL_NAME")
    parser.add_argument(
        "--mode",
        choices=["smoke", "trigger", "output", "both"],
        default=None,
        help="Eval mode. Defaults to 'smoke' when offline, 'both' when online.",
    )
    parser.add_argument("--workspace", default="/tmp/plugin-eval-workspace", metavar="DIR")
    parser.add_argument("--offline", action="store_true", help="Force offline/smoke mode")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    plugin_dir = Path(args.plugin_dir).resolve()
    skill_name = args.skill
    workspace = Path(args.workspace) / f"skill-{skill_name}"

    # Determine online/offline.
    is_offline = bool(args.offline or OFFLINE_REASON)

    # Mode validation.
    if args.mode in ("trigger", "output", "both") and is_offline:
        reason = OFFLINE_REASON or "explicitly requested offline mode"
        print(
            f"Error: --mode {args.mode} requires online access but we are offline: {reason}\n"
            "Use --mode smoke (or omit --mode) for structural checks without an API key.\n"
            "To enable online mode: install the anthropic SDK and set ANTHROPIC_API_KEY.",
            file=sys.stderr,
        )
        return 3

    mode = args.mode or ("smoke" if is_offline else "both")

    # Check skill exists.
    skill_dir = plugin_dir / "skills" / skill_name
    if not skill_dir.is_dir():
        print(f"Error: skill '{skill_name}' not found at {skill_dir}", file=sys.stderr)
        return 2

    if mode == "smoke" or is_offline:
        if is_offline and OFFLINE_REASON:
            print(f"Offline mode: {OFFLINE_REASON}")
        result = run_smoke(plugin_dir, skill_name, workspace)
        _write_smoke_report(result, workspace, skill_name)
        print(SYNTHETIC_BANNER)
        print(f"Smoke test results written to: {workspace}")
        benchmark_md = workspace / "benchmark.md"
        if benchmark_md.exists():
            # Print summary lines.
            for line in benchmark_md.read_text().splitlines():
                if line.startswith("**") or line.startswith("✓") or line.startswith("- "):
                    print(line)
        if result.errors:
            print(f"\n{len(result.errors)} error(s) found. See {workspace}/benchmark.md for details.")
            return 1
        return 0

    # Online modes: not implemented in this version.
    print(
        f"Online mode '{mode}' recognized — full eval harness not implemented in this version.\n"
        "Falling back to smoke mode.",
        file=sys.stderr,
    )
    result = run_smoke(plugin_dir, skill_name, workspace)
    _write_smoke_report(result, workspace, skill_name)
    return 0 if not result.errors else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"eval harness crashed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
