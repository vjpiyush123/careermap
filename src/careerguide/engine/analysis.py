"""Deterministic analysis engine — pure functions, no LLM involvement.

Core invariant: same input → same output. Always.
"""

from __future__ import annotations

from careerguide.data.career_data import (
    get_career_options,
    get_coaching_institutes,
    get_entrance_exams,
    get_industries,
    get_stream_data,
    get_stream_growth,
    get_top_colleges_by_state,
    get_top_colleges_india,
)
from careerguide.models.analysis import (
    AnalysisResult,
    CollegeRecommendation,
    StreamAnalysis,
)
from careerguide.models.student import StudentProfile


def _compute_suitability_score(
    profile: StudentProfile,
    stream_name: str,
    psychology_scores: dict[str, float] | None,
) -> float:
    """Compute a deterministic suitability score (0–100) for a student + stream.

    Scoring components:
    - Academic performance (40%): based on percentage marks
    - Stream alignment (30%): is the selected stream the student's declared interest?
    - Psychology alignment (30%): psychology test aptitude score for this stream
    """
    # Academic performance score (0–100)
    marks = profile.percentage_10th
    if profile.percentage_12th is not None:
        marks = (profile.percentage_10th + profile.percentage_12th) / 2.0
    academic_score = min(marks, 100.0)

    # Stream alignment (binary: 100 if matches interest, 50 otherwise)
    stream_alignment = 100.0 if profile.stream_interest.value == stream_name else 50.0

    # Psychology alignment (0–100 or 50 if not taken)
    psych_score = 50.0
    if psychology_scores and stream_name in psychology_scores:
        psych_score = psychology_scores[stream_name]

    total = (academic_score * 0.4) + (stream_alignment * 0.3) + (psych_score * 0.3)
    return round(min(total, 100.0), 1)


def _generate_pros(stream_name: str, suitability: float) -> list[str]:
    """Generate deterministic pros based on stream data."""
    growth = get_stream_growth(stream_name)
    pros: list[str] = []

    if suitability >= 70:
        pros.append(f"Strong suitability score ({suitability}/100) indicates good alignment")
    if "Very High" in growth.get("india", ""):
        pros.append(f"Very high growth potential in India: {growth['india'][:80]}")
    elif "High" in growth.get("india", ""):
        pros.append(f"High growth potential in India")
    if "Very High" in growth.get("abroad", ""):
        pros.append("Excellent international career opportunities")
    elif "High" in growth.get("abroad", ""):
        pros.append("Good international career opportunities")

    options = get_career_options(stream_name)
    if options:
        high_salary = [o for o in options if o.avg_starting_salary_lpa >= 6.0]
        if high_salary:
            pros.append(f"High starting salaries (up to ₹{max(o.avg_starting_salary_lpa for o in options):.1f} LPA)")
        pros.append(f"Multiple career paths available ({len(options)} options)")

    return pros if pros else ["Career stream is available for exploration"]


def _generate_cons(stream_name: str, profile: StudentProfile, suitability: float) -> list[str]:
    """Generate deterministic cons based on profile and stream."""
    cons: list[str] = []

    if suitability < 50:
        cons.append(f"Low suitability score ({suitability}/100) — may not be the best fit")
    elif suitability < 70:
        cons.append(f"Moderate suitability ({suitability}/100) — consider exploring alternatives")

    marks = profile.percentage_10th
    if profile.percentage_12th is not None:
        marks = (profile.percentage_10th + profile.percentage_12th) / 2.0

    if marks < 60:
        cons.append("Academic performance may limit options at top institutions")

    stream_data = get_stream_data(stream_name)
    if stream_data:
        entrance = stream_data.get("entrance_exams", [])
        if len(entrance) > 2:
            cons.append(f"Competitive entrance exams required ({', '.join(entrance[:3])})")

    growth = get_stream_growth(stream_name)
    if "Limited" in growth.get("abroad", "") or "N/A" in growth.get("abroad", ""):
        cons.append("Limited international career opportunities")
    if "Moderate" in growth.get("india", ""):
        cons.append("Moderate growth outlook in India")

    return cons if cons else ["No significant disadvantages identified"]


