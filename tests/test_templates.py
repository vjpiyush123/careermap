"""Tests for the LLM templates (fallback narratives)."""

from __future__ import annotations

import pytest

from careerguide.engine.analysis import run_analysis
from careerguide.llm.templates import generate_template_report
from careerguide.models.student import Board, Standard, StreamInterest, StudentProfile


def _make_profile(**kwargs) -> StudentProfile:
    defaults = dict(
        name="Template Student",
        standard=Standard.TENTH,
        board=Board.CBSE,
        state="Maharashtra",
        year_of_study=2026,
        percentage_10th=80.0,
        stream_interest=StreamInterest.ENGINEERING_TECHNOLOGY,
    )
    defaults.update(kwargs)
    return StudentProfile(**defaults)


class TestTemplateReport:
    def test_generates_all_sections(self):
        profile = _make_profile()
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert report.executive_summary
        assert report.stream_recommendation_narrative
        assert report.career_guidance_narrative
        assert report.dependency_explanation
        assert report.source == "template_fallback"

    def test_executive_summary_contains_student_name(self):
        profile = _make_profile(name="Summary Student")
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert "Summary Student" in report.executive_summary

    def test_recommendation_contains_stream_name(self):
        profile = _make_profile()
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert "Engineering & Technology" in report.stream_recommendation_narrative

    def test_guidance_contains_colleges(self):
        profile = _make_profile()
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert "College" in report.career_guidance_narrative or "college" in report.career_guidance_narrative.lower()

    def test_methodology_explains_scoring(self):
        profile = _make_profile()
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert "40%" in report.dependency_explanation
        assert "30%" in report.dependency_explanation

    def test_analysis_id_matches(self):
        profile = _make_profile()
        analysis = run_analysis(profile)
        report = generate_template_report(analysis)
        assert report.analysis_id == analysis.id
