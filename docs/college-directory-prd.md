# College Directory — PRD

## Problem Statement

Students selecting career streams need detailed, actionable college information to make informed decisions. The current CareerGuide portal provides only a top-10 summary per stream with basic fields (name, ranking, fees, placement, seats). Students lack:

- **Branch-level details** — Which departments exist at each college? How many seats per branch?
- **Course type clarity** — Is B.Tech available? What about Dual Degree, Integrated M.Tech, BS-MS, PhD?
- **Cutoff information** — What JEE/NEET rank do I need for CSE at IIT Bombay vs NIT Trichy?
- **Per-branch placement data** — CSE placements differ vastly from Civil at the same college
- **Filtering & comparison** — No way to filter colleges by state, fees, branch, or compare side-by-side
- **Accreditation & ranking context** — NIRF rank, NAAC grade, NBA accreditation missing

This information is scattered across dozens of websites (college portals, JoSAA, MCC, NIRF). Students waste weeks manually researching. A centralized, structured college directory solves this.

## Solution

Add a dedicated **College Directory** page (`/colleges`) that provides comprehensive, filterable, and comparable college data for all 14 career streams.

## Scope

### Implemented (All Streams)
- **Engineering & Technology** — 23 top India (IITs, NITs, BITS, State/Private) + 30 IIITs = **53 colleges**
- **Medical & Healthcare** — Top 25 India = **25 colleges**
- **Law & Legal Studies** — Top 10 India = **10 colleges**
- **Science & Research** — Top 10 India (IISc, IISERs, ISI, CMI) = **10 colleges**
- **Commerce, Finance & Business** — Top 10 India (IIMs, ISB, SRCC, FMS) = **10 colleges**
- **Education & Teaching** — Top 10 India (NCERT, TISS, APU, BHU) = **10 colleges**
- **Design & Creative Arts** — Top 10 India (NID, NIFT, IDC) = **10 colleges**
- **Arts & Humanities** — Top 10 India (JNU, DU, Ashoka) = **10 colleges**
- **Performing & Fine Arts** — Top 5 India (NSD, FTII, SRFTI) = **5 colleges**
- **Sports & Physical Education** — Top 5 India (LNIPE, SAI) = **5 colleges**
- **Civil Services & Government** — Top 5 India (LBSNAA, NPA, IIPA) = **5 colleges**
- **Hospitality, Travel & Tourism** — Top 5 India (IHM, WGSHA) = **5 colleges**
- **Agriculture & Environmental Studies** — Top 5 India (IARI, TNAU, PAU) = **5 colleges**
- **Defence & Military** — Top 5 India (NDA, IMA, AFMC) = **5 colleges**

**Total: 168 colleges across 14 career streams**

### Future Expansion
- Top 25 per stream for all categories
- State-level colleges (33 states × ~10 per stream)

## Data Structure

### College (Enhanced Model)

```
College:
  # ── Identity ──
  name: str                          # "Indian Institute of Technology Bombay"
  short_name: str                    # "IIT Bombay"
  institute_type: str                # "IIT" | "NIT" | "IIIT" | "State Govt" | "Private" | "Deemed" | "Central University" | "AIIMS"
  established: int                   # 1958
  website: str                       # "https://www.iitb.ac.in"

  # ── Location ──
  city: str
  state: str
  campus_area_acres: float

  # ── Rankings & Accreditation ──
  nirf_ranking: int
  nirf_year: int                     # 2025
  naac_grade: str                    # "A++" | "A+" | "A" | "B++" | etc.
  nba_accredited: bool
  ranking_source: str                # "NIRF 2025"

  # ── Admissions ──
  entrance_exams: list[str]          # ["JEE Advanced", "GATE", "JAM"]
  admission_process: str             # "JoSAA Counselling for B.Tech; COAP for M.Tech"
  total_seats: int

  # ── Financials ──
  avg_fees_lpa: float
  hostel_fees_per_year: float
  fee_waiver_policy: str             # "Full tuition waiver for SC/ST"

  # ── Placements (aggregate) ──
  avg_placement_lpa: float
  median_placement_lpa: float
  highest_placement_lpa: float
  placement_percentage: float
  top_recruiters: list[str]          # ["Google", "Microsoft", "Goldman Sachs"]

  # ── Facilities ──
  hostel_available: bool
  notable_alumni: list[str]

  # ── Nested ──
  branches: list[Branch]
  course_types: list[CourseType]
```

