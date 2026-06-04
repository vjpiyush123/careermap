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
        branch_names=branches or [],
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
# SCHOLARSHIP DATA — Top scholarship programs for each stream
# ═══════════════════════════════════════════════════════════════════════════

_SCHOLARSHIP_DATA: dict[str, list[dict]] = {
    "Engineering & Technology": [
        {"name": "AICTE Pragati Scholarship", "provider": "AICTE, Govt of India", "amount": "₹50,000/year", "eligibility": "Girl students in AICTE-approved institutions, family income < ₹8 LPA", "process": "Apply online through AICTE portal during academic year. Submit income certificate, admission proof, and bank details.", "website": "https://www.aicte-india.org/schemes/students-development-schemes/Pragati"},
        {"name": "KVPY Fellowship (now INSPIRE)", "provider": "DST, Govt of India", "amount": "₹5,000-₹7,000/month + contingency", "eligibility": "Students studying basic sciences, top performers in KVPY exam", "process": "Register on INSPIRE portal, submit academic records, appear for exam. Fellowship awarded based on merit.", "website": "https://www.online-inspire.gov.in"},
        {"name": "JN Tata Endowment Scholarship", "provider": "JN Tata Endowment Trust", "amount": "Loan scholarship up to ₹10 Lakhs", "eligibility": "Indian graduates admitted to foreign universities, age < 35", "process": "Apply online at JN Tata website between Feb-Mar. Submit admission offer letter, academic transcripts, SOP.", "website": "https://www.jntataendowment.org"},
        {"name": "HDFC Badhte Kadam Scholarship", "provider": "HDFC Ltd", "amount": "Up to ₹75,000/year", "eligibility": "Students in engineering colleges, family income < ₹6 LPA", "process": "Apply through Buddy4Study portal. Submit income proof, college ID, and academic records.", "website": "https://www.buddy4study.com/scholarship/hdfc-badhte-kadam"},
        {"name": "ONGC Scholarship", "provider": "ONGC Foundation", "amount": "₹48,000/year", "eligibility": "SC/ST students in engineering, family income < ₹2 LPA", "process": "Apply online via ONGC website. Submit caste certificate, income proof, and admission letter.", "website": "https://www.ongcscholar.org"},
    ],
    "Medical & Healthcare": [
        {"name": "AICTE/MCI Merit Scholarship", "provider": "AICTE / NMC", "amount": "₹50,000/year", "eligibility": "Merit-based for MBBS/BDS students in government colleges", "process": "Apply through college administration. Submit NEET scorecard, admission letter, and income certificate.", "website": "https://www.nmc.org.in"},
        {"name": "INSPIRE Scholarship", "provider": "DST, Govt of India", "amount": "₹80,000/year", "eligibility": "Top 1% in 12th board exams studying science/medical courses", "process": "Apply on INSPIRE portal after admission. Submit board marksheet and college admission proof.", "website": "https://www.online-inspire.gov.in"},
        {"name": "Post-Matric Scholarship for SC/ST", "provider": "Ministry of Social Justice", "amount": "Full tuition + maintenance", "eligibility": "SC/ST students, family income < ₹2.5 LPA", "process": "Apply through National Scholarship Portal. Submit caste certificate, income proof, and college fee receipt.", "website": "https://scholarships.gov.in"},
        {"name": "Kishore Vaigyanik Protsahan Yojana", "provider": "IISc Bangalore / DST", "amount": "₹5,000-₹7,000/month", "eligibility": "Students in 11th/12th studying science, through national exam", "process": "Register on KVPY website, appear for aptitude test, attend interview if shortlisted.", "website": "https://kvpy.iisc.ac.in"},
        {"name": "Lady Meherbai D Tata Education Trust", "provider": "Tata Trusts", "amount": "Varies — up to full tuition abroad", "eligibility": "Indian women graduates going abroad for higher studies in medical/healthcare", "process": "Apply to Tata Trusts with admission offer letter, academic records, and recommendation letters.", "website": "https://www.tatatrusts.org"},
    ],
    "Law & Legal Studies": [
        {"name": "NLU Merit Scholarships", "provider": "Individual NLUs", "amount": "25%-100% tuition waiver", "eligibility": "Top CLAT rankers and merit performers in NLUs", "process": "Automatically considered based on CLAT rank at time of admission. Some NLUs require separate application.", "website": "https://consortiumofnlus.ac.in"},
        {"name": "Lex Fellowship", "provider": "Various law firms", "amount": "₹50,000-₹1,00,000", "eligibility": "Law students with excellent academic record and moot court participation", "process": "Apply through law firm websites during annual fellowship cycle. Submit essays, CV, and faculty recommendation.", "website": "https://www.lexfellowship.in"},
        {"name": "Inlaks Shivdasani Foundation Scholarship", "provider": "Inlaks Foundation", "amount": "Up to $100,000 for foreign studies", "eligibility": "Indian students under 30, admitted to top foreign universities for LLM", "process": "Apply online with admission offer, academic transcripts, SOP, and references. Interview required.", "website": "https://www.inlaksfoundation.org"},
        {"name": "Central Sector Scheme of Scholarship", "provider": "MHRD, Govt of India", "amount": "₹10,000-₹20,000/year", "eligibility": "Top 20 percentile in 12th board, family income < ₹8 LPA", "process": "Apply through National Scholarship Portal after 12th results. Renewed annually based on performance.", "website": "https://scholarships.gov.in"},
        {"name": "Post-Matric Scholarship for Minorities", "provider": "Ministry of Minority Affairs", "amount": "Up to ₹25,000/year", "eligibility": "Minority community students, family income < ₹2 LPA", "process": "Apply through National Scholarship Portal. Submit minority certificate and income proof.", "website": "https://scholarships.gov.in"},
    ],
    "Science & Research": [
        {"name": "INSPIRE SHE Scholarship", "provider": "DST, Govt of India", "amount": "₹80,000/year for BSc/MSc", "eligibility": "Top 1% in 12th boards, pursuing basic/natural sciences", "process": "Register on INSPIRE portal. Submit 12th marksheet and college admission letter. Renewed based on performance.", "website": "https://www.online-inspire.gov.in"},
        {"name": "CSIR-UGC JRF/NET Fellowship", "provider": "CSIR / UGC", "amount": "₹31,000/month (JRF) + HRA", "eligibility": "MSc graduates qualifying CSIR-UGC NET exam", "process": "Apply online for CSIR-UGC NET. Qualify the exam and secure JRF. Join research at any university/lab.", "website": "https://csirhrdg.res.in"},
        {"name": "KVPY Fellowship", "provider": "DST / IISc", "amount": "₹5,000-₹7,000/month + contingency", "eligibility": "Students in 11th to 1st year BSc, through national exam", "process": "Register on KVPY website, appear for aptitude test, attend interview.", "website": "https://kvpy.iisc.ac.in"},
        {"name": "DST SERB Research Grant", "provider": "Science & Engineering Research Board", "amount": "Research project funding up to ₹30 Lakhs", "eligibility": "Early career researchers with PhD, for research projects", "process": "Submit research proposal through SERB online portal. Peer-reviewed selection.", "website": "https://www.serbonline.in"},
        {"name": "Raman Research Fellowship", "provider": "UGC / CSIR", "amount": "Full funding for post-doc abroad", "eligibility": "Indian faculty members and scientists for research at US universities", "process": "Apply through UGC portal with research proposal, CV, and invitation from US host institution.", "website": "https://www.ugc.ac.in"},
    ],
    "Education & Teaching": [
        {"name": "Central Teacher Eligibility Test (CTET) Fee Waiver", "provider": "CBSE / MHRD", "amount": "Exam fee waiver + stipend", "eligibility": "SC/ST/PwD candidates appearing for CTET", "process": "Apply through CTET website with relevant certificates for fee waiver.", "website": "https://ctet.nic.in"},
        {"name": "MHRD National Scholarship (BEd)", "provider": "MHRD, Govt of India", "amount": "₹10,000-₹20,000/year", "eligibility": "BEd students from economically weaker sections", "process": "Apply through National Scholarship Portal. Submit income certificate and college admission proof.", "website": "https://scholarships.gov.in"},
        {"name": "Fulbright Teaching Assistant Program", "provider": "USIEF (US-India Education Foundation)", "amount": "Full funding for teaching assistantship in USA", "eligibility": "Indian teachers/graduates with teaching experience, age 21-29", "process": "Apply on USIEF website. Includes online application, interview, and US university placement.", "website": "https://www.usief.org.in"},
        {"name": "Azim Premji Foundation Fellowship", "provider": "Azim Premji Foundation", "amount": "₹25,000/month stipend + accommodation", "eligibility": "Graduates with commitment to education, willing to work in rural areas", "process": "Apply online on Azim Premji Foundation website. Multi-stage selection with interviews.", "website": "https://azimpremjifoundation.org"},
        {"name": "Commonwealth Scholarship", "provider": "Commonwealth Scholarship Commission", "amount": "Full tuition + living expenses for UK study", "eligibility": "Indian citizens with first class degree, for Master's/PhD in Education in UK", "process": "Apply through UGC/MHRD nomination. Submit application with academic records and research proposal.", "website": "https://cscuk.fcdo.gov.uk"},
    ],
    "Commerce, Finance & Business": [
        {"name": "ICAI Scholarship for CA Students", "provider": "ICAI (Institute of Chartered Accountants)", "amount": "₹2,500/month", "eligibility": "Economically weak CA articleship students, family income < ₹3 LPA", "process": "Apply through ICAI regional offices with income proof and article registration details.", "website": "https://www.icai.org"},
        {"name": "National Means-cum-Merit Scholarship", "provider": "MHRD, Govt of India", "amount": "₹12,000/year", "eligibility": "Students from class 9 to 12, family income < ₹3.5 LPA, through state-level exam", "process": "Appear for NMMS exam in class 8. Apply through state education department.", "website": "https://scholarships.gov.in"},
        {"name": "Aditya Birla Scholarship", "provider": "Aditya Birla Group", "amount": "₹65,000-₹1,75,000/year", "eligibility": "Students at IIMs, XLRI, BITS, Law schools — based on merit and interview", "process": "Shortlisted based on entrance exam rank. Attend group discussion and interview at AB Group office.", "website": "https://www.adityabirla.com/scholarships"},
        {"name": "Kotak Kanya Scholarship", "provider": "Kotak Mahindra Group", "amount": "Up to ₹1.5 Lakhs/year", "eligibility": "Meritorious girl students from underprivileged families in professional courses", "process": "Apply through Buddy4Study platform with academic records, income proof, and personal essay.", "website": "https://www.buddy4study.com/scholarship/kotak-kanya-scholarship"},
        {"name": "ONGC Foundation Scholarship", "provider": "ONGC", "amount": "₹48,000/year", "eligibility": "SC/ST students in professional courses, family income < ₹2 LPA", "process": "Apply through ONGC Scholarship portal with caste and income certificates.", "website": "https://www.ongcscholar.org"},
    ],
    "Arts & Humanities": [
        {"name": "UGC Non-NET Fellowship", "provider": "UGC", "amount": "₹8,000-₹12,000/month", "eligibility": "MPhil/PhD scholars in universities who haven't qualified NET", "process": "Apply through university. Fellowship activated upon PhD registration. Submit research synopsis.", "website": "https://www.ugc.ac.in"},
        {"name": "Maulana Azad National Fellowship", "provider": "Ministry of Minority Affairs / UGC", "amount": "₹31,000/month (JRF) for 2 years, then SRF", "eligibility": "Minority community students pursuing MPhil/PhD, qualified NET", "process": "Apply on UGC website with NET qualification, minority certificate, and PhD admission letter.", "website": "https://www.ugc.ac.in"},
        {"name": "Inlaks Research Travel Grant", "provider": "Inlaks Shivdasani Foundation", "amount": "Up to ₹3 Lakhs for research travel", "eligibility": "Indian scholars pursuing humanities research, need international archive/library access", "process": "Apply online with research proposal, budget, and supervisor recommendation.", "website": "https://www.inlaksfoundation.org"},
        {"name": "Rhodes Scholarship", "provider": "Rhodes Trust", "amount": "Full funding for Oxford University study", "eligibility": "Indian citizens, age 19-25, with outstanding academic and leadership record", "process": "Apply through Rhodes India website. Multi-round selection — application, interviews at state and national level.", "website": "https://www.rhodeshouse.ox.ac.uk"},
        {"name": "Charles Wallace India Trust Grants", "provider": "Charles Wallace India Trust (UK)", "amount": "Fully funded short visits to UK for research/arts", "eligibility": "Indian nationals age 25-38 in arts/humanities/heritage for UK-based work", "process": "Apply on CWIT website with project proposal, CV, and UK institutional invitation.", "website": "https://www.charleswallaceindia.org"},
    ],
    "Design & Creative Arts": [
        {"name": "NID Fee Waiver Scheme", "provider": "National Institute of Design", "amount": "25%-100% fee waiver", "eligibility": "Economically disadvantaged students admitted to NID, family income < ₹6 LPA", "process": "Apply after admission through NID financial aid office with income documents.", "website": "https://www.nid.edu"},
        {"name": "NIFT Fee Concession", "provider": "NIFT", "amount": "Full/partial fee waiver", "eligibility": "SC/ST/EWS students admitted to NIFT campuses", "process": "Apply through NIFT admission office with caste/income certificates at time of admission.", "website": "https://www.nift.ac.in"},
        {"name": "Adobe Design Achievement Awards", "provider": "Adobe Inc.", "amount": "$10,000 prize + Adobe tools", "eligibility": "Students aged 18+ enrolled in accredited institutions globally", "process": "Submit design projects on ADAA website. Judged by international panel.", "website": "https://www.adobeawards.com"},
        {"name": "Tata Trust Individual Artist Grant", "provider": "Tata Trusts", "amount": "Up to ₹5 Lakhs", "eligibility": "Indian artists and designers with demonstrated creative practice", "process": "Apply through Tata Trusts portal with portfolio, project proposal, and artist statement.", "website": "https://www.tatatrusts.org"},
        {"name": "Central Sector Scholarship", "provider": "MHRD", "amount": "₹10,000-₹20,000/year", "eligibility": "Top 20 percentile in 12th, family income < ₹8 LPA", "process": "Apply on National Scholarship Portal after admission to design college.", "website": "https://scholarships.gov.in"},
    ],
    "Performing & Fine Arts": [
        {"name": "Ministry of Culture Scholarship", "provider": "Ministry of Culture, Govt of India", "amount": "₹5,000/month for 2 years", "eligibility": "Outstanding young artists aged 18-25 in music, dance, theatre, visual arts", "process": "Apply through Ministry of Culture website. Submit portfolio/performance video, recommendation from guru.", "website": "https://www.indiaculture.gov.in"},
        {"name": "CCRT Junior Fellowship", "provider": "Centre for Cultural Resources and Training", "amount": "₹10,000/month for 2 years", "eligibility": "Artists below age 40 for research in Indian art forms", "process": "Apply on CCRT website with research proposal and samples of artistic work.", "website": "https://ccrt.gov.in"},
        {"name": "Sahitya Kala Parishad Grant", "provider": "Delhi Government", "amount": "Project-based grants up to ₹2 Lakhs", "eligibility": "Artists and performers based in Delhi with ongoing creative projects", "process": "Submit grant application with project details and budget to Sahitya Kala Parishad office.", "website": "https://www.sahityakalaparishad.com"},
        {"name": "FTII Fee Waiver", "provider": "FTII Pune", "amount": "Full fee waiver + stipend", "eligibility": "SC/ST students admitted to FTII courses", "process": "Apply through FTII admission with caste certificate and income documents.", "website": "https://www.ftii.ac.in"},
        {"name": "Raza Foundation Fellowship", "provider": "Raza Foundation", "amount": "₹1,00,000 fellowship", "eligibility": "Young Indian artists in visual and performing arts", "process": "Apply through Raza Foundation with portfolio, artist statement, and project proposal.", "website": "https://www.razafoundation.org"},
    ],
    "Sports & Physical Education": [
        {"name": "SAI Sports Scholarship", "provider": "Sports Authority of India", "amount": "₹5,000-₹28,000/month + training", "eligibility": "Talented athletes selected through SAI trials and state sports federations", "process": "Attend SAI selection trials at regional/national centres. Selected athletes receive scholarship and training.", "website": "https://sfrms.sportsauthorityofindia.nic.in"},
        {"name": "Khelo India Scholarship", "provider": "Ministry of Youth Affairs & Sports", "amount": "₹5 Lakhs/year for 8 years", "eligibility": "Athletes identified through Khelo India Games (top performers)", "process": "Perform at Khelo India Games. Identified athletes get long-term scholarship for training and competition.", "website": "https://kheloindia.gov.in"},
        {"name": "Eklavya Award / State Sports Scholarships", "provider": "State Governments", "amount": "₹25,000-₹1,00,000/year", "eligibility": "State-level medal-winning athletes", "process": "Apply through state sports department with competition certificates and medals.", "website": "https://www.mygov.in"},
        {"name": "Prakash Padukone Badminton Academy Scholarship", "provider": "PPBA", "amount": "Full training + accommodation", "eligibility": "Young badminton players aged 10-16 with talent potential", "process": "Attend selection trials at PPBA Bangalore. Selected players receive fully funded training.", "website": "https://www.ppba.in"},
        {"name": "JSW Sports Excellence Program", "provider": "JSW Sports", "amount": "Full funding for training + international competitions", "eligibility": "Elite athletes in targeted Olympic sports", "process": "Nominated by national sports federations or identified by JSW scouts. Includes coaching, equipment, travel.", "website": "https://www.jsw.in/sports"},
    ],
    "Civil Services & Government Services": [
        {"name": "Jamia Millia Islamia UPSC Coaching", "provider": "Jamia Millia Islamia / RCA", "amount": "Free coaching + study material", "eligibility": "Graduates from minority/disadvantaged backgrounds attempting UPSC", "process": "Apply through Jamia RCA (Residential Coaching Academy). Selection based on test and interview.", "website": "https://www.jmi.ac.in"},
        {"name": "Dr. Ambedkar Foundation Scholarship", "provider": "Dr. Ambedkar Foundation", "amount": "₹70,000-₹1,00,000/year", "eligibility": "SC/ST students preparing for civil services or pursuing post-graduation", "process": "Apply through Dr. Ambedkar Foundation website with educational and caste documents.", "website": "https://www.ambedkarfoundation.nic.in"},
        {"name": "Rajiv Gandhi National Fellowship", "provider": "UGC / Ministry of Social Justice", "amount": "₹31,000/month (JRF) for 2 years, then SRF", "eligibility": "SC students pursuing PhD/MPhil in any discipline", "process": "Apply on UGC website with PhD admission proof and caste certificate.", "website": "https://www.ugc.ac.in"},
        {"name": "State Government Free UPSC Coaching", "provider": "Various State Governments", "amount": "Free coaching + hostel + monthly stipend", "eligibility": "Domiciles of respective states, usually from weaker sections", "process": "Apply through state backward class/SC-ST department. Selection through exam and interview.", "website": "https://scholarships.gov.in"},
        {"name": "Tata Trusts Individual Grant", "provider": "Tata Trusts", "amount": "Up to ₹2 Lakhs for exam preparation", "eligibility": "Meritorious students from economically weaker sections preparing for civil services", "process": "Apply on Tata Trusts website with academic records, income proof, and preparation plan.", "website": "https://www.tatatrusts.org"},
    ],
    "Hospitality, Travel & Tourism": [
        {"name": "NCHMCT JEE Merit Scholarship", "provider": "NCHMCT / IHM", "amount": "25%-100% tuition waiver", "eligibility": "Top rankers in NCHMCT JEE exam admitted to IHMs", "process": "Automatically awarded based on JEE rank and college admission. Apply at IHM admission office.", "website": "https://www.nchmct.org"},
        {"name": "Oberoi STEP Program", "provider": "The Oberoi Group", "amount": "Full scholarship (tuition + stipend)", "eligibility": "Selected students through Oberoi's Systematic Training & Education Programme", "process": "Apply through Oberoi STEP website. Undergo aptitude test, group discussion, and personal interview.", "website": "https://www.oberoihotels.com/step"},
        {"name": "IHM Fee Concession for SC/ST", "provider": "Government IHMs", "amount": "Full fee waiver", "eligibility": "SC/ST students admitted to government IHMs", "process": "Apply through IHM admission office with caste certificate.", "website": "https://www.nchmct.org"},
        {"name": "Tourism Ministry Study Grant", "provider": "Ministry of Tourism", "amount": "₹30,000-₹50,000/year", "eligibility": "Students pursuing tourism/hospitality degrees, financial need basis", "process": "Apply through Ministry of Tourism portal with admission and income documents.", "website": "https://tourism.gov.in"},
        {"name": "Swiss Hotel Management School Scholarship", "provider": "Swiss hotel schools (EHL, Les Roches)", "amount": "CHF 5,000-20,000 merit scholarship", "eligibility": "International students admitted to Swiss hospitality schools based on merit", "process": "Apply during admission to Swiss schools. Submit essays, academic records, and portfolio.", "website": "https://www.ehl.edu"},
    ],
    "Agriculture & Environmental Studies": [
        {"name": "ICAR National Talent Scholarship", "provider": "Indian Council of Agricultural Research", "amount": "₹2,000/month", "eligibility": "Students admitted to ICAR-affiliated agriculture universities through AIEEA", "process": "Apply through ICAR online portal after admission. Based on AIEEA rank.", "website": "https://icar.org.in"},
        {"name": "ICAR International Fellowship", "provider": "ICAR / DARE", "amount": "Full funding for PhD abroad", "eligibility": "ICAR scientists/faculty for doctoral research at international universities", "process": "Apply through ICAR HQ with research proposal and supervisor's recommendation.", "website": "https://icar.org.in"},
        {"name": "Borlaug Fellowship", "provider": "USDA / ICAR", "amount": "Full funding for 12-week research at US university", "eligibility": "Indian agricultural researchers and faculty", "process": "Apply through ICAR with research proposal and US host institution invitation.", "website": "https://www.usda.gov"},
        {"name": "NABARD Scholarship", "provider": "NABARD", "amount": "₹25,000-₹40,000/year", "eligibility": "Students from rural backgrounds in agriculture/allied courses", "process": "Apply through NABARD regional offices with admission proof and rural domicile certificate.", "website": "https://www.nabard.org"},
        {"name": "Erasmus Mundus (Agricultural Sciences)", "provider": "European Commission", "amount": "Full scholarship for Master's in EU universities", "eligibility": "Graduates in agriculture/environment from partner countries", "process": "Apply through Erasmus Mundus consortium website for specific agricultural programs.", "website": "https://erasmus-plus.ec.europa.eu"},
    ],
    "Defence Research": [
        {"name": "NDA/CDS Cadet Allowance", "provider": "Ministry of Defence", "amount": "₹56,100/month (starting) + free education", "eligibility": "NDA and CDS selected cadets during training", "process": "Selected through UPSC NDA/CDS exam followed by SSB interview. Full training funded by government.", "website": "https://www.nda.nic.in"},
        {"name": "DRDO Scholarship for Defence Studies", "provider": "DRDO", "amount": "₹18,000-₹25,000/month", "eligibility": "Engineering/science students working on DRDO-sponsored projects", "process": "Apply through DRDO lab recruitment for JRF/SRF positions attached to research projects.", "website": "https://www.drdo.gov.in"},
        {"name": "Sainik School Scholarship", "provider": "Sainik Schools Society", "amount": "Full fee waiver + boarding", "eligibility": "SC/ST students and wards of defence personnel", "process": "Apply through Sainik School admission (AISSEE exam). Fee waivers applied automatically for eligible categories.", "website": "https://sainikschool.ncog.gov.in"},
        {"name": "Prime Minister's Special Scholarship (J&K/Ladakh)", "provider": "AICTE / Govt of India", "amount": "₹75,000-₹1,25,000/year", "eligibility": "Students from J&K/Ladakh studying in other states", "process": "Apply through AICTE PMSSS portal. Select college, submit domicile and income certificates.", "website": "https://www.aicte-india.org/schemes/students-development-schemes/PMSSS"},
        {"name": "Agniveer Post-Service Education Fund", "provider": "Ministry of Defence", "amount": "Seva Nidhi package up to ₹11.71 Lakhs", "eligibility": "Agniveers completing 4-year service in Armed Forces", "process": "Automatic enrollment. Post-service education fund accessible for higher education or skill courses.", "website": "https://www.joinindianarmy.nic.in/agniveer"},
    ],
}


