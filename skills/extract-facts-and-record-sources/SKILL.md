---
name: extract-facts-and-record-sources
description: Extract only rule-relevant facts from each subject's PDFs, tables, or documents and record the exact source location for every value.
---

# Extract Facts and Record Sources

Extract only the fields required by the rule checklist for each subject.

- Preserve values, units, dates, statuses, and relevant source wording.
- Link every value to a file path and a page, table row, or cell when available.
- Use the exact missing, unreadable, and conflict labels defined in `templates/facts-with-sources.md`.
- Do not interpret a blank value as zero or no.
- Select a sample of subjects and manually compare extracted values with the originals.

Record results in `templates/facts-with-sources.md`. Keep extraction separate from decision-making so the facts are fixed first.
