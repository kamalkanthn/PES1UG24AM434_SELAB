# Static analysis findings

Findings below are from the original `museum_catalog_before.py`. Severity is based on practical impact to this small demonstration.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command execution | Security (high) | 37 | `subprocess.call(..., shell=True)` passes a command through the system shell. | Removed the subprocess call; `backup_note` now returns the notice as a string. |
| SQL injection risk | Security (high) | 12 | Artifact values are concatenated into an SQL statement, allowing crafted text to alter the query. | Replaced concatenation with SQLite `?` placeholders and bound values. |
| Hard-coded credential | Security (medium) | 9 | A curator password is embedded in source and is unused. | Removed the unused credential instead of retaining a secret in code. |
| Unused import | Quality (low) | 2 | `datetime` is imported but never used. | Removed the unused import. |
| Unused function parameter | Quality (low) | 19 | `curator` is accepted but never used. | Removed the parameter; the function now accepts only the artifact ID and connection. |
| Missing-row crash | Reliability (medium) | 18 | `fetchone()` may return `None`; indexing it crashes for an unknown artifact ID. | Added a missing-record check and a clear `artifact not found` result. |
| Naming and formatting violations | Style (low) | 12-50 | Function names use camelCase, spacing is inconsistent, and blank lines are excessive. | Renamed functions to snake_case and formatted the module consistently. |

The original findings overlap across tools: Bandit flags the shell use and SQL construction, Pylint flags code-quality problems, and Flake8 flags style violations.
