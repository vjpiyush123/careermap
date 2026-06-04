"""State-specific career opportunities data for all Indian states and UTs."""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════════════════
# STATE OPPORTUNITIES DATA — 33 States & Union Territories
# ═══════════════════════════════════════════════════════════════════════════

_STATE_OPPORTUNITIES: dict[str, dict] = {
    # ───────────────────────────────────────────────────────────────────────
    # 1. ANDHRA PRADESH
    # ───────────────────────────────────────────────────────────────────────
    "Andhra Pradesh": {
        "job_market": {
            "major_cities": ["Visakhapatnam", "Vijayawada", "Tirupati", "Guntur", "Amaravati"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Vizag IT SEZ, fintech hub growing"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Major pharma manufacturing hub"},
                {"sector": "Aquaculture & Fisheries", "growth": "Medium", "avg_salary": "₹3-8 LPA", "description": "Largest shrimp exporter in India"},
                {"sector": "Automobiles", "growth": "Medium", "avg_salary": "₹4-10 LPA", "description": "Kia Motors plant in Anantapur"},
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Rice, groundnut, cotton production"},
            ],
            "it_parks": ["Vizag IT SEZ", "Millennium Towers Vijayawada", "Rushikonda IT Hub"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "Jagananna Vidya Deevena", "department": "Dept of Higher Education", "amount": "Full tuition fee reimbursement", "eligibility": "Family income < ₹2.5 LPA, studying in AP", "website": "https://jnanabhumi.ap.gov.in"},
            {"name": "Jagananna Vasathi Deevena", "department": "Dept of Higher Education", "amount": "₹10,000-20,000/year for hostel/mess", "eligibility": "SC/ST/BC/EBC/Kapu/Minority students", "website": "https://jnanabhumi.ap.gov.in"},
            {"name": "AP Epass Scholarship", "department": "Social Welfare Dept", "amount": "₹10,000-35,000/year", "eligibility": "SC/ST/BC students, income < ₹2 LPA", "website": "https://apepass.cgg.gov.in"},
            {"name": "Pratibha Awards", "department": "Dept of School Education", "amount": "₹5,000-10,000 one-time", "eligibility": "10th/12th toppers from govt schools", "website": "https://cse.ap.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Andhra Pradesh Public Service Commission (APPSC)",
            "psc_website": "https://psc.ap.gov.in",
            "major_exams": [
                {"exam": "APPSC Group-I", "posts": "Deputy Collector, DSP, etc.", "eligibility": "Graduation", "age": "21-42"},
                {"exam": "APPSC Group-II", "posts": "Municipal Commissioner, Tahsildar", "eligibility": "Graduation", "age": "18-42"},
                {"exam": "Panchayat Secretary", "posts": "Village-level administration", "eligibility": "Graduation", "age": "18-42"},
            ],
            "other_recruiters": ["APSRTC", "AP Police", "AP Transco", "AP Genco", "APCOB"],
        },
        "industry_clusters": [
            {"name": "Vizag Pharma City", "type": "Pharmaceuticals", "companies": "Aurobindo, Hetero, Divis Labs", "jobs_potential": "High", "relevant_streams": ["Science", "Medical"]},
            {"name": "Sri City SEZ", "type": "Multi-sector", "companies": "Kellogg's, Colgate, Kobelco, Isuzu", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Tirupati Industrial Hub", "type": "Manufacturing", "companies": "Electronics, textiles, food processing", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging Startup Hub",
            "total_startups": "3,500+",
            "notable_startups": ["ePoise", "BiBox", "Aragen Life Sciences"],
            "incubators": ["T-Hub Vizag", "IIIT Sri City Incubator", "JNTU Innovation Hub"],
            "govt_schemes": [
                {"name": "AP Innovation Society", "benefit": "Seed funding up to ₹15 lakh, mentorship", "website": "https://apis.ap.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "YSR Nethanna Nestham", "benefit": "₹24,000/year for handloom weavers", "eligibility": "Registered handloom weavers", "website": "https://ysrnethanna.ap.gov.in"},
            {"name": "Jagananna Chedodu", "benefit": "₹10,000 for tailors, dhobis, barbers", "eligibility": "Traditional occupation workers", "website": "https://navasakam.ap.gov.in"},
            {"name": "YSR Kapu Nestham", "benefit": "₹15,000/year for Kapu women", "eligibility": "Kapu community women aged 45-60", "website": "https://ysrkapunestham.ap.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 2. ARUNACHAL PRADESH
    # ───────────────────────────────────────────────────────────────────────
    "Arunachal Pradesh": {
        "job_market": {
            "major_cities": ["Itanagar", "Naharlagun", "Pasighat", "Tawang", "Ziro"],
            "top_sectors": [
                {"sector": "Hydropower", "growth": "High", "avg_salary": "₹5-15 LPA", "description": "Massive untapped hydro potential"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹3-8 LPA", "description": "Eco-tourism, adventure tourism growing"},
                {"sector": "Handicrafts", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Traditional weaving, cane & bamboo"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-6 LPA", "description": "Kiwi, apple, orange, large cardamom"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Largest employer in the state"},
            ],
            "it_parks": ["Itanagar IT Park (proposed)"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "Pre-Matric Scholarship ST", "department": "Tribal Affairs Dept", "amount": "₹150-350/month + books", "eligibility": "ST students, class 1-10", "website": "https://scholarship.arunachal.gov.in"},
            {"name": "Post-Matric Scholarship ST", "department": "Tribal Affairs Dept", "amount": "₹230-1200/month", "eligibility": "ST students, class 11 onwards", "website": "https://scholarship.arunachal.gov.in"},
            {"name": "Chief Minister's Merit Scholarship", "department": "Education Dept", "amount": "₹50,000/year", "eligibility": "Top 10 in class 10/12 board exams", "website": "https://arunachaleducation.gov.in"},
            {"name": "Stipend for Technical Education", "department": "Technical Education Dept", "amount": "₹500-1500/month", "eligibility": "Students in polytechnic/ITI", "website": "https://arunachaleducation.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Arunachal Pradesh Public Service Commission (APPSC)",
            "psc_website": "https://appsc.gov.in",
            "major_exams": [
                {"exam": "APPSCCE (Combined Competitive)", "posts": "APCS, APS, Allied services", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "JE/AE Recruitment", "posts": "Junior/Assistant Engineers", "eligibility": "Diploma/B.Tech", "age": "18-35"},
                {"exam": "TGT/PGT", "posts": "Teachers Gr-I and II", "eligibility": "Graduation/PG with B.Ed", "age": "18-35"},
            ],
            "other_recruiters": ["APST", "AP Police", "Hydro Projects", "Forest Dept", "Health Dept"],
        },
        "industry_clusters": [
            {"name": "Banderdewa Industrial Area", "type": "Manufacturing", "companies": "Food processing, handicrafts", "jobs_potential": "Low", "relevant_streams": ["Commerce", "Arts"]},
            {"name": "Hydro Power Projects", "type": "Energy", "companies": "NHPC, NEEPCO, SJVN", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "100+",
            "notable_startups": ["Arunachal Orange", "Ziro Valley Organic"],
            "incubators": ["NIT Arunachal Incubation Centre", "NERIST Innovation Hub"],
            "govt_schemes": [
                {"name": "CM's Startup Scheme", "benefit": "Interest-free loans up to ₹20 lakh", "website": "https://arunachal.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Dulari Kanya", "benefit": "₹20,000 FD for girl child at birth", "eligibility": "Girl child born in Arunachal", "website": "https://wcd.arunachal.gov.in"},
            {"name": "Chief Minister's Arogya Arunachal Yojana", "benefit": "Health insurance up to ₹5 lakh", "eligibility": "All residents", "website": "https://cmaay.arunachal.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 3. ASSAM
    # ───────────────────────────────────────────────────────────────────────
    "Assam": {
        "job_market": {
            "major_cities": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Tezpur"],
            "top_sectors": [
                {"sector": "Tea Industry", "growth": "Stable", "avg_salary": "₹2-8 LPA", "description": "World's largest tea growing region"},
                {"sector": "Oil & Natural Gas", "growth": "Medium", "avg_salary": "₹6-20 LPA", "description": "ONGC, Oil India operations"},
                {"sector": "Silk & Handloom", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Muga, Eri, Pat silk production"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹3-8 LPA", "description": "Kaziranga, Majuli, river tourism"},
                {"sector": "IT & BPO", "growth": "High", "avg_salary": "₹3-10 LPA", "description": "Guwahati emerging as IT hub"},
            ],
            "it_parks": ["Guwahati IT Park", "Assam IT Hub Bongora"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "Pre-Matric Scholarship Minorities", "department": "Minority Welfare Dept", "amount": "₹100-500/month", "eligibility": "Minority students, class 1-10, income < ₹1 LPA", "website": "https://scholarships.assam.gov.in"},
            {"name": "Post-Matric Scholarship SC/ST", "department": "Welfare Dept", "amount": "₹230-1200/month", "eligibility": "SC/ST students, class 11+", "website": "https://scholarships.assam.gov.in"},
            {"name": "Pragati Scholarship (Girls)", "department": "AICTE via State", "amount": "₹50,000/year", "eligibility": "Girls in technical courses", "website": "https://scholarships.assam.gov.in"},
            {"name": "Anundoram Borooah Award", "department": "Education Dept", "amount": "Laptop/₹30,000", "eligibility": "1st division in HSLC from govt school", "website": "https://arbas.assam.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Assam Public Service Commission (APSC)",
            "psc_website": "https://apsc.nic.in",
            "major_exams": [
                {"exam": "APSC CCE", "posts": "ACS, APS, Allied Services", "eligibility": "Graduation", "age": "21-38"},
                {"exam": "APSC JE", "posts": "Junior Engineers PWD/PHE", "eligibility": "Diploma", "age": "21-38"},
                {"exam": "Assam TET", "posts": "Teachers LP/UP", "eligibility": "D.El.Ed/B.Ed", "age": "18-38"},
            ],
            "other_recruiters": ["ASTC", "Assam Police", "Oil India", "ONGC", "NRL", "Assam Gramin Vikash Bank"],
        },
        "industry_clusters": [
            {"name": "Guwahati Industrial Estate", "type": "Manufacturing", "companies": "FMCG, textiles, plastics", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Oil & Gas Belt (Upper Assam)", "type": "Energy", "companies": "ONGC, Oil India, NRL", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Tea Gardens (Dibrugarh-Jorhat)", "type": "Agriculture", "companies": "Tata Tea, McLeod Russel, Goodricke", "jobs_potential": "High", "relevant_streams": ["Agriculture", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Aspiring Leader (NE Leader)",
            "total_startups": "1,500+",
            "notable_startups": ["UrbanPiper", "KhaBi (food delivery)", "Assam Startup"],
            "incubators": ["IIT Guwahati TBI", "NIT Silchar Incubator", "Assam Startup Nest"],
            "govt_schemes": [
                {"name": "Assam Startup Policy 2017", "benefit": "Seed fund up to ₹20 lakh, 5-year tax holiday", "website": "https://startup.assam.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Orunodoi Scheme", "benefit": "₹1,250/month to women-headed families", "eligibility": "BPL families, woman head", "website": "https://orunodoi.assam.gov.in"},
            {"name": "Swami Vivekananda Assam Youth Empowerment", "benefit": "Skill training + placement", "eligibility": "Youth 18-40 years", "website": "https://svayem.assam.gov.in"},
            {"name": "Arundhati Gold Scheme", "benefit": "10g gold to brides", "eligibility": "Registered marriages, family income < ₹5 LPA", "website": "https://wcd.assam.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 4. BIHAR
    # ───────────────────────────────────────────────────────────────────────
    "Bihar": {
        "job_market": {
            "major_cities": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga"],
            "top_sectors": [
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Rice, wheat, maize, vegetables"},
                {"sector": "Education & Coaching", "growth": "High", "avg_salary": "₹3-10 LPA", "description": "Major UPSC/competitive exam hub"},
                {"sector": "Dairy & Food Processing", "growth": "Medium", "avg_salary": "₹2-6 LPA", "description": "Sudha dairy, litchi processing"},
                {"sector": "IT & BPO", "growth": "Emerging", "avg_salary": "₹3-8 LPA", "description": "Patna IT park development"},
                {"sector": "Tourism", "growth": "Medium", "avg_salary": "₹2-6 LPA", "description": "Buddhist circuit: Bodh Gaya, Nalanda"},
            ],
            "it_parks": ["Bihar IT Park Patna (under development)", "Software Technology Park Patna"],
            "avg_entry_salary": "₹2-3.5 LPA",
        },
        "scholarships": [
            {"name": "BC/EBC Post Matric Scholarship", "department": "BC/EBC Welfare Dept", "amount": "Full fee + ₹700/month", "eligibility": "BC/EBC students, income < ₹1.5 LPA", "website": "https://state.bihar.gov.in/bcebcwelfare"},
            {"name": "SC/ST Post Matric Scholarship", "department": "SC/ST Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST students, income < ₹2.5 LPA", "website": "https://pmsonline.bih.nic.in"},
            {"name": "Mukhyamantri Kanya Utthan Yojana", "department": "Women Development Dept", "amount": "₹25,000 on graduation", "eligibility": "Girls graduating from Bihar", "website": "https://ekalyan.bih.nic.in"},
            {"name": "Combined Counselling Board Scholarship", "department": "Education Dept", "amount": "Based on rank", "eligibility": "Engineering/medical admission merit", "website": "https://bceceboard.bihar.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Bihar Public Service Commission (BPSC)",
            "psc_website": "https://bpsc.bih.nic.in",
            "major_exams": [
                {"exam": "BPSC Combined Competitive Exam", "posts": "SDO, DSP, BAS, BPS", "eligibility": "Graduation", "age": "20-37"},
                {"exam": "BPSC TRE (Teacher)", "posts": "School Teachers 7-12", "eligibility": "PG + B.Ed/TET", "age": "21-37"},
                {"exam": "Bihar SI", "posts": "Sub Inspector Police", "eligibility": "Graduation", "age": "20-37"},
            ],
            "other_recruiters": ["BSRTC", "Bihar Police", "BSPHCL", "Bihar Gramin Bank", "Co-operative Banks"],
        },
        "industry_clusters": [
            {"name": "Hajipur Industrial Area", "type": "Manufacturing", "companies": "Britannia, Parle, food processing", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Muzaffarpur Litchi Cluster", "type": "Agro-processing", "companies": "Litchi processing, export units", "jobs_potential": "Seasonal", "relevant_streams": ["Agriculture", "Commerce"]},
            {"name": "Patna Dairy Belt", "type": "Dairy", "companies": "Sudha (Comfed), Mother Dairy", "jobs_potential": "Medium", "relevant_streams": ["Agriculture", "Science"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "800+",
            "notable_startups": ["Jeevtronics", "EasyGov", "Bihar Angika Innovative"],
            "incubators": ["Bihar Startup Fund", "IIT Patna Incubator", "Chandragupt Institute TBI"],
            "govt_schemes": [
                {"name": "Bihar Startup Policy 2017", "benefit": "Seed fund up to ₹10 lakh, 3-year tax exemption", "website": "https://startup.bihar.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Yuva Udyami Yojana", "benefit": "₹10 lakh loan at 1% interest for entrepreneurship", "eligibility": "Youth 18-40 years, 10th pass", "website": "https://udyami.bihar.gov.in"},
            {"name": "Bihar Student Credit Card", "benefit": "₹4 lakh education loan at 4% interest", "eligibility": "Class 12 passed, Bihar resident", "website": "https://7nishchay-yuvaupmission.bihar.gov.in"},
            {"name": "Kushal Yuva Program", "benefit": "Free soft skill + computer training", "eligibility": "Youth 15-28 years, 10th pass", "website": "https://skillmissionbihar.org"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 5. CHHATTISGARH
    # ───────────────────────────────────────────────────────────────────────
    "Chhattisgarh": {
        "job_market": {
            "major_cities": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Durg"],
            "top_sectors": [
                {"sector": "Steel & Mining", "growth": "Stable", "avg_salary": "₹4-15 LPA", "description": "Bhilai Steel Plant, NMDC"},
                {"sector": "Power & Energy", "growth": "Medium", "avg_salary": "₹5-12 LPA", "description": "Thermal plants, power surplus state"},
                {"sector": "Agriculture & Rice", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Rice bowl of India"},
                {"sector": "Cement", "growth": "Medium", "avg_salary": "₹4-10 LPA", "description": "UltraTech, ACC, Ambuja plants"},
                {"sector": "IT & BPO", "growth": "Emerging", "avg_salary": "₹3-8 LPA", "description": "Raipur IT corridor developing"},
            ],
            "it_parks": ["Naya Raipur IT Park", "STPI Raipur"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "Post Matric Scholarship SC", "department": "SC Welfare Dept", "amount": "Full fee + ₹380-1200/month", "eligibility": "SC students, income < ₹2.5 LPA", "website": "https://sw.cg.gov.in"},
            {"name": "Post Matric Scholarship ST", "department": "Tribal Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "ST students, income < ₹2.5 LPA", "website": "https://sw.cg.gov.in"},
            {"name": "OBC/Minority Scholarship", "department": "BC Welfare Dept", "amount": "₹5,000-15,000/year", "eligibility": "OBC/Minority, income < ₹1 LPA", "website": "https://sw.cg.gov.in"},
            {"name": "Chhattisgarh Merit Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-20,000/year", "eligibility": "Top performers in board exams", "website": "https://cgscholar.cg.nic.in"},
        ],
        "government_jobs": {
            "psc_name": "Chhattisgarh Public Service Commission (CGPSC)",
            "psc_website": "https://psc.cg.gov.in",
            "major_exams": [
                {"exam": "CGPSC State Services Exam", "posts": "Deputy Collector, DSP, etc.", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "CGPSC State Engineering Services", "posts": "Assistant Engineers", "eligibility": "B.Tech/B.E.", "age": "21-40"},
                {"exam": "CG Vyapam (Various)", "posts": "Teachers, Clerks, Patwari", "eligibility": "10+2/Graduation", "age": "18-40"},
            ],
            "other_recruiters": ["CSEB", "CSPGCL", "SAIL BSP", "NMDC", "SECL", "CG Police"],
        },
        "industry_clusters": [
            {"name": "Bhilai Steel City", "type": "Steel & Heavy Industry", "companies": "SAIL BSP, ancillary units", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Korba Power Hub", "type": "Power Generation", "companies": "NTPC, CSEB thermal plants", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Naya Raipur IT Hub", "type": "IT & Services", "companies": "TCS, Wipro, govt IT projects", "jobs_potential": "Growing", "relevant_streams": ["Engineering", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "600+",
            "notable_startups": ["36inc (incubator)", "AgriTech startups"],
            "incubators": ["36inc Raipur", "NIT Raipur Innovation Centre", "IIM Raipur Incubator"],
            "govt_schemes": [
                {"name": "CG Startup Policy 2019", "benefit": "Seed fund up to ₹25 lakh, reimbursements", "website": "https://startup.cg.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Rajiv Yuva Mitan Club", "benefit": "Youth club funding, skill development", "eligibility": "Youth groups 18-35", "website": "https://cgstate.gov.in"},
            {"name": "Mukhyamantri Yuva Swarozgar Yojana", "benefit": "₹15 lakh loan for business at subsidy", "eligibility": "Youth 18-35, 10th pass", "website": "https://industries.cg.gov.in"},
            {"name": "Godhan Nyay Yojana", "benefit": "₹2/kg for cow dung to farmers", "eligibility": "Cattle owners", "website": "https://godhannyay.cgstate.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 6. GOA
    # ───────────────────────────────────────────────────────────────────────
    "Goa": {
        "job_market": {
            "major_cities": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
            "top_sectors": [
                {"sector": "Tourism & Hospitality", "growth": "High", "avg_salary": "₹3-12 LPA", "description": "Beach tourism, casinos, MICE"},
                {"sector": "Mining", "growth": "Low", "avg_salary": "₹4-10 LPA", "description": "Iron ore (currently restricted)"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Syngene, Cipla, major pharma SEZ"},
                {"sector": "IT & Startups", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "IT parks and startup culture"},
                {"sector": "Fisheries", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Seafood processing, export"},
            ],
            "it_parks": ["Goa IT Park Dona Paula", "Electronic City Tuem"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "Post Matric Scholarship OBC", "department": "Social Welfare Dept", "amount": "Fee + maintenance", "eligibility": "OBC students, income < ₹1 LPA", "website": "https://egov.goa.nic.in"},
            {"name": "Dayanand Bandodkar Scholarship", "department": "Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Merit-based for Goa domiciles", "website": "https://dhe.goa.gov.in"},
            {"name": "Goa State SC/ST Scholarship", "department": "Tribal Welfare Dept", "amount": "Full fee coverage", "eligibility": "SC/ST students", "website": "https://www.goa.gov.in"},
            {"name": "Chief Minister's Education Loan Scheme", "department": "Education Dept", "amount": "Interest subsidy on education loans", "eligibility": "Students pursuing higher education", "website": "https://dhe.goa.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Goa Public Service Commission (GPSC)",
            "psc_website": "https://gpsc.goa.gov.in",
            "major_exams": [
                {"exam": "Goa Civil Services", "posts": "Deputy Collector, Mamlatdar", "eligibility": "Graduation", "age": "20-42"},
                {"exam": "GPSC AE/JE", "posts": "Engineers in PWD/WRD", "eligibility": "Diploma/B.Tech", "age": "18-42"},
                {"exam": "Staff Selection", "posts": "LDC, UDC, Assistants", "eligibility": "12th/Graduation", "age": "18-45"},
            ],
            "other_recruiters": ["Kadamba Transport", "Goa Police", "Goa Shipyard", "Tourism Dept", "Port Authority"],
        },
        "industry_clusters": [
            {"name": "Verna Industrial Estate", "type": "Pharma & Manufacturing", "companies": "Syngene, Cipla, Glenmark, Lupin", "jobs_potential": "High", "relevant_streams": ["Science", "Engineering"]},
            {"name": "Goa IT Hub Dona Paula", "type": "IT & BPO", "companies": "TCS, Persistent, startups", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Mormugao Port Cluster", "type": "Logistics & Shipping", "companies": "Port handling, shipping agencies", "jobs_potential": "Medium", "relevant_streams": ["Commerce", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Performer (small state leader)",
            "total_startups": "700+",
            "notable_startups": ["Alina Technologies", "Mojo Pizza origins", "GBS Tech"],
            "incubators": ["Startup Goa", "BITS Goa Incubator", "GIM Incubation Centre"],
            "govt_schemes": [
                {"name": "Goa Startup Policy 2017", "benefit": "Seed funding up to ₹50 lakh, mentorship", "website": "https://startup.goa.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Dayanand Samajik Suraksha Yojana", "benefit": "Pension for unemployed, disabled", "eligibility": "BPL families", "website": "https://dssy.goa.gov.in"},
            {"name": "Ladli Laxmi Scheme", "benefit": "₹1 lakh for girl child education", "eligibility": "Girls born after 2012", "website": "https://dwcd.goa.gov.in"},
            {"name": "Goa Skill Development Mission", "benefit": "Free skill training", "eligibility": "Youth 18-35", "website": "https://gsdm.goa.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 7. GUJARAT
    # ───────────────────────────────────────────────────────────────────────
    "Gujarat": {
        "job_market": {
            "major_cities": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "GIFT City"],
            "top_sectors": [
                {"sector": "Petrochemicals & Refining", "growth": "High", "avg_salary": "₹5-20 LPA", "description": "Reliance, Nayara, IOCL refineries"},
                {"sector": "Textiles & Diamonds", "growth": "Stable", "avg_salary": "₹3-10 LPA", "description": "Surat diamond hub, Ahmedabad textiles"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Zydus, Cadila, Sun Pharma"},
                {"sector": "Dairy (Amul)", "growth": "Stable", "avg_salary": "₹3-8 LPA", "description": "World's largest dairy cooperative"},
                {"sector": "Ports & Logistics", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Mundra, Pipavav, Kandla ports"},
                {"sector": "Automobiles", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Maruti, Tata, MG Motor plants"},
            ],
            "it_parks": ["GIFT City IFSC", "Infocity Gandhinagar", "SG Highway IT corridor", "GIDC Electronics Estate"],
            "avg_entry_salary": "₹3-6 LPA",
        },
        "scholarships": [
            {"name": "MYSY (Mukhyamantri Yuva Swavalamban Yojana)", "department": "Education Dept", "amount": "Up to ₹2 lakh/year for higher ed", "eligibility": "HSC pass, family income < ₹6 LPA", "website": "https://mysy.guj.nic.in"},
            {"name": "Post Matric Scholarship SC/ST", "department": "Social Justice Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST, income < ₹2.5 LPA", "website": "https://sje.gujarat.gov.in"},
            {"name": "Ganga Swaroop Scholarship (Girls)", "department": "Social Justice Dept", "amount": "₹500/month for school girls", "eligibility": "SC/ST/SEBC girls, Class 9-12", "website": "https://sje.gujarat.gov.in"},
            {"name": "Swami Vivekanand Stipend", "department": "Higher Education Dept", "amount": "₹1,200/month for EWS", "eligibility": "EWS students in higher ed", "website": "https://sje.gujarat.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Gujarat Public Service Commission (GPSC)",
            "psc_website": "https://gpsc.gujarat.gov.in",
            "major_exams": [
                {"exam": "GPSC Class 1 & 2", "posts": "Deputy Collector, DySP, etc.", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "GPSC Civil Services", "posts": "Administrative posts", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "Gujarat TET/TAT", "posts": "Primary/Secondary Teachers", "eligibility": "D.El.Ed/B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["GSRTC", "Gujarat Police", "GUVNL", "GNFC", "GSPC", "Gujarat Gas"],
        },
        "industry_clusters": [
            {"name": "GIFT City (Gandhinagar)", "type": "Finance & Fintech", "companies": "Banks, NSE, BSE, insurance, fintech", "jobs_potential": "Very High", "relevant_streams": ["Commerce", "Engineering"]},
            {"name": "Surat Diamond Bourse", "type": "Gems & Jewelry", "companies": "Diamond cutting, polishing, export", "jobs_potential": "High", "relevant_streams": ["Commerce", "Design"]},
            {"name": "Sanand Auto Hub", "type": "Automobile", "companies": "Tata Nano, Ford (closed), MG Motor", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Dahej & Hazira Petrochemical", "type": "Chemicals & Refining", "companies": "ONGC, IOCL, Reliance, OPAL", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Science"]},
        ],
        "startup_ecosystem": {
            "ranking": "Leader (Top 5 in India)",
            "total_startups": "10,000+",
            "notable_startups": ["Cygnet Infotech", "91Squarefeet", "Oizom"],
            "incubators": ["GUSEC (Gujarat University)", "iCreate", "AIC Pedestal", "IIM-A CIIE"],
            "govt_schemes": [
                {"name": "Gujarat Startup Policy 2022", "benefit": "Seed fund up to ₹30 lakh, IPR support", "website": "https://startupgujarat.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Garima Path Scheme", "benefit": "Interest-free loans for manual scavengers' children", "eligibility": "Children of manual scavengers", "website": "https://sje.gujarat.gov.in"},
            {"name": "Manav Garima Yojana", "benefit": "₹8,000-12,000 tool kit grant for artisans", "eligibility": "SC/ST/OBC artisans", "website": "https://sje.gujarat.gov.in"},
            {"name": "Vahali Dikri Yojana", "benefit": "₹1.1 lakh in 3 installments for girls", "eligibility": "First 2 girls in family", "website": "https://wcd.gujarat.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 8. HARYANA
    # ───────────────────────────────────────────────────────────────────────
    "Haryana": {
        "job_market": {
            "major_cities": ["Gurugram", "Faridabad", "Panipat", "Ambala", "Rohtak", "Hisar"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹6-30 LPA", "description": "Cyber City Gurugram - India's largest IT hub"},
                {"sector": "Automobiles", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Maruti, Hero, Honda plants"},
                {"sector": "Real Estate", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Gurugram, Faridabad development"},
                {"sector": "Textiles & Handloom", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Panipat textiles, Hisar cotton"},
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Wheat, rice, basmati, dairy"},
            ],
            "it_parks": ["Cyber City DLF Gurugram", "Cyber Hub", "Sohna Road IT corridor", "Faridabad NIT"],
            "avg_entry_salary": "₹4-8 LPA",
        },
        "scholarships": [
            {"name": "Haryana State Merit Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Top performers in board exams", "website": "https://haryana.gov.in"},
            {"name": "Post Matric SC Scholarship", "department": "Welfare Dept", "amount": "Full fee + ₹1,000/month", "eligibility": "SC students, income < ₹2.5 LPA", "website": "https://scholarship.haryana.gov.in"},
            {"name": "BC/EWS Scholarship", "department": "Welfare Dept", "amount": "₹6,000-12,000/year", "eligibility": "BC/EWS students", "website": "https://scholarship.haryana.gov.in"},
            {"name": "Dr. APJ Abdul Kalam Scholarship", "department": "Minorities Welfare", "amount": "₹10,000/year for technical courses", "eligibility": "Minority students in technical ed", "website": "https://minority.haryana.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Haryana Public Service Commission (HPSC)",
            "psc_website": "https://hpsc.gov.in",
            "major_exams": [
                {"exam": "HPSC HCS (Haryana Civil Services)", "posts": "SDM, DSP, Tehsildar", "eligibility": "Graduation", "age": "21-42"},
                {"exam": "HPSC AE/JE", "posts": "Engineers in Govt depts", "eligibility": "Diploma/B.Tech", "age": "18-42"},
                {"exam": "Haryana SSC (HSSC)", "posts": "Clerks, Patwari, Gram Sachiv", "eligibility": "10th/12th/Graduation", "age": "18-42"},
                {"exam": "HTET", "posts": "Teachers TGT/PGT", "eligibility": "B.Ed", "age": "18-42"},
            ],
            "other_recruiters": ["Haryana Roadways", "Haryana Police", "HSVP", "UHBVN", "DHBVN"],
        },
        "industry_clusters": [
            {"name": "Cyber City Gurugram", "type": "IT & Corporate HQs", "companies": "Google, Microsoft, Deloitte, Accenture, 500+ MNCs", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "IMT Manesar", "type": "Automobile & Manufacturing", "companies": "Maruti, Hero MotoCorp, Honda", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "Faridabad Industrial Area", "type": "Manufacturing", "companies": "FMCG, textiles, light engineering", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Panipat Textile Hub", "type": "Textiles & Handloom", "companies": "Home furnishing export units", "jobs_potential": "High", "relevant_streams": ["Design", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Leader (NCR Hub)",
            "total_startups": "7,000+",
            "notable_startups": ["Zomato", "PolicyBazaar", "MakeMyTrip (HQ moved)", "Cars24"],
            "incubators": ["T-Hub Gurugram", "91springboard", "WeWork Labs", "NASSCOM CoE"],
            "govt_schemes": [
                {"name": "Haryana Startup Policy 2022", "benefit": "Seed fund up to ₹50 lakh, rent subsidy, IP support", "website": "https://startupharyana.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Saksham Yuva Yojana", "benefit": "₹3,000/month to unemployed graduates while seeking job", "eligibility": "Graduate/PG, unemployed, income < ₹3 LPA", "website": "https://hreyahs.gov.in"},
            {"name": "Mukhyamantri Awas Yojana", "benefit": "₹3.5 lakh housing assistance", "eligibility": "BPL families in urban areas", "website": "https://hsfdc.gov.in"},
            {"name": "Meri Fasal Mera Byora", "benefit": "Direct farmer support, MSP payments", "eligibility": "Registered farmers", "website": "https://fasal.haryana.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 9. HIMACHAL PRADESH
    # ───────────────────────────────────────────────────────────────────────
    "Himachal Pradesh": {
        "job_market": {
            "major_cities": ["Shimla", "Dharamshala", "Solan", "Mandi", "Kullu"],
            "top_sectors": [
                {"sector": "Tourism & Hospitality", "growth": "High", "avg_salary": "₹3-10 LPA", "description": "Hill stations, adventure tourism"},
                {"sector": "Hydropower", "growth": "High", "avg_salary": "₹5-15 LPA", "description": "Major hydro projects"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Baddi pharma hub"},
                {"sector": "Horticulture", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Apple, stone fruits"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Major employer"},
            ],
            "it_parks": ["IT Park Shimla (proposed)", "Baddi Industrial Area"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "HP Post Matric Scholarship SC/ST/OBC", "department": "Social Justice Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST/OBC students", "website": "https://scholarship.hp.gov.in"},
            {"name": "Merit Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Top performers in board exams", "website": "https://hpedu.gov.in"},
            {"name": "Dr. Ambedkar Medhavi Scholarship", "department": "SC Welfare Dept", "amount": "₹10,000/year", "eligibility": "SC students scoring 60%+", "website": "https://scholarship.hp.gov.in"},
            {"name": "Indira Gandhi Utkrisht Scholarship", "department": "Education Dept", "amount": "₹10,000 one-time", "eligibility": "Girls in 10+2 science", "website": "https://hpedu.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Himachal Pradesh Public Service Commission (HPPSC)",
            "psc_website": "https://hppsc.hp.gov.in",
            "major_exams": [
                {"exam": "HPAS (HP Administrative Services)", "posts": "SDM, BDO, Tehsildar", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "HP TET", "posts": "Teachers", "eligibility": "B.Ed", "age": "18-45"},
                {"exam": "HP Allied Services", "posts": "Naib Tehsildar, Excise Inspector", "eligibility": "Graduation", "age": "21-35"},
            ],
            "other_recruiters": ["HRTC", "HP Police", "HPSEB", "HP Forest Dept", "HP Tourism"],
        },
        "industry_clusters": [
            {"name": "Baddi-Barotiwala-Nalagarh", "type": "Pharma & FMCG", "companies": "Dr. Reddy's, Cipla, Zydus, Dabur", "jobs_potential": "Very High", "relevant_streams": ["Science", "Engineering"]},
            {"name": "Shimla IT Hub", "type": "IT & BPO", "companies": "State IT projects", "jobs_potential": "Low", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "400+",
            "notable_startups": ["Himachal-origin agritech startups"],
            "incubators": ["IIT Mandi Catalyst", "HP University Incubator"],
            "govt_schemes": [
                {"name": "HP Startup Policy", "benefit": "Seed fund, mentorship", "website": "https://emerginghimachal.hp.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Sukh-Ashray Yojana", "benefit": "Support for orphans till age 27", "eligibility": "Orphan children", "website": "https://himachal.nic.in"},
            {"name": "Sahara Yojana", "benefit": "₹3,000/month for serious illness patients", "eligibility": "BPL patients with serious illness", "website": "https://sahara.hp.gov.in"},
            {"name": "Beti Hai Anmol Yojana", "benefit": "₹12,000 on birth + education support", "eligibility": "BPL families with girls", "website": "https://hpwcd.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 10. JHARKHAND
    # ───────────────────────────────────────────────────────────────────────
    "Jharkhand": {
        "job_market": {
            "major_cities": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
            "top_sectors": [
                {"sector": "Mining & Minerals", "growth": "Stable", "avg_salary": "₹4-15 LPA", "description": "Coal, iron, mica, uranium"},
                {"sector": "Steel & Heavy Industry", "growth": "Stable", "avg_salary": "₹5-18 LPA", "description": "Tata Steel, SAIL"},
                {"sector": "IT & Services", "growth": "Emerging", "avg_salary": "₹3-10 LPA", "description": "Ranchi IT development"},
                {"sector": "Forest Products", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Lac, timber, kendu leaves"},
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-4 LPA", "description": "Rice, vegetables"},
            ],
            "it_parks": ["IT Park Ranchi", "STPI Ranchi"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "e-Kalyan Scholarship SC/ST", "department": "Welfare Dept", "amount": "Full fee + ₹2,000/month", "eligibility": "SC/ST students, income < ₹2.5 LPA", "website": "https://ekalyan.jharkhand.gov.in"},
            {"name": "OBC/Minority Post Matric Scholarship", "department": "Welfare Dept", "amount": "₹5,000-15,000/year", "eligibility": "OBC/Minority students", "website": "https://ekalyan.jharkhand.gov.in"},
            {"name": "Guruji Credit Card Scheme", "department": "Higher Education Dept", "amount": "₹10 lakh education loan at 4%", "eligibility": "Jharkhand domicile students", "website": "https://jssc.jharkhand.gov.in"},
            {"name": "Chief Minister Fellowship", "department": "CM Office", "amount": "₹30,000/month fellowship", "eligibility": "Top graduates for district admin", "website": "https://jharkhand.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Jharkhand Public Service Commission (JPSC)",
            "psc_website": "https://jpsc.gov.in",
            "major_exams": [
                {"exam": "JPSC Combined Civil Services", "posts": "Deputy Collector, DSP", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "JPSC AE/JE", "posts": "Engineers", "eligibility": "B.Tech/Diploma", "age": "18-40"},
                {"exam": "JSSC CGL", "posts": "Clerks, Assistants", "eligibility": "Graduation", "age": "18-35"},
            ],
            "other_recruiters": ["Coal India (CCL, BCCL)", "Tata Steel", "SAIL", "JSEB", "Jharkhand Police"],
        },
        "industry_clusters": [
            {"name": "Jamshedpur Steel City", "type": "Steel & Heavy Industry", "companies": "Tata Steel, Tinplate, Tata Motors", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "Dhanbad Coal Belt", "type": "Mining", "companies": "BCCL, CCL, private mines", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Bokaro Steel City", "type": "Steel", "companies": "SAIL BSL", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "350+",
            "notable_startups": ["Jharkhand-origin mining tech startups"],
            "incubators": ["IIT ISM Dhanbad Incubator", "BIT Mesra Incubator"],
            "govt_schemes": [
                {"name": "Jharkhand Startup Policy 2016", "benefit": "Seed fund up to ₹25 lakh", "website": "https://startup.jharkhand.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Sukanya Yojana", "benefit": "₹40,000 for girl child education", "eligibility": "BPL girls completing Class 12", "website": "https://jharkhand.gov.in"},
            {"name": "Mukhyamantri Protsahan Yojana", "benefit": "₹5,000 for unemployed graduates annually", "eligibility": "Graduate, unemployed, Jharkhand domicile", "website": "https://rojgar.jharkhand.gov.in"},
            {"name": "Savitribai Phule Scholarship", "benefit": "₹2,500/year for tribal girls", "eligibility": "ST girl students class 9-12", "website": "https://ekalyan.jharkhand.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 11. KARNATAKA
    # ───────────────────────────────────────────────────────────────────────
    "Karnataka": {
        "job_market": {
            "major_cities": ["Bengaluru", "Mysuru", "Hubballi-Dharwad", "Mangaluru", "Belagavi"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹6-30 LPA", "description": "~38% of India's IT exports from Bengaluru"},
                {"sector": "Biotechnology", "growth": "High", "avg_salary": "₹5-18 LPA", "description": "60% of India's biotech industry"},
                {"sector": "Aerospace & Defence", "growth": "High", "avg_salary": "₹8-25 LPA", "description": "HAL, ISRO, DRDO, NAL"},
                {"sector": "Automobiles", "growth": "Medium", "avg_salary": "₹4-12 LPA", "description": "Toyota, TVS, Bosch"},
                {"sector": "Agriculture & Coffee", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "70% of India's coffee"},
            ],
            "it_parks": ["Electronic City", "Whitefield ITPL", "Manyata Tech Park", "Embassy Tech Village", "Bagmane Tech Park"],
            "avg_entry_salary": "₹4-8 LPA",
        },
        "scholarships": [
            {"name": "Vidyasiri Scholarship", "department": "BC Welfare Dept", "amount": "₹10,000-30,000/year", "eligibility": "OBC/SC/ST, income < ₹2.5 LPA", "website": "https://sw.kar.nic.in"},
            {"name": "Fee Reimbursement (Professional Courses)", "department": "Higher Education Dept", "amount": "Full tuition fee", "eligibility": "Cat-I, income < ₹1 LPA", "website": "https://karepass.cgg.gov.in"},
            {"name": "Sanchi Honnamma Scholarship", "department": "Women & Child Dept", "amount": "₹2,000/year for girls", "eligibility": "Girls in Class 1-10 from rural areas", "website": "https://kswcd.gov.in"},
            {"name": "Food & Accommodation Scholarship", "department": "Social Welfare Dept", "amount": "Free hostel + food", "eligibility": "SC/ST students in hostels", "website": "https://sw.kar.nic.in"},
        ],
        "government_jobs": {
            "psc_name": "Karnataka Public Service Commission (KPSC)",
            "psc_website": "https://kpsc.kar.nic.in",
            "major_exams": [
                {"exam": "KAS (Karnataka Administrative Service)", "posts": "Deputy Collector, DSP, Tahsildar", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "FDA/SDA", "posts": "First/Second Division Assistants", "eligibility": "Graduation/PUC", "age": "18-35"},
                {"exam": "Karnataka TET", "posts": "Primary/High School Teachers", "eligibility": "D.Ed/B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["KSRTC", "Karnataka Police", "BESCOM", "KPTCL", "Karnataka Bank"],
        },
        "industry_clusters": [
            {"name": "Electronic City Bengaluru", "type": "IT & Electronics", "companies": "Infosys, Wipro, TCS, Biocon", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Science"]},
            {"name": "Whitefield Tech Corridor", "type": "IT & Startups", "companies": "SAP, IBM, Oracle, startups", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Aerospace Cluster (HAL Belt)", "type": "Aerospace & Defence", "companies": "HAL, ISRO, NAL, DRDO labs", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Peenya Industrial Area", "type": "Manufacturing", "companies": "Engineering, textiles, food", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "#1 in India (DPIIT 2024)",
            "total_startups": "14,000+",
            "notable_startups": ["Flipkart", "Swiggy", "Meesho", "Razorpay", "Zerodha", "PhonePe", "Ola"],
            "incubators": ["NASSCOM 10K Startups", "IIM-B NSRCEL", "IISc Startup Hub", "T-Hub Bengaluru"],
            "govt_schemes": [
                {"name": "Karnataka Startup Policy 2022-27", "benefit": "Seed funding up to ₹50L, tax exemptions, free patents", "website": "https://startup.karnataka.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Yuva Nidhi", "benefit": "₹3,000-5,000/month for unemployed graduates", "eligibility": "Graduate/Diploma, 0-2 years since passing", "website": "https://sevasindhuservices.karnataka.gov.in"},
            {"name": "Anna Bhagya", "benefit": "Free 10kg rice/month", "eligibility": "BPL families", "website": "https://ahara.kar.nic.in"},
            {"name": "Gruha Lakshmi", "benefit": "₹2,000/month to women heads of family", "eligibility": "Women-headed households", "website": "https://sevasindhu.karnataka.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 12. KERALA
    # ───────────────────────────────────────────────────────────────────────
    "Kerala": {
        "job_market": {
            "major_cities": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kannur"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Technopark, Infopark, Cyberpark"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹3-10 LPA", "description": "Backwaters, Ayurveda tourism"},
                {"sector": "Healthcare & Ayurveda", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Medical tourism, hospitals"},
                {"sector": "Rubber & Spices", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Major producer"},
                {"sector": "Remittance Economy", "growth": "Stable", "avg_salary": "N/A", "description": "Gulf employment significant"},
            ],
            "it_parks": ["Technopark Trivandrum", "Infopark Kochi", "Cyberpark Kozhikode", "UL Cyberpark Kozhikode"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "E-Grantz (SC/ST/OBC)", "department": "Scheduled Castes Dev Dept", "amount": "₹10,000-50,000/year", "eligibility": "SC/ST/OBC students", "website": "https://egrantz.kerala.gov.in"},
            {"name": "State Merit Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Top performers in SSLC/Plus Two", "website": "https://dcescholarship.kerala.gov.in"},
            {"name": "Suvarna Jubilee Merit Scholarship", "department": "Higher Education Dept", "amount": "₹10,000-25,000/year", "eligibility": "Economically backward meritorious", "website": "https://dcescholarship.kerala.gov.in"},
            {"name": "PMS for Minorities", "department": "Minority Welfare Dept", "amount": "Fee + maintenance", "eligibility": "Minority students", "website": "https://minoritywelfare.kerala.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Kerala Public Service Commission (Kerala PSC)",
            "psc_website": "https://keralapsc.gov.in",
            "major_exams": [
                {"exam": "Kerala Administrative Service (KAS)", "posts": "Deputy Collector, Tahsildar", "eligibility": "Graduation", "age": "20-40"},
                {"exam": "LDC/LD Clerk", "posts": "Lower Division Clerks", "eligibility": "12th pass", "age": "18-36"},
                {"exam": "Kerala SET", "posts": "College Lecturers", "eligibility": "PG 55%+", "age": "No limit"},
            ],
            "other_recruiters": ["KSRTC", "Kerala Police", "KSEB", "FACT", "Cochin Shipyard"],
        },
        "industry_clusters": [
            {"name": "Technopark Trivandrum", "type": "IT & ITES", "companies": "TCS, Infosys, UST Global, IBS", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Infopark Kochi", "type": "IT & Electronics", "companies": "TCS, Wipro, Cognizant", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "KINFRA Kochi", "type": "Manufacturing & Electronics", "companies": "Electronics, food processing", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Kochi Port & Logistics", "type": "Shipping & Trade", "companies": "Cochin Port, Vallarpadam Terminal", "jobs_potential": "High", "relevant_streams": ["Commerce", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top Performer",
            "total_startups": "4,500+",
            "notable_startups": ["Open Financial", "Genrobotics", "SocialCops Kerala origins"],
            "incubators": ["Kerala Startup Mission", "NASSCOM CoE", "Maker Village Kochi", "IIM-K Incubator"],
            "govt_schemes": [
                {"name": "Kerala Startup Policy 2.0", "benefit": "Seed fund up to ₹25 lakh, innovation grants", "website": "https://startupmission.kerala.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "KASE (Kerala Academy for Skills Excellence)", "benefit": "Free skill training + placement", "eligibility": "Youth 18-35", "website": "https://kase.kerala.gov.in"},
            {"name": "Life Mission Housing", "benefit": "₹4 lakh for house construction", "eligibility": "Homeless BPL families", "website": "https://lifemission.kerala.gov.in"},
            {"name": "Snehapoorvam Scholarship", "benefit": "₹300-1,000/month for orphans", "eligibility": "Orphan students", "website": "https://swdprd.kerala.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 13. MADHYA PRADESH
    # ───────────────────────────────────────────────────────────────────────
    "Madhya Pradesh": {
        "job_market": {
            "major_cities": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
            "top_sectors": [
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Soybean, wheat, pulses"},
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹3-12 LPA", "description": "Indore IT hub emerging"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-8 LPA", "description": "Khajuraho, wildlife, heritage"},
                {"sector": "Textiles & Handloom", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Maheshwar, Chanderi saris"},
                {"sector": "Mining & Manufacturing", "growth": "Medium", "avg_salary": "₹3-10 LPA", "description": "Diamond, cement"},
            ],
            "it_parks": ["Crystal IT Park Indore", "STPI Bhopal", "STPI Indore"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "MP Post Matric Scholarship SC/ST", "department": "Tribal/SC Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST, income < ₹2.5 LPA", "website": "https://scholarshipportal.mp.nic.in"},
            {"name": "Gaon Ki Beti", "department": "Higher Education Dept", "amount": "₹500/month for 10 months", "eligibility": "Rural girls passing Class 12 with 60%+", "website": "https://scholarshipportal.mp.nic.in"},
            {"name": "Pratibha Kiran", "department": "Higher Education Dept", "amount": "₹500/month", "eligibility": "Urban BPL girls with 60%+ in Class 12", "website": "https://scholarshipportal.mp.nic.in"},
            {"name": "Vikramaditya Yojana", "department": "Higher Education Dept", "amount": "Fee waiver for graduation", "eligibility": "EWS students with 60%+ in Class 12", "website": "https://scholarshipportal.mp.nic.in"},
        ],
        "government_jobs": {
            "psc_name": "Madhya Pradesh Public Service Commission (MPPSC)",
            "psc_website": "https://mppsc.mp.gov.in",
            "major_exams": [
                {"exam": "MPPSC State Services Exam", "posts": "Deputy Collector, DSP", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "MPPSC State Forest Services", "posts": "Forest Ranger, ACF", "eligibility": "Graduation/B.Sc Forestry", "age": "21-40"},
                {"exam": "MP Vyapam (Various)", "posts": "Teachers, Clerks, Patwari", "eligibility": "10+2/Graduation", "age": "18-40"},
            ],
            "other_recruiters": ["MPSRTC", "MP Police", "MPPGCL", "MP Forest Dept", "MPEB"],
        },
        "industry_clusters": [
            {"name": "Pithampur Industrial Area", "type": "Automobile & Pharma", "companies": "Force Motors, Eicher, pharma units", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Indore Super Corridor", "type": "IT & Services", "companies": "TCS, Infosys, Impetus", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Mandideep Industrial Area", "type": "Manufacturing", "companies": "BHEL, engineering units", "jobs_potential": "Medium", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging (Top 10)",
            "total_startups": "2,000+",
            "notable_startups": ["Logistic Infotech", "Indore-origin startups"],
            "incubators": ["AIC Sangini", "IIT Indore Incubator", "IIM Indore Incubator"],
            "govt_schemes": [
                {"name": "MP Startup Policy 2022", "benefit": "Seed fund up to ₹20 lakh, incubation support", "website": "https://startup.mp.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Seekho Kamao Yojana", "benefit": "₹8,000-10,000/month stipend during training", "eligibility": "Youth 18-29, 12th pass", "website": "https://mmsky.mp.gov.in"},
            {"name": "Ladli Bahna Yojana", "benefit": "₹1,250/month to women", "eligibility": "Women 21-60, income < ₹2.5 LPA", "website": "https://ladlibahna.mp.gov.in"},
            {"name": "Mukhyamantri Udyam Kranti Yojana", "benefit": "₹1 crore loan for MSME at subsidy", "eligibility": "Entrepreneurs 18-40", "website": "https://samast.mponline.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 14. MAHARASHTRA
    # ───────────────────────────────────────────────────────────────────────
    "Maharashtra": {
        "job_market": {
            "major_cities": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Navi Mumbai"],
            "top_sectors": [
                {"sector": "Finance & Banking", "growth": "High", "avg_salary": "₹6-40 LPA", "description": "Mumbai - India's financial capital"},
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹5-25 LPA", "description": "Pune IT hub, Mumbai fintech"},
                {"sector": "Film & Entertainment", "growth": "High", "avg_salary": "₹3-50 LPA", "description": "Bollywood, OTT platforms"},
                {"sector": "Automobiles", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Pune-Nashik auto corridor"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Major pharma manufacturing"},
            ],
            "it_parks": ["Hinjewadi IT Park Pune", "SEEPZ Mumbai", "Mindspace Thane", "EON IT Park Pune", "Magarpatta City"],
            "avg_entry_salary": "₹4-8 LPA",
        },
        "scholarships": [
            {"name": "MahaDBT Scholarships (Various)", "department": "Social Justice Dept", "amount": "Fee + maintenance", "eligibility": "SC/ST/OBC/SBC/VJNT/Minority", "website": "https://mahadbt.maharashtra.gov.in"},
            {"name": "Rajarshi Chhatrapati Shahu Scholarship", "department": "Higher Education Dept", "amount": "Up to ₹2 lakh/year", "eligibility": "EWS students in professional courses", "website": "https://mahadbt.maharashtra.gov.in"},
            {"name": "Government of India PMS", "department": "Central via State", "amount": "Fee + ₹550-1200/month", "eligibility": "SC/ST/OBC/Minority students", "website": "https://mahadbt.maharashtra.gov.in"},
            {"name": "Dr. Panjabrao Deshmukh Scholarship", "department": "Agriculture Dept", "amount": "Full fee for agriculture courses", "eligibility": "EWS students in agriculture", "website": "https://mahadbt.maharashtra.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Maharashtra Public Service Commission (MPSC)",
            "psc_website": "https://mpsc.gov.in",
            "major_exams": [
                {"exam": "MPSC State Services Exam", "posts": "Deputy Collector, DSP, Tahsildar", "eligibility": "Graduation", "age": "19-38"},
                {"exam": "MPSC Engineering Services", "posts": "Assistant Engineers", "eligibility": "B.E./B.Tech", "age": "19-38"},
                {"exam": "Maharashtra SET", "posts": "Assistant Professors", "eligibility": "PG 55%+", "age": "No limit"},
            ],
            "other_recruiters": ["MSRTC", "Mumbai Police", "Maharashtra Police", "MSEDCL", "MHADA", "BMC"],
        },
        "industry_clusters": [
            {"name": "Hinjewadi IT Park Pune", "type": "IT & ITES", "companies": "Infosys, Wipro, TCS, Cognizant, 200+ companies", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "BKC Mumbai", "type": "Finance & Corporate HQs", "companies": "Banks, MNCs, consulting firms", "jobs_potential": "Very High", "relevant_streams": ["Commerce", "Law"]},
            {"name": "MIDC Chakan-Talegaon", "type": "Automobile", "companies": "Volkswagen, Mercedes, GM, Mahindra", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "JNPT & Nhava Sheva", "type": "Ports & Logistics", "companies": "Container shipping, logistics", "jobs_potential": "High", "relevant_streams": ["Commerce", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "#2 in India",
            "total_startups": "15,000+",
            "notable_startups": ["Zomato (origins)", "Dream11", "Shaadi.com", "BookMyShow", "Nykaa"],
            "incubators": ["SINE IIT Bombay", "Venture Center Pune", "CIIE.CO IIM-A", "91springboard"],
            "govt_schemes": [
                {"name": "Maharashtra Startup Policy 2023", "benefit": "Seed fund up to ₹50 lakh, reimbursements", "website": "https://startup.maharashtra.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Majhi Kanya Bhagyashree", "benefit": "₹50,000-1 lakh for girls' education", "eligibility": "One/two girl child families", "website": "https://womenchild.maharashtra.gov.in"},
            {"name": "MJPJAY (Health Insurance)", "benefit": "₹1.5 lakh/year health cover", "eligibility": "BPL and yellow ration card holders", "website": "https://www.jeevandayee.gov.in"},
            {"name": "Chief Minister Employment Scheme", "benefit": "Subsidy on loans for business", "eligibility": "Youth 18-45, 7th pass", "website": "https://cmegp.maharashtra.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 15. MANIPUR
    # ───────────────────────────────────────────────────────────────────────
    "Manipur": {
        "job_market": {
            "major_cities": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur"],
            "top_sectors": [
                {"sector": "Handloom & Handicrafts", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Traditional weaving, cane & bamboo"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-6 LPA", "description": "Loktak Lake, Sangai festival"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-4 LPA", "description": "Passion fruit, pineapple"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Major employer"},
                {"sector": "Sports & Fitness", "growth": "Medium", "avg_salary": "₹2-8 LPA", "description": "Powerhouse of sports talent"},
            ],
            "it_parks": ["Proposed IT Park Imphal"],
            "avg_entry_salary": "₹2-3.5 LPA",
        },
        "scholarships": [
            {"name": "Pre-Matric Scholarship ST", "department": "Tribal Affairs Dept", "amount": "₹150-350/month", "eligibility": "ST students, class 1-10", "website": "https://manipur.gov.in"},
            {"name": "Post-Matric Scholarship ST/SC", "department": "Tribal/SC Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "ST/SC students", "website": "https://manipur.gov.in"},
            {"name": "Chief Minister's Merit Scholarship", "department": "Education Dept", "amount": "₹25,000/year", "eligibility": "Top performers in HSLC/HSSLC", "website": "https://manipureducation.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC via State", "amount": "₹10,000-30,000/year", "eligibility": "NE students in higher ed", "website": "https://necouncil.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Manipur Public Service Commission (MPSC Manipur)",
            "psc_website": "https://mpscmanipur.gov.in",
            "major_exams": [
                {"exam": "Manipur Civil Services", "posts": "SDO, DSP, Extra Asst Commissioner", "eligibility": "Graduation", "age": "21-38"},
                {"exam": "MCS Judicial", "posts": "Civil Judge", "eligibility": "LLB", "age": "23-35"},
                {"exam": "Combined Graduate Level", "posts": "Assistants, Inspectors", "eligibility": "Graduation", "age": "18-38"},
            ],
            "other_recruiters": ["Manipur Police", "MSRTC", "Manipur State Power", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Imphal Industrial Estate", "type": "Light Manufacturing", "companies": "Food processing, handicrafts", "jobs_potential": "Low", "relevant_streams": ["Commerce", "Design"]},
            {"name": "Handloom Clusters", "type": "Textiles", "companies": "Traditional weaving units, cooperatives", "jobs_potential": "Medium", "relevant_streams": ["Design", "Arts"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "100+",
            "notable_startups": ["Handloom e-commerce startups"],
            "incubators": ["MSME DI Imphal", "NIT Manipur Incubation"],
            "govt_schemes": [
                {"name": "Start-Up Manipur", "benefit": "Seed fund, mentorship", "website": "https://startupmanipur.mn.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Chief Minister's Health for All", "benefit": "₹2 lakh health coverage", "eligibility": "All residents", "website": "https://health.mn.gov.in"},
            {"name": "Lairik Yenjin Thokpa (Free Education)", "benefit": "Free textbooks and uniforms", "eligibility": "Govt school students", "website": "https://manipureducation.gov.in"},
            {"name": "Ima Market Loan Scheme", "benefit": "₹50,000 interest-free loan for women vendors", "eligibility": "Women vendors at Ima Keithel", "website": "https://manipur.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 16. MEGHALAYA
    # ───────────────────────────────────────────────────────────────────────
    "Meghalaya": {
        "job_market": {
            "major_cities": ["Shillong", "Tura", "Jowai", "Nongstoin"],
            "top_sectors": [
                {"sector": "Mining (Coal/Limestone)", "growth": "Low", "avg_salary": "₹3-8 LPA", "description": "Regulated due to NGT orders"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-7 LPA", "description": "Living root bridges, Cherrapunji"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Strawberry, turmeric, ginger"},
                {"sector": "Handloom & Handicrafts", "growth": "Medium", "avg_salary": "₹2-4 LPA", "description": "Khasi, Garo textiles"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Major employer"},
            ],
            "it_parks": ["Shillong Technology Park"],
            "avg_entry_salary": "₹2-3.5 LPA",
        },
        "scholarships": [
            {"name": "Umbrella Scholarship ST", "department": "Tribal Welfare Dept", "amount": "Full fee + ₹380-1200/month", "eligibility": "ST students", "website": "https://meghalaya.gov.in/schemes"},
            {"name": "SC Post Matric Scholarship", "department": "Social Welfare Dept", "amount": "Fee + maintenance", "eligibility": "SC students, income < ₹2.5 LPA", "website": "https://megsocialwelfare.gov.in"},
            {"name": "State Merit Scholarship", "department": "Education Dept", "amount": "₹10,000/year", "eligibility": "Top performers in Class 10/12", "website": "https://megeducation.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC", "amount": "₹10,000-30,000/year", "eligibility": "NE students in professional courses", "website": "https://necouncil.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Meghalaya Public Service Commission (MPSC Meghalaya)",
            "psc_website": "https://mpsc.nic.in",
            "major_exams": [
                {"exam": "Meghalaya Civil Services", "posts": "MCS, MPS, Allied Services", "eligibility": "Graduation", "age": "21-32"},
                {"exam": "Lower Division Assistant", "posts": "LDA in depts", "eligibility": "12th pass", "age": "18-27"},
                {"exam": "Combined Technical Services", "posts": "JE, AE", "eligibility": "Diploma/B.Tech", "age": "18-32"},
            ],
            "other_recruiters": ["MTC (Transport)", "Meghalaya Police", "MeSEB", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Byrnihat Industrial Area", "type": "Manufacturing & Food Processing", "companies": "Cement, food processing", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Mendipathar (Garo Hills)", "type": "Mining & Processing", "companies": "Limestone, cement", "jobs_potential": "Medium", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "150+",
            "notable_startups": ["Tourism-tech, agritech startups"],
            "incubators": ["Meghalaya Basin Development Authority", "IIM Shillong Incubator"],
            "govt_schemes": [
                {"name": "Meghalaya Startup Policy", "benefit": "Seed fund, incubation support", "website": "https://meghalaya.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Chief Minister's Social Assistance", "benefit": "₹700/month pension to elderly/disabled", "eligibility": "Elderly, disabled, widows", "website": "https://megsocialwelfare.gov.in"},
            {"name": "Meghalaya Youth Policy", "benefit": "Skill training, sports support", "eligibility": "Youth 15-35", "website": "https://dyas.meghalaya.gov.in"},
            {"name": "Focus Meghalaya", "benefit": "Livelihood support, enterprise fund", "eligibility": "Youth entrepreneurs", "website": "https://mbda.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 17. MIZORAM
    # ───────────────────────────────────────────────────────────────────────
    "Mizoram": {
        "job_market": {
            "major_cities": ["Aizawl", "Lunglei", "Champhai", "Serchhip"],
            "top_sectors": [
                {"sector": "Bamboo Industry", "growth": "High", "avg_salary": "₹2-6 LPA", "description": "Bamboo products, construction"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-6 LPA", "description": "Eco-tourism, adventure tourism"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-4 LPA", "description": "Anthurium, passion fruit, grapes"},
                {"sector": "Handloom", "growth": "Stable", "avg_salary": "₹2-4 LPA", "description": "Traditional Mizo textiles"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Primary employer"},
            ],
            "it_parks": ["Proposed Electronic Manufacturing Cluster"],
            "avg_entry_salary": "₹2-3 LPA",
        },
        "scholarships": [
            {"name": "Post Matric Scholarship ST", "department": "Tribal Affairs", "amount": "Full fee + maintenance", "eligibility": "ST students", "website": "https://mizoram.gov.in"},
            {"name": "State Merit Scholarship", "department": "Education Dept", "amount": "₹10,000/year", "eligibility": "Top performers in HSLC/HSSLC", "website": "https://sedmizoram.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC", "amount": "₹10,000-30,000/year", "eligibility": "NE students in higher ed", "website": "https://necouncil.gov.in"},
            {"name": "Professional Course Stipend", "department": "Higher Education Dept", "amount": "₹500-1000/month", "eligibility": "Students in professional courses", "website": "https://dhe.mizoram.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Mizoram Public Service Commission (MPSC Mizoram)",
            "psc_website": "https://mpsc.mizoram.gov.in",
            "major_exams": [
                {"exam": "Mizoram Civil Services", "posts": "MCS, MPS officers", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "Lower Division Clerk", "posts": "LDC in departments", "eligibility": "12th pass", "age": "18-30"},
                {"exam": "JE/AE Technical", "posts": "Junior/Asst Engineers", "eligibility": "Diploma/B.Tech", "age": "18-35"},
            ],
            "other_recruiters": ["Mizoram Police", "MST (Transport)", "Zoram Energy", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Lengte Industrial Estate", "type": "Light Manufacturing", "companies": "Food processing, handicrafts", "jobs_potential": "Low", "relevant_streams": ["Commerce", "Agriculture"]},
            {"name": "Bamboo Processing Units", "type": "Bamboo Products", "companies": "Furniture, handicrafts, incense sticks", "jobs_potential": "Medium", "relevant_streams": ["Design", "Agriculture"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "80+",
            "notable_startups": ["Agri-tech, handloom e-commerce"],
            "incubators": ["Mizoram University Incubation Centre", "NIT Mizoram"],
            "govt_schemes": [
                {"name": "New Economic Development Policy", "benefit": "Support for startups, MSMEs", "website": "https://mizoram.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Socio-Economic Development Policy (SEDP)", "benefit": "Enterprise loans, subsidies", "eligibility": "Youth entrepreneurs", "website": "https://mizoram.gov.in"},
            {"name": "Chief Minister's Scholarship", "benefit": "₹10,000 for meritorious students", "eligibility": "Top performers", "website": "https://sedmizoram.gov.in"},
            {"name": "Mizo Hmeichhe Tan", "benefit": "Financial assistance to women SHGs", "eligibility": "Women's self-help groups", "website": "https://wcd.mizoram.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 18. NAGALAND
    # ───────────────────────────────────────────────────────────────────────
    "Nagaland": {
        "job_market": {
            "major_cities": ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-7 LPA", "description": "Hornbill Festival, tribal tourism"},
                {"sector": "Handicrafts & Weaving", "growth": "Medium", "avg_salary": "₹2-4 LPA", "description": "Naga shawls, woodcraft"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "King chili, kiwi, passion fruit"},
                {"sector": "Oil & Gas", "growth": "Low", "avg_salary": "₹5-12 LPA", "description": "Limited exploration"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Primary employer"},
            ],
            "it_parks": ["Proposed IT Hub Kohima"],
            "avg_entry_salary": "₹2-3.5 LPA",
        },
        "scholarships": [
            {"name": "Umbrella Scheme for ST", "department": "Tribal Affairs", "amount": "Full fee + maintenance", "eligibility": "ST students", "website": "https://nagaland.gov.in"},
            {"name": "State Merit Scholarship", "department": "Education Dept", "amount": "₹15,000/year", "eligibility": "Top performers", "website": "https://nagaland.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC", "amount": "₹10,000-30,000/year", "eligibility": "NE students", "website": "https://necouncil.gov.in"},
            {"name": "Chief Minister's Scholarship", "department": "CM Office", "amount": "₹25,000/year", "eligibility": "Students in national institutes", "website": "https://nagaland.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Nagaland Public Service Commission (NPSC)",
            "psc_website": "https://npsc.nagaland.gov.in",
            "major_exams": [
                {"exam": "Nagaland Civil Services", "posts": "NCS, NPS officers", "eligibility": "Graduation", "age": "21-35"},
                {"exam": "Combined Technical Services", "posts": "JE, AE", "eligibility": "Diploma/B.Tech", "age": "18-35"},
                {"exam": "Secretariat Assistant", "posts": "LDA, UDA", "eligibility": "Graduation", "age": "18-32"},
            ],
            "other_recruiters": ["Nagaland Police", "NST (Transport)", "Power Dept", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Dimapur Industrial Growth Centre", "type": "Light Manufacturing", "companies": "Food processing, handicrafts", "jobs_potential": "Low", "relevant_streams": ["Commerce"]},
            {"name": "Handicraft Clusters", "type": "Traditional Crafts", "companies": "Weaving cooperatives, woodcraft", "jobs_potential": "Medium", "relevant_streams": ["Design", "Arts"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "60+",
            "notable_startups": ["Hornbill-themed tourism startups"],
            "incubators": ["NIT Nagaland Incubation", "Entrepreneurship Development Centre"],
            "govt_schemes": [
                {"name": "Nagaland Startup Policy", "benefit": "Seed fund, mentorship", "website": "https://nagaland.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Chief Minister's Health Insurance", "benefit": "₹2 lakh health coverage", "eligibility": "All residents", "website": "https://nagaland.gov.in"},
            {"name": "Free Education Initiative", "benefit": "Free textbooks up to Class 8", "eligibility": "Govt school students", "website": "https://education.nagaland.gov.in"},
            {"name": "Youth Resources & Sports", "benefit": "Sports infrastructure, training", "eligibility": "Youth athletes", "website": "https://sports.nagaland.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 19. ODISHA
    # ───────────────────────────────────────────────────────────────────────
    "Odisha": {
        "job_market": {
            "major_cities": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Puri"],
            "top_sectors": [
                {"sector": "Steel & Mining", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Major steel, iron ore, aluminium"},
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Bhubaneswar IT hub growing fast"},
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-8 LPA", "description": "Puri, Konark, tribal tourism"},
                {"sector": "Handloom & Handicrafts", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Sambalpuri, Bomkai saris"},
                {"sector": "Seafood & Fisheries", "growth": "Medium", "avg_salary": "₹2-6 LPA", "description": "Shrimp, fish processing"},
            ],
            "it_parks": ["Infocity Bhubaneswar", "STPI Bhubaneswar", "Infovalley"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "Prerana Scholarship", "department": "ST/SC Welfare Dept", "amount": "₹75,000/year for NEET/JEE qualified", "eligibility": "ST/SC students clearing NEET/JEE", "website": "https://scholarship.odisha.gov.in"},
            {"name": "Medhabruti Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Class 9-PG meritorious students", "website": "https://scholarship.odisha.gov.in"},
            {"name": "Post Matric Scholarship SC/ST", "department": "Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST students", "website": "https://scholarship.odisha.gov.in"},
            {"name": "Gopabandhu Sikhya Sahayata", "department": "School & Mass Education", "amount": "₹600-1,000/month", "eligibility": "EWS students in govt schools", "website": "https://scholarship.odisha.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Odisha Public Service Commission (OPSC)",
            "psc_website": "https://opsc.gov.in",
            "major_exams": [
                {"exam": "OAS (Odisha Administrative Service)", "posts": "Deputy Collector, DSP", "eligibility": "Graduation", "age": "21-38"},
                {"exam": "OPSC ASO", "posts": "Assistant Section Officers", "eligibility": "Graduation", "age": "21-38"},
                {"exam": "OSSSC CGL", "posts": "Revenue Inspector, Amin", "eligibility": "Graduation", "age": "18-32"},
            ],
            "other_recruiters": ["OSRTC", "Odisha Police", "GRIDCO", "NALCO", "MCL", "Tata Steel Kalinganagar"],
        },
        "industry_clusters": [
            {"name": "Infocity Bhubaneswar", "type": "IT & ITES", "companies": "TCS, Infosys, Mindtree, Wipro", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Angul-Talcher Industrial Belt", "type": "Steel, Aluminium, Power", "companies": "NALCO, MCL, NTPC, Jindal Steel", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "Kalinganagar Industrial Complex", "type": "Steel", "companies": "Tata Steel, VISA Steel", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top Performer",
            "total_startups": "2,200+",
            "notable_startups": ["Milk Mantra", "Sambad Odia origins"],
            "incubators": ["O-Hub", "STPI Startup Hub", "KIIT TBI", "XIMB Incubator"],
            "govt_schemes": [
                {"name": "Odisha Startup Policy 2016", "benefit": "Seed fund up to ₹20 lakh, 5-year tax holiday", "website": "https://startup.odisha.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "KALIA Scheme", "benefit": "₹25,000/year for farmers", "eligibility": "Small/marginal farmers", "website": "https://kalia.odisha.gov.in"},
            {"name": "Biju Swasthya Kalyan Yojana", "benefit": "₹5-10 lakh health insurance", "eligibility": "All ration card holders", "website": "https://bsky.odisha.gov.in"},
            {"name": "State Skill Development Programme", "benefit": "Free skill training + placement", "eligibility": "Youth 18-35", "website": "https://wsd.odisha.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 20. PUNJAB
    # ───────────────────────────────────────────────────────────────────────
    "Punjab": {
        "job_market": {
            "major_cities": ["Chandigarh (shared)", "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Mohali"],
            "top_sectors": [
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Wheat, rice, basmati - food bowl of India"},
                {"sector": "Textiles & Hosiery", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Ludhiana knitwear hub"},
                {"sector": "Sports Goods", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Jalandhar - major exporter"},
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Mohali IT City"},
                {"sector": "Dairy & Food Processing", "growth": "Medium", "avg_salary": "₹2-6 LPA", "description": "Milkfed, Verka"},
            ],
            "it_parks": ["IT City Mohali", "Quark City Mohali", "STPI Mohali"],
            "avg_entry_salary": "₹2.5-5 LPA",
        },
        "scholarships": [
            {"name": "Post Matric Scholarship SC", "department": "SC Welfare Dept", "amount": "Full fee + ₹550-1200/month", "eligibility": "SC students, income < ₹2.5 LPA", "website": "https://punjabscholarships.gov.in"},
            {"name": "OBC/BC Scholarship", "department": "BC Welfare Dept", "amount": "₹5,000-15,000/year", "eligibility": "OBC students", "website": "https://punjabscholarships.gov.in"},
            {"name": "Ashirwad Scheme", "department": "Social Security Dept", "amount": "₹51,000 for marriage", "eligibility": "SC/BPL families' daughters", "website": "https://punjab.gov.in"},
            {"name": "Punjab State Merit Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Top performers in board exams", "website": "https://punjabscholarships.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Punjab Public Service Commission (PPSC)",
            "psc_website": "https://ppsc.gov.in",
            "major_exams": [
                {"exam": "PCS (Punjab Civil Services)", "posts": "SDM, DSP, Tehsildar", "eligibility": "Graduation", "age": "21-37"},
                {"exam": "Punjab Police SI", "posts": "Sub Inspector", "eligibility": "Graduation", "age": "18-28"},
                {"exam": "PSSSB Clerk", "posts": "Clerks, Assistants", "eligibility": "Graduation", "age": "18-37"},
            ],
            "other_recruiters": ["PRTC", "Punjab Police", "PSPCL", "Markfed", "Punjab National Bank"],
        },
        "industry_clusters": [
            {"name": "Ludhiana Industrial Belt", "type": "Textiles & Bicycles", "companies": "Hero Cycles, Avon, Monte Carlo, Oswal", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "IT City Mohali", "type": "IT & BPO", "companies": "Infosys, TCS, Dell, Quark", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Jalandhar Sports Goods", "type": "Sports Equipment", "companies": "Cosco, Mayor, BDM", "jobs_potential": "Medium", "relevant_streams": ["Commerce", "Design"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "1,500+",
            "notable_startups": ["Punjab-origin agritech, edtech startups"],
            "incubators": ["iStart Punjab", "IIT Ropar TBI", "ISB Mohali"],
            "govt_schemes": [
                {"name": "Punjab Startup Policy 2022", "benefit": "Seed fund up to ₹10 lakh, incubation", "website": "https://pbindustries.gov.in/startup"},
            ],
        },
        "govt_schemes": [
            {"name": "Ghar Ghar Rozgar Yojana", "benefit": "Employment linkage, job fairs", "eligibility": "Unemployed youth", "website": "https://pgrkam.punjab.gov.in"},
            {"name": "Atta-Dal Scheme", "benefit": "Free wheat & dal to BPL", "eligibility": "Blue card holders", "website": "https://punjab.gov.in"},
            {"name": "Sarbat Sehat Bima Yojana", "benefit": "₹5 lakh health insurance", "eligibility": "All families", "website": "https://sha.punjab.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 21. RAJASTHAN
    # ───────────────────────────────────────────────────────────────────────
    "Rajasthan": {
        "job_market": {
            "major_cities": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer", "Bikaner"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-10 LPA", "description": "Palaces, forts, desert tourism"},
                {"sector": "Mining (Marble/Granite)", "growth": "Stable", "avg_salary": "₹3-8 LPA", "description": "Largest marble producer"},
                {"sector": "Textiles & Handicrafts", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Block printing, gems & jewelry"},
                {"sector": "IT & BPO", "growth": "High", "avg_salary": "₹3-12 LPA", "description": "Jaipur IT corridor growing"},
                {"sector": "Education & Coaching", "growth": "Very High", "avg_salary": "₹3-15 LPA", "description": "Kota - coaching capital of India"},
            ],
            "it_parks": ["Mahindra World City Jaipur", "STPI Jaipur", "Sitapura IT Park"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "Mukhyamantri Uch Shiksha Scholarship", "department": "Higher Education Dept", "amount": "₹5,000/year for 5 years", "eligibility": "Class 12 pass with 60%+, income < ₹2.5 LPA", "website": "https://hte.rajasthan.gov.in"},
            {"name": "Devnarayan Scholarship", "department": "Social Justice Dept", "amount": "₹10,000-20,000/year", "eligibility": "OBC girls with 50%+ marks", "website": "https://sje.rajasthan.gov.in"},
            {"name": "Kalibai Bheel Medhavi Scholarship", "department": "Tribal Welfare Dept", "amount": "Up to ₹50,000/year", "eligibility": "ST girls in class 12+", "website": "https://sje.rajasthan.gov.in"},
            {"name": "Ambedkar International Scholarship", "department": "Social Justice Dept", "amount": "Up to ₹30 lakh for abroad study", "eligibility": "SC students for foreign masters/PhD", "website": "https://sje.rajasthan.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Rajasthan Public Service Commission (RPSC)",
            "psc_website": "https://rpsc.rajasthan.gov.in",
            "major_exams": [
                {"exam": "RAS/RTS (Rajasthan Administrative Service)", "posts": "SDO, DSP, Tehsildar", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "RPSC School Lecturer", "posts": "Lecturers in Govt schools", "eligibility": "PG with B.Ed", "age": "21-40"},
                {"exam": "RSMSSB Patwari", "posts": "Patwari, Clerk", "eligibility": "12th/Graduation", "age": "18-40"},
            ],
            "other_recruiters": ["RSRTC", "Rajasthan Police", "RVUNL", "RSMML", "RIICO"],
        },
        "industry_clusters": [
            {"name": "Mahindra World City Jaipur", "type": "IT & Manufacturing", "companies": "Infosys, Wipro, Genpact, auto components", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Bhiwadi Industrial Area", "type": "Automobile & Electronics", "companies": "Honda, Daikin, Saint-Gobain", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Jodhpur Handicrafts Cluster", "type": "Handicrafts & Furniture", "companies": "Furniture export, handicrafts", "jobs_potential": "Medium", "relevant_streams": ["Design", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top 10 Performer",
            "total_startups": "3,000+",
            "notable_startups": ["CarDekho (origins)", "Jaipur-origin edtech, travel startups"],
            "incubators": ["iStart Rajasthan", "RIICO Incubation", "MNIT Incubator"],
            "govt_schemes": [
                {"name": "iStart Rajasthan", "benefit": "Seed fund up to ₹25 lakh, sustenance allowance", "website": "https://istart.rajasthan.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Indira Rasoi Yojana", "benefit": "₹8 meal for poor", "eligibility": "Anyone needing food", "website": "https://indirarasoi.rajasthan.gov.in"},
            {"name": "Chiranjeevi Yojana", "benefit": "₹25 lakh health insurance", "eligibility": "All families", "website": "https://chiranjeevi.rajasthan.gov.in"},
            {"name": "Anuprati Coaching Scheme", "benefit": "Free coaching for competitive exams", "eligibility": "SC/ST/OBC/EWS students", "website": "https://sje.rajasthan.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 22. SIKKIM
    # ───────────────────────────────────────────────────────────────────────
    "Sikkim": {
        "job_market": {
            "major_cities": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-8 LPA", "description": "Himalayan tourism, eco-tourism"},
                {"sector": "Organic Farming", "growth": "High", "avg_salary": "₹2-5 LPA", "description": "India's first 100% organic state"},
                {"sector": "Hydropower", "growth": "High", "avg_salary": "₹5-15 LPA", "description": "Multiple hydro projects"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Large cardamom, floriculture"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Tax-free zone attracted pharma"},
            ],
            "it_parks": ["Proposed IT Park Gangtok"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "Chief Minister's Merit Scholarship", "department": "Education Dept", "amount": "₹50,000-1 lakh/year", "eligibility": "Toppers in Class 10/12", "website": "https://sikkim.gov.in"},
            {"name": "Post Matric Scholarship ST", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "ST students (majority population)", "website": "https://sikkim.gov.in"},
            {"name": "OBC Scholarship", "department": "Social Welfare Dept", "amount": "₹5,000-15,000/year", "eligibility": "OBC students", "website": "https://sikkim.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC", "amount": "₹10,000-30,000/year", "eligibility": "NE students in higher ed", "website": "https://necouncil.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Sikkim Public Service Commission (SPSC)",
            "psc_website": "https://spscskm.gov.in",
            "major_exams": [
                {"exam": "Sikkim State Civil Services", "posts": "SCS, SPS officers", "eligibility": "Graduation", "age": "21-30"},
                {"exam": "Lower Division Clerk", "posts": "LDC in departments", "eligibility": "12th pass", "age": "18-30"},
                {"exam": "Technical Services", "posts": "JE, AE", "eligibility": "Diploma/B.Tech", "age": "18-30"},
            ],
            "other_recruiters": ["SNT (Transport)", "Sikkim Police", "Energy & Power Dept", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Rangpo Industrial Area", "type": "Pharma & Alcohol", "companies": "Sun Pharma, Intas, Zydus, Alcobrew", "jobs_potential": "High", "relevant_streams": ["Science", "Engineering"]},
            {"name": "Organic Farming Clusters", "type": "Agriculture", "companies": "Organic cooperatives, export units", "jobs_potential": "Medium", "relevant_streams": ["Agriculture", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "100+",
            "notable_startups": ["Tourism-tech, organic food startups"],
            "incubators": ["Sikkim State Livelihood Mission", "SMU Incubation"],
            "govt_schemes": [
                {"name": "Sikkim Startup Policy", "benefit": "Seed fund, incubation", "website": "https://sikkim.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Chief Minister's Self Employment Scheme", "benefit": "Loans at 4% for youth enterprise", "eligibility": "Youth 18-35", "website": "https://sikkim.gov.in"},
            {"name": "One Family One Job", "benefit": "Govt job guarantee to one per family", "eligibility": "Sikkim domicile families", "website": "https://sikkim.gov.in"},
            {"name": "Free Education Policy", "benefit": "Free education up to college level", "eligibility": "All Sikkim students in govt institutions", "website": "https://sikkim.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 23. TAMIL NADU
    # ───────────────────────────────────────────────────────────────────────
    "Tamil Nadu": {
        "job_market": {
            "major_cities": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
            "top_sectors": [
                {"sector": "Automobiles", "growth": "Very High", "avg_salary": "₹4-18 LPA", "description": "Detroit of India - Hyundai, Ford, Renault-Nissan"},
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹5-25 LPA", "description": "Chennai IT corridor"},
                {"sector": "Textiles", "growth": "Stable", "avg_salary": "₹2-8 LPA", "description": "Coimbatore, Tirupur knitwear"},
                {"sector": "Film & Entertainment", "growth": "High", "avg_salary": "₹3-30 LPA", "description": "Kollywood"},
                {"sector": "Leather & Footwear", "growth": "Medium", "avg_salary": "₹2-8 LPA", "description": "Ranipet, Chennai export hub"},
            ],
            "it_parks": ["Tidel Park Chennai", "SIPCOT IT Park", "ELCOT IT Park", "Coimbatore IT Park", "Mahindra World City"],
            "avg_entry_salary": "₹3.5-6 LPA",
        },
        "scholarships": [
            {"name": "BC/MBC/DNC Scholarship", "department": "BC Welfare Dept", "amount": "Full fee for professional courses", "eligibility": "BC/MBC/DNC students", "website": "https://bcmbcmw.tn.gov.in"},
            {"name": "SC/ST Scholarship", "department": "Adi Dravidar Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST students", "website": "https://adwelfare.tn.gov.in"},
            {"name": "Moovalur Ramamirtham Scheme", "department": "Social Welfare Dept", "amount": "₹1,000/month for girls in higher ed", "eligibility": "Undergraduate girls from govt schools", "website": "https://tnsocialwelfare.tn.gov.in"},
            {"name": "EVR Maniammaiyar Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Meritorious girls in UG/PG", "website": "https://tn.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Tamil Nadu Public Service Commission (TNPSC)",
            "psc_website": "https://tnpsc.gov.in",
            "major_exams": [
                {"exam": "TNPSC Group I", "posts": "Deputy Collector, DSP", "eligibility": "Graduation", "age": "21-37"},
                {"exam": "TNPSC Group II", "posts": "Tahsildar, BDO, Assistant Commercial Tax Officer", "eligibility": "Graduation", "age": "21-37"},
                {"exam": "TNPSC Group IV", "posts": "VAO, Jr Assistant, Typist", "eligibility": "10th/12th pass", "age": "18-30"},
            ],
            "other_recruiters": ["TNSTC", "TN Police", "TANGEDCO", "TIDCO", "Chennai Metro"],
        },
        "industry_clusters": [
            {"name": "Chennai IT Corridor", "type": "IT & ITES", "companies": "TCS, Infosys, Cognizant, HCL, Zoho", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Sriperumbudur Auto Hub", "type": "Automobile", "companies": "Hyundai, Renault-Nissan, BMW, Daimler", "jobs_potential": "Very High", "relevant_streams": ["Engineering"]},
            {"name": "Tirupur Textile Hub", "type": "Textiles & Knitwear", "companies": "Eastman Exports, KPR Mills, export units", "jobs_potential": "Very High", "relevant_streams": ["Commerce", "Design"]},
            {"name": "Coimbatore Industrial Belt", "type": "Manufacturing & Pumps", "companies": "Pump manufacturers, textiles, foundries", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top 3 in India",
            "total_startups": "8,000+",
            "notable_startups": ["Zoho", "Freshworks", "Chargebee", "Kissflow", "GUVI"],
            "incubators": ["StartupTN", "IIT Madras Research Park", "Anna University TBI", "Forge Coimbatore"],
            "govt_schemes": [
                {"name": "Tamil Nadu Startup Policy 2.0", "benefit": "Seed fund up to ₹30 lakh, innovation vouchers", "website": "https://startuptn.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Kalaignar Magalir Urimai Thogai", "benefit": "₹1,000/month to women heads of family", "eligibility": "Women-headed households", "website": "https://tn.gov.in"},
            {"name": "Chief Minister's Health Insurance", "benefit": "₹5 lakh medical insurance", "eligibility": "All families", "website": "https://cmchistn.com"},
            {"name": "Naan Mudhalvan Scheme", "benefit": "Free skill training + internships", "eligibility": "College students", "website": "https://naanmudhalvan.tn.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 24. TELANGANA
    # ───────────────────────────────────────────────────────────────────────
    "Telangana": {
        "job_market": {
            "major_cities": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹5-25 LPA", "description": "HITEC City - major IT hub"},
                {"sector": "Pharmaceuticals", "growth": "Very High", "avg_salary": "₹4-15 LPA", "description": "Genome Valley, bulk drug manufacturing"},
                {"sector": "Biotechnology", "growth": "High", "avg_salary": "₹5-15 LPA", "description": "Genome Valley biotech cluster"},
                {"sector": "Defence & Aerospace", "growth": "High", "avg_salary": "₹6-20 LPA", "description": "DRDO labs, private defence"},
                {"sector": "Film & Entertainment", "growth": "High", "avg_salary": "₹3-25 LPA", "description": "Tollywood"},
            ],
            "it_parks": ["HITEC City", "Gachibowli Financial District", "Genome Valley", "Pocharam IT SEZ"],
            "avg_entry_salary": "₹4-7 LPA",
        },
        "scholarships": [
            {"name": "TS Epass Scholarship", "department": "Welfare Dept", "amount": "Fee reimbursement + maintenance", "eligibility": "SC/ST/BC/EBC/Minority students", "website": "https://telanganaepass.cgg.gov.in"},
            {"name": "Ambedkar Overseas Scholarship", "department": "BC Welfare Dept", "amount": "Up to ₹20 lakh for abroad study", "eligibility": "SC/ST students for foreign masters", "website": "https://ambedkaroverseas.telangana.gov.in"},
            {"name": "Kalyana Lakshmi/Shadi Mubarak", "department": "Women Dev Dept", "amount": "₹1,00,116 for marriage", "eligibility": "SC/ST/BC/Minority girls at marriage", "website": "https://telanganaepass.cgg.gov.in"},
            {"name": "Chief Minister's Scholarship", "department": "Higher Education Dept", "amount": "₹20,000/year", "eligibility": "Meritorious students in professional courses", "website": "https://hed.telangana.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Telangana State Public Service Commission (TSPSC)",
            "psc_website": "https://tspsc.gov.in",
            "major_exams": [
                {"exam": "Group I (TS Civil Services)", "posts": "Deputy Collector, DSP, RDO", "eligibility": "Graduation", "age": "18-44"},
                {"exam": "Group II", "posts": "Tehsildar, Municipal Commissioner", "eligibility": "Graduation", "age": "18-44"},
                {"exam": "Group IV", "posts": "Junior Assistants, Typists", "eligibility": "10th/12th", "age": "18-44"},
            ],
            "other_recruiters": ["TSRTC", "Telangana Police", "TSSPDCL", "Hyderabad Metro", "HMDA"],
        },
        "industry_clusters": [
            {"name": "HITEC City Hyderabad", "type": "IT & ITES", "companies": "Microsoft, Google, Amazon, Facebook, Qualcomm, 1500+ companies", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Genome Valley", "type": "Pharma & Biotech", "companies": "Dr. Reddy's, Bharat Biotech, Biological E, Hetero", "jobs_potential": "Very High", "relevant_streams": ["Science", "Medical"]},
            {"name": "Gachibowli Financial District", "type": "Finance & IT", "companies": "Deloitte, Capgemini, WellsFargo, HSBC", "jobs_potential": "Very High", "relevant_streams": ["Commerce", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top 3 in India",
            "total_startups": "9,000+",
            "notable_startups": ["Bharat Biotech", "Skyroot Aerospace", "Darwinbox", "Zenoti"],
            "incubators": ["T-Hub (largest in India)", "WE Hub", "IIIT Hyderabad Research Park", "AIC CCMB"],
            "govt_schemes": [
                {"name": "Telangana Startup Policy 2.0", "benefit": "Seed fund up to ₹25 lakh, prototype funding", "website": "https://startup.telangana.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Kalyana Lakshmi", "benefit": "₹1,00,116 for girl's marriage", "eligibility": "All communities' girls at marriage", "website": "https://wcdsc.telangana.gov.in"},
            {"name": "Rythu Bandhu", "benefit": "₹10,000/acre/year investment support", "eligibility": "All farmers", "website": "https://rythubandhu.telangana.gov.in"},
            {"name": "Telangana Young India Skill University", "benefit": "Industry-linked skill training", "eligibility": "Youth 18-35", "website": "https://tgskilluniversity.ac.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 25. TRIPURA
    # ───────────────────────────────────────────────────────────────────────
    "Tripura": {
        "job_market": {
            "major_cities": ["Agartala", "Udaipur", "Dharmanagar", "Kailashahar"],
            "top_sectors": [
                {"sector": "Rubber", "growth": "High", "avg_salary": "₹2-6 LPA", "description": "2nd largest rubber producer"},
                {"sector": "Tea", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Tea gardens"},
                {"sector": "Bamboo & Forest Products", "growth": "Medium", "avg_salary": "₹2-4 LPA", "description": "Bamboo craft, agarbatti"},
                {"sector": "Handloom", "growth": "Stable", "avg_salary": "₹2-4 LPA", "description": "Traditional weaving"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "Major employer"},
            ],
            "it_parks": ["STPI Agartala"],
            "avg_entry_salary": "₹2-3.5 LPA",
        },
        "scholarships": [
            {"name": "Post Matric Scholarship ST", "department": "Tribal Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "ST students", "website": "https://tripura.gov.in"},
            {"name": "SC Post Matric Scholarship", "department": "SC Welfare Dept", "amount": "Fee + ₹380-1200/month", "eligibility": "SC students, income < ₹2.5 LPA", "website": "https://tripura.gov.in"},
            {"name": "State Merit Scholarship", "department": "Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Top performers", "website": "https://tripura.gov.in"},
            {"name": "NEC Merit Scholarship", "department": "NEC", "amount": "₹10,000-30,000/year", "eligibility": "NE students in professional courses", "website": "https://necouncil.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Tripura Public Service Commission (TPSC)",
            "psc_website": "https://tpsc.tripura.gov.in",
            "major_exams": [
                {"exam": "Tripura Civil Services", "posts": "TCS, TPS officers", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "Jr/Sr Clerk Recruitment", "posts": "Clerks in departments", "eligibility": "Graduation", "age": "18-40"},
                {"exam": "Teachers Recruitment", "posts": "TGT/PGT", "eligibility": "PG with B.Ed/TET", "age": "18-40"},
            ],
            "other_recruiters": ["TRTC (Transport)", "Tripura Police", "TSECL (Power)", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Bodhjungnagar Industrial Estate", "type": "Manufacturing", "companies": "Food processing, rubber, bamboo", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Rubber Processing Units", "type": "Rubber Industry", "companies": "Tripura State Rubber Ltd, private units", "jobs_potential": "Medium", "relevant_streams": ["Agriculture", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "80+",
            "notable_startups": ["Agritech, handloom e-commerce startups"],
            "incubators": ["NIT Agartala Incubation", "Tripura University TBI"],
            "govt_schemes": [
                {"name": "Tripura Startup Support", "benefit": "Seed fund, mentorship", "website": "https://tripura.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Chief Minister's Livelihood Scheme", "benefit": "Interest subvention on MSME loans", "eligibility": "Youth entrepreneurs", "website": "https://tripura.gov.in"},
            {"name": "Tripura Health Assurance Scheme", "benefit": "₹5 lakh health insurance", "eligibility": "All families", "website": "https://tripura.gov.in"},
            {"name": "Mukhyamantri Yuba Yogayog Yojana", "benefit": "Interest-free loans for youth startups", "eligibility": "Youth 18-45", "website": "https://tripura.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 26. UTTAR PRADESH
    # ───────────────────────────────────────────────────────────────────────
    "Uttar Pradesh": {
        "job_market": {
            "major_cities": ["Lucknow", "Noida", "Greater Noida", "Ghaziabad", "Kanpur", "Agra", "Varanasi", "Prayagraj"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹5-25 LPA", "description": "Noida - major IT hub, NCR region"},
                {"sector": "Agriculture", "growth": "Stable", "avg_salary": "₹2-5 LPA", "description": "Largest producer of foodgrains"},
                {"sector": "Sugar & Distillery", "growth": "Stable", "avg_salary": "₹3-8 LPA", "description": "Largest sugar producer"},
                {"sector": "Handicrafts & Textiles", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Banarasi silk, Chikankari, carpets"},
                {"sector": "Leather & Footwear", "growth": "Medium", "avg_salary": "₹2-8 LPA", "description": "Agra, Kanpur leather hub"},
            ],
            "it_parks": ["Noida IT City", "Greater Noida Tech Zone", "Lucknow IT City", "STPI Noida"],
            "avg_entry_salary": "₹3-6 LPA",
        },
        "scholarships": [
            {"name": "UP Post Matric Scholarship SC/ST/OBC", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST/OBC students", "website": "https://scholarship.up.gov.in"},
            {"name": "Dassault Scholarship", "department": "Higher Education via Dassault", "amount": "₹40,000-60,000/year", "eligibility": "Girls in engineering", "website": "https://scholarship.up.gov.in"},
            {"name": "Pre-Matric Scholarship Minorities", "department": "Minority Welfare Dept", "amount": "₹100-500/month", "eligibility": "Minority students Class 1-10", "website": "https://scholarship.up.gov.in"},
            {"name": "Chief Minister's Scholarship", "department": "CM Office", "amount": "Variable based on merit", "eligibility": "Top performers", "website": "https://scholarship.up.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Uttar Pradesh Public Service Commission (UPPSC)",
            "psc_website": "https://uppsc.up.nic.in",
            "major_exams": [
                {"exam": "UPPSC PCS", "posts": "SDM, DSP, BDO, Tehsildar", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "UPPSC RO/ARO", "posts": "Review Officer/Asst Review Officer", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "UP Police SI", "posts": "Sub Inspector", "eligibility": "Graduation", "age": "21-28"},
                {"exam": "UP TET/STET", "posts": "Primary/Upper Primary Teachers", "eligibility": "D.El.Ed/B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["UPSRTC", "UP Police", "UPPCL", "UP Metro", "Lucknow Metro"],
        },
        "industry_clusters": [
            {"name": "Noida-Greater Noida IT/Electronics", "type": "IT & Electronics", "companies": "Samsung, HCL, TCS, Infosys, Wipro", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "YEIDA Jewar", "type": "Airport & Logistics (upcoming)", "companies": "Noida Int'l Airport, logistics hubs", "jobs_potential": "Very High (future)", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Agra-Kanpur Leather Belt", "type": "Leather & Footwear", "companies": "Export units, tanneries", "jobs_potential": "High", "relevant_streams": ["Commerce", "Design"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top 5 in India",
            "total_startups": "6,000+",
            "notable_startups": ["Paytm (Noida)", "BharatPe", "Zomato (now Gurgaon)", "Policy Bazaar (NCR)"],
            "incubators": ["Startup UP", "IIT Kanpur SIIC", "IIM Lucknow Incubator"],
            "govt_schemes": [
                {"name": "UP Startup Policy 2020", "benefit": "Seed fund up to ₹50 lakh, incubation support", "website": "https://startup.up.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Kanya Sumangala Yojana", "benefit": "₹15,000 in 6 installments for girls", "eligibility": "Girls born after April 2019", "website": "https://mksy.up.gov.in"},
            {"name": "UP Pankh Yojana", "benefit": "Career guidance for NEET/JEE", "eligibility": "Class 9-12 students", "website": "https://uppankh.in"},
            {"name": "UP Skill Development Mission", "benefit": "Free skill training + placement", "eligibility": "Youth 18-35", "website": "https://upsdm.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 27. UTTARAKHAND
    # ───────────────────────────────────────────────────────────────────────
    "Uttarakhand": {
        "job_market": {
            "major_cities": ["Dehradun", "Haridwar", "Rishikesh", "Haldwani", "Roorkee"],
            "top_sectors": [
                {"sector": "Tourism & Hospitality", "growth": "Very High", "avg_salary": "₹2-10 LPA", "description": "Char Dham, adventure tourism"},
                {"sector": "IT & BPO", "growth": "High", "avg_salary": "₹3-12 LPA", "description": "Dehradun IT Park growing"},
                {"sector": "AYUSH & Wellness", "growth": "High", "avg_salary": "₹3-10 LPA", "description": "Yoga capital, AYUSH manufacturing"},
                {"sector": "Pharmaceuticals", "growth": "High", "avg_salary": "₹4-12 LPA", "description": "Haridwar-Roorkee pharma belt"},
                {"sector": "Horticulture", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Apple, basmati rice"},
            ],
            "it_parks": ["IT Park Dehradun", "STPI Dehradun"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "UK Post Matric Scholarship SC/ST/OBC", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST/OBC students", "website": "https://escholarship.uk.gov.in"},
            {"name": "Merit-cum-Means Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Meritorious EWS students", "website": "https://escholarship.uk.gov.in"},
            {"name": "Gaura Devi Scholarship", "department": "Women Welfare Dept", "amount": "₹50,000 for girls", "eligibility": "BPL girls completing Class 12", "website": "https://escholarship.uk.gov.in"},
            {"name": "Uttarakhand Sainik Scholarship", "department": "Sainik Welfare Dept", "amount": "₹10,000-25,000/year", "eligibility": "Children of defence personnel", "website": "https://uk.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Uttarakhand Public Service Commission (UKPSC)",
            "psc_website": "https://ukpsc.gov.in",
            "major_exams": [
                {"exam": "UKPSC PCS", "posts": "Deputy Collector, DSP, BDO", "eligibility": "Graduation", "age": "21-42"},
                {"exam": "UKPSC Lower PCS", "posts": "Naib Tehsildar, Lekhpal", "eligibility": "Graduation", "age": "21-42"},
                {"exam": "UK TET", "posts": "Primary/Upper Primary Teachers", "eligibility": "D.El.Ed/B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["UKTC (Transport)", "UK Police", "UPCL (Power)", "THDC", "Forest Dept"],
        },
        "industry_clusters": [
            {"name": "Haridwar SIDCUL", "type": "Pharma & FMCG", "companies": "Dabur, Patanjali, HUL, Pharma units", "jobs_potential": "Very High", "relevant_streams": ["Science", "Engineering"]},
            {"name": "Dehradun IT Corridor", "type": "IT & BPO", "companies": "HCL, TCS, state IT projects", "jobs_potential": "Medium", "relevant_streams": ["Engineering"]},
            {"name": "Pantnagar Industrial Area", "type": "Automobile & Manufacturing", "companies": "Tata Motors, Ashok Leyland", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "600+",
            "notable_startups": ["Patanjali (Haridwar)", "Agritech, wellness startups"],
            "incubators": ["IIT Roorkee TIDES", "Startup Uttarakhand", "Doon University Incubator"],
            "govt_schemes": [
                {"name": "UK Startup Policy 2018", "benefit": "Seed fund up to ₹25 lakh, tax exemptions", "website": "https://startuputtarakhand.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Swarozgar Yojana", "benefit": "₹25 lakh loan at subsidy for youth business", "eligibility": "Youth 18-45", "website": "https://msy.uk.gov.in"},
            {"name": "Atal Ayushman Uttarakhand Yojana", "benefit": "₹5 lakh health insurance", "eligibility": "All families", "website": "https://ayushmanuttarakhand.org"},
            {"name": "Mukhyamantri Vatsalya Yojana", "benefit": "Support for orphans of COVID", "eligibility": "Children who lost parents to COVID", "website": "https://uk.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 28. WEST BENGAL
    # ───────────────────────────────────────────────────────────────────────
    "West Bengal": {
        "job_market": {
            "major_cities": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Kharagpur"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "Salt Lake Sector V IT hub"},
                {"sector": "Jute & Textiles", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Largest jute producer"},
                {"sector": "Steel & Mining", "growth": "Stable", "avg_salary": "₹4-15 LPA", "description": "Durgapur steel city"},
                {"sector": "Tea", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Darjeeling, Dooars tea"},
                {"sector": "Film & Entertainment", "growth": "High", "avg_salary": "₹2-20 LPA", "description": "Tollygunge film industry"},
            ],
            "it_parks": ["Salt Lake Sector V", "New Town Rajarhat", "Bengal Silicon Valley Hub"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "Swami Vivekananda Scholarship", "department": "Higher Education Dept", "amount": "₹1,000-5,000/month", "eligibility": "Class 5 to PhD, income < ₹2.5 LPA", "website": "https://svmcm.wbhed.gov.in"},
            {"name": "Kanyashree Prakalpa", "department": "Women Dev Dept", "amount": "₹750/year + ₹25,000 at age 18", "eligibility": "Girls 13-18 years", "website": "https://wbkanyashree.gov.in"},
            {"name": "Aikyashree (Minority)", "department": "Minority Affairs Dept", "amount": "₹1,000-5,000/month", "eligibility": "Minority students", "website": "https://wbmdfc.gov.in"},
            {"name": "Oasis (SC/ST/OBC)", "department": "BC/SC/ST Welfare Dept", "amount": "Fee + maintenance", "eligibility": "SC/ST/OBC students", "website": "https://oasis.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "West Bengal Public Service Commission (WBPSC)",
            "psc_website": "https://wbpsc.gov.in",
            "major_exams": [
                {"exam": "WBCS (West Bengal Civil Service)", "posts": "BDO, DSP, Deputy Magistrate", "eligibility": "Graduation", "age": "21-36"},
                {"exam": "WBPSC Clerkship", "posts": "Clerks in state depts", "eligibility": "Graduation", "age": "18-40"},
                {"exam": "WB TET", "posts": "Primary/Upper Primary Teachers", "eligibility": "D.El.Ed/B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["WBTC (Transport)", "WB Police", "WBSETCL", "Kolkata Metro", "Kolkata Port"],
        },
        "industry_clusters": [
            {"name": "Salt Lake Sector V", "type": "IT & ITES", "companies": "TCS, Wipro, Cognizant, Capgemini, IBM", "jobs_potential": "Very High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Durgapur-Asansol Industrial Belt", "type": "Steel & Mining", "companies": "SAIL DSP, Burnpur, coal mines", "jobs_potential": "High", "relevant_streams": ["Engineering"]},
            {"name": "Haldia Petrochemical Complex", "type": "Petrochemicals", "companies": "HPCL, Mitsubishi, petrochemical units", "jobs_potential": "High", "relevant_streams": ["Engineering", "Science"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging Leader",
            "total_startups": "2,500+",
            "notable_startups": ["Licious (co-founder)", "Kolkata-origin fintech, edtech"],
            "incubators": ["Bengal Silicon Valley", "IIT Kharagpur STEP", "Calcutta Angels Network"],
            "govt_schemes": [
                {"name": "WB Startup Policy", "benefit": "Seed fund up to ₹25 lakh, state support", "website": "https://wbstartup.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Lakshmir Bhandar", "benefit": "₹500-1,000/month to women", "eligibility": "Women 25-60 years", "website": "https://socialsecurity.wb.gov.in"},
            {"name": "Swasthya Sathi", "benefit": "₹5 lakh health insurance", "eligibility": "All families", "website": "https://swasthyasathi.gov.in"},
            {"name": "Yuvasree Prakalpa", "benefit": "₹1,500/month unemployment allowance", "eligibility": "Unemployed youth with diploma", "website": "https://wbyuvasree.in"},
        ],
    },

    # ═══════════════════════════════════════════════════════════════════════
    # UNION TERRITORIES
    # ═══════════════════════════════════════════════════════════════════════

    # ───────────────────────────────────────────────────────────────────────
    # 29. DELHI
    # ───────────────────────────────────────────────────────────────────────
    "Delhi": {
        "job_market": {
            "major_cities": ["New Delhi", "Central Delhi", "South Delhi", "East Delhi", "Dwarka"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "Very High", "avg_salary": "₹5-30 LPA", "description": "NCR IT hub"},
                {"sector": "Finance & Banking", "growth": "High", "avg_salary": "₹5-25 LPA", "description": "Corporate HQs, banks"},
                {"sector": "Media & Advertising", "growth": "High", "avg_salary": "₹4-20 LPA", "description": "News, entertainment, advertising"},
                {"sector": "Government & PSUs", "growth": "Stable", "avg_salary": "₹6-20 LPA", "description": "Central govt, PSU HQs"},
                {"sector": "Retail & E-commerce", "growth": "Very High", "avg_salary": "₹3-15 LPA", "description": "E-commerce HQs, retail chains"},
            ],
            "it_parks": ["Nehru Place", "Okhla IT Hub", "Jasola IT Park"],
            "avg_entry_salary": "₹4-8 LPA",
        },
        "scholarships": [
            {"name": "Delhi Higher Education Scholarship", "department": "Higher Education Dept", "amount": "Fee reimbursement", "eligibility": "Delhi domicile EWS students", "website": "https://edistrict.delhigovt.nic.in"},
            {"name": "SC/ST/OBC Scholarship", "department": "Social Welfare Dept", "amount": "Full fee + ₹1,000/month", "eligibility": "SC/ST/OBC students", "website": "https://edistrict.delhigovt.nic.in"},
            {"name": "Merit Scholarship", "department": "Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Top performers in Class 12", "website": "https://edudel.nic.in"},
            {"name": "Jai Bhim Mukhyamantri Scholarship", "department": "Social Welfare Dept", "amount": "Coaching support for competitive exams", "eligibility": "SC/ST students", "website": "https://edistrict.delhigovt.nic.in"},
        ],
        "government_jobs": {
            "psc_name": "Delhi Subordinate Services Selection Board (DSSSB)",
            "psc_website": "https://dsssb.delhi.gov.in",
            "major_exams": [
                {"exam": "DSSSB TGT/PGT", "posts": "Teachers in Delhi govt schools", "eligibility": "Graduation/PG with B.Ed", "age": "18-42"},
                {"exam": "DSSSB JE/AE", "posts": "Junior/Assistant Engineers", "eligibility": "Diploma/B.Tech", "age": "18-30"},
                {"exam": "DSSSB LDC/Steno", "posts": "Clerks, Stenographers", "eligibility": "12th pass", "age": "18-27"},
            ],
            "other_recruiters": ["DTC", "Delhi Police (via SSC)", "NDMC", "Delhi Metro", "Delhi Jal Board"],
        },
        "industry_clusters": [
            {"name": "Connaught Place", "type": "Finance & Corporate", "companies": "Banks, MNCs, consulting", "jobs_potential": "Very High", "relevant_streams": ["Commerce", "Law"]},
            {"name": "Nehru Place-Okhla", "type": "IT & Electronics", "companies": "IT companies, electronic goods", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Narela Industrial Area", "type": "Manufacturing", "companies": "Light manufacturing, FMCG", "jobs_potential": "Medium", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Top 3 in India (with NCR)",
            "total_startups": "12,000+ (NCR region)",
            "notable_startups": ["Paytm", "Zomato", "OYO", "Urban Company", "Byjus"],
            "incubators": ["IIT Delhi TBI", "Delhi Technology University Incubator", "Startup India Hub"],
            "govt_schemes": [
                {"name": "Delhi Startup Policy", "benefit": "Seed fund, collateral-free loans", "website": "https://startup.delhi.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mukhyamantri Vigyan Pratibha Pariksha", "benefit": "₹5,000-10,000 for science students", "eligibility": "Class 9 students scoring 80%+", "website": "https://edudel.nic.in"},
            {"name": "Ladli Scheme", "benefit": "₹11,000 financial assistance for girls", "eligibility": "Girls born in Delhi", "website": "https://wcd.delhigovt.nic.in"},
            {"name": "E-rickshaw/Auto Scheme", "benefit": "Subsidy on e-vehicles", "eligibility": "Unemployed youth", "website": "https://ev.delhi.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 30. CHANDIGARH
    # ───────────────────────────────────────────────────────────────────────
    "Chandigarh": {
        "job_market": {
            "major_cities": ["Chandigarh (planned city)"],
            "top_sectors": [
                {"sector": "IT & ITES", "growth": "High", "avg_salary": "₹4-15 LPA", "description": "IT Park, tech companies"},
                {"sector": "Education", "growth": "Stable", "avg_salary": "₹4-12 LPA", "description": "Major educational hub"},
                {"sector": "Pharmaceuticals", "growth": "Medium", "avg_salary": "₹4-12 LPA", "description": "Pharma manufacturing"},
                {"sector": "Banking & Finance", "growth": "Stable", "avg_salary": "₹4-15 LPA", "description": "Regional banking hub"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹5-15 LPA", "description": "UT Administration, PSUs"},
            ],
            "it_parks": ["Chandigarh IT Park", "Rajiv Gandhi Chandigarh Technology Park"],
            "avg_entry_salary": "₹3-5 LPA",
        },
        "scholarships": [
            {"name": "SC/ST Scholarship", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST students", "website": "https://chandigarh.gov.in"},
            {"name": "Merit Scholarship", "department": "Education Dept", "amount": "₹5,000-15,000/year", "eligibility": "Top performers", "website": "https://chandigarh.gov.in"},
            {"name": "Minority Scholarship", "department": "Minority Welfare", "amount": "Fee support", "eligibility": "Minority students", "website": "https://chandigarh.gov.in"},
            {"name": "EWS Scholarship", "department": "Education Dept", "amount": "Fee reimbursement", "eligibility": "EWS students in Chandigarh schools", "website": "https://chandigarh.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Chandigarh Administration (via UPSC/SSC)",
            "psc_website": "https://chandigarh.gov.in",
            "major_exams": [
                {"exam": "UT Cadre Posts (via SSC)", "posts": "Clerks, Assistants", "eligibility": "Graduation", "age": "18-27"},
                {"exam": "Chandigarh Police", "posts": "SI, Constable", "eligibility": "10+2/Graduation", "age": "18-25"},
                {"exam": "UT Teachers", "posts": "TGT/PGT", "eligibility": "Graduation/PG with B.Ed", "age": "18-37"},
            ],
            "other_recruiters": ["CTU (Transport)", "Chandigarh Police", "PGI Chandigarh", "Panjab University"],
        },
        "industry_clusters": [
            {"name": "IT Park Chandigarh", "type": "IT & ITES", "companies": "Infosys, Tech Mahindra, Quark", "jobs_potential": "High", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Industrial Area Phase I & II", "type": "Manufacturing", "companies": "Light engineering, pharma", "jobs_potential": "Medium", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging (Tricity Hub)",
            "total_startups": "800+ (Tricity)",
            "notable_startups": ["Tricity-based edtech, healthtech startups"],
            "incubators": ["Chandigarh Launchpad", "IIT Ropar TBI", "ISB Mohali"],
            "govt_schemes": [
                {"name": "Chandigarh Startup Policy", "benefit": "Incubation support, mentorship", "website": "https://chandigarh.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "EWS Housing Scheme", "benefit": "Affordable housing for EWS", "eligibility": "EWS families", "website": "https://chandigarh.gov.in"},
            {"name": "Pension Schemes", "benefit": "Old age, widow, disability pension", "eligibility": "Eligible categories", "website": "https://chandigarh.gov.in"},
            {"name": "Skill Development Programs", "benefit": "Free skill training", "eligibility": "Youth 18-35", "website": "https://chandigarh.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 31. PUDUCHERRY
    # ───────────────────────────────────────────────────────────────────────
    "Puducherry": {
        "job_market": {
            "major_cities": ["Puducherry", "Karaikal", "Mahe", "Yanam"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "High", "avg_salary": "₹2-8 LPA", "description": "French heritage, beach tourism"},
                {"sector": "IT & BPO", "growth": "Medium", "avg_salary": "₹3-10 LPA", "description": "IT services growing"},
                {"sector": "Leather & Textiles", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Leather goods export"},
                {"sector": "Healthcare", "growth": "High", "avg_salary": "₹3-12 LPA", "description": "JIPMER, medical tourism"},
                {"sector": "Education", "growth": "Stable", "avg_salary": "₹3-10 LPA", "description": "Central universities, institutions"},
            ],
            "it_parks": ["Puducherry Techpark (proposed)"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "SC/ST Scholarship", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST students", "website": "https://py.gov.in"},
            {"name": "OBC Scholarship", "department": "BC Welfare Dept", "amount": "₹5,000-15,000/year", "eligibility": "OBC students", "website": "https://py.gov.in"},
            {"name": "State Merit Scholarship", "department": "Education Dept", "amount": "₹5,000-10,000/year", "eligibility": "Top performers", "website": "https://py.gov.in"},
            {"name": "Girl Child Scholarship", "department": "Women Welfare Dept", "amount": "₹3,000-5,000/year", "eligibility": "Girls in higher education", "website": "https://py.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Puducherry Administration (via UPSC/SSC)",
            "psc_website": "https://py.gov.in",
            "major_exams": [
                {"exam": "UT Cadre Posts", "posts": "Administrative posts", "eligibility": "Graduation", "age": "18-30"},
                {"exam": "Puducherry Police", "posts": "SI, Constable", "eligibility": "10+2/Graduation", "age": "18-28"},
                {"exam": "UT Teachers", "posts": "TGT/PGT", "eligibility": "Graduation/PG with B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["PRTC (Transport)", "Puducherry Police", "JIPMER", "Pondicherry University"],
        },
        "industry_clusters": [
            {"name": "Puducherry Industrial Estate", "type": "Manufacturing", "companies": "Leather, textiles, electronics", "jobs_potential": "Medium", "relevant_streams": ["Engineering", "Commerce"]},
            {"name": "Karaikal Port Area", "type": "Port & Logistics", "companies": "Port operations, warehousing", "jobs_potential": "Medium", "relevant_streams": ["Commerce", "Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "150+",
            "notable_startups": ["Tourism-tech, healthcare startups"],
            "incubators": ["Pondicherry University Incubator", "NIT Puducherry TBI"],
            "govt_schemes": [
                {"name": "Puducherry Startup Support", "benefit": "Mentorship, networking", "website": "https://py.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Free Rice Scheme", "benefit": "Free rice to BPL families", "eligibility": "Ration card holders", "website": "https://py.gov.in"},
            {"name": "Marriage Assistance", "benefit": "₹25,000 for girls' marriage", "eligibility": "BPL families", "website": "https://py.gov.in"},
            {"name": "Dr. Abdul Kalam Educational Loan", "benefit": "Education loan at low interest", "eligibility": "Students in higher education", "website": "https://py.gov.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 32. JAMMU & KASHMIR
    # ───────────────────────────────────────────────────────────────────────
    "Jammu & Kashmir": {
        "job_market": {
            "major_cities": ["Srinagar", "Jammu", "Anantnag", "Baramulla", "Udhampur"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "Very High", "avg_salary": "₹2-10 LPA", "description": "Dal Lake, Gulmarg, Pahalgam"},
                {"sector": "Handicrafts", "growth": "Stable", "avg_salary": "₹2-6 LPA", "description": "Pashmina, carpets, papier-mâché"},
                {"sector": "Horticulture", "growth": "High", "avg_salary": "₹2-6 LPA", "description": "Apples, saffron, walnuts"},
                {"sector": "IT & BPO", "growth": "Emerging", "avg_salary": "₹3-10 LPA", "description": "IT parks being developed"},
                {"sector": "Education", "growth": "Stable", "avg_salary": "₹3-10 LPA", "description": "Universities, coaching"},
            ],
            "it_parks": ["IT Park Srinagar (Rangreth)", "IT Hub Jammu"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "PMSSS (PM's Special Scholarship)", "department": "AICTE/Central Govt", "amount": "₹75,000-1,25,000/year", "eligibility": "J&K students studying outside", "website": "https://aicte-india.org/schemes/students-development-schemes/PMSSS"},
            {"name": "Merit-cum-Means Scholarship", "department": "Higher Education Dept", "amount": "₹5,000-20,000/year", "eligibility": "Meritorious EWS students", "website": "https://jkscholarships.nic.in"},
            {"name": "SC/ST/OBC Scholarship", "department": "Social Welfare Dept", "amount": "Full fee + maintenance", "eligibility": "SC/ST/OBC students", "website": "https://jkscholarships.nic.in"},
            {"name": "Pragati/Saksham (AICTE)", "department": "AICTE", "amount": "₹50,000/year", "eligibility": "Girls/Divyang in technical education", "website": "https://aicte-india.org"},
        ],
        "government_jobs": {
            "psc_name": "Jammu & Kashmir Public Service Commission (JKPSC)",
            "psc_website": "https://jkpsc.nic.in",
            "major_exams": [
                {"exam": "JKAS (J&K Administrative Service)", "posts": "Deputy Commissioner, SP", "eligibility": "Graduation", "age": "21-40"},
                {"exam": "JKSSB Various Posts", "posts": "Clerks, Accounts Asst, Jr Assistants", "eligibility": "Graduation", "age": "18-40"},
                {"exam": "J&K Police SI", "posts": "Sub Inspector", "eligibility": "Graduation", "age": "18-28"},
            ],
            "other_recruiters": ["JKSRTC", "J&K Police", "J&K Bank", "JKPDD (Power)", "Tourism Dept"],
        },
        "industry_clusters": [
            {"name": "Rangreth IT Park", "type": "IT & ITES", "companies": "IT companies, BPOs", "jobs_potential": "Growing", "relevant_streams": ["Engineering"]},
            {"name": "Srinagar Handicraft Cluster", "type": "Handicrafts", "companies": "Carpet cooperatives, pashmina units", "jobs_potential": "High", "relevant_streams": ["Design", "Arts"]},
            {"name": "Sopore Apple Belt", "type": "Horticulture", "companies": "Apple processing, cold storage", "jobs_potential": "Seasonal", "relevant_streams": ["Agriculture", "Commerce"]},
        ],
        "startup_ecosystem": {
            "ranking": "Emerging",
            "total_startups": "300+",
            "notable_startups": ["Kashmir-origin handicraft e-commerce, agritech"],
            "incubators": ["J&K Entrepreneurship Development Institute", "IIT Jammu Incubator", "NIT Srinagar TBI"],
            "govt_schemes": [
                {"name": "J&K Startup Policy", "benefit": "Seed fund, tax benefits, mentorship", "website": "https://jkindustriescommerce.nic.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Mumkin Scheme", "benefit": "Vehicle loans for youth livelihood", "eligibility": "Unemployed youth", "website": "https://jk.gov.in"},
            {"name": "Himayat", "benefit": "Skill training + job placement", "eligibility": "Youth 15-35", "website": "https://himayat.jk.gov.in"},
            {"name": "Tejaswini Scheme", "benefit": "₹5 lakh loan for women entrepreneurs", "eligibility": "Women entrepreneurs 18-35", "website": "https://jkwelfare.nic.in"},
        ],
    },

    # ───────────────────────────────────────────────────────────────────────
    # 33. LADAKH
    # ───────────────────────────────────────────────────────────────────────
    "Ladakh": {
        "job_market": {
            "major_cities": ["Leh", "Kargil"],
            "top_sectors": [
                {"sector": "Tourism", "growth": "Very High", "avg_salary": "₹2-10 LPA", "description": "Pangong Lake, monasteries, adventure tourism"},
                {"sector": "Defence", "growth": "Stable", "avg_salary": "₹4-12 LPA", "description": "Army, ITBP presence"},
                {"sector": "Renewable Energy", "growth": "Very High", "avg_salary": "₹4-15 LPA", "description": "Solar power projects"},
                {"sector": "Pashmina & Handicrafts", "growth": "Medium", "avg_salary": "₹2-5 LPA", "description": "Ladakhi Pashmina, crafts"},
                {"sector": "Government Services", "growth": "Stable", "avg_salary": "₹4-10 LPA", "description": "UT Administration"},
            ],
            "it_parks": ["Proposed Digital Hub"],
            "avg_entry_salary": "₹2.5-4 LPA",
        },
        "scholarships": [
            {"name": "PMSSS", "department": "AICTE/Central Govt", "amount": "₹75,000-1,25,000/year", "eligibility": "Ladakh students studying outside", "website": "https://aicte-india.org/schemes/students-development-schemes/PMSSS"},
            {"name": "ST Scholarship", "department": "Tribal Welfare", "amount": "Full fee + maintenance", "eligibility": "ST students (majority population)", "website": "https://ladakh.gov.in"},
            {"name": "Merit Scholarship", "department": "Education Dept", "amount": "₹10,000-25,000/year", "eligibility": "Top performers", "website": "https://ladakh.gov.in"},
            {"name": "Professional Course Scholarship", "department": "Higher Education Dept", "amount": "Fee support", "eligibility": "Students in professional courses", "website": "https://ladakh.gov.in"},
        ],
        "government_jobs": {
            "psc_name": "Ladakh UT Administration (via UPSC/SSC)",
            "psc_website": "https://ladakh.gov.in",
            "major_exams": [
                {"exam": "UT Cadre Posts", "posts": "Administrative, technical posts", "eligibility": "Graduation", "age": "18-37"},
                {"exam": "Ladakh Police", "posts": "SI, Constable", "eligibility": "10+2/Graduation", "age": "18-28"},
                {"exam": "Teachers Recruitment", "posts": "TGT/PGT", "eligibility": "Graduation/PG with B.Ed", "age": "18-40"},
            ],
            "other_recruiters": ["BRO", "ITBP", "Army Civilian Posts", "Tourism Dept", "LAHDC"],
        },
        "industry_clusters": [
            {"name": "Leh Tourism Cluster", "type": "Tourism & Hospitality", "companies": "Hotels, tour operators, adventure sports", "jobs_potential": "High (seasonal)", "relevant_streams": ["Hospitality", "Commerce"]},
            {"name": "Pashmina Cluster", "type": "Handicrafts", "companies": "Pashmina cooperatives", "jobs_potential": "Medium", "relevant_streams": ["Design", "Commerce"]},
            {"name": "Solar Power Projects", "type": "Renewable Energy", "companies": "SECI, private solar developers", "jobs_potential": "Growing", "relevant_streams": ["Engineering"]},
        ],
        "startup_ecosystem": {
            "ranking": "Nascent",
            "total_startups": "50+",
            "notable_startups": ["Tourism-tech, sustainable living startups"],
            "incubators": ["Ladakh UT Entrepreneurship Cell (proposed)"],
            "govt_schemes": [
                {"name": "Ladakh Startup Support", "benefit": "Mentorship, handholding support", "website": "https://ladakh.gov.in"},
            ],
        },
        "govt_schemes": [
            {"name": "Carbon Neutral Ladakh Mission", "benefit": "Green jobs, sustainable livelihood", "eligibility": "Ladakh residents", "website": "https://ladakh.gov.in"},
            {"name": "Ladakh Autonomous Hill Development", "benefit": "Local development schemes", "eligibility": "LAHDC beneficiaries", "website": "https://leh.nic.in"},
            {"name": "Skill Development for Youth", "benefit": "Skill training in tourism, IT", "eligibility": "Youth 18-35", "website": "https://ladakh.gov.in"},
        ],
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# PUBLIC API FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
# STATE RESERVATION DATA — State-wise reservation policies for education & jobs
# ═══════════════════════════════════════════════════════════════════════════

_STATE_RESERVATION: dict[str, dict] = {
    "Andhra Pradesh": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC (Scheduled Caste)", "percentage": "15%", "details": "Mala, Madiga, Adi Andhra and other notified castes"},
            {"category": "ST (Scheduled Tribe)", "percentage": "6%", "details": "Chenchu, Gond, Koya, Lambada and other notified tribes"},
            {"category": "BC-A (Backward Class A)", "percentage": "7%", "details": "Viswabrahmin, Kummari, Vaddera and other BC-A communities"},
            {"category": "BC-B", "percentage": "10%", "details": "Yadava, Kuruma, Golla and other BC-B communities"},
            {"category": "BC-C", "percentage": "1%", "details": "Christians converted from SC/ST"},
            {"category": "BC-D", "percentage": "7%", "details": "Muslims (BC-D)"},
            {"category": "BC-E", "percentage": "4%", "details": "Kapu, Balija, Telaga, Ontari and other BC-E communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections (family income < ₹8 LPA)"},
        ],
        "applicable_to": "State engineering colleges (EAMCET), state medical colleges (NEET state quota), state universities, state government jobs (APPSC)",
        "special_provisions": [
            "Andhra Pradesh follows 50% cap as per Supreme Court mandate",
            "Kapu community included under BC-E with 4% reservation",
            "Women get 33% horizontal reservation in state government jobs",
            "PwD candidates get 4% horizontal reservation",
        ],
    },
    "Arunachal Pradesh": {
        "total_reservation": "80%",
        "categories": [
            {"category": "APST (Arunachal Pradesh Scheduled Tribe)", "percentage": "80%", "details": "All recognized indigenous tribes of Arunachal Pradesh"},
            {"category": "EWS", "percentage": "10%", "details": "From remaining 20% unreserved seats"},
        ],
        "applicable_to": "State colleges, state university admissions, state government jobs (APPSC)",
        "special_provisions": [
            "Arunachal Pradesh has one of the highest tribal reservation percentages in India",
            "Most seats in state institutions reserved for indigenous tribal communities",
            "Non-APST candidates compete for limited unreserved seats",
            "Central institutions in the state follow central reservation norms",
        ],
    },
    "Assam": {
        "total_reservation": "52%",
        "categories": [
            {"category": "SC", "percentage": "7%", "details": "Kaivarta, Hira, Jhalo Malo, Namasudra and other notified castes"},
            {"category": "ST (Plains)", "percentage": "10%", "details": "Bodo, Mising, Rabha, Tiwa and other plains tribes"},
            {"category": "ST (Hills)", "percentage": "5%", "details": "Khasi, Garo, Karbi, Dimasa and other hill tribes"},
            {"category": "OBC/MOBC", "percentage": "27%", "details": "More Other Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "State engineering/medical colleges, Gauhati University, state government jobs (APSC)",
        "special_provisions": [
            "Assam's total reservation exceeds 50% due to historical tribal provisions",
            "Separate reservation for Plains and Hills tribal communities",
            "Tea-tribe community included under OBC/MOBC category",
            "Women get 30% horizontal reservation in state government services",
        ],
    },
    "Bihar": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "Dhobi, Chamar, Musahar, Dom, Pasi and other notified castes"},
            {"category": "ST", "percentage": "1%", "details": "Santhal, Oraon, Munda, Ho and other notified tribes"},
            {"category": "EBC (Extremely Backward Class)", "percentage": "18%", "details": "Teli, Kewat, Mali, Bind and other EBC communities"},
            {"category": "BC (Backward Class)", "percentage": "12%", "details": "Yadav, Kurmi, Koeri and other BC communities"},
            {"category": "BC Women", "percentage": "3%", "details": "Women from BC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "State engineering/medical colleges, Bihar universities, state government jobs (BPSC)",
        "special_provisions": [
            "Bihar has separate EBC (18%) and BC (12%) reservation categories",
            "Additional 3% reservation for women from Backward Classes",
            "65% total reservation (including EWS) — exceeds 50% cap, subject to legal challenges",
            "Mahadalit sub-category within SC gets priority in welfare schemes",
        ],
    },
    "Chhattisgarh": {
        "total_reservation": "58%",
        "categories": [
            {"category": "SC", "percentage": "13%", "details": "Chamar, Satnami, Ganda, Mehra and other notified castes"},
            {"category": "ST", "percentage": "32%", "details": "Gond, Baiga, Halba, Kawar, Oraon and other notified tribes"},
            {"category": "OBC", "percentage": "14%", "details": "Teli, Sahu, Kurmi, Yadav and other OBC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "State colleges, Pt. Ravishankar University, state government jobs (CGPSC)",
        "special_provisions": [
            "High ST reservation (32%) due to large tribal population (~30% of state)",
            "Total reservation at 58% exceeds Supreme Court's 50% cap — upheld due to special circumstances",
            "Baiga and Kamar tribes get additional PVTG (Particularly Vulnerable Tribal Group) benefits",
            "Women get 30% horizontal reservation in state government jobs",
        ],
    },
    "Goa": {
        "total_reservation": "49%",
        "categories": [
            {"category": "SC", "percentage": "2%", "details": "Mahar, Chambhar and other notified castes"},
            {"category": "ST", "percentage": "12%", "details": "Gawda, Kunbi, Velip, Dhangar and other notified tribes"},
            {"category": "OBC", "percentage": "25%", "details": "Other Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Goa University, GEC Farmagudi, Goa Medical College, state government jobs (Goa PSC)",
        "special_provisions": [
            "Relatively low SC reservation (2%) due to small SC population",
            "Bhandari community is the largest OBC group in Goa",
            "Central institutions in Goa (NIT Goa, BITS Pilani Goa) follow central reservation",
            "PwD candidates get 4% horizontal reservation",
        ],
    },
    "Gujarat": {
        "total_reservation": "49.5%",
        "categories": [
            {"category": "SC", "percentage": "7%", "details": "Vankar, Chamar, Senva, Bhangi and other notified castes"},
            {"category": "ST", "percentage": "15%", "details": "Bhil, Rathwa, Nayaka, Dhodia, Gamit and other notified tribes"},
            {"category": "SEBC (Socially & Educationally Backward)", "percentage": "27%", "details": "Patel (partially), Koli, Thakor, Darbar and other SEBC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Gujarat Technological University, state medical colleges, state government jobs (GPSC)",
        "special_provisions": [
            "Patidar community has been demanding OBC reservation — EWS quota partially addresses this",
            "Gujarat was one of the first states to implement EWS reservation",
            "High ST reservation (15%) due to significant tribal population in eastern districts",
            "Women get 33% horizontal reservation in state government services",
        ],
    },
    "Haryana": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "20%", "details": "Chamar, Balmiki, Dhanak, Khatik and other notified castes"},
            {"category": "BC-A", "percentage": "16%", "details": "Ahir (Yadav), Gujjar, Saini, Lodh and other BC-A communities"},
            {"category": "BC-B", "percentage": "11%", "details": "Jat and other BC-B communities (in some categories)"},
            {"category": "SBC (Special Backward Class)", "percentage": "3%", "details": "Special Backward Class communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "State engineering/medical colleges, MDU Rohtak, KUK, state government jobs (HPSC)",
        "special_provisions": [
            "High SC reservation (20%) due to large Dalit population",
            "Jat community included as BC-B after prolonged legal battles",
            "Haryana provides reservation in private sector jobs for state domiciles (75% quota in ₹50K/month salary jobs)",
            "Ex-servicemen and their dependents get additional reservation benefits",
        ],
    },
    "Himachal Pradesh": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "25%", "details": "Chamar, Koli, Hali, Doom, Dagee and other notified castes"},
            {"category": "ST", "percentage": "5%", "details": "Gaddi, Gujjar, Kinnaura, Lahaula and other notified tribes"},
            {"category": "OBC", "percentage": "20%", "details": "Other Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "HP University, state engineering/medical colleges, state government jobs (HPPSC)",
        "special_provisions": [
            "One of the highest SC reservation percentages (25%) among Indian states",
            "Tribal communities in Kinnaur, Lahaul-Spiti get special area considerations",
            "State domicile required for state quota benefits",
            "PwD candidates get 5% horizontal reservation",
        ],
    },
    "Jharkhand": {
        "total_reservation": "60%",
        "categories": [
            {"category": "SC", "percentage": "10%", "details": "Chamar, Dhobi, Dom, Musahar and other notified castes"},
            {"category": "ST", "percentage": "26%", "details": "Santhal, Munda, Ho, Oraon, Kharia, Birhor and other notified tribes"},
            {"category": "OBC-I", "percentage": "14%", "details": "Other Backward Class – I"},
            {"category": "OBC-II", "percentage": "12%", "details": "Other Backward Class – II"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Ranchi University, BIT Mesra (state quota), state government jobs (JPSC)",
        "special_provisions": [
            "High ST reservation (26%) reflecting large tribal population",
            "Total reservation at 60% exceeds 50% cap — subject to ongoing legal review",
            "PVTG communities (Birhor, Asur, Sauria Paharia) get additional welfare benefits",
            "Local domicile reservation applies for state government jobs",
        ],
    },
    "Karnataka": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "15%", "details": "Adi Karnataka, Madiga, Bhovi, Lambani and other notified castes"},
            {"category": "ST", "percentage": "3%", "details": "Soliga, Jenu Kuruba, Iruliga and other notified tribes"},
            {"category": "OBC (Category I)", "percentage": "4%", "details": "Category I backward communities"},
            {"category": "OBC (Category IIA)", "percentage": "15%", "details": "Vokkaliga, Lingayat, Kuruba and other communities"},
            {"category": "OBC (Category IIB)", "percentage": "4%", "details": "Muslim OBC communities"},
            {"category": "OBC (Category IIIA)", "percentage": "4%", "details": "Category IIIA backward communities"},
            {"category": "OBC (Category IIIB)", "percentage": "5%", "details": "Category IIIB backward communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "VTU, state medical colleges (KCET), Karnataka state universities, state government jobs (KPSC)",
        "special_provisions": [
            "Karnataka has a highly detailed multi-tier OBC classification (Cat I, IIA, IIB, IIIA, IIIB)",
            "Hyderabad-Karnataka region gets special reservation under Article 371(J)",
            "Kannada medium students get additional preference in state admissions",
            "Rural candidates get preference in some state recruitment categories",
        ],
    },
    "Kerala": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "8%", "details": "Pulaya, Paraya, Cheruma, Kuravan and other notified castes"},
            {"category": "ST", "percentage": "2%", "details": "Paniya, Irula, Kattunaikan, Adiya and other notified tribes"},
            {"category": "OBC (SEBC)", "percentage": "40%", "details": "Ezhava/Thiyya (14%), Muslim (12%), Latin Catholic/SIUC (4%), OBC Christians (2%), Dheevara (2%), Vishwakarma (2%), Other SEBC (4%)"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Kerala University, CUSAT, state medical/engineering colleges (KEAM), state government jobs (Kerala PSC)",
        "special_provisions": [
            "Kerala has one of the most detailed OBC sub-classifications in India",
            "Ezhava/Thiyya community gets 14% within OBC quota — largest single community reservation",
            "Muslim community gets 12% within OBC reservation",
            "Community-wise merit lists ensure equitable distribution within OBC",
        ],
    },
    "Madhya Pradesh": {
        "total_reservation": "63%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "Chamar, Bhangi, Balai, Meghwal and other notified castes"},
            {"category": "ST", "percentage": "20%", "details": "Bhil, Gond, Kol, Baiga, Korku and other notified tribes"},
            {"category": "OBC", "percentage": "27%", "details": "Other Backward Classes including Yadav, Teli, Kurmi"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "RGPV, state medical colleges, MP state universities, state government jobs (MPPSC)",
        "special_provisions": [
            "Total reservation at 63% exceeds 50% cap — challenged in courts",
            "High ST reservation (20%) due to large tribal population in eastern MP",
            "Baiga, Bharia, Saharia tribes get PVTG status with additional benefits",
            "Women get 33% horizontal reservation in state government jobs",
        ],
    },
    "Maharashtra": {
        "total_reservation": "52%",
        "categories": [
            {"category": "SC", "percentage": "13%", "details": "Mahar, Matang, Chambhar, Dhor and other notified castes"},
            {"category": "ST", "percentage": "7%", "details": "Bhil, Warli, Gond, Mahadeo Koli, Katkari and other notified tribes"},
            {"category": "OBC", "percentage": "19%", "details": "Kunbi, Mali, Dhangar, Teli and other OBC communities"},
            {"category": "VJNT (De-notified Tribes)", "percentage": "3%", "details": "Vimukta Jati and Nomadic Tribes"},
            {"category": "SBC (Special Backward)", "percentage": "2%", "details": "Special Backward Class communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Mumbai University, state engineering (MHT CET), state medical colleges, state government jobs (MPSC)",
        "special_provisions": [
            "Maharashtra has unique VJNT (De-notified Tribes) and SBC categories",
            "Maratha reservation (up to 10%) has been subject to ongoing legal battles — currently stayed by Supreme Court",
            "52% reservation (without Maratha quota) slightly exceeds 50% cap",
            "Women get 30% horizontal reservation in state government services",
        ],
    },
    "Manipur": {
        "total_reservation": "56%",
        "categories": [
            {"category": "SC", "percentage": "3%", "details": "Lois, Yaithibi and other notified castes"},
            {"category": "ST", "percentage": "34%", "details": "Naga, Kuki, Hmar, Mizo, Anal and other hill tribes"},
            {"category": "OBC", "percentage": "17%", "details": "Other Backward Classes including Meitei Muslims"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Manipur University, state colleges, state government jobs (MPSC Manipur)",
        "special_provisions": [
            "High ST reservation (34%) due to large tribal population in hill districts",
            "Separate provisions for Meitei community in valley areas",
            "Hill area vs Valley area seat distribution in some state institutions",
            "Inner Line Permit (ILP) requirement affects non-local admissions",
        ],
    },
    "Meghalaya": {
        "total_reservation": "80%",
        "categories": [
            {"category": "ST (Khasi)", "percentage": "40%", "details": "Khasi and Jaintia tribal communities"},
            {"category": "ST (Garo)", "percentage": "40%", "details": "Garo tribal communities"},
            {"category": "EWS", "percentage": "10%", "details": "From remaining 20% unreserved seats"},
        ],
        "applicable_to": "NEHU, state colleges, state government jobs (MPSC Meghalaya)",
        "special_provisions": [
            "Meghalaya has 80% tribal reservation — one of the highest in India",
            "Equal split between Khasi (40%) and Garo (40%) tribal groups",
            "Non-tribal candidates compete for only 20% unreserved seats",
            "Sixth Schedule areas have additional autonomous district council provisions",
        ],
    },
    "Mizoram": {
        "total_reservation": "80%",
        "categories": [
            {"category": "ST", "percentage": "80%", "details": "Mizo (Lushai), Lai, Mara, Chakma and other notified tribes"},
            {"category": "EWS", "percentage": "10%", "details": "From remaining unreserved seats"},
        ],
        "applicable_to": "Mizoram University, state colleges, state government jobs (MPSC Mizoram)",
        "special_provisions": [
            "Mizoram has 80% tribal reservation — among the highest nationally",
            "Almost entire population belongs to Scheduled Tribe category (~95%)",
            "Inner Line Permit required for non-Mizo residents",
            "Central institutions (MZU, NIT Mizoram) follow central reservation norms",
        ],
    },
    "Nagaland": {
        "total_reservation": "80%",
        "categories": [
            {"category": "ST (Naga Tribes)", "percentage": "80%", "details": "Angami, Ao, Sema, Lotha, Chakhesang, Rengma and other Naga tribes"},
            {"category": "EWS", "percentage": "10%", "details": "From remaining unreserved seats"},
        ],
        "applicable_to": "Nagaland University, state colleges, state government jobs (NPSC)",
        "special_provisions": [
            "80% tribal reservation reflecting predominantly tribal population",
            "Article 371(A) provides special provisions for Nagaland — Naga customary law protected",
            "Inner Line Permit requirement for non-Naga residents",
            "Tribe-wise roster system ensures representation of all Naga tribes",
        ],
    },
    "Odisha": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "Bauri, Chamar, Dom, Hadi, Pana and other notified castes"},
            {"category": "ST", "percentage": "22%", "details": "Gond, Kandha, Santhal, Saora, Bonda and other notified tribes"},
            {"category": "SEBC (OBC)", "percentage": "11%", "details": "Socially & Educationally Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Utkal University, state engineering/medical colleges, state government jobs (OPSC)",
        "special_provisions": [
            "High ST reservation (22%) due to significant tribal population",
            "13 PVTG communities (Bonda, Dongria Kondh, etc.) get additional welfare support",
            "Women get 33% horizontal reservation in state government jobs",
            "Odisha follows strict 50% cap as per Supreme Court guidelines",
        ],
    },
    "Punjab": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "25%", "details": "Mazhabi Sikh, Ravidasia, Ad Dharmi, Balmiki and other notified castes"},
            {"category": "BC (Backward Class)", "percentage": "12%", "details": "Tarkhaan, Kumhar, Nai, Saini and other BC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
            {"category": "Ex-Servicemen", "percentage": "3%", "details": "From unreserved category"},
            {"category": "Sports Persons", "percentage": "2%", "details": "Sports quota in state institutions"},
        ],
        "applicable_to": "Punjabi University, Punjab Engineering College, state medical colleges, state government jobs (PPSC)",
        "special_provisions": [
            "High SC reservation (25%) — among the highest in India due to large Dalit population",
            "Separate sub-categories within SC: Mazhabi Sikh / Balmiki get 50% of SC quota",
            "Additional reservation for ex-servicemen (3%) and sports persons (2%)",
            "Rural area candidates get preference in some recruitment categories",
        ],
    },
    "Rajasthan": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "Meghwal, Bairwa, Balai, Khatik and other notified castes"},
            {"category": "ST", "percentage": "12%", "details": "Meena, Bhil, Garasia, Saharia and other notified tribes"},
            {"category": "OBC", "percentage": "21%", "details": "Jat, Gujjar, Mali, Teli and other OBC communities"},
            {"category": "MBC (Most Backward)", "percentage": "1%", "details": "Most Backward Classes — Gujjar and 4 other communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Rajasthan University, state engineering/medical colleges, state government jobs (RPSC)",
        "special_provisions": [
            "Gujjar community gets additional MBC reservation after prolonged agitations",
            "Meena community is the largest ST group in Rajasthan",
            "Women get 30% horizontal reservation in state government services",
            "State follows strict 50% cap as per Supreme Court mandate",
        ],
    },
    "Sikkim": {
        "total_reservation": "70%",
        "categories": [
            {"category": "SC", "percentage": "5%", "details": "Kami, Damai, Sarki and other notified castes"},
            {"category": "ST (Bhutia-Lepcha)", "percentage": "33%", "details": "Bhutia, Lepcha and other notified tribes"},
            {"category": "OBC", "percentage": "22%", "details": "Newar, Gurung, Tamang, Rai, Limbu and other OBC communities"},
            {"category": "MBC (Most Backward)", "percentage": "10%", "details": "Most Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Sikkim University, state colleges, state government jobs (SPSC)",
        "special_provisions": [
            "Sikkim has 70% total reservation — exceeds 50% cap due to special provisions",
            "Article 371(F) provides special provisions for Sikkim",
            "Bhutia-Lepcha communities get 33% reservation",
            "Local/subject/domicile certificate required for state reservation benefits",
        ],
    },
    "Tamil Nadu": {
        "total_reservation": "69%",
        "categories": [
            {"category": "SC", "percentage": "18%", "details": "Adi Dravida, Pallar, Paraiyar, Chakkiliar and other notified castes"},
            {"category": "SC (Arunthathiyar)", "percentage": "3%", "details": "Arunthathiyar sub-group within SC"},
            {"category": "ST", "percentage": "1%", "details": "Irular, Kadar, Toda, Kota and other notified tribes"},
            {"category": "BC (Backward Class)", "percentage": "26.5%", "details": "Nadar, Thevar, Vanniyar, Mudaliar and other BC communities"},
            {"category": "BC (Muslim)", "percentage": "3.5%", "details": "Muslim community under BC"},
            {"category": "MBC (Most Backward)", "percentage": "20%", "details": "Vanniyar (10.5% within MBC), and other MBC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Anna University, state medical colleges (NEET state quota), state government jobs (TNPSC)",
        "special_provisions": [
            "Tamil Nadu has 69% reservation — highest among major states, protected by 9th Schedule",
            "Placed in 9th Schedule of Constitution to protect from judicial review",
            "Separate 3% reservation for Arunthathiyar (most oppressed SC sub-group)",
            "Vanniyar community gets 10.5% internal reservation within MBC quota",
            "No creamy layer concept applied for BC/MBC in Tamil Nadu",
        ],
    },
    "Telangana": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "15%", "details": "Madiga, Mala, Adi Andhra and other notified castes"},
            {"category": "ST", "percentage": "6%", "details": "Gond, Lambada, Koya, Chenchu and other notified tribes"},
            {"category": "BC-A", "percentage": "7%", "details": "Backward Class A communities"},
            {"category": "BC-B", "percentage": "10%", "details": "Backward Class B communities including Yadava"},
            {"category": "BC-C", "percentage": "1%", "details": "SC/ST converts to Christianity"},
            {"category": "BC-D", "percentage": "7%", "details": "Muslim OBC communities"},
            {"category": "BC-E", "percentage": "4%", "details": "Kapu, Balija and other BC-E communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "JNTU Hyderabad, Osmania University, state medical colleges, state government jobs (TSPSC)",
        "special_provisions": [
            "Telangana follows similar reservation structure as Andhra Pradesh (parent state)",
            "Telangana state domicile required for state quota benefits",
            "Local area preference in Telangana state government jobs",
            "Women get 33% horizontal reservation in state government services",
        ],
    },
    "Tripura": {
        "total_reservation": "55%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "Dhobi, Muchi, Namasudra, Patni and other notified castes"},
            {"category": "ST", "percentage": "31%", "details": "Tripuri, Reang, Jamatia, Chakma, Halam and other notified tribes"},
            {"category": "OBC", "percentage": "2%", "details": "Other Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Tripura University, state colleges, state government jobs (TPSC)",
        "special_provisions": [
            "High ST reservation (31%) reflecting significant tribal population",
            "Tripura Tribal Areas Autonomous District Council has additional provisions",
            "Bengali and tribal language medium education both available",
            "Particularly Vulnerable Tribal Groups (Reang) get additional welfare support",
        ],
    },
    "Uttar Pradesh": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "21%", "details": "Chamar, Pasi, Dhobi, Kori, Balmiki and other notified castes"},
            {"category": "ST", "percentage": "2%", "details": "Tharu, Buksa, Bhotia, Raji and other notified tribes"},
            {"category": "OBC", "percentage": "27%", "details": "Yadav, Kurmi, Lodh, Kushwaha, Jat and other OBC communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "UP state universities, state engineering/medical colleges, state government jobs (UPPSC)",
        "special_provisions": [
            "Highest SC reservation (21%) among Indian states due to large Dalit population",
            "UP has the largest number of reserved seats in absolute terms",
            "Women get 33% horizontal reservation in state government jobs (recently increased from 20%)",
            "Freedom fighter and ex-servicemen dependents get additional reservation benefits",
        ],
    },
    "Uttarakhand": {
        "total_reservation": "50%",
        "categories": [
            {"category": "SC", "percentage": "19%", "details": "Chamar, Dom, Kol, Badi and other notified castes"},
            {"category": "ST", "percentage": "4%", "details": "Tharu, Buksa, Bhotia, Jaunsari and other notified tribes"},
            {"category": "OBC", "percentage": "14%", "details": "Other Backward Classes"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "GBPUAT, state engineering/medical colleges, state government jobs (UKPSC)",
        "special_provisions": [
            "High SC reservation (19%) carried forward from parent state UP",
            "Hill area candidates get additional relaxation in some recruitment",
            "Women get 30% horizontal reservation in state government services",
            "Uttarakhand follows strict 50% cap as per Supreme Court mandate",
        ],
    },
    "West Bengal": {
        "total_reservation": "45%",
        "categories": [
            {"category": "SC", "percentage": "22%", "details": "Rajbanshi, Namasudra, Pod, Bagdi, Chamar and other notified castes"},
            {"category": "ST", "percentage": "6%", "details": "Santhal, Oraon, Munda, Bhumij and other notified tribes"},
            {"category": "OBC-A", "percentage": "10%", "details": "OBC sub-group A — Muslim OBC and other communities"},
            {"category": "OBC-B", "percentage": "7%", "details": "OBC sub-group B — other backward communities"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Jadavpur University, Calcutta University, state engineering/medical colleges, state government jobs (WBPSC)",
        "special_provisions": [
            "High SC reservation (22%) — second highest among states",
            "West Bengal has sub-divided OBC into OBC-A and OBC-B categories",
            "Total reservation at 45% (without EWS) is below 50% cap",
            "Women get 35% horizontal reservation in state government jobs — among the highest",
        ],
    },
    "Delhi": {
        "total_reservation": "49.5%",
        "categories": [
            {"category": "SC", "percentage": "15%", "details": "Chamar, Balmiki, Khatik, Jatav and other notified castes"},
            {"category": "ST", "percentage": "7.5%", "details": "Delhi has negligible ST population; seats often remain vacant"},
            {"category": "OBC", "percentage": "27%", "details": "Other Backward Classes as per central list"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Delhi University, IP University, DTU, NSUT, state government jobs (DSSSB)",
        "special_provisions": [
            "Delhi follows central reservation norms being a Union Territory",
            "Delhi University has 85% Delhi quota with central reservation norms",
            "DSSSB recruitment follows central government reservation policy",
            "ST reservation seats often remain unfilled due to negligible ST population",
        ],
    },
    "Chandigarh": {
        "total_reservation": "49.5%",
        "categories": [
            {"category": "SC", "percentage": "15%", "details": "As per central SC list"},
            {"category": "ST", "percentage": "7.5%", "details": "As per central ST list"},
            {"category": "OBC", "percentage": "27%", "details": "As per central OBC list"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "PU Chandigarh, PEC, GGDSD College, UT administration jobs",
        "special_provisions": [
            "Chandigarh follows central reservation norms as a UT",
            "Panjab University has its own reservation policy following central norms",
            "PEC Chandigarh follows central reservation for admissions",
            "UT administration recruitment follows central government norms",
        ],
    },
    "Puducherry": {
        "total_reservation": "49.5%",
        "categories": [
            {"category": "SC", "percentage": "16%", "details": "As per Puducherry SC list"},
            {"category": "ST", "percentage": "0%", "details": "No ST population in Puducherry"},
            {"category": "OBC", "percentage": "33.5%", "details": "Other Backward Classes as per Puducherry list"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "Pondicherry University, JIPMER (state quota), state government jobs (UT Administration)",
        "special_provisions": [
            "Puducherry has no ST reservation as there is no ST population",
            "Higher OBC reservation (33.5%) to compensate for zero ST reservation",
            "JIPMER follows central reservation for its seats",
            "French-origin residents get some consideration in state government jobs",
        ],
    },
    "Jammu & Kashmir": {
        "total_reservation": "54%",
        "categories": [
            {"category": "SC", "percentage": "8%", "details": "As per J&K SC list"},
            {"category": "ST", "percentage": "10%", "details": "Gujjar, Bakerwal and other notified tribes"},
            {"category": "OBC", "percentage": "4%", "details": "Other Backward Classes"},
            {"category": "RBA (Resident of Backward Area)", "percentage": "10%", "details": "Residents of backward/remote areas like Poonch, Rajouri, Doda"},
            {"category": "ALC (Actual Line of Control)", "percentage": "2%", "details": "Residents near LoC areas"},
            {"category": "PSP (Pahari Speaking People)", "percentage": "4%", "details": "Pahari speaking community — newly added"},
            {"category": "EWS", "percentage": "10%", "details": "Economically Weaker Sections"},
        ],
        "applicable_to": "University of Jammu, University of Kashmir, NIT Srinagar (state quota), state government jobs (JKPSC)",
        "special_provisions": [
            "J&K has unique reservation categories like RBA, ALC, and PSP not found in other states",
            "Gujjar and Bakerwal communities are the major ST groups",
            "After abrogation of Article 370, central reservation norms apply to central institutions",
            "Kashmiri Pandit migrants have reserved seats in J&K educational institutions",
            "Ladakh UT now has separate reservation policy",
        ],
    },
    "Ladakh": {
        "total_reservation": "75%",
        "categories": [
            {"category": "ST", "percentage": "75%", "details": "Balti, Beda, Bot, Brokpa, Changpa, Mon, Purigpa and other notified tribes"},
            {"category": "EWS", "percentage": "10%", "details": "From remaining unreserved seats"},
        ],
        "applicable_to": "University of Ladakh, state colleges, UT administration jobs",
        "special_provisions": [
            "Ladakh has 75% ST reservation reflecting predominantly tribal population",
            "Newly formed UT — reservation policies still evolving",
            "Central institutions follow central reservation norms",
            "Special provisions under 6th Schedule being discussed for Ladakh",
        ],
    },
}

# ═══════════════════════════════════════════════════════════════════════════

def get_all_states() -> list[str]:
    """Return list of all states in the data."""
    return list(_STATE_OPPORTUNITIES.keys())


def get_state_data(state: str) -> dict | None:
    """Return full data for a given state, or None if not found."""
    data = _STATE_OPPORTUNITIES.get(state)
    if data is None:
        return None
    result = dict(data)
    reservation = _STATE_RESERVATION.get(state)
    if reservation:
        result["reservation"] = reservation
    return result


def get_all_state_data() -> dict[str, dict]:
    """Return all state data (for template rendering)."""
    result = {}
    for state, data in _STATE_OPPORTUNITIES.items():
        entry = dict(data)
        reservation = _STATE_RESERVATION.get(state)
        if reservation:
            entry["reservation"] = reservation
        result[state] = entry
    return result