# ═══════════════════════════════════════════════════════════════════════════
# AI IMPACT DATA — AI analysis for each career stream
# ═══════════════════════════════════════════════════════════════════════════

_AI_IMPACT_DATA: dict[str, dict] = {
    "Engineering & Technology": {
        "impact_level": "Medium",
        "summary": "AI is transforming engineering through automated code generation, AI-assisted design, and smart manufacturing. While routine coding and testing tasks face high automation risk, core engineering disciplines requiring physical-world problem solving, creative system design, and cross-domain expertise remain strong. Engineers who embrace AI tools will see productivity multiply rather than job displacement.",
        "risk_mitigation": [
            "Learn AI/ML tools and integrate them into your engineering workflow (GitHub Copilot, AutoCAD AI, etc.)",
            "Focus on systems thinking and cross-disciplinary engineering skills",
            "Develop expertise in AI-augmented engineering (AI for structural analysis, predictive maintenance)",
            "Build domain expertise that AI cannot easily replicate — physical intuition and client interaction",
            "Pursue certifications in emerging areas: edge computing, quantum computing, robotics",
        ],
        "valuable_roles_5_10_years": ["AI/ML Engineer", "Robotics Engineer", "Quantum Computing Researcher", "Cybersecurity Architect", "EV & Battery Systems Engineer", "Semiconductor Design Engineer", "AR/VR Systems Architect"],
        "low_impact_areas": [
            {"role": "Robotics & Mechatronics Engineer", "explanation": "Physical-world robotics requires hardware intuition, real-world testing, and cross-disciplinary skills AI cannot replace."},
            {"role": "Cybersecurity Architect", "explanation": "Security requires adversarial thinking, creative attack modeling, and strategic planning — highly human-dependent."},
            {"role": "Systems Architect", "explanation": "Designing complex systems at scale requires deep domain understanding, trade-off analysis, and stakeholder management."},
            {"role": "Hardware Design Engineer", "explanation": "Chip and circuit design involves physical constraints, manufacturing knowledge, and creative problem solving."},
        ],
        "high_impact_areas": [
            {"role": "Manual QA / Software Tester", "explanation": "AI-powered testing tools can automate most test case generation, execution, and regression testing."},
            {"role": "Basic Web/App Developer", "explanation": "AI code generators can produce standard CRUD applications, reducing demand for junior-level developers."},
            {"role": "Data Entry Engineer", "explanation": "Automated data processing and OCR/NLP pipelines handle most structured data tasks."},
            {"role": "Technical Documentation Writer", "explanation": "AI tools can generate documentation from code, reducing manual documentation work."},
        ],
    },
    "Medical & Healthcare": {
        "impact_level": "Low",
        "summary": "Healthcare is one of the most AI-resilient career streams. While AI excels at diagnostic imaging analysis and drug discovery, the core of medicine — patient interaction, clinical judgment, empathy, surgical skills, and ethical decision-making — remains fundamentally human. AI will augment doctors rather than replace them, making healthcare professionals more effective.",
        "risk_mitigation": [
            "Learn to use AI diagnostic tools (AI radiology, pathology AI) as clinical aids",
            "Focus on patient communication, empathy, and holistic care — skills AI cannot replicate",
            "Develop expertise in telemedicine and digital health platforms",
            "Stay updated on precision medicine and genomics-based treatment approaches",
            "Consider specializations in areas combining medicine with technology (health informatics, biomedical AI)",
        ],
        "valuable_roles_5_10_years": ["Precision Medicine Specialist", "Health Informatics Director", "Telemedicine Physician", "Genomics Counselor", "AI-Assisted Surgeon", "Geriatric Specialist", "Mental Health Professional"],
        "low_impact_areas": [
            {"role": "Surgeon", "explanation": "Surgery requires dexterity, real-time judgment, and adaptability to unexpected situations — highly resistant to AI automation."},
            {"role": "Psychiatrist / Psychologist", "explanation": "Mental health care depends on human empathy, rapport building, and nuanced emotional understanding."},
            {"role": "Emergency Medicine Doctor", "explanation": "ER medicine requires rapid multi-factor decision-making, physical examination, and crisis management."},
            {"role": "Geriatric Care Specialist", "explanation": "Elderly care combines medical expertise with compassionate human interaction and family counseling."},
        ],
        "high_impact_areas": [
            {"role": "Diagnostic Radiologist (routine)", "explanation": "AI can read X-rays, CT scans, and MRIs with high accuracy, reducing demand for routine image reading."},
            {"role": "Medical Transcriptionist", "explanation": "Voice-to-text AI and NLP tools handle medical transcription increasingly well."},
            {"role": "Lab Technician (basic tests)", "explanation": "Automated lab systems handle standard blood tests and pathology with minimal human intervention."},
            {"role": "Insurance Claims Reviewer", "explanation": "AI can process and verify medical insurance claims, reducing manual review needs."},
        ],
    },
    "Law & Legal Studies": {
        "impact_level": "Medium",
        "summary": "AI is reshaping legal practice through automated document review, contract analysis, and legal research. However, courtroom advocacy, strategic negotiation, client counseling, and complex legal reasoning remain deeply human activities. Lawyers who leverage AI for research and documentation will gain significant competitive advantages.",
        "risk_mitigation": [
            "Learn legal tech tools (AI contract review, e-discovery platforms, legal analytics)",
            "Develop strong advocacy, negotiation, and interpersonal skills",
            "Specialize in areas requiring human judgment — constitutional law, criminal defence, IP strategy",
            "Build expertise in AI regulation, data privacy law, and technology law — growing demand areas",
            "Focus on client relationships and strategic advisory rather than routine document work",
        ],
        "valuable_roles_5_10_years": ["AI & Technology Lawyer", "Data Privacy & GDPR Specialist", "Cyber Law Expert", "International Arbitration Lawyer", "ESG & Climate Law Advisor", "IP Strategist"],
        "low_impact_areas": [
            {"role": "Criminal Defence Lawyer", "explanation": "Criminal law requires courtroom presence, jury persuasion, witness examination, and emotional intelligence."},
            {"role": "Constitutional Law Expert", "explanation": "Constitutional interpretation requires deep philosophical reasoning and understanding of democratic values."},
            {"role": "International Arbitrator", "explanation": "Arbitration involves complex negotiations, cultural sensitivity, and human relationship management."},
            {"role": "Human Rights Lawyer", "explanation": "Advocacy for rights requires passion, cultural awareness, and field work that AI cannot replicate."},
        ],
        "high_impact_areas": [
            {"role": "Legal Research Assistant", "explanation": "AI tools can scan millions of case laws and extract relevant precedents in seconds."},
            {"role": "Document Review Specialist", "explanation": "AI-powered e-discovery and contract analysis tools handle bulk document review."},
            {"role": "Paralegal (routine tasks)", "explanation": "Standard legal drafting, filing, and compliance checks can be automated."},
            {"role": "Patent Search Analyst", "explanation": "AI can search patent databases and identify prior art more efficiently than manual search."},
        ],
    },
    "Science & Research": {
        "impact_level": "Medium",
        "summary": "AI is accelerating scientific research through faster data analysis, simulation, and hypothesis generation. However, formulating research questions, designing experiments, interpreting results in context, and scientific creativity remain human strengths. AI is a powerful tool for scientists rather than a replacement.",
        "risk_mitigation": [
            "Learn computational methods and AI tools specific to your research domain",
            "Focus on experimental design, creative hypothesis formation, and interdisciplinary research",
            "Develop skills in AI-assisted research methodologies (bioinformatics, computational physics)",
            "Build strong communication skills for translating research to policy and public understanding",
            "Pursue interdisciplinary research combining science with AI applications",
        ],
        "valuable_roles_5_10_years": ["Computational Biologist", "AI Research Scientist", "Quantum Physicist", "Climate Modeler", "Neuroscience Researcher", "Space Science Engineer"],
        "low_impact_areas": [
            {"role": "Experimental Physicist", "explanation": "Designing and running physical experiments requires creativity, lab skills, and real-world intuition."},
            {"role": "Field Ecologist", "explanation": "Fieldwork, specimen collection, and ecosystem observation require physical presence and contextual expertise."},
            {"role": "Research Lab Director", "explanation": "Leading research teams requires mentorship, grant writing, strategic planning, and human management."},
            {"role": "Science Communicator", "explanation": "Making complex science accessible requires storytelling, empathy, and audience understanding."},
        ],
        "high_impact_areas": [
            {"role": "Data Collection Technician", "explanation": "Automated sensors, IoT devices, and drones can handle routine data collection tasks."},
            {"role": "Literature Review Analyst", "explanation": "AI tools can scan thousands of papers and synthesize literature reviews rapidly."},
            {"role": "Statistical Modeler (basic)", "explanation": "Standard statistical analyses can be automated with AI tools and pre-built models."},
            {"role": "Lab Sample Processor", "explanation": "Automated lab equipment handles routine sample preparation and processing."},
        ],
    },
    "Education & Teaching": {
        "impact_level": "Low",
        "summary": "Teaching is inherently human-centric. While AI can personalize learning content, automate grading, and provide tutoring assistance, the core of education — mentoring, inspiring, building character, managing classrooms, and developing social-emotional skills — requires human teachers. AI will be a powerful tool for educators rather than a replacement.",
        "risk_mitigation": [
            "Embrace EdTech tools and AI-assisted teaching platforms to enhance classroom experience",
            "Focus on mentoring, social-emotional learning, and character development",
            "Develop expertise in personalized/adaptive learning design",
            "Build skills in special education and inclusive teaching practices",
            "Learn to create engaging hybrid (online + offline) learning experiences",
        ],
        "valuable_roles_5_10_years": ["EdTech Curriculum Designer", "Special Education Expert", "Education Policy Advisor", "Social-Emotional Learning Specialist", "AI Literacy Educator", "Early Childhood Development Expert"],
        "low_impact_areas": [
            {"role": "Early Childhood Educator", "explanation": "Young children need human warmth, patience, and social development that AI cannot provide."},
            {"role": "Special Education Teacher", "explanation": "Students with special needs require individualized human attention, empathy, and adaptive strategies."},
            {"role": "School Counselor", "explanation": "Student counseling requires emotional intelligence, trust-building, and crisis intervention skills."},
            {"role": "Physical Education Teacher", "explanation": "Physical activity, team sports, and motor skill development require in-person human instruction."},
        ],
        "high_impact_areas": [
            {"role": "Routine Grading & Assessment", "explanation": "AI can grade objective tests, essays (basic), and provide instant feedback."},
            {"role": "Content Delivery (lectures)", "explanation": "Recorded and AI-generated content can supplement or replace standard lectures."},
            {"role": "Administrative Coordinator", "explanation": "AI can handle scheduling, attendance tracking, and routine administrative tasks."},
            {"role": "Test Paper Creator", "explanation": "AI can generate varied question papers from question banks efficiently."},
        ],
    },
    "Commerce, Finance & Business": {
        "impact_level": "High",
        "summary": "Finance and business face significant AI disruption. Algorithmic trading, AI-driven auditing, automated bookkeeping, and robo-advisory services are transforming the industry. However, strategic advisory, relationship management, complex negotiation, and regulatory navigation remain human-dominated. Professionals who combine financial expertise with AI literacy will thrive.",
        "risk_mitigation": [
            "Learn data analytics, Python/R, and financial modeling with AI tools",
            "Focus on strategic advisory, client relationship management, and complex problem-solving",
            "Develop expertise in fintech, blockchain, and digital banking platforms",
            "Build skills in regulatory technology (RegTech) and compliance automation",
            "Pursue certifications in AI for finance (CFA + AI, CA + data analytics)",
        ],
        "valuable_roles_5_10_years": ["FinTech Product Manager", "Blockchain/DeFi Analyst", "ESG Investment Advisor", "AI Risk Manager", "Wealth Tech Strategist", "Regulatory Technology Consultant"],
        "low_impact_areas": [
            {"role": "CFO / Financial Strategist", "explanation": "Strategic financial leadership requires judgment, stakeholder management, and vision that AI cannot replicate."},
            {"role": "M&A Advisor", "explanation": "Mergers & acquisitions involve complex negotiations, due diligence, and relationship management."},
            {"role": "Venture Capitalist", "explanation": "VC decisions require founder evaluation, market intuition, and network-based deal flow — deeply human."},
            {"role": "Forensic Accountant", "explanation": "Fraud investigation requires creative thinking, interviewing skills, and courtroom testimony."},
        ],
        "high_impact_areas": [
            {"role": "Bookkeeper", "explanation": "Automated accounting software handles journal entries, reconciliation, and basic bookkeeping."},
            {"role": "Tax Return Preparer", "explanation": "AI tax software can prepare and file standard tax returns with high accuracy."},
            {"role": "Bank Teller", "explanation": "Digital banking, UPI, and ATMs have already significantly reduced teller demand."},
            {"role": "Basic Financial Analyst", "explanation": "AI can generate financial reports, ratio analysis, and trend forecasts from data."},
        ],
    },
    "Arts & Humanities": {
        "impact_level": "Low",
        "summary": "Arts and humanities are among the most AI-resilient fields. While AI can generate text and images, human creativity, cultural insight, critical thinking, ethical reasoning, and emotional depth remain irreplaceable. The arts nurture the very human qualities that differentiate us from machines.",
        "risk_mitigation": [
            "Develop a unique creative voice and perspective that AI cannot replicate",
            "Learn to use AI as a creative tool — for brainstorming, research, and content augmentation",
            "Focus on critical analysis, cultural commentary, and interdisciplinary thinking",
            "Build expertise in digital humanities and computational social science",
            "Develop strong public speaking, writing, and storytelling skills",
        ],
        "valuable_roles_5_10_years": ["AI Ethics Researcher", "Cultural Policy Advisor", "Digital Humanities Scholar", "Content Strategy Director", "Social Impact Consultant", "Narrative Designer (Gaming/XR)"],
        "low_impact_areas": [
            {"role": "UPSC Civil Services Officer", "explanation": "Governance requires leadership, empathy, field-level decision making, and political acumen."},
            {"role": "Investigative Journalist", "explanation": "Deep investigative work requires source relationships, ethical judgment, and field reporting."},
            {"role": "Historian / Cultural Researcher", "explanation": "Historical interpretation requires contextual understanding, archival research, and critical analysis."},
            {"role": "Social Worker / NGO Leader", "explanation": "Social work requires empathy, community engagement, and advocacy — deeply human roles."},
        ],
        "high_impact_areas": [
            {"role": "Basic Content Writer", "explanation": "AI can generate standard articles, blog posts, and social media content at scale."},
            {"role": "Translator (standard texts)", "explanation": "AI translation tools handle routine document translation with increasing accuracy."},
            {"role": "Data Entry / Record Keeper", "explanation": "Digitization and AI-powered OCR handle document processing and data entry."},
            {"role": "Proofreader (basic)", "explanation": "AI grammar and style checkers perform basic proofreading tasks effectively."},
        ],
    },
    "Design & Creative Arts": {
        "impact_level": "Medium",
        "summary": "Generative AI is creating both disruption and opportunity in design. AI can produce images, layouts, and prototypes rapidly, but human designers bring cultural sensitivity, user empathy, strategic thinking, and brand storytelling that AI lacks. Designers who master AI tools will become significantly more productive and valuable.",
        "risk_mitigation": [
            "Master AI design tools (Midjourney, DALL-E, Figma AI, Adobe Firefly) as productivity multipliers",
            "Focus on design thinking, user research, and strategic design — not just visual execution",
            "Develop expertise in UX strategy, service design, and design systems",
            "Build a strong personal brand and unique design aesthetic",
            "Learn prompt engineering and AI-assisted design workflows",
        ],
        "valuable_roles_5_10_years": ["AI-Augmented UX Designer", "Design Systems Architect", "Sustainable Fashion Designer", "XR Experience Designer", "Generative Design Specialist", "Design Ethicist"],
        "low_impact_areas": [
            {"role": "UX Researcher", "explanation": "Understanding human behavior through interviews, usability tests, and ethnography requires human empathy."},
            {"role": "Design Strategist", "explanation": "Aligning design with business goals requires strategic thinking, stakeholder management, and vision."},
            {"role": "Sustainable Fashion Designer", "explanation": "Sustainable design requires material knowledge, ethical sourcing, and cultural awareness."},
            {"role": "Interior/Architecture Designer", "explanation": "Spatial design involves client interaction, site visits, material selection, and regulatory compliance."},
        ],
        "high_impact_areas": [
            {"role": "Production Graphic Designer", "explanation": "AI tools can generate social media graphics, banners, and templates at scale."},
            {"role": "Stock Illustrator", "explanation": "AI image generators produce illustrations and stock imagery, reducing demand for generic illustration."},
            {"role": "Basic Logo Designer", "explanation": "AI logo generators create acceptable logo options for small businesses quickly."},
            {"role": "Photo Retoucher", "explanation": "AI photo editing tools handle background removal, color correction, and retouching automatically."},
        ],
    },
    "Performing & Fine Arts": {
        "impact_level": "Low",
        "summary": "Performing arts are inherently human experiences. Live performance, emotional expression, physical presence, and artistic authenticity cannot be replicated by AI. While AI can assist in production, music generation, and visual effects, the essence of performing arts — connecting with audiences through human emotion — remains irreplaceable.",
        "risk_mitigation": [
            "Develop versatile performance skills across multiple formats (live, digital, immersive)",
            "Learn to use AI tools for production — AI music composition, virtual sets, motion capture",
            "Build a strong personal brand and online presence for direct audience engagement",
            "Explore emerging performance formats — VR theatre, interactive storytelling, gaming",
            "Develop teaching and mentoring skills as a secondary income stream",
        ],
        "valuable_roles_5_10_years": ["Immersive Experience Creator", "Motion Capture Actor", "AI-Assisted Music Producer", "Virtual Production Specialist", "Digital Performance Artist", "Content Creator (multi-platform)"],
        "low_impact_areas": [
            {"role": "Theatre Actor", "explanation": "Live theatre depends on presence, audience energy, and unique nightly performances."},
            {"role": "Classical Musician", "explanation": "Live musical performance requires technical mastery, emotional depth, and audience connection."},
            {"role": "Dance Choreographer", "explanation": "Choreography combines physical creativity, spatial awareness, and cultural expression."},
            {"role": "Film Director", "explanation": "Directing requires creative vision, actor management, and complex decision-making on set."},
        ],
        "high_impact_areas": [
            {"role": "Background Music Composer (stock)", "explanation": "AI music generators produce royalty-free background music for videos and ads."},
            {"role": "Voice-over Artist (basic)", "explanation": "AI voice synthesis can generate natural-sounding voiceovers for standard content."},
            {"role": "Basic Video Editor", "explanation": "AI editing tools can auto-cut, color grade, and add effects to standard video content."},
            {"role": "Subtitle / Dubbing Technician", "explanation": "AI dubbing and subtitle generation tools handle standard localization tasks."},
        ],
    },
    "Sports & Physical Education": {
        "impact_level": "Low",
        "summary": "Sports is fundamentally about human physical performance, competition, and teamwork. AI enhances sports through performance analytics, training optimization, and injury prevention, but the actual playing, coaching relationships, and competitive spirit remain entirely human. AI is a powerful tool for athletes and coaches, not a replacement.",
        "risk_mitigation": [
            "Learn sports analytics and data-driven performance optimization",
            "Use wearable tech and AI tools for training enhancement and injury prevention",
            "Develop coaching and mentoring skills alongside athletic performance",
            "Build expertise in sports science, biomechanics, and nutrition",
            "Explore sports media, commentary, and content creation as career extensions",
        ],
        "valuable_roles_5_10_years": ["Sports Data Analyst", "Performance Science Director", "E-Sports Professional", "Sports Tech Entrepreneur", "Athlete Wellness Manager", "Sports Biomechanics Expert"],
        "low_impact_areas": [
            {"role": "Professional Athlete", "explanation": "Athletic competition is inherently human — physical performance, strategy, and sportsmanship."},
            {"role": "Head Coach", "explanation": "Coaching requires motivational leadership, tactical intuition, and player relationship management."},
            {"role": "Sports Psychologist", "explanation": "Mental performance coaching requires empathy, trust, and understanding of individual psychology."},
            {"role": "Physical Education Teacher", "explanation": "Teaching sports and physical activity requires demonstration, safety supervision, and inspiration."},
        ],
        "high_impact_areas": [
            {"role": "Scorekeeper / Stats Recorder", "explanation": "Automated tracking systems and computer vision handle real-time sports statistics."},
            {"role": "Basic Fitness Trainer (template-based)", "explanation": "AI fitness apps generate personalized workout plans, reducing demand for generic trainers."},
            {"role": "Sports Journalist (match reports)", "explanation": "AI can generate standard match reports and statistics summaries automatically."},
            {"role": "Ticket Sales Agent", "explanation": "Online ticketing platforms and AI chatbots handle most ticket sales operations."},
        ],
    },
    "Civil Services & Government Services": {
        "impact_level": "Low",
        "summary": "Government services require human judgment, political acumen, public accountability, and ethical leadership. While AI can improve government efficiency through e-governance and data analytics, the core of civil services — policy making, crisis management, public engagement, and administrative leadership — remains firmly human. AI will make officers more effective, not obsolete.",
        "risk_mitigation": [
            "Learn e-governance tools and digital administration platforms",
            "Develop data literacy for evidence-based policy making",
            "Build expertise in emerging areas — AI governance, digital policy, cyber security regulation",
            "Focus on leadership, crisis management, and public communication skills",
            "Stay updated on government technology initiatives (Digital India, Smart Cities)",
        ],
        "valuable_roles_5_10_years": ["AI Governance Officer", "Digital Policy Advisor", "Smart City Administrator", "Cyber Security Regulator", "Data-Driven Policy Maker", "E-Governance Specialist"],
        "low_impact_areas": [
            {"role": "IAS/IPS/IFS Officer", "explanation": "Administrative leadership requires judgment, political navigation, and public accountability."},
            {"role": "District Collector", "explanation": "District administration involves crisis management, public hearings, and multi-stakeholder coordination."},
            {"role": "Diplomat (IFS)", "explanation": "Diplomacy requires cultural intelligence, negotiation skills, and strategic relationship building."},
            {"role": "Election Commission Officer", "explanation": "Election management requires integrity, public trust, and complex logistical coordination."},
        ],
        "high_impact_areas": [
            {"role": "Government Data Entry Clerk", "explanation": "Digitization and AI-powered data processing reduce manual data entry needs."},
            {"role": "RTI Response Processor", "explanation": "AI can categorize and draft responses to routine RTI queries."},
            {"role": "Permit/License Processing Clerk", "explanation": "Automated e-governance portals handle license applications and approvals."},
            {"role": "Basic Translation Services", "explanation": "AI translation tools handle standard government document translations."},
        ],
    },
    "Hospitality, Travel & Tourism": {
        "impact_level": "Medium",
        "summary": "Hospitality is built on human warmth and personal service. While AI handles booking, pricing, and basic customer queries efficiently, the luxury hospitality experience — personalized service, cultural hosting, crisis management, and creating memorable guest experiences — depends on human touch. Mid-segment operations face more disruption than luxury/experiential tourism.",
        "risk_mitigation": [
            "Focus on luxury hospitality and experiential tourism where human touch is premium",
            "Learn revenue management systems and hospitality AI tools",
            "Develop cultural intelligence and multilingual capabilities",
            "Build expertise in sustainable tourism and eco-tourism",
            "Explore food tech, culinary innovation, and fusion cuisine",
        ],
        "valuable_roles_5_10_years": ["Experience Designer", "Sustainable Tourism Manager", "Luxury Concierge Specialist", "Food Tech Innovator", "Wellness Tourism Director", "Cultural Tourism Curator"],
        "low_impact_areas": [
            {"role": "Luxury Hotel General Manager", "explanation": "Managing premium properties requires leadership, guest relationship mastery, and crisis handling."},
            {"role": "Executive Chef", "explanation": "Culinary creativity, kitchen leadership, and menu innovation remain distinctly human."},
            {"role": "Event Manager", "explanation": "Live event management requires real-time coordination, vendor relationships, and creative problem-solving."},
            {"role": "Cultural Tour Guide", "explanation": "Guided tours need storytelling, local knowledge, and personal engagement with travelers."},
        ],
        "high_impact_areas": [
            {"role": "Hotel Reservation Agent", "explanation": "Online booking platforms and AI chatbots handle most hotel reservations."},
            {"role": "Travel Booking Agent", "explanation": "AI-powered travel platforms (MakeMyTrip, Booking.com) automate itinerary planning."},
            {"role": "Front Desk (basic check-in)", "explanation": "Self-check-in kiosks and mobile apps reduce front desk staffing needs."},
            {"role": "Menu Translation / Standard F&B Service", "explanation": "Digital menus, QR ordering, and AI translation reduce routine F&B tasks."},
        ],
    },
    "Agriculture & Environmental Studies": {
        "impact_level": "Medium",
        "summary": "AI is transforming agriculture through precision farming, drone monitoring, automated irrigation, and crop disease detection. However, farming decisions require local knowledge, seasonal understanding, soil expertise, and community engagement. Environmental science combines fieldwork, policy advocacy, and ecological understanding that remains human-dependent.",
        "risk_mitigation": [
            "Learn precision agriculture technologies — drones, satellite imaging, IoT sensors",
            "Develop expertise in sustainable and organic farming practices",
            "Build skills in agricultural data analytics and farm management software",
            "Focus on agri-entrepreneurship and farm-to-fork business models",
            "Stay updated on climate adaptation strategies and environmental policy",
        ],
        "valuable_roles_5_10_years": ["Precision Agriculture Specialist", "Climate Adaptation Scientist", "Agri-Tech Entrepreneur", "Sustainable Food Systems Manager", "Carbon Credit Consultant", "Vertical Farming Engineer"],
        "low_impact_areas": [
            {"role": "Agricultural Extension Officer", "explanation": "Farmer training requires field visits, local language skills, and trust-building with rural communities."},
            {"role": "Environmental Impact Assessor", "explanation": "EIA requires site visits, stakeholder consultations, and complex regulatory knowledge."},
            {"role": "Forest Officer / Conservationist", "explanation": "Wildlife conservation requires fieldwork, community engagement, and enforcement activities."},
            {"role": "Organic Farming Consultant", "explanation": "Organic farming advice requires soil knowledge, local climate understanding, and hands-on expertise."},
        ],
        "high_impact_areas": [
            {"role": "Crop Monitoring Technician", "explanation": "Drones and satellite imagery automate crop health monitoring and yield prediction."},
            {"role": "Soil Testing Lab Technician", "explanation": "Automated soil analysis equipment handles standard testing with minimal human input."},
            {"role": "Weather Data Recorder", "explanation": "Automated weather stations and AI models handle climate data collection and forecasting."},
            {"role": "Commodity Price Tracker", "explanation": "AI-powered market platforms track and predict commodity prices automatically."},
        ],
    },
    "Defence Research": {
        "impact_level": "Medium",
        "summary": "AI is increasingly critical in defence — autonomous systems, cyber warfare, surveillance, and strategic analysis all leverage AI. However, command decisions, troop leadership, ethical judgment in conflict, and national security strategy remain firmly in human hands. Military leadership and defence research will increasingly combine human judgment with AI capabilities.",
        "risk_mitigation": [
            "Develop expertise in AI-enabled defence systems and autonomous technologies",
            "Build skills in cyber security, electronic warfare, and information operations",
            "Focus on strategic thinking, leadership, and decision-making under pressure",
            "Learn about defence AI ethics and autonomous weapons governance",
            "Stay updated on India's defence technology modernization programs",
        ],
        "valuable_roles_5_10_years": ["Cyber Warfare Specialist", "Autonomous Systems Engineer", "Defence AI Researcher", "Space Defence Analyst", "Electronic Warfare Expert", "Strategic Intelligence Analyst"],
        "low_impact_areas": [
            {"role": "Military Commander", "explanation": "Command leadership requires moral courage, troop motivation, and battlefield judgment."},
            {"role": "Intelligence Officer", "explanation": "Human intelligence (HUMINT) requires interpersonal skills, cultural knowledge, and analytical reasoning."},
            {"role": "Defence Diplomat", "explanation": "Military diplomacy requires cultural sensitivity, negotiation skills, and strategic relationship building."},
            {"role": "Combat Pilot", "explanation": "Fighter pilots require split-second judgment, physical endurance, and situational awareness."},
        ],
        "high_impact_areas": [
            {"role": "Surveillance Operator (routine)", "explanation": "AI-powered surveillance systems can monitor borders and analyze feeds continuously."},
            {"role": "Logistics Coordinator (supply chain)", "explanation": "AI optimizes military supply chains, inventory management, and logistics planning."},
            {"role": "Basic Communication Operator", "explanation": "Automated communication systems handle standard military communications."},
            {"role": "Map/Terrain Analyst (basic)", "explanation": "AI geospatial tools generate terrain analysis and mapping from satellite data."},
        ],
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# STATE-LEVEL COLLEGES for streams that were missing them
# ═══════════════════════════════════════════════════════════════════════════

_LAW_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Karnataka": [
        _college("NLSIU Bangalore", 1, "Bangalore", "Karnataka", 2.5, 15.0, 120, "https://www.nls.ac.in"),
        _college("Karnataka State Law University", 2, "Hubli", "Karnataka", 0.3, 4.0, 500, ""),
        _college("Christ University (Law)", 3, "Bangalore", "Karnataka", 2.0, 5.0, 200, ""),
        _college("Bangalore Institute of Legal Studies", 4, "Bangalore", "Karnataka", 0.5, 3.5, 150, ""),
        _college("KLE Society's Law College", 5, "Bangalore", "Karnataka", 0.8, 3.0, 200, ""),
    ],
    "Delhi": [
        _college("NLU Delhi", 1, "New Delhi", "Delhi", 2.0, 14.0, 120, "https://nludelhi.ac.in"),
        _college("Faculty of Law DU", 2, "New Delhi", "Delhi", 0.2, 8.0, 500, ""),
        _college("Jamia Millia Islamia (Law)", 3, "New Delhi", "Delhi", 0.3, 5.0, 200, ""),
        _college("Amity Law School Delhi", 4, "New Delhi", "Delhi", 2.5, 4.0, 300, ""),
        _college("Guru Gobind Singh IP University (Law)", 5, "New Delhi", "Delhi", 0.5, 4.0, 400, ""),
    ],
    "Maharashtra": [
        _college("Government Law College Mumbai", 1, "Mumbai", "Maharashtra", 0.1, 6.0, 600, ""),
        _college("ILS Law College Pune", 2, "Pune", "Maharashtra", 0.3, 5.0, 400, ""),
        _college("Symbiosis Law School Pune", 3, "Pune", "Maharashtra", 3.0, 7.0, 200, ""),
        _college("Maharashtra National Law University", 4, "Mumbai", "Maharashtra", 2.0, 8.0, 120, ""),
        _college("K.C. Law College Mumbai", 5, "Mumbai", "Maharashtra", 0.2, 4.0, 300, ""),
    ],
    "West Bengal": [
        _college("WBNUJS Kolkata", 1, "Kolkata", "West Bengal", 2.0, 12.0, 100, ""),
        _college("University of Calcutta (Law)", 2, "Kolkata", "West Bengal", 0.1, 3.0, 500, ""),
        _college("Jogesh Chandra Chaudhuri Law College", 3, "Kolkata", "West Bengal", 0.1, 2.5, 300, ""),
        _college("Surendranath Law College", 4, "Kolkata", "West Bengal", 0.1, 2.0, 200, ""),
        _college("KIIT Law School", 5, "Kolkata", "West Bengal", 1.5, 3.5, 150, ""),
    ],
    "Telangana": [
        _college("NALSAR Hyderabad", 1, "Hyderabad", "Telangana", 2.5, 14.0, 120, "https://www.nalsar.ac.in"),
        _college("Osmania University (Law)", 2, "Hyderabad", "Telangana", 0.1, 3.0, 400, ""),
        _college("Symbiosis Law School Hyderabad", 3, "Hyderabad", "Telangana", 2.5, 5.0, 120, ""),
        _college("ICFAI Law School", 4, "Hyderabad", "Telangana", 1.5, 3.5, 200, ""),
        _college("Mahindra University (Law)", 5, "Hyderabad", "Telangana", 3.0, 5.0, 100, ""),
    ],
}

