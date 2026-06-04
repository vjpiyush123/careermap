"""Comprehensive college directory data — Engineering & Medical.

Compact static data with branch-level details, cutoffs, and placements.
Phase 1: Engineering Top 25.  Phase 2: Medical Top 25.
"""

from __future__ import annotations

from careerguide.models.career import Branch, College, CourseType


# ── Helpers ────────────────────────────────────────────────────────────────

def _b(name: str, short: str, ug: int = 0, pg: int = 0, dual: int = 0,
       exam: str = "", gen_c: int = 0, obc_c: int = 0, sc_c: int = 0,
       st_c: int = 0, ews_c: int = 0, fem_c: int = 0,
       avg_p: float = 0, med_p: float = 0, high_p: float = 0,
       pct: float = 0, specs: list[str] | None = None) -> Branch:
    return Branch(
        name=name, short_name=short, ug_seats=ug, pg_seats=pg,
        dual_degree_seats=dual, cutoff_exam=exam,
        general_closing_rank=gen_c, obc_closing_rank=obc_c,
        sc_closing_rank=sc_c, st_closing_rank=st_c,
        ews_closing_rank=ews_c, female_closing_rank=fem_c,
        avg_placement_lpa=avg_p, median_placement_lpa=med_p,
        highest_placement_lpa=high_p, placement_percentage=pct,
        specializations=specs or [],
    )


def _ct(name: str, dur: float, exam: str = "", elig: str = "",
        seats: int = 0, fee: float = 0, branches: list[str] | None = None) -> CourseType:
    return CourseType(
        name=name, duration_years=dur, entrance_exam=exam,
        eligibility=elig, total_seats=seats, fee_per_year_lpa=fee,
        available_branches=branches or [],
    )


# ── Standard course-type sets ─────────────────────────────────────────────

_IIT_COURSES = [
    _ct("B.Tech", 4, "JEE Advanced", "10+2 PCM, 75%", 0, 2.5),
    _ct("Dual Degree (B.Tech+M.Tech)", 5, "JEE Advanced", "10+2 PCM, 75%", 0, 2.5),
    _ct("M.Tech", 2, "GATE", "B.Tech/BE with valid GATE", 0, 0.35),
    _ct("MS by Research", 2.5, "GATE", "B.Tech/BE", 0, 0.35),
    _ct("PhD", 4, "GATE/UGC-NET", "M.Tech/MS or B.Tech with GATE", 0, 0.35),
]

_NIT_COURSES = [
    _ct("B.Tech", 4, "JEE Main", "10+2 PCM, 75%", 0, 1.5),
    _ct("M.Tech", 2, "GATE", "B.Tech/BE with valid GATE", 0, 0.30),
    _ct("PhD", 4, "GATE/UGC-NET", "M.Tech/MS", 0, 0.30),
]

_PRIVATE_COURSES = [
    _ct("B.Tech", 4, "JEE Main / Institute Exam", "10+2 PCM, 75%", 0, 4.0),
    _ct("M.Tech", 2, "GATE / Institute Exam", "B.Tech/BE", 0, 2.5),
]

_IIIT_COURSES = [
    _ct("B.Tech", 4, "JEE Main / IIIT Entrance", "10+2 PCM, 75%", 0, 2.0),
    _ct("M.Tech", 2, "GATE", "B.Tech/BE with valid GATE", 0, 0.50),
    _ct("PhD", 4, "GATE/UGC-NET", "M.Tech/MS", 0, 0.30),
]

_IIIT_PPP_COURSES = [
    _ct("B.Tech", 4, "JEE Main", "10+2 PCM, 75%", 0, 2.5),
    _ct("M.Tech", 2, "GATE", "B.Tech/BE with valid GATE", 0, 0.60),
]


# ═══════════════════════════════════════════════════════════════════════════
# ENGINEERING — TOP 25 INDIA
# ═══════════════════════════════════════════════════════════════════════════

