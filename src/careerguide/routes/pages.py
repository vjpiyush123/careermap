"""FastAPI routes — all page routes and API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from careerguide.data import (
    build_career_tree,
    get_admission_categories,
    get_all_branches,
    get_all_college_states,
    get_all_institute_types,
    get_all_state_data,
    get_all_states,
    get_all_stream_names,
    get_college_directory,
    get_college_streams,
    get_documents_checklist,
    get_stream_data,
)
from careerguide.db.session import get_session_factory
from careerguide.models.student import (
    INDIAN_STATES,
    Board,
    PsychologyTestSubmission,
    Standard,
    StreamInterest,
    StudentProfileCreate,
)
from careerguide.services.career_service import (
    create_student_profile,
    generate_full_report,
    get_all_reports,
    get_dashboard_data,
    get_existing_report,
    get_psychology_test_data,
    get_student_analyses,
    get_student_profile,
    list_student_profiles,
    run_student_analysis,
    submit_psychology_test,
)
from careerguide.db.crud import create_feedback, list_all_feedbacks

from pathlib import Path

_TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "templates"
templates = Jinja2Templates(directory=str(_TEMPLATES_DIR))

router = APIRouter()


# ─── Dependency: DB session ────────────────────────────────────────────

async def _get_session() -> AsyncSession:
    factory = get_session_factory()
    async with factory() as session:
        yield session


# ═══════════════════════════════════════════════════════════════════════════
# PAGE ROUTES (HTML responses)
# ═══════════════════════════════════════════════════════════════════════════

@router.get("/", response_class=HTMLResponse)
async def dashboard_page(request: Request, session: AsyncSession = Depends(_get_session)):
    """Dashboard — summary cards and analytics."""
    stats = await get_dashboard_data(session)
    return templates.TemplateResponse(request, "dashboard.html", {
        "stats": stats,
    })


@router.get("/careeroptions", response_class=HTMLResponse)
async def career_options_page(request: Request):
    """Career options — tree structure of all streams."""
    tree = build_career_tree()
    streams = get_all_stream_names()
    stream_details = {s: get_stream_data(s) for s in streams}
    return templates.TemplateResponse(request, "career_options.html", {
        "tree": tree,
        "streams": streams,
        "stream_details": stream_details,
    })


@router.get("/stateopportunities", response_class=HTMLResponse)
async def state_opportunities_page(request: Request):
    """State-specific career opportunities — scholarships, jobs, industry."""
    states = get_all_states()
    state_data = get_all_state_data()
    return templates.TemplateResponse(request, "state_opportunities.html", {
        "states": states,
        "state_data": state_data,
    })


@router.get("/colleges", response_class=HTMLResponse)
async def colleges_page(request: Request):
    """College directory — browse, filter, compare colleges."""
    streams = get_college_streams()
    colleges = [c.model_dump() for c in get_college_directory("all")]
    all_states = get_all_college_states("all")
    all_types = get_all_institute_types("all")
    all_branches = get_all_branches("all")
    return templates.TemplateResponse(request, "colleges.html", {
        "streams": streams,
        "colleges_json": colleges,
        "all_states": all_states,
        "all_types": all_types,
        "all_branches": all_branches,
    })


@router.get("/specialadmissions", response_class=HTMLResponse)
async def special_admissions_page(request: Request):
    """Special admission criteria — quotas, direct entry, and special schemes."""
    categories = get_admission_categories()
    checklist = get_documents_checklist()
    return templates.TemplateResponse(request, "special_admissions.html", {
        "categories": categories,
        "checklist": checklist,
    })


@router.get("/feedback", response_class=HTMLResponse)
async def feedback_page(request: Request):
    """Feedback page — collect student pain points."""
    streams = get_all_stream_names()
    return templates.TemplateResponse(request, "feedback.html", {
        "streams": streams,
    })


# Pydantic model for feedback submission
class FeedbackCreate(BaseModel):
    student_name: str
    email: EmailStr
    standard: str
    stream: str | None = None
    feedback: str


@router.post("/api/feedback")
async def submit_feedback(
    data: FeedbackCreate,
    session: AsyncSession = Depends(_get_session),
):
    """API endpoint to submit student feedback."""
    if len(data.feedback) < 20:
        raise HTTPException(status_code=400, detail="Feedback must be at least 20 characters")
    
    await create_feedback(
        session=session,
        student_name=data.student_name,
        email=data.email,
        standard=data.standard,
        stream=data.stream,
        feedback=data.feedback,
    )
    return JSONResponse({"status": "success", "message": "Feedback submitted successfully"})


@router.get("/admin/feedback", response_class=HTMLResponse)
async def feedback_admin_page(request: Request, session: AsyncSession = Depends(_get_session)):
    """Admin page to view all feedback."""
    feedbacks = await list_all_feedbacks(session)
    return templates.TemplateResponse(request, "feedback_admin.html", {
        "feedbacks": feedbacks,
    })


@router.get("/studentdetails", response_class=HTMLResponse)
async def student_details_page(request: Request, session: AsyncSession = Depends(_get_session)):
    """Student details — profile form and list."""
    students = await list_student_profiles(session)
    return templates.TemplateResponse(request, "student_details.html", {
        "students": students,
        "standards": [s.value for s in Standard],
        "boards": [b.value for b in Board],
        "states": INDIAN_STATES,
        "streams": [s.value for s in StreamInterest],
    })


@router.get("/studentdetails/{student_id}", response_class=HTMLResponse)
async def student_profile_page(
    request: Request,
    student_id: str,
    session: AsyncSession = Depends(_get_session),
):
    """Individual student profile view."""
    profile = await get_student_profile(session, student_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Student not found")
    analyses = await get_student_analyses(session, student_id)
    psychology_test = get_psychology_test_data()
    return templates.TemplateResponse(request, "student_profile.html", {
        "student": profile,
        "analyses": analyses,
        "psychology_test": psychology_test,
        "has_psychology": profile.psychology_score is not None,
    })


@router.get("/analysis", response_class=HTMLResponse)
async def analysis_page(request: Request, session: AsyncSession = Depends(_get_session)):
    """Analysis reports listing."""
    reports = await get_all_reports(session)
    return templates.TemplateResponse(request, "analysis.html", {
        "reports": reports,
    })


@router.get("/analysis/{analysis_id}", response_class=HTMLResponse)
async def analysis_detail_page(
    request: Request,
    analysis_id: str,
    session: AsyncSession = Depends(_get_session),
):
    """Individual analysis report view."""
    report = await get_existing_report(session, analysis_id)
    if report is None:
        # Auto-generate report if analysis exists but enrichment hasn't been created yet
        report = await generate_full_report(session, analysis_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return templates.TemplateResponse(request, "report.html", {
        "report": report,
    })


# ═══════════════════════════════════════════════════════════════════════════
# API ROUTES (JSON responses)
# ═══════════════════════════════════════════════════════════════════════════

@router.post("/api/students")
async def api_create_student(
    data: StudentProfileCreate,
    session: AsyncSession = Depends(_get_session),
):
    profile = await create_student_profile(session, data)
    return profile.model_dump()


@router.get("/api/students")
async def api_list_students(session: AsyncSession = Depends(_get_session)):
    students = await list_student_profiles(session)
    return [s.model_dump() for s in students]


@router.get("/api/students/{student_id}")
async def api_get_student(student_id: str, session: AsyncSession = Depends(_get_session)):
    profile = await get_student_profile(session, student_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return profile.model_dump()


@router.get("/api/psychology-test")
async def api_get_psychology_test():
    test = get_psychology_test_data()
    return test.model_dump()


@router.post("/api/psychology-test/submit")
async def api_submit_psychology_test(
    submission: PsychologyTestSubmission,
    session: AsyncSession = Depends(_get_session),
):
    result = await submit_psychology_test(session, submission)
    return result.model_dump()


@router.post("/api/analysis/{student_id}")
async def api_run_analysis(
    student_id: str,
    session: AsyncSession = Depends(_get_session),
):
    try:
        result = await run_student_analysis(session, student_id)
        return result.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/api/report/{analysis_id}")
async def api_generate_report(
    analysis_id: str,
    session: AsyncSession = Depends(_get_session),
):
    try:
        report = await generate_full_report(session, analysis_id)
        return report.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/report/{analysis_id}")
async def api_get_report(
    analysis_id: str,
    session: AsyncSession = Depends(_get_session),
):
    report = await get_existing_report(session, analysis_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report.model_dump()


@router.get("/api/career-tree")
async def api_career_tree():
    tree = build_career_tree()
    return tree.model_dump()


@router.get("/api/streams")
async def api_list_streams():
    return get_all_stream_names()


@router.get("/api/streams/{stream_name}")
async def api_get_stream(stream_name: str):
    data = get_stream_data(stream_name)
    if data is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    # Serialize pydantic models in the dict
    serialized = {}
    for key, value in data.items():
        if isinstance(value, list) and value and hasattr(value[0], "model_dump"):
            serialized[key] = [v.model_dump() for v in value]
        elif isinstance(value, dict):
            inner = {}
            for k, v in value.items():
                if isinstance(v, list) and v and hasattr(v[0], "model_dump"):
                    inner[k] = [item.model_dump() for item in v]
                else:
                    inner[k] = v
            serialized[key] = inner
        else:
            serialized[key] = value
    return serialized


@router.get("/api/dashboard")
async def api_dashboard(session: AsyncSession = Depends(_get_session)):
    return await get_dashboard_data(session)


@router.get("/api/reports")
async def api_list_reports(session: AsyncSession = Depends(_get_session)):
    reports = await get_all_reports(session)
    return [r.model_dump() for r in reports]


@router.get("/api/students/{student_id}/analyses")
async def api_student_analyses(
    student_id: str,
    session: AsyncSession = Depends(_get_session),
):
    analyses = await get_student_analyses(session, student_id)
    return [a.model_dump() for a in analyses]


@router.get("/api/report/{analysis_id}/pdf")
async def api_download_pdf(
    analysis_id: str,
    session: AsyncSession = Depends(_get_session),
):
    """Download the analysis report as a PDF."""
    report = await get_existing_report(session, analysis_id)
    if report is None:
        # Try generating the report first
        from careerguide.services.career_service import generate_full_report as gen_report
        try:
            report = await gen_report(session, analysis_id)
        except ValueError:
            raise HTTPException(status_code=404, detail="Analysis not found")

    from careerguide.services.pdf_service import generate_pdf
    try:
        pdf_bytes = generate_pdf(report)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    filename = f"{report.analysis.student_name}_{report.analysis.selected_stream}_report.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
