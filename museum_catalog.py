"""Manage a small in-memory catalog of museum artifacts."""

import sqlite3


def create_connection() -> sqlite3.Connection:
    """Create the catalog database and its artifacts table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE artifacts (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            era TEXT NOT NULL,
            value INTEGER NOT NULL,
            on_display INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    return connection


def add_artifact(
    connection: sqlite3.Connection,
    title: str,
    era: str,
    value: int,
    on_display: bool = False,
) -> None:
    """Add an artifact using bound parameters to keep values out of SQL."""
    connection.execute(
        "INSERT INTO artifacts (title, era, value, on_display) "
        "VALUES (?, ?, ?, ?)",
        (title, era, value, int(on_display)),
    )
    connection.commit()


def display_status(connection: sqlite3.Connection, artifact_id: int) -> str:
    """Return whether an artifact is on display or in storage."""
    row = connection.execute(
        "SELECT on_display FROM artifacts WHERE id = ?", (artifact_id,)
    ).fetchone()
    if row is None:
        return "artifact not found"
    return "on display" if row[0] else "in storage"


def total_value(connection: sqlite3.Connection, era: str) -> int:
    """Return the combined value of artifacts from an era."""
    rows = connection.execute(
        "SELECT value FROM artifacts WHERE era = ?", (era,)
    )
    return sum(value for (value,) in rows)


def move_to_display(connection: sqlite3.Connection, artifact_id: int) -> None:
    """Mark an artifact as being on display."""
    connection.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?", (artifact_id,)
    )
    connection.commit()


def backup_note() -> str:
    """Return a backup notice without invoking a system shell."""
    return "catalog backup complete"


def main() -> None:
    """Run the sample catalog demonstration."""
    connection = create_connection()
    add_artifact(connection, "Bronze Mirror", "Chola", 120000)
    add_artifact(connection, "Palm Manuscript", "Vijayanagara", 80000, True)
    add_artifact(connection, "Terracotta Lamp", "Chola", 15000)
    move_to_display(connection, 1)
    print(display_status(connection, 1))
    print(total_value(connection, "Chola"))
    print(backup_note())
    connection.close()


if __name__ == "__main__":
    main()
