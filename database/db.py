import sqlite3
from pathlib import Path

# Create data directory if it doesn't exist
Path("data").mkdir(exist_ok=True)

DB_PATH = "data/studymate.db"


def get_connection():
    """Return a SQLite connection."""
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def create_table():
    """Create the tasks table."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        task_name TEXT NOT NULL,
        deadline TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        estimated_hours REAL NOT NULL,
        priority TEXT,
        status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()


def add_task(subject, task_name, deadline, difficulty, estimated_hours, priority):
    """Insert a new task."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks(
        subject,
        task_name,
        deadline,
        difficulty,
        estimated_hours,
        priority
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        subject,
        task_name,
        deadline,
        difficulty,
        estimated_hours,
        priority
    ))

    conn.commit()
    conn.close()


def get_tasks():
    """Return all tasks."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM tasks
    ORDER BY deadline
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_task_by_id(task_id):
    """Return a single task."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM tasks
    WHERE id=?
    """, (task_id,))

    task = cursor.fetchone()

    conn.close()

    return task


def update_status(task_id, status):
    """Update task status."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET status=?
    WHERE id=?
    """, (status, task_id))

    conn.commit()
    conn.close()


def delete_task(task_id):
    """Delete a task."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM tasks
    WHERE id=?
    """, (task_id,))

    conn.commit()
    conn.close()


def update_priority(task_id, priority):
    """Update task priority."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET priority=?
    WHERE id=?
    """, (priority, task_id))

    conn.commit()
    conn.close()