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

### Option A: Brevo (Recommended) ⭐

**Pros:**
- ✅ **Unlimited emails** on free tier (no subscriber caps)
- ✅ **Automation workflows** on free tier (welcome sequences, triggers)
- ✅ **Professional templates** and builder
- ✅ **SMS integration** (future capability)
- ✅ **Better segmentation** for local vs. remote fans
- ✅ **SMTP access** for website integration
- ✅ **Stays free longer** than competitors

**Cons:**
- UI is slightly more complex than Mailchimp
- Smaller ecosystem (but growing fast)

**Cost:** FREE up to 20,000 emails/month, then affordable scaling ($20-100+/month for premium)

### Option B: Mailchimp (If you prefer simpler UI)

**Pros:**
- Simpler interface
- More templates
- Larger community

**Cons:**
- Free tier caps at 500 subscribers
- Limited automation on free tier
- Not ideal long-term

**Cost:** Free until 500 subscribers, then $20-100+/month

### Option C: ConvertKit

**Pros:**
- Creator-focused (great for artists)
- Better segmentation
- Landing pages + email builder

**Cons:**
- $25/month minimum
- Steeper learning curve

**Cost:** $25-300+/month depending on features

---

## Recommendation: Brevo + Long-term Scalability

**Why Brevo:** Unlimited emails on free tier, better automation, professional features as you scale.

**Phase 1 (Now):** Use **Brevo free tier**
- Unlimited emails (no subscriber caps like Mailchimp)
- Built-in automation workflows
- SMS integration (future-proof)
- Professional segmentation
- Stays free as you grow to 500+

**Phase 2 (Scaling):** Premium features
- SMS campaigns ($0.04-0.06/message)
- Advanced analytics
- Dedicated support

---

## Implementation Plan (Brevo)

### Step 1: Set Up Brevo Account

1. Create account at brevo.com (free)
2. Verify your email
3. Create your first contact list: "Groove Therapy"
4. Set up sender identity (band email: q@groovetherapy.live)

### Step 2: Create Website Signup Form

**Option A: Brevo Embedded Form (Quick)**
- Use Brevo's form builder
- Embed on website homepage
- Professional templates
- Built-in validation

**Option B: Custom Website Form (Better UX)**
- Create custom HTML form on website
- Use Brevo's API to add subscribers
- More control over design
- Integrates with automation

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

**Anti-Spam (Brevo handles most of this):**
- Built-in spam detection
- Double opt-in option (recommended)
- Rate limiting on forms
- Email verification step

### Step 3: Create Welcome Email Automation

Brevo's **Automation Workflows** are perfect for this:

**Email 1: Welcome (Immediate)**
- **Trigger:** When contact added to list
- **Subject:** Welcome to Groove Therapy!
- **Content:**
  ```
  Hi {{FIRSTNAME}},
  
  Thanks for signing up! You're now part of the Groove Therapy community.
  
  Here's what to expect:
  📬 Gig announcements (never spam — just dates & venues)
  🎵 Behind-the-scenes stories from the band
  🎷 Jazz tips & music spotlights
  💌 Monthly newsletter with upcoming events
  
  Follow us:
  - Instagram: @groovetherapysac
  - Facebook: Groove Therapy
  
  See you at a show soon!
  Best, Kevin & Groove Therapy
  ```

**Email 2: Band Story (Day 3)**
- **Trigger:** 3 days after signup
- **Subject:** Meet Groove Therapy 🎷
- **Content:** Band origin story, video link, next gig info

**Email 3: Exclusive Content (Day 7)**
- **Trigger:** 7 days after signup
- **Subject:** Exclusive: Behind-the-Scenes with Groove Therapy 🎬
- **Content:** Exclusive audio/video clip, next gig

**Setup in Brevo:**
1. Go to Automation > Workflows
2. Create new workflow: "Welcome Sequence"
3. Trigger: Contact added to "Groove Therapy" list
4. Add 3 emails with delays (0 days, 3 days, 7 days)
5. Test with yourself before activating

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
3. Lenny loads into Brevo email editor
4. Schedule for 1st of month, 10am
5. Send! (Brevo handles delivery, tracking)

### Step 5: Analytics & Tracking

**Monitor Monthly:**
- Open Rate (goal: >30%)
- Click-Through Rate (goal: >5%)
- Unsubscribe Rate (goal: <0.5%)
- Bounce Rate (keep <2%)
- Subscriber Growth (track additions/removals)

**In Brevo:**
- Dashboard > Campaigns > View detailed reports
- Track automation performance (welcome sequence opens/clicks)
- Contact insights (segment by engagement level)
- Trends (what content performs best?)
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

## Staying with Brevo as You Scale

**The great news:** Brevo grows with you. You won't need to migrate!

### Brevo's Scaling Features

**Free tier (always):**
- Unlimited emails (up to 300/day)
- Automation workflows
- Basic segmentation
- Good for 0-20,000 contacts

**Plus tier ($20-60/month at scale):**
- Priority support
- Advanced segmentation
- SMS campaigns
- Dedicated IP (if needed)
- Perfect for 20k-100k contacts

**No need to switch platforms** — just upgrade plan as you grow.

### Why Brevo Beats Migration

1. **No data loss** — everything stays in place
2. **No platform learning curve** — you're already comfortable
3. **Same tools scale** — automation grows with you
4. **SMS ready** — if you want text alerts later
5. **Cost-effective** — you only pay for what you use

---

## Quick Implementation Timeline

| Week | Action |
|------|--------|
| **Week 1** | Create Brevo account, set up contact list |
| **Week 2** | Create signup form, add to website |
| **Week 3** | Set up welcome automation workflow |
| **Week 4** | Create first monthly newsletter, send |
| **Ongoing** | Review analytics monthly, optimize content |

---

## Cost Summary

| Item | Cost |
|------|------|
| Brevo (Free tier, Year 1) | FREE |
| Website hosting (if needed) | $10-20/mo |
| Custom domain (optional) | $10-15/year |
| **TOTAL (Year 1)** | **$60-90** |
| **Brevo Plus (when scaling past 20k contacts)** | +$20-60/month |

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

- Brevo docs: brevo.com/help
- Brevo tutorials: brevo.com/learning-center
- Email best practices: guides.brevo.com
- Signup form templates: Built-in Brevo form builder
