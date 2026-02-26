"""Groove Therapy Jazz — website backend."""

from __future__ import annotations

import os
import smtplib
from email.mime.text import MIMEText

from flask import Flask, jsonify, render_template, request

# ── Config ──────────────────────────────────────────────────────────────────
# Set these environment variables for the contact form to send email.
# If not set, form submissions are logged to the console instead.
SMTP_HOST = os.environ.get("SMTP_HOST", "")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "info@groovetherapy.live")

app = Flask(__name__)


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
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Event Type: {event_type}\n"
        f"Event Date: {event_date}\n"
        f"---\n{message}"
    )

    if SMTP_HOST and SMTP_USER:
        try:
            msg = MIMEText(body)
            msg["Subject"] = f"Groove Therapy Inquiry from {name}"
            msg["From"] = SMTP_USER
            msg["To"] = CONTACT_EMAIL
            msg["Reply-To"] = email
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as srv:
                srv.starttls()
                srv.login(SMTP_USER, SMTP_PASS)
                srv.send_message(msg)
        except Exception as exc:
            print(f"[EMAIL ERROR] {exc}")
            return jsonify({"error": "Failed to send. Please email us directly."}), 500
    else:
        print(f"\n{'='*50}")
        print("NEW CONTACT FORM SUBMISSION")
        print(f"{'='*50}")
        print(body)
        print(f"{'='*50}\n")

    return jsonify({"ok": True})


if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://localhost:8080")
    app.run(debug=False, port=8080)
