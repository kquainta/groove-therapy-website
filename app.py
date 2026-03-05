"""Groove Therapy Jazz — website backend."""

from __future__ import annotations

import base64
import json
import os
from email.mime.text import MIMEText
from pathlib import Path

from flask import Flask, jsonify, render_template, request, abort, session, redirect, url_for
import markdown
from functools import wraps
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
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "groove-therapy-dev-key-change-in-production")


# ── Authentication ─────────────────────────────────────────────────────────
BPLAN_PASSWORD = os.environ.get("BPLAN_PASSWORD", "Groovers")

def require_bplan_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("bplan_authenticated"):
            return redirect(url_for("bplan_login"))
        return f(*args, **kwargs)
    return decorated_function


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


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/bplan/login", methods=["GET", "POST"])
def bplan_login():
    """Login page for business plan."""
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == BPLAN_PASSWORD:
            session["bplan_authenticated"] = True
            return redirect(url_for("business_plan"))
        else:
            return render_template("bplan_login.html", error="Incorrect password")
    return render_template("bplan_login.html")


@app.route("/bplan/logout")
def bplan_logout():
    """Logout from business plan."""
    session.pop("bplan_authenticated", None)
    return redirect(url_for("bplan_login"))


@app.route("/bplan")
@require_bplan_auth
def business_plan():
    return render_template("business_plan.html")


@app.route("/bplan/<slug>")
@require_bplan_auth
def business_plan_doc(slug):
    """Render a business plan markdown document as HTML."""
    # Sanitize slug to prevent directory traversal
    if ".." in slug or "/" in slug:
        abort(400)
    
    # Map slug to filename
    slug_to_file = {
        "quick-start": "00_QUICK_START.md",
        "executive-summary": "01_EXECUTIVE_SUMMARY.md",
        "mailing-list": "02_MAILING_LIST_STRATEGY.md",
        "social-media": "03_SOCIAL_MEDIA_STRATEGY.md",
        "venue-booking": "04_VENUE_BOOKING_STRATEGY.md",
        "corporate-gigs": "05_CORPORATE_GIG_STRATEGY.md",
        "festival": "06_SACRAMENTO_JAZZ_FESTIVAL_PLAN.md",
        "mailing-list-tool": "TOOL_MAILING_LIST_SPEC.md",
        "social-media-tool": "TOOL_SOCIAL_MEDIA_SPEC.md",
    }
    
    if slug not in slug_to_file:
        abort(404)
    
    filename = slug_to_file[slug]
    filepath = Path(__file__).parent / "static" / "business-plan" / filename
    
    if not filepath.exists():
        abort(404)
    
    # Read and convert markdown to HTML
    with open(filepath, "r") as f:
        content = f.read()
    
    html_content = markdown.markdown(content, extensions=["tables", "fenced_code"])
    
    return render_template("business_plan_doc.html", content=html_content, title=filename)


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
