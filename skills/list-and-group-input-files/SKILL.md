---
name: list-and-group-input-files
description: Inventory all provided input files, group them by person, equipment, vendor, or other subject, and identify missing or duplicate files.
---

# List and Group Input Files

Confirm the full input count and structure before analysis.

- Create a table with file path, type, size, subject ID, and document type.
- Do not rely only on filenames; compare identifiers inside documents when possible.
- Compare expected and actual document counts for each subject.
- Mark possible duplicates, empty files, and unreadable files separately.
- Do not modify source files. Record relative paths in the output.

Record the inventory in `templates/input-file-list.md`. If an identifier is unclear, do not merge records by guess; use the template's needs-review label.
