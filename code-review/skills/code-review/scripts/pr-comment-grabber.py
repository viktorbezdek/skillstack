#!/usr/bin/env python3
"""
PR Comment Grabber - Extract ALL comments from a GitHub Pull Request

Fetches both:
- Review comments (inline code comments)
- Issue comments (general PR conversation)

Features:
- Incremental updates: Merges new comments with existing file
- One file per PR: pr-code-review-comments/pr{number}-code-review-comments.json
- Deduplication: Comments are merged by ID (no duplicates)
- Relative path: Saves in current working directory

Usage:
    python pr-comment-grabber.py <owner/repo> <pr_number> [--token TOKEN]

    Or set GITHUB_TOKEN environment variable:
    export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
    python pr-comment-grabber.py owner/repo 123

Example:
    cd /path/to/your/repo
    python pr-comment-grabber.py auldsyababua/mac-workhorse-integration 1
    # Saves to: ./pr-code-review-comments/pr1-code-review-comments.json
"""

import sys
import os
import json
import argparse
from typing import List, Dict, Any

try:
    import requests
except ImportError:
    print("ERROR: requests library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


def parse_link_header(link_header: str) -> Dict[str, str]:
    """Parse GitHub's Link header for pagination."""
    links = {}
    if not link_header:
        return links

    for link in link_header.split(','):
        parts = link.split(';')
        if len(parts) != 2:
            continue
        url = parts[0].strip()[1:-1]  # Remove < and >
        rel = parts[1].strip()
        if 'rel="next"' in rel:
            links['next'] = url
        elif 'rel="last"' in rel:
            links['last'] = url
    return links


def fetch_paginated_comments(url: str, headers: Dict[str, str], comment_type: str) -> List[Dict[str, Any]]:
    """
    Generic function to fetch paginated comments from GitHub API.

    Args:
        url: Starting API endpoint URL
        headers: HTTP headers including auth
        comment_type: "review" or "issue" for metadata tagging

    Returns:
        List of comment objects with metadata
    """
    all_comments = []
    page_count = 0

    while url:
        page_count += 1
        print(f"Fetching {comment_type} comments page {page_count}...", file=sys.stderr)

        try:
            response = requests.get(url, headers=headers, params={"per_page": 100})
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"ERROR: HTTP {e.response.status_code} - {e.response.reason}", file=sys.stderr)
            if e.response.status_code == 401:
                print("Authentication failed. Check your GITHUB_TOKEN.", file=sys.stderr)
            elif e.response.status_code == 404:
                print(f"Resource not found. Check repository and PR number.", file=sys.stderr)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Request failed: {e}", file=sys.stderr)
            sys.exit(1)

        comments = response.json()

        for comment in comments:
            all_comments.append(comment)

        # Check for next page
        link_header = response.headers.get('Link', '')
        links = parse_link_header(link_header)
        url = links.get('next')

    print(f"Fetched {len(all_comments)} {comment_type} comments across {page_count} pages.", file=sys.stderr)
    return all_comments


def fetch_all_review_comments(owner: str, repo: str, pr_number: int, token: str) -> List[Dict[str, Any]]:
    """
    Fetch all review comments (inline code comments) for a PR.

    Endpoint: GET /repos/{owner}/{repo}/pulls/{pull_number}/comments
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "PR-Comment-Grabber/2.0"
    }

    raw_comments = fetch_paginated_comments(url, headers, "review")

    # Extract relevant metadata from each review comment
    review_comments = []
    for comment in raw_comments:
        comment_data = {
            "comment_type": "review",
            "id": comment.get("id"),
            "pull_request_review_id": comment.get("pull_request_review_id"),
            "user": comment.get("user", {}).get("login"),
            "body": comment.get("body"),
            "path": comment.get("path"),
            "position": comment.get("position"),
            "original_position": comment.get("original_position"),
            "line": comment.get("line"),
            "original_line": comment.get("original_line"),
            "commit_id": comment.get("commit_id"),
            "original_commit_id": comment.get("original_commit_id"),
            "diff_hunk": comment.get("diff_hunk"),
            "created_at": comment.get("created_at"),
            "updated_at": comment.get("updated_at"),
            "html_url": comment.get("html_url"),
            "url": comment.get("url"),
            "in_reply_to_id": comment.get("in_reply_to_id"),
        }
        review_comments.append(comment_data)

    return review_comments


def fetch_all_issue_comments(owner: str, repo: str, pr_number: int, token: str) -> List[Dict[str, Any]]:
    """
    Fetch all issue comments (general PR conversation comments) for a PR.

    Endpoint: GET /repos/{owner}/{repo}/issues/{issue_number}/comments
    Note: PRs are issues in GitHub's API, so we use the same number.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "PR-Comment-Grabber/2.0"
    }

    raw_comments = fetch_paginated_comments(url, headers, "issue")

    # Extract relevant metadata from each issue comment
    issue_comments = []
    for comment in raw_comments:
        comment_data = {
            "comment_type": "issue",
            "id": comment.get("id"),
            "user": comment.get("user", {}).get("login"),
            "body": comment.get("body"),
            "created_at": comment.get("created_at"),
            "updated_at": comment.get("updated_at"),
            "html_url": comment.get("html_url"),
            "url": comment.get("url"),
            # Issue comments don't have file/line info
            "path": None,
            "position": None,
            "line": None,
            "pull_request_review_id": None,
            "diff_hunk": None,
        }
        issue_comments.append(comment_data)

    return issue_comments


