"""Database layer — SQLAlchemy models, session, and CRUD."""

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
from careerguide.db.models import AnalysisRow, Base, ReportRow, StudentRow
from careerguide.db.session import get_db_session, get_engine, get_session_factory, init_db

__all__ = [
    "AnalysisRow",
    "Base",
    "ReportRow",
    "StudentRow",
    "create_student",
    "get_analysis",
    "get_dashboard_stats",
    "get_db_session",
    "get_engine",
    "get_report_for_analysis",
    "get_session_factory",
    "get_student",
    "init_db",
    "list_all_analyses",
    "list_analyses_for_student",
    "list_students",
    "save_analysis",
    "save_report",
    "update_student_psychology",
]
