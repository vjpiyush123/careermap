"""Static career paths data for all 14 streams.

This module provides the complete career tree structure, college data,
career options, and industry mappings used by the deterministic analysis engine.
All data is static and deterministic — no LLM involvement.
"""

from __future__ import annotations

from careerguide.models.career import CareerOption, College, CareerTree, StreamNode


# ---------------------------------------------------------------------------
# Helper to build colleges — keeps the data declarations compact
# ---------------------------------------------------------------------------

def _college(
    name: str,
    ranking: int,
    city: str,
    state: str,
    avg_fees_lpa: float,
    avg_placement_lpa: float,
    total_seats: int,
    website: str = "",
    branches: list[str] | None = None,
) -> College:
    return College(
        name=name,
        ranking=ranking,
        city=city,
        state=state,
        avg_fees_lpa=avg_fees_lpa,
        avg_placement_lpa=avg_placement_lpa,
        total_seats=total_seats,
        website=website,
        branches=branches or [],
    )


# ═══════════════════════════════════════════════════════════════════════════
# 1. ENGINEERING & TECHNOLOGY
# ═══════════════════════════════════════════════════════════════════════════

_ENGINEERING_COLLEGES_INDIA: list[College] = [
    _college("IIT Bombay", 1, "Mumbai", "Maharashtra", 2.5, 21.0, 1200, "https://www.iitb.ac.in", ["CSE", "EE", "ME", "CE", "CH"]),
    _college("IIT Delhi", 2, "New Delhi", "Delhi", 2.5, 20.0, 1100, "https://home.iitd.ac.in", ["CSE", "EE", "ME", "CE"]),
    _college("IIT Madras", 3, "Chennai", "Tamil Nadu", 2.5, 19.5, 1050, "https://www.iitm.ac.in", ["CSE", "EE", "ME", "CE"]),
    _college("IIT Kanpur", 4, "Kanpur", "Uttar Pradesh", 2.5, 18.0, 1000, "https://www.iitk.ac.in", ["CSE", "EE", "ME"]),
    _college("IIT Kharagpur", 5, "Kharagpur", "West Bengal", 2.5, 17.5, 1500, "https://www.iitkgp.ac.in", ["CSE", "EE", "ME", "CE", "AG"]),
    _college("IIT Roorkee", 6, "Roorkee", "Uttarakhand", 2.5, 16.0, 1100, "https://www.iitr.ac.in", ["CSE", "EE", "CE"]),
    _college("IIT Guwahati", 7, "Guwahati", "Assam", 2.5, 15.0, 900, "https://www.iitg.ac.in", ["CSE", "EE", "ME"]),
    _college("IIT Hyderabad", 8, "Hyderabad", "Telangana", 2.5, 16.0, 800, "https://iith.ac.in", ["CSE", "EE", "ME"]),
    _college("NIT Trichy", 9, "Tiruchirappalli", "Tamil Nadu", 1.5, 12.0, 1200, "https://www.nitt.edu", ["CSE", "EE", "ME", "CE"]),
    _college("BITS Pilani", 10, "Pilani", "Rajasthan", 4.5, 14.0, 900, "https://www.bits-pilani.ac.in", ["CSE", "EE", "ME", "CH"]),
]

_ENGINEERING_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Maharashtra": [
        _college("IIT Bombay", 1, "Mumbai", "Maharashtra", 2.5, 21.0, 1200, "https://www.iitb.ac.in"),
        _college("VJTI Mumbai", 2, "Mumbai", "Maharashtra", 0.8, 8.0, 600, "https://vjti.ac.in"),
        _college("COEP Pune", 3, "Pune", "Maharashtra", 0.6, 7.5, 700, "https://www.coep.org.in"),
        _college("Veermata Jijabai Technological Institute", 4, "Mumbai", "Maharashtra", 0.8, 7.0, 480, ""),
        _college("ICT Mumbai", 5, "Mumbai", "Maharashtra", 1.5, 10.0, 400, "https://www.ict.ac.in"),
    ],
    "Tamil Nadu": [
        _college("IIT Madras", 1, "Chennai", "Tamil Nadu", 2.5, 19.5, 1050, "https://www.iitm.ac.in"),
        _college("NIT Trichy", 2, "Tiruchirappalli", "Tamil Nadu", 1.5, 12.0, 1200, "https://www.nitt.edu"),
        _college("Anna University", 3, "Chennai", "Tamil Nadu", 0.5, 5.0, 3000, "https://www.annauniv.edu"),
        _college("PSG College of Technology", 4, "Coimbatore", "Tamil Nadu", 1.0, 6.0, 800, ""),
        _college("SSN College of Engineering", 5, "Chennai", "Tamil Nadu", 2.0, 8.0, 600, ""),
    ],
    "Delhi": [
        _college("IIT Delhi", 1, "New Delhi", "Delhi", 2.5, 20.0, 1100, "https://home.iitd.ac.in"),
        _college("DTU (Delhi Technological University)", 2, "New Delhi", "Delhi", 1.7, 12.0, 1700, "http://dtu.ac.in"),
        _college("NSUT (Netaji Subhas University of Technology)", 3, "New Delhi", "Delhi", 1.5, 11.0, 1200, ""),
        _college("IIIT Delhi", 4, "New Delhi", "Delhi", 3.0, 15.0, 500, "https://iiitd.ac.in"),
        _college("Jamia Millia Islamia", 5, "New Delhi", "Delhi", 0.5, 5.0, 400, ""),
    ],
    "Karnataka": [
        _college("IISc Bangalore", 1, "Bangalore", "Karnataka", 0.5, 22.0, 400, "https://iisc.ac.in"),
        _college("NIT Karnataka Surathkal", 2, "Surathkal", "Karnataka", 1.5, 12.0, 900, "https://www.nitk.ac.in"),
        _college("RV College of Engineering", 3, "Bangalore", "Karnataka", 3.0, 8.0, 800, ""),
        _college("PES University", 4, "Bangalore", "Karnataka", 4.0, 9.0, 1000, ""),
        _college("BMS College of Engineering", 5, "Bangalore", "Karnataka", 2.5, 7.0, 700, ""),
    ],
    "West Bengal": [
        _college("IIT Kharagpur", 1, "Kharagpur", "West Bengal", 2.5, 17.5, 1500, "https://www.iitkgp.ac.in"),
        _college("Jadavpur University", 2, "Kolkata", "West Bengal", 0.2, 7.0, 1500, "http://www.jaduniv.edu.in"),
        _college("NIT Durgapur", 3, "Durgapur", "West Bengal", 1.2, 8.0, 900, ""),
        _college("IIEST Shibpur", 4, "Howrah", "West Bengal", 1.0, 7.5, 700, ""),
        _college("Heritage Institute of Technology", 5, "Kolkata", "West Bengal", 2.0, 5.0, 600, ""),
    ],
    "Uttar Pradesh": [
        _college("IIT Kanpur", 1, "Kanpur", "Uttar Pradesh", 2.5, 18.0, 1000, "https://www.iitk.ac.in"),
        _college("IIT BHU Varanasi", 2, "Varanasi", "Uttar Pradesh", 2.5, 15.0, 1100, "https://iitbhu.ac.in"),
        _college("MNNIT Allahabad", 3, "Prayagraj", "Uttar Pradesh", 1.2, 9.0, 800, ""),
        _college("HBTU Kanpur", 4, "Kanpur", "Uttar Pradesh", 0.5, 5.0, 600, ""),
        _college("Aligarh Muslim University", 5, "Aligarh", "Uttar Pradesh", 0.5, 4.0, 500, ""),
    ],
    "Rajasthan": [
        _college("BITS Pilani", 1, "Pilani", "Rajasthan", 4.5, 14.0, 900, "https://www.bits-pilani.ac.in"),
        _college("MNIT Jaipur", 2, "Jaipur", "Rajasthan", 1.5, 10.0, 800, ""),
        _college("LNMIIT Jaipur", 3, "Jaipur", "Rajasthan", 2.5, 7.0, 400, ""),
        _college("Manipal University Jaipur", 4, "Jaipur", "Rajasthan", 3.0, 5.0, 1000, ""),
        _college("Poornima University", 5, "Jaipur", "Rajasthan", 1.5, 4.0, 800, ""),
    ],
    "Telangana": [
        _college("IIT Hyderabad", 1, "Hyderabad", "Telangana", 2.5, 16.0, 800, "https://iith.ac.in"),
        _college("IIIT Hyderabad", 2, "Hyderabad", "Telangana", 3.5, 18.0, 500, "https://www.iiit.ac.in"),
        _college("NIT Warangal", 3, "Warangal", "Telangana", 1.5, 12.0, 900, ""),
        _college("CBIT Hyderabad", 4, "Hyderabad", "Telangana", 1.5, 6.0, 700, ""),
        _college("VNR VJIET", 5, "Hyderabad", "Telangana", 2.0, 5.0, 600, ""),
    ],
}

_ENGINEERING_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Software Engineer", description="Design, develop, and maintain software systems", industries=["IT", "Fintech", "E-commerce", "SaaS"], typical_roles=["SDE", "Backend Dev", "Frontend Dev", "Full Stack Dev"], avg_starting_salary_lpa=8.0, growth_india="Very High – India's IT sector projected to reach $350B by 2030", growth_abroad="Very High – Global demand for software engineers remains strong"),
    CareerOption(name="Data Scientist", description="Analyze large datasets to extract insights and build predictive models", industries=["IT", "Finance", "Healthcare", "E-commerce"], typical_roles=["Data Analyst", "ML Engineer", "Data Scientist"], avg_starting_salary_lpa=7.0, growth_india="High – Growing AI/ML adoption across industries", growth_abroad="High – One of the fastest growing careers globally"),
    CareerOption(name="Mechanical Engineer", description="Design and manufacture mechanical systems and products", industries=["Automotive", "Aerospace", "Manufacturing", "Energy"], typical_roles=["Design Engineer", "Production Engineer", "R&D Engineer"], avg_starting_salary_lpa=4.5, growth_india="Moderate – Manufacturing push under Make in India", growth_abroad="Moderate – Steady demand in automotive and aerospace"),
    CareerOption(name="Civil Engineer", description="Plan, design, and oversee construction of infrastructure", industries=["Construction", "Real Estate", "Government", "Infrastructure"], typical_roles=["Structural Engineer", "Site Engineer", "Project Manager"], avg_starting_salary_lpa=4.0, growth_india="High – Massive infrastructure development ongoing", growth_abroad="Moderate – Stable demand in urban planning"),
    CareerOption(name="Electrical Engineer", description="Design and develop electrical systems and equipment", industries=["Power", "Electronics", "Automotive", "Telecom"], typical_roles=["Power Systems Engineer", "Control Engineer", "Electronics Designer"], avg_starting_salary_lpa=5.0, growth_india="High – EV and renewable energy sectors expanding", growth_abroad="Moderate-High – Green energy transition driving demand"),
]

_ENGINEERING_COACHING: list[str] = [
    "Allen Career Institute (Kota)",
    "FIITJEE",
    "Resonance Eduventures",
    "Aakash Institute",
    "Narayana Group",
    "Vidyamandir Classes (VMC)",
    "Bansal Classes",
    "Motion Education",
    "Unacademy (Online)",
    "Physics Wallah (Online)",
]

# ═══════════════════════════════════════════════════════════════════════════
# 2. MEDICAL & HEALTHCARE
# ═══════════════════════════════════════════════════════════════════════════

_MEDICAL_COLLEGES_INDIA: list[College] = [
    _college("AIIMS New Delhi", 1, "New Delhi", "Delhi", 0.1, 15.0, 100, "https://www.aiims.edu", ["MBBS", "BDS", "Nursing"]),
    _college("PGIMER Chandigarh", 2, "Chandigarh", "Chandigarh", 0.1, 14.0, 75, "https://pgimer.edu.in", ["MBBS"]),
    _college("CMC Vellore", 3, "Vellore", "Tamil Nadu", 0.5, 12.0, 100, "https://www.cmch-vellore.edu", ["MBBS", "BDS"]),
    _college("JIPMER Puducherry", 4, "Puducherry", "Puducherry", 0.1, 12.0, 150, "https://jipmer.edu.in", ["MBBS"]),
    _college("Maulana Azad Medical College", 5, "New Delhi", "Delhi", 0.05, 10.0, 250, "", ["MBBS", "BDS"]),
    _college("King George's Medical University", 6, "Lucknow", "Uttar Pradesh", 0.2, 8.0, 250, "", ["MBBS"]),
    _college("Armed Forces Medical College", 7, "Pune", "Maharashtra", 0.1, 12.0, 150, "", ["MBBS"]),
    _college("Grant Medical College", 8, "Mumbai", "Maharashtra", 0.1, 9.0, 200, "", ["MBBS"]),
    _college("Kasturba Medical College", 9, "Manipal", "Karnataka", 3.0, 10.0, 250, "https://manipal.edu", ["MBBS"]),
    _college("Madras Medical College", 10, "Chennai", "Tamil Nadu", 0.1, 8.0, 250, "", ["MBBS"]),
]

