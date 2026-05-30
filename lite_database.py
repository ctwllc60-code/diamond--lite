#!/usr/bin/env python3
# ENGINE_ID: lite_database.py | VERSION: 1.0
"""
Diamond Lite – Database Engine
SQLite database for user accounts, conversation history,
and per‑user memory. Creates tables automatically on first run.
"""

import sqlite3
from datetime import datetime

DB_PATH = "diamond_lite.db"


def get_connection():
    """Return a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize():
    """Create all required tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            display_name TEXT DEFAULT 'User',
            created_at TEXT DEFAULT (datetime('now')),
            tier TEXT DEFAULT 'free',
            messages_today INTEGER DEFAULT 0,
            last_reset_date TEXT DEFAULT (date('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            user_id INTEGER PRIMARY KEY,
            projects TEXT DEFAULT '',
            preferences TEXT DEFAULT '',
            milestones TEXT DEFAULT '',
            themes TEXT DEFAULT '',
            updated_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()


def create_user(email: str, password_hash: str, display_name: str = "User") -> int | None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (email, password_hash, display_name) VALUES (?, ?, ?)",
            (email, password_hash, display_name)
        )
        user_id = cursor.lastrowid
        cursor.execute("INSERT INTO memory (user_id) VALUES (?)", (user_id,))
        conn.commit()
        return user_id
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()


def get_user_by_email(email: str) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def get_user_by_id(user_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def save_message(user_id: int, role: str, content: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversations (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content)
    )
    conn.commit()
    conn.close()


def get_recent_conversation(user_id: int, limit: int = 20) -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content FROM conversations WHERE user_id = ? ORDER BY id DESC LIMIT ?",
        (user_id, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in reversed(rows)]


def update_memory(user_id: int, user_message: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO memory (user_id) VALUES (?)", (user_id,))
        conn.commit()
        cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()

    data = dict(row)
    themes = data.get("themes", "") or ""
    theme_list = themes.split(", ") if themes else []
    for word in ["build", "create", "design", "business", "system", "idea", "project"]:
        if word in user_message.lower() and word not in theme_list:
            theme_list.append(word)
    themes = ", ".join(theme_list[-10:])

    cursor.execute(
        "UPDATE memory SET themes = ?, updated_at = datetime('now') WHERE user_id = ?",
        (themes, user_id)
    )
    conn.commit()
    conn.close()


def get_memory_context(user_id: int) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return ""
    data = dict(row)
    parts = []
    if data.get("projects"):
        parts.append(f"Projects: {data['projects']}")
    if data.get("themes"):
        parts.append(f"Themes: {data['themes']}")
    if parts:
        return " | ".join(parts)
    return ""


def increment_message_count(user_id: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT messages_today, last_reset_date FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    if row["last_reset_date"] != today:
        cursor.execute(
            "UPDATE users SET messages_today = 1, last_reset_date = ? WHERE id = ?",
            (today, user_id)
        )
        conn.commit()
        conn.close()
        return 1
    else:
        cursor.execute(
            "UPDATE users SET messages_today = messages_today + 1 WHERE id = ?",
            (user_id,)
        )
        conn.commit()
        new_count = row["messages_today"] + 1
        conn.close()
        return new_count


initialize()