_ENGINEERING_DIRECTORY: list[College] = [
    # ── 1. IIT Bombay ──────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Bombay",
        short_name="IIT Bombay", institute_type="IIT", established=1958,
        ranking=1, city="Mumbai", state="Maharashtra",
        nirf_ranking=3, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.25,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=21.0, median_placement_lpa=18.0,
        highest_placement_lpa=310.0, placement_percentage=95.0,
        top_recruiters=["Google", "Microsoft", "Goldman Sachs", "Apple", "Uber"],
        total_seats=1200, website="https://www.iitb.ac.in",
        notable_alumni=["Nandan Nilekani", "Raghuram Rajan"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 110, 60, 20, "JEE Advanced",
               66, 95, 350, 138, 85, 155,
               32.0, 28.0, 310.0, 100, ["AI/ML", "Systems", "Theory"]),
            _b("Electrical Engineering", "EE", 140, 80, 15, "JEE Advanced",
               170, 260, 920, 450, 220, 410,
               24.0, 20.0, 120.0, 97, ["VLSI", "Power", "Signal Processing"]),
            _b("Mechanical Engineering", "ME", 180, 70, 10, "JEE Advanced",
               680, 950, 2800, 1400, 850, 1200,
               18.0, 15.0, 80.0, 92, ["Design", "Thermal", "Manufacturing"]),
            _b("Civil Engineering", "CE", 80, 50, 5, "JEE Advanced",
               1800, 2500, 5500, 3000, 2200, 3200,
               14.0, 12.0, 45.0, 88, ["Structural", "Geotech", "Transportation"]),
            _b("Chemical Engineering", "CH", 100, 40, 5, "JEE Advanced",
               900, 1300, 3800, 2000, 1100, 1800,
               16.0, 14.0, 55.0, 90, ["Process", "Polymers", "Biotech"]),
            _b("Aerospace Engineering", "AE", 60, 30, 5, "JEE Advanced",
               550, 780, 2200, 1100, 680, 1050,
               18.0, 16.0, 65.0, 93, ["Aerodynamics", "Propulsion", "Structures"]),
            _b("Engineering Physics", "EP", 40, 0, 0, "JEE Advanced",
               850, 1200, 3500, 1800, 1050, 1600,
               20.0, 17.0, 90.0, 91, ["Photonics", "Nano", "Quantum"]),
            _b("Metallurgical & Materials", "MME", 70, 30, 5, "JEE Advanced",
               2400, 3200, 6500, 3800, 2800, 4200,
               14.0, 12.0, 40.0, 85, ["Ceramics", "Composites", "Corrosion"]),
        ],
    ),

    # ── 2. IIT Delhi ───────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Delhi",
        short_name="IIT Delhi", institute_type="IIT", established=1961,
        ranking=2, city="New Delhi", state="Delhi",
        nirf_ranking=2, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.20,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=20.0, median_placement_lpa=17.5,
        highest_placement_lpa=280.0, placement_percentage=94.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Samsung", "JP Morgan"],
        total_seats=1100, website="https://home.iitd.ac.in",
        notable_alumni=["Sundar Pichai (partial)", "Rajeev Suri"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 75, 55, 15, "JEE Advanced",
               62, 88, 320, 130, 80, 145,
               30.0, 26.0, 280.0, 100, ["AI/ML", "Data Science", "Security"]),
            _b("Electrical Engineering", "EE", 130, 75, 10, "JEE Advanced",
               165, 250, 880, 430, 210, 400,
               23.0, 19.0, 110.0, 96, ["Power Systems", "Communications", "VLSI"]),
            _b("Mechanical Engineering", "ME", 160, 65, 10, "JEE Advanced",
               650, 900, 2600, 1350, 800, 1150,
               17.5, 14.5, 75.0, 91, ["Robotics", "Thermal", "Design"]),
            _b("Civil Engineering", "CE", 70, 45, 5, "JEE Advanced",
               1700, 2400, 5200, 2800, 2100, 3000,
               13.5, 11.5, 42.0, 87, ["Structural", "Environmental", "Geotech"]),
            _b("Textile Technology", "TT", 50, 25, 3, "JEE Advanced",
               5500, 7200, 12000, 8000, 6500, 9000,
               10.0, 8.5, 25.0, 80, ["Technical Textiles", "Fashion Tech"]),
        ],
    ),

    # ── 3. IIT Madras ──────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Madras",
        short_name="IIT Madras", institute_type="IIT", established=1959,
        ranking=3, city="Chennai", state="Tamil Nadu",
        nirf_ranking=1, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.22,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=19.5, median_placement_lpa=17.0,
        highest_placement_lpa=250.0, placement_percentage=95.0,
        top_recruiters=["Google", "Microsoft", "Intel", "Qualcomm", "DE Shaw"],
        total_seats=1050, website="https://www.iitm.ac.in",
        notable_alumni=["Raghunath Mashelkar", "S. Ramadorai"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 85, 50, 18, "JEE Advanced",
               70, 100, 370, 150, 90, 165,
               30.0, 26.0, 250.0, 100, ["AI/ML", "Theoretical CS", "Systems"]),
            _b("Electrical Engineering", "EE", 135, 70, 12, "JEE Advanced",
               180, 275, 950, 470, 230, 420,
               22.0, 18.0, 100.0, 96, ["VLSI", "Control", "Power"]),
            _b("Mechanical Engineering", "ME", 170, 60, 8, "JEE Advanced",
               700, 980, 2900, 1450, 870, 1250,
               17.0, 14.0, 70.0, 92, ["Thermal", "Design", "Manufacturing"]),
            _b("Civil Engineering", "CE", 75, 40, 5, "JEE Advanced",
               1850, 2600, 5600, 3100, 2250, 3300,
               13.0, 11.0, 40.0, 86, ["Structural", "Water Resources", "Geotech"]),
            _b("Engineering Physics", "EP", 35, 0, 0, "JEE Advanced",
               900, 1250, 3600, 1900, 1100, 1650,
               19.0, 16.0, 85.0, 90, ["Photonics", "Nano", "Quantum Computing"]),
        ],
    ),

    # ── 4. IIT Kanpur ──────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Kanpur",
        short_name="IIT Kanpur", institute_type="IIT", established=1959,
        ranking=4, city="Kanpur", state="Uttar Pradesh",
        nirf_ranking=4, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.22,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=18.0, median_placement_lpa=15.5,
        highest_placement_lpa=220.0, placement_percentage=92.0,
        top_recruiters=["Google", "Microsoft", "Goldman Sachs", "Flipkart", "Uber"],
        total_seats=1000, website="https://www.iitk.ac.in",
        notable_alumni=["N. R. Narayana Murthy", "Manindra Agrawal"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 50, 15, "JEE Advanced",
               80, 115, 400, 165, 100, 180,
               28.0, 24.0, 220.0, 100, ["AI/ML", "Algorithms", "Systems"]),
            _b("Electrical Engineering", "EE", 130, 65, 10, "JEE Advanced",
               200, 300, 1000, 500, 250, 450,
               21.0, 17.0, 95.0, 94, ["Signal Processing", "Power", "Communications"]),
            _b("Mechanical Engineering", "ME", 150, 55, 8, "JEE Advanced",
               750, 1050, 3000, 1550, 920, 1300,
               16.0, 13.5, 65.0, 90, ["Design", "Thermal", "Fluids"]),
            _b("Aerospace Engineering", "AE", 50, 25, 5, "JEE Advanced",
               600, 850, 2400, 1200, 730, 1100,
               17.5, 15.0, 60.0, 91, ["Flight Mechanics", "Propulsion", "Structures"]),
        ],
    ),

    # ── 5. IIT Kharagpur ───────────────────────────────────────────
    College(
        name="Indian Institute of Technology Kharagpur",
        short_name="IIT Kharagpur", institute_type="IIT", established=1951,
        ranking=5, city="Kharagpur", state="West Bengal",
        nirf_ranking=5, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=17.5, median_placement_lpa=15.0,
        highest_placement_lpa=200.0, placement_percentage=93.0,
        top_recruiters=["Google", "Amazon", "TCS", "Infosys", "JP Morgan"],
        total_seats=1500, website="https://www.iitkgp.ac.in",
        notable_alumni=["Sundar Pichai", "Vinod Gupta"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 90, 55, 18, "JEE Advanced",
               85, 120, 420, 170, 105, 190,
               27.0, 23.0, 200.0, 99, ["AI/ML", "Software Engg", "Networks"]),
            _b("Electrical Engineering", "EE", 140, 70, 10, "JEE Advanced",
               210, 320, 1050, 520, 260, 470,
               20.0, 16.5, 90.0, 93, ["Power", "Electronics", "Control"]),
            _b("Mechanical Engineering", "ME", 180, 65, 8, "JEE Advanced",
               780, 1100, 3100, 1600, 950, 1350,
               15.5, 13.0, 62.0, 90, ["Manufacturing", "Thermal", "Design"]),
            _b("Civil Engineering", "CE", 85, 45, 5, "JEE Advanced",
               1900, 2700, 5800, 3200, 2300, 3400,
               12.5, 10.5, 38.0, 85, ["Structural", "Geotech", "Water"]),
            _b("Agricultural & Food Engg", "AG", 40, 20, 3, "JEE Advanced",
               4800, 6500, 10000, 7000, 5500, 8000,
               10.0, 8.0, 25.0, 78, ["Food Processing", "Farm Machinery"]),
        ],
    ),

    # ── 6. IIT Roorkee ─────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Roorkee",
        short_name="IIT Roorkee", institute_type="IIT", established=1847,
        ranking=6, city="Roorkee", state="Uttarakhand",
        nirf_ranking=6, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.20,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=16.0, median_placement_lpa=14.0,
        highest_placement_lpa=180.0, placement_percentage=91.0,
        top_recruiters=["Google", "Microsoft", "Samsung", "Qualcomm", "Adobe"],
        total_seats=1100, website="https://www.iitr.ac.in",
        notable_alumni=["Shantanu Narayen (partial)", "Ajit Singh"],
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 85, 50, 12, "JEE Advanced",
               380, 520, 1600, 800, 470, 750,
               25.0, 21.0, 180.0, 98, ["AI/ML", "Data Science", "Cyber Security"]),
            _b("Electrical Engineering", "EE", 120, 55, 8, "JEE Advanced",
               750, 1050, 3200, 1600, 920, 1400,
               18.0, 15.0, 75.0, 92, ["Power", "VLSI", "Control"]),
            _b("Civil Engineering", "CE", 90, 50, 8, "JEE Advanced",
               2200, 3100, 6200, 3500, 2600, 3800,
               12.0, 10.0, 35.0, 84, ["Structural", "Water", "Earthquake"]),
            _b("Mechanical Engineering", "ME", 140, 55, 6, "JEE Advanced",
               1200, 1700, 4200, 2200, 1400, 2000,
               14.5, 12.0, 55.0, 89, ["Thermal", "Design", "Industrial"]),
        ],
    ),

    # ── 7. IIT Guwahati ────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Guwahati",
        short_name="IIT Guwahati", institute_type="IIT", established=1994,
        ranking=7, city="Guwahati", state="Assam",
        nirf_ranking=7, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=15.0, median_placement_lpa=13.0,
        highest_placement_lpa=160.0, placement_percentage=90.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "TCS", "Goldman Sachs"],
        total_seats=900, website="https://www.iitg.ac.in",
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 45, 12, "JEE Advanced",
               420, 580, 1800, 900, 520, 820,
               24.0, 20.0, 160.0, 98, ["AI/ML", "Data Science", "Networks"]),
            _b("Electronics & Electrical Engg", "EEE", 110, 50, 8, "JEE Advanced",
               850, 1200, 3500, 1750, 1050, 1600,
               17.0, 14.0, 68.0, 91, ["VLSI", "Signal Processing", "Power"]),
            _b("Mechanical Engineering", "ME", 120, 50, 6, "JEE Advanced",
               1400, 1950, 4800, 2500, 1650, 2300,
               13.5, 11.0, 50.0, 88, ["Design", "Thermal", "Manufacturing"]),
        ],
    ),

    # ── 8. IIT Hyderabad ───────────────────────────────────────────
    College(
        name="Indian Institute of Technology Hyderabad",
        short_name="IIT Hyderabad", institute_type="IIT", established=2008,
        ranking=8, city="Sangareddy", state="Telangana",
        nirf_ranking=8, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.20,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=16.0, median_placement_lpa=13.5,
        highest_placement_lpa=170.0, placement_percentage=91.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Qualcomm", "Texas Instruments"],
        total_seats=800, website="https://iith.ac.in",
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 40, 10, "JEE Advanced",
               450, 620, 1900, 950, 550, 870,
               25.0, 21.0, 170.0, 99, ["AI/ML", "Cyber Security", "Data Science"]),
            _b("Electrical Engineering", "EE", 100, 45, 8, "JEE Advanced",
               900, 1250, 3600, 1800, 1100, 1650,
               17.0, 14.0, 70.0, 91, ["VLSI", "Communications", "Power"]),
            _b("Mechanical Engineering", "ME", 110, 40, 5, "JEE Advanced",
               1500, 2100, 5000, 2700, 1750, 2500,
               13.0, 11.0, 48.0, 87, ["Design", "Thermal", "Manufacturing"]),
            _b("Biomedical Engineering", "BME", 40, 20, 5, "JEE Advanced",
               3000, 4200, 8000, 5000, 3500, 5500,
               12.0, 10.0, 35.0, 82, ["Medical Devices", "Biomaterials", "Imaging"]),
        ],
    ),

    # ── 9. IIT BHU Varanasi ────────────────────────────────────────
    College(
        name="Indian Institute of Technology (BHU) Varanasi",
        short_name="IIT BHU", institute_type="IIT", established=1919,
        ranking=9, city="Varanasi", state="Uttar Pradesh",
        nirf_ranking=10, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=15.5, median_placement_lpa=13.0,
        highest_placement_lpa=150.0, placement_percentage=90.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Samsung", "Flipkart"],
        total_seats=1050, website="https://www.iitbhu.ac.in",
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 45, 10, "JEE Advanced",
               500, 700, 2100, 1050, 620, 950,
               23.0, 19.0, 150.0, 98, ["AI/ML", "Software Engg", "Data Science"]),
            _b("Electrical Engineering", "EE", 100, 50, 8, "JEE Advanced",
               1000, 1400, 3800, 1950, 1200, 1800,
               16.0, 13.5, 65.0, 90, ["Power", "Electronics", "Signal Processing"]),
            _b("Mechanical Engineering", "ME", 130, 50, 6, "JEE Advanced",
               1600, 2200, 5200, 2800, 1850, 2600,
               13.0, 11.0, 48.0, 87, ["Thermal", "Design", "Manufacturing"]),
            _b("Ceramic Engineering", "CER", 50, 20, 3, "JEE Advanced",
               4200, 5800, 10000, 6500, 4800, 7500,
               10.0, 8.5, 25.0, 80, ["Glass", "Refractories", "Advanced Ceramics"]),
        ],
    ),

    # ── 10. IIT Indore ─────────────────────────────────────────────
    College(
        name="Indian Institute of Technology Indore",
        short_name="IIT Indore", institute_type="IIT", established=2009,
        ranking=10, city="Indore", state="Madhya Pradesh",
        nirf_ranking=11, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        fee_waiver_policy="Full tuition waiver for SC/ST/PwD",
        avg_placement_lpa=14.5, median_placement_lpa=12.0,
        highest_placement_lpa=140.0, placement_percentage=89.0,
        top_recruiters=["Microsoft", "Amazon", "Samsung", "TCS", "Goldman Sachs"],
        total_seats=600, website="https://www.iiti.ac.in",
        course_types=_IIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 35, 8, "JEE Advanced",
               1200, 1650, 4500, 2300, 1450, 2200,
               22.0, 18.0, 140.0, 97, ["AI/ML", "Data Science", "Security"]),
            _b("Electrical Engineering", "EE", 80, 35, 6, "JEE Advanced",
               2200, 3000, 6500, 3500, 2600, 3800,
               15.0, 12.5, 55.0, 88, ["VLSI", "Communications", "Power"]),
            _b("Mechanical Engineering", "ME", 80, 30, 5, "JEE Advanced",
               3000, 4200, 8000, 4800, 3500, 5200,
               12.5, 10.5, 42.0, 85, ["Design", "Thermal", "Manufacturing"]),
        ],
    ),

    # ── 11. NIT Trichy ─────────────────────────────────────────────
    College(
        name="National Institute of Technology Tiruchirappalli",
        short_name="NIT Trichy", institute_type="NIT", established=1964,
        ranking=11, city="Tiruchirappalli", state="Tamil Nadu",
        nirf_ranking=9, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.12,
        fee_waiver_policy="Tuition waiver for SC/ST",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=60.0, placement_percentage=92.0,
        top_recruiters=["Amazon", "Microsoft", "TCS", "Infosys", "Oracle"],
        total_seats=1200, website="https://www.nitt.edu",
        course_types=_NIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 35, 0, "JEE Main",
               1200, 2500, 6500, 4200, 1800, 3500,
               18.0, 15.0, 60.0, 97, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 90, 35, 0, "JEE Main",
               2800, 5200, 12000, 7500, 3800, 7000,
               14.0, 11.5, 45.0, 90, ["VLSI", "Signal Processing", "IoT"]),
            _b("Electrical & Electronics Engg", "EEE", 80, 30, 0, "JEE Main",
               4000, 7000, 15000, 9000, 5500, 9500,
               12.5, 10.0, 38.0, 87, ["Power", "Control", "Drives"]),
            _b("Mechanical Engineering", "ME", 120, 40, 0, "JEE Main",
               5500, 9000, 18000, 11000, 7000, 12000,
               11.0, 9.0, 32.0, 85, ["Thermal", "Design", "Production"]),
        ],
    ),

    # ── 12. NIT Karnataka Surathkal ────────────────────────────────
    College(
        name="National Institute of Technology Karnataka",
        short_name="NIT Surathkal", institute_type="NIT", established=1960,
        ranking=12, city="Surathkal", state="Karnataka",
        nirf_ranking=12, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.12,
        fee_waiver_policy="Tuition waiver for SC/ST",
        avg_placement_lpa=11.5, median_placement_lpa=9.5,
        highest_placement_lpa=55.0, placement_percentage=91.0,
        top_recruiters=["Amazon", "Google", "TCS", "Samsung", "Oracle"],
        total_seats=1100, website="https://www.nitk.ac.in",
        course_types=_NIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 75, 30, 0, "JEE Main",
               1400, 2800, 7000, 4500, 2000, 3800,
               17.5, 14.5, 55.0, 96, ["AI/ML", "Web", "Cloud Computing"]),
            _b("Electronics & Comm Engg", "ECE", 85, 30, 0, "JEE Main",
               3200, 5800, 13000, 8000, 4200, 7500,
               13.5, 11.0, 42.0, 89, ["VLSI", "Embedded", "Communications"]),
            _b("Mechanical Engineering", "ME", 110, 35, 0, "JEE Main",
               6000, 9500, 19000, 12000, 7500, 13000,
               10.5, 8.5, 30.0, 84, ["Design", "Manufacturing", "Thermal"]),
        ],
    ),

    # ── 13. NIT Warangal ───────────────────────────────────────────
    College(
        name="National Institute of Technology Warangal",
        short_name="NIT Warangal", institute_type="NIT", established=1959,
        ranking=13, city="Warangal", state="Telangana",
        nirf_ranking=15, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.10,
        fee_waiver_policy="Tuition waiver for SC/ST",
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=50.0, placement_percentage=90.0,
        top_recruiters=["Amazon", "Microsoft", "TCS", "Infosys", "Deloitte"],
        total_seats=1050, website="https://www.nitw.ac.in",
        course_types=_NIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 30, 0, "JEE Main",
               1600, 3200, 7500, 4800, 2200, 4200,
               17.0, 14.0, 50.0, 95, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 80, 30, 0, "JEE Main",
               3500, 6200, 14000, 8500, 4500, 8000,
               13.0, 10.5, 40.0, 88, ["VLSI", "Communications", "IoT"]),
            _b("Mechanical Engineering", "ME", 100, 30, 0, "JEE Main",
               6500, 10000, 20000, 13000, 8000, 14000,
               10.0, 8.0, 28.0, 83, ["Thermal", "Design", "Production"]),
        ],
    ),

    # ── 14. NIT Calicut ────────────────────────────────────────────
    College(
        name="National Institute of Technology Calicut",
        short_name="NIT Calicut", institute_type="NIT", established=1961,
        ranking=14, city="Kozhikode", state="Kerala",
        nirf_ranking=14, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=1.2, hostel_fees_per_year=0.10,
        fee_waiver_policy="Tuition waiver for SC/ST",
        avg_placement_lpa=10.5, median_placement_lpa=8.5,
        highest_placement_lpa=48.0, placement_percentage=89.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Oracle", "Wipro"],
        total_seats=1000, website="https://www.nitc.ac.in",
        course_types=_NIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 25, 0, "JEE Main",
               1800, 3500, 8000, 5200, 2500, 4500,
               16.0, 13.0, 48.0, 94, ["AI/ML", "Web Tech", "Networks"]),
            _b("Electronics & Comm Engg", "ECE", 75, 25, 0, "JEE Main",
               3800, 6800, 15000, 9000, 5000, 8500,
               12.5, 10.0, 38.0, 87, ["VLSI", "Signal Processing", "IoT"]),
            _b("Mechanical Engineering", "ME", 90, 30, 0, "JEE Main",
               7000, 11000, 22000, 14000, 8500, 15000,
               9.5, 7.5, 26.0, 82, ["Thermal", "Design", "Manufacturing"]),
        ],
    ),

    # ── 15. NIT Rourkela ───────────────────────────────────────────
    College(
        name="National Institute of Technology Rourkela",
        short_name="NIT Rourkela", institute_type="NIT", established=1961,
        ranking=15, city="Rourkela", state="Odisha",
        nirf_ranking=16, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=1.2, hostel_fees_per_year=0.10,
        fee_waiver_policy="Tuition waiver for SC/ST",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=45.0, placement_percentage=88.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "L&T"],
        total_seats=1000, website="https://www.nitrkl.ac.in",
        course_types=_NIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 65, 25, 0, "JEE Main",
               2000, 3800, 8500, 5500, 2700, 4800,
               15.0, 12.5, 45.0, 93, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 70, 25, 0, "JEE Main",
               4200, 7200, 16000, 9500, 5500, 9000,
               12.0, 9.5, 35.0, 86, ["VLSI", "Communications", "IoT"]),
            _b("Mechanical Engineering", "ME", 85, 30, 0, "JEE Main",
               7500, 12000, 23000, 15000, 9000, 16000,
               9.0, 7.0, 24.0, 81, ["Design", "Thermal", "Industrial"]),
        ],
    ),

    # ── 16. BITS Pilani ────────────────────────────────────────────
    College(
        name="Birla Institute of Technology & Science, Pilani",
        short_name="BITS Pilani", institute_type="Private", established=1964,
        ranking=16, city="Pilani", state="Rajasthan",
        nirf_ranking=20, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=4.5, hostel_fees_per_year=0.40,
        fee_waiver_policy="Merit scholarships available",
        avg_placement_lpa=14.0, median_placement_lpa=12.0,
        highest_placement_lpa=130.0, placement_percentage=92.0,
        top_recruiters=["Google", "Microsoft", "Goldman Sachs", "Samsung", "DE Shaw"],
        total_seats=900, website="https://www.bits-pilani.ac.in",
        notable_alumni=["Kumar Mangalam Birla", "Shankar Vailaya"],
        course_types=_PRIVATE_COURSES + [
            _ct("BE (Hons)", 4, "BITSAT", "10+2 PCM, 75%", 0, 4.5),
            _ct("MSc (Hons) + BE (Hons) Dual", 5, "BITSAT", "10+2 PCM, 75%", 0, 4.5),
        ],
        branches=[
            _b("Computer Science", "CSE", 90, 0, 0, "BITSAT",
               0, 0, 0, 0, 0, 0,
               26.0, 22.0, 130.0, 98, ["AI/ML", "Full Stack", "Security"]),
            _b("Electronics & Instrumentation", "EI", 60, 0, 0, "BITSAT",
               0, 0, 0, 0, 0, 0,
               18.0, 15.0, 60.0, 92, ["VLSI", "IoT", "Control"]),
            _b("Electrical & Electronics", "EEE", 70, 0, 0, "BITSAT",
               0, 0, 0, 0, 0, 0,
               16.0, 13.0, 52.0, 90, ["Power", "Drives", "Embedded"]),
            _b("Mechanical Engineering", "ME", 100, 0, 0, "BITSAT",
               0, 0, 0, 0, 0, 0,
               13.0, 10.5, 40.0, 86, ["Design", "Thermal", "Robotics"]),
            _b("Chemical Engineering", "CH", 70, 0, 0, "BITSAT",
               0, 0, 0, 0, 0, 0,
               14.0, 11.5, 42.0, 88, ["Process", "Polymers", "Pharma"]),
        ],
    ),

    # ── 17. DTU Delhi ──────────────────────────────────────────────
    College(
        name="Delhi Technological University",
        short_name="DTU", institute_type="State Govt", established=1941,
        ranking=17, city="New Delhi", state="Delhi",
        nirf_ranking=30, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=1.8, hostel_fees_per_year=0.15,
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=65.0, placement_percentage=88.0,
        top_recruiters=["Amazon", "Microsoft", "Google", "Samsung", "Adobe"],
        total_seats=1800, website="https://dtu.ac.in",
        course_types=[_ct("B.Tech", 4, "JEE Main / JAC Delhi", "10+2 PCM, 75%", 0, 1.8)],
        branches=[
            _b("Computer Science & Engineering", "CSE", 120, 30, 0, "JEE Main",
               800, 1800, 5500, 3200, 1200, 2800,
               18.0, 15.0, 65.0, 94, ["AI/ML", "Web Dev", "Cloud"]),
            _b("Information Technology", "IT", 80, 20, 0, "JEE Main",
               1200, 2500, 7000, 4000, 1600, 3500,
               16.0, 13.0, 55.0, 91, ["Cyber Security", "Data Science", "DevOps"]),
            _b("Electronics & Comm Engg", "ECE", 90, 25, 0, "JEE Main",
               2500, 5000, 11000, 6500, 3500, 6500,
               12.0, 10.0, 38.0, 85, ["VLSI", "Embedded", "IoT"]),
            _b("Mechanical Engineering", "ME", 120, 30, 0, "JEE Main",
               5000, 8500, 18000, 11000, 6500, 12000,
               9.5, 7.5, 28.0, 80, ["Design", "Thermal", "Automotive"]),
        ],
    ),

    # ── 18. NSUT Delhi ─────────────────────────────────────────────
    College(
        name="Netaji Subhas University of Technology",
        short_name="NSUT", institute_type="State Govt", established=1983,
        ranking=18, city="New Delhi", state="Delhi",
        nirf_ranking=35, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=1.8, hostel_fees_per_year=0.15,
        avg_placement_lpa=10.5, median_placement_lpa=8.5,
        highest_placement_lpa=60.0, placement_percentage=87.0,
        top_recruiters=["Amazon", "Microsoft", "TCS", "Samsung", "Flipkart"],
        total_seats=1500, website="https://nsut.ac.in",
        course_types=[_ct("B.Tech", 4, "JEE Main / JAC Delhi", "10+2 PCM, 75%", 0, 1.8)],
        branches=[
            _b("Computer Science & Engineering", "CSE", 110, 25, 0, "JEE Main",
               900, 2000, 6000, 3500, 1300, 3000,
               17.0, 14.0, 60.0, 93, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Information Technology", "IT", 70, 15, 0, "JEE Main",
               1300, 2800, 7500, 4200, 1700, 3800,
               15.0, 12.0, 50.0, 90, ["Data Science", "Web Dev", "DevOps"]),
            _b("Electronics & Comm Engg", "ECE", 80, 20, 0, "JEE Main",
               2800, 5500, 12000, 7000, 3800, 7000,
               11.5, 9.5, 35.0, 84, ["VLSI", "Embedded", "Communications"]),
        ],
    ),

    # ── 19. VIT Vellore ────────────────────────────────────────────
    College(
        name="Vellore Institute of Technology",
        short_name="VIT Vellore", institute_type="Private", established=1984,
        ranking=19, city="Vellore", state="Tamil Nadu",
        nirf_ranking=18, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=3.5, hostel_fees_per_year=0.35,
        avg_placement_lpa=8.5, median_placement_lpa=6.5,
        highest_placement_lpa=50.0, placement_percentage=85.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "Wipro"],
        total_seats=5000, website="https://vit.ac.in",
        course_types=[_ct("B.Tech", 4, "VITEEE", "10+2 PCM, 60%", 0, 3.5)],
        branches=[
            _b("Computer Science & Engineering", "CSE", 600, 100, 0, "VITEEE",
               0, 0, 0, 0, 0, 0,
               14.0, 11.0, 50.0, 92, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 400, 60, 0, "VITEEE",
               0, 0, 0, 0, 0, 0,
               8.0, 6.0, 25.0, 80, ["VLSI", "Embedded", "IoT"]),
            _b("Mechanical Engineering", "ME", 300, 40, 0, "VITEEE",
               0, 0, 0, 0, 0, 0,
               6.5, 5.0, 18.0, 75, ["Design", "Manufacturing", "Automotive"]),
        ],
    ),

    # ── 20. COEP Pune ──────────────────────────────────────────────
    College(
        name="College of Engineering Pune",
        short_name="COEP Pune", institute_type="State Govt", established=1854,
        ranking=20, city="Pune", state="Maharashtra",
        nirf_ranking=38, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=1.2, hostel_fees_per_year=0.10,
        avg_placement_lpa=9.5, median_placement_lpa=7.5,
        highest_placement_lpa=45.0, placement_percentage=87.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Persistent", "L&T"],
        total_seats=900, website="https://www.coep.org.in",
        course_types=[_ct("B.Tech", 4, "JEE Main / MHT CET", "10+2 PCM, 60%", 0, 1.2)],
        branches=[
            _b("Computer Engineering", "CSE", 70, 20, 0, "JEE Main",
               4000, 7000, 15000, 9000, 5000, 9000,
               16.0, 13.0, 45.0, 93, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Telecom Engg", "EXTC", 60, 15, 0, "JEE Main",
               6000, 10000, 20000, 12000, 7500, 13000,
               10.0, 8.0, 28.0, 82, ["VLSI", "Communications", "Embedded"]),
            _b("Mechanical Engineering", "ME", 80, 20, 0, "JEE Main",
               8000, 14000, 25000, 16000, 10000, 18000,
               8.0, 6.5, 20.0, 78, ["Design", "Thermal", "Manufacturing"]),
        ],
    ),

    # ── 21. Jadavpur University ────────────────────────────────────
    College(
        name="Jadavpur University",
        short_name="Jadavpur Univ", institute_type="State Govt", established=1955,
        ranking=21, city="Kolkata", state="West Bengal",
        nirf_ranking=19, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.15, hostel_fees_per_year=0.05,
        avg_placement_lpa=9.0, median_placement_lpa=7.0,
        highest_placement_lpa=42.0, placement_percentage=86.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "L&T"],
        total_seats=1200, website="http://www.jaduniv.edu.in",
        course_types=[_ct("B.E.", 4, "WBJEE / JEE Main", "10+2 PCM, 60%", 0, 0.15)],
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 20, 0, "WBJEE",
               0, 0, 0, 0, 0, 0,
               15.0, 12.0, 42.0, 92, ["AI/ML", "Software Engg", "Networks"]),
            _b("Electronics & Telecom Engg", "ETCE", 60, 15, 0, "WBJEE",
               0, 0, 0, 0, 0, 0,
               10.0, 8.0, 28.0, 82, ["VLSI", "Signal Processing", "IoT"]),
            _b("Mechanical Engineering", "ME", 80, 20, 0, "WBJEE",
               0, 0, 0, 0, 0, 0,
               7.5, 6.0, 18.0, 75, ["Design", "Thermal", "Manufacturing"]),
        ],
    ),

    # ── 22. Anna University ────────────────────────────────────────
    College(
        name="Anna University",
        short_name="Anna Univ", institute_type="State Govt", established=1978,
        ranking=22, city="Chennai", state="Tamil Nadu",
        nirf_ranking=17, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.50, hostel_fees_per_year=0.08,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=35.0, placement_percentage=80.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=2500, website="https://www.annauniv.edu",
        course_types=[_ct("B.E.", 4, "TNEA (12th marks based)", "10+2 PCM, 50%", 0, 0.50)],
        branches=[
            _b("Computer Science & Engineering", "CSE", 120, 40, 0, "TNEA",
               0, 0, 0, 0, 0, 0,
               12.0, 9.0, 35.0, 88, ["AI/ML", "Cloud", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 120, 35, 0, "TNEA",
               0, 0, 0, 0, 0, 0,
               7.5, 5.5, 20.0, 75, ["VLSI", "Communications", "Embedded"]),
            _b("Mechanical Engineering", "ME", 120, 30, 0, "TNEA",
               0, 0, 0, 0, 0, 0,
               6.0, 4.5, 15.0, 70, ["Design", "Manufacturing", "Thermal"]),
        ],
    ),

    # ── 23. ICT Mumbai ─────────────────────────────────────────────
    College(
        name="Institute of Chemical Technology Mumbai",
        short_name="ICT Mumbai", institute_type="Deemed", established=1933,
        ranking=23, city="Mumbai", state="Maharashtra",
        nirf_ranking=28, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.80, hostel_fees_per_year=0.10,
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=40.0, placement_percentage=88.0,
        top_recruiters=["Reliance", "BASF", "UPL", "Pidilite", "Asian Paints"],
        total_seats=700, website="https://www.ictmumbai.edu.in",
        course_types=[_ct("B.Tech", 4, "MHT CET / JEE Main", "10+2 PCM, 60%", 0, 0.80)],
        branches=[
            _b("Chemical Engineering", "CH", 100, 40, 10, "MHT CET",
               0, 0, 0, 0, 0, 0,
               14.0, 11.0, 40.0, 90, ["Process Design", "Petroleum", "Pharma"]),
            _b("Pharmaceutical Engg & Tech", "PT", 60, 20, 5, "MHT CET",
               0, 0, 0, 0, 0, 0,
               10.0, 8.0, 28.0, 85, ["Drug Formulation", "QA", "Bioprocess"]),
            _b("Food Engineering & Technology", "FT", 40, 15, 3, "MHT CET",
               0, 0, 0, 0, 0, 0,
               8.0, 6.5, 22.0, 80, ["Food Processing", "Quality Control", "Packaging"]),
        ],
    ),
]


