#!/usr/bin/env python3
"""
Link Checker - Validate all links in documentation files.

Usage:
    python check_links.py ./docs [--external] [--output report.json]
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from urllib.parse import urlparse, urljoin


@dataclass
class LinkResult:
    """Result of checking a single link."""
    source_file: str
    line_number: int
    link_text: str
    link_url: str
    link_type: str  # 'internal', 'external', 'anchor'
    status: str  # 'ok', 'broken', 'warning', 'skipped'
    message: str


class LinkChecker:
    """Check links in documentation files."""

    def __init__(self, docs_path: str, check_external: bool = False):
        self.docs_path = Path(docs_path).resolve()
        self.check_external = check_external
        self.results: list[LinkResult] = []

        if not self.docs_path.exists():
            raise ValueError(f"Documentation path does not exist: {docs_path}")

    def check_all(self) -> dict[str, Any]:
        """Check all links in all markdown files."""
        print(f"Checking links in: {self.docs_path}")

        # Find all markdown files
        md_files = list(self.docs_path.rglob('*.md'))
        print(f"Found {len(md_files)} markdown files")

        for md_file in md_files:
            self._check_file(md_file)

        # Check external links in parallel if enabled
        if self.check_external:
            external_links = [r for r in self.results if r.link_type == 'external' and r.status == 'pending']
            if external_links:
                print(f"Checking {len(external_links)} external links...")
                self._check_external_links(external_links)

        return self._generate_report()

    def _check_file(self, file_path: Path):
        """Check all links in a single file."""
        try:
            content = file_path.read_text()
            lines = content.splitlines()

            # Find all markdown links: [text](url)
            link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

            for line_num, line in enumerate(lines, 1):
                for match in link_pattern.finditer(line):
                    text = match.group(1)
                    url = match.group(2)

                    result = self._check_link(file_path, line_num, text, url)
                    self.results.append(result)

        except Exception as e:
            self.results.append(LinkResult(
                source_file=str(file_path.relative_to(self.docs_path)),
                line_number=0,
                link_text="",
                link_url="",
                link_type="error",
                status="broken",
                message=f"Could not read file: {e}"
            ))

    def _check_link(self, source_file: Path, line_num: int, text: str, url: str) -> LinkResult:
        """Check a single link."""
        rel_source = str(source_file.relative_to(self.docs_path))

        # Determine link type
        if url.startswith(('http://', 'https://')):
            link_type = 'external'
        elif url.startswith('#'):
            link_type = 'anchor'
        elif url.startswith('mailto:'):
            link_type = 'mailto'
        else:
            link_type = 'internal'

        # Check based on type
        if link_type == 'external':
            if self.check_external:
                # Mark as pending, will check later
                return LinkResult(
                    source_file=rel_source,
                    line_number=line_num,
                    link_text=text,
                    link_url=url,
                    link_type=link_type,
                    status='pending',
                    message=''
                )
            else:
                return LinkResult(
                    source_file=rel_source,
                    line_number=line_num,
                    link_text=text,
                    link_url=url,
                    link_type=link_type,
                    status='skipped',
                    message='External link checking disabled'
                )

        elif link_type == 'anchor':
            # Check if anchor exists in same file
            try:
                content = source_file.read_text()
                anchor = url[1:]  # Remove #

                # Look for heading that would create this anchor
                headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
                anchors = [self._heading_to_anchor(h) for h in headings]

                if anchor.lower() in [a.lower() for a in anchors]:
                    return LinkResult(
                        source_file=rel_source,
                        line_number=line_num,
                        link_text=text,
                        link_url=url,
                        link_type=link_type,
                        status='ok',
                        message=''
                    )
                else:
                    return LinkResult(
                        source_file=rel_source,
                        line_number=line_num,
                        link_text=text,
                        link_url=url,
                        link_type=link_type,
                        status='broken',
                        message=f'Anchor not found in document'
                    )
            except Exception as e:
                return LinkResult(
                    source_file=rel_source,
                    line_number=line_num,
                    link_text=text,
                    link_url=url,
                    link_type=link_type,
                    status='warning',
                    message=f'Could not verify anchor: {e}'
                )

        elif link_type == 'mailto':
            return LinkResult(
                source_file=rel_source,
                line_number=line_num,
                link_text=text,
                link_url=url,
                link_type=link_type,
                status='skipped',
                message='mailto links not checked'
            )

        else:  # internal
            # Parse URL and anchor
            if '#' in url:
                path_part, anchor = url.split('#', 1)
            else:
                path_part, anchor = url, None

            # Resolve relative path
            if path_part:
                target = (source_file.parent / path_part).resolve()
            else:
                target = source_file

            # Check if file exists
            if not target.exists():
                return LinkResult(
                    source_file=rel_source,
                    line_number=line_num,
                    link_text=text,
                    link_url=url,
                    link_type=link_type,
                    status='broken',
                    message=f'File not found: {path_part}'
                )

            # If there's an anchor, check it
            if anchor:
                try:
                    content = target.read_text()
                    headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
                    anchors = [self._heading_to_anchor(h) for h in headings]

                    if anchor.lower() not in [a.lower() for a in anchors]:
                        return LinkResult(
                            source_file=rel_source,
                            line_number=line_num,
                            link_text=text,
                            link_url=url,
                            link_type=link_type,
                            status='warning',
                            message=f'Anchor #{anchor} not found in target file'
                        )
                except Exception:
                    pass

            return LinkResult(
                source_file=rel_source,
                line_number=line_num,
                link_text=text,
                link_url=url,
                link_type=link_type,
                status='ok',
                message=''
            )

    def _heading_to_anchor(self, heading: str) -> str:
        """Convert heading text to anchor ID."""
        # Basic conversion: lowercase, replace spaces with hyphens, remove special chars
        anchor = heading.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        return anchor

    def _check_external_links(self, links: list[LinkResult]):
        """Check external links in parallel."""
        def check_url(result: LinkResult) -> LinkResult:
            try:
                req = urllib.request.Request(
                    result.link_url,
                    method='HEAD',
                    headers={'User-Agent': 'Documentation Link Checker'}
                )
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.status < 400:
                        result.status = 'ok'
                    else:
                        result.status = 'broken'
                        result.message = f'HTTP {response.status}'
            except urllib.error.HTTPError as e:
                if e.code == 405:  # Method not allowed, try GET
                    try:
                        req = urllib.request.Request(
                            result.link_url,
                            headers={'User-Agent': 'Documentation Link Checker'}
                        )
                        with urllib.request.urlopen(req, timeout=10) as response:
                            if response.status < 400:
                                result.status = 'ok'
                            else:
                                result.status = 'broken'
                                result.message = f'HTTP {response.status}'
                    except Exception as e2:
                        result.status = 'broken'
                        result.message = str(e2)
                else:
                    result.status = 'broken'
                    result.message = f'HTTP {e.code}'
            except Exception as e:
                result.status = 'warning'
                result.message = str(e)
            return result

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(check_url, link): link for link in links}
            for future in as_completed(futures):
                # Results are updated in place
                pass

    def _generate_report(self) -> dict[str, Any]:
        """Generate a report of link checking results."""
        ok = [r for r in self.results if r.status == 'ok']
        broken = [r for r in self.results if r.status == 'broken']
        warnings = [r for r in self.results if r.status == 'warning']
        skipped = [r for r in self.results if r.status == 'skipped']

        return {
            'docs_path': str(self.docs_path),
            'summary': {
                'total_links': len(self.results),
                'ok': len(ok),
                'broken': len(broken),
                'warnings': len(warnings),
                'skipped': len(skipped),
            },
            'broken_links': [
                {
                    'file': r.source_file,
                    'line': r.line_number,
                    'text': r.link_text,
                    'url': r.link_url,
                    'type': r.link_type,
                    'message': r.message,
                }
                for r in broken
            ],
            'warnings': [
                {
                    'file': r.source_file,
                    'line': r.line_number,
                    'text': r.link_text,
                    'url': r.link_url,
                    'type': r.link_type,
                    'message': r.message,
                }
                for r in warnings
            ],
        }


def main():
    parser = argparse.ArgumentParser(
        description='Check links in documentation files'
    )
    parser.add_argument('docs_path', help='Path to documentation directory')
    parser.add_argument('--external', '-e', action='store_true',
                        help='Also check external links')
    parser.add_argument('--output', '-o', help='Output report to JSON file')

    args = parser.parse_args()

    try:
        checker = LinkChecker(args.docs_path, check_external=args.external)
        report = checker.check_all()

        # Output JSON if requested
        if args.output:
            Path(args.output).write_text(json.dumps(report, indent=2))
            print(f"Report written to: {args.output}")

        # Print summary
        print("\n" + "="*60)
        print("LINK CHECK REPORT")
        print("="*60)
        print(f"Total links: {report['summary']['total_links']}")
        print(f"  OK: {report['summary']['ok']}")
        print(f"  Broken: {report['summary']['broken']}")
        print(f"  Warnings: {report['summary']['warnings']}")
        print(f"  Skipped: {report['summary']['skipped']}")

        # Print broken links
        if report['broken_links']:
            print("\n" + "-"*60)
            print("BROKEN LINKS")
            print("-"*60)
            for link in report['broken_links']:
                print(f"\n✗ {link['file']}:{link['line']}")
                print(f"  [{link['text']}]({link['url']})")
                print(f"  Error: {link['message']}")

        # Exit with error if broken links found
        if report['summary']['broken'] > 0:
            print(f"\n❌ FAILED: Found {report['summary']['broken']} broken link(s)")
            sys.exit(1)
        else:
            print("\n✓ All links are valid")
            sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