### Branch (per college)

```
Branch:
  name: str                          # "Computer Science & Engineering"
  short_name: str                    # "CSE"

  # ── Seats ──
  ug_seats: int                      # 120 (B.Tech)
  pg_seats: int                      # 60 (M.Tech)
  phd_seats: int
  dual_degree_seats: int

  # ── Cutoffs (latest year) ──
  cutoff_year: int                   # 2025
  cutoff_exam: str                   # "JEE Advanced" | "NEET UG"
  general_opening_rank: int
  general_closing_rank: int
  obc_closing_rank: int
  sc_closing_rank: int
  st_closing_rank: int
  ews_closing_rank: int
  female_closing_rank: int           # supernumerary where applicable

  # ── Branch-specific Placements ──
  avg_placement_lpa: float
  median_placement_lpa: float
  highest_placement_lpa: float
  placement_percentage: float

  # ── Key Info ──
  specializations: list[str]         # ["AI/ML", "Systems", "Theory"]
```

### CourseType (per college)

```
CourseType:
  name: str                          # "B.Tech" | "MBBS" | "Dual Degree"
  duration_years: float              # 4.0, 5.5, 2.0
  entrance_exam: str                 # "JEE Advanced" | "NEET UG"
  eligibility: str                   # "10+2 with PCM, 75% aggregate"
  total_seats: int
  fee_per_year_lpa: float
  available_branches: list[str]      # ["CSE", "EE", "ME"]
```

## Data Coverage

### Engineering — Top 23 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IIT Bombay | IIT | Maharashtra |
| 2 | IIT Delhi | IIT | Delhi |
| 3 | IIT Madras | IIT | Tamil Nadu |
| 4 | IIT Kanpur | IIT | Uttar Pradesh |
| 5 | IIT Kharagpur | IIT | West Bengal |
| 6 | IIT Roorkee | IIT | Uttarakhand |
| 7 | IIT Guwahati | IIT | Assam |
| 8 | IIT Hyderabad | IIT | Telangana |
| 9 | IIT BHU Varanasi | IIT | Uttar Pradesh |
| 10 | IIT Indore | IIT | Madhya Pradesh |
| 11 | NIT Trichy | NIT | Tamil Nadu |
| 12 | NIT Karnataka Surathkal | NIT | Karnataka |
| 13 | NIT Warangal | NIT | Telangana |
| 14 | NIT Calicut | NIT | Kerala |
| 15 | NIT Rourkela | NIT | Odisha |
| 16 | BITS Pilani | Private | Rajasthan |
| 17 | DTU Delhi | State Govt | Delhi |
| 18 | NSUT Delhi | State Govt | Delhi |
| 19 | VIT Vellore | Private | Tamil Nadu |
| 20 | COEP Pune | State Govt | Maharashtra |
| 21 | Jadavpur University | State Govt | West Bengal |
| 22 | Anna University | State Govt | Tamil Nadu |
| 23 | ICT Mumbai | Deemed | Maharashtra |

**Engineering branches:** CSE, EE, ECE, ME, CE, CH, AE, MME, BT, MnC, EP, AI

**Engineering course types:** B.Tech (4yr), Dual Degree B.Tech+M.Tech (5yr), BS+MS (5yr), M.Tech (2yr), MS by Research (2-3yr), PhD (3-5yr), B.Arch (5yr)

