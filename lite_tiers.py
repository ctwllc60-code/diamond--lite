#!/usr/bin/env python3
# ENGINE_ID: lite_tiers.py | VERSION: 1.0
"""
Diamond Lite – Tier Management
Defines subscription tiers, daily message limits, and tier upgrade/downgrade logic.
Ready for real payment integration (Stripe, Google Play Billing) later.
"""

from lite_database import get_connection

# ---- Tier definitions ----
TIERS = {
    "free": {
        "name": "Free",
        "daily_limit": 20,
        "voice_enabled": False,
        "memory_enabled": True,
        "ads_enabled": True,
        "price_monthly": 0,
    },
    "personal": {
        "name": "Personal",
        "daily_limit": None,  # unlimited
        "voice_enabled": True,
        "memory_enabled": True,
        "ads_enabled": False,
        "price_monthly": 14.99,
    },
    "professional": {
        "name": "Professional",
        "daily_limit": None,
        "voice_enabled": True,
        "memory_enabled": True,
        "ads_enabled": False,
        "price_monthly": 29.99,
    },
}


def get_tier_info(tier: str) -> dict:
    """Return the full tier definition."""
    return TIERS.get(tier, TIERS["free"])


def get_user_tier(user_id: int) -> str:
    """Return the user's current tier string."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tier FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row["tier"] if row else "free"


def set_user_tier(user_id: int, tier: str):
    """Upgrade or downgrade a user's tier."""
    if tier not in TIERS:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET tier = ? WHERE id = ?", (tier, user_id))
    conn.commit()
    conn.close()


def check_message_allowed(user_id: int) -> tuple[bool, str]:
    """
    Check if the user is allowed to send another message.
    Returns (allowed: bool, reason: str).
    """
    user_tier = get_user_tier(user_id)
    tier_info = get_tier_info(user_tier)

    if tier_info["daily_limit"] is None:
        return True, ""

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT messages_today, last_reset_date FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return True, ""

    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    if row["last_reset_date"] != today:
        return True, ""

    if row["messages_today"] >= tier_info["daily_limit"]:
        return False, f"Daily limit of {tier_info['daily_limit']} messages reached. Upgrade to continue."

    return True, ""


def get_tiers_for_display() -> list:
    """Return a simplified list of tiers for the frontend."""
    return [
        {
            "id": tid,
            "name": t["name"],
            "price": t["price_monthly"],
            "daily_limit": t["daily_limit"] if t["daily_limit"] else "Unlimited",
            "voice": t["voice_enabled"],
            "ads": t["ads_enabled"],
        }
        for tid, t in TIERS.items()
    ]
