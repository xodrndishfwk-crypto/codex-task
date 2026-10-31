#!/usr/bin/env python3
"""Validate the toolkit structure and high-risk content locally."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "START-HERE.md", "WHAT-EACH-TOOL-DOES.md", "kit.py",
    "skills/inspect-task-and-choose-workflow/SKILL.md",
    "skills/list-required-results-and-rules/SKILL.md",
    "skills/prepare-clear-business-questions/SKILL.md",
    "skills/plan-small-steps-and-checks/SKILL.md",
    "skills/plan-time-and-stop-points/SKILL.md",
    "skills/inspect-app-project-and-run-locally/SKILL.md",
    "skills/define-app-users-screens-and-core-flow/SKILL.md",
    "skills/build-smallest-working-app-first/SKILL.md",
    "skills/connect-app-data-storage-and-state/SKILL.md",
    "skills/test-app-screens-inputs-and-navigation/SKILL.md",
    "skills/list-and-group-input-files/SKILL.md",
    "skills/turn-manual-into-rule-checklist/SKILL.md",
    "skills/extract-facts-and-record-sources/SKILL.md",
    "skills/apply-rules-and-explain-each-decision/SKILL.md",
    "skills/find-missing-duplicate-or-conflicting-data/SKILL.md",
    "skills/analyze-table-data-and-find-patterns/SKILL.md",
    "skills/rank-items-and-explain-the-order/SKILL.md",
    "skills/build-result-table-and-short-summary/SKILL.md",
    "skills/find-and-fix-code-errors/SKILL.md",
    "skills/test-results-against-requirements/SKILL.md",
    "skills/write-result-and-test-report/SKILL.md",
    "skills/check-everything-before-submit/SKILL.md",
    "templates/required-results-and-rules.md",
    "templates/step-by-step-work-plan.md",
    "templates/test-results-and-evidence.md",
    "templates/final-submission-checklist.md",
    "templates/decisions-and-work-log.md",
    "templates/work-explanation-notes.md",
    "templates/app-user-flow-and-screen-plan.md",
    "templates/app-screen-and-flow-test-checklist.md",
    "templates/input-file-list.md", "templates/rule-checklist.md",
    "templates/facts-with-sources.md", "templates/decision-table.md",
    "docs/HOW-TO-USE-THIS-TOOLKIT.md",
    "docs/BEFORE-EXAM-CHECKLIST.md",
    "docs/ALLOWED-AND-NOT-ALLOWED.md",
    "docs/WHEN-MCP-IS-SAFE-TO-USE.md",
    "docs/STEP-BY-STEP-EXAM-WORKFLOW.md",
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
            continue
        match = re.search(r"^name:\s*([^\s]+)\s*$", text, re.MULTILINE)
        if match and match.group(1) != skill.parent.name:
            errors.append(f"skill name does not match folder: {skill.relative_to(root)}")

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