### IIIT — All 30 IIITs in India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IIIT Hyderabad | IIIT | Telangana |
| 2 | IIIT Delhi | IIIT | Delhi |
| 3 | IIIT Allahabad | IIIT | Uttar Pradesh |
| 4 | IIIT Bangalore | IIIT | Karnataka |
| 5 | ABV-IIITM Gwalior | IIIT | Madhya Pradesh |
| 6 | IIITDM Jabalpur | IIIT | Madhya Pradesh |
| 7 | IIITDM Kancheepuram | IIIT | Tamil Nadu |
| 8 | IIIT Sri City | IIIT | Andhra Pradesh |
| 9 | IIIT Lucknow | IIIT | Uttar Pradesh |
| 10 | IIIT Guwahati | IIIT | Assam |
| 11 | IIIT Vadodara | IIIT | Gujarat |
| 12 | IIIT Kota | IIIT | Rajasthan |
| 13 | IIIT Trichy | IIIT | Tamil Nadu |
| 14 | IIIT Una | IIIT | Himachal Pradesh |
| 15 | IIIT Sonepat | IIIT | Haryana |
| 16 | IIIT Kalyani | IIIT | West Bengal |
| 17 | IIIT Dharwad | IIIT | Karnataka |
| 18 | IIIT Kancheepuram (PPP) | IIIT | Tamil Nadu |
| 19 | IIITDM Kurnool | IIIT | Andhra Pradesh |
| 20 | IIIT Nagpur | IIIT | Maharashtra |
| 21 | IIIT Pune | IIIT | Maharashtra |
| 22 | IIIT Ranchi | IIIT | Jharkhand |
| 23 | IIIT Bhagalpur | IIIT | Bihar |
| 24 | IIIT Bhopal | IIIT | Madhya Pradesh |
| 25 | IIIT Surat | IIIT | Gujarat |
| 26 | IIIT Kottayam | IIIT | Kerala |
| 27 | IIIT Raichur | IIIT | Karnataka |
| 28 | IIIT Agartala | IIIT | Tripura |
| 29 | IIIT Manipur | IIIT | Manipur |
| 30 | IIIT Srikakulam | IIIT | Andhra Pradesh |

**IIIT categories:**
- Government-funded (autonomous): IIIT Hyderabad, IIIT Delhi, IIIT Allahabad, IIIT Bangalore, ABV-IIITM Gwalior
- IIITDM (Design & Manufacturing): IIITDM Jabalpur, IIITDM Kancheepuram, IIITDM Kurnool
- PPP (Public-Private Partnership): All remaining IIITs (established under MHRD PPP scheme)

**IIIT branches:** CSE, IT, ECE, ME, ICT, CSD, CSAM

**IIIT course types:** B.Tech (4yr), Dual Degree B.Tech+M.Tech (5yr), M.Tech (2yr), IPG (5yr), MS by Research (2.5yr)

### Medical — Top 25 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | AIIMS New Delhi | Central | Delhi |
| 2 | PGIMER Chandigarh | Central | Chandigarh |
| 3 | CMC Vellore | Private | Tamil Nadu |
| 4 | JIPMER Puducherry | Central | Puducherry |
| 5 | NIMHANS Bangalore | Central | Karnataka |
| 6 | Kasturba Medical College Manipal | Private | Karnataka |
| 7 | BHU IMS Varanasi | Central University | Uttar Pradesh |
| 8 | King George's Medical University | State Govt | Uttar Pradesh |
| 9 | Maulana Azad Medical College | State Govt | Delhi |
| 10 | Madras Medical College | State Govt | Tamil Nadu |
| 11 | Grant Medical College Mumbai | State Govt | Maharashtra |
| 12 | Seth GS Medical College Mumbai | State Govt | Maharashtra |
| 13 | AFMC Pune | Defence | Maharashtra |
| 14 | Lady Hardinge Medical College | Central | Delhi |
| 15 | Stanley Medical College Chennai | State Govt | Tamil Nadu |
| 16 | Govt Medical College Trivandrum | State Govt | Kerala |
| 17 | AIIMS Jodhpur | Central | Rajasthan |
| 18 | AIIMS Bhopal | Central | Madhya Pradesh |
| 19 | AIIMS Rishikesh | Central | Uttarakhand |
| 20 | St. John's Medical College | Private | Karnataka |
| 21 | Osmania Medical College | State Govt | Telangana |
| 22 | SCB Medical College Cuttack | State Govt | Odisha |
| 23 | JNMC Belgaum | Private | Karnataka |
| 24 | RIMS Ranchi | State Govt | Jharkhand |
| 25 | Patna Medical College | State Govt | Bihar |

