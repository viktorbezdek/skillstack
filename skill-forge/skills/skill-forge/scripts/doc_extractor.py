#!/usr/bin/env python3
"""
Documentation Extractor for skill-creator-from-docs

Extracts documentation from URLs (via crawl4ai-cli) or local markdown files.
Creates a structured DocumentationCorpus for analysis.
"""

import json
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any
from urllib.parse import urlparse


@dataclass
class Page:
    """Represents a single documentation page."""
    url: str
    title: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __repr__(self):
        return f"Page(url='{self.url}', title='{self.title}', length={len(self.content)})"


@dataclass
class DocumentationCorpus:
    """Collection of documentation pages with metadata."""
    source: str
    pages: List[Page]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if 'extraction_date' not in self.metadata:
            self.metadata['extraction_date'] = datetime.now().isoformat()

    def __repr__(self):
        return f"DocumentationCorpus(source='{self.source}', pages={len(self.pages)})"

    def total_content_length(self) -> int:
        """Calculate total content length across all pages."""
        return sum(len(page.content) for page in self.pages)

    def get_page_by_url(self, url: str) -> Optional[Page]:
        """Find page by URL."""
        for page in self.pages:
            if page.url == url:
                return page
        return None


class DocExtractor:
    """Extract documentation from various sources."""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[DocExtractor] {message}", file=sys.stderr)

    def extract_from_url(
        self,
        url: str,
        key_pages: Optional[List[str]] = None,
        use_crawl4ai: bool = True
    ) -> DocumentationCorpus:
        """
        Extract documentation from URL using crawl4ai-cli.

        Args:
            url: Base URL to extract from
            key_pages: Optional list of specific pages to focus on
            use_crawl4ai: Whether to use crawl4ai-cli skill (True) or direct approach

        Returns:
            DocumentationCorpus with extracted pages

        Raises:
            RuntimeError: If extraction fails
        """
        self.log(f"Extracting from URL: {url}")

        if use_crawl4ai:
            return self._extract_with_crawl4ai(url, key_pages)
        else:
            return self._extract_direct(url, key_pages)

    def _extract_with_crawl4ai(
        self,
        url: str,
        key_pages: Optional[List[str]] = None
    ) -> DocumentationCorpus:
        """
        Extract using crawl4ai-cli skill.

        This method would integrate with the crawl4ai-cli skill.
        For now, returns a placeholder implementation.
        """
        self.log("Using crawl4ai-cli for extraction")

        # TODO: Integrate with crawl4ai-cli skill
        # For now, create a minimal corpus

        try:
            # Placeholder: Would use crawl4ai-cli skill here
            self.log("⚠️  crawl4ai-cli integration not yet implemented")
            self.log("   Falling back to direct extraction")

            return self._extract_direct(url, key_pages)

        except Exception as e:
            raise RuntimeError(f"crawl4ai extraction failed: {e}")

    def _extract_direct(
        self,
        url: str,
        key_pages: Optional[List[str]] = None
    ) -> DocumentationCorpus:
        """
        Direct extraction without crawl4ai (fallback).

        Uses basic HTTP fetch for single-page docs.
        """
        self.log("Using direct extraction (fallback)")

        try:
            import requests
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            # Parse HTML to markdown if needed
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = soup.title.string if soup.title else urlparse(url).path

            # Extract main content (simple approach)
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()

            content = soup.get_text(separator='\n', strip=True)

            page = Page(
                url=url,
                title=title,
                content=content,
                metadata={'method': 'direct_fetch'}
            )

            corpus = DocumentationCorpus(
                source=url,
                pages=[page],
                metadata={
                    'extraction_method': 'direct',
                    'key_pages': key_pages or []
                }
            )

            self.log(f"✅ Extracted 1 page ({len(content)} chars)")
            return corpus

        except ImportError as e:
            raise RuntimeError(
                f"Direct extraction requires 'requests' and 'beautifulsoup4': {e}\n"
                "Install with: pip install requests beautifulsoup4"
            )
        except Exception as e:
            raise RuntimeError(f"Direct extraction failed: {e}")

    def extract_from_markdown(self, file_path: str) -> DocumentationCorpus:
        """
        Extract documentation from local markdown file(s).

        Args:
            file_path: Path to markdown file or directory

        Returns:
            DocumentationCorpus with extracted pages

        Raises:
            FileNotFoundError: If file doesn't exist
            RuntimeError: If extraction fails
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Documentation not found: {file_path}")

        pages = []

        if path.is_file():
            self.log(f"Extracting from file: {path}")
            pages.append(self._extract_markdown_file(path))
        elif path.is_dir():
            self.log(f"Extracting from directory: {path}")
            md_files = list(path.rglob("*.md"))
            self.log(f"Found {len(md_files)} markdown files")

            for md_file in md_files:
                try:
                    pages.append(self._extract_markdown_file(md_file))
                except Exception as e:
                    self.log(f"⚠️  Failed to extract {md_file}: {e}")
        else:
            raise RuntimeError(f"Invalid path: {file_path}")

        corpus = DocumentationCorpus(
            source=str(path.absolute()),
            pages=pages,
            metadata={
                'extraction_method': 'markdown',
                'total_files': len(pages)
            }
        )

        self.log(f"✅ Extracted {len(pages)} pages ({corpus.total_content_length()} chars)")
        return corpus

    def _extract_markdown_file(self, file_path: Path) -> Page:
        """Extract content from a single markdown file."""
        content = file_path.read_text(encoding='utf-8')

        # Try to extract title from first h1 or filename
        title = file_path.stem
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                title = line[2:].strip()
                break

        return Page(
            url=f"file://{file_path.absolute()}",
            title=title,
            content=content,
            metadata={
                'file_path': str(file_path),
                'file_size': file_path.stat().st_size
            }
        )

    def save_raw_docs(
        self,
        corpus: DocumentationCorpus,
        output_dir: str,
        format: str = 'markdown'
    ):
        """
        Save raw documentation to disk.

        Args:
            corpus: Documentation corpus to save
            output_dir: Directory to save to
            format: 'markdown' or 'json'
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        self.log(f"Saving raw docs to: {output_dir}")

        if format == 'markdown':
            for i, page in enumerate(corpus.pages):
                filename = f"page_{i:03d}_{self._sanitize_filename(page.title)}.md"
                file_path = output_path / filename

                # Write markdown with metadata header
                content = f"""---
url: {page.url}
title: {page.title}
extracted: {corpus.metadata.get('extraction_date')}
---

{page.content}
"""
                file_path.write_text(content, encoding='utf-8')

            # Save corpus metadata
            metadata_file = output_path / "_metadata.json"
            metadata_file.write_text(
                json.dumps(corpus.metadata, indent=2),
                encoding='utf-8'
            )

            self.log(f"✅ Saved {len(corpus.pages)} pages + metadata")

        elif format == 'json':
            # Save as JSON
            data = {
                'source': corpus.source,
                'metadata': corpus.metadata,
                'pages': [
                    {
                        'url': p.url,
                        'title': p.title,
                        'content': p.content,
                        'metadata': p.metadata
                    }
                    for p in corpus.pages
                ]
            }

            json_file = output_path / "corpus.json"
            json_file.write_text(
                json.dumps(data, indent=2),
                encoding='utf-8'
            )

            self.log(f"✅ Saved corpus as JSON")

        else:
            raise ValueError(f"Unknown format: {format}")

    @staticmethod
    def _sanitize_filename(name: str) -> str:
        """Convert title to safe filename."""
        # Remove/replace unsafe characters
        safe = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name)
        # Collapse multiple spaces/underscores
        safe = '_'.join(safe.split())
        # Limit length
        return safe[:50]


