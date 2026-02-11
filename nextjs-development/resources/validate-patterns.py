#!/usr/bin/env python3
"""
Next.js Pattern Validator

Validates Next.js App Router patterns in a source directory:
- Server Components don't use client-only APIs
- Client Components have 'use client' directive
- Data fetching uses proper cache strategy
- Server Actions are marked with 'use server'
- Metadata API used correctly
- Image optimization (<Image> not <img>)
- Dynamic imports for heavy components

Usage: python validate-patterns.py /path/to/src
"""

import argparse
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class ValidationIssue:
    file: str
    line: int
    severity: str  # "error", "warning"
    rule: str
    message: str


CLIENT_ONLY_APIS = [
    "useState",
    "useEffect",
    "useReducer",
    "useRef",
    "useCallback",
    "useMemo",
    "useContext",
    "useLayoutEffect",
    "useInsertionEffect",
    "useTransition",
    "useDeferredValue",
    "useSyncExternalStore",
    "useFormStatus",
    "useOptimistic",
    "onClick",
    "onChange",
    "onSubmit",
    "onFocus",
    "onBlur",
    "addEventListener",
    "window.",
    "document.",
    "localStorage",
    "sessionStorage",
]

HEAVY_LIBRARIES = [
    "chart.js",
    "recharts",
    "d3",
    "three",
    "monaco-editor",
    "codemirror",
    "mapbox-gl",
    "leaflet",
    "video.js",
    "quill",
    "draft-js",
    "slate",
    "tiptap",
    "framer-motion",
    "gsap",
    "lottie",
]


def has_use_client(content: str) -> bool:
    """Check if file has 'use client' directive."""
    first_lines = content.split("\n")[:5]
    return any("use client" in line for line in first_lines)


def has_use_server(content: str) -> bool:
    """Check if file has 'use server' directive."""
    first_lines = content.split("\n")[:5]
    return any("use server" in line for line in first_lines)


def is_component_file(path: Path) -> bool:
    """Check if file is a React component (tsx/jsx in app/ or components/)."""
    suffixes = {".tsx", ".jsx"}
    return path.suffix in suffixes


def validate_server_component(path: Path, content: str) -> list[ValidationIssue]:
    """Check that server components don't use client-only APIs."""
    issues = []
    if has_use_client(content):
        return issues  # Client component, skip

    for i, line in enumerate(content.split("\n"), 1):
        # Skip imports and comments
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("import"):
            continue

        for api in CLIENT_ONLY_APIS:
            if api in line and not f"// {api}" in line:
                # Check for hooks specifically (must start with "use")
                if api.startswith("use"):
                    pattern = rf"\b{re.escape(api)}\b"
                    if re.search(pattern, line):
                        issues.append(ValidationIssue(
                            file=str(path),
                            line=i,
                            severity="error",
                            rule="no-client-api-in-server",
                            message=f"Client-only API '{api}' used in Server Component. Add 'use client' directive or move to a Client Component.",
                        ))
                elif api in ["window.", "document.", "localStorage", "sessionStorage"]:
                    if api in line:
                        issues.append(ValidationIssue(
                            file=str(path),
                            line=i,
                            severity="error",
                            rule="no-browser-api-in-server",
                            message=f"Browser API '{api.rstrip('.')}' used in Server Component.",
                        ))
    return issues


def validate_client_directive(path: Path, content: str) -> list[ValidationIssue]:
    """Check that files using client APIs have 'use client' directive."""
    issues = []
    if has_use_client(content):
        return issues

    uses_client_api = False
    for line in content.split("\n"):
        for api in ["useState", "useEffect", "useReducer", "onClick", "onChange"]:
            if re.search(rf"\b{api}\b", line) and not line.strip().startswith("//"):
                uses_client_api = True
                break
        if uses_client_api:
            break

    if uses_client_api:
        issues.append(ValidationIssue(
            file=str(path),
            line=1,
            severity="error",
            rule="missing-use-client",
            message="File uses client APIs but missing 'use client' directive.",
        ))
    return issues


def validate_server_actions(path: Path, content: str) -> list[ValidationIssue]:
    """Check that server actions are properly marked."""
    issues = []
    # Check for async functions that look like server actions
    if "formAction" in content or "action=" in content:
        # Check if any function has 'use server'
        if "'use server'" not in content and '"use server"' not in content:
            for i, line in enumerate(content.split("\n"), 1):
                if "formAction" in line or re.search(r'action\s*=\s*\{', line):
                    issues.append(ValidationIssue(
                        file=str(path),
                        line=i,
                        severity="warning",
                        rule="server-action-directive",
                        message="Form action used but no 'use server' directive found. Ensure server actions are marked.",
                    ))
                    break
    return issues


