"""SQLAlchemy ORM models for persistence."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import JSON, Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Declarative base for all ORM models."""


class StudentRow(Base):
    __tablename__ = "students"

    id = Column(String(32), primary_key=True)
    name = Column(String(200), nullable=False)
    standard = Column(String(10), nullable=False)
    board = Column(String(50), nullable=False)
    state = Column(String(100), nullable=False)
    year_of_study = Column(Integer, nullable=False)
    percentage_10th = Column(Float, nullable=False)
    percentage_12th = Column(Float, nullable=True)
    stream_interest = Column(String(100), nullable=False)
    psychology_score = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)


class AnalysisRow(Base):
    __tablename__ = "analyses"

    id = Column(String(32), primary_key=True)
    student_id = Column(String(32), nullable=False, index=True)
    student_name = Column(String(200), nullable=False)
    standard = Column(String(10), nullable=False)
    board = Column(String(50), nullable=False)
    state = Column(String(100), nullable=False)
    percentage_10th = Column(Float, nullable=False)
    percentage_12th = Column(Float, nullable=True)
    selected_stream = Column(String(100), nullable=False)
    stream_analysis_json = Column(JSON, nullable=False)
    top_2_recommendations = Column(JSON, nullable=True)
    psychology_alignment = Column(JSON, nullable=True)
    data_sufficient = Column(Integer, default=1, nullable=False)  # 1 = True
    insufficient_data_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)


class ReportRow(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    analysis_id = Column(String(32), nullable=False, index=True)
    executive_summary = Column(Text, nullable=False)
    stream_recommendation_narrative = Column(Text, nullable=False)
    career_guidance_narrative = Column(Text, nullable=False)
    dependency_explanation = Column(Text, nullable=False)
    source = Column(String(30), nullable=False, default="template_fallback")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