_SCIENCE_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Karnataka": [
        _college("IISc Bangalore", 1, "Bangalore", "Karnataka", 0.5, 22.0, 400, "https://iisc.ac.in"),
        _college("Christ University", 2, "Bangalore", "Karnataka", 1.5, 5.0, 1000, ""),
        _college("Jain University", 3, "Bangalore", "Karnataka", 1.5, 4.0, 500, ""),
        _college("St. Joseph's College", 4, "Bangalore", "Karnataka", 0.5, 3.5, 400, ""),
        _college("Manipal Institute of Technology", 5, "Manipal", "Karnataka", 3.0, 6.0, 600, ""),
    ],
    "Delhi": [
        _college("St. Stephen's College DU", 1, "New Delhi", "Delhi", 0.1, 5.0, 400, ""),
        _college("Hindu College DU", 2, "New Delhi", "Delhi", 0.1, 4.5, 400, ""),
        _college("Miranda House DU", 3, "New Delhi", "Delhi", 0.1, 4.0, 300, ""),
        _college("Hansraj College DU", 4, "New Delhi", "Delhi", 0.1, 4.0, 300, ""),
        _college("IIIT Delhi", 5, "New Delhi", "Delhi", 3.0, 15.0, 500, ""),
    ],
    "Maharashtra": [
        _college("Fergusson College Pune", 1, "Pune", "Maharashtra", 0.1, 3.0, 1200, ""),
        _college("St. Xavier's College Mumbai", 2, "Mumbai", "Maharashtra", 0.5, 4.0, 500, ""),
        _college("Ruia College Mumbai", 3, "Mumbai", "Maharashtra", 0.1, 3.0, 600, ""),
        _college("Savitribai Phule Pune University", 4, "Pune", "Maharashtra", 0.1, 3.0, 2000, ""),
        _college("IIT Bombay", 5, "Mumbai", "Maharashtra", 2.5, 21.0, 1200, ""),
    ],
    "Tamil Nadu": [
        _college("Loyola College Chennai", 1, "Chennai", "Tamil Nadu", 0.2, 4.5, 600, ""),
        _college("Madras Christian College", 2, "Chennai", "Tamil Nadu", 0.2, 3.5, 500, ""),
        _college("PSG College of Arts & Science", 3, "Coimbatore", "Tamil Nadu", 0.5, 3.0, 400, ""),
        _college("CMI Chennai", 4, "Chennai", "Tamil Nadu", 0.1, 12.0, 50, ""),
        _college("IIT Madras", 5, "Chennai", "Tamil Nadu", 2.5, 19.5, 1050, ""),
    ],
    "West Bengal": [
        _college("Presidency University Kolkata", 1, "Kolkata", "West Bengal", 0.1, 3.5, 500, ""),
        _college("ISI Kolkata", 2, "Kolkata", "West Bengal", 0.1, 15.0, 50, ""),
        _college("St. Xavier's College Kolkata", 3, "Kolkata", "West Bengal", 0.3, 3.5, 400, ""),
        _college("Jadavpur University", 4, "Kolkata", "West Bengal", 0.2, 7.0, 1500, ""),
        _college("Scottish Church College", 5, "Kolkata", "West Bengal", 0.1, 2.5, 300, ""),
    ],
}

