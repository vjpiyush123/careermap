# Masterplan.PRD

## Career Guide for students

---

## 1. Product Vision & Problem Statement

### Vision

Enable **real-time, transparent, and trustworthy analysis** by automating labor-intensive human data analysis to find out which subject stream has what type of career opportunity going forward when we select the specific subject stream after 10th / 12th class, **fetching data from trustworthy sources**.

### Problem Statement

The 10th or 12th grade students are confused about which subject stream to select and what different types of opportunities are available, and what related career options will be available going forward.

- **Highly manual and time-consuming**, relying on word of mouth information, getting manual data from different sources.
- **Error-prone and non-scalable**, especially when many students are confused about which subject stream to select.
- **Opaque and fragmented**, with insights residing with a few individuals

- Students not aware of all the stream available
  - Traditional - Science PCM , PCMB, Commerce , Arts
  - Skill based Training for e.g. - ITI,  

### Key pain points include

- Manually validating **whether those subject streams are good career paths with growth in future**
- Identifying **how to select the best subject streams which have effective career growth paths**
- Assessing **based on the 10th and 12th percentage marks the student achieved in exams**
- Arriving at a defensible **top 2 selection for the student based on the data**
- Selecting the college based on the **budgets**
- List all the top 10 colleges in India.
- List top 2 college from each states
- Display the college data in tabular format

- Table format
| College Name | College Ranking | City | state | Average fees |  Placement (LPA) | Total seats

- User should be able to have the option to fetch the further details of each college as below
| College Name | Branch Details | Total seats

### Why This Product Exists

To **eliminate repetitive human reasoning on selecting the subject stream for student**, replace it with **deterministic + LLM-assisted analysis** summary to the parents and student.

---

## 2. Target Users & Usage Context

### Primary Users

- Parents
- Students

### Usage Context

- Used to take the data driven approach to suggest best subject stream of student.

### User Intent

- Understand *what stream can be the best fix for the student*

---

## 2A. User-Supplied Inputs

The system must accept the following inputs at analysis invocation time:

| Input | Description | Example |
|-------|-------------|---------|
| Name | Name of the student | Ravi Sharma |
| Standard | 10th, 11th, 12th | Class the student is currently studying in |
| Percentage | 10th or 12th marks percentage | Percentage obtained in the respective class |
| Interest | Commerce, Science, Maths, etc. | Single subject stream the student is most interested in (radio button — one selection only) |

> **Analysis scope:** When a student selects an interest, the analysis engine generates results **only for the selected stream** and its associated career paths. If no interest is selected, all streams are analysed.

---

> **Note**: Sections 3 (Data Model), 4 (Analysis Rules), and 5 (Scoring Logic) are detailed in the supporting PRDs listed in §13.

---

## 6. Trust, Transparency & Explainability Principles

### T1. AI as Advisor, Not Authority

- The agent **supports decision-making**
- Accountability always remains with humans

### T2. Data-First Reasoning

- All conclusions must be grounded in:
  - Input data
  - Data provided by the user
  - No speculative inference
  
## 7. Reliability & Predictability

### Predictability Expectations

- Same input state → same analysis output
- No non-deterministic behavior
- No hallucinated insights

### Accuracy Guardrails

- If data is insufficient:
  - The system must say so explicitly
  - And avoid forced conclusions

### AI Reasoning Boundaries

- **Deterministic steps** (no LLM): data fetching, capacity math, cutoff calculation, flag generation
- **LLM-assisted steps** : executive summary narrative, recommendation phrasing, dependency impact explanation
- The system must produce **correct results without an LLM**; AI enhances explanation quality only

> Pipeline component details belong in the **Architecture PRD**. Reasoning rules per step belong in the **AI-Reasoning & Analysis PRD**.

---

## 11. Non-Functional Requirements

### Performance

- Full analysis should complete in **< 2 minutes**
- 100+ users will be using simultaneously
- Results must be cacheable with a clear staleness indicator
- **MVP observation**: Typical analysis runs complete in 30–60 seconds for any queries

---

## 12. Success Metrics

| Metric | Target |
|--------|--------|

| Analysis accuracy vs. manual analysis | ≥ 95% agreement on decisions |

---

## 13. References to Supporting PRDs

This Masterplan intentionally **does not contain details** covered elsewhere.

It references the following supporting PRDs:

| PRD | Scope | Status |
|-----|-------|--------|

| **[UI & Interaction PRD](ui-interaction-prd.md)** | User flows, report presentation, explainability in UI | Complete |
| **[Student Profile](student_profile.md)** | Psychometric questionnaire for stream aptitude assessment | Complete |
| **[Psychology Test](psychology_test.md)** | Psychometric questionnaire for stream aptitude assessment | Complete |
| **[Career Path](careermap-prd.md)** | listed all the career paths | Complete |
| **AI-Reasoning & Analysis PRD** | Reasoning rules, analysis dimensions, conservatism rules, explainability | Planned |
| **Data & Integration PRD** | Canonical data model, field mappings, API contracts | Planned |
| **Validation & Quality PRD** | Acceptance criteria, test strategy, correctness verification | Planned |

---

## 14. Career Options Page — Tabbed UI Enhancement (v2)

### Overview

The `/careeroptions` page was redesigned with a professional sidebar + tabbed content layout to provide comprehensive career guidance for each of the 14 streams.

### Tab Structure (per stream)

