"""Special admission criteria data for Indian colleges."""

from __future__ import annotations


def get_admission_categories() -> list[dict]:
    """Return all special admission categories with criteria and sources."""
    return _ADMISSION_CATEGORIES


def get_documents_checklist() -> list[dict]:
    """Return the key documents checklist for special admissions."""
    return _DOCUMENTS_CHECKLIST


# ── Documents Checklist ───────────────────────────────────────────────

_DOCUMENTS_CHECKLIST: list[dict] = [
    {"name": "Board Marksheets", "detail": "10th & 12th (original + attested copies)"},
    {"name": "Category Certificate", "detail": "SC/ST/OBC/EWS from competent authority"},
    {"name": "Domicile Certificate", "detail": "From district magistrate / tehsildar"},
    {"name": "PwD Certificate", "detail": "UDID card (if applicable)"},
    {"name": "Income Certificate", "detail": "For EWS / fee waiver eligibility"},
    {"name": "Sports Certificate", "detail": "SAI grading / federation certificate"},
    {"name": "NCC Certificate", "detail": "A/B/C certificate (original)"},
    {"name": "Olympiad Certificates", "detail": "HBCSE / stage-level proof"},
    {"name": "Defence Dependent Card", "detail": "If applicable"},
    {"name": "Migration Certificate", "detail": "From previous board/university"},
    {"name": "Passport-size Photographs", "detail": "20+ copies (recent)"},
    {"name": "Aadhaar Card", "detail": "For identity verification"},
]


# ── Admission Categories ─────────────────────────────────────────────