_EDUCATION_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Delhi": [
        _college("Lady Shri Ram College (DU)", 1, "New Delhi", "Delhi", 0.1, 4.0, 300, ""),
        _college("Jamia Millia Islamia", 2, "New Delhi", "Delhi", 0.2, 3.5, 400, ""),
        _college("CIE, University of Delhi", 3, "New Delhi", "Delhi", 0.1, 3.5, 200, ""),
        _college("IGNOU (BEd)", 4, "New Delhi", "Delhi", 0.3, 2.5, 5000, ""),
        _college("IP University (BEd)", 5, "New Delhi", "Delhi", 0.5, 3.0, 400, ""),
    ],
    "Maharashtra": [
        _college("TISS Mumbai", 1, "Mumbai", "Maharashtra", 0.5, 6.0, 200, "https://www.tiss.edu"),
        _college("SNDT Women's University", 2, "Mumbai", "Maharashtra", 0.2, 3.0, 500, ""),
        _college("Savitribai Phule Pune University", 3, "Pune", "Maharashtra", 0.1, 2.5, 1000, ""),
        _college("Tilak College of Education", 4, "Pune", "Maharashtra", 0.3, 2.5, 200, ""),
        _college("University of Mumbai (BEd)", 5, "Mumbai", "Maharashtra", 0.2, 2.5, 800, ""),
    ],
    "Karnataka": [
        _college("Azim Premji University", 1, "Bangalore", "Karnataka", 1.0, 5.0, 300, ""),
        _college("Christ University (BEd)", 2, "Bangalore", "Karnataka", 1.0, 3.5, 200, ""),
        _college("University of Mysore (BEd)", 3, "Mysore", "Karnataka", 0.1, 2.5, 300, ""),
        _college("Bangalore University (BEd)", 4, "Bangalore", "Karnataka", 0.2, 2.5, 500, ""),
        _college("JSS Institute of Education", 5, "Mysore", "Karnataka", 0.3, 2.5, 200, ""),
    ],
    "Uttar Pradesh": [
        _college("BHU (BEd)", 1, "Varanasi", "Uttar Pradesh", 0.1, 3.0, 500, ""),
        _college("AMU (BEd)", 2, "Aligarh", "Uttar Pradesh", 0.1, 2.5, 400, ""),
        _college("Lucknow University (BEd)", 3, "Lucknow", "Uttar Pradesh", 0.1, 2.5, 300, ""),
        _college("Allahabad University (BEd)", 4, "Prayagraj", "Uttar Pradesh", 0.1, 2.0, 300, ""),
        _college("Amity University (BEd)", 5, "Noida", "Uttar Pradesh", 1.5, 3.0, 200, ""),
    ],
}

