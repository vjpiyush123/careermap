# Student Feedback Feature — PRD

**Version:** 1.1  
**Date:** May 2026  
**Status:** Implemented (Database-backed)

---

## 1. Problem Statement

Students exploring career options often face challenges that are not immediately visible to educators and platform developers. Understanding the real pain points, confusions, and information gaps helps:

- Improve CareerGuide content and user experience
- Identify missing features or data
- Understand regional or demographic-specific challenges
- Build a feedback loop for continuous improvement

---

## 2. Feature Overview

A dedicated **Feedback Page** where students can share their challenges, questions, and pain points related to career exploration. Feedback is stored in the database and can be viewed by administrators.

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

### 4.1 Database Model
Feedback is stored in the `feedbacks` table:

```python
class FeedbackRow(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    standard = Column(String(50), nullable=False)
    stream = Column(String(100), nullable=True)  # Optional
    feedback = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
```

### 4.2 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/feedback` | Display feedback form |
| POST | `/api/feedback` | Submit feedback (JSON) |
| GET | `/admin/feedback` | Admin view of all feedback |

### 4.3 Files Created/Modified

| File | Purpose |
|------|---------|
| `src/careerguide/db/models.py` | Added FeedbackRow model |
| `src/careerguide/db/crud.py` | Added create_feedback, list_all_feedbacks |
| `src/careerguide/templates/feedback.html` | Feedback form (AJAX submission) |
| `src/careerguide/templates/feedback_admin.html` | Admin view template |
| `src/careerguide/routes/pages.py` | API and page routes |
| `src/careerguide/static/css/style.css` | Styling for feedback pages |

---

## 5. User Flow

### Student Submission Flow
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
│  • AJAX POST to /api/feedback                                │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Feedback saved to database                      │
│  • User sees "Thank You" message                             │
└─────────────────────────────────────────────────────────────┘
```

### Admin View Flow
```
Admin navigates to /admin/feedback
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│              All feedback displayed                          │
│  • Sorted by most recent first                               │
│  • Shows student name, email, standard, stream, feedback     │
│  • Timestamps for each submission                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. UI Design

### Feedback Form Page (`/feedback`)
- Introduction card explaining why feedback matters
- Clean form with labeled fields
- Submit button with loading state
- Success message after submission

### Admin View Page (`/admin/feedback`)
- Total feedback count stat card
- List of feedback cards showing:
  - Student name and email
  - Standard and stream tags
  - Full feedback content
  - Submission timestamp
- Empty state when no feedback exists

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

## 8. Access Control

| Route | Access |
|-------|--------|
| `/feedback` | Public (all users) |
| `/admin/feedback` | Currently open (future: admin authentication) |

**Future Enhancement:** Add authentication for admin routes.

---

## 9. Success Metrics

- Number of feedback submissions per week
- Common pain points identified
- Feature requests frequency
- Demographic distribution of feedback (by standard/stream)

---

## 10. Future Enhancements

1. **Admin Authentication** — Protect admin routes with login
2. **Analytics Dashboard** — Visualize feedback trends
3. **Auto-categorization** — Use AI to categorize feedback themes
4. **Follow-up System** — Email students when their feedback is addressed
5. **Export to CSV** — Download feedback data for analysis
6. **Delete/Archive** — Allow admins to manage feedback entries