**Medical departments:** MBBS, BDS, General Medicine (MD), Surgery (MS), Pediatrics, Orthopedics, Ob-Gyn, Dermatology, Radiology, Anaesthesiology, Ophthalmology, ENT, Psychiatry, Cardiology (DM), Neurology (DM), Nephrology (DM), Gastroenterology (DM)

**Medical course types:** MBBS (5.5yr), BDS (5yr), MD (3yr), MS (3yr), DM (3yr), MCh (3yr), B.Sc Nursing (4yr), BPT (4.5yr), B.Pharm (4yr), PhD

### Law & Legal Studies — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | NLU Delhi | Central | Delhi |
| 2 | NLSIU Bangalore | Central | Karnataka |
| 3 | NALSAR Hyderabad | Central | Telangana |
| 4 | NLU Jodhpur | Central | Rajasthan |
| 5 | WBNUJS Kolkata | Central | West Bengal |
| 6 | GNLU Gandhinagar | State | Gujarat |
| 7 | Symbiosis Law School | Private | Maharashtra |
| 8 | Faculty of Law DU | Central University | Delhi |
| 9 | ILS Law College Pune | Private | Maharashtra |
| 10 | NUJS Kolkata | Central | West Bengal |

### Science & Research — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IISc Bangalore | Central | Karnataka |
| 2 | IISER Pune | Central | Maharashtra |
| 3 | IISER Kolkata | Central | West Bengal |
| 4 | St. Stephen's Delhi | Private | Delhi |
| 5 | Presidency Kolkata | State Govt | West Bengal |
| 6 | Loyola Chennai | Private | Tamil Nadu |
| 7 | IISER Mohali | Central | Punjab |
| 8 | IISER Bhopal | Central | Madhya Pradesh |
| 9 | CMI Chennai | Private | Tamil Nadu |
| 10 | ISI Kolkata | Central | West Bengal |

### Commerce, Finance & Business — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IIM Ahmedabad | Central | Gujarat |
| 2 | IIM Bangalore | Central | Karnataka |
| 3 | IIM Calcutta | Central | West Bengal |
| 4 | SRCC Delhi | Central University | Delhi |
| 5 | ISB Hyderabad | Private | Telangana |
| 6 | FMS Delhi | Central University | Delhi |
| 7 | XLRI Jamshedpur | Private | Jharkhand |
| 8 | NMIMS Mumbai | Deemed | Maharashtra |
| 9 | IIM Lucknow | Central | Uttar Pradesh |
| 10 | LSR Delhi | Central University | Delhi |

### Education & Teaching — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | NCERT Delhi | Central | Delhi |
| 2 | LSR Education | Central University | Delhi |
| 3 | TISS Mumbai | Deemed | Maharashtra |
| 4 | Jamia Education | Central University | Delhi |
| 5 | BHU Education | Central University | Uttar Pradesh |
| 6 | RIE Mysore | Central | Karnataka |
| 7 | APU Bangalore | Private | Karnataka |
| 8 | CIE Delhi | Central University | Delhi |
| 9 | MSU Education | State Govt | Gujarat |
| 10 | DU Education | Central University | Delhi |