_COMMERCE_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Delhi": [
        _college("SRCC Delhi", 1, "New Delhi", "Delhi", 0.3, 8.0, 600, ""),
        _college("Hindu College DU", 2, "New Delhi", "Delhi", 0.1, 6.0, 400, ""),
        _college("Hansraj College DU", 3, "New Delhi", "Delhi", 0.1, 5.5, 400, ""),
        _college("Lady Shri Ram College", 4, "New Delhi", "Delhi", 0.1, 5.0, 300, ""),
        _college("Kirori Mal College DU", 5, "New Delhi", "Delhi", 0.1, 4.5, 400, ""),
    ],
    "Maharashtra": [
        _college("St. Xavier's College Mumbai", 1, "Mumbai", "Maharashtra", 0.5, 6.0, 500, ""),
        _college("Narsee Monjee College Mumbai", 2, "Mumbai", "Maharashtra", 0.5, 5.0, 400, ""),
        _college("HR College Mumbai", 3, "Mumbai", "Maharashtra", 0.3, 4.5, 400, ""),
        _college("Symbiosis College Pune", 4, "Pune", "Maharashtra", 0.5, 4.0, 600, ""),
        _college("Mithibai College Mumbai", 5, "Mumbai", "Maharashtra", 0.3, 3.5, 500, ""),
    ],
    "Karnataka": [
        _college("Christ University", 1, "Bangalore", "Karnataka", 1.5, 5.0, 1000, ""),
        _college("St. Joseph's College", 2, "Bangalore", "Karnataka", 0.5, 4.0, 500, ""),
        _college("Jain University", 3, "Bangalore", "Karnataka", 1.5, 4.0, 600, ""),
        _college("Mount Carmel College", 4, "Bangalore", "Karnataka", 0.5, 3.5, 400, ""),
        _college("Bangalore University", 5, "Bangalore", "Karnataka", 0.2, 3.0, 2000, ""),
    ],
    "Tamil Nadu": [
        _college("Loyola College Chennai", 1, "Chennai", "Tamil Nadu", 0.2, 4.5, 600, ""),
        _college("Madras Christian College", 2, "Chennai", "Tamil Nadu", 0.2, 3.5, 500, ""),
        _college("PSG College Coimbatore", 3, "Coimbatore", "Tamil Nadu", 0.5, 3.5, 400, ""),
        _college("SRM University", 4, "Chennai", "Tamil Nadu", 2.0, 4.0, 500, ""),
        _college("Anna Adarsh College", 5, "Chennai", "Tamil Nadu", 0.2, 3.0, 300, ""),
    ],
}

_ARTS_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Delhi": [
        _college("St. Stephen's College DU", 1, "New Delhi", "Delhi", 0.1, 5.0, 400, ""),
        _college("Lady Shri Ram College DU", 2, "New Delhi", "Delhi", 0.1, 4.5, 300, ""),
        _college("Hindu College DU", 3, "New Delhi", "Delhi", 0.1, 4.0, 400, ""),
        _college("Miranda House DU", 4, "New Delhi", "Delhi", 0.1, 4.0, 300, ""),
        _college("JNU", 5, "New Delhi", "Delhi", 0.1, 5.0, 300, ""),
    ],
    "Maharashtra": [
        _college("Fergusson College Pune", 1, "Pune", "Maharashtra", 0.1, 3.0, 1200, ""),
        _college("TISS Mumbai", 2, "Mumbai", "Maharashtra", 0.5, 6.0, 200, ""),
        _college("St. Xavier's College Mumbai", 3, "Mumbai", "Maharashtra", 0.5, 4.0, 500, ""),
        _college("Elphinstone College Mumbai", 4, "Mumbai", "Maharashtra", 0.1, 3.0, 400, ""),
        _college("Savitribai Phule Pune University", 5, "Pune", "Maharashtra", 0.1, 2.5, 2000, ""),
    ],
    "West Bengal": [
        _college("Presidency University Kolkata", 1, "Kolkata", "West Bengal", 0.1, 3.5, 500, ""),
        _college("Jadavpur University", 2, "Kolkata", "West Bengal", 0.2, 4.0, 1500, ""),
        _college("St. Xavier's College Kolkata", 3, "Kolkata", "West Bengal", 0.3, 3.5, 400, ""),
        _college("Calcutta University", 4, "Kolkata", "West Bengal", 0.1, 2.5, 2000, ""),
        _college("Scottish Church College", 5, "Kolkata", "West Bengal", 0.1, 2.0, 300, ""),
    ],
    "Karnataka": [
        _college("Christ University", 1, "Bangalore", "Karnataka", 1.5, 4.0, 1000, ""),
        _college("St. Joseph's College", 2, "Bangalore", "Karnataka", 0.5, 3.5, 400, ""),
        _college("Jain University", 3, "Bangalore", "Karnataka", 1.5, 3.5, 600, ""),
        _college("University of Mysore", 4, "Mysore", "Karnataka", 0.1, 2.5, 1000, ""),
        _college("Mount Carmel College", 5, "Bangalore", "Karnataka", 0.5, 3.0, 300, ""),
    ],
}

_DESIGN_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Gujarat": [
        _college("NID Ahmedabad", 1, "Ahmedabad", "Gujarat", 3.0, 10.0, 200, "https://www.nid.edu"),
        _college("CEPT University", 2, "Ahmedabad", "Gujarat", 2.5, 6.0, 200, ""),
        _college("MICA Ahmedabad", 3, "Ahmedabad", "Gujarat", 3.0, 8.0, 200, ""),
        _college("L.D. College of Engineering (Design)", 4, "Ahmedabad", "Gujarat", 0.5, 4.0, 100, ""),
        _college("Karnavati University", 5, "Gandhinagar", "Gujarat", 2.0, 3.5, 150, ""),
    ],
    "Maharashtra": [
        _college("IIT Bombay (IDC)", 1, "Mumbai", "Maharashtra", 2.5, 15.0, 50, ""),
        _college("MIT Institute of Design Pune", 2, "Pune", "Maharashtra", 3.0, 5.0, 200, ""),
        _college("Symbiosis Institute of Design", 3, "Pune", "Maharashtra", 3.5, 5.0, 150, ""),
        _college("JJ School of Art Mumbai", 4, "Mumbai", "Maharashtra", 0.1, 2.5, 150, ""),
        _college("L.S. Raheja School of Art", 5, "Mumbai", "Maharashtra", 1.0, 3.0, 100, ""),
    ],
    "Delhi": [
        _college("NIFT Delhi", 1, "New Delhi", "Delhi", 2.0, 8.0, 300, "https://www.nift.ac.in"),
        _college("Pearl Academy", 2, "New Delhi", "Delhi", 4.0, 4.0, 400, ""),
        _college("School of Planning and Architecture", 3, "New Delhi", "Delhi", 0.5, 8.0, 100, ""),
        _college("IIIT Delhi (HCI)", 4, "New Delhi", "Delhi", 3.0, 12.0, 50, ""),
        _college("Ambedkar University Delhi", 5, "New Delhi", "Delhi", 0.2, 3.0, 100, ""),
    ],
    "Karnataka": [
        _college("Srishti Manipal Institute", 1, "Bangalore", "Karnataka", 3.0, 5.0, 300, ""),
        _college("NID Bangalore Campus", 2, "Bangalore", "Karnataka", 3.0, 9.0, 100, ""),
        _college("Jain University (Design)", 3, "Bangalore", "Karnataka", 2.0, 3.5, 150, ""),
        _college("Christ University (Design)", 4, "Bangalore", "Karnataka", 1.5, 3.5, 100, ""),
        _college("Reva University (Design)", 5, "Bangalore", "Karnataka", 1.5, 3.0, 100, ""),
    ],
}

