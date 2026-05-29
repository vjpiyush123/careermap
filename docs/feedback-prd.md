# Student Feedback Feature — PRD

**Version:** 1.0  
**Date:** May 2026  
**Status:** Implemented

---

## 1. Problem Statement

Students exploring career options often face challenges that are not immediately visible to educators and platform developers. Understanding the real pain points, confusions, and information gaps helps:

- Improve CareerGuide content and user experience
- Identify missing features or data
- Understand regional or demographic-specific challenges
- Build a feedback loop for continuous improvement

---

## 2. Feature Overview

A dedicated **Feedback Page** where students can share their challenges, questions, and pain points related to career exploration. The form collects structured data while allowing free-form feedback.

---

## 3. Form Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Student Name** | Text | ✅ Yes | Full name of the student |
| **Email Address** | Email | ✅ Yes | For follow-up if needed (not shared publicly) |
| **Currently Studying In** | Dropdown | ✅ Yes | Class/standard (8th to 12th, UG, PG, Other) |
| **Career Stream of Interest** | Dropdown | ❌ No | Optional - one of 14 career streams or "Not Sure Yet" |
| **Feedback / Pain Points** | Textarea | ✅ Yes | Detailed description of challenges (min 20 chars) |

### Standard Options
- 8th Standard
- 9th Standard
- 10th Standard
- 11th Standard (Science/Commerce/Arts)
- 12th Standard (Science/Commerce/Arts)
- Undergraduate
- Postgraduate
- Other

### Stream Options (Optional)
All 14 career streams:
1. Engineering & Technology
2. Medical & Healthcare
3. Law & Legal Studies
4. Science & Research
5. Education & Teaching
6. Commerce, Finance & Business
7. Arts & Humanities
8. Design & Creative Arts
9. Performing & Fine Arts
10. Sports & Physical Education
11. Civil Services & Government Services
12. Hospitality, Travel & Tourism
13. Agriculture & Environmental Studies
14. Defence Research
15. Not Sure Yet

---

## 4. Technical Implementation

### 4.1 Form Submission
Since CareerGuide's GitHub Pages deployment is static (no backend), form submissions are handled via **Formspree.io**:

- Free tier: 50 submissions/month
- Submissions forwarded to configured email
- No backend required
- AJAX support with redirect capability

**Formspree Endpoint:** `https://formspree.io/f/xanywpbz`

### 4.2 Files Created/Modified

| File | Purpose |
|------|---------|
| `src/careerguide/templates/feedback.html` | Feedback page template |
| `src/careerguide/routes/pages.py` | Added `/feedback` route |
| `src/careerguide/templates/base.html` | Added navbar link |
| `src/careerguide/static/css/style.css` | Feedback form styling |
| `build_static.py` | Include feedback page in static build |

### 4.3 Routes

| Route | Page | Static File |
|-------|------|-------------|
| `/feedback` | Feedback Form | `feedback.html` |

---

## 5. User Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    User clicks "Feedback"                    │
│                         in navbar                            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  Feedback Form Displayed                     │
│  • Introduction explaining why feedback matters              │
│  • Form with 5 fields                                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               User fills form and submits                    │
│  • Client-side validation (min 20 chars for feedback)        │
│  • All required fields validated                             │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Form submitted to Formspree                     │
│  • Data forwarded to configured email                        │
│  • User sees "Thank You" message                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. UI Design

### Page Layout
```
┌─────────────────────────────────────────────────────────────┐
│  🎓 CareerGuide    [Home] [Career Options] [State Guide]    │
│                    [Feedback] [Student Details] [Reports]    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│         Share Your Feedback                                  │
│   Help us understand your challenges in finding              │
│   the right career path                                      │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ 🎯 Why Your Feedback Matters                           │ │
│  │                                                         │ │
│  │ We want to understand the real pain points students     │ │
│  │ face when exploring career options...                   │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                                                         │ │
│  │  Student Name *            [___________________]        │ │
│  │                                                         │ │
│  │  Email Address *           [___________________]        │ │
│  │                                                         │ │
│  │  Currently Studying In *   [___________________▼]       │ │
│  │                                                         │ │
│  │  Stream of Interest        [___________________▼]       │ │
│  │  (Optional)                                             │ │
│  │                                                         │ │
│  │  Your Feedback / Pain Points *                          │ │
│  │  ┌────────────────────────────────────────────────┐    │ │
│  │  │                                                │    │ │
│  │  │                                                │    │ │
│  │  │                                                │    │ │
│  │  └────────────────────────────────────────────────┘    │ │
│  │                                                         │ │
│  │              [ 📨 Submit Feedback ]                     │ │
│  │                                                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  © 2026 CareerGuide — AI-powered career stream guidance      │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Validation Rules

| Field | Validation |
|-------|------------|
| Student Name | Required, non-empty |
| Email | Required, valid email format |
| Standard | Required, must select an option |
| Stream | Optional |
| Feedback | Required, minimum 20 characters |

---

## 8. Success Metrics

- Number of feedback submissions per week
- Common pain points identified
- Feature requests frequency
- Demographic distribution of feedback (by standard/stream)

---

## 9. Future Enhancements

1. **Analytics Dashboard** — Visualize feedback trends
2. **Auto-categorization** — Use AI to categorize feedback themes
3. **Follow-up System** — Email students when their feedback is addressed
4. **Upvoting** — Let students vote on common pain points
5. **Integration with Database** — Store feedback in DB for full-stack deployment

---

## 10. Privacy & Data Handling

- Email addresses are only used for follow-up purposes
- No data is shared with third parties
- Formspree complies with GDPR
- Students can request data deletion via email
