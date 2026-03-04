# Social Media Coordination Tool Specification
**Content Calendar + Approval Workflow**

---

## Overview

You need a system where:
1. **Lenny** plans social media posts (captions, hashtags, media)
2. **Kevin** reviews and approves (or edits) before publishing
3. Posts automatically publish at optimal times
4. You can track engagement and analytics
5. Content is organized by week/month

---

## Architecture Decision

### Option A: Buffer or Later (SaaS, Recommended for MVP)

**Pros:**
- Designed for this exact workflow
- Built-in scheduling
- Calendar view
- Analytics dashboard
- Collaboration/approval tools
- Integrates Instagram + Facebook + others

**Cons:**
- Subscription cost ($15-35/month)
- Some limitations on smaller plans
- External tool (data outside your control)

**Cost:** $15-35/month

### Option B: Hootsuite

**Pros:**
- Powerful features
- Good for multi-platform management
- Approval workflows
- Advanced analytics

**Cons:**
- Steeper learning curve
- Pricier ($49-739/month)
- Overkill for starting out

**Cost:** $49-739/month

### Option C: Custom-Built Tool

**Pros:**
- Tailored exactly to your needs
- No subscription costs
- Full control

**Cons:**
- Takes time to build (2-3 weeks)
- Needs maintenance
- Complexity of integrating with Instagram/Facebook APIs

**Cost:** $300-500 development + $20-50/month hosting

### Option D: Simple Google Sheets + Native Platform Scheduling

**Pros:**
- Free
- Collaborative (Kevin & Lenny can both edit)
- Integrates with tools you already use
- Simple

**Cons:**
- More manual work
- No central publishing hub
- Harder to track analytics
- Can't schedule to Instagram natively (Threads only)

**Cost:** Free (Google Workspace if not already used)

---

## Recommendation: Hybrid Approach (Month 1-2)

**Phase 1 (Now - Month 2):** **Google Sheets + Native Scheduling**
- Build weekly content calendar in Sheets
- Lenny plans posts with media
- Kevin reviews in Sheets
- Posts scheduled natively on Instagram/Facebook
- Cost: $0
- Time investment: 2 hours/week

**Phase 2 (Month 3+):** **Upgrade to Buffer** (if workflow works)
- Higher volume posting
- Better analytics
- Less manual work
- Cost: $15-35/month
- Time investment: 1 hour/week

---

## Implementation: Phase 1 (Google Sheets)

### Create Content Calendar Template

**Spreadsheet Structure:**

```
Columns:
A: Date (Friday, March 15)
B: Platform (Instagram, Facebook, Both)
C: Content Type (Video, Photo, Story, Text)
D: Caption/Copy (post text + hashtags)
E: Media (link to image/video file)
F: Schedule Time (e.g., 6:00pm)
G: Status (Draft, Pending Review, Approved, Posted)
H: Lenny Notes (context, inspiration)
I: Kevin Feedback (edits/approval)
J: Engagement (likes, comments after posting)
```

**Sample Row:**
```
Date: Friday, March 15
Platform: Instagram
Type: Video
Caption: "Vibes last Saturday @ [Venue] 🎷✨ Who else was there? [LINK] #GrooveTherapy #LiveJazz #Sacramento"
Media: [Google Drive link to video]
Schedule: 6:00pm
Status: Pending Review
Lenny Notes: "Performance clip from gig, high energy. Good example of stage presence."
Kevin Feedback: "Love this! Can you add the date of the next show in the caption?"
Engagement: [Will fill after posting]
```

### Weekly Planning Process

**Every Tuesday Morning (1 hour work):**

1. **Lenny** plans next week's content (8-10 posts)
   - 2-3 videos or reels
   - 2-3 BTS/member content
   - 2 gig announcements (if applicable)
   - 1-2 educational posts
   - Hashtags and CTAs for each

2. **Wednesday-Thursday:**
   - Kevin reviews all posts
   - Edits copy, hashtags, timing as needed
   - Approves or requests changes
   - Marks status as "Approved"

3. **Friday-Sunday:**
   - Lenny schedules approved posts natively
   - Instagram: Use Business Account native scheduling
   - Facebook: Use native scheduling
   - Note "Posted" in Status column with timestamp

