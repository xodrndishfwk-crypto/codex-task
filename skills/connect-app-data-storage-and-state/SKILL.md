---
name: connect-app-data-storage-and-state
description: Connect app screens to the required data source, storage, and state changes while preserving data integrity and making loading, empty, error, and saved states visible.
---

# Connect App Data, Storage, and State

Trace each required user action from input to stored or calculated result and back to the interface.

- Identify the source of truth for each value and who is allowed to change it.
- Define initial, loading, empty, valid, invalid, saving, saved, and failure states where applicable.
- Validate input at the appropriate boundary and show a useful local error without discarding valid user work.
- Keep state updates deterministic and avoid duplicate records or double submissions.
- Preserve required data across navigation or restart only when the task requires persistence.
- Use the provided local data mechanism before introducing a new database, service, or dependency.
- Do not claim persistence, synchronization, or recovery that was not tested.

Verify at least one complete create or update path and one failure or invalid-input path. Record what persists, when it persists, and how it was checked.
