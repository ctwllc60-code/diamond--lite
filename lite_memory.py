#!/usr/bin/env python3
# ENGINE_ID: lite_memory.py | VERSION: 1.0
"""
Diamond Lite – Per‑User Evolving Memory
Extracts and stores user preferences, projects, recurring themes,
and personal details from conversations. Grows with every interaction.
"""

import json
from datetime import datetime
from lite_database import get_connection


def update_user_memory(user_id: int, user_message: str, assistant_response: str):
    """
    Analyze the latest exchange and update the user's memory record.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Ensure memory row exists
    cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO memory (user_id) VALUES (?)", (user_id,))
        conn.commit()
        cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()

    data = dict(row)

    # --- Extract projects ---
    projects = _parse_list(data.get("projects", ""))
    project_keywords = ["build", "create", "design", "start", "launch", "develop"]
    for word in project_keywords:
        if word in user_message.lower():
            projects.append(user_message[:200])
            break

    # --- Extract preferences ---
    preferences = _parse_list(data.get("preferences", ""))
    if "i prefer" in user_message.lower() or "i like" in user_message.lower():
        preferences.append(user_message[:200])

    # --- Extract themes ---
    themes = _parse_list(data.get("themes", ""))
    theme_words = [
        "business", "technology", "creative", "health", "education",
        "finance", "music", "writing", "coding", "design", "startup",
        "family", "career", "learning", "travel"
    ]
    for word in theme_words:
        if word in user_message.lower() and word not in themes:
            themes.append(word)

    # --- Extract milestones ---
    milestones = _parse_list(data.get("milestones", ""))
    milestone_signals = ["done", "complete", "finished", "achieved", "launched", "got"]
    if any(w in user_message.lower() for w in milestone_signals):
        milestones.append(f"{datetime.now().strftime('%Y-%m-%d')}: {user_message[:200]}")

    # --- Update database ---
    cursor.execute("""
        UPDATE memory
        SET projects = ?, preferences = ?, themes = ?, milestones = ?, updated_at = datetime('now')
        WHERE user_id = ?
    """, (
        _to_json(projects[-10:]),
        _to_json(preferences[-10:]),
        _to_json(themes[-15:]),
        _to_json(milestones[-20:]),
        user_id
    ))
    conn.commit()
    conn.close()


def get_memory_summary(user_id: int) -> str:
    """
    Build a concise, personal summary that can be injected into the LLM prompt.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memory WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return ""

    data = dict(row)
    parts = []

    projects = _parse_list(data.get("projects", ""))
    if projects:
        parts.append(f"Recent projects: {'; '.join(projects[-3:])}")

    themes = _parse_list(data.get("themes", ""))
    if themes:
        parts.append(f"Interests: {', '.join(themes[-8:])}")

    milestones = _parse_list(data.get("milestones", ""))
    if milestones:
        parts.append(f"Recent achievements: {milestones[-1][:100]}")

    if parts:
        return " | ".join(parts)
    return ""


# ---- Helpers ----

def _parse_list(raw: str) -> list:
    """Safely parse a JSON string into a list."""
    if not raw:
        return []
    try:
        return json.loads(raw)
    except Exception:
        return []


def _to_json(lst: list) -> str:
    """Convert a list to a JSON string."""
    return json.dumps(lst)