4. **Monitor & Engage:**
   - Daily: Check comments/DMs
   - Respond within 24 hours
   - Note top-performing posts for future planning

### Where to Store Media

**Google Drive Folder Structure:**
```
Groove Therapy Social Media/
├── 2026-03 (March 2026)
│   ├── Video Clips
│   │   ├── Gig_FridayKillers_3-15.mp4
│   │   ├── BTS_Rehearsal_3-12.mp4
│   ├── Photos
│   │   ├── Band_Promo_1.jpg
│   │   ├── BTS_Setup_1.jpg
│   ├── Graphics
│   │   ├── Event_Poster.png
│   │   ├── Quote_Graphic.png
├── Templates (for recurring content types)
│   ├── Story_Quote.png
│   ├── Gig_Announcement_Template.png
```

**Share link in Sheets:** `=HYPERLINK("Google Drive URL", "Link")`

---

## Instagram Business Account Setup

### Initial Setup

1. Convert personal to Business Account
   - Settings > Account Type > Switch to Professional
   - Choose "Creator" or "Business"
   - Link website/mailing list

2. Add Team Members
   - Settings > Roles > Add Lenny as Businesspartner or Content Creator
   - Set permissions (can manage content, respond to messages, view analytics)

### Native Scheduling

**For Posts (Not Stories):**
1. Create post normally
2. Tap "Schedule" instead of "Share"
3. Select date + time
4. Confirm

**For Stories/Reels:**
- Instagram doesn't support native scheduling for Stories/Reels
- Use Buffer or schedule via URL/app

---

## Facebook Setup

### Page Configuration

1. Create Business Page: facebook.com/pages/create
2. Page name: "Groove Therapy"
3. Link Instagram account (optional but recommended)
4. Add website link to About section

### Native Scheduling

1. Create post on Page (photo, video, or text)
2. Click schedule icon (clock)
3. Choose date + time
4. Confirm

---

## Engagement & Response Protocol

### Daily Checklist (30 min)

- [ ] Check Instagram comments (all posts from last 3 days)
- [ ] Check Facebook comments
- [ ] Check DMs (Instagram + Facebook)
- [ ] Respond to comments with appreciation
- [ ] Flag any booking inquiries for Kevin

**Response Examples:**

*Comment: "Loved your set last Saturday!"*
Response: "Thanks so much! You made the night amazing 🙌 Hope to see you at our next show [date]!"

*Comment: "What's that song in the video?"*
Response: "That's an original called [Song] 🎷 We play it every Friday @ [Venue]!"

*DM: "How much do you charge for private events?"*
Response: "Great question! We'd love to play your event. Can I get more details about the date/venue? Feel free to email q@groovetherapy.live for a quote."

---

## Analytics Tracking (Weekly Review)

**Every Friday, review metrics:**

| Metric | Instagram | Facebook | Notes |
|--------|-----------|----------|-------|
| Followers | +___ | +___ | Track growth |
| Post Reach | ___ | ___ | Average per post |
| Engagement | ___ | ___ | Likes + comments |
| Clicks | ___ | ___ | Link clicks (if tracking) |
| Top Post | ___ | ___ | Best performer |

**Use:** Instagram Insights (accessed via app/web) + Facebook Analytics

**What to Do With Data:**
- Which content types perform best? (video vs photo vs text)
- What time gets best engagement? (adjust schedule time)
- Which hashtags drive most reach? (use more)
- Are CTAs converting? (gig announcements → ticket sales?)

---

## Phase 2: Upgrade to Buffer (Optional, Month 3+)

If Sheets is working but you want to streamline:

### Buffer Setup

1. Create account at buffer.com
2. Connect Instagram account
3. Connect Facebook page
4. Grant permission to publish

### Buffer Workflow

1. **Lenny** creates post in Buffer
   - Add caption
   - Add media
   - Select time
   - Assign to "Pending Review" list

2. **Kevin** reviews in Buffer
   - Can edit copy
   - Can change time
   - Approves or requests changes

3. **Buffer** publishes automatically
   - Sends at scheduled time
   - Tracks analytics automatically

### Buffer Analytics

