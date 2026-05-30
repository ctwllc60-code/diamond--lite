#!/usr/bin/env python3
# ENGINE_ID: lite_database.py | VERSION: 2.0 (Search + export)
"""
Diamond Lite – Database Engine
SQLite database for user accounts, conversation history,
per‑user memory, message search, and export support.
"""

import sqlite3
import json
from datetime import datetime

DB_PATH = "diamond_lite.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize():
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


def search_conversations(user_id: int, query: str, limit: int = 50) -> list:
    """Search the user's conversation history for messages containing the query."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content, timestamp FROM conversations WHERE user_id = ? AND content LIKE ? ORDER BY id DESC LIMIT ?",
        (user_id, f"%{query}%", limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in reversed(rows)]


def export_conversations(user_id: int) -> str:
    """Export all conversations for a user as a formatted text string."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content, timestamp FROM conversations WHERE user_id = ? ORDER BY id ASC",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No conversations yet."

    lines = ["Diamond Lite – Conversation Export\n"]
    for r in rows:
        role = "You" if r["role"] == "user" else "Diamond Lite"
        lines.append(f"[{r['timestamp']}] {role}: {r['content']}\n")

    return "\n".join(lines)


def get_memory_summary(user_id: int) -> dict:
    """Return the user's memory dashboard summary."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return {"projects": [], "themes": [], "preferences": [], "milestones": []}
    data = dict(row)
    return {
        "projects": _parse_json(data.get("projects", "[]"), []),
        "themes": _parse_json(data.get("themes", "[]"), []),
        "preferences": _parse_json(data.get("preferences", "[]"), []),
        "milestones": _parse_json(data.get("milestones", "[]"), []),
        "updated_at": data.get("updated_at", ""),
    }


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
    themes = _parse_json(data.get("themes", "[]"), [])
    for word in ["build", "create", "design", "business", "system", "idea", "project"]:
        if word in user_message.lower() and word not in themes:
            themes.append(word)

    cursor.execute(
        "UPDATE memory SET themes = ?, updated_at = datetime('now') WHERE user_id = ?",
        (_to_json(themes[-10:]), user_id)
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
    projects = _parse_json(data.get("projects", "[]"), [])
    if projects:
        parts.append(f"Projects: {', '.join(projects)}")
    themes = _parse_json(data.get("themes", "[]"), [])
    if themes:
        parts.append(f"Interests: {', '.join(themes)}")
    return " | ".join(parts) if parts else ""


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


def _parse_json(raw, default):
    if not raw:
        return default
    try:
        return json.loads(raw)
    except Exception:
        return default


def _to_json(lst):
    return json.dumps(lst)


initialize()
