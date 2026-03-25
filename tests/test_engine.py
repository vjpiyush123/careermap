"""Tests for the deterministic analysis engine."""

from __future__ import annotations

import pytest

from careerguide.engine.analysis import analyze_stream, run_analysis
from careerguide.models.student import Board, Standard, StreamInterest, StudentProfile


def _make_profile(
    name: str = "Test Student",
    standard: str = "10th",
    percentage_10th: float = 80.0,
    percentage_12th: float | None = None,
    stream: str = "Engineering & Technology",
    state: str = "Maharashtra",
    psychology_score: dict[str, float] | None = None,
) -> StudentProfile:
    return StudentProfile(
        name=name,
        standard=Standard(standard),
        board=Board.CBSE,
        state=state,
        year_of_study=2026,
        percentage_10th=percentage_10th,
        percentage_12th=percentage_12th,
        stream_interest=StreamInterest(stream),
        psychology_score=psychology_score,
    )


class TestAnalyzeStream:
    def test_returns_stream_analysis(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert result.stream_name == "Engineering & Technology"

    def test_suitability_score_range(self):
        profile = _make_profile(percentage_10th=85.0)
        result = analyze_stream(profile, "Engineering & Technology")
        assert 0 <= result.suitability_score <= 100

    def test_has_career_options(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert len(result.career_options) >= 1

    def test_has_industries(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert len(result.industries) >= 1

    def test_has_pros_and_cons(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert len(result.pros) >= 1
        assert len(result.cons) >= 1

    def test_has_growth_info(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert result.growth_india
        assert result.growth_abroad

    def test_has_colleges(self):
        profile = _make_profile(state="Maharashtra")
        result = analyze_stream(profile, "Engineering & Technology")
        assert len(result.top_colleges) >= 10  # India + state

    def test_has_coaching_institutes(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert len(result.coaching_institutes) >= 1

    def test_has_salary_info(self):
        profile = _make_profile()
        result = analyze_stream(profile, "Engineering & Technology")
        assert result.avg_starting_salary_lpa > 0

    def test_higher_marks_higher_score(self):
        low = _make_profile(percentage_10th=50.0)
        high = _make_profile(percentage_10th=95.0)
        result_low = analyze_stream(low, "Engineering & Technology")
        result_high = analyze_stream(high, "Engineering & Technology")
        assert result_high.suitability_score > result_low.suitability_score

    def test_interest_alignment_boosts_score(self):
        aligned = _make_profile(stream="Engineering & Technology")
        misaligned = _make_profile(stream="Arts & Humanities")
        score_aligned = analyze_stream(aligned, "Engineering & Technology").suitability_score
        score_misaligned = analyze_stream(misaligned, "Engineering & Technology").suitability_score
        assert score_aligned > score_misaligned

    def test_psychology_affects_score(self):
        no_psych = _make_profile()
        with_psych = _make_profile(
            psychology_score={"Engineering & Technology": 90.0}
        )
        score_no = analyze_stream(no_psych, "Engineering & Technology").suitability_score
        score_with = analyze_stream(with_psych, "Engineering & Technology").suitability_score
        assert score_with > score_no


class TestRunAnalysis:
    def test_deterministic_same_input_same_output(self):
        profile = _make_profile()
        r1 = run_analysis(profile)
        r2 = run_analysis(profile)
        assert r1.stream_analysis.suitability_score == r2.stream_analysis.suitability_score
        assert r1.stream_analysis.career_options == r2.stream_analysis.career_options
        assert r1.stream_analysis.industries == r2.stream_analysis.industries

    def test_has_top_2_recommendations(self):
        profile = _make_profile()
        result = run_analysis(profile)
        assert len(result.top_2_recommendations) == 2

    def test_result_has_student_info(self):
        profile = _make_profile(name="Analysis Student")
        result = run_analysis(profile)
        assert result.student_name == "Analysis Student"
        assert result.student_id == profile.id

    def test_selected_stream_matches_interest(self):
        profile = _make_profile(stream="Medical & Healthcare")
        result = run_analysis(profile)
        assert result.selected_stream == "Medical & Healthcare"

    def test_data_sufficient_for_valid_profile(self):
        profile = _make_profile(percentage_10th=80.0)
        result = run_analysis(profile)
        assert result.data_sufficient is True

    def test_data_insufficient_for_12th_without_marks(self):
        profile = _make_profile(standard="12th", percentage_12th=None)
        result = run_analysis(profile)
        assert result.data_sufficient is False
        assert result.insufficient_data_reason is not None

    def test_all_streams_analysable(self):
        """Every stream should produce valid analysis."""
        for stream_val in StreamInterest:
            profile = _make_profile(stream=stream_val.value)
            result = run_analysis(profile)
            assert result.stream_analysis.stream_name == stream_val.value
            assert 0 <= result.stream_analysis.suitability_score <= 100
