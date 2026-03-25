"""CRUD operations for persistent storage."""

from __future__ import annotations

import json
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from careerguide.db.models import AnalysisRow, ReportRow, StudentRow
from careerguide.models.analysis import (
    AnalysisResult,
    FullReport,
    LLMEnrichedReport,
    StreamAnalysis,
)
from careerguide.models.student import StudentProfile, StudentProfileCreate


# ─── Student CRUD ───────────────────────────────────────────────────────

async def create_student(session: AsyncSession, data: StudentProfileCreate) -> StudentProfile:
    profile = StudentProfile(**data.model_dump())
    row = StudentRow(
        id=profile.id,
        name=profile.name,
        standard=profile.standard.value,
        board=profile.board.value,
        state=profile.state,
        year_of_study=profile.year_of_study,
        percentage_10th=profile.percentage_10th,
        percentage_12th=profile.percentage_12th,
        stream_interest=profile.stream_interest.value,
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return profile


async def get_student(session: AsyncSession, student_id: str) -> StudentProfile | None:
    result = await session.execute(select(StudentRow).where(StudentRow.id == student_id))
    row = result.scalar_one_or_none()
    if row is None:
        return None
    return StudentProfile(
        id=row.id,
        name=row.name,
        standard=row.standard,
        board=row.board,
        state=row.state,
        year_of_study=row.year_of_study,
        percentage_10th=row.percentage_10th,
        percentage_12th=row.percentage_12th,
        stream_interest=row.stream_interest,
        psychology_score=row.psychology_score,
        created_at=row.created_at,
        updated_at=row.updated_at,
    )


async def update_student_psychology(
    session: AsyncSession,
    student_id: str,
    scores: dict[str, float],
) -> StudentProfile | None:
    result = await session.execute(select(StudentRow).where(StudentRow.id == student_id))
    row = result.scalar_one_or_none()
    if row is None:
        return None
    row.psychology_score = scores
    row.updated_at = datetime.now(UTC)
    await session.commit()
    await session.refresh(row)
    return await get_student(session, student_id)


async def list_students(session: AsyncSession) -> list[StudentProfile]:
    result = await session.execute(select(StudentRow).order_by(StudentRow.created_at.desc()))
    rows = result.scalars().all()
    return [
        StudentProfile(
            id=r.id, name=r.name, standard=r.standard, board=r.board,
            state=r.state, year_of_study=r.year_of_study,
            percentage_10th=r.percentage_10th, percentage_12th=r.percentage_12th,
            stream_interest=r.stream_interest, psychology_score=r.psychology_score,
            created_at=r.created_at, updated_at=r.updated_at,
        )
        for r in rows
    ]


# ─── Analysis CRUD ─────────────────────────────────────────────────────

async def save_analysis(session: AsyncSession, result: AnalysisResult) -> AnalysisResult:
    row = AnalysisRow(
        id=result.id,
        student_id=result.student_id,
        student_name=result.student_name,
        standard=result.standard,
        board=result.board,
        state=result.state,
        percentage_10th=result.percentage_10th,
        percentage_12th=result.percentage_12th,
        selected_stream=result.selected_stream,
        stream_analysis_json=result.stream_analysis.model_dump(),
        top_2_recommendations=result.top_2_recommendations,
        psychology_alignment=result.psychology_alignment,
        data_sufficient=1 if result.data_sufficient else 0,
        insufficient_data_reason=result.insufficient_data_reason,
        created_at=result.created_at,
    )
    session.add(row)
    await session.commit()
    return result


async def get_analysis(session: AsyncSession, analysis_id: str) -> AnalysisResult | None:
    result = await session.execute(select(AnalysisRow).where(AnalysisRow.id == analysis_id))
    row = result.scalar_one_or_none()
    if row is None:
        return None
    return AnalysisResult(
        id=row.id,
        student_id=row.student_id,
        student_name=row.student_name,
        standard=row.standard,
        board=row.board,
        state=row.state,
        percentage_10th=row.percentage_10th,
        percentage_12th=row.percentage_12th,
        selected_stream=row.selected_stream,
        stream_analysis=StreamAnalysis(**row.stream_analysis_json),
        top_2_recommendations=row.top_2_recommendations or [],
        psychology_alignment=row.psychology_alignment,
        data_sufficient=bool(row.data_sufficient),
        insufficient_data_reason=row.insufficient_data_reason,
        created_at=row.created_at,
    )


async def list_analyses_for_student(
    session: AsyncSession,
    student_id: str,
) -> list[AnalysisResult]:
    result = await session.execute(
        select(AnalysisRow)
        .where(AnalysisRow.student_id == student_id)
        .order_by(AnalysisRow.created_at.desc())
    )
    rows = result.scalars().all()
    return [
        AnalysisResult(
            id=r.id, student_id=r.student_id, student_name=r.student_name,
            standard=r.standard, board=r.board, state=r.state,
            percentage_10th=r.percentage_10th, percentage_12th=r.percentage_12th,
            selected_stream=r.selected_stream,
            stream_analysis=StreamAnalysis(**r.stream_analysis_json),
            top_2_recommendations=r.top_2_recommendations or [],
            psychology_alignment=r.psychology_alignment,
            data_sufficient=bool(r.data_sufficient),
            insufficient_data_reason=r.insufficient_data_reason,
            created_at=r.created_at,
        )
        for r in rows
    ]


async def list_all_analyses(session: AsyncSession) -> list[AnalysisResult]:
    result = await session.execute(select(AnalysisRow).order_by(AnalysisRow.created_at.desc()))
    rows = result.scalars().all()
    return [
        AnalysisResult(
            id=r.id, student_id=r.student_id, student_name=r.student_name,
            standard=r.standard, board=r.board, state=r.state,
            percentage_10th=r.percentage_10th, percentage_12th=r.percentage_12th,
            selected_stream=r.selected_stream,
            stream_analysis=StreamAnalysis(**r.stream_analysis_json),
            top_2_recommendations=r.top_2_recommendations or [],
            psychology_alignment=r.psychology_alignment,
            data_sufficient=bool(r.data_sufficient),
            insufficient_data_reason=r.insufficient_data_reason,
            created_at=r.created_at,
        )
        for r in rows
    ]


# ─── Report CRUD ───────────────────────────────────────────────────────

async def save_report(session: AsyncSession, report: LLMEnrichedReport) -> LLMEnrichedReport:
    row = ReportRow(
        analysis_id=report.analysis_id,
        executive_summary=report.executive_summary,
        stream_recommendation_narrative=report.stream_recommendation_narrative,
        career_guidance_narrative=report.career_guidance_narrative,
        dependency_explanation=report.dependency_explanation,
        source=report.source,
    )
    session.add(row)
    await session.commit()
    return report


async def get_report_for_analysis(
    session: AsyncSession,
    analysis_id: str,
) -> LLMEnrichedReport | None:
    result = await session.execute(
        select(ReportRow).where(ReportRow.analysis_id == analysis_id)
        .order_by(ReportRow.id.desc())
        .limit(1)
    )
    row = result.scalar_one_or_none()
    if row is None:
        return None
    return LLMEnrichedReport(
        analysis_id=row.analysis_id,
        executive_summary=row.executive_summary,
        stream_recommendation_narrative=row.stream_recommendation_narrative,
        career_guidance_narrative=row.career_guidance_narrative,
        dependency_explanation=row.dependency_explanation,
        source=row.source,
    )


# ─── Dashboard aggregates ──────────────────────────────────────────────

async def get_dashboard_stats(session: AsyncSession) -> dict:
    """Get aggregate stats for the dashboard."""
    from sqlalchemy import func

    # Total analyses
    total_result = await session.execute(select(func.count(AnalysisRow.id)))
    total_analyses = total_result.scalar() or 0

    # By stream
    stream_result = await session.execute(
        select(AnalysisRow.selected_stream, func.count(AnalysisRow.id))
        .group_by(AnalysisRow.selected_stream)
    )
    by_stream = {row[0]: row[1] for row in stream_result.all()}

    # By state
    state_result = await session.execute(
        select(AnalysisRow.state, func.count(AnalysisRow.id))
        .group_by(AnalysisRow.state)
    )
    by_state = {row[0]: row[1] for row in state_result.all()}

    # By board
    board_result = await session.execute(
        select(AnalysisRow.board, func.count(AnalysisRow.id))
        .group_by(AnalysisRow.board)
    )
    by_board = {row[0]: row[1] for row in board_result.all()}

    return {
        "total_analyses": total_analyses,
        "by_stream": by_stream,
        "by_state": by_state,
        "by_board": by_board,
    }
