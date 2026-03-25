"""Tests for database CRUD operations."""

from __future__ import annotations

import pytest
import pytest_asyncio

from careerguide.db.crud import (
    create_student,
    get_analysis,
    get_dashboard_stats,
    get_student,
    list_students,
    save_analysis,
    update_student_psychology,
)
from careerguide.engine.analysis import run_analysis
from careerguide.models.student import (
    Board,
    Standard,
    StreamInterest,
    StudentProfile,
    StudentProfileCreate,
)


def _make_create_data(**kwargs) -> StudentProfileCreate:
    defaults = dict(
        name="DB Student",
        standard=Standard.TENTH,
        board=Board.CBSE,
        state="Maharashtra",
        year_of_study=2026,
        percentage_10th=80.0,
        stream_interest=StreamInterest.ENGINEERING_TECHNOLOGY,
    )
    defaults.update(kwargs)
    return StudentProfileCreate(**defaults)


class TestStudentCRUD:
    @pytest.mark.asyncio
    async def test_create_and_retrieve_student(self, db_session):
        data = _make_create_data(name="Create Test")
        profile = await create_student(db_session, data)
        assert profile.name == "Create Test"
        assert profile.id

        retrieved = await get_student(db_session, profile.id)
        assert retrieved is not None
        assert retrieved.name == "Create Test"

    @pytest.mark.asyncio
    async def test_list_students(self, db_session):
        await create_student(db_session, _make_create_data(name="List Test 1"))
        await create_student(db_session, _make_create_data(name="List Test 2"))
        students = await list_students(db_session)
        assert len(students) >= 2

    @pytest.mark.asyncio
    async def test_update_psychology_scores(self, db_session):
        data = _make_create_data(name="Psych Test")
        profile = await create_student(db_session, data)
        scores = {"Engineering & Technology": 85.0, "Medical & Healthcare": 60.0}
        updated = await update_student_psychology(db_session, profile.id, scores)
        assert updated is not None
        assert updated.psychology_score == scores

    @pytest.mark.asyncio
    async def test_get_nonexistent_student(self, db_session):
        result = await get_student(db_session, "nonexistent_id")
        assert result is None


class TestAnalysisCRUD:
    @pytest.mark.asyncio
    async def test_save_and_retrieve_analysis(self, db_session):
        data = _make_create_data(name="Analysis DB Test")
        profile = await create_student(db_session, data)
        analysis = run_analysis(profile)
        saved = await save_analysis(db_session, analysis)
        assert saved.id == analysis.id

        retrieved = await get_analysis(db_session, analysis.id)
        assert retrieved is not None
        assert retrieved.student_name == "Analysis DB Test"
        assert retrieved.stream_analysis.stream_name == "Engineering & Technology"


class TestDashboardStats:
    @pytest.mark.asyncio
    async def test_empty_dashboard(self, db_session):
        stats = await get_dashboard_stats(db_session)
        assert stats["total_analyses"] == 0
        assert stats["by_stream"] == {}

    @pytest.mark.asyncio
    async def test_dashboard_with_data(self, db_session):
        data = _make_create_data(name="Dashboard Test")
        profile = await create_student(db_session, data)
        analysis = run_analysis(profile)
        await save_analysis(db_session, analysis)
        stats = await get_dashboard_stats(db_session)
        assert stats["total_analyses"] >= 1