_PERFORMING_ARTS_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Maharashtra": [
        _college("FTII Pune", 1, "Pune", "Maharashtra", 0.5, 5.0, 50, "https://www.ftii.ac.in"),
        _college("JJ School of Art Mumbai", 2, "Mumbai", "Maharashtra", 0.1, 2.5, 150, ""),
        _college("Whistling Woods International", 3, "Mumbai", "Maharashtra", 5.0, 4.0, 200, ""),
        _college("Lalit Kala Kendra (Savitribai Phule)", 4, "Pune", "Maharashtra", 0.1, 2.0, 100, ""),
        _college("Sir JJ School of Applied Art", 5, "Mumbai", "Maharashtra", 0.1, 2.5, 100, ""),
    ],
    "Delhi": [
        _college("NSD New Delhi", 1, "New Delhi", "Delhi", 0.3, 3.0, 30, "https://nsd.gov.in"),
        _college("Faculty of Music & Fine Arts DU", 2, "New Delhi", "Delhi", 0.1, 2.5, 100, ""),
        _college("Shri Ram Centre for Performing Arts", 3, "New Delhi", "Delhi", 0.3, 2.5, 50, ""),
        _college("Triveni Kala Sangam", 4, "New Delhi", "Delhi", 0.2, 2.0, 50, ""),
        _college("Kathak Kendra", 5, "New Delhi", "Delhi", 0.1, 2.0, 40, ""),
    ],
    "West Bengal": [
        _college("Satyajit Ray Film & TV Institute", 1, "Kolkata", "West Bengal", 0.5, 4.0, 40, ""),
        _college("Shantiniketan (Visva-Bharati)", 2, "Bolpur", "West Bengal", 0.1, 2.0, 200, ""),
        _college("Rabindra Bharati University", 3, "Kolkata", "West Bengal", 0.1, 2.0, 300, ""),
        _college("Government Art College Kolkata", 4, "Kolkata", "West Bengal", 0.1, 1.5, 100, ""),
        _college("ICCR Cultural Centre", 5, "Kolkata", "West Bengal", 0.1, 1.5, 50, ""),
    ],
    "Tamil Nadu": [
        _college("LV Prasad Film & TV Academy", 1, "Chennai", "Tamil Nadu", 2.0, 3.0, 100, ""),
        _college("Government College of Fine Arts Chennai", 2, "Chennai", "Tamil Nadu", 0.1, 2.0, 100, ""),
        _college("Kalakshetra Foundation", 3, "Chennai", "Tamil Nadu", 0.2, 2.0, 80, ""),
        _college("Adyar Music Academy", 4, "Chennai", "Tamil Nadu", 0.1, 1.5, 50, ""),
        _college("Asian College of Journalism", 5, "Chennai", "Tamil Nadu", 2.0, 4.0, 50, ""),
    ],
}

_SPORTS_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Punjab": [
        _college("NIS Patiala", 1, "Patiala", "Punjab", 0.1, 3.0, 150, ""),
        _college("Guru Nanak Dev University", 2, "Amritsar", "Punjab", 0.1, 2.5, 200, ""),
        _college("Punjabi University Patiala", 3, "Patiala", "Punjab", 0.1, 2.0, 200, ""),
        _college("DAV College Chandigarh", 4, "Chandigarh", "Punjab", 0.2, 2.5, 150, ""),
        _college("Khalsa College Amritsar", 5, "Amritsar", "Punjab", 0.1, 2.0, 100, ""),
    ],
    "Madhya Pradesh": [
        _college("LNIPE Gwalior", 1, "Gwalior", "Madhya Pradesh", 0.1, 3.0, 200, ""),
        _college("Barkatullah University (PE)", 2, "Bhopal", "Madhya Pradesh", 0.1, 2.0, 150, ""),
        _college("Jiwaji University (PE)", 3, "Gwalior", "Madhya Pradesh", 0.1, 2.0, 100, ""),
        _college("DAVV Indore (PE)", 4, "Indore", "Madhya Pradesh", 0.1, 2.0, 100, ""),
        _college("Rani Durgavati University", 5, "Jabalpur", "Madhya Pradesh", 0.1, 1.5, 100, ""),
    ],
    "Karnataka": [
        _college("Jain University", 1, "Bangalore", "Karnataka", 1.5, 3.0, 150, ""),
        _college("Symbiosis School of Sports Sciences", 2, "Pune", "Maharashtra", 2.5, 3.5, 60, ""),
        _college("Mangalore University (PE)", 3, "Mangalore", "Karnataka", 0.1, 2.0, 100, ""),
        _college("Bangalore University (PE)", 4, "Bangalore", "Karnataka", 0.2, 2.5, 200, ""),
        _college("Kuvempu University", 5, "Shimoga", "Karnataka", 0.1, 1.5, 100, ""),
    ],
    "Maharashtra": [
        _college("Symbiosis School of Sports Sciences", 1, "Pune", "Maharashtra", 2.5, 3.5, 60, ""),
        _college("Deccan Education Society (PE)", 2, "Pune", "Maharashtra", 0.3, 2.5, 100, ""),
        _college("University of Mumbai (PE)", 3, "Mumbai", "Maharashtra", 0.2, 2.0, 200, ""),
        _college("Shivaji University (PE)", 4, "Kolhapur", "Maharashtra", 0.1, 2.0, 150, ""),
        _college("Tilak Maharashtra Vidyapeeth", 5, "Pune", "Maharashtra", 0.3, 2.0, 100, ""),
    ],
}

_CIVIL_SERVICES_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Delhi": [
        _college("St. Stephen's College DU", 1, "New Delhi", "Delhi", 0.1, 5.0, 400, ""),
        _college("Hindu College DU", 2, "New Delhi", "Delhi", 0.1, 5.0, 400, ""),
        _college("JNU", 3, "New Delhi", "Delhi", 0.1, 5.0, 300, ""),
        _college("Jamia Millia Islamia", 4, "New Delhi", "Delhi", 0.2, 3.5, 400, ""),
        _college("Lady Shri Ram College DU", 5, "New Delhi", "Delhi", 0.1, 4.5, 300, ""),
    ],
    "Uttar Pradesh": [
        _college("BHU", 1, "Varanasi", "Uttar Pradesh", 0.1, 3.0, 1000, ""),
        _college("AMU", 2, "Aligarh", "Uttar Pradesh", 0.1, 3.0, 1000, ""),
        _college("Lucknow University", 3, "Lucknow", "Uttar Pradesh", 0.1, 2.5, 800, ""),
        _college("Allahabad University", 4, "Prayagraj", "Uttar Pradesh", 0.1, 2.5, 600, ""),
        _college("MNNIT (for technical UPSC optional)", 5, "Prayagraj", "Uttar Pradesh", 1.2, 5.0, 800, ""),
    ],
    "Maharashtra": [
        _college("Fergusson College Pune", 1, "Pune", "Maharashtra", 0.1, 3.0, 1200, ""),
        _college("TISS Mumbai", 2, "Mumbai", "Maharashtra", 0.5, 6.0, 200, ""),
        _college("St. Xavier's College Mumbai", 3, "Mumbai", "Maharashtra", 0.5, 4.0, 500, ""),
        _college("Savitribai Phule Pune University", 4, "Pune", "Maharashtra", 0.1, 2.5, 2000, ""),
        _college("Government College of Arts & Science", 5, "Mumbai", "Maharashtra", 0.1, 2.5, 500, ""),
    ],
    "Tamil Nadu": [
        _college("Loyola College Chennai", 1, "Chennai", "Tamil Nadu", 0.2, 3.5, 600, ""),
        _college("Madras Christian College", 2, "Chennai", "Tamil Nadu", 0.2, 3.0, 500, ""),
        _college("Presidency College Chennai", 3, "Chennai", "Tamil Nadu", 0.1, 3.0, 400, ""),
        _college("PSG College Coimbatore", 4, "Coimbatore", "Tamil Nadu", 0.5, 3.0, 400, ""),
        _college("Annamalai University", 5, "Chidambaram", "Tamil Nadu", 0.1, 2.0, 1000, ""),
    ],
}

_HOSPITALITY_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Maharashtra": [
        _college("IHM Mumbai", 1, "Mumbai", "Maharashtra", 1.0, 5.0, 300, ""),
        _college("Welcomgroup WGSHA Manipal (affiliated)", 2, "Mumbai", "Maharashtra", 2.0, 4.0, 100, ""),
        _college("Apeejay Institute of Hospitality", 3, "Navi Mumbai", "Maharashtra", 1.5, 3.0, 100, ""),
        _college("D.Y. Patil (Hospitality)", 4, "Pune", "Maharashtra", 2.0, 3.0, 150, ""),
        _college("Kohinoor IMI (Hotel Management)", 5, "Mumbai", "Maharashtra", 1.5, 3.0, 100, ""),
    ],
    "Delhi": [
        _college("IHM Delhi (Pusa)", 1, "New Delhi", "Delhi", 0.5, 4.5, 300, ""),
        _college("Oberoi STEP", 2, "New Delhi", "Delhi", 0.0, 4.0, 50, ""),
        _college("Amity University (Hospitality)", 3, "Noida", "Delhi", 3.0, 3.0, 200, ""),
        _college("IITTM Delhi", 4, "New Delhi", "Delhi", 0.5, 3.0, 100, ""),
        _college("Banarsidas Chandiwala Institute", 5, "New Delhi", "Delhi", 1.0, 2.5, 100, ""),
    ],
    "Karnataka": [
        _college("IHM Bangalore", 1, "Bangalore", "Karnataka", 0.5, 4.0, 200, ""),
        _college("WGSHA Manipal", 2, "Manipal", "Karnataka", 3.0, 5.0, 150, ""),
        _college("Christ University (Tourism)", 3, "Bangalore", "Karnataka", 1.5, 3.5, 200, ""),
        _college("Acharya Institute of Hotel Management", 4, "Bangalore", "Karnataka", 1.0, 2.5, 100, ""),
        _college("PES University (Hospitality)", 5, "Bangalore", "Karnataka", 1.5, 3.0, 100, ""),
    ],
    "Goa": [
        _college("IHM Goa", 1, "Goa", "Goa", 0.5, 3.5, 150, ""),
        _college("Goa University (Tourism)", 2, "Goa", "Goa", 0.2, 2.5, 100, ""),
        _college("Don Bosco College (Hotel Management)", 3, "Goa", "Goa", 0.8, 2.5, 80, ""),
        _college("Padre Conceicao College", 4, "Goa", "Goa", 0.3, 2.0, 60, ""),
        _college("Fr Agnel College Goa", 5, "Goa", "Goa", 0.5, 2.0, 80, ""),
    ],
}

_AGRICULTURE_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Tamil Nadu": [
        _college("TNAU Coimbatore", 1, "Coimbatore", "Tamil Nadu", 0.2, 4.0, 800, ""),
        _college("Annamalai University (Agri)", 2, "Chidambaram", "Tamil Nadu", 0.2, 2.5, 400, ""),
        _college("AC&RI Madurai", 3, "Madurai", "Tamil Nadu", 0.1, 3.0, 200, ""),
        _college("Pandit Jawaharlal Nehru CAR", 4, "Karaikal", "Tamil Nadu", 0.1, 2.5, 150, ""),
        _college("SRM University (Agri)", 5, "Chennai", "Tamil Nadu", 1.5, 3.0, 100, ""),
    ],
    "Punjab": [
        _college("PAU Ludhiana", 1, "Ludhiana", "Punjab", 0.2, 3.5, 600, ""),
        _college("Guru Angad Dev Veterinary University", 2, "Ludhiana", "Punjab", 0.2, 3.0, 200, ""),
        _college("Lovely Professional University (Agri)", 3, "Phagwara", "Punjab", 1.5, 2.5, 200, ""),
        _college("Khalsa College (Agri)", 4, "Amritsar", "Punjab", 0.1, 2.0, 100, ""),
        _college("CT University (Agri)", 5, "Ludhiana", "Punjab", 1.0, 2.0, 100, ""),
    ],
    "Karnataka": [
        _college("UAS Bangalore", 1, "Bangalore", "Karnataka", 0.2, 3.5, 500, ""),
        _college("UAS Dharwad", 2, "Dharwad", "Karnataka", 0.2, 3.0, 400, ""),
        _college("UAS Raichur", 3, "Raichur", "Karnataka", 0.1, 2.5, 200, ""),
        _college("University of Horticultural Sciences", 4, "Bagalkot", "Karnataka", 0.1, 2.5, 150, ""),
        _college("Keladi Shivappa Nayaka University", 5, "Shimoga", "Karnataka", 0.1, 2.0, 100, ""),
    ],
    "Uttar Pradesh": [
        _college("GB Pant University", 1, "Pantnagar", "Uttarakhand", 0.2, 3.0, 500, ""),
        _college("BHU (Agriculture)", 2, "Varanasi", "Uttar Pradesh", 0.1, 3.0, 300, ""),
        _college("CSAUAT Kanpur", 3, "Kanpur", "Uttar Pradesh", 0.1, 2.5, 300, ""),
        _college("NDUAT Ayodhya", 4, "Ayodhya", "Uttar Pradesh", 0.1, 2.0, 200, ""),
        _college("SVPUAT Meerut", 5, "Meerut", "Uttar Pradesh", 0.1, 2.0, 200, ""),
    ],
}

