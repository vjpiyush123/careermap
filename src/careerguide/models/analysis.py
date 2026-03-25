"""Analysis result data models."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Optional

from pydantic import BaseModel, Field


class CollegeRecommendation(BaseModel):
    """A college recommendation within an analysis."""
    college_name: str
    ranking: int
    city: str
    state: str
    avg_fees_lpa: float
    avg_placement_lpa: float
    total_seats: int
    website: str = ""
    top_companies_hiring: list[str] = Field(default_factory=list)


class StreamAnalysis(BaseModel):
    """Deterministic analysis output for a single stream."""
    stream_name: str
    suitability_score: float = Field(..., ge=0, le=100)
    career_options: list[str]
    industries: list[str]
    pros: list[str]
    cons: list[str]
    growth_india: str
    growth_abroad: str
    top_colleges: list[CollegeRecommendation]
    coaching_institutes: list[str] = Field(default_factory=list)
    avg_starting_salary_lpa: float = 0.0
    subjects_10th: list[str] = Field(default_factory=list)
    subjects_12th: list[str] = Field(default_factory=list)
    entrance_exams: list[str] = Field(default_factory=list)


class AnalysisResult(BaseModel):
    """Complete deterministic analysis result."""
    id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    student_id: str
    student_name: str
    standard: str
    board: str
    state: str
    percentage_10th: float
    percentage_12th: Optional[float] = None
    selected_stream: str
    stream_analysis: StreamAnalysis
    top_2_recommendations: list[str] = Field(default_factory=list)
    psychology_alignment: Optional[dict[str, float]] = None
    data_sufficient: bool = True
    insufficient_data_reason: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class LLMEnrichedReport(BaseModel):
    """LLM-generated narratives layered on top of deterministic results."""
    analysis_id: str
    executive_summary: str
    stream_recommendation_narrative: str
    career_guidance_narrative: str
    dependency_explanation: str
    source: str = "llm"  # "llm" or "template_fallback"


class FullReport(BaseModel):
    """Combined deterministic analysis + LLM narratives."""
    analysis: AnalysisResult
    enrichment: LLMEnrichedReport
