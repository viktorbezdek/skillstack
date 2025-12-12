#!/usr/bin/env python3
"""
Documentation Generator CLI - Main entry point for the documentation skill.

This script provides a unified interface for all documentation operations.

Usage:
    python doc-gen.py analyze /path/to/repo
    python doc-gen.py generate /path/to/repo
    python doc-gen.py validate /path/to/repo
    python doc-gen.py check-links /path/to/repo
    python doc-gen.py drift /path/to/repo
    python doc-gen.py full /path/to/repo  # Run complete workflow
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


# Get the directory where this script lives (skill directory)
SKILL_DIR = Path(__file__).parent.parent.resolve()
SCRIPTS_DIR = SKILL_DIR / 'scripts'


def run_script(script_path: Path, args: list[str]) -> int:
    """Run a Python script with arguments."""
    cmd = [sys.executable, str(script_path)] + args
    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd)


def cmd_analyze(args):
    """Analyze a repository."""
    script = SCRIPTS_DIR / 'core' / 'analyze_repo.py'
    cmd_args = [args.repo_path]
    if args.output:
        cmd_args.extend(['--output', args.output])
    if args.pretty:
        cmd_args.append('--pretty')
    return run_script(script, cmd_args)


def cmd_validate(args):
    """Validate documentation quality."""
    script = SCRIPTS_DIR / 'validation' / 'validate_docs.py'
    cmd_args = [args.repo_path]
    if args.min_score:
        cmd_args.extend(['--min-score', str(args.min_score)])
    if args.verbose:
        cmd_args.append('--verbose')
    if args.output:
        cmd_args.extend(['--output', args.output])
    return run_script(script, cmd_args)


def cmd_check_links(args):
    """Check for broken links."""
    script = SCRIPTS_DIR / 'validation' / 'check_links.py'
    cmd_args = [args.repo_path]
    if args.external:
        cmd_args.append('--external')
    if args.output:
        cmd_args.extend(['--output', args.output])
    return run_script(script, cmd_args)


def cmd_drift(args):
    """Detect documentation drift."""
    script = SCRIPTS_DIR / 'management' / 'detect_drift.py'
    cmd_args = [args.repo_path, args.docs_path or args.repo_path]
    if args.output:
        cmd_args.extend(['--output', args.output])
    return run_script(script, cmd_args)


def cmd_generate(args):
    """Generate documentation."""
    script = SCRIPTS_DIR / 'generation' / 'generate_docs.py'
    cmd_args = [args.repo_path]
    if args.output:
        cmd_args.extend(['--output', args.output])
    if args.plan:
        cmd_args.extend(['--plan', args.plan])
    return run_script(script, cmd_args)


def cmd_full(args):
    """Run the complete documentation workflow."""
    repo_path = Path(args.repo_path).resolve()
    print(f"\n{'='*60}")
    print(f"FULL DOCUMENTATION WORKFLOW")
    print(f"Repository: {repo_path}")
    print(f"{'='*60}\n")

    # Step 1: Analyze
    print("\n[Step 1/4] Analyzing repository...")
    analysis_file = '/tmp/doc-analysis.json'
    script = SCRIPTS_DIR / 'core' / 'analyze_repo.py'
    result = run_script(script, [str(repo_path), '--output', analysis_file, '--pretty'])
    if result != 0:
        print("Analysis failed!")
        return result

    # Step 2: Generate
    print("\n[Step 2/4] Generating documentation...")
    docs_output = str(repo_path / 'docs') if not args.output else args.output
    script = SCRIPTS_DIR / 'generation' / 'generate_docs.py'
    result = run_script(script, [str(repo_path), '--output', docs_output, '--plan', analysis_file])
    if result != 0:
        print("Generation failed!")
        return result

    # Step 3: Validate
    print("\n[Step 3/4] Validating documentation...")
    script = SCRIPTS_DIR / 'validation' / 'validate_docs.py'
    result = run_script(script, [docs_output, '--verbose'])
    # Don't fail on validation, just report

    # Step 4: Check links
    print("\n[Step 4/4] Checking links...")
    script = SCRIPTS_DIR / 'validation' / 'check_links.py'
    result = run_script(script, [docs_output])
    # Don't fail on link check, just report

    print(f"\n{'='*60}")
    print("WORKFLOW COMPLETE")
    print(f"Documentation generated in: {docs_output}")
    print(f"{'='*60}\n")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Documentation Generator - Generate perfect documentation for any repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s analyze ./myproject              # Analyze repository
  %(prog)s generate ./myproject             # Generate docs
  %(prog)s validate ./myproject/docs        # Validate quality
  %(prog)s full ./myproject                 # Run complete workflow
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Analyze command
    p_analyze = subparsers.add_parser('analyze', help='Analyze repository structure')
    p_analyze.add_argument('repo_path', help='Path to repository')
    p_analyze.add_argument('--output', '-o', help='Output JSON file')
    p_analyze.add_argument('--pretty', '-p', action='store_true', help='Pretty print JSON')
    p_analyze.set_defaults(func=cmd_analyze)

    # Generate command
    p_generate = subparsers.add_parser('generate', help='Generate documentation')
    p_generate.add_argument('repo_path', help='Path to repository')
    p_generate.add_argument('--output', '-o', help='Output directory')
    p_generate.add_argument('--plan', '-p', help='Analysis JSON file')
    p_generate.set_defaults(func=cmd_generate)

    # Validate command
    p_validate = subparsers.add_parser('validate', help='Validate documentation quality')
    p_validate.add_argument('repo_path', help='Path to documentation')
    p_validate.add_argument('--min-score', '-m', type=int, default=70, help='Minimum score')
    p_validate.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    p_validate.add_argument('--output', '-o', help='Output JSON file')
    p_validate.set_defaults(func=cmd_validate)

    # Check links command
    p_links = subparsers.add_parser('check-links', help='Check for broken links')
    p_links.add_argument('repo_path', help='Path to documentation')
    p_links.add_argument('--external', '-e', action='store_true', help='Check external links')
    p_links.add_argument('--output', '-o', help='Output JSON file')
    p_links.set_defaults(func=cmd_check_links)

    # Drift command
    p_drift = subparsers.add_parser('drift', help='Detect documentation drift')
    p_drift.add_argument('repo_path', help='Path to repository')
    p_drift.add_argument('--docs-path', '-d', help='Path to docs (default: repo_path)')
    p_drift.add_argument('--output', '-o', help='Output JSON file')
    p_drift.set_defaults(func=cmd_drift)

    # Full workflow command
    p_full = subparsers.add_parser('full', help='Run complete documentation workflow')
    p_full.add_argument('repo_path', help='Path to repository')
    p_full.add_argument('--output', '-o', help='Output directory for docs')
    p_full.set_defaults(func=cmd_full)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