def analyze_stream(
    profile: StudentProfile,
    stream_name: str,
) -> StreamAnalysis:
    """Produce a deterministic analysis for one stream.

    This is a pure function. No LLM, no network calls.
    Same input → same output.
    """
    psychology_scores = profile.psychology_score

    suitability = _compute_suitability_score(profile, stream_name, psychology_scores)
    career_options = get_career_options(stream_name)
    industries = get_industries(stream_name)
    growth = get_stream_growth(stream_name)
    colleges_india = get_top_colleges_india(stream_name)
    coaching = get_coaching_institutes(stream_name)
    entrance_exams = get_entrance_exams(stream_name)
    stream_data = get_stream_data(stream_name) or {}
    subjects_10th = stream_data.get("10th_subjects", [])
    subjects_12th = stream_data.get("12th_subjects", [])

    # College recommendations
    college_recs: list[CollegeRecommendation] = []
    for c in colleges_india:
        college_recs.append(CollegeRecommendation(
            college_name=c.name,
            ranking=c.ranking,
            city=c.city,
            state=c.state,
            avg_fees_lpa=c.avg_fees_lpa,
            avg_placement_lpa=c.avg_placement_lpa,
            total_seats=c.total_seats,
            website=c.website,
            top_companies_hiring=[],
        ))

    # State-specific colleges
    state_colleges = get_top_colleges_by_state(stream_name, profile.state)
    for c in state_colleges:
        if not any(cr.college_name == c.name for cr in college_recs):
            college_recs.append(CollegeRecommendation(
                college_name=c.name,
                ranking=c.ranking,
                city=c.city,
                state=c.state,
                avg_fees_lpa=c.avg_fees_lpa,
                avg_placement_lpa=c.avg_placement_lpa,
                total_seats=c.total_seats,
                website=c.website,
                top_companies_hiring=[],
            ))

    avg_salary = 0.0
    if career_options:
        avg_salary = round(
            sum(co.avg_starting_salary_lpa for co in career_options) / len(career_options),
            1,
        )

    return StreamAnalysis(
        stream_name=stream_name,
        suitability_score=suitability,
        career_options=[co.name for co in career_options],
        industries=industries,
        pros=_generate_pros(stream_name, suitability),
        cons=_generate_cons(stream_name, profile, suitability),
        growth_india=growth.get("india", ""),
        growth_abroad=growth.get("abroad", ""),
        top_colleges=college_recs,
        coaching_institutes=coaching,
        avg_starting_salary_lpa=avg_salary,
        subjects_10th=subjects_10th,
        subjects_12th=subjects_12th,
        entrance_exams=entrance_exams,
    )


def run_analysis(profile: StudentProfile) -> AnalysisResult:
    """Run deterministic analysis for a student profile.

    Analyses the student's selected stream of interest.
    Returns complete result with top-2 stream recommendations.
    """
    selected_stream = profile.stream_interest.value
    stream_analysis = analyze_stream(profile, selected_stream)

    # Compute top-2 recommendations by scoring all streams
    from careerguide.data.career_data import get_all_stream_names

    all_scores: list[tuple[str, float]] = []
    for stream in get_all_stream_names():
        score = _compute_suitability_score(profile, stream, profile.psychology_score)
        all_scores.append((stream, score))

    all_scores.sort(key=lambda x: x[1], reverse=True)
    top_2 = [s[0] for s in all_scores[:2]]

    # Data sufficiency check
    data_sufficient = True
    insufficient_reason = None
    if profile.percentage_10th <= 0:
        data_sufficient = False
        insufficient_reason = "10th percentage marks are required for analysis"
    if profile.standard.value == "12th" and profile.percentage_12th is None:
        data_sufficient = False
        insufficient_reason = "12th percentage marks are required for 12th standard students"

    return AnalysisResult(
        student_id=profile.id,
        student_name=profile.name,
        standard=profile.standard.value,
        board=profile.board.value,
        state=profile.state,
        percentage_10th=profile.percentage_10th,
        percentage_12th=profile.percentage_12th,
        selected_stream=selected_stream,
        stream_analysis=stream_analysis,
        top_2_recommendations=top_2,
        psychology_alignment=profile.psychology_score,
        data_sufficient=data_sufficient,
        insufficient_data_reason=insufficient_reason,
    )