# ═══════════════════════════════════════════════════════════════════════════
# IIITs — ALL INDIA (28 COLLEGES)
# ═══════════════════════════════════════════════════════════════════════════

_IIIT_DIRECTORY: list[College] = [
    # ── 1. IIIT Hyderabad ──────────────────────────────────────────
    College(
        name="International Institute of Information Technology Hyderabad",
        short_name="IIIT Hyderabad", institute_type="IIIT", established=1998,
        ranking=1, city="Hyderabad", state="Telangana",
        nirf_ranking=22, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=3.5, hostel_fees_per_year=0.25,
        avg_placement_lpa=18.0, median_placement_lpa=16.0,
        highest_placement_lpa=150.0, placement_percentage=96.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Uber", "Qualcomm"],
        total_seats=500, website="https://www.iiit.ac.in",
        course_types=[
            _ct("B.Tech", 4, "JEE Main / UGEE", "10+2 PCM, 75%", 0, 3.5),
            _ct("Dual Degree (B.Tech+MS)", 5, "JEE Main / UGEE", "10+2 PCM, 75%", 0, 3.5),
        ],
        branches=[
            _b("Computer Science & Engineering", "CSE", 150, 50, 20, "JEE Main",
               800, 1500, 5000, 3000, 1200, 2500,
               28.0, 24.0, 150.0, 99, ["AI/ML", "NLP", "Computer Vision"]),
            _b("Electronics & Comm Engg", "ECE", 100, 30, 10, "JEE Main",
               2500, 4500, 10000, 6500, 3500, 6000,
               16.0, 13.0, 55.0, 90, ["VLSI", "Signal Processing", "IoT"]),
        ],
    ),
    # ── 2. IIIT Delhi ──────────────────────────────────────────────
    College(
        name="Indraprastha Institute of Information Technology Delhi",
        short_name="IIIT Delhi", institute_type="IIIT", established=2008,
        ranking=2, city="New Delhi", state="Delhi",
        nirf_ranking=25, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=3.8, hostel_fees_per_year=0.30,
        avg_placement_lpa=16.0, median_placement_lpa=14.0,
        highest_placement_lpa=120.0, placement_percentage=93.0,
        top_recruiters=["Google", "Amazon", "Microsoft", "Samsung", "Adobe"],
        total_seats=450, website="https://iiitd.ac.in",
        course_types=[
            _ct("B.Tech", 4, "JEE Main / JAC Delhi", "10+2 PCM, 75%", 0, 3.8),
            _ct("M.Tech", 2, "GATE", "B.Tech/BE", 0, 2.0),
        ],
        branches=[
            _b("Computer Science & Engineering", "CSE", 120, 40, 15, "JEE Main",
               1000, 2000, 6000, 3500, 1500, 3000,
               24.0, 20.0, 120.0, 97, ["AI/ML", "Data Science", "Security"]),
            _b("Electronics & Comm Engg", "ECE", 80, 20, 8, "JEE Main",
               3000, 5500, 12000, 7000, 4000, 7000,
               14.0, 11.5, 48.0, 89, ["VLSI", "IoT", "Communications"]),
            _b("Computer Science & Applied Math", "CSAM", 60, 0, 0, "JEE Main",
               1500, 3000, 7500, 4500, 2200, 4000,
               22.0, 18.0, 100.0, 95, ["ML", "Optimization", "Algorithms"]),
        ],
    ),
    # ── 3. IIIT Allahabad ──────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Allahabad",
        short_name="IIIT Allahabad", institute_type="IIIT", established=1999,
        ranking=3, city="Prayagraj", state="Uttar Pradesh",
        nirf_ranking=30, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.20,
        fee_waiver_policy="Tuition waiver for SC/ST/PwD",
        avg_placement_lpa=14.0, median_placement_lpa=12.0,
        highest_placement_lpa=80.0, placement_percentage=90.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Samsung", "Adobe"],
        total_seats=600, website="https://www.iiita.ac.in",
        course_types=_IIIT_COURSES + [
            _ct("Dual Degree (B.Tech+M.Tech)", 5, "JEE Main", "10+2 PCM, 75%", 0, 2.0),
        ],
        branches=[
            _b("Information Technology", "IT", 90, 30, 15, "JEE Main",
               1500, 3000, 7000, 4500, 2200, 4000,
               22.0, 18.0, 80.0, 96, ["AI/ML", "Web Tech", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 80, 25, 10, "JEE Main",
               3500, 6000, 13000, 8000, 4500, 7500,
               14.0, 11.0, 45.0, 88, ["VLSI", "IoT", "Signal Processing"]),
            _b("Computer Science & Engineering", "CSE", 60, 20, 0, "JEE Main",
               2000, 4000, 9000, 5500, 2800, 5000,
               20.0, 16.0, 75.0, 94, ["AI/ML", "Data Science", "Security"]),
        ],
    ),
    # ── 4. IIIT Bangalore ──────────────────────────────────────────
    College(
        name="International Institute of Information Technology Bangalore",
        short_name="IIIT Bangalore", institute_type="IIIT", established=1999,
        ranking=4, city="Bangalore", state="Karnataka",
        nirf_ranking=45, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=4.0, hostel_fees_per_year=0.30,
        avg_placement_lpa=15.0, median_placement_lpa=13.0,
        highest_placement_lpa=90.0, placement_percentage=92.0,
        top_recruiters=["Google", "Microsoft", "Amazon", "Flipkart", "SAP"],
        total_seats=400, website="https://www.iiitb.ac.in",
        course_types=[
            _ct("B.Tech (IMT)", 5, "JEE Main / PESSAT", "10+2 PCM, 75%", 0, 4.0),
            _ct("M.Tech", 2, "GATE", "B.Tech/BE", 0, 3.0),
            _ct("MS by Research", 2.5, "GATE", "B.Tech/BE", 0, 3.0),
        ],
        branches=[
            _b("Computer Science & Engineering", "CSE", 120, 60, 0, "JEE Main",
               0, 0, 0, 0, 0, 0,
               24.0, 20.0, 90.0, 97, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 20, 0, "JEE Main",
               0, 0, 0, 0, 0, 0,
               14.0, 11.0, 45.0, 85, ["VLSI", "Embedded Systems", "IoT"]),
        ],
    ),
    # ── 5. ABV-IIITM Gwalior ───────────────────────────────────────
    College(
        name="ABV Indian Institute of Information Technology & Management Gwalior",
        short_name="ABV-IIITM Gwalior", institute_type="IIIT", established=1997,
        ranking=5, city="Gwalior", state="Madhya Pradesh",
        nirf_ranking=55, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=1.8, hostel_fees_per_year=0.15,
        fee_waiver_policy="Tuition waiver for SC/ST/PwD",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=55.0, placement_percentage=88.0,
        top_recruiters=["Amazon", "Microsoft", "TCS", "Infosys", "Samsung"],
        total_seats=450, website="https://www.iiitm.ac.in",
        course_types=_IIIT_COURSES + [
            _ct("IPG (Integrated PG)", 5, "JEE Main", "10+2 PCM, 75%", 0, 1.8),
        ],
        branches=[
            _b("Information Technology", "IT", 80, 25, 0, "JEE Main",
               2500, 4500, 10000, 6500, 3500, 6000,
               18.0, 14.0, 55.0, 92, ["AI/ML", "Web Tech", "Data Science"]),
            _b("Information & Comm Technology", "ICT", 60, 20, 0, "JEE Main",
               3000, 5500, 12000, 7500, 4000, 7000,
               14.0, 11.0, 42.0, 86, ["IoT", "Networks", "Signal Processing"]),
        ],
    ),
    # ── 6. IIITDM Jabalpur ─────────────────────────────────────────
    College(
        name="IIIT Design & Manufacturing Jabalpur",
        short_name="IIITDM Jabalpur", institute_type="IIIT", established=2005,
        ranking=6, city="Jabalpur", state="Madhya Pradesh",
        nirf_ranking=65, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.12,
        fee_waiver_policy="Tuition waiver for SC/ST/PwD",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=42.0, placement_percentage=85.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Samsung", "L&T"],
        total_seats=350, website="https://www.iiitdmj.ac.in",
        course_types=_IIIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 20, 0, "JEE Main",
               5000, 8500, 18000, 11000, 6500, 12000,
               16.0, 13.0, 42.0, 90, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 15, 0, "JEE Main",
               7000, 12000, 22000, 14000, 8500, 15000,
               10.0, 8.0, 28.0, 82, ["VLSI", "Embedded", "IoT"]),
            _b("Mechanical Engineering", "ME", 50, 15, 0, "JEE Main",
               9000, 15000, 28000, 18000, 11000, 20000,
               8.0, 6.5, 22.0, 78, ["Design", "Smart Manufacturing", "CAD/CAM"]),
            _b("Computer Science & Design", "CSD", 30, 0, 0, "JEE Main",
               6000, 10000, 20000, 13000, 7500, 14000,
               14.0, 11.0, 38.0, 88, ["UI/UX", "Product Design", "HCI"]),
        ],
    ),
    # ── 7. IIITDM Kancheepuram ─────────────────────────────────────
    College(
        name="IIIT Design & Manufacturing Kancheepuram",
        short_name="IIITDM Kancheepuram", institute_type="IIIT", established=2007,
        ranking=7, city="Chennai", state="Tamil Nadu",
        nirf_ranking=60, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.12,
        fee_waiver_policy="Tuition waiver for SC/ST/PwD",
        avg_placement_lpa=10.5, median_placement_lpa=8.5,
        highest_placement_lpa=45.0, placement_percentage=86.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Zoho", "Samsung"],
        total_seats=380, website="https://www.iiitdm.ac.in",
        course_types=_IIIT_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 65, 20, 0, "JEE Main",
               4500, 8000, 17000, 10000, 6000, 11000,
               16.5, 13.5, 45.0, 91, ["AI/ML", "Data Science", "Security"]),
            _b("Electronics & Comm Engg", "ECE", 55, 15, 0, "JEE Main",
               6500, 11000, 21000, 13000, 8000, 14000,
               10.5, 8.5, 30.0, 83, ["VLSI", "Signal Processing", "IoT"]),
            _b("Mechanical Engineering", "ME", 55, 15, 0, "JEE Main",
               8500, 14000, 26000, 17000, 10500, 19000,
               8.5, 7.0, 24.0, 79, ["Smart Manufacturing", "Design", "Mechatronics"]),
        ],
    ),
    # ── 8. IIIT Sri City ───────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Sri City",
        short_name="IIIT Sri City", institute_type="IIIT", established=2013,
        ranking=8, city="Chittoor", state="Andhra Pradesh",
        nirf_ranking=70, naac_grade="A",
        avg_fees_lpa=2.5, hostel_fees_per_year=0.20,
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=42.0, placement_percentage=85.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "Wipro"],
        total_seats=300, website="https://www.iiits.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 100, 0, 0, "JEE Main",
               5500, 9000, 19000, 12000, 7000, 13000,
               16.0, 13.0, 42.0, 90, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 0, 0, "JEE Main",
               8000, 13000, 24000, 15000, 9500, 17000,
               9.5, 7.5, 25.0, 80, ["VLSI", "Embedded", "IoT"]),
        ],
    ),
    # ── 9. IIIT Lucknow ────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Lucknow",
        short_name="IIIT Lucknow", institute_type="IIIT", established=2015,
        ranking=9, city="Lucknow", state="Uttar Pradesh",
        nirf_ranking=92,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=8.0, median_placement_lpa=6.5,
        highest_placement_lpa=30.0, placement_percentage=80.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "Samsung"],
        total_seats=240, website="https://iiitl.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               7500, 12500, 23000, 15000, 9000, 16000,
               13.0, 10.5, 30.0, 85, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Information Technology", "IT", 60, 0, 0, "JEE Main",
               9000, 15000, 26000, 17000, 11000, 19000,
               10.0, 8.0, 25.0, 78, ["Web Tech", "Data Science", "DevOps"]),
        ],
    ),
    # ── 10. IIIT Guwahati ──────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Guwahati",
        short_name="IIIT Guwahati", institute_type="IIIT", established=2013,
        ranking=10, city="Guwahati", state="Assam",
        nirf_ranking=80,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=8.5, median_placement_lpa=7.0,
        highest_placement_lpa=35.0, placement_percentage=82.0,
        top_recruiters=["Amazon", "TCS", "Infosys", "Cognizant", "L&T"],
        total_seats=250, website="https://www.iiitg.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               7000, 12000, 22000, 14000, 8500, 15000,
               14.0, 11.0, 35.0, 87, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 0, 0, "JEE Main",
               10000, 16000, 28000, 18000, 12000, 20000,
               8.0, 6.5, 22.0, 78, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 11. IIIT Vadodara ──────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Vadodara",
        short_name="IIIT Vadodara", institute_type="IIIT", established=2013,
        ranking=11, city="Vadodara", state="Gujarat",
        nirf_ranking=85,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=8.0, median_placement_lpa=6.5,
        highest_placement_lpa=32.0, placement_percentage=80.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "L&T"],
        total_seats=240, website="https://iiitvadodara.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               7500, 12500, 23000, 15000, 9000, 16000,
               13.0, 10.0, 32.0, 85, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Information Technology", "IT", 60, 0, 0, "JEE Main",
               9000, 15000, 26000, 17000, 11000, 19000,
               10.0, 8.0, 25.0, 78, ["Web Tech", "Cloud", "DevOps"]),
        ],
    ),
    # ── 12. IIIT Kota ──────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Kota",
        short_name="IIIT Kota", institute_type="IIIT", established=2013,
        ranking=12, city="Kota", state="Rajasthan",
        nirf_ranking=90,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=7.5, median_placement_lpa=6.0,
        highest_placement_lpa=28.0, placement_percentage=78.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=220, website="https://www.iiitkota.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               8000, 13000, 24000, 15500, 9500, 17000,
               12.0, 9.5, 28.0, 83, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 0, 0, "JEE Main",
               11000, 17000, 30000, 19000, 13000, 22000,
               7.5, 6.0, 20.0, 75, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 13. IIIT Trichy ────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Tiruchirappalli",
        short_name="IIIT Trichy", institute_type="IIIT", established=2013,
        ranking=13, city="Tiruchirappalli", state="Tamil Nadu",
        nirf_ranking=88,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=8.0, median_placement_lpa=6.5,
        highest_placement_lpa=30.0, placement_percentage=80.0,
        top_recruiters=["TCS", "Infosys", "Zoho", "Cognizant", "Wipro"],
        total_seats=220, website="https://www.iiitt.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               7500, 12500, 23000, 15000, 9000, 16000,
               13.0, 10.5, 30.0, 85, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 0, 0, "JEE Main",
               10500, 16500, 28000, 18500, 12500, 20500,
               8.0, 6.5, 22.0, 77, ["VLSI", "Signal Processing", "IoT"]),
        ],
    ),
    # ── 14. IIIT Una ───────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Una",
        short_name="IIIT Una", institute_type="IIIT", established=2014,
        ranking=14, city="Una", state="Himachal Pradesh",
        nirf_ranking=95,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=25.0, placement_percentage=76.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=200, website="https://iiitu.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 0, 0, "JEE Main",
               9000, 14500, 26000, 17000, 11000, 19000,
               11.0, 8.5, 25.0, 81, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               12000, 18000, 32000, 21000, 14000, 24000,
               7.0, 5.5, 18.0, 73, ["VLSI", "IoT", "Embedded"]),
            _b("Information Technology", "IT", 40, 0, 0, "JEE Main",
               10000, 16000, 28000, 18500, 12000, 20000,
               9.5, 7.5, 22.0, 78, ["Web Tech", "Data Science", "DevOps"]),
        ],
    ),
    # ── 15. IIIT Sonepat ───────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Sonepat",
        short_name="IIIT Sonepat", institute_type="IIIT", established=2014,
        ranking=15, city="Sonepat", state="Haryana",
        nirf_ranking=100,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=24.0, placement_percentage=75.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=200, website="https://iiitsonepat.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               9500, 15000, 27000, 17500, 11500, 19500,
               11.0, 8.5, 24.0, 80, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               13000, 19000, 33000, 22000, 15000, 25000,
               7.0, 5.5, 18.0, 72, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 16. IIIT Kalyani ───────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Kalyani",
        short_name="IIIT Kalyani", institute_type="IIIT", established=2014,
        ranking=16, city="Kalyani", state="West Bengal",
        nirf_ranking=105,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.15,
        avg_placement_lpa=6.5, median_placement_lpa=5.0,
        highest_placement_lpa=22.0, placement_percentage=74.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "Capgemini"],
        total_seats=200, website="https://iiitkalyani.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 0, 0, "JEE Main",
               10000, 16000, 28000, 18000, 12000, 20000,
               10.5, 8.0, 22.0, 79, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               14000, 20000, 34000, 23000, 16000, 26000,
               6.5, 5.0, 16.0, 70, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 17. IIIT Dharwad ───────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Dharwad",
        short_name="IIIT Dharwad", institute_type="IIIT", established=2015,
        ranking=17, city="Dharwad", state="Karnataka",
        nirf_ranking=98,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=7.5, median_placement_lpa=6.0,
        highest_placement_lpa=28.0, placement_percentage=78.0,
        top_recruiters=["TCS", "Infosys", "Wipro", "Cognizant", "HCL"],
        total_seats=220, website="https://iiitdwd.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 80, 0, 0, "JEE Main",
               8000, 13500, 24000, 15500, 9500, 17000,
               12.0, 9.5, 28.0, 83, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 60, 0, 0, "JEE Main",
               11000, 17000, 30000, 19500, 13000, 22000,
               7.5, 6.0, 20.0, 75, ["VLSI", "Signal Processing", "IoT"]),
        ],
    ),
    # ── 18. IIIT Kancheepuram (PPP) ────────────────────────────────
    College(
        name="Indian Institute of Information Technology Kancheepuram",
        short_name="IIIT Kancheepuram", institute_type="IIIT", established=2014,
        ranking=18, city="Kancheepuram", state="Tamil Nadu",
        nirf_ranking=102,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.15,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=25.0, placement_percentage=76.0,
        top_recruiters=["TCS", "Infosys", "Zoho", "Cognizant", "Wipro"],
        total_seats=200, website="https://www.iiitk.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 0, 0, "JEE Main",
               9000, 14500, 26000, 17000, 11000, 19000,
               11.0, 8.5, 25.0, 80, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               12500, 18500, 32000, 21000, 14500, 24000,
               7.0, 5.5, 18.0, 73, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 19. IIITDM Kurnool ─────────────────────────────────────────
    College(
        name="IIIT Design & Manufacturing Kurnool",
        short_name="IIITDM Kurnool", institute_type="IIIT", established=2015,
        ranking=19, city="Kurnool", state="Andhra Pradesh",
        nirf_ranking=110,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.15,
        avg_placement_lpa=6.5, median_placement_lpa=5.0,
        highest_placement_lpa=22.0, placement_percentage=74.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "L&T"],
        total_seats=180, website="https://iiitk.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               10000, 16000, 28000, 18500, 12000, 20000,
               10.5, 8.0, 22.0, 79, ["AI/ML", "Data Science", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 40, 0, 0, "JEE Main",
               14000, 20000, 34000, 22000, 16000, 26000,
               6.5, 5.0, 16.0, 70, ["VLSI", "IoT", "Smart Manufacturing"]),
            _b("Mechanical Engineering", "ME", 40, 0, 0, "JEE Main",
               16000, 24000, 38000, 26000, 18000, 30000,
               6.0, 4.5, 14.0, 68, ["Design", "Smart Manufacturing", "CAD/CAM"]),
        ],
    ),
    # ── 20. IIIT Nagpur ────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Nagpur",
        short_name="IIIT Nagpur", institute_type="IIIT", established=2016,
        ranking=20, city="Nagpur", state="Maharashtra",
        nirf_ranking=108,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=25.0, placement_percentage=76.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "Tech Mahindra"],
        total_seats=200, website="https://iiitn.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 0, 0, "JEE Main",
               9000, 15000, 27000, 17500, 11000, 19000,
               11.0, 8.5, 25.0, 81, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               12500, 18500, 32000, 21000, 14500, 24000,
               7.0, 5.5, 18.0, 73, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 21. IIIT Pune ──────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Pune",
        short_name="IIIT Pune", institute_type="IIIT", established=2016,
        ranking=21, city="Pune", state="Maharashtra",
        nirf_ranking=112,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=24.0, placement_percentage=76.0,
        top_recruiters=["TCS", "Infosys", "Persistent", "Cognizant", "Wipro"],
        total_seats=200, website="https://www.iiitp.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 70, 0, 0, "JEE Main",
               9500, 15500, 27500, 18000, 11500, 20000,
               11.0, 8.5, 24.0, 80, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               13000, 19000, 33000, 22000, 15000, 25000,
               7.0, 5.5, 18.0, 72, ["VLSI", "IoT", "Signal Processing"]),
        ],
    ),
    # ── 22. IIIT Ranchi ────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Ranchi",
        short_name="IIIT Ranchi", institute_type="IIIT", established=2016,
        ranking=22, city="Ranchi", state="Jharkhand",
        nirf_ranking=115,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        avg_placement_lpa=6.0, median_placement_lpa=4.5,
        highest_placement_lpa=20.0, placement_percentage=72.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=180, website="https://iiitranchi.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               11000, 17000, 30000, 19500, 13000, 22000,
               9.5, 7.5, 20.0, 77, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               15000, 22000, 36000, 24000, 17000, 28000,
               6.0, 4.5, 15.0, 68, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 23. IIIT Bhagalpur ─────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Bhagalpur",
        short_name="IIIT Bhagalpur", institute_type="IIIT", established=2017,
        ranking=23, city="Bhagalpur", state="Bihar",
        nirf_ranking=120,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        avg_placement_lpa=5.5, median_placement_lpa=4.0,
        highest_placement_lpa=18.0, placement_percentage=70.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=180, website="https://iiitbh.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               12000, 18000, 32000, 21000, 14000, 24000,
               9.0, 7.0, 18.0, 75, ["AI/ML", "Full Stack", "Web Tech"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               16000, 23000, 38000, 25000, 18000, 30000,
               5.5, 4.0, 14.0, 66, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 24. IIIT Bhopal ───────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Bhopal",
        short_name="IIIT Bhopal", institute_type="IIIT", established=2017,
        ranking=24, city="Bhopal", state="Madhya Pradesh",
        nirf_ranking=118,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        avg_placement_lpa=5.5, median_placement_lpa=4.0,
        highest_placement_lpa=18.0, placement_percentage=70.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=180, website="https://www.iiitbhopal.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               12000, 18500, 32500, 21500, 14500, 24500,
               9.0, 7.0, 18.0, 75, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               16000, 23500, 38500, 25500, 18500, 30500,
               5.5, 4.0, 14.0, 66, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 25. IIIT Surat ────────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Surat",
        short_name="IIIT Surat", institute_type="IIIT", established=2017,
        ranking=25, city="Surat", state="Gujarat",
        nirf_ranking=116,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=6.0, median_placement_lpa=4.5,
        highest_placement_lpa=20.0, placement_percentage=72.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=180, website="https://svnit.ac.in/iiitsurat",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               11000, 17500, 30500, 20000, 13000, 22000,
               9.5, 7.5, 20.0, 77, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               15000, 22000, 36000, 24000, 17000, 28000,
               6.0, 4.5, 15.0, 68, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 26. IIIT Kottayam ─────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Kottayam",
        short_name="IIIT Kottayam", institute_type="IIIT", established=2015,
        ranking=26, city="Kottayam", state="Kerala",
        nirf_ranking=125,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.18,
        avg_placement_lpa=6.0, median_placement_lpa=4.5,
        highest_placement_lpa=20.0, placement_percentage=72.0,
        top_recruiters=["TCS", "Infosys", "UST", "Cognizant", "Wipro"],
        total_seats=180, website="https://www.iiitkottayam.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               11000, 17000, 30000, 19500, 13000, 22000,
               9.5, 7.5, 20.0, 77, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 50, 0, 0, "JEE Main",
               15000, 22000, 36000, 24000, 17000, 28000,
               6.0, 4.5, 15.0, 68, ["VLSI", "IoT", "Signal Processing"]),
        ],
    ),
    # ── 27. IIIT Raichur ──────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Raichur",
        short_name="IIIT Raichur", institute_type="IIIT", established=2019,
        ranking=27, city="Raichur", state="Karnataka",
        nirf_ranking=130,
        avg_fees_lpa=2.5, hostel_fees_per_year=0.15,
        avg_placement_lpa=5.0, median_placement_lpa=3.5,
        highest_placement_lpa=15.0, placement_percentage=68.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=150, website="https://iiitr.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 60, 0, 0, "JEE Main",
               14000, 21000, 35000, 23000, 16000, 27000,
               8.0, 6.0, 15.0, 73, ["AI/ML", "Full Stack", "Data Science"]),
            _b("Electronics & Comm Engg", "ECE", 40, 0, 0, "JEE Main",
               18000, 26000, 42000, 28000, 20000, 34000,
               5.0, 3.5, 12.0, 64, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 28. IIIT Agartala ─────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Agartala",
        short_name="IIIT Agartala", institute_type="IIIT", established=2018,
        ranking=28, city="Agartala", state="Tripura",
        nirf_ranking=135,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.12,
        avg_placement_lpa=4.5, median_placement_lpa=3.5,
        highest_placement_lpa=14.0, placement_percentage=65.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=140, website="https://iiitagartala.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 50, 0, 0, "JEE Main",
               15000, 22000, 36000, 24000, 17000, 28000,
               7.5, 5.5, 14.0, 70, ["AI/ML", "Full Stack", "Web Tech"]),
            _b("Electronics & Comm Engg", "ECE", 40, 0, 0, "JEE Main",
               19000, 27000, 44000, 29000, 21000, 35000,
               4.5, 3.5, 11.0, 62, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
    # ── 29. IIIT Manipur ──────────────────────────────────────────
    College(
        name="Indian Institute of Information Technology Senapati, Manipur",
        short_name="IIIT Manipur", institute_type="IIIT", established=2015,
        ranking=29, city="Imphal", state="Manipur",
        nirf_ranking=140,
        avg_fees_lpa=2.0, hostel_fees_per_year=0.12,
        avg_placement_lpa=4.5, median_placement_lpa=3.5,
        highest_placement_lpa=14.0, placement_percentage=65.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=130, website="https://iiitmanipur.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 50, 0, 0, "JEE Main",
               15000, 22000, 37000, 25000, 17500, 28500,
               7.5, 5.5, 14.0, 70, ["AI/ML", "Full Stack", "Cloud"]),
            _b("Electronics & Comm Engg", "ECE", 40, 0, 0, "JEE Main",
               19000, 28000, 45000, 30000, 22000, 36000,
               4.5, 3.5, 11.0, 62, ["VLSI", "IoT", "Communications"]),
        ],
    ),
    # ── 30. IIIT Srikakulam ───────────────────────────────────────
    College(
        name="Rajiv Gandhi University of Knowledge Technologies IIIT Srikakulam",
        short_name="IIIT Srikakulam", institute_type="IIIT", established=2015,
        ranking=30, city="Srikakulam", state="Andhra Pradesh",
        nirf_ranking=145,
        avg_fees_lpa=1.5, hostel_fees_per_year=0.10,
        avg_placement_lpa=4.0, median_placement_lpa=3.0,
        highest_placement_lpa=12.0, placement_percentage=62.0,
        top_recruiters=["TCS", "Infosys", "Cognizant", "Wipro", "HCL"],
        total_seats=120, website="https://www.rgukt.ac.in",
        course_types=_IIIT_PPP_COURSES,
        branches=[
            _b("Computer Science & Engineering", "CSE", 50, 0, 0, "JEE Main",
               16000, 24000, 38000, 26000, 18000, 30000,
               6.5, 5.0, 12.0, 67, ["AI/ML", "Full Stack", "Web Tech"]),
            _b("Electronics & Comm Engg", "ECE", 40, 0, 0, "JEE Main",
               20000, 29000, 46000, 31000, 23000, 37000,
               4.0, 3.0, 10.0, 60, ["VLSI", "IoT", "Embedded"]),
        ],
    ),
]


