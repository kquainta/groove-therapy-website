"""Groove Therapy Jazz — website backend."""

from __future__ import annotations

import base64
import json
import os
from email.mime.text import MIMEText

from flask import Flask, jsonify, render_template, request
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ── Config ──────────────────────────────────────────────────────────────────
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "groovetherapysacto@gmail.com")

# Gmail OAuth credentials (injected via env vars at deploy time)
GMAIL_REFRESH_TOKEN = os.environ.get("GMAIL_REFRESH_TOKEN", "")
GMAIL_CLIENT_ID = os.environ.get("GMAIL_CLIENT_ID", "")
GMAIL_CLIENT_SECRET = os.environ.get("GMAIL_CLIENT_SECRET", "")

app = Flask(__name__)


def get_gmail_service():
    creds = Credentials(
        token=None,
        refresh_token=GMAIL_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=GMAIL_CLIENT_ID,
        client_secret=GMAIL_CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/gmail.modify"]
    )
    creds.refresh(Request())
    return build("gmail", "v1", credentials=creds)


# ── Routes ──────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.json or {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    event_type = data.get("eventType", "").strip()
    event_date = data.get("eventDate", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"error": "Name, email, and message are required."}), 400

    body = (
        f"New booking inquiry from the Groove Therapy website!\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Event Type: {event_type}\n"
        f"Event Date: {event_date}\n"
        f"{'─'*40}\n"
        f"{message}"
    )

    if GMAIL_REFRESH_TOKEN and GMAIL_CLIENT_ID:
        try:
            gmail = get_gmail_service()
            msg = MIMEText(body)
            msg["Subject"] = f"🎷 Groove Therapy Inquiry from {name}"
            msg["From"] = "groovetherapysacto@gmail.com"
            msg["To"] = CONTACT_EMAIL
            msg["Reply-To"] = email
            raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
            gmail.users().messages().send(userId="me", body={"raw": raw}).execute()
            print(f"[CONTACT] Email sent for inquiry from {name} ({email})")
        except Exception as exc:
            import traceback
            print(f"[EMAIL ERROR] {exc}")
            print(traceback.format_exc())
            return jsonify({"error": "Failed to send. Please email us directly."}), 500
    else:
        print(f"\n{'='*50}")
        print("NEW CONTACT FORM SUBMISSION (no Gmail creds configured)")
        print(f"{'='*50}")
        print(body)
        print(f"{'='*50}\n")

    return jsonify({"ok": True})


if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://localhost:8080")
    app.run(debug=False, port=8080)