_DEFENCE_COLLEGES_BY_STATE: dict[str, list[College]] = {
    "Maharashtra": [
        _college("NDA Khadakwasla", 1, "Pune", "Maharashtra", 0.0, 6.0, 320, "https://www.nda.nic.in"),
        _college("Armed Forces Medical College", 2, "Pune", "Maharashtra", 0.1, 12.0, 150, ""),
        _college("College of Military Engineering", 3, "Pune", "Maharashtra", 0.0, 7.0, 100, ""),
        _college("INS Shivaji (Naval Training)", 4, "Lonavala", "Maharashtra", 0.0, 6.0, 100, ""),
        _college("National Defence Academy Museum", 5, "Pune", "Maharashtra", 0.0, 0.0, 0, ""),
    ],
    "Uttarakhand": [
        _college("IMA Dehradun", 1, "Dehradun", "Uttarakhand", 0.0, 6.0, 250, ""),
        _college("Rashtriya Indian Military College", 2, "Dehradun", "Uttarakhand", 0.0, 5.0, 25, ""),
        _college("Indian Military Academy (IMA)", 3, "Dehradun", "Uttarakhand", 0.0, 6.0, 250, ""),
        _college("Forest Research Institute (Defence related)", 4, "Dehradun", "Uttarakhand", 0.1, 4.0, 200, ""),
        _college("Doon School (pre-defence)", 5, "Dehradun", "Uttarakhand", 5.0, 5.0, 50, ""),
    ],
    "Telangana": [
        _college("AFA Dundigal", 1, "Hyderabad", "Telangana", 0.0, 6.0, 150, ""),
        _college("MCEME Secunderabad", 2, "Secunderabad", "Telangana", 0.0, 7.0, 200, ""),
        _college("College of Defence Management", 3, "Secunderabad", "Telangana", 0.0, 8.0, 100, ""),
        _college("Defence Research Lab (DRDO)", 4, "Hyderabad", "Telangana", 0.0, 8.0, 100, ""),
        _college("DRDL Hyderabad", 5, "Hyderabad", "Telangana", 0.0, 8.0, 50, ""),
    ],
    "Tamil Nadu": [
        _college("OTA Chennai", 1, "Chennai", "Tamil Nadu", 0.0, 5.5, 200, ""),
        _college("Naval War College (Wellington)", 2, "Wellington", "Tamil Nadu", 0.0, 6.0, 50, ""),
        _college("DSSC Wellington", 3, "Wellington", "Tamil Nadu", 0.0, 7.0, 100, ""),
        _college("Sainik School Amaravathinagar", 4, "Amaravathinagar", "Tamil Nadu", 0.1, 4.0, 60, ""),
        _college("Madras Regimental Centre", 5, "Wellington", "Tamil Nadu", 0.0, 5.0, 200, ""),
    ],
}

# ═══════════════════════════════════════════════════════════════════════════
# RESERVATION DATA — Central & state-level reservation policies per stream
# ═══════════════════════════════════════════════════════════════════════════