### Design & Creative Arts — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | NID Ahmedabad | Central | Gujarat |
| 2 | IIT Bombay IDC | IIT | Maharashtra |
| 3 | NIFT Delhi | Central | Delhi |
| 4 | Srishti Manipal | Private | Karnataka |
| 5 | MIT ID Pune | Private | Maharashtra |
| 6 | IIT Hyderabad Design | IIT | Telangana |
| 7 | NID Gandhinagar | Central | Gujarat |
| 8 | Pearl Academy | Private | Delhi |
| 9 | SID Pune | Deemed | Maharashtra |
| 10 | LPU Design | Private | Punjab |

### Arts & Humanities — Top 10 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | JNU Delhi | Central University | Delhi |
| 2 | DU Arts | Central University | Delhi |
| 3 | Jadavpur University | State Govt | West Bengal |
| 4 | Ashoka Sonipat | Private | Haryana |
| 5 | Presidency Arts | State Govt | West Bengal |
| 6 | BHU Arts | Central University | Uttar Pradesh |
| 7 | AMU Arts | Central University | Uttar Pradesh |
| 8 | Fergusson Pune | Private | Maharashtra |
| 9 | Loyola Arts | Private | Tamil Nadu |
| 10 | Christ Arts Bangalore | Deemed | Karnataka |

### Performing & Fine Arts — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | NSD Delhi | Central | Delhi |
| 2 | FTII Pune | Central | Maharashtra |
| 3 | SRFTI Kolkata | Central | West Bengal |
| 4 | DU Fine Arts | Central University | Delhi |
| 5 | Kalakshetra Chennai | Central | Tamil Nadu |

### Sports & Physical Education — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | LNIPE Gwalior | Central | Madhya Pradesh |
| 2 | SAI NSNIS Patiala | Central | Punjab |
| 3 | IGIPESS Delhi | State Govt | Delhi |
| 4 | TNPESU Chennai | State Govt | Tamil Nadu |
| 5 | GNDU Sports | State Govt | Punjab |

### Civil Services & Government — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | LBSNAA Mussoorie | Central | Uttarakhand |
| 2 | NPA Hyderabad | Central | Telangana |
| 3 | IIPA Delhi | Central | Delhi |
| 4 | JNU SIS | Central University | Delhi |
| 5 | NDC Delhi | Defence | Delhi |

### Hospitality, Travel & Tourism — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IHM Delhi | Central | Delhi |
| 2 | IHM Mumbai | Central | Maharashtra |
| 3 | WGSHA Manipal | Private | Karnataka |
| 4 | Christ Hospitality | Deemed | Karnataka |
| 5 | IHM Bangalore | Central | Karnataka |

### Agriculture & Environmental Studies — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | IARI Delhi | Central | Delhi |
| 2 | TNAU Coimbatore | State Govt | Tamil Nadu |
| 3 | PAU Ludhiana | State Govt | Punjab |
| 4 | GBPUAT Pantnagar | State Govt | Uttarakhand |
| 5 | UAS Bangalore | State Govt | Karnataka |

### Defence & Military — Top 5 India

| # | College | Type | State |
|---|---------|------|-------|
| 1 | NDA Pune | Defence | Maharashtra |
| 2 | IMA Dehradun | Defence | Uttarakhand |
| 3 | AFMC Pune | Defence | Maharashtra |
| 4 | INA Ezhimala | Defence | Kerala |
| 5 | AFA Dundigal | Defence | Telangana |

