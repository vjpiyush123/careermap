"""Service layer — orchestrates data, engine, LLM, and persistence."""

from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from careerguide.data import compute_psychology_scores, get_psychology_test
from careerguide.db.crud import (
    create_student,
    get_analysis,
    get_dashboard_stats,
    get_report_for_analysis,
    get_student,
    list_all_analyses,
    list_analyses_for_student,
    list_students,
    save_analysis,
    save_report,
    update_student_psychology,
)
from careerguide.engine.analysis import run_analysis
from careerguide.llm.pipeline import run_llm_pipeline
from careerguide.models.analysis import AnalysisResult, FullReport, LLMEnrichedReport
from careerguide.models.psychology import PsychologyTest
from careerguide.models.student import (
    PsychologyResult,
    PsychologyTestSubmission,
    StudentProfile,
    StudentProfileCreate,
)

logger = logging.getLogger(__name__)


# ─── Student service ───────────────────────────────────────────────────

async def create_student_profile(
    session: AsyncSession,
    data: StudentProfileCreate,
) -> StudentProfile:
    return await create_student(session, data)


async def get_student_profile(
    session: AsyncSession,
    student_id: str,
) -> StudentProfile | None:
    return await get_student(session, student_id)


async def list_student_profiles(session: AsyncSession) -> list[StudentProfile]:
    return await list_students(session)


# ─── Psychology service ────────────────────────────────────────────────

def get_psychology_test_data() -> PsychologyTest:
    return get_psychology_test()


async def submit_psychology_test(
    session: AsyncSession,
    submission: PsychologyTestSubmission,
) -> PsychologyResult:
    answers = [(a.question_id, a.selected_option) for a in submission.answers]
    scores = compute_psychology_scores(answers)

    # Determine top streams
    sorted_streams = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    recommended = [s[0] for s in sorted_streams[:3]]

    # Update student profile with psychology scores
    await update_student_psychology(session, submission.student_id, scores)

    return PsychologyResult(
        student_id=submission.student_id,
        scores=scores,
        recommended_streams=recommended,
    )


# ─── Analysis service ──────────────────────────────────────────────────

async def run_student_analysis(
    session: AsyncSession,
    student_id: str,
) -> AnalysisResult:
    """Run deterministic analysis for a student and persist the results."""
    profile = await get_student(session, student_id)
    if profile is None:
        raise ValueError(f"Student not found: {student_id}")

    result = run_analysis(profile)
    await save_analysis(session, result)
    return result


async def generate_full_report(
    session: AsyncSession,
    analysis_id: str,
) -> FullReport:
    """Generate the full report (deterministic + LLM narratives)."""
    analysis = await get_analysis(session, analysis_id)
    if analysis is None:
        raise ValueError(f"Analysis not found: {analysis_id}")

    # Check if report already exists
    existing = await get_report_for_analysis(session, analysis_id)
    if existing is not None:
        return FullReport(analysis=analysis, enrichment=existing)

    # Run LLM pipeline (falls back to templates if unavailable)
    enrichment = await run_llm_pipeline(analysis)
    await save_report(session, enrichment)

    return FullReport(analysis=analysis, enrichment=enrichment)


async def get_existing_report(
    session: AsyncSession,
    analysis_id: str,
) -> FullReport | None:
    """Retrieve an existing report if available."""
    analysis = await get_analysis(session, analysis_id)
    if analysis is None:
        return None
    enrichment = await get_report_for_analysis(session, analysis_id)
    if enrichment is None:
        return None
    return FullReport(analysis=analysis, enrichment=enrichment)


async def get_student_analyses(
    session: AsyncSession,
    student_id: str,
) -> list[AnalysisResult]:
    return await list_analyses_for_student(session, student_id)


async def get_all_reports(session: AsyncSession) -> list[AnalysisResult]:
    return await list_all_analyses(session)


async def get_dashboard_data(session: AsyncSession) -> dict:
    return await get_dashboard_stats(session)