def load_existing_comments(file_path: str) -> List[Dict[str, Any]]:
    """
    Load existing comments from file if it exists.

    Returns:
        List of existing comments, or empty list if file doesn't exist
    """
    if not os.path.exists(file_path):
        print(f"No existing file found at: {file_path}", file=sys.stderr)
        print(f"Will create new file.", file=sys.stderr)
        return []

    try:
        with open(file_path, 'r') as f:
            existing = json.load(f)
            print(f"Loaded {len(existing)} existing comments from: {file_path}", file=sys.stderr)
            return existing
    except json.JSONDecodeError as e:
        print(f"WARNING: Existing file is invalid JSON: {e}", file=sys.stderr)
        print(f"Starting fresh (existing file will be backed up).", file=sys.stderr)
        # Backup corrupted file
        backup_path = file_path + ".backup"
        os.rename(file_path, backup_path)
        print(f"Backed up corrupted file to: {backup_path}", file=sys.stderr)
        return []


def merge_comments(existing: List[Dict[str, Any]], new: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Merge new comments with existing comments, deduplicating by ID.

    Args:
        existing: List of existing comments from file
        new: List of newly fetched comments from API

    Returns:
        Merged list with no duplicate IDs, sorted by created_at
    """
    # Create dict keyed by ID for deduplication
    comment_dict = {}

    # Add existing comments first
    for comment in existing:
        comment_id = comment.get("id")
        if comment_id:
            comment_dict[comment_id] = comment

    # Add/update with new comments (newer data takes precedence)
    added_count = 0
    updated_count = 0
    for comment in new:
        comment_id = comment.get("id")
        if comment_id:
            if comment_id in comment_dict:
                # Check if comment was updated
                old_updated = comment_dict[comment_id].get("updated_at")
                new_updated = comment.get("updated_at")
                if new_updated != old_updated:
                    updated_count += 1
                comment_dict[comment_id] = comment  # Update with newer data
            else:
                comment_dict[comment_id] = comment
                added_count += 1

    # Convert back to list and sort by created_at
    merged = list(comment_dict.values())
    merged.sort(key=lambda x: x.get("created_at", ""))

    print(f"\nMerge summary:", file=sys.stderr)
    print(f"  Existing comments: {len(existing)}", file=sys.stderr)
    print(f"  New comments added: {added_count}", file=sys.stderr)
    print(f"  Comments updated: {updated_count}", file=sys.stderr)
    print(f"  Total after merge: {len(merged)}", file=sys.stderr)

    return merged


def save_comments(file_path: str, comments: List[Dict[str, Any]]) -> None:
    """
    Save comments to JSON file.

    Args:
        file_path: Full path to output file
        comments: List of comment objects to save
    """
    # Ensure directory exists
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}", file=sys.stderr)

    # Write JSON file
    with open(file_path, 'w') as f:
        json.dump(comments, f, indent=2)

    print(f"\nSaved {len(comments)} comments to: {file_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Extract ALL comments from a GitHub Pull Request (review + issue comments)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cd /path/to/your/repo
  python pr-comment-grabber.py auldsyababua/mac-workhorse-integration 1
  # Saves to: ./pr-code-review-comments/pr1-code-review-comments.json

  python pr-comment-grabber.py owner/repo 90 --token ghp_xxxxx
  # Saves to: ./pr-code-review-comments/pr90-code-review-comments.json

Features:
  - Incremental updates: Re-running merges new comments (no duplicates)
  - One file per PR: pr{number}-code-review-comments.json
  - Relative path: Saves in current working directory
  - Deduplication: Comments merged by ID

Comment Types:
  - "review": Inline code comments (file path + line number)
  - "issue": General PR conversation comments (no file/line)
        """
    )
    parser.add_argument("repo", help="Repository in format: owner/repo")
    parser.add_argument("pr_number", type=int, help="Pull Request number")
    parser.add_argument("--token", help="GitHub Personal Access Token (or use GITHUB_TOKEN env var)")

    args = parser.parse_args()

    # Get token from args or environment
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("ERROR: GitHub token required. Provide via --token or GITHUB_TOKEN env var.", file=sys.stderr)
        sys.exit(1)

    # Parse owner/repo
    try:
        owner, repo = args.repo.split('/')
    except ValueError:
        print("ERROR: Repository must be in format: owner/repo", file=sys.stderr)
        sys.exit(1)

    # Construct output file path (relative to current working directory)
    output_dir = "pr-code-review-comments"
    output_file = f"pr{args.pr_number}-code-review-comments.json"
    output_path = os.path.join(output_dir, output_file)

    print(f"\n=== PR Comment Grabber ===", file=sys.stderr)
    print(f"PR: {owner}/{repo}#{args.pr_number}", file=sys.stderr)
    print(f"Output: {output_path}", file=sys.stderr)
    print(f"", file=sys.stderr)

    # Load existing comments if file exists
    existing_comments = load_existing_comments(output_path)

    # Fetch new comments from GitHub API
    print(f"\n=== Fetching comments from GitHub ===\n", file=sys.stderr)

    review_comments = fetch_all_review_comments(owner, repo, args.pr_number, token)
    issue_comments = fetch_all_issue_comments(owner, repo, args.pr_number, token)

    # Combine new comments
    new_comments = review_comments + issue_comments

    print(f"\n=== Fetched from API ===", file=sys.stderr)
    print(f"Review comments (inline): {len(review_comments)}", file=sys.stderr)
    print(f"Issue comments (general): {len(issue_comments)}", file=sys.stderr)
    print(f"Total fetched: {len(new_comments)}", file=sys.stderr)

    # Merge with existing comments (deduplicates by ID)
    merged_comments = merge_comments(existing_comments, new_comments)

    # Save to file
    save_comments(output_path, merged_comments)

    print(f"\n=== Done ===", file=sys.stderr)
    print(f"File location: {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