Built-in reporting:
- Best posting times
- Top performing content
- Follower growth
- Engagement metrics

### Buffer Cost

- **Buffer free tier:** 3 social accounts, 10 posts/month, basic analytics
- **Buffer Pro:** $15/month (unlimited posts, advanced scheduling)
- **Buffer Premium:** $35/month (team collaboration, more analytics)

**Recommendation:** Start with Pro ($15/month) when you hit 100+ posts/month

---

## Platform-Specific Tips

### Instagram

**Posting Times (Sacramento Audience):**
- Friday: 6-9pm (people planning weekend)
- Saturday: 9-11am (morning coffee scrolling)
- Sunday: 10am-12pm (weekend lazy time)

**Content Mix:**
- 60% Video/Reels (algorithm favors)
- 30% Carousel posts
- 10% Text/Stories

**Hashtag Strategy:**
- 20-30 hashtags per post
- Mix: Popular (#jazz, #livemusic) + Niche (#smoothjazz, #groovetherapy) + Local (#Sacramento, #sacramentomusic)

**Story Frequency:**
- 3-5 stories per week (behind-the-scenes, polls, announcements)
- Use swipe-up link if follower count allows

### Facebook

**Posting Times:**
- Friday: 6-8pm
- Saturday: 7-9pm
- Sunday: 10am-1pm

**Content Mix:**
- Video gets 10x engagement vs text
- Event posts (using Facebook Events) get high reach
- Community/local news gets shared more

**Engagement:**
- Respond to comments within 24 hours
- Reply to page messages in DMs
- Encourage discussion with questions

---

## Content Ideas (Pre-Generated)

### Videos (2-3 per week)
- 30-second performance clip from gig
- Member spotlight: "[Name] talks about..."
- Bloopers/funny moments
- Setlist for next show
- Quick jam/acoustic session
- "Ask the Band" Q&A
- Transition/behind-the-scenes

### Photos (2-3 per week)
- Band on stage (professional shots)
- Behind-the-scenes (setup, rehearsal, candids)
- Band at gig (crowd reactions, energy)
- Member close-ups/individual headshots
- Instrument details (beautiful detail shot)
- Crowd/venue atmosphere

### Text/Stories (2-3 per week)
- "Fun fact about [artist]"
- "One week until [gig]!"
- Poll: "What should we play next?"
- Quote about music
- Gig announcement
- Mailing list signup CTA

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Instagram won't let me schedule** | Use Buffer, or schedule manually at scheduled time |
| **Not getting views on posts** | Check timing, use more hashtags, use Reels instead of photos |
| **Low engagement** | Ask questions in captions, respond to comments, post more video |
| **Can't think of content** | Use pre-generated ideas list, ask band members for clips |
| **Hashtags look spammy** | Put them in first comment instead of caption |

---

## Quick-Start Checklist

- [ ] Create Google Sheets content calendar
- [ ] Convert Instagram account to Business
- [ ] Set up Facebook page
- [ ] Create Google Drive media folder
- [ ] Plan first 2 weeks of content (10-15 posts)
- [ ] Kevin reviews and approves
- [ ] Schedule posts natively
- [ ] Monitor analytics weekly

---

## Timeline

| Phase | Timeline | Tools | Cost |
|-------|----------|-------|------|
| **MVP** | Now - Week 4 | Sheets + Native | $0 |
| **Optimize** | Week 4-12 | Sheets + Buffer | $15/mo |
| **Scale** | Month 4+ | Buffer Pro + Analytics | $35/mo |

---

## Success Metrics

- [ ] 150+ followers (combined) by Month 3
- [ ] 3-5% engagement rate (likes+comments/followers)
- [ ] 1+ gig booked directly from social media
- [ ] 100+ mailing list signups from social CTAs
- [ ] Consistent 3x/week posting schedule maintained

---

## Owner: Lenny (with Kevin's Creative Direction & Approval)
**Status:** Ready to implement  
**Next Step:** Create Sheets template + start planning first week of content

---

## Resources

- Instagram Business Account docs: instagram.com/help
- Facebook Page setup: facebook.com/help
- Buffer tutorial: buffer.com/library/tutorials
- Hashtag generator: hashtagify.me
- Post scheduling guide: [Link]
