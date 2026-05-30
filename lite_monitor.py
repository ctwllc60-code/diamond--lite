#!/usr/bin/env python3
# ENGINE_ID: lite_monitor.py | VERSION: 2.0 (System‑health only)
"""
Diamond Lite – Monitor Bridge
Provides a system‑health check for Watchtower:
server responsiveness, database connectivity, and basic integrity.
No user conversation data is exposed.
"""

import time
import sqlite3
from lite_database import DB_PATH, get_connection


def check_database() -> bool:
    """Verify the database is accessible and not corrupted."""
    try:
        conn = get_connection()
        conn.execute("SELECT 1 FROM users LIMIT 1")
        conn.close()
        return True
    except Exception:
        return False


def check_response_time() -> float:
    """Measure how fast the database responds (in milliseconds)."""
    try:
        conn = get_connection()
        start = time.time()
        conn.execute("SELECT 1")
        conn.close()
        return round((time.time() - start) * 1000, 2)
    except Exception:
        return -1.0


def get_system_health() -> dict:
    """
    Return a minimal system‑health report suitable for Watchtower.
    Contains only infrastructure metrics, no user activity details.
    """
    db_ok = check_database()
    response_ms = check_response_time() if db_ok else -1.0

    return {
        "service": "Diamond Lite",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "database": "ok" if db_ok else "unreachable",
        "response_time_ms": response_ms,
        "healthy": db_ok and response_ms > 0,
    }


def get_health_status_line() -> str:
    """Return a single‑line status suitable for Watchtower alerts."""
    health = get_system_health()
    if health["healthy"]:
        return f"Diamond Lite is healthy (db response {health['response_time_ms']}ms)."
    else:
        return f"Diamond Lite may be down: database {health['database']}."