def validate_image_optimization(path: Path, content: str) -> list[ValidationIssue]:
    """Check that <Image> is used instead of <img>."""
    issues = []
    for i, line in enumerate(content.split("\n"), 1):
        if "<img " in line or "<img>" in line:
            if line.strip().startswith("//") or line.strip().startswith("*"):
                continue
            issues.append(ValidationIssue(
                file=str(path),
                line=i,
                severity="warning",
                rule="use-next-image",
                message="Use next/image <Image> component instead of <img> for automatic optimization.",
            ))
    return issues


def validate_metadata(path: Path, content: str) -> list[ValidationIssue]:
    """Check metadata API usage in layout/page files."""
    issues = []
    name = path.name.split(".")[0]

    if name in ["layout", "page"]:
        has_metadata_export = "export const metadata" in content or "export function generateMetadata" in content
        has_head_tag = "<head>" in content or "<Head>" in content

        if has_head_tag and not has_metadata_export:
            for i, line in enumerate(content.split("\n"), 1):
                if "<head>" in line or "<Head>" in line:
                    issues.append(ValidationIssue(
                        file=str(path),
                        line=i,
                        severity="warning",
                        rule="use-metadata-api",
                        message="Use Next.js Metadata API (export const metadata) instead of <head>/<Head>.",
                    ))
                    break
    return issues


def validate_dynamic_imports(path: Path, content: str) -> list[ValidationIssue]:
    """Check that heavy libraries use dynamic imports."""
    issues = []
    for i, line in enumerate(content.split("\n"), 1):
        if not line.strip().startswith("import "):
            continue
        for lib in HEAVY_LIBRARIES:
            if f'"{lib}"' in line or f"'{lib}'" in line:
                if "dynamic(" not in content and "next/dynamic" not in content:
                    issues.append(ValidationIssue(
                        file=str(path),
                        line=i,
                        severity="warning",
                        rule="dynamic-import-heavy-lib",
                        message=f"Heavy library '{lib}' imported statically. Consider using next/dynamic for code splitting.",
                    ))
    return issues


def validate_cache_strategy(path: Path, content: str) -> list[ValidationIssue]:
    """Check that data fetching uses proper cache configuration."""
    issues = []
    for i, line in enumerate(content.split("\n"), 1):
        if "fetch(" in line:
            # Check if cache or revalidate is specified
            fetch_block = content[content.index("fetch("):content.index("fetch(") + 500]
            if "cache:" not in fetch_block and "revalidate" not in fetch_block and "next:" not in fetch_block:
                issues.append(ValidationIssue(
                    file=str(path),
                    line=i,
                    severity="warning",
                    rule="explicit-cache-strategy",
                    message="fetch() without explicit cache/revalidate config. Specify { cache: 'force-cache' } or { next: { revalidate: N } }.",
                ))
            break  # Only flag once per file
    return issues


def validate_file(path: Path) -> list[ValidationIssue]:
    """Run all validations on a single file."""
    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return []

    issues = []
    if is_component_file(path):
        issues.extend(validate_server_component(path, content))
        issues.extend(validate_client_directive(path, content))
        issues.extend(validate_server_actions(path, content))
        issues.extend(validate_image_optimization(path, content))
        issues.extend(validate_metadata(path, content))
        issues.extend(validate_dynamic_imports(path, content))
        issues.extend(validate_cache_strategy(path, content))
    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate Next.js App Router patterns")
    parser.add_argument("src_dir", help="Source directory to validate")
    parser.add_argument("--severity", choices=["error", "warning", "all"], default="all", help="Minimum severity to report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    src = Path(args.src_dir)
    if not src.is_dir():
        print(f"Error: {src} is not a directory", file=sys.stderr)
        sys.exit(1)

    all_issues: list[ValidationIssue] = []
    file_count = 0

    for path in sorted(src.rglob("*")):
        if path.is_file() and is_component_file(path):
            if "node_modules" in str(path) or ".next" in str(path):
                continue
            file_count += 1
            all_issues.extend(validate_file(path))

    # Filter by severity
    if args.severity != "all":
        all_issues = [i for i in all_issues if i.severity == args.severity]

    if args.json:
        import json
        print(json.dumps([{
            "file": i.file, "line": i.line, "severity": i.severity,
            "rule": i.rule, "message": i.message,
        } for i in all_issues], indent=2))
    else:
        errors = [i for i in all_issues if i.severity == "error"]
        warnings = [i for i in all_issues if i.severity == "warning"]

        print(f"Scanned {file_count} component files\n")

        if errors:
            print(f"ERRORS ({len(errors)}):")
            for i in errors:
                print(f"  {i.file}:{i.line} [{i.rule}] {i.message}")
            print()

        if warnings:
            print(f"WARNINGS ({len(warnings)}):")
            for i in warnings:
                print(f"  {i.file}:{i.line} [{i.rule}] {i.message}")
            print()

        if not all_issues:
            print("No issues found!")

        print(f"Total: {len(errors)} errors, {len(warnings)} warnings")

    sys.exit(1 if any(i.severity == "error" for i in all_issues) else 0)


if __name__ == "__main__":
    main()