# ═══════════════════════════════════════════════════════════════════════════
# MEDICAL — TOP 25 INDIA
# ═══════════════════════════════════════════════════════════════════════════

# ── Standard medical course-type sets ─────────────────────────────────────

_GOVT_MED_COURSES = [
    _ct("MBBS", 5.5, "NEET UG", "10+2 PCB, 50% (40% SC/ST)", 0, 0.10),
    _ct("MD", 3, "NEET PG", "MBBS with internship", 0, 0.15),
    _ct("MS", 3, "NEET PG", "MBBS with internship", 0, 0.15),
    _ct("DM", 3, "NEET SS", "MD in relevant specialty", 0, 0.20),
    _ct("MCh", 3, "NEET SS", "MS in relevant specialty", 0, 0.20),
]

_PVT_MED_COURSES = [
    _ct("MBBS", 5.5, "NEET UG", "10+2 PCB, 50%", 0, 12.0),
    _ct("MD", 3, "NEET PG", "MBBS with internship", 0, 8.0),
    _ct("MS", 3, "NEET PG", "MBBS with internship", 0, 8.0),
]

_AIIMS_COURSES = [
    _ct("MBBS", 5.5, "NEET UG", "10+2 PCB, 60%", 0, 0.01),
    _ct("MD", 3, "INI CET", "MBBS with internship", 0, 0.01),
    _ct("MS", 3, "INI CET", "MBBS with internship", 0, 0.01),
    _ct("DM", 3, "INI SS", "MD in relevant specialty", 0, 0.01),
    _ct("MCh", 3, "INI SS", "MS in relevant specialty", 0, 0.01),
    _ct("B.Sc Nursing", 4, "NEET UG", "10+2 PCB, 55%", 0, 0.01),
]


