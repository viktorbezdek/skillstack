#!/usr/bin/env python3
"""
Show PR comments with status markers (addressed vs pending).

Generates a markdown report with:
- ✅ Addressed comments (strikethrough)
- 📝 Pending comments (normal text)
- 📊 Progress summary

Usage:
    python show-with-status.py <pr-number> [--format markdown|json]
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


def load_state(pr_number):
    """Load review state (addressed comment IDs)."""
    state_file = f"pr-code-review-comments/pr{pr_number}-review-state.json"
    if not Path(state_file).exists():
        return {"iteration": 0, "addressed_comments": []}

    with open(state_file, 'r') as f:
        return json.load(f)


def load_comments(pr_number, filtered=True):
    """Load PR comments."""
    suffix = "-filtered" if filtered else ""
    comment_file = f"pr-code-review-comments/pr{pr_number}-code-review-comments{suffix}.json"

    if not Path(comment_file).exists():
        print(f"Error: Comment file not found: {comment_file}", file=sys.stderr)
        sys.exit(1)

    with open(comment_file, 'r') as f:
        return json.load(f)


def format_comment_markdown(comment, addressed=False):
    """Format a single comment as markdown."""
    user = comment.get('user', 'unknown')
    comment_type = comment.get('comment_type', 'unknown')
    path = comment.get('path', '')
    line = comment.get('line', '')
    body = comment.get('body', '')
    html_url = comment.get('html_url', '')

    # Build location string
    location = path if path else "General comment"
    if line:
        location += f":{line}"

    # Truncate body for summary
    body_preview = body[:150].replace('\n', ' ')
    if len(body) > 150:
        body_preview += "..."

    # Apply strikethrough if addressed
    if addressed:
        status = "✅"
        location = f"~~{location}~~"
        body_preview = f"~~{body_preview}~~"
    else:
        status = "📝"

    # Format as markdown
    lines = [
        f"### {status} [{user}] {comment_type.title()} Comment",
        f"**Location**: {location}",
        f"**Preview**: {body_preview}",
    ]

    if html_url:
        lines.append(f"**Link**: {html_url}")

    if not addressed:
        # Show priority if available
        if 'importance' in body or '🔴' in body or '🟠' in body:
            if '🔴' in body or 'Critical' in body:
                lines.append(f"**Priority**: 🔴 CRITICAL")
            elif '🟠' in body or 'High' in body:
                lines.append(f"**Priority**: 🟠 HIGH")
            elif '🟡' in body:
                lines.append(f"**Priority**: 🟡 MEDIUM")

    lines.append("")  # Blank line separator

    return "\n".join(lines)


def generate_markdown_report(pr_number, comments, state):
    """Generate markdown report with progress tracking."""
    addressed_ids = set(state.get('addressed_comments', []))

    pending_comments = [c for c in comments if c['id'] not in addressed_ids]
    addressed_comments = [c for c in comments if c['id'] in addressed_ids]

    total = len(comments)
    addressed_count = len(addressed_comments)
    pending_count = len(pending_comments)
    progress = (addressed_count / total * 100) if total > 0 else 0

    # Build report
    lines = [
        f"# PR #{pr_number} Code Review Status",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Iteration**: {state.get('iteration', 0)}",
        "",
        "## Progress",
        "",
        f"- Total comments: {total}",
        f"- ✅ Addressed: {addressed_count}",
        f"- 📝 Pending: {pending_count}",
        f"- Progress: {progress:.1f}%",
        "",
        f"```",
        f"[{'█' * int(progress / 5)}{'░' * (20 - int(progress / 5))}] {progress:.1f}%",
        f"```",
        "",
    ]

    # Pending comments first
    if pending_comments:
        lines.extend([
            "## 📝 Pending Comments",
            "",
            f"**{pending_count} comment(s) require attention**",
            "",
        ])

        for comment in pending_comments:
            lines.append(format_comment_markdown(comment, addressed=False))

    # Addressed comments (collapsed)
    if addressed_comments:
        lines.extend([
            "---",
            "",
            "<details>",
            f"<summary>✅ Addressed Comments ({addressed_count})</summary>",
            "",
        ])

        for comment in addressed_comments:
            lines.append(format_comment_markdown(comment, addressed=True))

        lines.extend([
            "</details>",
            "",
        ])

    return "\n".join(lines)


def generate_json_report(pr_number, comments, state):
    """Generate JSON report with status flags."""
    addressed_ids = set(state.get('addressed_comments', []))

    enriched_comments = []
    for comment in comments:
        enriched = comment.copy()
        enriched['addressed'] = comment['id'] in addressed_ids
        enriched_comments.append(enriched)

    report = {
        "pr_number": pr_number,
        "generated_at": datetime.now().isoformat(),
        "iteration": state.get('iteration', 0),
        "total_comments": len(comments),
        "addressed_count": len([c for c in enriched_comments if c['addressed']]),
        "pending_count": len([c for c in enriched_comments if not c['addressed']]),
        "comments": enriched_comments,
    }

    return json.dumps(report, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='Show PR comments with addressing status',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument('pr_number', type=int, help='PR number')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown',
                       help='Output format (default: markdown)')
    parser.add_argument('--output', help='Output file (default: stdout)')
    parser.add_argument('--unaddressed-only', action='store_true',
                       help='Show only unaddressed comments')

    args = parser.parse_args()

    # Load data
    state = load_state(args.pr_number)
    comments = load_comments(args.pr_number, filtered=True)

    # Filter to unaddressed only if requested
    if args.unaddressed_only:
        addressed_ids = set(state.get('addressed_comments', []))
        comments = [c for c in comments if c['id'] not in addressed_ids]

    # Generate report
    if args.format == 'markdown':
        report = generate_markdown_report(args.pr_number, comments, state)
    else:
        report = generate_json_report(args.pr_number, comments, state)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)


if __name__ == '__main__':
    main()
