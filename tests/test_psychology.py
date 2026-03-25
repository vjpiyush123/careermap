"""Tests for psychology test data and scoring."""

from __future__ import annotations

import pytest

from careerguide.data.career_data import get_all_stream_names
from careerguide.data.psychology_data import compute_psychology_scores, get_psychology_test


class TestPsychologyTest:
    def test_has_20_questions(self):
        test = get_psychology_test()
        assert len(test.questions) == 20

    def test_each_question_has_4_options(self):
        test = get_psychology_test()
        for q in test.questions:
            assert len(q.options) == 4, f"Q{q.id} has {len(q.options)} options"

    def test_questions_have_unique_ids(self):
        test = get_psychology_test()
        ids = [q.id for q in test.questions]
        assert len(ids) == len(set(ids))

    def test_each_question_has_category(self):
        test = get_psychology_test()
        valid_categories = {"analytical", "scientific", "social", "creative", "practical", "values", "personality"}
        for q in test.questions:
            assert q.category in valid_categories, f"Q{q.id} has invalid category: {q.category}"

    def test_options_have_stream_weights(self):
        test = get_psychology_test()
        for q in test.questions:
            for opt in q.options:
                assert len(opt.stream_weights) > 0, f"Q{q.id} option '{opt.text}' has no weights"


class TestPsychologyScoring:
    def _all_first_options(self):
        """Helper: answer first option for all questions."""
        test = get_psychology_test()
        return [(q.id, 0) for q in test.questions]

    def test_scores_for_all_14_streams(self):
        answers = self._all_first_options()
        scores = compute_psychology_scores(answers)
        streams = get_all_stream_names()
        for stream in streams:
            assert stream in scores, f"Missing score for {stream}"

    def test_scores_between_0_and_100(self):
        answers = self._all_first_options()
        scores = compute_psychology_scores(answers)
        for stream, score in scores.items():
            assert 0 <= score <= 100, f"{stream} has score {score} outside 0-100"

    def test_different_answers_produce_different_scores(self):
        test = get_psychology_test()
        answers_a = [(q.id, 0) for q in test.questions]
        answers_b = [(q.id, 3) for q in test.questions]
        scores_a = compute_psychology_scores(answers_a)
        scores_b = compute_psychology_scores(answers_b)
        # At least some streams should differ
        diffs = sum(1 for s in scores_a if abs(scores_a[s] - scores_b.get(s, 0)) > 0.1)
        assert diffs > 0, "Different answers should produce different scores"

    def test_empty_answers_return_zero_scores(self):
        scores = compute_psychology_scores([])
        for score in scores.values():
            assert score == 0.0

    def test_invalid_question_id_ignored(self):
        scores = compute_psychology_scores([(999, 0)])
        # Should still return scores (all zero)
        assert isinstance(scores, dict)

    def test_invalid_option_index_ignored(self):
        scores = compute_psychology_scores([(1, 99)])
        # Should not crash
        assert isinstance(scores, dict)

    def test_deterministic_same_input_same_output(self):
        answers = self._all_first_options()
        scores1 = compute_psychology_scores(answers)
        scores2 = compute_psychology_scores(answers)
        assert scores1 == scores2
