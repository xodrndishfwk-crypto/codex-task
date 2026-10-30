#!/usr/bin/env python3
"""Validate the toolkit structure and high-risk content locally."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "START.md", "MENU.md", "kit.py",
    "skills/start/SKILL.md", "skills/needs/SKILL.md",
    "skills/ask/SKILL.md", "skills/plan/SKILL.md",
    "skills/time/SKILL.md", "skills/debug/SKILL.md",
    "skills/test/SKILL.md", "skills/docs/SKILL.md",
    "skills/review/SKILL.md",
    "templates/requirements.md", "templates/plan.md",
    "templates/validation-report.md", "templates/submission-checklist.md",
    "templates/worklog.md", "templates/final-defense-notes.md",
    "docs/USAGE.md", "docs/PRETRIAL-CHECKLIST.md",
    "docs/ALLOWED-USE-REVIEW.md", "docs/MCP-OPTIONAL.md",
    "docs/EXAM-STRATEGY.md",
]
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
TEXT_SUFFIXES = {".md", ".py", ".txt", ".yaml", ".yml", ".json", ".toml"}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for skill in (root / "skills").glob("*/SKILL.md") if (root / "skills").exists() else []:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            errors.append(f"invalid skill frontmatter: {skill.relative_to(root)}")

    ignored_parts = {".git", "__pycache__", ".pytest_cache"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label}: {path.relative_to(root)}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION PASSED: {len(REQUIRED)} required files and local secret patterns checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