def main():
    """CLI interface for doc_extractor."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract documentation from URLs or markdown files"
    )
    parser.add_argument(
        'source',
        help='URL or file/directory path to extract from'
    )
    parser.add_argument(
        '--key-pages',
        nargs='+',
        help='Specific pages to focus on (URLs)'
    )
    parser.add_argument(
        '--output-dir',
        default='planning/research-logs/raw',
        help='Directory to save raw documentation (default: planning/research-logs/raw)'
    )
    parser.add_argument(
        '--format',
        choices=['markdown', 'json'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '--no-crawl4ai',
        action='store_true',
        help='Do not use crawl4ai-cli (use direct fetch)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )

    args = parser.parse_args()

    extractor = DocExtractor(verbose=not args.quiet)

    try:
        # Determine if source is URL or file
        if args.source.startswith(('http://', 'https://')):
            corpus = extractor.extract_from_url(
                args.source,
                key_pages=args.key_pages,
                use_crawl4ai=not args.no_crawl4ai
            )
        else:
            if args.key_pages:
                print("⚠️  --key-pages ignored for local files", file=sys.stderr)
            corpus = extractor.extract_from_markdown(args.source)

        # Save raw docs
        extractor.save_raw_docs(corpus, args.output_dir, format=args.format)

        # Print summary
        print(f"\n✅ Extraction complete!")
        print(f"   Source: {corpus.source}")
        print(f"   Pages: {len(corpus.pages)}")
        print(f"   Total content: {corpus.total_content_length():,} characters")
        print(f"   Output: {args.output_dir}")

        return 0

    except Exception as e:
        print(f"\n❌ Extraction failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
