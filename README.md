# Groove Therapy — Smooth Jazz Band Website

Welcome to the Groove Therapy website repository. This is the official web presence for Groove Therapy, a smooth jazz band based in Sacramento, California.

## About Groove Therapy

Groove Therapy is a smooth jazz band offering live performances for events, corporate functions, and private parties. The band specializes in creating an elegant, relaxing atmosphere with sophisticated smooth jazz compositions.

**Contact:** q@groovetherapy.live

## Site Features

- **Homepage** — Introduction to the band and performance details
- **Booking Inquiries** — Contact form for event booking requests
- **Signup** — Mailing list signup to stay updated on performances
- **Business Plan** — Protected access to strategic planning documents (password-protected)

## Deployment

This site is deployed on **Google Cloud Platform (GCP)** using **Cloud Run**.

- **Live URL:** https://www.groovetherapy.live
- **Domain:** groovetherapy.live (www subdomain)
- **Service:** Cloud Run (auto-scaling serverless container)
- **Region:** us-central1
- **Deployment:** Automatic from GitHub (main branch)

## Management

This repository and deployment are **managed by Lenny** 🦦, the band's autonomous management assistant.

Lenny handles:
- Website updates and deployments
- Infrastructure management on GCP
- Email integration (contact forms, inquiries)
- Ongoing maintenance and improvements

For website changes or technical questions, coordinate with Kevin or contact Lenny directly.

## Tech Stack

- **Framework:** Flask (Python)
- **Frontend:** HTML/CSS/JavaScript
- **Backend:** Python Flask application
- **Container:** Docker (deployed to Cloud Run)
- **Email:** Gmail API integration
- **Markdown Support:** Business plan documents rendered as HTML

## Local Development

### Prerequisites

- Python 3.9+
- pip
- Docker (optional, for local container testing)

### Setup

```bash
# Clone the repository
git clone https://github.com/kquainta/groove-therapy-website.git
cd groove-therapy-website

# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional for local testing)
# export CONTACT_EMAIL="groovetherapysacto@gmail.com"
# export BPLAN_PASSWORD="Groovers"
# export GMAIL_REFRESH_TOKEN="..."  # See GCP credentials
# export GMAIL_CLIENT_ID="..."
# export GMAIL_CLIENT_SECRET="..."

# Run the app
python app.py
```

The app will start on `http://localhost:8080`

### Building & Running with Docker

```bash
# Build the Docker image
docker build -t groove-therapy-website .

# Run the container
docker run -p 8080:8080 groove-therapy-website
```

## API Endpoints

### `POST /api/contact`

Submit a booking inquiry.

**Request body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-1234",
  "eventType": "wedding",
  "eventDate": "2026-06-15",
  "message": "We'd love to book Groove Therapy for our event..."
}
```

**Response:**
```json
{
  "ok": true
}
```

Submissions are sent via Gmail to the configured contact email.

## Business Plan

Protected access to strategic documents at `/bplan`:

- Quick Start Guide
- Executive Summary
- Mailing List Strategy
- Social Media Strategy
- Venue Booking Strategy
- Corporate Gigs Strategy
- Sacramento Jazz Festival Plan

**Login:** Use the password configured in `BPLAN_PASSWORD` environment variable.

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `CONTACT_EMAIL` | Where booking inquiries are sent | groovetherapysacto@gmail.com |
| `BPLAN_PASSWORD` | Password for /bplan access | (set by Lenny) |
| `GMAIL_REFRESH_TOKEN` | Gmail API refresh token | (GCP credential) |
| `GMAIL_CLIENT_ID` | Gmail API client ID | (GCP credential) |
| `GMAIL_CLIENT_SECRET` | Gmail API client secret | (GCP credential) |
| `FLASK_SECRET_KEY` | Flask session secret (change in production) | (auto-generated for Cloud Run) |

## Deployment & CI/CD

This repository is automatically deployed to Cloud Run whenever changes are pushed to the `main` branch.

**Deployment process:**
1. Push code to GitHub (main branch)
2. Cloud Build automatically triggers
3. Docker image is built and pushed to Artifact Registry
4. Cloud Run service is updated with the new image
5. Changes are live at https://www.groovetherapy.live

For manual redeployment, use the `deploy.sh` script:

```bash
./deploy.sh
```

## Support & Questions

- **Website updates:** Contact Lenny 🦦
- **Band bookings:** Email q@groovetherapy.live
- **GitHub issues:** File an issue in this repository

---

**Maintained by:** Lenny 🦦  
**Last Updated:** 2026-04-24  
**Repository:** https://github.com/kquainta/groove-therapy-website