_MEDICAL_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Maharashtra": [
        _college("Armed Forces Medical College", 1, "Pune", "Maharashtra", 0.1, 12.0, 150, ""),
        _college("Grant Medical College", 2, "Mumbai", "Maharashtra", 0.1, 9.0, 200, ""),
        _college("BJ Government Medical College", 3, "Pune", "Maharashtra", 0.1, 8.0, 200, ""),
        _college("Seth GS Medical College", 4, "Mumbai", "Maharashtra", 0.1, 9.0, 180, ""),
        _college("LTMMC Sion", 5, "Mumbai", "Maharashtra", 0.1, 7.0, 200, ""),
    ],
    "Delhi": [
        _college("AIIMS New Delhi", 1, "New Delhi", "Delhi", 0.1, 15.0, 100, "https://www.aiims.edu"),
        _college("Maulana Azad Medical College", 2, "New Delhi", "Delhi", 0.05, 10.0, 250, ""),
        _college("Lady Hardinge Medical College", 3, "New Delhi", "Delhi", 0.05, 9.0, 200, ""),
        _college("UCMS & GTB Hospital", 4, "New Delhi", "Delhi", 0.05, 8.0, 150, ""),
        _college("Vardhman Mahavir Medical College", 5, "New Delhi", "Delhi", 0.05, 8.0, 150, ""),
    ],
    "Tamil Nadu": [
        _college("CMC Vellore", 1, "Vellore", "Tamil Nadu", 0.5, 12.0, 100, "https://www.cmch-vellore.edu"),
        _college("Madras Medical College", 2, "Chennai", "Tamil Nadu", 0.1, 8.0, 250, ""),
        _college("Stanley Medical College", 3, "Chennai", "Tamil Nadu", 0.1, 7.5, 200, ""),
        _college("Kilpauk Medical College", 4, "Chennai", "Tamil Nadu", 0.1, 7.0, 200, ""),
        _college("Government Medical College Coimbatore", 5, "Coimbatore", "Tamil Nadu", 0.1, 6.0, 150, ""),
    ],
    "Karnataka": [
        _college("Kasturba Medical College", 1, "Manipal", "Karnataka", 3.0, 10.0, 250, "https://manipal.edu"),
        _college("St. John's Medical College", 2, "Bangalore", "Karnataka", 2.5, 9.0, 100, ""),
        _college("Bangalore Medical College", 3, "Bangalore", "Karnataka", 0.2, 7.0, 200, ""),
        _college("JSS Medical College", 4, "Mysore", "Karnataka", 2.0, 6.0, 150, ""),
        _college("KIMS Hubli", 5, "Hubli", "Karnataka", 1.0, 5.0, 150, ""),
    ],
    "Uttar Pradesh": [
        _college("King George's Medical University", 1, "Lucknow", "Uttar Pradesh", 0.2, 8.0, 250, ""),
        _college("BHU IMS Varanasi", 2, "Varanasi", "Uttar Pradesh", 0.1, 7.0, 100, ""),
        _college("GSVM Medical College Kanpur", 3, "Kanpur", "Uttar Pradesh", 0.1, 5.0, 200, ""),
        _college("SN Medical College Agra", 4, "Agra", "Uttar Pradesh", 0.1, 4.5, 200, ""),
        _college("Era's Lucknow Medical College", 5, "Lucknow", "Uttar Pradesh", 3.0, 5.0, 150, ""),
    ],
}

_MEDICAL_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Doctor (MBBS/MD)", description="Diagnose and treat patients in hospitals and clinics", industries=["Healthcare", "Hospitals", "Research", "Pharma"], typical_roles=["General Physician", "Specialist", "Surgeon", "Consultant"], avg_starting_salary_lpa=8.0, growth_india="Very High – Doctor-patient ratio still low in India", growth_abroad="Very High – Universal healthcare demand"),
    CareerOption(name="Dentist (BDS/MDS)", description="Diagnose and treat dental conditions", industries=["Healthcare", "Dental Clinics"], typical_roles=["Dental Surgeon", "Orthodontist", "Periodontist"], avg_starting_salary_lpa=4.0, growth_india="Moderate – Growing dental awareness", growth_abroad="High – Good demand in developed countries"),
    CareerOption(name="Pharmacist", description="Dispense medications and advise on drug interactions", industries=["Pharma", "Healthcare", "Retail"], typical_roles=["Clinical Pharmacist", "Hospital Pharmacist", "R&D Pharmacist"], avg_starting_salary_lpa=3.5, growth_india="Moderate – Pharma industry growing rapidly", growth_abroad="High – Licensed pharmacists in demand"),
    CareerOption(name="Physiotherapist", description="Treat physical disabilities through exercise and manual therapy", industries=["Healthcare", "Sports", "Rehabilitation"], typical_roles=["Physiotherapist", "Sports Rehab Specialist", "Ortho Rehab"], avg_starting_salary_lpa=3.0, growth_india="Growing – Awareness of rehab increasing", growth_abroad="High – Aging populations need physio services"),
    CareerOption(name="Biomedical Engineer", description="Develop medical devices and healthcare technology", industries=["MedTech", "Pharma", "Hospitals", "Research"], typical_roles=["Device Engineer", "Clinical Engineer", "R&D Engineer"], avg_starting_salary_lpa=5.0, growth_india="High – MedTech sector expanding", growth_abroad="Very High – Innovation in healthcare tech"),
]

_MEDICAL_COACHING: list[str] = [
    "Allen Career Institute (Kota)",
    "Aakash Institute",
    "Narayana Group",
    "FIITJEE (Medical Division)",
    "Resonance (Medical Division)",
    "Physics Wallah (Online)",
    "Unacademy (Online)",
]

# ═══════════════════════════════════════════════════════════════════════════
# 3. LAW & LEGAL STUDIES
# ═══════════════════════════════════════════════════════════════════════════

_LAW_COLLEGES_INDIA: list[College] = [
    _college("NLSIU Bangalore", 1, "Bangalore", "Karnataka", 2.5, 15.0, 120, "https://www.nls.ac.in", ["BA LLB", "LLM"]),
    _college("NALSAR Hyderabad", 2, "Hyderabad", "Telangana", 2.5, 14.0, 120, "https://www.nalsar.ac.in", ["BA LLB"]),
    _college("NLU Delhi", 3, "New Delhi", "Delhi", 2.0, 14.0, 120, "https://nludelhi.ac.in", ["BA LLB"]),
    _college("WBNUJS Kolkata", 4, "Kolkata", "West Bengal", 2.0, 12.0, 100, "", ["BA LLB"]),
    _college("NLU Jodhpur", 5, "Jodhpur", "Rajasthan", 2.0, 10.0, 120, "", ["BA LLB"]),
    _college("GNLU Gandhinagar", 6, "Gandhinagar", "Gujarat", 2.0, 10.0, 120, "", ["BA LLB"]),
    _college("RMLNLU Lucknow", 7, "Lucknow", "Uttar Pradesh", 1.5, 8.0, 160, "", ["BA LLB"]),
    _college("HNLU Raipur", 8, "Raipur", "Chhattisgarh", 1.5, 7.0, 120, "", ["BA LLB"]),
    _college("NLU Odisha", 9, "Cuttack", "Odisha", 1.5, 7.0, 100, "", ["BA LLB"]),
    _college("Faculty of Law DU", 10, "New Delhi", "Delhi", 0.2, 8.0, 500, "", ["LLB", "BA LLB"]),
]

_LAW_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Corporate Lawyer", description="Handle corporate legal matters, mergers, acquisitions", industries=["Legal", "Corporate", "Finance", "Consulting"], typical_roles=["Associate", "Partner", "Legal Counsel"], avg_starting_salary_lpa=8.0, growth_india="High – Corporate law growing with economy", growth_abroad="Very High – International firms hiring Indian lawyers"),
    CareerOption(name="Litigation Lawyer", description="Represent clients in court proceedings", industries=["Legal", "Government", "NGO"], typical_roles=["Advocate", "Public Prosecutor", "Legal Aid Lawyer"], avg_starting_salary_lpa=3.0, growth_india="Moderate – Large litigation volume", growth_abroad="Limited – Need local bar qualifications"),
    CareerOption(name="Civil Services (Judiciary)", description="Serve as judges and magistrates in the judicial system", industries=["Government", "Judiciary"], typical_roles=["Civil Judge", "Magistrate", "High Court Judge"], avg_starting_salary_lpa=6.0, growth_india="Stable – Government positions always available", growth_abroad="N/A – Country-specific"),
]

_LAW_COACHING: list[str] = ["CLAT Possible", "Career Launcher (CLAT)", "Legal Edge", "Unacademy (CLAT)", "SuperGrads"]

# ═══════════════════════════════════════════════════════════════════════════
# 4. SCIENCE & RESEARCH
# ═══════════════════════════════════════════════════════════════════════════

_SCIENCE_COLLEGES_INDIA: list[College] = [
    _college("IISc Bangalore", 1, "Bangalore", "Karnataka", 0.5, 22.0, 400, "https://iisc.ac.in", ["BSc Research", "Physics", "Chemistry", "Biology"]),
    _college("IISERs (Pune/Mohali/Kolkata/Bhopal/TVM)", 2, "Multiple", "Multiple", 0.3, 10.0, 1200, "", ["BS-MS Dual Degree"]),
    _college("St. Stephen's College DU", 3, "New Delhi", "Delhi", 0.1, 5.0, 400, "", ["BSc Physics", "Chemistry", "Maths"]),
    _college("Presidency University Kolkata", 4, "Kolkata", "West Bengal", 0.1, 4.0, 500, "", ["BSc"]),
    _college("Loyola College Chennai", 5, "Chennai", "Tamil Nadu", 0.2, 4.5, 600, "", ["BSc"]),
    _college("Christ University", 6, "Bangalore", "Karnataka", 1.5, 5.0, 1000, "", ["BSc"]),
    _college("NISER Bhubaneswar", 7, "Bhubaneswar", "Odisha", 0.2, 8.0, 150, "", ["Integrated MSc"]),
    _college("CMI Chennai", 8, "Chennai", "Tamil Nadu", 0.1, 12.0, 50, "", ["BSc Maths"]),
    _college("ISI Kolkata", 9, "Kolkata", "West Bengal", 0.1, 15.0, 50, "", ["BStat", "BMath"]),
    _college("Fergusson College Pune", 10, "Pune", "Maharashtra", 0.1, 3.0, 1200, "", ["BSc"]),
]

_SCIENCE_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Research Scientist", description="Conduct original research in physics, chemistry, biology, or mathematics", industries=["Research Labs", "Academia", "Government", "Pharma"], typical_roles=["Research Fellow", "Scientist", "Professor"], avg_starting_salary_lpa=6.0, growth_india="Moderate – Govt pushing R&D spending", growth_abroad="High – Strong demand especially in US/EU labs"),
    CareerOption(name="Data Scientist / Statistician", description="Apply statistical methods to solve real-world problems", industries=["IT", "Finance", "Healthcare", "Government"], typical_roles=["Statistician", "Data Analyst", "Quantitative Researcher"], avg_starting_salary_lpa=7.0, growth_india="Very High – Data-driven decision making growing", growth_abroad="Very High"),
    CareerOption(name="Space Scientist", description="Work on space research, satellite technology, and astronomy", industries=["Space", "Defence", "Research"], typical_roles=["ISRO Scientist", "Astronomer", "Astrophysicist"], avg_starting_salary_lpa=8.0, growth_india="Growing – ISRO and private space sector expanding", growth_abroad="High – NASA, ESA, SpaceX opportunities"),
]

_SCIENCE_COACHING: list[str] = ["IMS (for ISI/CMI)", "Cheenta (for Olympiads)", "KVPY coaching centres"]

# ═══════════════════════════════════════════════════════════════════════════
# 5. EDUCATION & TEACHING
# ═══════════════════════════════════════════════════════════════════════════

_EDUCATION_COLLEGES_INDIA: list[College] = [
    _college("NCERT / RIE (Regional Inst of Education)", 1, "Multiple", "Multiple", 0.1, 4.0, 500, "", ["BEd", "MEd"]),
    _college("Lady Shri Ram College (DU)", 2, "New Delhi", "Delhi", 0.1, 4.0, 300, "", ["BA", "BEd"]),
    _college("Jamia Millia Islamia", 3, "New Delhi", "Delhi", 0.2, 3.5, 400, "", ["BEd"]),
    _college("Banaras Hindu University", 4, "Varanasi", "Uttar Pradesh", 0.1, 3.0, 500, "", ["BEd", "BA Education"]),
    _college("Tata Institute of Social Sciences (TISS)", 5, "Mumbai", "Maharashtra", 0.5, 6.0, 200, "https://www.tiss.edu", ["MA Education"]),
    _college("Azim Premji University", 6, "Bangalore", "Karnataka", 1.0, 5.0, 300, "", ["BEd", "MA Education"]),
    _college("MS University Baroda", 7, "Vadodara", "Gujarat", 0.1, 3.0, 400, "", ["BEd"]),
    _college("University of Mysore", 8, "Mysore", "Karnataka", 0.1, 2.5, 300, "", ["BEd"]),
    _college("Osmania University", 9, "Hyderabad", "Telangana", 0.1, 2.5, 500, "", ["BEd"]),
    _college("Patna University", 10, "Patna", "Bihar", 0.1, 2.0, 300, "", ["BEd"]),
]

_EDUCATION_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="School Teacher", description="Teach at primary, secondary, or senior secondary level", industries=["Education", "Government Schools", "Private Schools"], typical_roles=["TGT", "PGT", "Primary Teacher"], avg_starting_salary_lpa=3.5, growth_india="Stable – Always in demand", growth_abroad="Moderate – Need local certification"),
    CareerOption(name="Education Researcher", description="Study education policy, curriculum design, and learning methods", industries=["Academia", "Government", "NGO", "EdTech"], typical_roles=["Research Fellow", "Policy Advisor", "Curriculum Designer"], avg_starting_salary_lpa=5.0, growth_india="Growing – NEP 2020 driving reforms", growth_abroad="Moderate"),
    CareerOption(name="EdTech Professional", description="Develop technology-driven education solutions", industries=["EdTech", "IT", "E-learning"], typical_roles=["Instructional Designer", "Content Developer", "Product Manager"], avg_starting_salary_lpa=5.0, growth_india="Very High – EdTech boom in India", growth_abroad="High – Global e-learning growth"),
]

_EDUCATION_COACHING: list[str] = ["CTET coaching centres", "State TET coaching", "Unacademy (Teaching exams)"]

