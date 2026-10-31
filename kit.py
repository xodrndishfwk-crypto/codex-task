#!/usr/bin/env python3
"""Small local entry point for the public Codex task toolkit."""

from __future__ import annotations

import csv
import json
import statistics
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def print_help() -> None:
    print("Codex task kit")
    print("  python kit.py check          validate this toolkit")
    print("  python kit.py scan [PATH]    summarize a task folder")
    print("  python kit.py files [PATH]   list input files with size and type")
    print("  python kit.py data FILE      inspect a CSV or JSON file")
    print("  python kit.py decisions FILE check a decision CSV for missing evidence")
    print("  python kit.py menu           show the simple skill menu")
    print("Start guide: START-HERE.md")


def check() -> int:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_toolkit.py")],
        check=False,
    ).returncode


def scan(path: Path) -> int:
    path = path.resolve()
    if not path.is_dir():
        print(f"ERROR: folder not found: {path}")
        return 2

    ignored = {".git", "node_modules", "__pycache__", ".venv", "venv"}
    files = [p for p in path.rglob("*") if p.is_file() and not any(part in ignored for part in p.parts)]
    extensions = Counter((p.suffix.lower() or "[no extension]") for p in files)
    markers = [
        "README.md", "AGENTS.md", "package.json", "pyproject.toml",
        "requirements.txt", "Cargo.toml", "go.mod", "Makefile",
    ]
    data_suffixes = {".csv", ".json", ".jsonl", ".xlsx", ".xls", ".tsv", ".parquet"}

    print(f"FOLDER: {path}")
    print(f"FILES: {len(files)}")
    print("TOP TYPES:")
    for suffix, count in extensions.most_common(12):
        print(f"  {suffix}: {count}")
    print("KEY FILES:")
    found_markers = [name for name in markers if (path / name).exists()]
    for name in found_markers or ["[none at folder root]"]:
        print(f"  {name}")
    print("DATA FILES:")
    data_files = [p.relative_to(path) for p in files if p.suffix.lower() in data_suffixes]
    for item in data_files[:30] or ["[none detected]"]:
        print(f"  {item}")
    if len(data_files) > 30:
        print(f"  ... and {len(data_files) - 30} more")
    return 0


def list_files(path: Path) -> int:
    path = path.resolve()
    if not path.is_dir():
        print(f"ERROR: folder not found: {path}")
        return 2
    ignored = {".git", "node_modules", "__pycache__", ".venv", "venv"}
    files = sorted(
        p for p in path.rglob("*")
        if p.is_file() and not any(part in ignored for part in p.parts)
    )
    print("PATH\tTYPE\tBYTES")
    for item in files:
        print(f"{item.relative_to(path)}\t{item.suffix.lower() or '[none]'}\t{item.stat().st_size}")
    print(f"TOTAL FILES: {len(files)}")
    return 0


def _blank(value: object) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def _number(value: object) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(str(value).replace(",", "").strip())
    except ValueError:
        return None


def _profile_rows(rows: list[dict[str, object]], source: Path) -> int:
    columns = list(dict.fromkeys(key for row in rows for key in row))
    print(f"FILE: {source}")
    print(f"ROWS: {len(rows)}")
    print(f"COLUMNS: {len(columns)}")
    duplicate_count = len(rows) - len({json.dumps(row, sort_keys=True, ensure_ascii=False, default=str) for row in rows})
    print(f"DUPLICATE ROWS: {duplicate_count}")
    print("COLUMN PROFILE:")
    for column in columns:
        values = [row.get(column) for row in rows]
        blanks = sum(_blank(value) for value in values)
        nonblank = [value for value in values if not _blank(value)]
        unique = len({str(value) for value in nonblank})
        numbers = [number for value in nonblank if (number := _number(value)) is not None]
        summary = f"  {column}: blank={blanks}, unique={unique}"
        if numbers and len(numbers) == len(nonblank):
            summary += f", min={min(numbers):g}, max={max(numbers):g}, mean={statistics.fmean(numbers):g}"
        print(summary)
    return 0


def inspect_data(path: Path) -> int:
    path = path.resolve()
    if not path.is_file():
        print(f"ERROR: file not found: {path}")
        return 2
    suffix = path.suffix.lower()
    try:
        if suffix == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.DictReader(stream))
            return _profile_rows(rows, path)
        if suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return _profile_rows(data, path)
            if isinstance(data, dict):
                print(f"FILE: {path}")
                print("JSON OBJECT KEYS:")
                for key, value in data.items():
                    kind = type(value).__name__
                    size = len(value) if isinstance(value, (list, dict, str)) else "-"
                    print(f"  {key}: type={kind}, size={size}")
                return 0
            print(f"FILE: {path}\nJSON ROOT TYPE: {type(data).__name__}")
            return 0
    except (OSError, UnicodeError, csv.Error, json.JSONDecodeError) as error:
        print(f"ERROR: could not read {path}: {error}")
        return 1
    print("ERROR: data command currently supports .csv and .json")
    return 2


def check_decisions(path: Path) -> int:
    path = path.resolve()
    if not path.is_file() or path.suffix.lower() != ".csv":
        print(f"ERROR: decision CSV not found: {path}")
        return 2
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            rows = list(reader)
            fields = set(reader.fieldnames or [])
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"ERROR: could not read {path}: {error}")
        return 1
    aliases = {
        "subject": {"subject", "subject_id", "id", "대상", "대상 ID"},
        "decision": {"decision", "result", "판정", "전체 판정"},
        "reason": {"reason", "이유"},
        "source": {"source", "evidence", "근거", "근거 파일·위치"},
    }
    chosen = {key: next((name for name in names if name in fields), None) for key, names in aliases.items()}
    missing_columns = [key for key, name in chosen.items() if name is None]
    if missing_columns:
        print("ERROR: missing columns: " + ", ".join(missing_columns))
        return 2
    issues: list[str] = []
    seen: Counter[str] = Counter()
    for number, row in enumerate(rows, start=2):
        subject = str(row.get(chosen["subject"], "")).strip()
        if subject:
            seen[subject] += 1
        for key in ("subject", "decision", "reason", "source"):
            if _blank(row.get(chosen[key])):
                issues.append(f"row {number}: blank {key}")
    for subject, count in seen.items():
        if count > 1:
            issues.append(f"duplicate subject: {subject} ({count} rows)")
    print(f"ROWS: {len(rows)}")
    print(f"UNIQUE SUBJECTS: {len(seen)}")
    print(f"ISSUES: {len(issues)}")
    for issue in issues[:50]:
        print(f"  {issue}")
    if len(issues) > 50:
        print(f"  ... and {len(issues) - 50} more")
    return 1 if issues else 0


def main(argv: list[str]) -> int:
    if len(argv) == 1 or argv[1] in {"help", "-h", "--help"}:
        print_help()
        return 0
    command = argv[1]
    if command == "check":
        return check()
    if command == "menu":
        print((ROOT / "WHAT-EACH-TOOL-DOES.md").read_text(encoding="utf-8"))
        return 0
    if command == "scan":
        return scan(Path(argv[2]) if len(argv) > 2 else Path.cwd())
    if command == "files":
        return list_files(Path(argv[2]) if len(argv) > 2 else Path.cwd())
    if command == "data" and len(argv) > 2:
        return inspect_data(Path(argv[2]))
    if command == "decisions" and len(argv) > 2:
        return check_decisions(Path(argv[2]))
    print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
