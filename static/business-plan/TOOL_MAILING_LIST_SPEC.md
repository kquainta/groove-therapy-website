# Mailing List Tool Specification
**Technical Design & Implementation Plan**

---

## Overview

Build a lightweight mailing list system that allows:
1. Website signup form (with validation & spam prevention)
2. Automated welcome sequence
3. Monthly newsletter (templated, easy to create)
4. Analytics (open rates, clicks, subscriber growth)
5. Easy subscriber management (add/remove/segment)

---

## Architecture Decision

### Option A: Mailchimp (Recommended for MVP)

**Pros:**
- Free tier up to 500 subscribers
- Built-in email templates
- API integration (if we want custom website form)
- Good analytics
- Reliable, industry standard

**Cons:**
- Limited customization
- Not ideal long-term as you scale
- Limited segmentation on free tier

**Cost:** Free until 500 subscribers, then $20-100+/month

### Option B: ConvertKit

**Pros:**
- Creator-focused (great for artists)
- Better segmentation
- Landing pages + email builder
- Affiliate program (future revenue)

**Cons:**
- $25/month minimum
- Steeper learning curve

**Cost:** $25-300+/month depending on features

### Option C: Custom-Built (Long-term)

**Pros:**
- Full control
- Can integrate directly with website
- Owned data
- Scalable

**Cons:**
- Development time (2-4 weeks)
- Requires maintenance
- Need email service provider (AWS SES, SendGrid)

**Cost:** $200-500 development + $50-100/month hosting

---

## Recommendation: Mailchimp MVP + Migration Path

**Phase 1 (Now):** Use **Mailchimp free tier**
- Get list growing quickly
- Low friction to start
- Validate demand

**Phase 2 (500+ subscribers):** Evaluate upgrade
- Migrate to ConvertKit OR
- Build custom solution if budget allows

---

## Implementation Plan (Mailchimp)

### Step 1: Set Up Mailchimp Account

1. Create account at mailchimp.com
2. Create new audience "Groove Therapy"
3. Set up default signup forms

### Step 2: Create Website Signup Form

**Option A: Simple Embedded Form**
- Use Mailchimp's built-in form embed
- Add to website homepage
- Minimal customization needed

**Option B: Custom Website Form (Better UX)**
- Create custom HTML form on website
- Uses Mailchimp API to add subscribers
- More professional appearance

**Form Fields:**
```
- Email (required, validated)
- First Name (optional)
- Zip Code (optional, for targeting local gigs)
```

**Validation:**
```javascript
// Check email format
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Check if email already exists
// Check if blacklisted/spam email provider
```

**Anti-Spam:**
- Rate limit: Max 5 signups per IP per hour
- Check against known spam providers
- Double opt-in (require email confirmation)

### Step 3: Create Welcome Email Sequence

**Email 1: Welcome (Immediate)**
```
Subject: Welcome to Groove Therapy!

Hi {{FNAME}},

Thanks for signing up! You're now part of the Groove Therapy community.

Here's what to expect:
📬 Gig announcements (never spam — just dates & venues)
🎵 Behind-the-scenes stories from the band
🎷 Jazz tips & music spotlights
💌 Monthly newsletter with upcoming events

In the meantime, follow us on social:
- Instagram: @groovetherapysac
- Facebook: Groove Therapy

See you at a show soon!

Best,
Kevin & The Groove Therapy Band
```

**Email 2: Band Story (Day 3)**
```
Subject: Meet Groove Therapy 🎷

Hi {{FNAME}},

A lot of you are wondering: who are these guys?

Groove Therapy is Sacramento's smooth jazz band, formed in [YEAR] with a mission to bring quality live music to our community. We play everything from jazz standards to original compositions, all with a vibe that's sophisticated but never stuffy.

[2-3 paragraph origin story]

Watch us live: [Video Link]

Next gig: [Date] @ [Venue]

See you soon,
Kevin
```

**Email 3: Exclusive Content (Day 7)**
```
Subject: Exclusive: Behind-the-Scenes with Groove Therapy 🎬

Hi {{FNAME}},

As a subscriber, you get exclusive access to content we don't share anywhere else.

[Attach exclusive video or audio clip]

This week we recorded an acoustic version of [Song] — enjoy!

Next gig: [Date] @ [Venue]

Best,
Kevin
```

**Setup in Mailchimp:**
1. Automations > Welcome Series
2. Trigger: When someone joins audience
3. Add 3 emails (immediately, day 3, day 7)
4. Test sequence before going live