_RESERVATION_DATA: dict[str, dict] = {
    "Engineering & Technology": {
        "summary": "Engineering admissions through JEE and state CETs follow central and state reservation norms. IITs/NITs/IIITs follow the central policy; state engineering colleges follow their respective state policies.",
        "central_reservation": [
            {"category": "SC (Scheduled Caste)", "percentage": "15%", "applicable_to": "IITs, NITs, IIITs, Central Universities", "details": "Based on Constitution (1st Amendment) Act, 1951"},
            {"category": "ST (Scheduled Tribe)", "percentage": "7.5%", "applicable_to": "IITs, NITs, IIITs, Central Universities", "details": "Based on Constitution (1st Amendment) Act, 1951"},
            {"category": "OBC-NCL (Other Backward Classes – Non-Creamy Layer)", "percentage": "27%", "applicable_to": "IITs, NITs, IIITs, Central Universities", "details": "Based on Central Educational Institutions Act, 2006"},
            {"category": "EWS (Economically Weaker Section)", "percentage": "10%", "applicable_to": "IITs, NITs, IIITs, Central Universities", "details": "103rd Constitutional Amendment, 2019. Family income < ₹8 LPA"},
            {"category": "PwD (Persons with Disability)", "percentage": "5%", "applicable_to": "Horizontal reservation across all categories", "details": "Rights of Persons with Disabilities Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "JEE Main / JEE Advanced", "policy": "Central reservation norms (SC 15%, ST 7.5%, OBC-NCL 27%, EWS 10%)", "notes": "Separate rank lists for each category; relaxed cutoff scores"},
            {"exam": "State CETs (MHT CET, KCET, EAMCET, etc.)", "policy": "State-specific reservation norms apply", "notes": "Varies by state; some states have higher OBC/SC/ST percentages"},
        ],
        "important_notes": [
            "Central institutions (IITs/NITs) follow uniform central reservation policy",
            "State-level colleges follow state-specific reservation policies which may differ significantly",
            "Creamy layer limit for OBC: ₹8 LPA family income",
            "EWS certificate required from district magistrate; family income must be < ₹8 LPA",
            "Supernumerary seats available for female candidates at IITs (20% additional seats)",
        ],
    },
    "Medical & Healthcare": {
        "summary": "Medical admissions via NEET follow central reservation for AIIMS/JIPMER/central colleges and state reservation norms for state medical colleges. The All India Quota (15%) follows central norms while state quotas (85%) follow respective state policies.",
        "central_reservation": [
            {"category": "SC (Scheduled Caste)", "percentage": "15%", "applicable_to": "AIIMS, JIPMER, Central Quota (15% AIQ)", "details": "All India Quota seats in government medical colleges"},
            {"category": "ST (Scheduled Tribe)", "percentage": "7.5%", "applicable_to": "AIIMS, JIPMER, Central Quota (15% AIQ)", "details": "All India Quota seats in government medical colleges"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "AIIMS, JIPMER, Central Quota (15% AIQ)", "details": "Implemented in AIQ from 2007; Supreme Court upheld in 2008"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "AIIMS, JIPMER, Central Quota (15% AIQ)", "details": "Applicable from 2019-20 academic session onwards"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation across all categories", "details": "Benchmark disabilities as per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "NEET UG", "policy": "15% AIQ: Central reservation; 85% State Quota: State reservation norms", "notes": "State quota seats follow individual state reservation policies"},
            {"exam": "NEET PG", "policy": "Central reservation norms for AIQ; state norms for state seats", "notes": "50% AIQ seats in PG follow central reservation"},
        ],
        "important_notes": [
            "All India Quota (15% UG, 50% PG) follows central reservation policy",
            "State Quota (85% UG, 50% PG) follows respective state reservation policies",
            "Some states like Tamil Nadu have up to 69% reservation in state quota",
            "Domicile certificate required for state quota seats",
            "OBC/SC/ST candidates get fee concessions at most government medical colleges",
        ],
    },
    "Law & Legal Studies": {
        "summary": "Law admissions through CLAT and university-level exams follow reservation norms. National Law Universities (NLUs) follow central reservation; state law colleges follow state policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "NLUs, Central Universities", "details": "Applied through CLAT counselling"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "NLUs, Central Universities", "details": "Applied through CLAT counselling"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "NLUs, Central Universities", "details": "Most NLUs follow central norms; a few follow state norms"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "NLUs, Central Universities", "details": "Implemented from 2020 onwards in most NLUs"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation at NLUs", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "CLAT", "policy": "Central reservation norms for NLUs", "notes": "Separate merit lists and cutoffs for reserved categories"},
            {"exam": "AILET (NLU Delhi)", "policy": "Central reservation norms", "notes": "NLU Delhi conducts its own entrance exam"},
        ],
        "important_notes": [
            "NLUs established by state acts may follow state reservation in some seats",
            "NLSIU Bangalore follows Karnataka state reservation for a portion of seats",
            "Some NLUs have additional reservations for Kashmiri migrants, wards of defence personnel",
            "Fee waivers available for SC/ST students at most NLUs",
        ],
    },
    "Science & Research": {
        "summary": "Science and research admissions through KVPY, NEST, IISER aptitude tests follow central reservation. IISc and IISERs follow central norms; state universities follow state policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "IISc, IISERs, Central Universities", "details": "Applied through entrance exam counselling"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "IISc, IISERs, Central Universities", "details": "Applied through entrance exam counselling"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "IISc, IISERs, Central Universities", "details": "Central reservation norms"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "IISc, IISERs, Central Universities", "details": "103rd Amendment applicable"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "KVPY / INSPIRE", "policy": "Central reservation norms", "notes": "Fellowship amounts same across categories"},
            {"exam": "NEST (NISER/CEBS)", "policy": "Central reservation norms", "notes": "Separate cutoffs for reserved categories"},
        ],
        "important_notes": [
            "CSIR/UGC fellowships follow central reservation for PhD admissions",
            "INSPIRE Fellowship by DST has no category-based reservation but encourages diversity",
            "IISERs provide full tuition fee waiver for SC/ST candidates",
            "Research fellowships (JRF/SRF) follow central reservation in selection",
        ],
    },
    "Education & Teaching": {
        "summary": "Education and teaching admissions follow central reservation for central universities and CTET. State-level TET and B.Ed admissions follow respective state policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "Central Universities, KVS, NVS", "details": "B.Ed admissions and teacher recruitment"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "Central Universities, KVS, NVS", "details": "B.Ed admissions and teacher recruitment"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "Central Universities, KVS, NVS", "details": "B.Ed admissions and teacher recruitment"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "Central Universities, KVS, NVS", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "Includes visual, hearing, locomotor, and intellectual disabilities"},
        ],
        "key_exams_reservation": [
            {"exam": "CTET", "policy": "Qualification exam — no reservation in exam, but reservation in recruitment", "notes": "Relaxed qualifying marks for SC/ST: 55% vs 60%"},
            {"exam": "State TET", "policy": "State-specific reservation in teacher recruitment", "notes": "Varies by state"},
        ],
        "important_notes": [
            "Teacher recruitment follows roster system with point-based reservation",
            "KVS and NVS recruitment follows central government reservation norms",
            "State teacher recruitment follows state-specific policies",
            "Many states provide relaxed age limits for SC/ST/OBC candidates (3-5 years relaxation)",
        ],
    },
    "Commerce, Finance & Business": {
        "summary": "Commerce and business admissions through CUET, CA Foundation, and MBA exams follow central reservation for central institutions. Professional bodies like ICAI (CA) have no category reservation in exams but follow norms for articleship placements.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "IIMs, Central Universities, DU colleges", "details": "Applicable through CUET/CAT counselling"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "IIMs, Central Universities, DU colleges", "details": "Applicable through CUET/CAT counselling"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "IIMs, Central Universities, DU colleges", "details": "Applicable through CUET/CAT counselling"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "IIMs, Central Universities, DU colleges", "details": "Implemented from 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "Applicable at IIMs and central institutions"},
        ],
        "key_exams_reservation": [
            {"exam": "CA Foundation / Intermediate / Final", "policy": "No category reservation in ICAI exams — merit-based", "notes": "However, ICAI offers fee concessions and scholarships for SC/ST students"},
            {"exam": "CAT (IIMs)", "policy": "Central reservation norms at IIMs", "notes": "Relaxed cutoff scores for reserved categories"},
        ],
        "important_notes": [
            "ICAI, ICSI, and ICMAI exams are purely merit-based with no reservation",
            "CA/CS/CMA professional bodies offer financial assistance to SC/ST candidates",
            "IIM admissions follow central reservation with separate shortlisting criteria",
            "State commerce colleges follow respective state reservation policies",
        ],
    },
    "Arts & Humanities": {
        "summary": "Arts and humanities admissions through CUET and university-level exams follow central reservation for central universities. UPSC Civil Services follows the most comprehensive reservation policy.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "Central Universities, UPSC", "details": "DU, JNU, BHU, etc."},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "Central Universities, UPSC", "details": "DU, JNU, BHU, etc."},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "Central Universities, UPSC", "details": "DU, JNU, BHU, etc."},
            {"category": "EWS", "percentage": "10%", "applicable_to": "Central Universities, UPSC", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "UPSC CSE", "policy": "SC 15%, ST 7.5%, OBC 27%, EWS 10%; age relaxation SC/ST +5 yrs, OBC +3 yrs", "notes": "Unlimited attempts for SC/ST (till age limit); 9 for OBC"},
            {"exam": "CUET", "policy": "Central reservation for central university admissions", "notes": "Separate cutoffs per category"},
        ],
        "important_notes": [
            "UPSC provides maximum age relaxation: SC/ST get 5 years, OBC 3 years extra",
            "SC/ST candidates get unlimited UPSC attempts until upper age limit",
            "Fee waivers for SC/ST candidates in UPSC and most entrance exams",
            "JNU, BHU, AMU have additional internal reservation policies (deprivation points at JNU)",
        ],
    },
    "Design & Creative Arts": {
        "summary": "Design admissions through UCEED, NID DAT, and NIFT entrance follow central reservation. NIDs and NIFTs being centrally funded follow central norms.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "NID, NIFT, IIT Design (IDC)", "details": "Applied through entrance exam counselling"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "NID, NIFT, IIT Design (IDC)", "details": "Applied through entrance exam counselling"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "NID, NIFT, IIT Design (IDC)", "details": "Applied through entrance exam counselling"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "NID, NIFT, IIT Design (IDC)", "details": "Implemented from 2020"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "UCEED (IIT Design)", "policy": "Central reservation norms", "notes": "Same policy as JEE Advanced"},
            {"exam": "NID DAT / NIFT Entrance", "policy": "Central reservation norms", "notes": "Separate merit lists for reserved categories"},
        ],
        "important_notes": [
            "NID offers full fee waiver for SC/ST and economically disadvantaged students",
            "NIFT provides fee concession and hostel subsidy for SC/ST students",
            "Private design colleges (Srishti, Pearl Academy) may not follow reservation",
            "Portfolio/studio tests are common — category relaxation mainly in entrance exam cutoffs",
        ],
    },
    "Performing & Fine Arts": {
        "summary": "Performing arts admissions through institution-specific auditions and entrance tests follow reservation norms at central institutions (FTII, NSD, Satyajit Ray). State arts universities follow state policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "FTII, NSD, SRFTI, Central Universities", "details": "Applied during admissions"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "FTII, NSD, SRFTI, Central Universities", "details": "Applied during admissions"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "FTII, NSD, SRFTI, Central Universities", "details": "Applied during admissions"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "FTII, NSD, SRFTI, Central Universities", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "FTII Entrance (JET)", "policy": "Central reservation norms", "notes": "Audition/interview rounds for all candidates; cutoff relaxation for reserved categories"},
            {"exam": "NSD Entrance", "policy": "Central reservation norms", "notes": "Workshop-based selection; reservation applied at admission stage"},
        ],
        "important_notes": [
            "Talent/audition is the primary selection criterion — reservation applies to cutoff scores",
            "FTII offers full tuition fee waiver and stipend for SC/ST students",
            "NSD provides hostel and mess fee waiver for economically weaker students",
            "Many performing arts institutions have a small intake (15-30 students), making reserved seats limited",
        ],
    },
    "Sports & Physical Education": {
        "summary": "Sports admissions follow a dual policy — sports quota (supernumerary) and regular reservation. Central sports bodies (SAI, LNIPE) follow central norms; state sports colleges follow state policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "SAI, LNIPE, Central Universities", "details": "Sports + academic admissions"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "SAI, LNIPE, Central Universities", "details": "Sports + academic admissions"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "SAI, LNIPE, Central Universities", "details": "Sports + academic admissions"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "SAI, LNIPE, Central Universities", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation (Para-sports emphasis)", "details": "Para-sports athletes get additional support"},
        ],
        "key_exams_reservation": [
            {"exam": "SAI Selection Trials", "policy": "Central reservation norms + sports merit", "notes": "Performance in trials is primary; reservation in final selection"},
            {"exam": "BPEd / MPEd Entrance", "policy": "Central/state reservation norms", "notes": "Physical fitness tests mandatory for all categories"},
        ],
        "important_notes": [
            "Sports quota admissions are supernumerary (5% in most central universities)",
            "Khelo India scholarship provides ₹5-6 lakh/year — no category restriction but reserved category candidates prioritized",
            "SAI Training Centres provide free training, boarding, and equipment for talented athletes",
            "Para-sports athletes eligible for additional government funding and training support",
        ],
    },
    "Civil Services & Government Services": {
        "summary": "Government services follow the most comprehensive reservation policy in India. UPSC, SSC, Banking, Railways — all follow central reservation. State services follow respective state policies which may have higher reservation percentages.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "UPSC, SSC, Banking, Railways, PSUs", "details": "All central government services"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "UPSC, SSC, Banking, Railways, PSUs", "details": "All central government services"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "UPSC, SSC, Banking, Railways, PSUs", "details": "All central government services"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "UPSC, SSC, Banking, Railways, PSUs", "details": "Since 2019; family income < ₹8 LPA"},
            {"category": "PwD", "percentage": "4%", "applicable_to": "Horizontal reservation across all categories", "details": "Increased from 3% to 4% under RPwD Act, 2016"},
            {"category": "Ex-Servicemen", "percentage": "10%", "applicable_to": "Group C & D posts (SSC, Railways)", "details": "Not applicable to Group A & B services like IAS/IPS"},
        ],
        "key_exams_reservation": [
            {"exam": "UPSC CSE (IAS/IPS/IFS)", "policy": "SC 15%, ST 7.5%, OBC 27%, EWS 10%; age relaxation: SC/ST +5, OBC +3 yrs", "notes": "SC/ST: unlimited attempts; OBC: 9 attempts; General/EWS: 6 attempts"},
            {"exam": "SSC CGL / CHSL", "policy": "Central reservation norms + ex-servicemen 10%", "notes": "Age relaxation and fee waivers for reserved categories"},
            {"exam": "IBPS PO / Clerk", "policy": "Central reservation norms", "notes": "Relaxed qualifying marks and age for reserved categories"},
        ],
        "important_notes": [
            "UPSC CSE: SC/ST get unlimited attempts (till age limit 37); OBC gets 9 attempts (till 38); General/EWS 6 (till 32)",
            "Exam fee waiver for SC/ST/PwD and female candidates in most central exams",
            "Carry-forward of unfilled reserved vacancies to subsequent recruitment cycles",
            "State PCS exams may have different (often higher) reservation percentages — check state policy",
            "Roster system ensures proportional representation across all levels",
        ],
    },
    "Hospitality, Travel & Tourism": {
        "summary": "Hospitality admissions through NCHMCT JEE follow central reservation for IHMs (central). State IHMs and private colleges follow their own policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "Central IHMs (NCHMCT)", "details": "IHM Mumbai, Delhi, Hyderabad, etc."},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "Central IHMs (NCHMCT)", "details": "IHM Mumbai, Delhi, Hyderabad, etc."},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "Central IHMs (NCHMCT)", "details": "IHM Mumbai, Delhi, Hyderabad, etc."},
            {"category": "EWS", "percentage": "10%", "applicable_to": "Central IHMs (NCHMCT)", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "NCHMCT JEE", "policy": "Central reservation norms", "notes": "Separate rank lists for each category"},
        ],
        "important_notes": [
            "21 central IHMs follow central reservation; state IHMs follow state policies",
            "SC/ST candidates get fee waiver at central IHMs",
            "Private hospitality colleges (Oberoi, Taj, Welcome) do not follow reservation but offer scholarships",
            "Industry placements are merit-based regardless of admission category",
        ],
    },
    "Agriculture & Environmental Studies": {
        "summary": "Agricultural university admissions through ICAR AIEEA follow central reservation for deemed universities. State agricultural universities follow state reservation policies.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "ICAR Deemed Universities, Central Agriculture Universities", "details": "IARI, NDRI, IVRI, etc."},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "ICAR Deemed Universities, Central Agriculture Universities", "details": "IARI, NDRI, IVRI, etc."},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "ICAR Deemed Universities, Central Agriculture Universities", "details": "IARI, NDRI, IVRI, etc."},
            {"category": "EWS", "percentage": "10%", "applicable_to": "ICAR Deemed Universities", "details": "Since 2019"},
            {"category": "PwD", "percentage": "5%", "applicable_to": "Horizontal reservation", "details": "As per RPwD Act, 2016"},
        ],
        "key_exams_reservation": [
            {"exam": "ICAR AIEEA (UG/PG)", "policy": "Central reservation norms for ICAR seats", "notes": "15% All India seats + ICAR deemed university seats"},
            {"exam": "State agriculture entrance", "policy": "State reservation norms", "notes": "85% state quota seats follow state policies"},
        ],
        "important_notes": [
            "State agricultural universities have 85% state quota with state reservation",
            "ICAR provides scholarships (₹1,000-3,000/month) with priority to SC/ST/OBC students",
            "Tribal sub-plan seats available at several state agriculture universities",
            "KVK (Krishi Vigyan Kendra) training programs have reserved slots for tribal farmers",
        ],
    },
    "Defence Research": {
        "summary": "Defence admissions through NDA, CDS, and AFCAT follow UPSC reservation norms for officer cadre. DRDO recruitment follows central reservation. Jawans/other ranks follow state-wise roster.",
        "central_reservation": [
            {"category": "SC", "percentage": "15%", "applicable_to": "DRDO, DPSU recruitment", "details": "Officer-level technical positions at DRDO/HAL/BEL"},
            {"category": "ST", "percentage": "7.5%", "applicable_to": "DRDO, DPSU recruitment", "details": "Officer-level technical positions at DRDO/HAL/BEL"},
            {"category": "OBC-NCL", "percentage": "27%", "applicable_to": "DRDO, DPSU recruitment", "details": "Officer-level technical positions at DRDO/HAL/BEL"},
            {"category": "EWS", "percentage": "10%", "applicable_to": "DRDO, DPSU recruitment", "details": "Since 2019"},
            {"category": "PwD", "percentage": "4%", "applicable_to": "DRDO civilian positions only", "details": "Not applicable to armed forces combatant roles"},
        ],
        "key_exams_reservation": [
            {"exam": "NDA / CDS (UPSC)", "policy": "No reservation for officer cadre in Armed Forces", "notes": "Armed Forces officer entry is purely merit-based; no caste reservation"},
            {"exam": "DRDO SET / RAC", "policy": "Central reservation norms (SC 15%, ST 7.5%, OBC 27%)", "notes": "Scientist positions at DRDO follow full central reservation"},
            {"exam": "AFCAT", "policy": "No reservation for IAF officer entry", "notes": "Air Force officer selection is merit + medical fitness based"},
        ],
        "important_notes": [
            "Armed Forces officer cadre (Army/Navy/Air Force) does NOT follow caste-based reservation",
            "Jawan/other ranks recruitment follows state-wise roster and reservation",
            "DRDO, BEL, HAL, BDL and other DPSUs follow full central reservation in recruitment",
            "Sainik Schools follow central reservation for admissions",
            "Agnipath scheme (Agniveer) follows state-wise, category-wise reservation for recruitment",
        ],
    },
}

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
        "scholarships": _SCHOLARSHIP_DATA["Engineering & Technology"],
        "ai_impact": _AI_IMPACT_DATA["Engineering & Technology"],
        "reservation": _RESERVATION_DATA["Engineering & Technology"],
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
        "scholarships": _SCHOLARSHIP_DATA["Medical & Healthcare"],
        "ai_impact": _AI_IMPACT_DATA["Medical & Healthcare"],
        "reservation": _RESERVATION_DATA["Medical & Healthcare"],
    },
    "Law & Legal Studies": {
        "colleges_india": _LAW_COLLEGES_INDIA,
        "colleges_by_state": _LAW_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Law & Legal Studies"],
        "ai_impact": _AI_IMPACT_DATA["Law & Legal Studies"],
        "reservation": _RESERVATION_DATA["Law & Legal Studies"],
    },
    "Science & Research": {
        "colleges_india": _SCIENCE_COLLEGES_INDIA,
        "colleges_by_state": _SCIENCE_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Science & Research"],
        "ai_impact": _AI_IMPACT_DATA["Science & Research"],
        "reservation": _RESERVATION_DATA["Science & Research"],
    },
    "Education & Teaching": {
        "colleges_india": _EDUCATION_COLLEGES_INDIA,
        "colleges_by_state": _EDUCATION_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Education & Teaching"],
        "ai_impact": _AI_IMPACT_DATA["Education & Teaching"],
        "reservation": _RESERVATION_DATA["Education & Teaching"],
    },
    "Commerce, Finance & Business": {
        "colleges_india": _COMMERCE_COLLEGES_INDIA,
        "colleges_by_state": _COMMERCE_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Commerce, Finance & Business"],
        "ai_impact": _AI_IMPACT_DATA["Commerce, Finance & Business"],
        "reservation": _RESERVATION_DATA["Commerce, Finance & Business"],
    },
    "Arts & Humanities": {
        "colleges_india": _ARTS_COLLEGES_INDIA,
        "colleges_by_state": _ARTS_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Arts & Humanities"],
        "ai_impact": _AI_IMPACT_DATA["Arts & Humanities"],
        "reservation": _RESERVATION_DATA["Arts & Humanities"],
    },
    "Design & Creative Arts": {
        "colleges_india": _DESIGN_COLLEGES_INDIA,
        "colleges_by_state": _DESIGN_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Design & Creative Arts"],
        "ai_impact": _AI_IMPACT_DATA["Design & Creative Arts"],
        "reservation": _RESERVATION_DATA["Design & Creative Arts"],
    },
    "Performing & Fine Arts": {
        "colleges_india": _PERFORMING_ARTS_COLLEGES_INDIA,
        "colleges_by_state": _PERFORMING_ARTS_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Performing & Fine Arts"],
        "ai_impact": _AI_IMPACT_DATA["Performing & Fine Arts"],
        "reservation": _RESERVATION_DATA["Performing & Fine Arts"],
    },
    "Sports & Physical Education": {
        "colleges_india": _SPORTS_COLLEGES_INDIA,
        "colleges_by_state": _SPORTS_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Sports & Physical Education"],
        "ai_impact": _AI_IMPACT_DATA["Sports & Physical Education"],
        "reservation": _RESERVATION_DATA["Sports & Physical Education"],
    },
    "Civil Services & Government Services": {
        "colleges_india": _CIVIL_SERVICES_COLLEGES_INDIA,
        "colleges_by_state": _CIVIL_SERVICES_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Civil Services & Government Services"],
        "ai_impact": _AI_IMPACT_DATA["Civil Services & Government Services"],
        "reservation": _RESERVATION_DATA["Civil Services & Government Services"],
    },
    "Hospitality, Travel & Tourism": {
        "colleges_india": _HOSPITALITY_COLLEGES_INDIA,
        "colleges_by_state": _HOSPITALITY_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Hospitality, Travel & Tourism"],
        "ai_impact": _AI_IMPACT_DATA["Hospitality, Travel & Tourism"],
        "reservation": _RESERVATION_DATA["Hospitality, Travel & Tourism"],
    },
    "Agriculture & Environmental Studies": {
        "colleges_india": _AGRICULTURE_COLLEGES_INDIA,
        "colleges_by_state": _AGRICULTURE_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Agriculture & Environmental Studies"],
        "ai_impact": _AI_IMPACT_DATA["Agriculture & Environmental Studies"],
        "reservation": _RESERVATION_DATA["Agriculture & Environmental Studies"],
    },
    "Defence Research": {
        "colleges_india": _DEFENCE_COLLEGES_INDIA,
        "colleges_by_state": _DEFENCE_COLLEGES_BY_STATE,
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
        "scholarships": _SCHOLARSHIP_DATA["Defence Research"],
        "ai_impact": _AI_IMPACT_DATA["Defence Research"],
        "reservation": _RESERVATION_DATA["Defence Research"],
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
