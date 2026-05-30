#!/usr/bin/env python3
# ENGINE_ID: lite_llm.py | VERSION: 1.0
"""
Diamond Lite – LLM Bridge
Connects to OpenRouter free API using the same key as Diamond.
"""

import os
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.2-3b-instruct"

# Use the same key file as Diamond
KEY_FILE = os.path.join(os.path.dirname(__file__), "..", "diamond", ".openrouter_key")


def _get_api_key() -> str:
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            key = f.read().strip()
            if key:
                return key
    return os.getenv("OPENROUTER_API_KEY", "")


def ask_llm(user_message: str, memory_context: str = "") -> str:
    """Send a message to the LLM and return the response."""
    api_key = _get_api_key()
    if not api_key:
        return "I'm having trouble reaching my mind right now. Please try again later."

    system_prompt = (
        "You are Diamond Lite, a personal AI companion. "
        "You are warm, thoughtful, and evolve with each user through conversation. "
        "Respond in a natural, conversational voice. Never mention that you are an AI model. "
        "Keep your responses helpful, concise, and personal."
    )

    messages = [{"role": "system", "content": system_prompt}]
    if memory_context:
        messages.append({"role": "system", "content": f"User context: {memory_context}"})
    messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={"model": MODEL, "messages": messages, "temperature": 0.7, "max_tokens": 250},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"I hit a snag: {e}"
