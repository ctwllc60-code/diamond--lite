#!/usr/bin/env python3
# ENGINE_ID: lite_server.py | VERSION: 5.2 (Compact mobile chat, no jump scrolling)
"""
Diamond Lite – Cloud Server
Flask application with signup, login, chat, memory, tier enforcement,
health endpoints, and a compact mobile‑first chat interface.
Voice is only available for paid (Personal / Professional) users.
"""

from flask import Flask, request, jsonify
import hashlib
import uuid

from lite_database import (
    create_user,
    get_user_by_email,
    get_user_by_id,
    save_message,
    get_recent_conversation,
    increment_message_count,
)
from lite_llm import ask_llm
from lite_memory import update_user_memory, get_memory_summary
from lite_tiers import check_message_allowed, get_tier_info

app = Flask(__name__)

active_tokens = {}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def generate_token(user_id: int) -> str:
    token = str(uuid.uuid4())
    active_tokens[token] = user_id
    return token


def get_user_id_from_token(token: str) -> int | None:
    return active_tokens.get(token)


# ---- Health endpoint (for Watchtower) ----
@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Diamond Lite"})


# ---- Signup ----
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    display_name = data.get("display_name", "User")

    if not email or not password:
        return jsonify({"error": "Email and password required."}), 400

    password_hash = hash_password(password)
    user_id = create_user(email, password_hash, display_name)
    if user_id is None:
        return jsonify({"error": "Email already registered."}), 409

    token = generate_token(user_id)
    return jsonify({"token": token, "user_id": user_id, "display_name": display_name})


# ---- Login ----
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    user = get_user_by_email(email)
    if not user or user["password_hash"] != hash_password(password):
        return jsonify({"error": "Invalid email or password."}), 401

    token = generate_token(user["id"])
    return jsonify({"token": token, "display_name": user["display_name"]})


# ---- Chat ----
@app.route("/chat", methods=["POST"])
def chat():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = get_user_id_from_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized."}), 401

    data = request.get_json()
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message required."}), 400

    allowed, reason = check_message_allowed(user_id)
    if not allowed:
        return jsonify({"response": reason, "limit_reached": True})

    count = increment_message_count(user_id)
    save_message(user_id, "user", message)

    memory_context = get_memory_summary(user_id)
    history = get_recent_conversation(user_id, 10)
    history_text = "\n".join(f"{m['role']}: {m['content']}" for m in history)

    full_prompt = f"Conversation history:\n{history_text}\n\nUser: {message}"
    response = ask_llm(full_prompt, memory_context)

    save_message(user_id, "assistant", response)
    update_user_memory(user_id, message, response)

    user = get_user_by_id(user_id)
    tier = user.get("tier", "free")
    tier_info = get_tier_info(tier)
    messages_remaining = (
        max(0, tier_info["daily_limit"] - count)
        if tier_info["daily_limit"]
        else "unlimited"
    )
    voice_allowed = tier_info.get("voice_enabled", False)

    return jsonify({
        "response": response,
        "messages_remaining": messages_remaining,
        "voice_allowed": voice_allowed,
    })


# ---- Compact Chat Web Interface ----
@app.route("/")
def index():
    return CHAT_PAGE


