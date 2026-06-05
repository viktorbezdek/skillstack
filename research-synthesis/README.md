# research-synthesis

Multi-source research coordination, evidence triangulation, competing-hypothesis analysis, and structured synthesis for knowledge-intensive tasks.

## Overview

This plugin provides the `research-synthesis` skill for Claude Code.

## Installation

Install via the SkillStack marketplace or copy this plugin directory into your Claude Code plugins folder.

## Usage

Invoke by describing your task naturally. The skill activates on relevant queries.

**Activates for:**
- Research the tradeoffs between gRPC and REST for internal microservice communication
- Synthesise what the evidence says about daily standups harming deep work
- Compare three sources on the effectiveness of TDD — what do they agree and disagree on?
- I have 5 conflicting reports on LLM inference costs — triangulate the actual picture

**Does NOT activate for:**
- Run a customer survey to validate our product hypothesis (Primary data collection — not synthesis)
- Explore this codebase and find where authentication happens (Code research — use CodeGraph/Semble)
- Write a blog post about distributed systems (Creative content generation — not evidence synthesis)

## Domain

**Meta-Infra**

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