# ═══════════════════════════════════════════════════════════════════════════
# 6. COMMERCE, FINANCE & BUSINESS
# ═══════════════════════════════════════════════════════════════════════════

_COMMERCE_COLLEGES_INDIA: list[College] = [
    _college("SRCC Delhi", 1, "New Delhi", "Delhi", 0.3, 8.0, 600, "", ["BCom Hons"]),
    _college("Hindu College DU", 2, "New Delhi", "Delhi", 0.1, 6.0, 400, "", ["BCom Hons"]),
    _college("St. Xavier's College Mumbai", 3, "Mumbai", "Maharashtra", 0.5, 6.0, 500, "", ["BCom", "BMS"]),
    _college("Christ University", 4, "Bangalore", "Karnataka", 1.5, 5.0, 1000, "", ["BCom", "BBA"]),
    _college("Loyola College Chennai", 5, "Chennai", "Tamil Nadu", 0.2, 4.5, 600, "", ["BCom"]),
    _college("St. Joseph's College Bangalore", 6, "Bangalore", "Karnataka", 0.5, 4.0, 500, "", ["BCom"]),
    _college("Narsee Monjee College Mumbai", 7, "Mumbai", "Maharashtra", 0.5, 5.0, 400, "", ["BCom"]),
    _college("Hansraj College DU", 8, "New Delhi", "Delhi", 0.1, 5.5, 400, "", ["BCom Hons"]),
    _college("Madras Christian College", 9, "Chennai", "Tamil Nadu", 0.2, 3.5, 500, "", ["BCom"]),
    _college("Symbiosis College of Arts & Commerce Pune", 10, "Pune", "Maharashtra", 0.5, 4.0, 600, "", ["BCom"]),
]

_COMMERCE_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Chartered Accountant (CA)", description="Audit, tax advisory, and financial consulting", industries=["Finance", "Audit", "Consulting", "Corporate"], typical_roles=["CA Intern", "Audit Associate", "Tax Consultant", "CFO"], avg_starting_salary_lpa=7.0, growth_india="Very High – Every business needs CA", growth_abroad="High – ACCA/CPA equivalences"),
    CareerOption(name="Investment Banker", description="Manage corporate fundraising, M&A, and financial advisory", industries=["Banking", "Finance", "Private Equity"], typical_roles=["Analyst", "Associate", "VP", "Managing Director"], avg_starting_salary_lpa=10.0, growth_india="High – Financial markets growing", growth_abroad="Very High – Major global career"),
    CareerOption(name="Company Secretary (CS)", description="Ensure corporate governance and regulatory compliance", industries=["Corporate", "Legal", "Government"], typical_roles=["CS Trainee", "Company Secretary", "Compliance Officer"], avg_starting_salary_lpa=5.0, growth_india="Moderate – Mandatory in listed companies", growth_abroad="Limited – India-specific role"),
    CareerOption(name="Cost & Management Accountant (CMA)", description="Strategic cost management and business advisory", industries=["Manufacturing", "Corporate", "Consulting"], typical_roles=["CMA Trainee", "Cost Accountant", "Management Accountant"], avg_starting_salary_lpa=5.0, growth_india="Moderate – Growing importance", growth_abroad="Moderate"),
]

_COMMERCE_COACHING: list[str] = ["CA coaching (VSI, Aldine)", "CS coaching", "CMA coaching", "ACCA coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 7. ARTS & HUMANITIES
# ═══════════════════════════════════════════════════════════════════════════

_ARTS_COLLEGES_INDIA: list[College] = [
    _college("St. Stephen's College DU", 1, "New Delhi", "Delhi", 0.1, 5.0, 400, "", ["BA History", "English", "Economics"]),
    _college("Lady Shri Ram College DU", 2, "New Delhi", "Delhi", 0.1, 4.5, 300, "", ["BA"]),
    _college("Presidency University Kolkata", 3, "Kolkata", "West Bengal", 0.1, 3.5, 500, "", ["BA"]),
    _college("Fergusson College Pune", 4, "Pune", "Maharashtra", 0.1, 3.0, 1200, "", ["BA"]),
    _college("Loyola College Chennai", 5, "Chennai", "Tamil Nadu", 0.2, 3.5, 600, "", ["BA"]),
    _college("Christ University", 6, "Bangalore", "Karnataka", 1.5, 4.0, 1000, "", ["BA"]),
    _college("Hindu College DU", 7, "New Delhi", "Delhi", 0.1, 4.0, 400, "", ["BA"]),
    _college("Miranda House DU", 8, "New Delhi", "Delhi", 0.1, 4.0, 300, "", ["BA"]),
    _college("JNU (School of Social Sciences)", 9, "New Delhi", "Delhi", 0.1, 5.0, 300, "", ["MA"]),
    _college("Tata Institute of Social Sciences", 10, "Mumbai", "Maharashtra", 0.5, 6.0, 200, "https://www.tiss.edu", ["BA Social Work"]),
]

_ARTS_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Civil Services (IAS/IPS/IFS)", description="Administrative and police services through UPSC", industries=["Government"], typical_roles=["IAS Officer", "IPS Officer", "IFS Officer", "IRS Officer"], avg_starting_salary_lpa=7.0, growth_india="Stable – Prestigious government career", growth_abroad="N/A"),
    CareerOption(name="Journalist / Media Professional", description="Report, analyze, and communicate news and stories", industries=["Media", "Publishing", "Digital", "Broadcasting"], typical_roles=["Reporter", "Editor", "Anchor", "Content Strategist"], avg_starting_salary_lpa=3.5, growth_india="Moderate – Digital media growing", growth_abroad="Moderate"),
    CareerOption(name="Psychologist / Counselor", description="Provide mental health support and counseling services", industries=["Healthcare", "Education", "Corporate", "NGO"], typical_roles=["Clinical Psychologist", "School Counselor", "Corporate Counselor"], avg_starting_salary_lpa=3.0, growth_india="Growing – Mental health awareness increasing", growth_abroad="High – Established field in Western countries"),
]

_ARTS_COACHING: list[str] = ["UPSC coaching (Vajiram, Shankar IAS, Vision IAS)", "Journalism entrance coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 8. DESIGN & CREATIVE ARTS
# ═══════════════════════════════════════════════════════════════════════════

_DESIGN_COLLEGES_INDIA: list[College] = [
    _college("NID Ahmedabad", 1, "Ahmedabad", "Gujarat", 3.0, 10.0, 200, "https://www.nid.edu", ["BDes", "MDes"]),
    _college("NIFT Delhi", 2, "New Delhi", "Delhi", 2.0, 8.0, 300, "https://www.nift.ac.in", ["BDes Fashion", "BFTech"]),
    _college("IIT Bombay (IDC)", 3, "Mumbai", "Maharashtra", 2.5, 15.0, 50, "", ["MDes"]),
    _college("Srishti Manipal Institute", 4, "Bangalore", "Karnataka", 3.0, 5.0, 300, "", ["BDes"]),
    _college("CEPT University", 5, "Ahmedabad", "Gujarat", 2.5, 6.0, 200, "", ["BDes", "BArch"]),
    _college("MIT Institute of Design Pune", 6, "Pune", "Maharashtra", 3.0, 5.0, 200, "", ["BDes"]),
    _college("Pearl Academy", 7, "New Delhi", "Delhi", 4.0, 4.0, 400, "", ["BDes"]),
    _college("Symbiosis Institute of Design", 8, "Pune", "Maharashtra", 3.5, 5.0, 150, "", ["BDes"]),
    _college("DJ Academy of Design", 9, "Coimbatore", "Tamil Nadu", 2.5, 3.5, 200, "", ["BDes"]),
    _college("Lovely Professional University", 10, "Phagwara", "Punjab", 2.0, 3.0, 500, "", ["BDes"]),
]

_DESIGN_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="UX/UI Designer", description="Design user experiences and interfaces for digital products", industries=["IT", "E-commerce", "FinTech", "SaaS"], typical_roles=["UX Designer", "UI Designer", "Product Designer", "UX Researcher"], avg_starting_salary_lpa=6.0, growth_india="Very High – Every tech company needs UX", growth_abroad="Very High – One of most in-demand design roles"),
    CareerOption(name="Fashion Designer", description="Design clothing, accessories, and fashion collections", industries=["Fashion", "Retail", "Luxury", "Textile"], typical_roles=["Fashion Designer", "Textile Designer", "Stylist", "Merchandiser"], avg_starting_salary_lpa=3.5, growth_india="Moderate – Fashion industry growing", growth_abroad="High – Global luxury market"),
    CareerOption(name="Graphic Designer", description="Create visual content for print and digital media", industries=["Advertising", "Media", "IT", "Publishing"], typical_roles=["Graphic Designer", "Art Director", "Brand Designer"], avg_starting_salary_lpa=3.5, growth_india="Moderate-High – Digital content demand", growth_abroad="Moderate"),
]

_DESIGN_COACHING: list[str] = ["NID entrance coaching", "NIFT entrance coaching", "UCEED coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 9. PERFORMING & FINE ARTS
# ═══════════════════════════════════════════════════════════════════════════

_PERFORMING_ARTS_COLLEGES_INDIA: list[College] = [
    _college("FTII Pune", 1, "Pune", "Maharashtra", 0.5, 5.0, 50, "https://www.ftii.ac.in", ["Film Direction", "Acting", "Cinematography"]),
    _college("NSD New Delhi", 2, "New Delhi", "Delhi", 0.3, 3.0, 30, "https://nsd.gov.in", ["Dramatic Arts"]),
    _college("Satyajit Ray Film & TV Institute", 3, "Kolkata", "West Bengal", 0.5, 4.0, 40, "", ["Film"]),
    _college("Faculty of Music & Fine Arts DU", 4, "New Delhi", "Delhi", 0.1, 2.5, 100, "", ["Music", "Fine Arts"]),
    _college("Faculty of Fine Arts, MSU Baroda", 5, "Vadodara", "Gujarat", 0.1, 2.0, 200, "", ["BFA", "MFA"]),
    _college("JJ School of Art Mumbai", 6, "Mumbai", "Maharashtra", 0.1, 2.5, 150, "", ["BFA"]),
    _college("Government College of Fine Arts Chennai", 7, "Chennai", "Tamil Nadu", 0.1, 2.0, 100, "", ["BFA"]),
    _college("Shantiniketan (Visva-Bharati)", 8, "Bolpur", "West Bengal", 0.1, 2.0, 200, "", ["BFA", "Music"]),
    _college("Whistling Woods International", 9, "Mumbai", "Maharashtra", 5.0, 4.0, 200, "", ["Film"]),
    _college("LV Prasad Film & TV Academy", 10, "Chennai", "Tamil Nadu", 2.0, 3.0, 100, "", ["Film"]),
]

_PERFORMING_ARTS_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Actor / Performing Artist", description="Perform in theatre, film, television, or digital media", industries=["Entertainment", "Film", "TV", "Theatre", "OTT"], typical_roles=["Actor", "Theatre Artist", "Voice Artist"], avg_starting_salary_lpa=2.0, growth_india="High – OTT platforms expanding content", growth_abroad="High – Global entertainment industry"),
    CareerOption(name="Film Director / Producer", description="Direct or produce films, short films, and series", industries=["Film", "OTT", "Advertising"], typical_roles=["Director", "Producer", "Screenwriter", "AD"], avg_starting_salary_lpa=3.0, growth_india="High – Bollywood + OTT boom", growth_abroad="High – Global entertainment"),
    CareerOption(name="Musician", description="Compose, perform, or produce music", industries=["Music", "Entertainment", "Advertising", "Film"], typical_roles=["Musician", "Composer", "Music Producer", "Sound Engineer"], avg_starting_salary_lpa=2.0, growth_india="Growing – Indie music scene expanding", growth_abroad="High – Global music market"),
]

_PERFORMING_ARTS_COACHING: list[str] = ["Barry John Acting Studio", "Anupam Kher's Actor Prepares", "FTII entrance coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 10. SPORTS & PHYSICAL EDUCATION
# ═══════════════════════════════════════════════════════════════════════════

_SPORTS_COLLEGES_INDIA: list[College] = [
    _college("LNIPE Gwalior", 1, "Gwalior", "Madhya Pradesh", 0.1, 3.0, 200, "", ["BPEd", "MPEd"]),
    _college("NIS Patiala", 2, "Patiala", "Punjab", 0.1, 3.0, 150, "", ["Sports Coaching"]),
    _college("TAMUniversity (Sports Science)", 3, "Chennai", "Tamil Nadu", 1.5, 4.0, 100, "", ["BSc Sports Science"]),
    _college("Amity University (Physical Ed)", 4, "Noida", "Uttar Pradesh", 2.0, 3.0, 200, "", ["BPEd"]),
    _college("Guru Nanak Dev University", 5, "Amritsar", "Punjab", 0.1, 2.5, 200, "", ["BPEd"]),
    _college("Jain University", 6, "Bangalore", "Karnataka", 1.5, 3.0, 150, "", ["BSc Sports"]),
    _college("SRM University (Sports Science)", 7, "Chennai", "Tamil Nadu", 2.0, 3.0, 100, "", ["BSc Sports"]),
    _college("Symbiosis School of Sports Sciences", 8, "Pune", "Maharashtra", 2.5, 3.5, 60, "", ["BSc Sports"]),
    _college("Indira Gandhi Inst of Physical Ed", 9, "New Delhi", "Delhi", 0.1, 2.5, 100, "", ["BPEd"]),
    _college("University of Lucknow (Physical Ed)", 10, "Lucknow", "Uttar Pradesh", 0.1, 2.0, 100, "", ["BPEd"]),
]

_SPORTS_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Professional Athlete", description="Compete at national/international level in chosen sport", industries=["Sports", "Franchise Leagues"], typical_roles=["Cricketer", "Footballer", "Badminton Player", "Wrestler"], avg_starting_salary_lpa=5.0, growth_india="High – IPL, ISL, PKL growing", growth_abroad="Very High – MLB, NBA, EPL opportunities"),
    CareerOption(name="Sports Coach / Trainer", description="Train athletes and teams for competition", industries=["Sports", "Fitness", "Education"], typical_roles=["Head Coach", "Fitness Trainer", "Physical Ed Teacher"], avg_starting_salary_lpa=3.0, growth_india="Growing – National sports push", growth_abroad="Moderate"),
    CareerOption(name="Sports Physiotherapist", description="Treat sports injuries and aid in athletic rehabilitation", industries=["Sports", "Healthcare", "Fitness"], typical_roles=["Sports Physio", "Team Physio", "Rehab Specialist"], avg_starting_salary_lpa=4.0, growth_india="Growing – Sports science gaining traction", growth_abroad="High"),
]