### Step 4: Create Monthly Newsletter Template

**Template Structure:**

```
SUBJECT: [Month] Groove Therapy News: Upcoming Gigs & Behind-the-Scenes

---

Hi {{FNAME}},

🎵 **This Month's Performances**

[List of gigs]
- [Date] @ [Venue] [Link to register/more info]
- [Date] @ [Venue] [Link to register/more info]

[CTA: "Get Tickets" button]

---

🎬 **What We're Up To**

[Short behind-the-scenes story or photo]

---

📚 **Jazz Spotlight**

[Educational content: history fact, musician spotlight, music tip]

---

💌 **From the Band**

[Personal note from Kevin or band]

---

🎸 **Bring a Friend**

Know someone who'd love Groove Therapy? Send them our way!

[Refer a Friend Link]

---

See you soon,
Kevin & Groove Therapy

[Social Links]
[Website Link]
```

**Process:**
1. Lenny prepares newsletter content
2. Kevin reviews + approves
3. Lenny loads into Mailchimp template
4. Schedule for 1st of month, 10am
5. Send!

### Step 5: Analytics & Tracking

**Monitor Monthly:**
- Open Rate (goal: >30%)
- Click-Through Rate (goal: >5%)
- Unsubscribe Rate (goal: <0.5%)
- Bounce Rate (keep <2%)
- Subscriber Growth (track additions/removals)

**In Mailchimp:**
- Automations > All Campaigns > View Reports
- Look for trends (what content performs best?)
- Adjust next month based on data

---

## Website Integration

### Simple Path (MVP)

1. Create basic website homepage
2. Embed Mailchimp signup form
3. Add link to form in bio/social media

### Better Path (Month 2+)

Create dedicated landing page with:
```
URL: groovetherapy.live/subscribe (or custom domain)

Page Content:
- Band photo/video
- "Get Gig Announcements First" headline
- Brief description: "Join 500+ fans who get tour dates and behind-the-scenes content"
- Signup form (custom HTML)
- Social media links
- Recent testimonials/reviews
```

**Incentives to Sign Up:**
- "Get gigs before anyone else"
- "Exclusive behind-the-scenes content"
- "Monthly jazz tips delivered to your inbox"

---

## Migration Path (If Growing Beyond 500)

### When to Upgrade

- Hit 400+ active subscribers
- Want advanced segmentation
- Need better automation
- Adding other content (blog, downloads)

### Options at Scale

1. **ConvertKit** ($25-100/month)
   - Better segmentation, landing pages
   - Creator-friendly interface
   - Can offer exclusive content/Patreon-style

2. **Custom Solution** (Build your own)
   ```
   Technology Stack:
   - Frontend: Simple React form
   - Backend: Node.js + Express
   - Email: SendGrid or AWS SES API
   - Database: MongoDB or PostgreSQL
   - Hosting: Vercel, Heroku, or AWS
   
   Timeline: 2-4 weeks development
   Cost: $200-500 dev + $50-150/month ops
   ```

3. **Substack**
   - Free newsletter hosting
   - Built-in subscriber management
   - Can monetize later
   - Less customizable but simpler

---

## Quick Implementation Timeline

| Week | Action |
|------|--------|
| **Week 1** | Create Mailchimp account, set up audience |
| **Week 2** | Create signup form, add to website |
| **Week 3** | Set up welcome email sequence |
| **Week 4** | Create first monthly newsletter, send |
| **Ongoing** | Review analytics monthly, optimize content |

---

## Cost Summary

| Item | Cost |
|------|------|
| Mailchimp (Months 1-6) | Free |
| Website hosting (if needed) | $10-20/mo |
| Custom domain (optional) | $10-15/year |
| **TOTAL (Year 1)** | **$60-90** |
| **Upgrade to ConvertKit (if needed)** | +$25-100/month |

---

## Success Metrics

- [ ] 100 subscribers by Month 3
- [ ] 250 subscribers by Month 6
- [ ] 500+ subscribers by Month 12
- [ ] 30%+ open rate on newsletters
- [ ] <0.5% monthly unsubscribe rate
- [ ] 5%+ click-through rate on CTAs

---

## Owner: Lenny
**Status:** Ready to implement  
**Next Step:** Create Mailchimp account (this week)

---

## Resources

- Mailchimp docs: mailchimp.com/help
- Email best practices: [Insert guide link]
- Signup form templates: [Insert resources]
