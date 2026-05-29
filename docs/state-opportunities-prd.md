# State-Specific Career Opportunities — PRD

## Problem Statement

Career opportunities, government schemes, scholarships, and job markets differ significantly by state in India. A student in Bihar has very different options compared to one in Karnataka or Tamil Nadu. Currently, the CareerGuide portal has state-level college data but lacks state-specific career information, government schemes, industry data, and job market insights.

Students struggle with:
- Not knowing what industries and job opportunities exist in their own state
- Missing state-specific government scholarships they are eligible for
- Unaware of state PSC exams and government job opportunities
- Not knowing about local industry clusters, IT parks, and SEZs near them
- Missing information about their state's startup ecosystem and incubators
- Not knowing about state-specific youth welfare schemes

## Solution

Add a dedicated **"State Guide"** page (`/stateopportunities`) that provides comprehensive state-specific career guidance for all 33 Indian states and union territories. Students select their state and instantly get localized information across 6 key areas.

## States & Union Territories Covered (33 total)

| # | State/UT | Major Industries | PSC Body |
|---|----------|-----------------|----------|
| 1 | Andhra Pradesh | IT, Pharma, Aquaculture, Automobiles | APPSC |
| 2 | Arunachal Pradesh | Hydropower, Tourism, Handicrafts, Forestry | APPSC |
| 3 | Assam | Tea, Oil & Gas, Silk, Tourism | APSC |
| 4 | Bihar | Agriculture, Dairy, IT (Patna), Education | BPSC |
| 5 | Chhattisgarh | Steel, Mining (Coal/Iron), Power, Rice | CGPSC |
| 6 | Goa | Tourism, Mining, Pharma, IT, Fisheries | Goa PSC |
| 7 | Gujarat | Petrochemicals, Textiles, Diamonds, Dairy, Ports | GPSC |
| 8 | Haryana | Automobiles (Gurugram), IT, Agriculture | HPSC |
| 9 | Himachal Pradesh | Tourism, Hydropower, Apple Farming, Pharma | HPPSC |
| 10 | Jharkhand | Mining (Coal/Iron/Mica), Steel, Forest Products | JPSC |
| 11 | Karnataka | IT/ITES (Bengaluru), Biotech, Aerospace, Coffee | KPSC |
| 12 | Kerala | Tourism, IT (Technopark), Rubber, Spices | Kerala PSC |
| 13 | Madhya Pradesh | Agriculture, Mining, Textiles, Tourism, IT | MPPSC |
| 14 | Maharashtra | Finance (Mumbai), IT (Pune), Film, Auto, Pharma | MPSC |
| 15 | Manipur | Handloom, Bamboo, Tourism, Horticulture | MPSC Manipur |
| 16 | Meghalaya | Mining, Tourism, Agriculture, Handloom | MPSC Meghalaya |
| 17 | Mizoram | Bamboo, Tourism, Horticulture, Handloom | MPSC Mizoram |
| 18 | Nagaland | Tourism, Handicrafts, Forest Products, Oil | NPSC |
| 19 | Odisha | Steel, Mining, IT (Bhubaneswar), Handloom | OPSC |
| 20 | Punjab | Agriculture, Textiles (Ludhiana), Sports goods, Dairy | PPSC |
| 21 | Rajasthan | Tourism, Mining (Marble), Textiles, Handicrafts | RPSC |
| 22 | Sikkim | Tourism, Organic Farming, Hydropower, Cardamom | SPSC |
| 23 | Tamil Nadu | Automobiles (Chennai), IT, Textiles, Leather, Film | TNPSC |
| 24 | Telangana | IT/ITES (Hyderabad), Pharma, Biotech, Defence | TSPSC |
| 25 | Tripura | Rubber, Tea, Bamboo, Handloom, Tourism | TPSC |
| 26 | Uttar Pradesh | Agriculture, IT (Noida), Handicrafts, Sugar | UPPSC |
| 27 | Uttarakhand | Tourism, IT (Dehradun), AYUSH, Hydropower | UKPSC |
| 28 | West Bengal | IT (Kolkata), Jute, Steel, Tea, Leather, Film | WBPSC |
| 29 | Delhi | IT, Finance, Media, Govt/PSU HQs, Startups | DSSSB |
| 30 | Chandigarh | IT, Pharma, Education, Govt Services | UT Administration |
| 31 | Puducherry | Tourism, Leather, Textiles, IT, Fisheries | UT Administration |
| 32 | Jammu & Kashmir | Tourism, Handicrafts, Horticulture (Apple/Saffron) | JKPSC |
| 33 | Ladakh | Tourism, Defence, Renewable Energy, Pashmina | UT Administration |

## Data Structure (per state)

Each state entry contains **6 sections**:

### 1. Job Market Snapshot
- Major cities for employment
- Top sectors with growth outlook, market share, and average salary
- Key IT parks, industrial areas, and SEZs
- Approximate unemployment rate and average entry-level salary

### 2. State Government Scholarships
- 4-6 state-specific scholarships
- Each with: name, department, amount, eligibility criteria, website/apply link

### 3. State PSC & Government Jobs
- PSC body name and website
- Major exams (KAS/PCS/FDA/SDA equivalents): posts, eligibility, age limit
- Other state-level recruiters (transport, police, banks, etc.)

### 4. Industry Clusters & SEZs
- 3-5 major industry clusters per state
- Each with: name, type/sector, major companies, job potential, relevant career streams

### 5. Startup Ecosystem
- State startup ranking (DPIIT)
- Number of registered startups
- Notable startups/unicorns from the state
- Incubators and accelerators
- State startup policy and funding schemes

### 6. Key Government Schemes for Youth
- 3-5 state + central schemes applicable to youth
- Each with: scheme name, benefit, eligibility, website

## Page Layout

```
┌─────────────────────────────────────────────────────────────┐
│  Navbar: Dashboard | Career Options | State Guide | ...     │
├─────────────────────────────────────────────────────────────┤
│  State-Specific Career Opportunities                        │
│  Discover career opportunities, scholarships, and schemes   │
│                                                             │
│  [Select State ▼ Karnataka                            ]     │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ 💼 Job Market │ 🎓 Scholarships │ 🏛️ Govt Jobs │     │ │
│  │ 🏭 Industry   │ 🚀 Startups    │ 📋 Schemes   │     │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │                                                        │ │
│  │  [Tab content — cards / tables / grids]                │ │
│  │                                                        │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Technical Implementation

### Files to Create
| File | Purpose |
|------|---------|
| `src/careerguide/data/state_data.py` | All 33 state entries with 6 sections each |
| `src/careerguide/templates/state_opportunities.html` | Page template with state dropdown + 6 tabs |

### Files to Modify
| File | Change |
|------|--------|
| `src/careerguide/data/__init__.py` | Export `get_state_data()`, `get_all_states()` |
| `src/careerguide/routes/pages.py` | Add `/stateopportunities` page route |
| `src/careerguide/templates/base.html` | Add "State Guide" link in navbar |
| `src/careerguide/static/css/style.css` | Add state-specific CSS classes |

### Route
- `GET /stateopportunities` — renders the State Guide page with all state data pre-loaded

### Data Volume
- 33 states × 6 sections × ~5 items per section ≈ 990 data entries
- Estimated `state_data.py` size: ~80-100 KB
