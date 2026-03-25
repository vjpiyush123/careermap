"""Integration tests for API endpoints."""

from __future__ import annotations

import pytest
import pytest_asyncio


class TestDashboardAPI:
    @pytest.mark.asyncio
    async def test_dashboard_page(self, client):
        resp = await client.get("/")
        assert resp.status_code == 200
        assert "Dashboard" in resp.text

    @pytest.mark.asyncio
    async def test_dashboard_api(self, client):
        resp = await client.get("/api/dashboard")
        assert resp.status_code == 200
        data = resp.json()
        assert "total_analyses" in data


class TestCareerOptionsAPI:
    @pytest.mark.asyncio
    async def test_career_options_page(self, client):
        resp = await client.get("/careeroptions")
        assert resp.status_code == 200
        assert "Career" in resp.text

    @pytest.mark.asyncio
    async def test_streams_api(self, client):
        resp = await client.get("/api/streams")
        assert resp.status_code == 200
        assert len(resp.json()) == 14

    @pytest.mark.asyncio
    async def test_stream_detail_api(self, client):
        resp = await client.get("/api/streams/Engineering & Technology")
        assert resp.status_code == 200
        data = resp.json()
        assert "colleges_india" in data

    @pytest.mark.asyncio
    async def test_career_tree_api(self, client):
        resp = await client.get("/api/career-tree")
        assert resp.status_code == 200
        data = resp.json()
        assert data["root"]["name"] == "Career Map"


