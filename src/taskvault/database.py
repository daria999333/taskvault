import sqlite3
from pathlib import Path
from typing import Any

DB_NAME = "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn


def init_db() -> None:
    """Initialize the database and create the tasks table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority TEXT DEFAULT 'Medium',
                status TEXT DEFAULT 'Pending'
            )
        """
        )
        conn.commit()


def add_task(title: str, priority: str) -> int:
    """Add a new task to the database and return its ID."""
    init_db()
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, priority) VALUES (?, ?)",
            (title, priority),
        )
        conn.commit()
        return cursor.lastrowid


def get_all_tasks() -> list[dict[str, Any]]:
    """Retrieve all tasks from the database."""
    init_db()
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def complete_task(task_id: int) -> bool:
    """Mark a task as completed by its ID."""
    init_db()
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,)
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_task(task_id: int) -> bool:
    """Delete a task by its ID."""
    init_db()
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0