## Page Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Navbar: Dashboard | Career Options | Colleges | State Guide   │
├─────────────────────────────────────────────────────────────────┤
│  College Directory                                              │
│  Explore colleges, branches, cutoffs, and placements            │
│                                                                 │
│  🔍 Search: [___________________________]                      │
│                                                                 │
│  Filters:                                                       │
│  [Stream ▼] [State ▼] [Type ▼] [Branch ▼]                     │
│  [Fees Range ▼] [Course Type ▼] [Sort By ▼]                   │
│  [Compare Selected (0/3)]  [Reset Filters]                     │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ ☐ IIT Bombay                              NIRF #3       │  │
│  │   Mumbai, Maharashtra | IIT | Est. 1958                  │  │
│  │   Branches: CSE | EE | ME | CE | CH | AE | EP | MnC     │  │
│  │   Courses: B.Tech | Dual Degree | M.Tech | MS | PhD     │  │
│  │   Fees: ₹2.5 LPA | Placement: ₹21 LPA | NAAC: A++      │  │
│  │   [View Details ↗]                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  College Detail (expanded):                                     │
│  [Overview | Branches | Courses | Cutoffs |                    │
│   Placements | Scholarships | Reservation]                     │
│                                                                 │
│  Compare View (modal): Side-by-side for up to 3 colleges       │
└─────────────────────────────────────────────────────────────────┘
```

## Filter Specifications

| Filter | Type | Options |
|--------|------|---------|
| Stream | Dropdown | Engineering, Medical, IIIT (Phase 1), all 14 later |
| State | Dropdown | All 33 states/UTs |
| Institute Type | Multi-select | IIT, NIT, IIIT, State Govt, Private, Deemed, Central, AIIMS |
| Branch | Dropdown | Dynamic based on stream |
| Course Type | Multi-select | B.Tech, M.Tech, Dual, MBBS, MD, PhD, etc. |
| Fees Range | Range slider | ₹0 — ₹25 LPA |
| NIRF Ranking | Range slider | 1 — 200 |
| Sort By | Dropdown | NIRF Rank, Fees, Placement, Seats, Cutoff |

## Technical Implementation

### Files to Create

| File | Purpose |
|------|---------|
| `src/careerguide/data/college_data.py` | Full college data — branches, courses, cutoffs |
| `src/careerguide/templates/colleges.html` | Directory page with filters, cards, detail, compare |

### Files to Modify

| File | Change |
|------|--------|
| `src/careerguide/models/career.py` | Add `Branch`, `CourseType` models; enhance `College` |
| `src/careerguide/data/__init__.py` | Export college accessor functions |
| `src/careerguide/routes/pages.py` | Add `GET /colleges` page route + `GET /api/colleges` JSON API |
| `src/careerguide/templates/base.html` | Add "Colleges" navbar link |
| `src/careerguide/static/css/style.css` | College directory styles |
| `src/careerguide/static/js/main.js` | Client-side filter, search, compare logic |

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `GET /colleges` | HTML | Full page render |
| `GET /api/colleges?stream=...&state=...` | JSON | Filtered list for client-side |

## Data Volume

| Item | Estimate |
|------|----------|
| Total colleges (all 14 streams) | 168 |
| Engineering + IIIT | 53 (23 + 30) |
| Medical | 25 |
| Law, Science, Commerce, Education, Design, Arts | 10 each (60) |
| Performing Arts, Sports, Civil Services, Hospitality, Agriculture, Defence | 5 each (30) |
| Branches per college (avg) | ~3-4 |
| `college_data.py` estimated size | ~250 KB |

## Cutoff Data Methodology

- **Source:** JoSAA (Engineering), MCC (Medical) official closing ranks
- **Year:** Latest available (2025)
- **Categories:** General, OBC-NCL, SC, ST, EWS, Female (supernumerary)
- **Round:** Last round closing ranks
- **Updated:** Annually (static data refresh)

## Future Enhancements (Post Phase 3)

- Individual college pages (`/colleges/iit-bombay`) with SEO
- **Admission Predictor** — "Enter your JEE rank → See colleges/branches you qualify for"
- Student reviews and ratings
- Live cutoff updates during counselling season
- College recommendation from student profile (psychology + marks + interests)