Each stream panel now contains **7 tabs** in the following order:

| # | Tab | Description |
|---|-----|-------------|
| 1 | **Roadmap** | Step-by-step guide (7 steps per stream) from Class 10th to career launch |
| 2 | **Selection Process** | Entrance exams table: Exam Name, Conducted By, Eligibility, Pattern, Tentative Dates, Website link |
| 3 | **Coaching** | List of coaching institutes relevant to the stream |
| 4 | **Career Paths** | Career options with salary, roles, and growth outlook (India & Abroad) |
| 5 | **Colleges (State)** | State-wise college tables with rankings, fees, placements, seats |
| 6 | **Top Colleges (India)** | National top 10 colleges with website links, rankings, fees, placements |
| 7 | **Abroad** | International opportunities: countries, exams, universities, costs, scholarships, work visas |

### Data Layer Changes

New data dictionaries added to `career_data.py`:

- **`_ROADMAP`** — 14 entries, each with 7 steps (step number, title, detail)
- **`_SELECTION_PROCESS`** — 14 entries, each with exam details (exam name, conducted by, eligibility, pattern, dates, website URL)
- **`_ABROAD_DATA`** — 14 entries, each with: overview, top countries, exams required, top universities, avg cost/year, scholarships, work visa info

Each stream in `_STREAM_DATA` now includes three additional keys:
- `roadmap` → references `_ROADMAP[stream_name]`
- `selection_process` → references `_SELECTION_PROCESS[stream_name]`
- `abroad` → references `_ABROAD_DATA[stream_name]`

### College Website Links

- All top-ranked national colleges (IITs, AIIMS, NLUs, NIDs, etc.) have website links
- College names in tables are displayed as clickable links when a website URL is available
- State-level colleges also display as links where website data exists

### UI/UX Features

- **Sidebar + Content layout**: Left sidebar lists all 14 streams; clicking switches the right-side content panel
- **Underline-style horizontal tabs**: Professional tab bar with active indicator
- **Roadmap timeline**: Visual vertical timeline with numbered step markers
- **Selection Process table**: Sortable exam data with direct website links ("Visit ↗")
- **Abroad cards**: Grid layout showing countries, universities, costs, scholarships, visas
- **Dark/Light theme toggle**: Accessible from navbar on all pages (persists via localStorage)
- **Responsive design**: Sidebar collapses to horizontal pills on mobile; tabs scroll horizontally

### Files Modified

| File | Changes |
|------|---------|
| `src/careerguide/data/career_data.py` | Added `_ROADMAP`, `_SELECTION_PROCESS`, `_ABROAD_DATA` dicts; wired into `_STREAM_DATA` |
| `src/careerguide/templates/career_options.html` | Rewrote with 7-tab layout, roadmap timeline, selection process table, abroad section |
| `src/careerguide/static/css/style.css` | Added roadmap timeline, abroad grid, and selection process table styles |
| `src/careerguide/templates/base.html` | Added theme toggle button and inline theme init script |
| `src/careerguide/static/js/main.js` | Added theme toggle logic with localStorage persistence |

---

## GitHub Pages Deployment

### Rule: Every Page Must Ship to GitHub Pages

**Any new page or menu item added to the FastAPI application MUST also be included in the static GitHub Pages build.** This ensures the public-facing site at `github.io` stays in sync with the full application.

### Checklist for Adding a New Page

When adding a new page to CareerGuide, complete ALL of the following:

1. **`build_static.py`** — Add a render step for the new page with its required template context (data imports, mock request, etc.)
2. **`static_templates/base.html`** — Add the page link to the navbar `nav-links` section
3. **`build_static.py` INDEX_TEMPLATE** — Add the page link to the landing page navbar
4. **Landing page CTAs** — If the page is a major feature, add a button/link to the landing page hero section
5. **Static template override** (if needed) — If the page has features that require a backend (form submissions, DB writes), create a `static_templates/<page>.html` override with a graceful fallback message (see `static_templates/feedback.html` as an example)
6. **Rebuild & verify** — Run `python build_static.py` and verify the new page renders in `_site/`

### Current Pages (Static Build)

| Page | File | Status |
|------|------|--------|
| Home / Landing | `index.html` | ✅ Built from INDEX_TEMPLATE |
| Career Options | `careeroptions.html` | ✅ Full data, all 14 streams |
| College Directory | `colleges.html` | ✅ Full data, 78 colleges (Engg + Medical + IIIT) |
| State Opportunities | `stateopportunities.html` | ✅ All 33 states/UTs |
| Feedback | `feedback.html` | ✅ Static override (email fallback) |

### Static Build Command

```bash
python build_static.py                    # relative paths (works everywhere)
python build_static.py --base /careermap  # for repo-based GitHub Pages
```

### Key Files

| File | Purpose |
|------|---------|
| `build_static.py` | Renders all pages + copies assets to `_site/` |
| `static_templates/base.html` | Navbar override for static site (all page links) |
| `static_templates/feedback.html` | Feedback page override (no DB backend) |
| `_site/` | Output directory deployed to GitHub Pages |
| `_site/.nojekyll` | Tells GitHub Pages to skip Jekyll processing |

---

## Closing Principle

> **The CareerGuide Analysis Agent exists to replace repetitive human analysis,
> not human judgment.
> It must be trusted because it is transparent,
> and conservative because commitments matter.**