_MEDICAL_DIRECTORY: list[College] = [
    # ── 1. AIIMS New Delhi ─────────────────────────────────────────
    College(
        name="All India Institute of Medical Sciences, New Delhi",
        short_name="AIIMS Delhi", institute_type="Central", established=1956,
        ranking=1, city="New Delhi", state="Delhi",
        nirf_ranking=1, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.01, hostel_fees_per_year=0.005,
        fee_waiver_policy="Virtually free education",
        avg_placement_lpa=15.0, median_placement_lpa=12.0,
        highest_placement_lpa=35.0, placement_percentage=100.0,
        top_recruiters=["AIIMS Hospitals", "Apollo", "Fortis", "Max Healthcare"],
        total_seats=107, website="https://www.aiims.edu",
        notable_alumni=["Dr. Randeep Guleria", "Dr. Devi Shetty"],
        course_types=_AIIMS_COURSES,
        branches=[
            _b("MBBS", "MBBS", 107, 0, 0, "NEET UG",
               1, 50, 250, 150, 70, 100,
               15.0, 12.0, 35.0, 100, ["General Medicine", "Surgery", "Pediatrics"]),
            _b("General Medicine", "MD-Med", 0, 25, 0, "INI CET",
               0, 0, 0, 0, 0, 0,
               25.0, 20.0, 45.0, 100, ["Cardiology", "Pulmonology", "Nephrology"]),
            _b("General Surgery", "MS-Surg", 0, 20, 0, "INI CET",
               0, 0, 0, 0, 0, 0,
               22.0, 18.0, 40.0, 100, ["Gastro Surgery", "Transplant", "Trauma"]),
            _b("Pediatrics", "MD-Peds", 0, 15, 0, "INI CET",
               0, 0, 0, 0, 0, 0,
               18.0, 15.0, 30.0, 100, ["Neonatology", "Pediatric ICU"]),
            _b("Orthopedics", "MS-Ortho", 0, 12, 0, "INI CET",
               0, 0, 0, 0, 0, 0,
               20.0, 17.0, 38.0, 100, ["Joint Replacement", "Spine", "Sports Medicine"]),
            _b("Dermatology", "MD-Derm", 0, 8, 0, "INI CET",
               0, 0, 0, 0, 0, 0,
               22.0, 18.0, 50.0, 100, ["Cosmetic", "Clinical", "Laser"]),
        ],
    ),

    # ── 2. PGIMER Chandigarh ───────────────────────────────────────
    College(
        name="Post Graduate Institute of Medical Education & Research",
        short_name="PGIMER", institute_type="Central", established=1962,
        ranking=2, city="Chandigarh", state="Chandigarh",
        nirf_ranking=2, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.02, hostel_fees_per_year=0.005,
        fee_waiver_policy="Nominal fees, government funded",
        avg_placement_lpa=14.0, median_placement_lpa=11.0,
        highest_placement_lpa=30.0, placement_percentage=100.0,
        top_recruiters=["PGIMER Hospital", "Medanta", "Max Healthcare"],
        total_seats=75, website="https://pgimer.edu.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 75, 0, 0, "NEET UG",
               50, 150, 500, 350, 200, 250,
               14.0, 11.0, 30.0, 100, ["Internal Medicine", "Surgery"]),
            _b("General Medicine", "MD-Med", 0, 20, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               24.0, 19.0, 42.0, 100, ["Cardiology", "Gastro", "Pulmonology"]),
            _b("General Surgery", "MS-Surg", 0, 18, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               20.0, 16.0, 35.0, 100, ["GI Surgery", "Transplant"]),
        ],
    ),

    # ── 3. CMC Vellore ─────────────────────────────────────────────
    College(
        name="Christian Medical College Vellore",
        short_name="CMC Vellore", institute_type="Private", established=1900,
        ranking=3, city="Vellore", state="Tamil Nadu",
        nirf_ranking=3, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.35, hostel_fees_per_year=0.10,
        fee_waiver_policy="Need-based scholarships available",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=28.0, placement_percentage=100.0,
        top_recruiters=["CMC Hospital", "Apollo", "NIMHANS", "Global Hospitals"],
        total_seats=100, website="https://www.cmch-vellore.edu",
        course_types=_PVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 100, 0, 0, "NEET UG",
               80, 300, 900, 600, 350, 500,
               12.0, 10.0, 28.0, 100, ["General Medicine", "Surgery", "Ob-Gyn"]),
            _b("General Medicine", "MD-Med", 0, 18, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               22.0, 18.0, 40.0, 100, ["Cardiology", "Neurology", "Nephrology"]),
            _b("General Surgery", "MS-Surg", 0, 15, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               20.0, 16.0, 35.0, 100, ["GI Surgery", "Urology", "Transplant"]),
        ],
    ),

    # ── 4. JIPMER Puducherry ───────────────────────────────────────
    College(
        name="Jawaharlal Institute of Postgraduate Medical Education & Research",
        short_name="JIPMER", institute_type="Central", established=1823,
        ranking=4, city="Puducherry", state="Puducherry",
        nirf_ranking=5, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.02, hostel_fees_per_year=0.005,
        fee_waiver_policy="Government funded, minimal fees",
        avg_placement_lpa=13.0, median_placement_lpa=10.5,
        highest_placement_lpa=28.0, placement_percentage=100.0,
        top_recruiters=["JIPMER Hospital", "Apollo", "AIIMS"],
        total_seats=200, website="https://www.jipmer.edu.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               100, 400, 1200, 800, 450, 650,
               13.0, 10.5, 28.0, 100, ["General Medicine", "Surgery"]),
            _b("General Medicine", "MD-Med", 0, 15, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               22.0, 17.0, 38.0, 100, ["Cardiology", "Nephrology"]),
        ],
    ),

    # ── 5. NIMHANS Bangalore ───────────────────────────────────────
    College(
        name="National Institute of Mental Health and Neurosciences",
        short_name="NIMHANS", institute_type="Central", established=1974,
        ranking=5, city="Bangalore", state="Karnataka",
        nirf_ranking=4, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.02, hostel_fees_per_year=0.005,
        fee_waiver_policy="Government funded",
        avg_placement_lpa=14.0, median_placement_lpa=11.0,
        highest_placement_lpa=30.0, placement_percentage=100.0,
        top_recruiters=["NIMHANS Hospital", "Apollo", "Manipal Hospitals"],
        total_seats=60, website="https://nimhans.ac.in",
        course_types=[
            _ct("MD Psychiatry", 3, "NEET PG", "MBBS", 0, 0.02),
            _ct("DM Neurology", 3, "NEET SS", "MD Medicine", 0, 0.02),
            _ct("DM Clinical Psychology", 3, "Institute Exam", "MA Psychology", 0, 0.02),
            _ct("MCh Neurosurgery", 3, "NEET SS", "MS Surgery", 0, 0.02),
        ],
        branches=[
            _b("Psychiatry", "MD-Psych", 0, 20, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               16.0, 13.0, 30.0, 100, ["Child Psychiatry", "Addiction", "Forensic"]),
            _b("Neurology", "DM-Neuro", 0, 10, 0, "NEET SS",
               0, 0, 0, 0, 0, 0,
               25.0, 20.0, 45.0, 100, ["Stroke", "Epilepsy", "Movement Disorders"]),
            _b("Neurosurgery", "MCh-NS", 0, 8, 0, "NEET SS",
               0, 0, 0, 0, 0, 0,
               28.0, 22.0, 50.0, 100, ["Spine", "Neuro-oncology", "Vascular"]),
        ],
    ),

    # ── 6. KMC Manipal ─────────────────────────────────────────────
    College(
        name="Kasturba Medical College Manipal",
        short_name="KMC Manipal", institute_type="Private", established=1953,
        ranking=6, city="Manipal", state="Karnataka",
        nirf_ranking=6, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=12.0, hostel_fees_per_year=1.0,
        fee_waiver_policy="Merit scholarships for top rankers",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=25.0, placement_percentage=95.0,
        top_recruiters=["Manipal Hospitals", "Apollo", "Fortis", "Columbia Asia"],
        total_seats=250, website="https://manipal.edu/kmc-manipal.html",
        course_types=_PVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               5000, 15000, 45000, 30000, 18000, 25000,
               10.0, 8.0, 25.0, 95, ["General Medicine", "Surgery", "Pediatrics"]),
            _b("General Medicine", "MD-Med", 0, 20, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               18.0, 15.0, 32.0, 100, ["Cardiology", "Endocrinology"]),
            _b("General Surgery", "MS-Surg", 0, 15, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               16.0, 13.0, 28.0, 100, ["Laparoscopic", "GI Surgery"]),
        ],
    ),

    # ── 7. BHU IMS Varanasi ────────────────────────────────────────
    College(
        name="Institute of Medical Sciences, BHU",
        short_name="IMS BHU", institute_type="Central University", established=1916,
        ranking=7, city="Varanasi", state="Uttar Pradesh",
        nirf_ranking=8, naac_grade="A++", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.01,
        fee_waiver_policy="Tuition waiver for SC/ST/PwD",
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=25.0, placement_percentage=98.0,
        top_recruiters=["BHU Hospital", "AIIMS", "Medanta", "Apollo"],
        total_seats=120, website="https://www.bhu.ac.in/ims",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 120, 0, 0, "NEET UG",
               200, 800, 2500, 1500, 900, 1200,
               11.0, 9.0, 25.0, 98, ["General Medicine", "Surgery", "Ob-Gyn"]),
            _b("General Medicine", "MD-Med", 0, 15, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               20.0, 16.0, 35.0, 100, ["Cardiology", "Gastro"]),
        ],
    ),

    # ── 8. KGMU Lucknow ───────────────────────────────────────────
    College(
        name="King George's Medical University",
        short_name="KGMU", institute_type="State Govt", established=1911,
        ranking=8, city="Lucknow", state="Uttar Pradesh",
        nirf_ranking=10, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.08, hostel_fees_per_year=0.01,
        fee_waiver_policy="State govt subsidized",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=22.0, placement_percentage=97.0,
        top_recruiters=["KGMU Hospital", "Medanta", "Apollo", "Max"],
        total_seats=250, website="https://www.kgmu.org",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               300, 1200, 4000, 2500, 1400, 1800,
               10.0, 8.0, 22.0, 97, ["General Medicine", "Surgery", "Pediatrics"]),
            _b("General Medicine", "MD-Med", 0, 20, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               18.0, 14.0, 30.0, 100, ["Cardiology", "Nephrology"]),
        ],
    ),

    # ── 9. Maulana Azad Medical College ────────────────────────────
    College(
        name="Maulana Azad Medical College",
        short_name="MAMC Delhi", institute_type="State Govt", established=1958,
        ranking=9, city="New Delhi", state="Delhi",
        nirf_ranking=7, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.01,
        fee_waiver_policy="Delhi govt subsidized",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=28.0, placement_percentage=100.0,
        top_recruiters=["Lok Nayak Hospital", "AIIMS", "Safdarjung", "Max"],
        total_seats=250, website="https://www.mamc.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               60, 200, 700, 450, 250, 350,
               12.0, 10.0, 28.0, 100, ["General Medicine", "Surgery", "Ob-Gyn"]),
            _b("General Medicine", "MD-Med", 0, 22, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               22.0, 18.0, 38.0, 100, ["Cardiology", "Pulmonology"]),
            _b("General Surgery", "MS-Surg", 0, 18, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               20.0, 16.0, 35.0, 100, ["Trauma", "GI Surgery"]),
        ],
    ),

    # ── 10. Madras Medical College ─────────────────────────────────
    College(
        name="Madras Medical College",
        short_name="MMC Chennai", institute_type="State Govt", established=1835,
        ranking=10, city="Chennai", state="Tamil Nadu",
        nirf_ranking=9, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.03, hostel_fees_per_year=0.005,
        fee_waiver_policy="TN state govt subsidized",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=22.0, placement_percentage=98.0,
        top_recruiters=["Rajiv Gandhi GH", "Apollo", "MIOT", "Fortis"],
        total_seats=250, website="https://www.mmc.tn.gov.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               150, 600, 2000, 1200, 700, 900,
               10.0, 8.0, 22.0, 98, ["General Medicine", "Surgery"]),
            _b("General Medicine", "MD-Med", 0, 18, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               18.0, 14.0, 30.0, 100, ["Cardiology", "Gastro"]),
        ],
    ),

    # ── 11. Grant Medical College Mumbai ───────────────────────────
    College(
        name="Grant Government Medical College",
        short_name="Grant MC Mumbai", institute_type="State Govt", established=1845,
        ranking=11, city="Mumbai", state="Maharashtra",
        nirf_ranking=15, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.01,
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=22.0, placement_percentage=97.0,
        top_recruiters=["JJ Hospital", "Bombay Hospital", "KEM", "Lilavati"],
        total_seats=200, website="https://www.gmcjjh.org",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               250, 900, 3000, 1800, 1100, 1400,
               10.0, 8.0, 22.0, 97, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 12. Seth GS Medical College Mumbai ─────────────────────────
    College(
        name="Seth GS Medical College & KEM Hospital",
        short_name="KEM Mumbai", institute_type="State Govt", established=1926,
        ranking=12, city="Mumbai", state="Maharashtra",
        nirf_ranking=12, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.01,
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=25.0, placement_percentage=98.0,
        top_recruiters=["KEM Hospital", "Hinduja", "Kokilaben", "Lilavati"],
        total_seats=200, website="https://www.kem.edu",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               200, 800, 2800, 1600, 1000, 1300,
               11.0, 9.0, 25.0, 98, ["General Medicine", "Surgery", "Ob-Gyn"]),
            _b("General Medicine", "MD-Med", 0, 16, 0, "NEET PG",
               0, 0, 0, 0, 0, 0,
               20.0, 16.0, 35.0, 100, ["Cardiology", "Nephrology"]),
        ],
    ),

    # ── 13. AFMC Pune ──────────────────────────────────────────────
    College(
        name="Armed Forces Medical College",
        short_name="AFMC Pune", institute_type="Defence", established=1948,
        ranking=13, city="Pune", state="Maharashtra",
        nirf_ranking=14, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.01, hostel_fees_per_year=0.005,
        fee_waiver_policy="Free for defence candidates",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=25.0, placement_percentage=100.0,
        top_recruiters=["Indian Armed Forces Medical Corps"],
        total_seats=150, website="https://www.afmc.nic.in",
        course_types=[_ct("MBBS", 5.5, "NEET UG + Interview", "10+2 PCB, 60%", 0, 0.01)],
        branches=[
            _b("MBBS", "MBBS", 150, 0, 0, "NEET UG",
               100, 400, 1500, 900, 500, 700,
               12.0, 10.0, 25.0, 100, ["Military Medicine", "Surgery", "Aviation Medicine"]),
        ],
    ),

    # ── 14. Lady Hardinge Medical College ──────────────────────────
    College(
        name="Lady Hardinge Medical College",
        short_name="LHMC Delhi", institute_type="Central", established=1916,
        ranking=14, city="New Delhi", state="Delhi",
        nirf_ranking=16, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.02, hostel_fees_per_year=0.005,
        fee_waiver_policy="Central govt funded",
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=25.0, placement_percentage=99.0,
        top_recruiters=["Smt. Sucheta Kriplani Hospital", "AIIMS", "Safdarjung"],
        total_seats=200, website="https://www.lhmc-hosp.gov.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               70, 250, 800, 500, 300, 400,
               11.0, 9.0, 25.0, 99, ["General Medicine", "Ob-Gyn", "Pediatrics"]),
        ],
    ),

    # ── 15. Stanley Medical College Chennai ────────────────────────
    College(
        name="Stanley Medical College",
        short_name="Stanley MC Chennai", institute_type="State Govt", established=1838,
        ranking=15, city="Chennai", state="Tamil Nadu",
        nirf_ranking=20, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.03, hostel_fees_per_year=0.005,
        avg_placement_lpa=9.0, median_placement_lpa=7.5,
        highest_placement_lpa=20.0, placement_percentage=97.0,
        top_recruiters=["Stanley Hospital", "Apollo", "MIOT"],
        total_seats=250, website="https://www.stanleymedicalcollege.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               200, 700, 2200, 1400, 800, 1100,
               9.0, 7.5, 20.0, 97, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 16. Govt Medical College Trivandrum ────────────────────────
    College(
        name="Government Medical College Thiruvananthapuram",
        short_name="GMC Trivandrum", institute_type="State Govt", established=1951,
        ranking=16, city="Thiruvananthapuram", state="Kerala",
        nirf_ranking=22, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.008,
        avg_placement_lpa=9.5, median_placement_lpa=7.5,
        highest_placement_lpa=22.0, placement_percentage=97.0,
        top_recruiters=["SAT Hospital", "KIMS", "Amrita Hospital"],
        total_seats=250, website="https://www.gmctvm.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               300, 1000, 3500, 2000, 1200, 1600,
               9.5, 7.5, 22.0, 97, ["General Medicine", "Surgery", "Pediatrics"]),
        ],
    ),

    # ── 17. AIIMS Jodhpur ──────────────────────────────────────────
    College(
        name="All India Institute of Medical Sciences Jodhpur",
        short_name="AIIMS Jodhpur", institute_type="Central", established=2012,
        ranking=17, city="Jodhpur", state="Rajasthan",
        nirf_ranking=11, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.01, hostel_fees_per_year=0.005,
        fee_waiver_policy="Virtually free education",
        avg_placement_lpa=12.0, median_placement_lpa=10.0,
        highest_placement_lpa=25.0, placement_percentage=100.0,
        top_recruiters=["AIIMS Jodhpur Hospital", "Fortis", "Medanta"],
        total_seats=125, website="https://www.aiimsjodhpur.edu.in",
        course_types=_AIIMS_COURSES,
        branches=[
            _b("MBBS", "MBBS", 125, 0, 0, "NEET UG",
               150, 600, 2000, 1200, 700, 950,
               12.0, 10.0, 25.0, 100, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 18. AIIMS Bhopal ──────────────────────────────────────────
    College(
        name="All India Institute of Medical Sciences Bhopal",
        short_name="AIIMS Bhopal", institute_type="Central", established=2012,
        ranking=18, city="Bhopal", state="Madhya Pradesh",
        nirf_ranking=13, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=0.01, hostel_fees_per_year=0.005,
        fee_waiver_policy="Virtually free education",
        avg_placement_lpa=11.0, median_placement_lpa=9.0,
        highest_placement_lpa=22.0, placement_percentage=100.0,
        top_recruiters=["AIIMS Bhopal Hospital", "Medanta", "Apollo"],
        total_seats=125, website="https://www.aiimsbhopal.edu.in",
        course_types=_AIIMS_COURSES,
        branches=[
            _b("MBBS", "MBBS", 125, 0, 0, "NEET UG",
               180, 700, 2200, 1400, 800, 1050,
               11.0, 9.0, 22.0, 100, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 19. AIIMS Rishikesh ────────────────────────────────────────
    College(
        name="All India Institute of Medical Sciences Rishikesh",
        short_name="AIIMS Rishikesh", institute_type="Central", established=2012,
        ranking=19, city="Rishikesh", state="Uttarakhand",
        nirf_ranking=17, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.01, hostel_fees_per_year=0.005,
        fee_waiver_policy="Virtually free education",
        avg_placement_lpa=10.5, median_placement_lpa=8.5,
        highest_placement_lpa=20.0, placement_percentage=100.0,
        top_recruiters=["AIIMS Rishikesh Hospital", "Max", "Fortis"],
        total_seats=125, website="https://www.aiims.edu/rishikesh",
        course_types=_AIIMS_COURSES,
        branches=[
            _b("MBBS", "MBBS", 125, 0, 0, "NEET UG",
               200, 750, 2400, 1500, 850, 1100,
               10.5, 8.5, 20.0, 100, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 20. St. John's Medical College ─────────────────────────────
    College(
        name="St. John's Medical College",
        short_name="SJMC Bangalore", institute_type="Private", established=1963,
        ranking=20, city="Bangalore", state="Karnataka",
        nirf_ranking=19, naac_grade="A+", nba_accredited=True,
        avg_fees_lpa=8.0, hostel_fees_per_year=0.80,
        fee_waiver_policy="Need-based scholarships",
        avg_placement_lpa=10.0, median_placement_lpa=8.0,
        highest_placement_lpa=22.0, placement_percentage=96.0,
        top_recruiters=["St. John's Hospital", "Manipal Hospitals", "Apollo"],
        total_seats=150, website="https://www.stjohns.in",
        course_types=_PVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 150, 0, 0, "NEET UG",
               3000, 10000, 30000, 20000, 12000, 16000,
               10.0, 8.0, 22.0, 96, ["General Medicine", "Surgery", "Pediatrics"]),
        ],
    ),

    # ── 21. Osmania Medical College ────────────────────────────────
    College(
        name="Osmania Medical College",
        short_name="OMC Hyderabad", institute_type="State Govt", established=1846,
        ranking=21, city="Hyderabad", state="Telangana",
        nirf_ranking=25, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=0.05, hostel_fees_per_year=0.008,
        avg_placement_lpa=9.0, median_placement_lpa=7.0,
        highest_placement_lpa=20.0, placement_percentage=96.0,
        top_recruiters=["Osmania GH", "NIMS", "Apollo", "Yashoda"],
        total_seats=250, website="https://www.osmania.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               400, 1500, 5000, 3000, 1800, 2500,
               9.0, 7.0, 20.0, 96, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 22. SCB Medical College Cuttack ────────────────────────────
    College(
        name="Shrirama Chandra Bhanja Medical College",
        short_name="SCB Cuttack", institute_type="State Govt", established=1944,
        ranking=22, city="Cuttack", state="Odisha",
        nirf_ranking=28, naac_grade="B++", nba_accredited=True,
        avg_fees_lpa=0.04, hostel_fees_per_year=0.005,
        avg_placement_lpa=8.0, median_placement_lpa=6.5,
        highest_placement_lpa=18.0, placement_percentage=95.0,
        top_recruiters=["SCB Hospital", "KIMS", "Apollo"],
        total_seats=250, website="https://www.scbmch.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 250, 0, 0, "NEET UG",
               500, 2000, 6000, 3500, 2200, 3000,
               8.0, 6.5, 18.0, 95, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 23. JNMC Belgaum ──────────────────────────────────────────
    College(
        name="Jawaharlal Nehru Medical College Belgaum",
        short_name="JNMC Belgaum", institute_type="Private", established=1963,
        ranking=23, city="Belgaum", state="Karnataka",
        nirf_ranking=30, naac_grade="A", nba_accredited=True,
        avg_fees_lpa=6.0, hostel_fees_per_year=0.60,
        avg_placement_lpa=8.0, median_placement_lpa=6.5,
        highest_placement_lpa=18.0, placement_percentage=92.0,
        top_recruiters=["KLES Hospital", "Manipal Hospitals", "Apollo"],
        total_seats=200, website="https://www.jnmc.edu",
        course_types=_PVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               8000, 25000, 60000, 40000, 28000, 35000,
               8.0, 6.5, 18.0, 92, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 24. RIMS Ranchi ────────────────────────────────────────────
    College(
        name="Rajendra Institute of Medical Sciences",
        short_name="RIMS Ranchi", institute_type="State Govt", established=1960,
        ranking=24, city="Ranchi", state="Jharkhand",
        nirf_ranking=35, naac_grade="B+", nba_accredited=True,
        avg_fees_lpa=0.04, hostel_fees_per_year=0.005,
        avg_placement_lpa=7.5, median_placement_lpa=6.0,
        highest_placement_lpa=16.0, placement_percentage=94.0,
        top_recruiters=["RIMS Hospital", "Medica", "Apollo"],
        total_seats=200, website="https://www.rimsranchi.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               600, 2500, 7000, 4000, 2500, 3500,
               7.5, 6.0, 16.0, 94, ["General Medicine", "Surgery"]),
        ],
    ),

    # ── 25. Patna Medical College ──────────────────────────────────
    College(
        name="Patna Medical College & Hospital",
        short_name="PMCH Patna", institute_type="State Govt", established=1925,
        ranking=25, city="Patna", state="Bihar",
        nirf_ranking=38, naac_grade="B+", nba_accredited=True,
        avg_fees_lpa=0.03, hostel_fees_per_year=0.005,
        avg_placement_lpa=7.0, median_placement_lpa=5.5,
        highest_placement_lpa=15.0, placement_percentage=93.0,
        top_recruiters=["PMCH Hospital", "AIIMS Patna", "Mahavir Hospital"],
        total_seats=200, website="https://www.pmch-bih.ac.in",
        course_types=_GOVT_MED_COURSES,
        branches=[
            _b("MBBS", "MBBS", 200, 0, 0, "NEET UG",
               700, 3000, 8000, 5000, 3000, 4000,
               7.0, 5.5, 15.0, 93, ["General Medicine", "Surgery"]),
        ],
    ),
]


# ═══════════════════════════════════════════════════════════════════════════
# ACCESSOR FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_college_directory(stream: str = "all") -> list[College]:
    """Return full college directory, optionally filtered by stream."""
    if stream == "engineering":
        return _ENGINEERING_DIRECTORY
    if stream == "medical":
        return _MEDICAL_DIRECTORY
    if stream == "iiit":
        return _IIIT_DIRECTORY
    return _ENGINEERING_DIRECTORY + _MEDICAL_DIRECTORY + _IIIT_DIRECTORY


def get_college_streams() -> list[str]:
    """Return available streams in the college directory."""
    streams = ["engineering"]
    if _MEDICAL_DIRECTORY:
        streams.append("medical")
    if _IIIT_DIRECTORY:
        streams.append("iiit")
    return streams


def get_college_by_state(state: str, stream: str = "all") -> list[College]:
    """Return colleges in a given state."""
    colleges = get_college_directory(stream)
    return [c for c in colleges if c.state.lower() == state.lower()]


def get_college_by_type(institute_type: str, stream: str = "all") -> list[College]:
    """Return colleges of a given institute type (IIT, NIT, etc.)."""
    colleges = get_college_directory(stream)
    return [c for c in colleges if c.institute_type.lower() == institute_type.lower()]


def get_college_by_branch(branch_short: str, stream: str = "all") -> list[College]:
    """Return colleges offering a specific branch."""
    colleges = get_college_directory(stream)
    return [c for c in colleges
            if any(b.short_name.lower() == branch_short.lower() for b in c.branches)]


def get_all_branches(stream: str = "all") -> list[str]:
    """Return sorted unique branch short names across all colleges."""
    colleges = get_college_directory(stream)
    shorts: set[str] = set()
    for c in colleges:
        for b in c.branches:
            shorts.add(b.short_name)
    return sorted(shorts)


def get_all_institute_types(stream: str = "all") -> list[str]:
    """Return sorted unique institute types."""
    colleges = get_college_directory(stream)
    return sorted({c.institute_type for c in colleges})


def get_all_college_states(stream: str = "all") -> list[str]:
    """Return sorted unique states from college directory."""
    colleges = get_college_directory(stream)
    return sorted({c.state for c in colleges})