_SPORTS_COACHING: list[str] = ["SAI (Sports Authority of India) centres", "NIS Patiala", "State sports academies"]

# ═══════════════════════════════════════════════════════════════════════════
# 11. CIVIL SERVICES & GOVERNMENT SERVICES
# ═══════════════════════════════════════════════════════════════════════════

_CIVIL_SERVICES_COLLEGES_INDIA: list[College] = [
    _college("LBSNAA Mussoorie (Training Academy)", 1, "Mussoorie", "Uttarakhand", 0.0, 7.0, 180, "", ["IAS Training"]),
    _college("St. Stephen's College DU", 2, "New Delhi", "Delhi", 0.1, 5.0, 400, "", ["BA", "BSc"]),
    _college("Hindu College DU", 3, "New Delhi", "Delhi", 0.1, 5.0, 400, "", ["BA"]),
    _college("JNU", 4, "New Delhi", "Delhi", 0.1, 5.0, 300, "", ["MA IR", "Social Sciences"]),
    _college("Presidency University Kolkata", 5, "Kolkata", "West Bengal", 0.1, 3.5, 500, "", ["BA"]),
    _college("Loyola College Chennai", 6, "Chennai", "Tamil Nadu", 0.2, 3.5, 600, "", ["BA"]),
    _college("Fergusson College Pune", 7, "Pune", "Maharashtra", 0.1, 3.0, 1200, "", ["BA"]),
    _college("BHU", 8, "Varanasi", "Uttar Pradesh", 0.1, 3.0, 1000, "", ["BA"]),
    _college("Jamia Millia Islamia", 9, "New Delhi", "Delhi", 0.2, 3.5, 400, "", ["BA"]),
    _college("Aligarh Muslim University", 10, "Aligarh", "Uttar Pradesh", 0.1, 3.0, 1000, "", ["BA"]),
]

_CIVIL_SERVICES_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="IAS (Indian Administrative Service)", description="Lead district administration, policy making, and governance", industries=["Government"], typical_roles=["SDM", "DM", "Commissioner", "Secretary"], avg_starting_salary_lpa=7.0, growth_india="Stable – Most prestigious civil service", growth_abroad="N/A"),
    CareerOption(name="IPS (Indian Police Service)", description="Lead police administration and law enforcement", industries=["Government", "Law Enforcement"], typical_roles=["ASP", "SP", "DIG", "IG"], avg_starting_salary_lpa=6.5, growth_india="Stable – Critical government role", growth_abroad="N/A"),
    CareerOption(name="IFS (Indian Foreign Service)", description="Represent India in diplomatic relations abroad", industries=["Government", "Diplomacy"], typical_roles=["Third Secretary", "Counselor", "Ambassador"], avg_starting_salary_lpa=7.0, growth_india="Stable – India's global role expanding", growth_abroad="Stationed abroad"),
    CareerOption(name="SSC / Banking Officer", description="Government jobs through SSC, IBPS, and related exams", industries=["Government", "Banking"], typical_roles=["Bank PO", "SSC CGL Officer", "Income Tax Officer"], avg_starting_salary_lpa=4.5, growth_india="Stable – Continuous recruitment", growth_abroad="N/A"),
]

_CIVIL_SERVICES_COACHING: list[str] = ["Vajiram & Ravi", "Shankar IAS Academy", "Vision IAS", "Drishti IAS", "Unacademy (UPSC)", "InsightsIAS", "ForumIAS"]

# ═══════════════════════════════════════════════════════════════════════════
# 12. HOSPITALITY, TRAVEL & TOURISM
# ═══════════════════════════════════════════════════════════════════════════

_HOSPITALITY_COLLEGES_INDIA: list[College] = [
    _college("IHM Mumbai", 1, "Mumbai", "Maharashtra", 1.0, 5.0, 300, "", ["BSc Hospitality"]),
    _college("IHM Delhi (Pusa)", 2, "New Delhi", "Delhi", 0.5, 4.5, 300, "", ["BSc Hospitality"]),
    _college("IHM Bangalore", 3, "Bangalore", "Karnataka", 0.5, 4.0, 200, "", ["BSc Hospitality"]),
    _college("IHM Chennai", 4, "Chennai", "Tamil Nadu", 0.5, 3.5, 200, "", ["BSc Hospitality"]),
    _college("Welcome Group Graduate School of Hotel Administration (WGSHA)", 5, "Manipal", "Karnataka", 3.0, 5.0, 150, "", ["BHM"]),
    _college("Christ University (Tourism)", 6, "Bangalore", "Karnataka", 1.5, 3.5, 200, "", ["BBA Tourism"]),
    _college("Amity University (Hospitality)", 7, "Noida", "Uttar Pradesh", 3.0, 3.0, 200, "", ["BHM"]),
    _college("IHM Hyderabad", 8, "Hyderabad", "Telangana", 0.5, 3.0, 200, "", ["BSc Hospitality"]),
    _college("IHM Goa", 9, "Goa", "Goa", 0.5, 3.5, 150, "", ["BSc Hospitality"]),
    _college("Oberoi STEP", 10, "New Delhi", "Delhi", 0.0, 4.0, 50, "", ["Hotel Management"]),
]

_HOSPITALITY_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Hotel Manager", description="Manage hotel operations, guest services, and staff", industries=["Hospitality", "Tourism", "Leisure"], typical_roles=["Front Office Manager", "F&B Manager", "GM"], avg_starting_salary_lpa=3.5, growth_india="High – Tourism sector expanding", growth_abroad="Very High – Global hospitality demand"),
    CareerOption(name="Chef", description="Prepare and manage cuisine in hotels, restaurants, and events", industries=["Hospitality", "Food", "Entertainment"], typical_roles=["Commis Chef", "Sous Chef", "Executive Chef"], avg_starting_salary_lpa=3.0, growth_india="High – Food industry growing", growth_abroad="Very High – International demand"),
    CareerOption(name="Travel & Tourism Manager", description="Plan and manage travel packages and tourism operations", industries=["Tourism", "Travel", "Airlines"], typical_roles=["Travel Consultant", "Tour Manager", "Airline Manager"], avg_starting_salary_lpa=3.0, growth_india="High – India's tourism potential", growth_abroad="High – Global tourism recovery"),
]

_HOSPITALITY_COACHING: list[str] = ["NCHMCT JEE coaching", "IHM entrance coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 13. AGRICULTURE & ENVIRONMENTAL STUDIES
# ═══════════════════════════════════════════════════════════════════════════

_AGRICULTURE_COLLEGES_INDIA: list[College] = [
    _college("IARI New Delhi", 1, "New Delhi", "Delhi", 0.1, 6.0, 200, "https://www.iari.res.in", ["BSc Agriculture"]),
    _college("TNAU Coimbatore", 2, "Coimbatore", "Tamil Nadu", 0.2, 4.0, 800, "", ["BSc Agriculture"]),
    _college("PAU Ludhiana", 3, "Ludhiana", "Punjab", 0.2, 3.5, 600, "", ["BSc Agriculture"]),
    _college("UAS Bangalore", 4, "Bangalore", "Karnataka", 0.2, 3.5, 500, "", ["BSc Agriculture"]),
    _college("GB Pant University", 5, "Pantnagar", "Uttarakhand", 0.2, 3.0, 500, "", ["BSc Agriculture"]),
    _college("NDRI Karnal", 6, "Karnal", "Haryana", 0.1, 4.0, 100, "", ["BTech Dairy"]),
    _college("AAU Jorhat", 7, "Jorhat", "Assam", 0.1, 2.5, 300, "", ["BSc Agriculture"]),
    _college("JNKVV Jabalpur", 8, "Jabalpur", "Madhya Pradesh", 0.1, 2.5, 400, "", ["BSc Agriculture"]),
    _college("OUAT Bhubaneswar", 9, "Bhubaneswar", "Odisha", 0.1, 2.5, 400, "", ["BSc Agriculture"]),
    _college("CSK HPKV Palampur", 10, "Palampur", "Himachal Pradesh", 0.1, 2.0, 200, "", ["BSc Agriculture"]),
]

_AGRICULTURE_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Agricultural Scientist", description="Conduct research on crop improvement, soil science, and sustainable farming", industries=["Agriculture", "Government", "Research"], typical_roles=["ICAR Scientist", "Research Associate", "Agri Extension Officer"], avg_starting_salary_lpa=5.0, growth_india="High – Agriculture is backbone of India", growth_abroad="Moderate"),
    CareerOption(name="Environmental Scientist", description="Study environmental issues and develop solutions for sustainability", industries=["Environment", "Government", "NGO", "Corporate"], typical_roles=["Environmental Consultant", "EIA Officer", "Sustainability Manager"], avg_starting_salary_lpa=4.0, growth_india="Growing – Climate change awareness", growth_abroad="Very High – Green economy transition"),
    CareerOption(name="Food Technologist", description="Develop and improve food processing and preservation methods", industries=["FMCG", "Food Processing", "Quality Control"], typical_roles=["Food Technologist", "QC Manager", "R&D Scientist"], avg_starting_salary_lpa=3.5, growth_india="High – Food processing industry expanding", growth_abroad="Moderate"),
]

_AGRICULTURE_COACHING: list[str] = ["ICAR AIEEA coaching", "JRF / SRF coaching"]

# ═══════════════════════════════════════════════════════════════════════════
# 14. DEFENCE RESEARCH
# ═══════════════════════════════════════════════════════════════════════════

_DEFENCE_COLLEGES_INDIA: list[College] = [
    _college("NDA Khadakwasla", 1, "Pune", "Maharashtra", 0.0, 6.0, 320, "https://www.nda.nic.in", ["Army", "Navy", "Air Force"]),
    _college("IMA Dehradun", 2, "Dehradun", "Uttarakhand", 0.0, 6.0, 250, "", ["Army"]),
    _college("AFA Dundigal", 3, "Hyderabad", "Telangana", 0.0, 6.0, 150, "", ["Air Force"]),
    _college("INA Ezhimala", 4, "Ezhimala", "Kerala", 0.0, 6.0, 100, "", ["Navy"]),
    _college("OTA Chennai", 5, "Chennai", "Tamil Nadu", 0.0, 5.5, 200, "", ["Army Short Service"]),
    _college("DRDO Labs (Various)", 6, "Multiple", "Multiple", 0.0, 8.0, 500, "https://www.drdo.gov.in", ["Defence R&D"]),
    _college("Rashtriya Indian Military College (RIMC)", 7, "Dehradun", "Uttarakhand", 0.0, 5.0, 25, "", ["Pre-NDA Training"]),
    _college("Sainik Schools (Various)", 8, "Multiple", "Multiple", 0.1, 4.0, 1500, "", ["Pre-NDA Training"]),
    _college("Military College of Electronics & Mechanical Eng", 9, "Secunderabad", "Telangana", 0.0, 7.0, 200, "", ["BTech"]),
    _college("College of Defence Management", 10, "Secunderabad", "Telangana", 0.0, 8.0, 100, "", ["Defence Management"]),
]

_DEFENCE_CAREER_OPTIONS: list[CareerOption] = [
    CareerOption(name="Armed Forces Officer", description="Lead military operations in Army, Navy, or Air Force", industries=["Defence", "Government"], typical_roles=["Lieutenant", "Captain", "Major", "Colonel"], avg_starting_salary_lpa=6.0, growth_india="Stable – India's defence modernization", growth_abroad="N/A – Indian armed forces"),
    CareerOption(name="DRDO Scientist", description="Conduct defence research and develop military technology", industries=["Defence", "Research", "Technology"], typical_roles=["Scientist B", "Scientist C", "Project Director"], avg_starting_salary_lpa=7.0, growth_india="High – Defence R&D budget increasing", growth_abroad="Limited – Security-classified"),
    CareerOption(name="Defence Analyst", description="Analyze security threats and advise on defence strategy", industries=["Government", "Think Tanks", "Media"], typical_roles=["Strategic Analyst", "Security Consultant", "Policy Advisor"], avg_starting_salary_lpa=5.0, growth_india="Growing – Geo-political awareness increasing", growth_abroad="Moderate"),
]

_DEFENCE_COACHING: list[str] = ["NDA coaching (Centurion Defence Academy)", "CDS coaching", "AFCAT coaching", "SSB interview coaching"]


# ═══════════════════════════════════════════════════════════════════════════
# ROADMAP DATA — Step-by-step path for each stream
# ═══════════════════════════════════════════════════════════════════════════

