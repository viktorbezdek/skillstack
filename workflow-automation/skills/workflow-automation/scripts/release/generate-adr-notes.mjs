#!/usr/bin/env node
/**
 * Generate ADR/Design Spec links for semantic-release notes
 * SHAREABLE: Works with any repository via dynamic repo URL detection
 *
 * Usage: node generate-adr-notes.mjs [lastTag]
 * Output: Markdown section written to stdout (or nothing if no ADRs)
 *
 * ADR: 2025-12-06-release-notes-adr-linking
 */

import { execSync } from "child_process";
import { readFileSync, existsSync } from "fs";

// ADR: 2025-12-08-mise-env-centralized-config
// Configuration via environment variables with defaults for backward compatibility
const ADR_DIR = process.env.ADR_DIR || "docs/adr";
const DESIGN_DIR = process.env.DESIGN_DIR || "docs/design";

// ADR file pattern: YYYY-MM-DD-slug.md
const ADR_FILE_PATTERN = /^docs\/adr\/(\d{4}-\d{2}-\d{2}-[\w-]+)\.md$/;
// Design spec pattern: YYYY-MM-DD-slug/spec.md
const DESIGN_SPEC_PATTERN = /^docs\/design\/(\d{4}-\d{2}-\d{2}-[\w-]+)\/spec\.md$/;
// ADR reference in commit messages: ADR: YYYY-MM-DD-slug
const ADR_COMMIT_REF_PATTERN = /ADR:\s*(\d{4}-\d{2}-\d{2}-[\w-]+)/g;

// Dynamic repo URL detection (works for any repo)
function getRepoUrl() {
  try {
    const remoteUrl = execSync("git remote get-url origin", {
      encoding: "utf8",
    }).trim();
    return remoteUrl
      .replace(/^git@github\.com:/, "https://github.com/")
      .replace(/\.git$/, "");
  } catch {
    throw new Error("Failed to get git remote URL");
  }
}

const REPO_URL = getRepoUrl();
const LAST_TAG = process.argv[2] || "";

/**
 * Get changed files via git diff
 * For first release (no tag), uses git ls-files to get all tracked files
 */
function getChangedFiles() {
  try {
    const cmd = LAST_TAG
      ? `git diff ${LAST_TAG}..HEAD --name-only --diff-filter=ACMR`
      : `git ls-files`;
    const output = execSync(cmd, { encoding: "utf8" }).trim();
    return output ? output.split("\n") : [];
  } catch {
    return [];
  }
}

/**
 * Parse commit messages for ADR references
 * Looks for patterns like "ADR: 2025-12-06-slug" in commit bodies
 */
function parseCommitMessages() {
  try {
    const cmd = LAST_TAG
      ? `git log ${LAST_TAG}..HEAD --format="%B"`
      : `git log HEAD --format="%B"`;
    const output = execSync(cmd, { encoding: "utf8" });
    const matches = [...output.matchAll(ADR_COMMIT_REF_PATTERN)];
    return matches.map((m) => m[1]);
  } catch {
    return [];
  }
}

/**
 * Extract title from H1 heading (skip YAML frontmatter)
 */
function extractTitle(filePath) {
  if (!existsSync(filePath)) return null;
  try {
    const content = readFileSync(filePath, "utf8");
    const lines = content.split("\n");
    let inFrontmatter = false;
    for (const line of lines) {
      if (line.trim() === "---") {
        inFrontmatter = !inFrontmatter;
        continue;
      }
      if (!inFrontmatter && line.startsWith("# ")) {
        return line.replace(/^# /, "").trim();
      }
    }
  } catch {
    // Ignore read errors - return null for fallback to slug
  }
  return null;
}

/**
 * Extract status from YAML frontmatter
 */
function extractStatus(filePath) {
  if (!existsSync(filePath)) return "unknown";
  try {
    const content = readFileSync(filePath, "utf8");
    const match = content.match(/^---\n([\s\S]*?)\n---/);
    if (!match) return "unknown";
    const statusMatch = match[1].match(/^status:\s*(\w+)/m);
    return statusMatch ? statusMatch[1] : "unknown";
  } catch {
    return "unknown";
  }
}

/**
 * Check if corresponding design spec exists for an ADR slug
 */
function findDesignSpec(adrSlug) {
  const specPath = `${DESIGN_DIR}/${adrSlug}/spec.md`;
  return existsSync(specPath) ? specPath : null;
}

// Main logic
const changedFiles = getChangedFiles();

// Filter for ADR files
const adrFiles = changedFiles.filter((f) => ADR_FILE_PATTERN.test(f));

// Filter for design spec files
const designFiles = changedFiles.filter((f) => DESIGN_SPEC_PATTERN.test(f));

// Get ADR references from commit messages
const commitSlugs = parseCommitMessages();

// Union + deduplicate ADR slugs
const allAdrSlugs = new Set();
adrFiles.forEach((f) => {
  const match = f.match(ADR_FILE_PATTERN);
  if (match) allAdrSlugs.add(match[1]);
});
commitSlugs.forEach((slug) => {
  if (existsSync(`${ADR_DIR}/${slug}.md`)) allAdrSlugs.add(slug);
});

// Collect design spec slugs from changed files
const allDesignSlugs = new Set();
designFiles.forEach((f) => {
  const match = f.match(DESIGN_SPEC_PATTERN);
  if (match) allDesignSlugs.add(match[1]);
});

// COUPLING: If design spec changed, include corresponding ADR
// This ensures ADR and spec always appear together in release notes
allDesignSlugs.forEach((slug) => {
  const adrPath = `${ADR_DIR}/${slug}.md`;
  if (existsSync(adrPath) && !allAdrSlugs.has(slug)) {
    allAdrSlugs.add(slug);
  }
});

// Exit silently if nothing found (prevents empty sections in release notes)
if (allAdrSlugs.size === 0 && allDesignSlugs.size === 0) {
  process.exit(0);
}

// Format output
let output = "\n---\n\n## Architecture Decisions\n";

if (allAdrSlugs.size > 0) {
  output += "\n### ADRs\n\n";
  for (const slug of [...allAdrSlugs].sort()) {
    const path = `${ADR_DIR}/${slug}.md`;
    const title = extractTitle(path) || slug;
    const status = extractStatus(path);
    const url = `${REPO_URL}/blob/main/${path}`;
    output += `- [${title}](${url}) (${status})\n`;

    // Check for corresponding design spec (add if not already tracked)
    const specPath = findDesignSpec(slug);
    if (specPath && !allDesignSlugs.has(slug)) {
      allDesignSlugs.add(slug);
    }
  }
}

if (allDesignSlugs.size > 0) {
  output += "\n### Design Specs\n\n";
  for (const slug of [...allDesignSlugs].sort()) {
    const path = `${DESIGN_DIR}/${slug}/spec.md`;
    if (existsSync(path)) {
      const title = extractTitle(path) || `${slug} Spec`;
      const url = `${REPO_URL}/blob/main/${path}`;
      output += `- [${title}](${url})\n`;
    }
  }
}

process.stdout.write(output);
