#!/usr/bin/env python3
"""Generate testing dependencies for Next.js projects."""

import argparse
import json
import sys


def generate_dependencies(nextjs_version: str, typescript: bool) -> dict:
    """Generate package.json dependencies for testing setup."""

    deps = {
        "devDependencies": {
            "vitest": "^2.0.0",
            "@vitejs/plugin-react": "^4.3.0",
            "@testing-library/react": "^16.0.0",
            "@testing-library/jest-dom": "^6.5.0",
            "@testing-library/user-event": "^14.5.0",
            "jsdom": "^25.0.0",
            "@playwright/test": "^1.48.0",
            "@axe-core/playwright": "^4.10.0",
            "happy-dom": "^15.0.0"
        }
    }

    if typescript:
        deps["devDependencies"]["@types/node"] = "^22.0.0"

    # Add coverage tools
    deps["devDependencies"]["@vitest/ui"] = "^2.0.0"
    deps["devDependencies"]["@vitest/coverage-v8"] = "^2.0.0"

    return deps


def generate_scripts() -> dict:
    """Generate package.json scripts for testing."""
    return {
        "scripts": {
            "test": "vitest",
            "test:ui": "vitest --ui",
            "test:watch": "vitest --watch",
            "test:coverage": "vitest --coverage",
            "test:e2e": "playwright test",
            "test:e2e:ui": "playwright test --ui",
            "test:e2e:debug": "playwright test --debug",
            "test:e2e:report": "playwright show-report"
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate testing dependencies for Next.js projects"
    )
    parser.add_argument(
        "--nextjs-version",
        default="14",
        help="Next.js version (default: 14)"
    )
    parser.add_argument(
        "--typescript",
        action="store_true",
        help="Include TypeScript types"
    )
    parser.add_argument(
        "--output",
        choices=["json", "install"],
        default="install",
        help="Output format (json or install command)"
    )

    args = parser.parse_args()

    deps = generate_dependencies(args.nextjs_version, args.typescript)
    scripts = generate_scripts()

    if args.output == "json":
        output = {**deps, **scripts}
        print(json.dumps(output, indent=2))
    else:
        # Generate install command
        packages = " ".join(
            f"{pkg}@{version}"
            for pkg, version in deps["devDependencies"].items()
        )
        print(f"npm install -D {packages}")
        print("\nAdd these scripts to package.json:")
        print(json.dumps(scripts, indent=2))


if __name__ == "__main__":
    main()
