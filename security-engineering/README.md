# security-engineering

Application security design, OWASP patterns, authentication architecture, secrets management, and threat-model-informed code review.

## Overview

This plugin provides the `security-engineering` skill for Claude Code.

## Installation

Install via the SkillStack marketplace or copy this plugin directory into your Claude Code plugins folder.

## Usage

Invoke by describing your task naturally. The skill activates on relevant queries.

**Activates for:**
- Design a JWT-based authentication system with refresh token rotation
- Review this login endpoint for security vulnerabilities
- How should I store API keys for third-party integrations?
- Implement role-based access control for our multi-tenant app

**Does NOT activate for:**
- Configure our AWS VPC security groups (Network/infra security — cloud-infrastructure skill)
- Help us pass our SOC2 Type II audit (Compliance audit — out of scope)
- Run a penetration test on our staging environment (Offensive/pentest — out of scope)

## Domain

**Engineering**

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
