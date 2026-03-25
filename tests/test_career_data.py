"""Tests for career data module."""

from __future__ import annotations

import pytest

from careerguide.data.career_data import (
    build_career_tree,
    get_all_stream_names,
    get_career_options,
    get_coaching_institutes,
    get_entrance_exams,
    get_industries,
    get_stream_data,
    get_stream_growth,
    get_top_colleges_by_state,
    get_top_colleges_india,
)


class TestStreamRegistry:
    def test_all_14_streams_available(self):
        streams = get_all_stream_names()
        assert len(streams) == 14

    def test_stream_names_non_empty(self):
        for stream in get_all_stream_names():
            assert len(stream) > 0

    def test_each_stream_has_data(self):
        for stream in get_all_stream_names():
            data = get_stream_data(stream)
            assert data is not None, f"Missing data for stream: {stream}"

    def test_unknown_stream_returns_none(self):
        assert get_stream_data("Imaginary Stream") is None


class TestColleges:
    def test_each_stream_has_top_10_colleges_india(self):
        for stream in get_all_stream_names():
            colleges = get_top_colleges_india(stream)
            assert len(colleges) == 10, f"{stream} has {len(colleges)} colleges, expected 10"

    def test_college_has_required_fields(self):
        colleges = get_top_colleges_india("Engineering & Technology")
        c = colleges[0]
        assert c.name
        assert c.ranking >= 1
        assert c.city
        assert c.state
        assert c.avg_fees_lpa >= 0
        assert c.avg_placement_lpa >= 0
        assert c.total_seats > 0

    def test_engineering_has_state_wise_colleges(self):
        colleges = get_top_colleges_by_state("Engineering & Technology", "Maharashtra")
        assert len(colleges) >= 3

    def test_state_colleges_empty_for_unknown_state(self):
        colleges = get_top_colleges_by_state("Engineering & Technology", "Unknown State")
        assert colleges == []


class TestCareerOptions:
    def test_each_stream_has_career_options(self):
        for stream in get_all_stream_names():
            options = get_career_options(stream)
            assert len(options) >= 1, f"{stream} has no career options"

    def test_career_option_has_fields(self):
        options = get_career_options("Engineering & Technology")
        opt = options[0]
        assert opt.name
        assert opt.description
        assert opt.avg_starting_salary_lpa > 0

    def test_industries_non_empty(self):
        for stream in get_all_stream_names():
            industries = get_industries(stream)
            assert len(industries) >= 1, f"{stream} has no industries"


class TestGrowthAndExtras:
    def test_growth_has_india_and_abroad(self):
        for stream in get_all_stream_names():
            growth = get_stream_growth(stream)
            assert "india" in growth
            assert "abroad" in growth
            assert len(growth["india"]) > 0

    def test_coaching_institutes_exist(self):
        for stream in get_all_stream_names():
            coaching = get_coaching_institutes(stream)
            assert len(coaching) >= 1, f"{stream} has no coaching institutes"

    def test_entrance_exams_exist(self):
        for stream in get_all_stream_names():
            exams = get_entrance_exams(stream)
            assert len(exams) >= 1, f"{stream} has no entrance exams"


class TestCareerTree:
    def test_tree_root_name(self):
        tree = build_career_tree()
        assert tree.root.name == "Career Map"
        assert tree.root.level == "root"

    def test_tree_has_10th_node(self):
        tree = build_career_tree()
        assert len(tree.root.children) == 1
        tenth = tree.root.children[0]
        assert tenth.name == "After 10th Standard"
        assert tenth.level == "10th"

    def test_tree_has_14_streams(self):
        tree = build_career_tree()
        tenth = tree.root.children[0]
        assert len(tenth.children) == 14

    def test_tree_stream_has_bachelors(self):
        tree = build_career_tree()
        eng = tree.root.children[0].children[0]  # First stream
        assert eng.level == "12th"
        assert len(eng.children) >= 1
        bachelors = eng.children[0]
        assert bachelors.level == "bachelors"