_ADMISSION_CATEGORIES: list[dict] = [
    {
        "id": "academic_merit",
        "title": "Academic Merit & Topper Quotas",
        "icon": "🏅",
        "criteria": [
            {
                "name": "State Board Topper",
                "description": "1st rank in state board exams (10th or 12th)",
                "institutions": ["IITs (supernumerary)", "NITs", "State Universities"],
            },
            {
                "name": "CBSE/ICSE Top 0.1%",
                "description": "National-level board toppers",
                "institutions": ["Select IITs", "NITs", "Central Universities"],
            },
            {
                "name": "KVPY Fellow",
                "description": "Kishore Vaigyanik Protsahan Yojana fellowship holder",
                "institutions": ["IISc Bangalore (direct)", "IISERs (direct)"],
            },
            {
                "name": "INSPIRE Scholar",
                "description": "DST INSPIRE scholarship awardee",
                "institutions": ["IISERs", "Central Universities"],
            },
            {
                "name": "NTSE Scholar",
                "description": "National Talent Search Exam awardee",
                "institutions": ["Scholarship support", "Some universities give preference"],
            },
            {
                "name": "Gold Medalist",
                "description": "University gold medal in UG programme",
                "institutions": ["Direct PG admission at select institutions"],
            },
        ],
        "certificates": [
            "Board marksheet",
            "KVPY award letter",
            "INSPIRE certificate",
            "NTSE certificate",
        ],
        "sources": [
            {"name": "KVPY", "url": "https://kvpy.iisc.ac.in"},
            {"name": "INSPIRE", "url": "https://online-inspire.gov.in"},
            {"name": "NTSE (NCERT)", "url": "https://ncert.nic.in/national-talent-examination.php"},
            {"name": "CBSE Results", "url": "https://cbseresults.nic.in"},
        ],
    },
    {
        "id": "olympiad",
        "title": "Olympiad & Competition Routes",
        "icon": "🧪",
        "criteria": [
            {
                "name": "International Olympiad Medal",
                "description": "Medal at IMO, IPhO, IChO, IBO, or IOI",
                "institutions": ["IITs (direct admission)", "IISc", "IISERs"],
            },
            {
                "name": "National Olympiad Finalist",
                "description": "Stage finalist in INPhO, INMO, INChO, INBO, INOI",
                "institutions": ["IISERs (direct entry via SCB channel)"],
            },
            {
                "name": "Regional Olympiad Qualifier",
                "description": "State-level Olympiad qualifier (RMO, NSEP, etc.)",
                "institutions": ["Some state universities give weightage"],
            },
            {
                "name": "IOQM / RMO",
                "description": "Indian Olympiad Qualifier in Mathematics / Regional Math Olympiad",
                "institutions": ["IISERs (aptitude channel shortlist)"],
            },
        ],
        "certificates": [
            "Olympiad medal/certificate",
            "HBCSE participation letter",
            "Camp selection proof",
        ],
        "sources": [
            {"name": "HBCSE Olympiad Programme", "url": "https://olympiads.hbcse.tifr.res.in"},
            {"name": "IISc Admissions", "url": "https://iisc.ac.in/admissions"},
            {"name": "IISER Admissions", "url": "https://www.iiseradmission.in"},
        ],
    },
    {
        "id": "sports",
        "title": "Sports Quota",
        "icon": "⚽",
        "criteria": [
            {
                "name": "International Representation",
                "description": "Represented India in Olympics, Asian Games, CWG, World Championships",
                "institutions": ["IITs", "NITs", "Central & State Universities (supernumerary)"],
            },
            {
                "name": "National Level (Senior/Junior)",
                "description": "Medal in Senior/Junior National Championship",
                "institutions": ["NITs (2% supernumerary)", "DU", "State Universities"],
            },
            {
                "name": "Khelo India Athlete",
                "description": "Selected for Khelo India programme",
                "institutions": ["State Universities", "SAI-affiliated institutions"],
            },
            {
                "name": "State Level",
                "description": "Medal in State-level championship",
                "institutions": ["State Universities", "Some deemed universities"],
            },
            {
                "name": "National Sports Award Winner",
                "description": "Arjuna, Dronacharya, or Rajiv Gandhi Khel Ratna awardee",
                "institutions": ["IITs", "NITs (direct supernumerary)"],
            },
        ],
        "certificates": [
            "SAI grading certificate",
            "Sports federation participation certificate",
            "Khelo India ID",
        ],
        "sources": [
            {"name": "Sports Authority of India", "url": "https://sfrdi.nic.in"},
            {"name": "Khelo India", "url": "https://kheloindia.gov.in"},
            {"name": "JoSAA Sports Quota", "url": "https://josaa.nic.in"},
        ],
    },
    {
        "id": "defence",
        "title": "Defence & Paramilitary Quotas",
        "icon": "🎖️",
        "criteria": [
            {
                "name": "Ward of Defence Personnel",
                "description": "Son/daughter of serving/retired/deceased defence personnel",
                "institutions": ["NITs (5% seats)", "Sainik Schools", "Defence colleges"],
            },
            {
                "name": "Ward of Gallantry Award Winner",
                "description": "Parent received Param Vir Chakra, Maha Vir Chakra, Vir Chakra, etc.",
                "institutions": ["IITs (supernumerary)", "NITs", "State Universities"],
            },
            {
                "name": "War Widow / Disabled Soldier Ward",
                "description": "Child of personnel killed or disabled in action",
                "institutions": ["Central & State Universities (priority)"],
            },
            {
                "name": "Ward of Ex-Servicemen",
                "description": "Child of ex-servicemen (any rank)",
                "institutions": ["State government institutions", "Polytechnics"],
            },
            {
                "name": "Paramilitary Ward",
                "description": "Child of CRPF, BSF, CISF, ITBP, SSB personnel",
                "institutions": ["Some central universities", "State quota"],
            },
        ],
        "certificates": [
            "Defence service certificate",
            "Dependent card",
            "Canteen card",
            "ESM certificate",
        ],
        "sources": [
            {"name": "DESW", "url": "https://desw.gov.in"},
            {"name": "Kendriya Sainik Board", "url": "https://ksb.gov.in"},
            {"name": "JoSAA Defence Quota", "url": "https://josaa.nic.in"},
        ],
    },
    {
        "id": "cultural",
        "title": "Cultural & Creative Talent (ECA Quota)",
        "icon": "🎭",
        "criteria": [
            {
                "name": "ECA Quota",
                "description": "Extra Curricular Activity quota in Music, Dance, Theatre, Fine Arts",
                "institutions": ["Delhi University", "JNU", "BHU", "AMU"],
            },
            {
                "name": "National Cultural Award",
                "description": "Recognised by Sangeet Natak Akademi or Lalit Kala Akademi",
                "institutions": ["Central Universities", "NSD", "FTII"],
            },
            {
                "name": "Bal Shakti Puraskar",
                "description": "National-level child prodigy recognition by Govt. of India",
                "institutions": ["Some central universities (preference)"],
            },
        ],
        "certificates": [
            "ECA certificates from recognised bodies",
            "Award citations",
            "Performance records / portfolio",
        ],
        "sources": [
            {"name": "Delhi University ECA", "url": "https://www.du.ac.in"},
            {"name": "Sangeet Natak Akademi", "url": "https://www.sangeetnatak.gov.in"},
            {"name": "National School of Drama", "url": "https://nsd.gov.in"},
        ],
    },
    {
        "id": "ncc_nss",
        "title": "NCC & NSS Quotas",
        "icon": "🏛️",
        "criteria": [
            {
                "name": "NCC 'C' Certificate Holder",
                "description": "Completed NCC Senior Division C certificate",
                "institutions": ["NITs (bonus marks)", "DU", "State Universities", "UPSC (bonus)"],
            },
            {
                "name": "NCC 'B' Certificate",
                "description": "Completed NCC B certificate",
                "institutions": ["Some state universities", "Polytechnics"],
            },
            {
                "name": "Republic Day Parade (NCC)",
                "description": "Participated in Republic Day camp / parade as NCC cadet",
                "institutions": ["Additional preference in NCC quota"],
            },
            {
                "name": "NSS National Award",
                "description": "Received NSS National Award by President of India",
                "institutions": ["Central Universities (preference)"],
            },
            {
                "name": "NSS Volunteer (240+ hours)",
                "description": "Completed NSS programme with 240+ service hours",
                "institutions": ["Some state universities (bonus marks)"],
            },
        ],
        "certificates": [
            "NCC A/B/C certificate (original)",
            "RD camp certificate",
            "NSS completion certificate",
        ],
        "sources": [
            {"name": "NCC Directorate", "url": "https://indiancc.nic.in"},
            {"name": "NSS", "url": "https://nss.gov.in"},
            {"name": "UPSC NCC Benefits", "url": "https://upsc.gov.in"},
        ],
    },
    {
        "id": "pwd_ews",
        "title": "Differently-Abled (PwD) & EWS",
        "icon": "♿",
        "criteria": [
            {
                "name": "PwD (Persons with Disabilities)",
                "description": "5% horizontal reservation for candidates with 40%+ disability",
                "institutions": ["All central govt institutions (IITs, NITs, IIITs, Central Universities)"],
            },
            {
                "name": "EWS (Economically Weaker Section)",
                "description": "10% reservation for families with income < ₹8 LPA",
                "institutions": ["All central govt institutions"],
            },
            {
                "name": "Single Girl Child",
                "description": "Supernumerary seat for the single girl child of a family",
                "institutions": ["NITs", "IIITs (via CSAB)", "Some state universities"],
            },
            {
                "name": "Transgender Quota",
                "description": "Reserved seats for transgender students (varies by state)",
                "institutions": ["Some state universities"],
            },
        ],
        "certificates": [
            "PwD certificate (UDID card)",
            "EWS certificate from tehsildar",
            "Single girl child affidavit",
        ],
        "sources": [
            {"name": "UDID Portal (PwD)", "url": "https://www.swavlambancard.gov.in"},
            {"name": "CSAB (Single Girl Child)", "url": "https://csab.nic.in"},
            {"name": "JoSAA PwD/EWS", "url": "https://josaa.nic.in"},
        ],
    },
    {
        "id": "domicile",
        "title": "Domicile & Regional Quotas",
        "icon": "🗺️",
        "criteria": [
            {
                "name": "Home State Quota (50%)",
                "description": "50% seats reserved for home-state students at NITs",
                "institutions": ["All NITs"],
            },
            {
                "name": "J&K / Ladakh Supernumerary",
                "description": "2 supernumerary seats per NIT for J&K/Ladakh domicile students",
                "institutions": ["All NITs", "Some IITs"],
            },
            {
                "name": "North-East (NE) Quota",
                "description": "Reserved seats for NE state domicile students",
                "institutions": ["IITs (supernumerary)", "NITs", "Central Universities"],
            },
            {
                "name": "Kashmiri Migrant (KM)",
                "description": "1 supernumerary seat per NIT for Kashmiri migrants",
                "institutions": ["All NITs", "Some IITs"],
            },
            {
                "name": "Domicile Reservation (State Govt)",
                "description": "70–85% seats reserved for home-state students in state institutions",
                "institutions": ["State Universities", "State engineering/medical colleges"],
            },
        ],
        "certificates": [
            "Domicile certificate",
            "State residency proof",
            "Migration certificate",
        ],
        "sources": [
            {"name": "JoSAA (Home State)", "url": "https://josaa.nic.in"},
            {"name": "CSAB Supernumerary", "url": "https://csab.nic.in"},
        ],
    },
    {
        "id": "international_special",
        "title": "International & Special Entry Routes",
        "icon": "🌍",
        "criteria": [
            {
                "name": "DASA",
                "description": "Direct Admission of Students Abroad — for NRI/PIO/OCI/foreign nationals",
                "institutions": ["NITs", "IIITs", "Other centrally-funded institutions"],
            },
            {
                "name": "ICCR Scholarship",
                "description": "Indian Council for Cultural Relations scholarship for foreign students",
                "institutions": ["Central Universities (JNU, DU, BHU, etc.)"],
            },
            {
                "name": "Ward of Freedom Fighter",
                "description": "Descendant of a recognised freedom fighter",
                "institutions": ["Some state universities (reservation in state quota)"],
            },
            {
                "name": "Central Govt Employee Ward",
                "description": "Child of central government employee with transferable job",
                "institutions": ["KVS priority", "Some state reservation"],
            },
            {
                "name": "Tuition Fee Waiver",
                "description": "Free/reduced tuition for SC/ST/OBC/EWS categories",
                "institutions": ["IITs (full waiver for SC/ST/PwD)", "NITs", "Central Universities"],
            },
        ],
        "certificates": [
            "DASA eligibility documents (passport, visa)",
            "ICCR nomination letter",
            "Freedom fighter certificate",
            "Central govt service certificate",
        ],
        "sources": [
            {"name": "DASA", "url": "https://dasanit.org"},
            {"name": "ICCR", "url": "https://www.iccr.gov.in"},
        ],
    },
]
