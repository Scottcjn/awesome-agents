#!/usr/bin/env python3
"""Dependency-free integrity checks for the Awesome Agents catalog."""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

CATALOG_ROW = re.compile(r"^- \[([^\]]+)\]\((https?://[^)\s]+)\) - (.+)$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
ANCHOR_LINK = re.compile(r"\]\(#([^)]+)\)")


def heading_slug(title: str) -> str:
    """Return the GitHub-style slug used for ordinary Markdown headings."""
    title = re.sub(r"`([^`]*)`", r"\1", title)
    title = re.sub(r"<[^>]+>", "", title).lower()
    title = re.sub(r"[^\w\- ]", "", title)
    return re.sub(r"\s+", "-", title.strip())


def heading_anchors(readme: str) -> set[str]:
    """Collect heading anchors, accounting for duplicate headings and code fences."""
    anchors: set[str] = set()
    seen: Counter[str] = Counter()
    fence: str | None = None

    for line in readme.splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)[0]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is not None:
            continue

        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        base = heading_slug(heading.group(1))
        occurrence = seen[base]
        seen[base] += 1
        anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return anchors


def extract_catalog_entries(readme: str) -> tuple[list[tuple[int, str, str]], list[str]]:
    """Return (line, label, URL) entries and row-format errors for catalog sections."""
    lines = readme.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == "## Platforms")
        end = next(i for i, line in enumerate(lines[start + 1 :], start + 1) if line.strip() == "## Contributing")
    except StopIteration:
        return [], ["README must contain ## Platforms and ## Contributing headings"]

    entries: list[tuple[int, str, str]] = []
    errors: list[str] = []
    for index in range(start + 1, end):
        line = lines[index]
        if not line.startswith("- "):
            continue
        match = CATALOG_ROW.fullmatch(line)
        if not match:
            errors.append(f"README.md:{index + 1}: catalog bullet must use `- [Name](https://...) - Description`")
            continue
        label, url, description = match.groups()
        if not description.rstrip().endswith("."):
            errors.append(f"README.md:{index + 1}: catalog description must end with a period")
        entries.append((index + 1, label, url))
    return entries, errors


def canonical_url(url: str) -> str:
    """Normalize only URL details that do not identify a distinct resource."""
    parts = urlsplit(url)
    path = parts.path.rstrip("/")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


def duplicate_targets(entries: list[tuple[int, str, str]]) -> dict[str, list[tuple[int, str]]]:
    grouped: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for line, label, url in entries:
        grouped[canonical_url(url)].append((line, label))
    return {url: rows for url, rows in grouped.items() if len(rows) > 1}


def validate_repository(root: Path) -> list[str]:
    root = Path(root)
    readme_path = root / "README.md"
    if not readme_path.is_file():
        return ["README.md is missing"]

    readme = readme_path.read_text(encoding="utf-8")
    errors: list[str] = []
    anchors = heading_anchors(readme)

    for line_number, line in enumerate(readme.splitlines(), 1):
        for fragment in ANCHOR_LINK.findall(line):
            if unquote(fragment) not in anchors:
                errors.append(f"README.md:{line_number}: broken in-file anchor #{fragment}")

    for match in MARKDOWN_LINK.finditer(readme):
        destination = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        parts = urlsplit(destination)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        local_path = root / unquote(parts.path)
        if not local_path.is_file():
            errors.append(f"README.md: local link target does not exist: {parts.path}")

    entries, row_errors = extract_catalog_entries(readme)
    errors.extend(row_errors)
    for url, rows in duplicate_targets(entries).items():
        labels = ", ".join(f"{label} (line {line})" for line, label in rows)
        errors.append(f"duplicate catalog target {url}: {labels}")

    license_path = root / "LICENSE"
    if not license_path.is_file() or not license_path.read_text(encoding="utf-8").startswith("MIT License"):
        errors.append("LICENSE must contain the MIT License text")
    if not re.search(r"\[!\[MIT License\]\([^)]+\)\]\(LICENSE\)", readme):
        errors.append("README license badge must identify the MIT License and link to LICENSE")
    if "[MIT License](LICENSE)" not in readme or re.search(r"\bCC0\b|Creative Commons Zero", readme, re.I):
        errors.append("README license text must match the MIT LICENSE file (not CC0)")

    bcos_path = root / "BCOS.md"
    bcos_text = bcos_path.read_text(encoding="utf-8") if bcos_path.is_file() else ""
    if not re.search(r"\[!\[BCOS Status:\s*Pending\]\([^)]+\)\]\(BCOS\.md\)", readme):
        errors.append("README must show the BCOS status as Pending and link to BCOS.md")
    if not re.search(r"On-Chain Proof\*\*:\s*pending", bcos_text, re.I):
        errors.append("BCOS.md must explicitly state the on-chain proof status")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    readme = (root / "README.md").read_text(encoding="utf-8")
    entries, _ = extract_catalog_entries(readme)
    print(
        f"Catalog checks passed: {len(entries)} entries; anchors, local links, row format, "
        "unique targets, MIT license, and pending BCOS status are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