CHAT_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>Diamond Lite</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; overflow: hidden; background: #0f0f0f; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
body { display: flex; justify-content: center; align-items: center; }
#app { width: 100%; height: 100%; max-width: 600px; display: flex; flex-direction: column; background: #0f0f0f; color: #eee; }
#auth { display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 24px; gap: 12px; height: 100%; }
#auth h2 { color: #0a7; font-size: 22px; margin-bottom: 12px; }
#auth input { width: 100%; padding: 10px 12px; border: none; border-radius: 8px; font-size: 14px; background: #1c1c1c; color: #eee; }
#auth button { width: 100%; padding: 10px; border: none; border-radius: 8px; font-size: 14px; font-weight: bold; cursor: pointer; }
#auth .primary { background: #0a7; color: #fff; }
#auth .secondary { background: #444; color: #fff; }
#auth-error { color: #e44; font-size: 12px; min-height: 16px; text-align: center; }
#chat-container { display: none; flex-direction: column; height: 100%; }
#header { padding: 8px 12px; background: #121212; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #222; }
#header h2 { font-size: 16px; color: #0a7; }
#logout-btn { background: transparent; border: 1px solid #444; color: #aaa; padding: 3px 10px; border-radius: 12px; font-size: 11px; cursor: pointer; }
#messages { flex: 1; overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 6px; -webkit-overflow-scrolling: touch; }
.msg { max-width: 85%; padding: 8px 10px; border-radius: 14px; line-height: 1.3; font-size: 13px; word-wrap: break-word; }
.msg.user { align-self: flex-end; background: #1a5fb4; color: #fff; border-bottom-right-radius: 3px; }
.msg.assistant { align-self: flex-start; background: #2a2a2a; color: #ddd; border-bottom-left-radius: 3px; }
#status { text-align: center; font-size: 10px; color: #666; padding: 4px; border-top: 1px solid #222; background: #0f0f0f; flex-shrink: 0; }
#input-area { display: flex; gap: 5px; padding: 6px 8px; background: #181818; border-top: 1px solid #333; flex-shrink: 0; }
#input-area input { flex: 1; padding: 8px 12px; border: none; border-radius: 18px; background: #252525; color: #eee; font-size: 13px; outline: none; }
#input-area button { padding: 8px 12px; border: none; border-radius: 18px; font-size: 13px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center; }
#mic-btn { background: #0a7; color: #fff; min-width: 40px; }
#send-btn { background: #444; color: #fff; min-width: 40px; }
</style>
</head>
<body>
<div id="app">
  <div id="auth">
    <h2>Diamond Lite</h2>
    <input id="email" type="email" placeholder="Email" autocomplete="email">
    <input id="password" type="password" placeholder="Password">
    <input id="display-name" type="text" placeholder="Your name (optional)">
    <button class="primary" onclick="signup()">Sign Up</button>
    <button class="secondary" onclick="login()">Log In</button>
    <p id="auth-error"></p>
  </div>
  <div id="chat-container">
    <div id="header">
      <h2>Diamond Lite</h2>
      <button id="logout-btn" onclick="logout()">Logout</button>
    </div>
    <div id="messages"></div>
    <div id="status">Free tier • 20 messages/day</div>
    <div id="input-area">
      <input id="msg-input" type="text" placeholder="Message..." autofocus>
      <button id="mic-btn" onclick="startVoice()">🎤</button>
      <button id="send-btn" onclick="send()">Send</button>
    </div>
  </div>
</div>
<script>
let token = localStorage.getItem('dl_token') || '';
let voiceAllowed = false;
const messages = document.getElementById('messages');
const input = document.getElementById('msg-input');
const statusEl = document.getElementById('status');

if (token) {
  document.getElementById('auth').style.display = 'none';
  document.getElementById('chat-container').style.display = 'flex';
}

async function api(url, body) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = 'Bearer ' + token;
  const res = await fetch(url, { method: 'POST', headers, body: JSON.stringify(body) });
  return res.json();
}

async function signup() {
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const display_name = document.getElementById('display-name').value.trim() || 'User';
  const data = await api('/signup', { email, password, display_name });
  if (data.error) return document.getElementById('auth-error').textContent = data.error;
  token = data.token;
  localStorage.setItem('dl_token', token);
  document.getElementById('auth').style.display = 'none';
  document.getElementById('chat-container').style.display = 'flex';
}

async function login() {
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const data = await api('/login', { email, password });
  if (data.error) return document.getElementById('auth-error').textContent = data.error;
  token = data.token;
  localStorage.setItem('dl_token', token);
  document.getElementById('auth').style.display = 'none';
  document.getElementById('chat-container').style.display = 'flex';
}

function logout() {
  localStorage.removeItem('dl_token');
  token = '';
  voiceAllowed = false;
  document.getElementById('auth').style.display = 'flex';
  document.getElementById('chat-container').style.display = 'none';
  messages.innerHTML = '';
}

function addMsg(role, text) {
  const div = document.createElement('div');
  div.className = 'msg ' + role;
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function speak(text) {
  if (!voiceAllowed) return;
  if ('speechSynthesis' in window) {
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    window.speechSynthesis.speak(u);
  }
}

async function send() {
  const msg = input.value.trim();
  if (!msg) return;
  addMsg('user', msg);
  input.value = '';
  const data = await api('/chat', { message: msg });
  if (data.response) {
    addMsg('assistant', data.response);
    voiceAllowed = data.voice_allowed || false;
    speak(data.response);
  }
  if (data.messages_remaining !== undefined) {
    statusEl.textContent = data.messages_remaining === 'unlimited' ? 'Unlimited messages' : `${data.messages_remaining} messages left today`;
  }
}

function startVoice() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) return alert('Voice not supported. Use Chrome.');
  const rec = new SR();
  rec.lang = 'en-US';
  rec.onresult = e => { input.value = e.results[0][0].transcript; send(); };
  rec.start();
}

input.addEventListener('keypress', e => { if (e.key === 'Enter') send(); });
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