class TestStudentAPI:
    @pytest.mark.asyncio
    async def test_create_student(self, client):
        resp = await client.post("/api/students", json={
            "name": "API Test Student",
            "standard": "10th",
            "board": "CBSE",
            "state": "Maharashtra",
            "year_of_study": 2026,
            "percentage_10th": 85.0,
            "stream_interest": "Engineering & Technology",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "API Test Student"
        assert data["id"]

    @pytest.mark.asyncio
    async def test_list_students(self, client):
        # Create a student first
        await client.post("/api/students", json={
            "name": "List API Student",
            "standard": "10th",
            "board": "CBSE",
            "state": "Delhi",
            "year_of_study": 2026,
            "percentage_10th": 75.0,
            "stream_interest": "Science & Research",
        })
        resp = await client.get("/api/students")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    @pytest.mark.asyncio
    async def test_get_student(self, client):
        create_resp = await client.post("/api/students", json={
            "name": "Get API Student",
            "standard": "12th",
            "board": "ICSE",
            "state": "Tamil Nadu",
            "year_of_study": 2026,
            "percentage_10th": 90.0,
            "percentage_12th": 88.0,
            "stream_interest": "Medical & Healthcare",
        })
        student_id = create_resp.json()["id"]
        resp = await client.get(f"/api/students/{student_id}")
        assert resp.status_code == 200
        assert resp.json()["name"] == "Get API Student"

    @pytest.mark.asyncio
    async def test_student_not_found(self, client):
        resp = await client.get("/api/students/nonexistent")
        assert resp.status_code == 404


class TestPsychologyAPI:
    @pytest.mark.asyncio
    async def test_get_psychology_test(self, client):
        resp = await client.get("/api/psychology-test")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["questions"]) == 20

    @pytest.mark.asyncio
    async def test_submit_psychology_test(self, client):
        # Create student
        create_resp = await client.post("/api/students", json={
            "name": "Psych API Student",
            "standard": "10th",
            "board": "CBSE",
            "state": "Karnataka",
            "year_of_study": 2026,
            "percentage_10th": 80.0,
            "stream_interest": "Engineering & Technology",
        })
        student_id = create_resp.json()["id"]

        # Get questions
        test_resp = await client.get("/api/psychology-test")
        questions = test_resp.json()["questions"]

        # Submit answers (all first option)
        answers = [{"question_id": q["id"], "selected_option": 0} for q in questions]
        submit_resp = await client.post("/api/psychology-test/submit", json={
            "student_id": student_id,
            "answers": answers,
        })
        assert submit_resp.status_code == 200
        data = submit_resp.json()
        assert "scores" in data
        assert len(data["scores"]) == 14
        assert len(data["recommended_streams"]) == 3


class TestAnalysisAPI:
    @pytest.mark.asyncio
    async def test_run_analysis(self, client):
        create_resp = await client.post("/api/students", json={
            "name": "Analysis API Student",
            "standard": "10th",
            "board": "CBSE",
            "state": "Maharashtra",
            "year_of_study": 2026,
            "percentage_10th": 82.0,
            "stream_interest": "Engineering & Technology",
        })
        student_id = create_resp.json()["id"]
        analysis_resp = await client.post(f"/api/analysis/{student_id}")
        assert analysis_resp.status_code == 200
        data = analysis_resp.json()
        assert data["selected_stream"] == "Engineering & Technology"
        assert data["stream_analysis"]["suitability_score"] > 0
        assert len(data["top_2_recommendations"]) == 2

    @pytest.mark.asyncio
    async def test_analysis_not_found(self, client):
        resp = await client.post("/api/analysis/nonexistent")
        assert resp.status_code == 404


class TestReportAPI:
    @pytest.mark.asyncio
    async def test_generate_and_get_report(self, client):
        # Create student
        create_resp = await client.post("/api/students", json={
            "name": "Report API Student",
            "standard": "10th",
            "board": "CBSE",
            "state": "Delhi",
            "year_of_study": 2026,
            "percentage_10th": 78.0,
            "stream_interest": "Commerce, Finance & Business",
        })
        student_id = create_resp.json()["id"]

        # Run analysis
        analysis_resp = await client.post(f"/api/analysis/{student_id}")
        analysis_id = analysis_resp.json()["id"]

        # Generate report
        report_resp = await client.post(f"/api/report/{analysis_id}")
        assert report_resp.status_code == 200
        data = report_resp.json()
        assert data["analysis"]["id"] == analysis_id
        assert data["enrichment"]["executive_summary"]
        assert data["enrichment"]["source"] in ("llm", "template_fallback")

        # Get report
        get_resp = await client.get(f"/api/report/{analysis_id}")
        assert get_resp.status_code == 200

    @pytest.mark.asyncio
    async def test_list_reports(self, client):
        resp = await client.get("/api/reports")
        assert resp.status_code == 200


class TestFullWorkflow:
    @pytest.mark.asyncio
    async def test_end_to_end_workflow(self, client):
        """Full workflow: create student → psych test → analysis → report."""
        # 1. Create student
        create_resp = await client.post("/api/students", json={
            "name": "E2E Student",
            "standard": "12th",
            "board": "CBSE",
            "state": "Karnataka",
            "year_of_study": 2026,
            "percentage_10th": 88.0,
            "percentage_12th": 85.0,
            "stream_interest": "Engineering & Technology",
        })
        assert create_resp.status_code == 200
        student_id = create_resp.json()["id"]

        # 2. Take psychology test
        test_resp = await client.get("/api/psychology-test")
        questions = test_resp.json()["questions"]
        answers = [{"question_id": q["id"], "selected_option": 0} for q in questions]
        psych_resp = await client.post("/api/psychology-test/submit", json={
            "student_id": student_id,
            "answers": answers,
        })
        assert psych_resp.status_code == 200

        # 3. Verify psychology scores stored
        student_resp = await client.get(f"/api/students/{student_id}")
        assert student_resp.json()["psychology_score"] is not None

        # 4. Run analysis
        analysis_resp = await client.post(f"/api/analysis/{student_id}")
        assert analysis_resp.status_code == 200
        analysis_id = analysis_resp.json()["id"]
        assert analysis_resp.json()["psychology_alignment"] is not None

        # 5. Generate report
        report_resp = await client.post(f"/api/report/{analysis_id}")
        assert report_resp.status_code == 200
        report = report_resp.json()
        assert report["enrichment"]["executive_summary"]
        assert report["enrichment"]["career_guidance_narrative"]

        # 6. Verify dashboard updated
        dash_resp = await client.get("/api/dashboard")
        assert dash_resp.json()["total_analyses"] >= 1
