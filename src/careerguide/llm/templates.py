"""Template-based fallback narratives when LLM is unavailable.

These produce human-readable text from deterministic analysis results,
ensuring zero loss of analytical accuracy.
"""

from __future__ import annotations

from careerguide.models.analysis import AnalysisResult, LLMEnrichedReport


def generate_executive_summary(result: AnalysisResult) -> str:
    """Produce a template-based executive summary."""
    sa = result.stream_analysis
    lines = [
        f"Career Analysis Report for {result.student_name}",
        f"{'=' * 50}",
        "",
        f"Student: {result.student_name}",
        f"Standard: {result.standard} | Board: {result.board} | State: {result.state}",
        f"10th Percentage: {result.percentage_10th}%",
    ]
    if result.percentage_12th is not None:
        lines.append(f"12th Percentage: {result.percentage_12th}%")
    lines.extend([
        "",
        f"Selected Stream: {sa.stream_name}",
        f"Suitability Score: {sa.suitability_score}/100",
        "",
    ])
    if not result.data_sufficient:
        lines.append(f"⚠ Data Insufficiency: {result.insufficient_data_reason}")
        lines.append("")
    if result.top_2_recommendations:
        lines.append(f"Top Recommended Streams: {', '.join(result.top_2_recommendations)}")
    return "\n".join(lines)


def generate_stream_recommendation(result: AnalysisResult) -> str:
    """Produce a template-based stream recommendation narrative."""
    sa = result.stream_analysis
    lines = [
        f"Stream Recommendation: {sa.stream_name}",
        f"{'-' * 40}",
        "",
        f"Based on the analysis, {result.student_name} has a suitability score of "
        f"{sa.suitability_score}/100 for {sa.stream_name}.",
        "",
        "Strengths:",
    ]
    for pro in sa.pros:
        lines.append(f"  ✓ {pro}")
    lines.extend(["", "Considerations:"])
    for con in sa.cons:
        lines.append(f"  • {con}")
    lines.extend([
        "",
        "Career Options:",
    ])
    for opt in sa.career_options:
        lines.append(f"  → {opt}")
    lines.extend([
        "",
        f"Average Starting Salary: ₹{sa.avg_starting_salary_lpa} LPA",
        "",
        "Industries:",
        "  " + ", ".join(sa.industries) if sa.industries else "  Not specified",
    ])
    return "\n".join(lines)


def generate_career_guidance(result: AnalysisResult) -> str:
    """Produce a template-based career guidance narrative with step-by-step roadmap."""
    sa = result.stream_analysis
    lines = [
        "Career Guidance & Step-by-Step Roadmap",
        f"{'-' * 40}",
        "",
        f"Here is your personalised roadmap to pursue {sa.stream_name}:",
        "",
        "STEP 1 — Subjects to Focus On",
    ]
    if sa.subjects_10th:
        lines.append(f"  10th Standard: {', '.join(sa.subjects_10th)}")
    if sa.subjects_12th:
        lines.append(f"  12th Standard: {', '.join(sa.subjects_12th)}")
    if not sa.subjects_10th and not sa.subjects_12th:
        lines.append("  Focus on core subjects relevant to your stream")

    lines.extend(["", "STEP 2 — Entrance Exams to Prepare For"])
    if sa.entrance_exams:
        for i, exam in enumerate(sa.entrance_exams, 1):
            lines.append(f"  {i}. {exam}")
    else:
        lines.append("  Check stream-specific entrance requirements")

    lines.extend(["", "STEP 3 — Top Coaching Institutes for Preparation"])
    if sa.coaching_institutes:
        for inst in sa.coaching_institutes:
            lines.append(f"  • {inst}")
    else:
        lines.append("  Self-study or local coaching recommended")

    lines.extend(["", "STEP 4 — Top Colleges to Target"])
    for i, c in enumerate(sa.top_colleges[:10], 1):
        fee_str = f"₹{c.avg_fees_lpa} LPA" if c.avg_fees_lpa else "N/A"
        placement_str = f"₹{c.avg_placement_lpa} LPA" if c.avg_placement_lpa else "N/A"
        lines.append(
            f"  {i}. {c.college_name} (Rank #{c.ranking}) — {c.city}, {c.state} | "
            f"Fees: {fee_str} | Placement: {placement_str} | Seats: {c.total_seats}"
        )

    lines.extend([
        "",
        "STEP 5 — Career Opportunities After Graduation",
    ])
    if sa.career_options:
        for opt in sa.career_options:
            lines.append(f"  → {opt}")
        lines.append(f"  Average Starting Salary: ₹{sa.avg_starting_salary_lpa} LPA")

    lines.extend([
        "",
        "Growth Outlook:",
        f"  India: {sa.growth_india}",
        f"  Abroad: {sa.growth_abroad}",
    ])
    return "\n".join(lines)


def generate_dependency_explanation(result: AnalysisResult) -> str:
    """Produce a template-based dependency/impact explanation."""
    sa = result.stream_analysis
    lines = [
        "Analysis Methodology & Dependencies",
        f"{'-' * 40}",
        "",
        "This analysis is based on:",
        f"  1. Academic performance: {result.percentage_10th}% (10th)",
    ]
    if result.percentage_12th is not None:
        lines.append(f"     {result.percentage_12th}% (12th)")
    lines.append(f"  2. Stream of interest: {sa.stream_name}")
    if result.psychology_alignment:
        psych_score = result.psychology_alignment.get(sa.stream_name, 0)
        lines.append(f"  3. Psychology aptitude score: {psych_score}/100 for {sa.stream_name}")
    else:
        lines.append("  3. Psychology test: Not taken (default alignment assumed)")
    lines.extend([
        "",
        "Scoring Formula:",
        "  Suitability = (Academic × 40%) + (Interest Alignment × 30%) + (Psychology × 30%)",
        "",
        "Note: This is a deterministic assessment based on available data. "
        "The system does not make authoritative decisions — it supports "
        "human judgment with data-driven insights.",
    ])
    return "\n".join(lines)


def generate_template_report(result: AnalysisResult) -> LLMEnrichedReport:
    """Generate a complete template-based report (fallback when LLM is unavailable)."""
    return LLMEnrichedReport(
        analysis_id=result.id,
        executive_summary=generate_executive_summary(result),
        stream_recommendation_narrative=generate_stream_recommendation(result),
        career_guidance_narrative=generate_career_guidance(result),
        dependency_explanation=generate_dependency_explanation(result),
        source="template_fallback",
    )