_ROADMAP: dict[str, list[dict[str, str]]] = {
    "Engineering & Technology": [
        {"step": "1", "title": "Class 10th — Build Foundation", "detail": "Score well in Maths, Science & English. Aim for 80%+ to keep all options open."},
        {"step": "2", "title": "Class 11-12th — Science (PCM)", "detail": "Take Physics, Chemistry, Mathematics. Start JEE preparation early."},
        {"step": "3", "title": "Entrance Exams", "detail": "Appear for JEE Main (Jan & Apr), JEE Advanced, BITSAT, VITEEE, and State CETs."},
        {"step": "4", "title": "B.Tech / BE (4 years)", "detail": "Join IIT/NIT/BITS or top private college. Choose branch based on interest & placement data."},
        {"step": "5", "title": "Internships & Projects", "detail": "Do at least 2 internships. Build portfolio with real-world projects."},
        {"step": "6", "title": "Campus Placement / GATE / GRE", "detail": "Either go for campus placement or prepare for GATE (M.Tech) / GRE (MS abroad)."},
        {"step": "7", "title": "Career Launch", "detail": "Join as SDE/Design Engineer/Data Scientist. Average starting: ₹8-21 LPA at top colleges."},
    ],
    "Medical & Healthcare": [
        {"step": "1", "title": "Class 10th — Science Focus", "detail": "Score well in Science, Maths & English. Biology is critical from here on."},
        {"step": "2", "title": "Class 11-12th — Science (PCB)", "detail": "Take Physics, Chemistry, Biology. Start NEET preparation alongside school."},
        {"step": "3", "title": "NEET UG Exam", "detail": "Appear for NEET UG (May). Score 600+ for government MBBS seats."},
        {"step": "4", "title": "MBBS / BDS / BAMS (5.5 years)", "detail": "Complete MBBS including 1 year internship. Choose specialization interest early."},
        {"step": "5", "title": "NEET PG / NEXT Exam", "detail": "Prepare for NEET PG to specialize (MD/MS). Highly competitive."},
        {"step": "6", "title": "Specialization (3 years)", "detail": "Complete MD/MS in chosen specialty. Super-specialization (DM/MCh) optional."},
        {"step": "7", "title": "Practice / Hospital", "detail": "Join hospital, start private practice, or pursue medical research."},
    ],
    "Law & Legal Studies": [
        {"step": "1", "title": "Class 10th — Strong Academics", "detail": "Good marks in all subjects. English & Social Studies are especially important."},
        {"step": "2", "title": "Class 12th — Any Stream", "detail": "Can come from Science, Commerce, or Arts. Focus on English comprehension & analytical reasoning."},
        {"step": "3", "title": "CLAT / AILET Exam", "detail": "Appear for CLAT (Dec), AILET, LSAT India for 5-year integrated law programs."},
        {"step": "4", "title": "BA LLB / BBA LLB (5 years)", "detail": "Join NLU or top law college. Participate in moot courts and internships."},
        {"step": "5", "title": "Internships & Clerkships", "detail": "Intern with law firms, courts, and corporate legal departments."},
        {"step": "6", "title": "Bar Council Registration", "detail": "Register with Bar Council of India. Can practice after enrollment."},
        {"step": "7", "title": "Career Launch", "detail": "Join law firm, corporate legal team, or start litigation practice."},
    ],
    "Science & Research": [
        {"step": "1", "title": "Class 10th — Excel in Science & Maths", "detail": "Build strong conceptual understanding. Participate in science olympiads."},
        {"step": "2", "title": "Class 11-12th — PCM or PCB", "detail": "Choose based on interest (Physics/Maths or Biology). Prepare for KVPY/NEST."},
        {"step": "3", "title": "Entrance Exams", "detail": "Appear for KVPY, NEST, IISER Aptitude Test, ISI Entrance, or JEE for IISc."},
        {"step": "4", "title": "BSc / BS / Integrated MS (3-5 years)", "detail": "Join IISc, IISER, IISERs, NISER, or top university for research-oriented degree."},
        {"step": "5", "title": "Research Internships", "detail": "Summer research programs at national labs (TIFR, IISC, NCBS). Build publications."},
        {"step": "6", "title": "MSc / PhD / IIT JAM", "detail": "Pursue MSc via IIT JAM or directly enter PhD programs. Apply for fellowships."},
        {"step": "7", "title": "Research Career", "detail": "Join academia, national labs (ISRO, DRDO, BARC), or R&D divisions of companies."},
    ],
    "Education & Teaching": [
        {"step": "1", "title": "Class 10th — All-round Performance", "detail": "Good marks across subjects. Develop communication skills."},
        {"step": "2", "title": "Class 12th — Any Stream", "detail": "Choose the subject you want to teach (Science, Commerce, Arts, Languages)."},
        {"step": "3", "title": "BA / BSc + B.Ed Entrance", "detail": "Apply for integrated B.Ed programs or standalone BA/BSc followed by B.Ed."},
        {"step": "4", "title": "Graduation + B.Ed (4-6 years)", "detail": "Complete bachelor's degree and B.Ed. Some colleges offer 4-year integrated BA B.Ed."},
        {"step": "5", "title": "CTET / State TET", "detail": "Clear Central/State Teacher Eligibility Test (mandatory for government school jobs)."},
        {"step": "6", "title": "Teaching Experience", "detail": "Start teaching in private or government schools. Gain 2-3 years experience."},
        {"step": "7", "title": "Career Growth", "detail": "Become PGT/Vice Principal/Principal, or join EdTech platforms. M.Ed for higher positions."},
    ],
    "Commerce, Finance & Business": [
        {"step": "1", "title": "Class 10th — Maths & English", "detail": "Score well in Mathematics and English. Basic accounting awareness helps."},
        {"step": "2", "title": "Class 11-12th — Commerce", "detail": "Take Accountancy, Business Studies, Economics, and Mathematics."},
        {"step": "3", "title": "CA/CS Foundation or CUET", "detail": "Register for CA Foundation (after 10th), CS Foundation, or prepare for CUET."},
        {"step": "4", "title": "B.Com / BBA / CA-Inter (3 years)", "detail": "Pursue B.Com alongside CA/CS. Or BBA from top college."},
        {"step": "5", "title": "CA Final / MBA Prep", "detail": "Complete CA Final (avg 4-5 yrs total) or prepare for CAT/GMAT for MBA."},
        {"step": "6", "title": "Articleship / Internships", "detail": "Complete 3-year articleship for CA. MBA students do summer internships."},
        {"step": "7", "title": "Career Launch", "detail": "Join Big 4, investment banks, corporate finance, or start practice."},
    ],
    "Arts & Humanities": [
        {"step": "1", "title": "Class 10th — Language & Social Studies", "detail": "Develop strong reading, writing, and analytical skills."},
        {"step": "2", "title": "Class 11-12th — Arts Stream", "detail": "Choose History, Political Science, Geography, Sociology, Psychology, or English."},
        {"step": "3", "title": "CUET / University Entrance", "detail": "Prepare for CUET for DU/JNU/BHU. Apply to St. Stephen's, LSR, Presidency."},
        {"step": "4", "title": "BA (3 years)", "detail": "Major in your subject of interest. Participate in debates, writing, and research."},
        {"step": "5", "title": "MA / UPSC Preparation", "detail": "Pursue MA or start UPSC CSE preparation. Both paths are common."},
        {"step": "6", "title": "Specialization / Exam", "detail": "Clear UPSC / UGC NET / State PCS or pursue MPhil/PhD."},
        {"step": "7", "title": "Career Launch", "detail": "Join civil services, academia, media, publishing, or NGO sector."},
    ],
    "Design & Creative Arts": [
        {"step": "1", "title": "Class 10th — Develop Creative Skills", "detail": "Practice sketching, digital design. Build a creative portfolio."},
        {"step": "2", "title": "Class 12th — Any Stream", "detail": "Any stream accepted. Focus on developing portfolio alongside studies."},
        {"step": "3", "title": "UCEED / NID DAT / NIFT Exam", "detail": "Appear for design entrance exams. Portfolio reviews are part of selection."},
        {"step": "4", "title": "B.Des / B.Arch (4-5 years)", "detail": "Join NID, NIFT, IIT IDC, or top design college. Specialize early."},
        {"step": "5", "title": "Internships & Portfolio", "detail": "Intern at design studios, tech companies. Build strong professional portfolio."},
        {"step": "6", "title": "M.Des / Industry Entry", "detail": "Optional M.Des (CEED exam for IITs). Direct entry into industry also viable."},
        {"step": "7", "title": "Career Launch", "detail": "Join as UX/UI Designer, Product Designer, Fashion Designer, or start own studio."},
    ],
    "Performing & Fine Arts": [
        {"step": "1", "title": "Class 10th — Pursue Artistic Interests", "detail": "Join theatre groups, music classes, art workshops. Build early experience."},
        {"step": "2", "title": "Class 12th — Any Stream", "detail": "Any stream works. Continue honing performance / art skills alongside."},
        {"step": "3", "title": "Entrance Exams / Auditions", "detail": "Apply to FTII, NSD, JJ School. Auditions and portfolio reviews."},
        {"step": "4", "title": "BFA / Diploma (3-4 years)", "detail": "Study at film institute, drama school, or fine arts college."},
        {"step": "5", "title": "Practice & Networking", "detail": "Perform in productions, exhibit art, build industry connections."},
        {"step": "6", "title": "Assistantships / Residencies", "detail": "Work as assistant director/artist. Apply for art residencies and grants."},
        {"step": "7", "title": "Career Launch", "detail": "Establish career in film, theatre, OTT, galleries, or freelance art."},
    ],
    "Sports & Physical Education": [
        {"step": "1", "title": "Class 10th — Sport Selection", "detail": "Choose your sport early. Join coaching academy. Compete at school/district level."},
        {"step": "2", "title": "Class 12th — Physical Education", "detail": "Take Physical Education as subject. Continue competitive sports alongside."},
        {"step": "3", "title": "Sports Quota / BPEd Entrance", "detail": "Apply through sports quota to universities. Or BPEd entrance exam."},
        {"step": "4", "title": "BPEd / BSc Sports Science (3-4 years)", "detail": "Study sports science, coaching methodology, nutrition, biomechanics."},
        {"step": "5", "title": "Competitive Sports / Certification", "detail": "Compete at state/national level. Get coaching certifications (NIS Patiala)."},
        {"step": "6", "title": "MPEd / Advanced Coaching", "detail": "Pursue MPEd or specialized coaching diplomas. SAI/NIS programs."},
        {"step": "7", "title": "Career Launch", "detail": "Become professional athlete, coach, sports manager, or PE teacher."},
    ],
    "Civil Services & Government Services": [
        {"step": "1", "title": "Class 10th — Strong Academics", "detail": "Score well across all subjects. Develop reading habit for current affairs."},
        {"step": "2", "title": "Class 12th — Any Stream (Arts Preferred)", "detail": "Arts gives advantage for UPSC optionals but any stream is fine."},
        {"step": "3", "title": "Graduate in Any Discipline", "detail": "Complete graduation (BA/BSc/B.Com/BTech) from any recognized university."},
        {"step": "4", "title": "UPSC CSE Preparation (1-2 years)", "detail": "Join coaching or self-study. Cover NCERT books, current affairs, optionals."},
        {"step": "5", "title": "UPSC Prelims (June)", "detail": "Clear Preliminary exam (GS Paper I & CSAT). Cutoff typically 95-100/200."},
        {"step": "6", "title": "UPSC Mains + Interview", "detail": "Write 9 papers in Mains. Clear personality test (interview) at UPSC."},
        {"step": "7", "title": "Service Allocation", "detail": "Get allocated IAS/IPS/IFS/IRS based on rank. Training at LBSNAA/SVPNPA."},
    ],
    "Hospitality, Travel & Tourism": [
        {"step": "1", "title": "Class 10th — Communication Skills", "detail": "Focus on English and communication. Develop people skills."},
        {"step": "2", "title": "Class 12th — Any Stream", "detail": "Any stream accepted. Science/Commerce students also welcome."},
        {"step": "3", "title": "NCHMCT JEE / IHM Entrance", "detail": "Appear for NCHMCT JEE (April) for IHM admission. Also direct admissions available."},
        {"step": "4", "title": "B.Sc Hospitality / BHM (3-4 years)", "detail": "Study at IHM or top hotel management college. Industrial training included."},
        {"step": "5", "title": "Industrial Training", "detail": "6-month placement in 5-star hotel. Critical for industry exposure."},
        {"step": "6", "title": "Specialization", "detail": "Choose front office, F&B, housekeeping, or culinary arts specialization."},
        {"step": "7", "title": "Career Launch", "detail": "Join hotel chains, airlines, cruise lines, or start own hospitality business."},
    ],
    "Agriculture & Environmental Studies": [
        {"step": "1", "title": "Class 10th — Science & Biology", "detail": "Strong in Science, especially Biology. Interest in environment and nature."},
        {"step": "2", "title": "Class 11-12th — PCB / PCM", "detail": "Take Biology or Mathematics with Physics & Chemistry."},
        {"step": "3", "title": "ICAR AIEEA / State Entrance", "detail": "Appear for ICAR AIEEA (June) or state agricultural university entrance exams."},
        {"step": "4", "title": "BSc Agriculture / B.Tech Agri (4 years)", "detail": "Study at top agricultural university. Includes farm practicals."},
        {"step": "5", "title": "Internship / Field Work", "detail": "Intern at agricultural research stations, ICAR labs, or agri-companies."},
        {"step": "6", "title": "MSc / ICAR NET / ARS", "detail": "Pursue MSc or clear ICAR NET for lecturership / ARS for scientist posts."},
        {"step": "7", "title": "Career Launch", "detail": "Join as agricultural officer, FMCG sector, agri-startup, or research."},
    ],
    "Defence Research": [
        {"step": "1", "title": "Class 10th — Physical Fitness + Academics", "detail": "Maintain physical fitness. Score well in Maths and Science."},
        {"step": "2", "title": "Class 11-12th — PCM", "detail": "Take Physics, Chemistry, Mathematics. Physical fitness training continues."},
        {"step": "3", "title": "NDA / CDS / AFCAT Entrance", "detail": "Apply for NDA after 12th or CDS/AFCAT after graduation."},
        {"step": "4", "title": "Training Academy (1-3 years)", "detail": "Join NDA Khadakwasla, IMA Dehradun, AFA Hyderabad, or INA Ezhimala."},
        {"step": "5", "title": "Service Commission", "detail": "Get commissioned as Lieutenant/Sub-Lieutenant/Flying Officer."},
        {"step": "6", "title": "Specialization & Promotions", "detail": "Specialize in technical/combat roles. Progress through ranks."},
        {"step": "7", "title": "Career in Defence", "detail": "Serve in armed forces or transition to DRDO/defence PSUs/defence consulting."},
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# SELECTION PROCESS DATA — Entrance exams with details
# ═══════════════════════════════════════════════════════════════════════════

_SELECTION_PROCESS: dict[str, list[dict[str, str]]] = {
    "Engineering & Technology": [
        {"exam": "JEE Main", "conducted_by": "NTA", "eligibility": "Class 12th with PCM (75% aggregate or top 20 percentile)", "pattern": "CBT — 90 questions, 300 marks, 3 hours", "dates": "January & April (two attempts)", "website": "https://jeemain.nta.nic.in"},
        {"exam": "JEE Advanced", "conducted_by": "IITs (Rotating)", "eligibility": "Top 2,50,000 in JEE Main", "pattern": "CBT — 2 papers, 3 hours each", "dates": "June", "website": "https://jeeadv.ac.in"},
        {"exam": "BITSAT", "conducted_by": "BITS Pilani", "eligibility": "Class 12th with PCM (75% aggregate)", "pattern": "CBT — 130 questions, 3 hours", "dates": "May-June", "website": "https://www.bitsadmission.com"},
        {"exam": "VITEEE", "conducted_by": "VIT University", "eligibility": "Class 12th with PCM (60% aggregate)", "pattern": "CBT — 125 questions, 2.5 hours", "dates": "April", "website": "https://viteee.vit.ac.in"},
        {"exam": "State CETs", "conducted_by": "Respective State Govts", "eligibility": "Varies by state — PCM in 12th", "pattern": "Varies — typically MCQ-based, 2-3 hours", "dates": "April-June", "website": "Check respective state CET portal"},
    ],
    "Medical & Healthcare": [
        {"exam": "NEET UG", "conducted_by": "NTA", "eligibility": "Class 12th with PCB (50% aggregate, 17-25 yrs)", "pattern": "Pen & Paper — 200 MCQs, 720 marks, 3.5 hours", "dates": "May (once a year)", "website": "https://neet.nta.nic.in"},
        {"exam": "NEET PG", "conducted_by": "NBEMS", "eligibility": "MBBS degree + internship completion", "pattern": "CBT — 200 MCQs, 3.5 hours", "dates": "March", "website": "https://natboard.edu.in"},
        {"exam": "AIIMS PG", "conducted_by": "AIIMS (merged with NEET PG)", "eligibility": "MBBS degree", "pattern": "Now part of NEET PG", "dates": "March (with NEET PG)", "website": "https://www.aiimsexams.ac.in"},
    ],
    "Law & Legal Studies": [
        {"exam": "CLAT", "conducted_by": "Consortium of NLUs", "eligibility": "Class 12th (45% for General, 40% for SC/ST)", "pattern": "CBT — 150 MCQs, 150 marks, 2 hours", "dates": "December", "website": "https://consortiumofnlus.ac.in"},
        {"exam": "AILET", "conducted_by": "NLU Delhi", "eligibility": "Class 12th (50% aggregate)", "pattern": "CBT — 150 questions, 150 marks, 1.5 hours", "dates": "December", "website": "https://nludelhi.ac.in"},
        {"exam": "LSAT India", "conducted_by": "Pearson VUE", "eligibility": "Class 12th pass", "pattern": "CBT — 92-100 questions, 2 hours 20 min", "dates": "January & June", "website": "https://www.lsatindia.in"},
        {"exam": "MH CET Law", "conducted_by": "Maharashtra CET Cell", "eligibility": "Class 12th (45% aggregate)", "pattern": "CBT — 150 MCQs, 2 hours", "dates": "May-June", "website": "https://cetcell.mahacet.org"},
    ],
    "Science & Research": [
        {"exam": "KVPY (now INSPIRE)", "conducted_by": "DST / IISc Bangalore", "eligibility": "Class 11/12 or 1st year BSc", "pattern": "Aptitude test + interview", "dates": "November (aptitude), Jan-Feb (interview)", "website": "https://www.online-inspire.gov.in"},
        {"exam": "NEST", "conducted_by": "NISER / UM-DAE CBS", "eligibility": "Class 12th with Science", "pattern": "CBT — Biology, Chemistry, Maths, Physics sections", "dates": "June", "website": "https://www.nestexam.in"},
        {"exam": "IISER Aptitude Test", "conducted_by": "IISERs", "eligibility": "Class 12th with 60%+ in Science", "pattern": "CBT — MCQ-based, 3 hours", "dates": "June", "website": "https://www.iiseradmission.in"},
        {"exam": "IIT JAM", "conducted_by": "IITs", "eligibility": "BSc / equivalent degree", "pattern": "CBT — 60 questions, 3 hours", "dates": "February", "website": "https://jam.iitb.ac.in"},
    ],
    "Education & Teaching": [
        {"exam": "CTET", "conducted_by": "CBSE", "eligibility": "Graduation + B.Ed (or D.El.Ed for Primary)", "pattern": "CBT — 150 MCQs, 2.5 hours (Paper I or II)", "dates": "January & July", "website": "https://ctet.nic.in"},
        {"exam": "State TET", "conducted_by": "Respective State Govts", "eligibility": "B.Ed + state domicile (varies)", "pattern": "Paper-based — 150 MCQs, 2.5 hours", "dates": "Varies by state", "website": "Check respective state education dept"},
        {"exam": "CUET (for B.Ed / BA Ed)", "conducted_by": "NTA", "eligibility": "Class 12th pass", "pattern": "CBT — Domain subjects + General Test", "dates": "May", "website": "https://cuet.nta.nic.in"},
    ],
    "Commerce, Finance & Business": [
        {"exam": "CA Foundation", "conducted_by": "ICAI", "eligibility": "Class 12th pass (register after 10th)", "pattern": "Pen & Paper — 4 papers, 100 marks each", "dates": "May & November", "website": "https://www.icai.org"},
        {"exam": "CS Foundation", "conducted_by": "ICSI", "eligibility": "Class 12th pass", "pattern": "CBT — 4 papers", "dates": "June & December", "website": "https://www.icsi.edu"},
        {"exam": "CMA Foundation", "conducted_by": "ICMAI", "eligibility": "Class 12th pass", "pattern": "Pen & Paper — 4 papers", "dates": "June & December", "website": "https://icmai.in"},
        {"exam": "CAT (for MBA)", "conducted_by": "IIMs", "eligibility": "Graduation (50% aggregate)", "pattern": "CBT — VARC, DILR, QA — 2 hours", "dates": "November", "website": "https://iimcat.ac.in"},
    ],
    "Arts & Humanities": [
        {"exam": "CUET", "conducted_by": "NTA", "eligibility": "Class 12th pass", "pattern": "CBT — Domain subjects + General Test + Language", "dates": "May", "website": "https://cuet.nta.nic.in"},
        {"exam": "UPSC CSE (for IAS/IPS)", "conducted_by": "UPSC", "eligibility": "Graduation in any discipline (21-32 yrs)", "pattern": "Prelims (MCQ) + Mains (Descriptive) + Interview", "dates": "June (Prelims), Sep (Mains), Mar-Apr (Interview)", "website": "https://www.upsc.gov.in"},
        {"exam": "TISS BAT", "conducted_by": "TISS Mumbai", "eligibility": "Class 12th (50% aggregate)", "pattern": "CBT + GD + Interview", "dates": "January", "website": "https://www.tiss.edu"},
        {"exam": "JNU Entrance (JNUEE)", "conducted_by": "NTA (via CUET)", "eligibility": "Varies by program", "pattern": "Through CUET scores", "dates": "May", "website": "https://www.jnu.ac.in"},
    ],
    "Design & Creative Arts": [
        {"exam": "UCEED", "conducted_by": "IIT Bombay", "eligibility": "Class 12th pass", "pattern": "CBT — NAT, MSQ, Sketching — 3 hours", "dates": "January", "website": "https://www.uceed.iitb.ac.in"},
        {"exam": "NID DAT", "conducted_by": "NID Ahmedabad", "eligibility": "Class 12th pass", "pattern": "Prelims (CBT) + Mains (Studio test + Interview)", "dates": "January (Prelims), April (Mains)", "website": "https://admissions.nid.edu"},
        {"exam": "NIFT Entrance", "conducted_by": "NIFT", "eligibility": "Class 12th pass", "pattern": "GAT + CAT (Creative Ability Test) + Situation Test", "dates": "February", "website": "https://nift.ac.in"},
        {"exam": "CEED (for M.Des)", "conducted_by": "IIT Bombay", "eligibility": "Graduation / final year", "pattern": "CBT + Sketching — 3 hours", "dates": "January", "website": "https://www.ceed.iitb.ac.in"},
    ],
    "Performing & Fine Arts": [
        {"exam": "FTII Entrance", "conducted_by": "FTII Pune", "eligibility": "Graduation (for most courses)", "pattern": "Written test + Screen test + Interview", "dates": "March-April", "website": "https://www.ftii.ac.in"},
        {"exam": "NSD Entrance", "conducted_by": "NSD Delhi", "eligibility": "Graduation + theatre experience", "pattern": "Written + Workshop + Interview", "dates": "April-May", "website": "https://nsd.gov.in"},
        {"exam": "BHU UET (Fine Arts)", "conducted_by": "BHU via CUET", "eligibility": "Class 12th (BFA program)", "pattern": "Through CUET + practical/portfolio", "dates": "May", "website": "https://www.bhu.ac.in"},
    ],
    "Sports & Physical Education": [
        {"exam": "BPEd Entrance", "conducted_by": "Various Universities", "eligibility": "Class 12th with Physical Education + sports certificates", "pattern": "Written test + Physical fitness test", "dates": "June-July", "website": "Check respective university"},
        {"exam": "SAI Trials", "conducted_by": "Sports Authority of India", "eligibility": "Age 8-25 (varies by sport)", "pattern": "Sport-specific trials and fitness tests", "dates": "Throughout the year", "website": "https://sfrportal.sai.gov.in"},
        {"exam": "Sports Quota Admissions", "conducted_by": "DU / JNU / State Universities", "eligibility": "Class 12th + state/national level certificates", "pattern": "Trials + certificate verification", "dates": "June-July", "website": "Check respective university admissions"},
    ],
    "Civil Services & Government Services": [
        {"exam": "UPSC CSE", "conducted_by": "UPSC", "eligibility": "Graduation in any discipline (21-32 yrs, 6 attempts for General)", "pattern": "Prelims (2 papers MCQ) + Mains (9 papers descriptive) + Interview", "dates": "June (Prelims), Sep (Mains), Mar-Apr (Interview)", "website": "https://www.upsc.gov.in"},
        {"exam": "SSC CGL", "conducted_by": "SSC", "eligibility": "Graduation in any discipline", "pattern": "Tier I (CBT) + Tier II (CBT) + Tier III (Descriptive)", "dates": "April (Tier I), June-July (Tier II)", "website": "https://ssc.nic.in"},
        {"exam": "IBPS PO", "conducted_by": "IBPS", "eligibility": "Graduation (20-30 yrs)", "pattern": "Prelims + Mains + Interview", "dates": "October (Prelims), November (Mains)", "website": "https://www.ibps.in"},
        {"exam": "State PCS", "conducted_by": "State PSCs", "eligibility": "Graduation + state domicile (varies)", "pattern": "Prelims + Mains + Interview (similar to UPSC)", "dates": "Varies by state", "website": "Check respective state PSC portal"},
    ],
    "Hospitality, Travel & Tourism": [
        {"exam": "NCHMCT JEE", "conducted_by": "NTA", "eligibility": "Class 12th pass (any stream)", "pattern": "CBT — English, Aptitude, Reasoning, GK, Science — 3 hours", "dates": "April", "website": "https://nchmjee.nta.nic.in"},
        {"exam": "IHM Entrance", "conducted_by": "Various IHMs", "eligibility": "Class 12th pass", "pattern": "Written test + GD + Interview", "dates": "May-June", "website": "Check respective IHM website"},
    ],
    "Agriculture & Environmental Studies": [
        {"exam": "ICAR AIEEA", "conducted_by": "NTA (for ICAR)", "eligibility": "Class 12th with PCB/PCM (50% aggregate)", "pattern": "CBT — Physics, Chemistry, Biology/Maths, Agriculture — 2.5 hours", "dates": "June", "website": "https://icar.nta.nic.in"},
        {"exam": "State Agriculture Entrance", "conducted_by": "State Agricultural Universities", "eligibility": "Class 12th with PCB/PCM", "pattern": "State-specific written exam", "dates": "May-July", "website": "Check respective state agriculture university"},
    ],
    "Defence Research": [
        {"exam": "NDA (UPSC)", "conducted_by": "UPSC", "eligibility": "Class 12th pass (16.5-19.5 yrs, unmarried males)", "pattern": "Written (Maths + GAT) + SSB Interview (5 days)", "dates": "April & September (twice a year)", "website": "https://www.upsc.gov.in"},
        {"exam": "CDS (UPSC)", "conducted_by": "UPSC", "eligibility": "Graduation (for IMA/AFA/INA/OTA)", "pattern": "Written (English + GK + Maths) + SSB Interview", "dates": "April & September", "website": "https://www.upsc.gov.in"},
        {"exam": "AFCAT", "conducted_by": "IAF", "eligibility": "Graduation (60% in relevant stream)", "pattern": "CBT — GK, English, Maths, Reasoning + AFSB Interview", "dates": "February & August", "website": "https://afcat.cdac.in"},
        {"exam": "DRDO SET", "conducted_by": "DRDO / RAC", "eligibility": "B.Tech / MSc (First Class)", "pattern": "CBT — Subject-specific + General Ability", "dates": "Notified periodically", "website": "https://rac.gov.in"},
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# ABROAD OPPORTUNITIES DATA — International options for each stream
# ═══════════════════════════════════════════════════════════════════════════

_ABROAD_DATA: dict[str, dict] = {
    "Engineering & Technology": {
        "overview": "Indian engineers are in high demand globally, especially in the US, Canada, Germany, and Australia. MS in the US remains the most popular route.",
        "top_countries": ["USA", "Canada", "Germany", "Australia", "UK", "Singapore"],
        "exams_required": ["GRE (300+/340)", "TOEFL (90+) / IELTS (6.5+)"],
        "top_universities": ["MIT", "Stanford", "Caltech", "ETH Zurich", "University of Toronto", "TU Munich"],
        "avg_cost_per_year": "$30,000 - $60,000",
        "scholarships": ["Fulbright", "DAAD (Germany)", "Erasmus Mundus", "Commonwealth Scholarships"],
        "work_visa": "H-1B (USA), PR (Canada), Blue Card (Germany), 485 (Australia)",
    },
    "Medical & Healthcare": {
        "overview": "Indian MBBS graduates can practice abroad after clearing local licensing exams (USMLE, PLAB, AMC). Long but rewarding pathway.",
        "top_countries": ["USA", "UK", "Australia", "Canada", "Germany"],
        "exams_required": ["USMLE Step 1, 2 & 3 (USA)", "PLAB 1 & 2 (UK)", "AMC (Australia)", "IELTS / OET"],
        "top_universities": ["Johns Hopkins", "Harvard Medical", "Oxford Medical", "University of Melbourne", "University of Toronto"],
        "avg_cost_per_year": "$40,000 - $70,000",
        "scholarships": ["WHO Fellowships", "Fulbright", "Chevening (UK)", "Endeavour (Australia)"],
        "work_visa": "J-1/H-1B (USA), Tier 2 (UK), Skilled Worker (Australia/Canada)",
    },
    "Law & Legal Studies": {
        "overview": "LLM from top foreign universities opens doors to international law firms. Corporate and IP law are in high demand globally.",
        "top_countries": ["USA", "UK", "Australia", "Singapore"],
        "exams_required": ["LSAT (some US schools)", "IELTS/TOEFL", "Bar exam of destination country"],
        "top_universities": ["Harvard Law", "Yale Law", "Oxford Law", "Cambridge Law", "NUS Law"],
        "avg_cost_per_year": "$40,000 - $65,000",
        "scholarships": ["Chevening", "Rhodes Scholarship", "Fulbright", "Gates Cambridge"],
        "work_visa": "H-1B (USA), Skilled Worker (UK), employer-sponsored",
    },
    "Science & Research": {
        "overview": "PhD positions in Science are often fully funded abroad. India produces strong researchers who are well-placed globally.",
        "top_countries": ["USA", "UK", "Germany", "Japan", "Switzerland", "Canada"],
        "exams_required": ["GRE Subject Test (some programs)", "TOEFL/IELTS"],
        "top_universities": ["MIT", "Caltech", "Cambridge", "Max Planck Institutes", "ETH Zurich", "University of Tokyo"],
        "avg_cost_per_year": "Often fully funded (PhD stipend $20,000-$35,000/yr)",
        "scholarships": ["DAAD", "MEXT (Japan)", "CSC (China)", "Marie Curie Fellowships (EU)", "Fulbright"],
        "work_visa": "Post-study work permits available in most countries",
    },
    "Education & Teaching": {
        "overview": "Indian teachers can work in international schools worldwide. Masters in Education from abroad enhances prospects significantly.",
        "top_countries": ["UAE", "Singapore", "UK", "USA", "Australia"],
        "exams_required": ["IELTS/TOEFL", "Country-specific teacher certification"],
        "top_universities": ["UCL IoE (London)", "Harvard GSE", "Stanford GSE", "University of Melbourne"],
        "avg_cost_per_year": "$25,000 - $50,000",
        "scholarships": ["Chevening", "Commonwealth Scholarships", "Fulbright"],
        "work_visa": "Dependent on country — teaching visas available in Gulf and Singapore",
    },
    "Commerce, Finance & Business": {
        "overview": "MBA from top global schools or CA/CPA equivalence opens excellent international finance careers. Investment banking and consulting are top paths.",
        "top_countries": ["USA", "UK", "Canada", "Singapore", "Hong Kong", "UAE"],
        "exams_required": ["GMAT (700+)/GRE", "TOEFL/IELTS", "CPA/ACCA/CFA (for finance roles)"],
        "top_universities": ["Harvard Business School", "Wharton", "London Business School", "INSEAD", "Ivey (Canada)"],
        "avg_cost_per_year": "$50,000 - $80,000 (MBA)",
        "scholarships": ["School-specific merit scholarships", "Fulbright", "Chevening", "Rotary Foundation"],
        "work_visa": "H-1B (USA), PSW (UK), PR pathway (Canada)",
    },
    "Arts & Humanities": {
        "overview": "Global universities value diverse perspectives. Fully-funded PhD and MA programs available in humanities at top universities.",
        "top_countries": ["USA", "UK", "Germany", "France", "Canada"],
        "exams_required": ["GRE (some programs)", "TOEFL/IELTS"],
        "top_universities": ["Oxford", "Cambridge", "Columbia", "Sorbonne (Paris)", "Heidelberg"],
        "avg_cost_per_year": "$20,000 - $50,000 (often funded at PhD level)",
        "scholarships": ["Rhodes", "Gates Cambridge", "Fulbright", "Erasmus Mundus", "DAAD"],
        "work_visa": "Post-study work permits; academic positions sponsor visas",
    },
    "Design & Creative Arts": {
        "overview": "Global design hubs offer cutting-edge education. UX/UI and product design roles are in high demand at international tech firms.",
        "top_countries": ["USA", "UK", "Italy", "Netherlands", "Japan"],
        "exams_required": ["Portfolio (most important)", "TOEFL/IELTS"],
        "top_universities": ["Parsons (NYC)", "Royal College of Art (London)", "Politecnico di Milano", "Rhode Island School of Design"],
        "avg_cost_per_year": "$30,000 - $55,000",
        "scholarships": ["School-based merit/portfolio scholarships", "Fulbright", "Chevening"],
        "work_visa": "H-1B (USA), Graduate Route (UK), employer-sponsored",
    },
    "Performing & Fine Arts": {
        "overview": "International exposure is transformative for performing artists. Film schools and art academies abroad provide global networks.",
        "top_countries": ["USA", "UK", "France", "Germany", "Australia"],
        "exams_required": ["Audition / Portfolio", "TOEFL/IELTS"],
        "top_universities": ["Juilliard (NYC)", "RADA (London)", "La Fémis (Paris)", "AFI (Los Angeles)"],
        "avg_cost_per_year": "$25,000 - $55,000",
        "scholarships": ["Talent-based scholarships", "Fulbright", "Inlaks Foundation"],
        "work_visa": "O-1 (USA, extraordinary ability), Graduate Route (UK)",
    },
    "Sports & Physical Education": {
        "overview": "Top sports science programs and professional sports leagues are abroad. Coaching certifications from UK/Australia are globally recognized.",
        "top_countries": ["USA", "UK", "Australia", "Germany"],
        "exams_required": ["TOEFL/IELTS", "Sports trials / certificates"],
        "top_universities": ["Loughborough University (UK)", "University of Michigan", "Australian Institute of Sport"],
        "avg_cost_per_year": "$20,000 - $45,000",
        "scholarships": ["Athletic scholarships (USA)", "Commonwealth", "Government sport scholarships"],
        "work_visa": "P-1 (USA, athlete visa), skilled worker routes",
    },
    "Civil Services & Government Services": {
        "overview": "International exposure through exchange programs, UN positions, and diplomatic postings. IFS officers serve in embassies worldwide.",
        "top_countries": ["Relevant for IFS postings, UN, World Bank, IMF positions"],
        "exams_required": ["UPSC CSE (for IFS)", "UN competitive exams (YPP)"],
        "top_universities": ["Masters in Public Policy/Administration — Harvard Kennedy, LSE, Sciences Po"],
        "avg_cost_per_year": "$40,000 - $70,000 (MPP programs)",
        "scholarships": ["Chevening", "Fulbright", "Humphrey Fellowship", "Inlaks"],
        "work_visa": "Diplomatic passport (IFS), international org contracts",
    },
    "Hospitality, Travel & Tourism": {
        "overview": "Hospitality is inherently international. Swiss, French, and Dubai hotel schools are gold-standard. Global hotel chains recruit from these schools.",
        "top_countries": ["Switzerland", "UAE", "France", "USA", "Singapore", "Australia"],
        "exams_required": ["IELTS/TOEFL", "School-specific admission tests"],
        "top_universities": ["EHL Lausanne (Switzerland)", "Les Roches", "Glion", "Cornell School of Hotel Admin"],
        "avg_cost_per_year": "$35,000 - $60,000 (Swiss schools)",
        "scholarships": ["School-specific scholarships", "Government scholarships (Swiss/French)"],
        "work_visa": "Hotel chains sponsor work visas globally",
    },
    "Agriculture & Environmental Studies": {
        "overview": "Sustainable agriculture and environmental science are growing fields globally. Netherlands and Australia lead in agricultural research.",
        "top_countries": ["Netherlands", "Australia", "USA", "Germany", "New Zealand"],
        "exams_required": ["IELTS/TOEFL", "GRE (for US programs)"],
        "top_universities": ["Wageningen University (Netherlands)", "UC Davis", "University of Queensland", "ETH Zurich"],
        "avg_cost_per_year": "$15,000 - $40,000",
        "scholarships": ["Orange Knowledge Programme (Netherlands)", "Erasmus Mundus", "DAAD", "Australia Awards"],
        "work_visa": "Skilled worker visas available; agriculture listed in shortage occupations in several countries",
    },
    "Defence Research": {
        "overview": "Defence-specific education abroad is limited due to security restrictions. However, aerospace engineering and strategic studies are accessible.",
        "top_countries": ["USA", "UK", "France", "Israel"],
        "exams_required": ["GRE/TOEFL (for MS/PhD in Aerospace/Strategic Studies)"],
        "top_universities": ["MIT (Aerospace)", "Georgia Tech", "Cranfield University (UK)", "King's College London (War Studies)"],
        "avg_cost_per_year": "$30,000 - $55,000",
        "scholarships": ["Fulbright", "Chevening", "DRDO-sponsored programs (limited)"],
        "work_visa": "Security clearance often required; academic positions available",
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# STREAM REGISTRY — maps StreamInterest enum values to data
# ═══════════════════════════════════════════════════════════════════════════

_STREAM_DATA: dict[str, dict] = {
    "Engineering & Technology": {
        "colleges_india": _ENGINEERING_COLLEGES_INDIA,
        "colleges_by_state": _ENGINEERING_COLLEGES_BY_STATE,
        "career_options": _ENGINEERING_CAREER_OPTIONS,
        "coaching": _ENGINEERING_COACHING,
        "industries": ["IT & Software", "Automotive", "Aerospace", "Construction", "Telecom", "Energy", "E-commerce", "FinTech"],
        "growth_india": "Very High – India is the world's largest IT services exporter; Make in India boosting manufacturing; EV and semiconductor push underway.",
        "growth_abroad": "Very High – Global demand for engineers across all disciplines remains strong; H-1B/skilled worker visas available.",
        "10th_subjects": ["Mathematics", "Science", "English"],
        "12th_subjects": ["Physics", "Chemistry", "Mathematics"],
        "entrance_exams": ["JEE Main", "JEE Advanced", "BITSAT", "VITEEE", "State CETs"],
        "roadmap": _ROADMAP["Engineering & Technology"],
        "selection_process": _SELECTION_PROCESS["Engineering & Technology"],
        "abroad": _ABROAD_DATA["Engineering & Technology"],
    },
    "Medical & Healthcare": {
        "colleges_india": _MEDICAL_COLLEGES_INDIA,
        "colleges_by_state": _MEDICAL_COLLEGES_BY_STATE,
        "career_options": _MEDICAL_CAREER_OPTIONS,
        "coaching": _MEDICAL_COACHING,
        "industries": ["Hospitals", "Pharma", "Biotech", "MedTech", "Public Health"],
        "growth_india": "Very High – India's healthcare sector projected to reach $372B by 2027; doctor-patient ratio improving.",
        "growth_abroad": "Very High – Universal need for medical professionals; Indian doctors globally respected.",
        "10th_subjects": ["Science", "Mathematics", "English"],
        "12th_subjects": ["Physics", "Chemistry", "Biology"],
        "entrance_exams": ["NEET UG", "NEET PG", "AIIMS PG"],
        "roadmap": _ROADMAP["Medical & Healthcare"],
        "selection_process": _SELECTION_PROCESS["Medical & Healthcare"],
        "abroad": _ABROAD_DATA["Medical & Healthcare"],
    },
    "Law & Legal Studies": {
        "colleges_india": _LAW_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _LAW_CAREER_OPTIONS,
        "coaching": _LAW_COACHING,
        "industries": ["Legal Services", "Corporate Law", "Government", "Judiciary", "NGO"],
        "growth_india": "High – Corporate legal sector growing rapidly; litigation always in demand.",
        "growth_abroad": "Moderate-High – Top NLU graduates placed at international firms.",
        "10th_subjects": ["English", "Social Studies", "Any"],
        "12th_subjects": ["Any stream (Arts/Commerce/Science)"],
        "entrance_exams": ["CLAT", "AILET", "LSAT India", "MH CET Law"],
        "roadmap": _ROADMAP["Law & Legal Studies"],
        "selection_process": _SELECTION_PROCESS["Law & Legal Studies"],
        "abroad": _ABROAD_DATA["Law & Legal Studies"],
    },
    "Science & Research": {
        "colleges_india": _SCIENCE_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _SCIENCE_CAREER_OPTIONS,
        "coaching": _SCIENCE_COACHING,
        "industries": ["Research Labs", "Academia", "Government", "Pharma", "Space", "Data Science"],
        "growth_india": "Moderate-High – Government increasing R&D spending; ISRO/DRDO expanding.",
        "growth_abroad": "High – Strong demand for researchers in US, EU, and UK.",
        "10th_subjects": ["Mathematics", "Science", "English"],
        "12th_subjects": ["Physics", "Chemistry", "Mathematics/Biology"],
        "entrance_exams": ["KVPY", "NEST", "IISER Aptitude Test", "ISI Entrance", "IIT JAM (for MSc)"],
        "roadmap": _ROADMAP["Science & Research"],
        "selection_process": _SELECTION_PROCESS["Science & Research"],
        "abroad": _ABROAD_DATA["Science & Research"],
    },
    "Education & Teaching": {
        "colleges_india": _EDUCATION_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _EDUCATION_CAREER_OPTIONS,
        "coaching": _EDUCATION_COACHING,
        "industries": ["Schools", "EdTech", "Government", "NGO", "Higher Education"],
        "growth_india": "High – NEP 2020 driving education reforms; EdTech booming.",
        "growth_abroad": "Moderate – Need local certifications; international schools hire Indian teachers.",
        "10th_subjects": ["Any"],
        "12th_subjects": ["Any stream"],
        "entrance_exams": ["CTET", "State TET", "CUET (for BA Ed)"],
        "roadmap": _ROADMAP["Education & Teaching"],
        "selection_process": _SELECTION_PROCESS["Education & Teaching"],
        "abroad": _ABROAD_DATA["Education & Teaching"],
    },
    "Commerce, Finance & Business": {
        "colleges_india": _COMMERCE_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _COMMERCE_CAREER_OPTIONS,
        "coaching": _COMMERCE_COACHING,
        "industries": ["Banking", "Finance", "Accounting", "Consulting", "Insurance", "Corporate"],
        "growth_india": "Very High – Financial sector growing rapidly; every business needs CA/CS.",
        "growth_abroad": "High – CPA/ACCA equivalences; investment banking is global.",
        "10th_subjects": ["Mathematics", "English", "Social Studies"],
        "12th_subjects": ["Accountancy", "Business Studies", "Economics", "Mathematics"],
        "entrance_exams": ["CA Foundation", "CS Foundation", "CMA Foundation", "CUET", "CLAT (for BBA LLB)"],
        "roadmap": _ROADMAP["Commerce, Finance & Business"],
        "selection_process": _SELECTION_PROCESS["Commerce, Finance & Business"],
        "abroad": _ABROAD_DATA["Commerce, Finance & Business"],
    },
    "Arts & Humanities": {
        "colleges_india": _ARTS_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _ARTS_CAREER_OPTIONS,
        "coaching": _ARTS_COACHING,
        "industries": ["Government", "Media", "Publishing", "NGO", "Education", "Corporate"],
        "growth_india": "Moderate – UPSC & media careers stable; creative writing and content growing.",
        "growth_abroad": "Moderate – Academic and NGO opportunities available.",
        "10th_subjects": ["English", "Social Studies", "Any"],
        "12th_subjects": ["History", "Political Science", "Geography", "Sociology", "Psychology", "English"],
        "entrance_exams": ["UPSC", "CUET", "TISS BAT", "JNU Entrance"],
        "roadmap": _ROADMAP["Arts & Humanities"],
        "selection_process": _SELECTION_PROCESS["Arts & Humanities"],
        "abroad": _ABROAD_DATA["Arts & Humanities"],
    },
    "Design & Creative Arts": {
        "colleges_india": _DESIGN_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _DESIGN_CAREER_OPTIONS,
        "coaching": _DESIGN_COACHING,
        "industries": ["IT/Product", "Fashion", "Architecture", "Advertising", "Gaming"],
        "growth_india": "High – UX/UI demand growing exponentially; fashion and gaming sectors expanding.",
        "growth_abroad": "Very High – Design is globally in demand especially in tech.",
        "10th_subjects": ["Any with creative aptitude"],
        "12th_subjects": ["Any stream (Science/Commerce/Arts)"],
        "entrance_exams": ["UCEED", "NID DAT", "NIFT Entrance", "CEED (for MDes)"],
        "roadmap": _ROADMAP["Design & Creative Arts"],
        "selection_process": _SELECTION_PROCESS["Design & Creative Arts"],
        "abroad": _ABROAD_DATA["Design & Creative Arts"],
    },
    "Performing & Fine Arts": {
        "colleges_india": _PERFORMING_ARTS_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _PERFORMING_ARTS_CAREER_OPTIONS,
        "coaching": _PERFORMING_ARTS_COACHING,
        "industries": ["Film", "Television", "Theatre", "OTT", "Music", "Advertising"],
        "growth_india": "High – OTT platforms creating massive demand for content and talent.",
        "growth_abroad": "High – Global entertainment industry expanding.",
        "10th_subjects": ["Any with artistic interest"],
        "12th_subjects": ["Any stream"],
        "entrance_exams": ["FTII Entrance", "NSD Entrance", "BHU UET (Fine Arts)"],
        "roadmap": _ROADMAP["Performing & Fine Arts"],
        "selection_process": _SELECTION_PROCESS["Performing & Fine Arts"],
        "abroad": _ABROAD_DATA["Performing & Fine Arts"],
    },
    "Sports & Physical Education": {
        "colleges_india": _SPORTS_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _SPORTS_CAREER_OPTIONS,
        "coaching": _SPORTS_COACHING,
        "industries": ["Sports", "Fitness", "Healthcare", "Education", "Media"],
        "growth_india": "High – IPL, ISL, PKL boosting professional sports; Khelo India initiative.",
        "growth_abroad": "High – Global sports industry worth $500B+.",
        "10th_subjects": ["Physical Education", "Any"],
        "12th_subjects": ["Physical Education", "Biology", "Any"],
        "entrance_exams": ["Sports quota admissions", "BPEd entrance", "SAI trials"],
        "roadmap": _ROADMAP["Sports & Physical Education"],
        "selection_process": _SELECTION_PROCESS["Sports & Physical Education"],
        "abroad": _ABROAD_DATA["Sports & Physical Education"],
    },
    "Civil Services & Government Services": {
        "colleges_india": _CIVIL_SERVICES_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _CIVIL_SERVICES_CAREER_OPTIONS,
        "coaching": _CIVIL_SERVICES_COACHING,
        "industries": ["Government", "Administration", "Banking", "PSU"],
        "growth_india": "Stable – Government hiring is continuous; IAS/IPS remain most prestigious careers.",
        "growth_abroad": "N/A – India-specific government positions.",
        "10th_subjects": ["Any"],
        "12th_subjects": ["Any stream (Arts preferred for UPSC optional subjects)"],
        "entrance_exams": ["UPSC CSE", "SSC CGL", "IBPS PO", "State PCS"],
        "roadmap": _ROADMAP["Civil Services & Government Services"],
        "selection_process": _SELECTION_PROCESS["Civil Services & Government Services"],
        "abroad": _ABROAD_DATA["Civil Services & Government Services"],
    },
    "Hospitality, Travel & Tourism": {
        "colleges_india": _HOSPITALITY_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _HOSPITALITY_CAREER_OPTIONS,
        "coaching": _HOSPITALITY_COACHING,
        "industries": ["Hotels", "Airlines", "Travel", "Cruise", "Food & Beverage", "Events"],
        "growth_india": "High – India's tourism sector set to become 3rd largest globally.",
        "growth_abroad": "Very High – Hospitality is a global industry with international mobility.",
        "10th_subjects": ["English", "Any"],
        "12th_subjects": ["Any stream"],
        "entrance_exams": ["NCHMCT JEE", "IHM entrance exams"],
        "roadmap": _ROADMAP["Hospitality, Travel & Tourism"],
        "selection_process": _SELECTION_PROCESS["Hospitality, Travel & Tourism"],
        "abroad": _ABROAD_DATA["Hospitality, Travel & Tourism"],
    },
    "Agriculture & Environmental Studies": {
        "colleges_india": _AGRICULTURE_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _AGRICULTURE_CAREER_OPTIONS,
        "coaching": _AGRICULTURE_COACHING,
        "industries": ["Agriculture", "FMCG", "Food Processing", "Environment", "Government"],
        "growth_india": "High – Agriculture employs 42% of India; food processing sector booming.",
        "growth_abroad": "Moderate – Opportunities in sustainable agriculture and environmental consulting.",
        "10th_subjects": ["Science", "Mathematics", "English"],
        "12th_subjects": ["Physics", "Chemistry", "Biology/Mathematics"],
        "entrance_exams": ["ICAR AIEEA", "State agriculture entrance exams"],
        "roadmap": _ROADMAP["Agriculture & Environmental Studies"],
        "selection_process": _SELECTION_PROCESS["Agriculture & Environmental Studies"],
        "abroad": _ABROAD_DATA["Agriculture & Environmental Studies"],
    },
    "Defence Research": {
        "colleges_india": _DEFENCE_COLLEGES_INDIA,
        "colleges_by_state": {},
        "career_options": _DEFENCE_CAREER_OPTIONS,
        "coaching": _DEFENCE_COACHING,
        "industries": ["Defence", "Government", "Research", "Aerospace"],
        "growth_india": "High – India is 3rd largest defence spender globally; Atmanirbhar Bharat in defence.",
        "growth_abroad": "Limited – Defence is highly country-specific and classified.",
        "10th_subjects": ["Mathematics", "Science", "English", "Physical Education"],
        "12th_subjects": ["Physics", "Chemistry", "Mathematics"],
        "entrance_exams": ["NDA (UPSC)", "CDS (UPSC)", "AFCAT", "DRDO SET"],
        "roadmap": _ROADMAP["Defence Research"],
        "selection_process": _SELECTION_PROCESS["Defence Research"],
        "abroad": _ABROAD_DATA["Defence Research"],
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# PUBLIC API
# ═══════════════════════════════════════════════════════════════════════════

def get_all_stream_names() -> list[str]:
    """Return names of all 14 career streams."""
    return list(_STREAM_DATA.keys())


def get_stream_data(stream_name: str) -> dict | None:
    """Return full data dict for a given stream name, or None if not found."""
    return _STREAM_DATA.get(stream_name)


def get_top_colleges_india(stream_name: str) -> list[College]:
    """Return top 10 colleges in India for the given stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data["colleges_india"]


def get_top_colleges_by_state(stream_name: str, state: str) -> list[College]:
    """Return top 5 colleges for a stream in a specific state."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data["colleges_by_state"].get(state, [])


def get_career_options(stream_name: str) -> list[CareerOption]:
    """Return career options for a given stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data["career_options"]


def get_coaching_institutes(stream_name: str) -> list[str]:
    """Return coaching institutes for a given stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data["coaching"]


def get_industries(stream_name: str) -> list[str]:
    """Return industries for a given stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data.get("industries", [])


def get_stream_growth(stream_name: str) -> dict[str, str]:
    """Return growth aspects (India + abroad) for a stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return {"india": "", "abroad": ""}
    return {
        "india": data.get("growth_india", ""),
        "abroad": data.get("growth_abroad", ""),
    }


def get_entrance_exams(stream_name: str) -> list[str]:
    """Return entrance exams for a stream."""
    data = _STREAM_DATA.get(stream_name)
    if data is None:
        return []
    return data.get("entrance_exams", [])


def build_career_tree() -> CareerTree:
    """Build the full career path tree structure for navigation.

    Tree levels: root → 10th → 12th_stream → bachelors → masters → higher_studies → jobs
    """
    root_children: list[StreamNode] = []
    for stream_name, sdata in _STREAM_DATA.items():
        stream_id = stream_name.lower().replace(" ", "_").replace("&", "and").replace(",", "")
        jobs_node = StreamNode(
            id=f"{stream_id}_jobs",
            name="Job Opportunities",
            level="jobs",
            career_options=sdata["career_options"],
        )
        higher_studies_node = StreamNode(
            id=f"{stream_id}_higher_studies",
            name="Higher Studies / Research / PhD",
            level="higher_studies",
            children=[jobs_node],
            top_colleges_india=sdata["colleges_india"][:5],
        )
        masters_node = StreamNode(
            id=f"{stream_id}_masters",
            name="Master's Degree",
            level="masters",
            children=[higher_studies_node, jobs_node],
            top_colleges_india=sdata["colleges_india"][:5],
            top_colleges_by_state=sdata["colleges_by_state"],
        )
        bachelors_node = StreamNode(
            id=f"{stream_id}_bachelors",
            name="Bachelor's Degree",
            level="bachelors",
            children=[masters_node, jobs_node],
            top_colleges_india=sdata["colleges_india"],
            top_colleges_by_state=sdata["colleges_by_state"],
            coaching_institutes=sdata["coaching"],
        )
        twelfth_node = StreamNode(
            id=f"{stream_id}_12th",
            name=stream_name,
            level="12th",
            children=[bachelors_node],
        )
        root_children.append(twelfth_node)

    tenth_node = StreamNode(
        id="after_10th",
        name="After 10th Standard",
        level="10th",
        children=root_children,
    )
    root = StreamNode(
        id="root",
        name="Career Map",
        level="root",
        children=[tenth_node],
    )
    return CareerTree(root=root)
