"""Student profile data models."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field


class Standard(StrEnum):
    TENTH = "10th"
    TWELFTH = "12th"


class Board(StrEnum):
    STATE_BOARD = "State Board"
    CBSE = "CBSE"
    ICSE = "ICSE"
    NIOS = "NIOS"
    IB = "IB"
    CAMBRIDGE = "Cambridge (IGCSE)"
    CISCE = "CISCE"


class StreamInterest(StrEnum):
    ENGINEERING_TECHNOLOGY = "Engineering & Technology"
    MEDICAL_HEALTHCARE = "Medical & Healthcare"
    LAW_LEGAL = "Law & Legal Studies"
    SCIENCE_RESEARCH = "Science & Research"
    EDUCATION_TEACHING = "Education & Teaching"
    COMMERCE_FINANCE = "Commerce, Finance & Business"
    ARTS_HUMANITIES = "Arts & Humanities"
    DESIGN_CREATIVE = "Design & Creative Arts"
    PERFORMING_FINE_ARTS = "Performing & Fine Arts"
    SPORTS_PHYSICAL_ED = "Sports & Physical Education"
    CIVIL_SERVICES = "Civil Services & Government Services"
    HOSPITALITY_TOURISM = "Hospitality, Travel & Tourism"
    AGRICULTURE_ENVIRONMENT = "Agriculture & Environmental Studies"
    DEFENCE_RESEARCH = "Defence Research"


INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Delhi", "Chandigarh", "Puducherry", "Jammu & Kashmir", "Ladakh",
]


class StudentProfileCreate(BaseModel):
    """Input model for creating a student profile."""
    name: str = Field(..., min_length=1, max_length=200)
    standard: Standard
    board: Board
    state: str = Field(..., min_length=1)
    year_of_study: int = Field(..., ge=2000, le=2040)
    percentage_10th: float = Field(..., ge=0, le=100)
    percentage_12th: Optional[float] = Field(None, ge=0, le=100)
    stream_interest: StreamInterest


class StudentProfile(BaseModel):
    """Full student profile with ID and timestamps."""
    id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    name: str
    standard: Standard
    board: Board
    state: str
    year_of_study: int
    percentage_10th: float
    percentage_12th: Optional[float] = None
    stream_interest: StreamInterest
    psychology_score: Optional[dict[str, float]] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class PsychologyAnswer(BaseModel):
    """Single answer to a psychology test question."""
    question_id: int
    selected_option: int = Field(..., ge=0, le=3)


class PsychologyTestSubmission(BaseModel):
    """Submission of psychology test answers."""
    student_id: str
    answers: list[PsychologyAnswer]


class PsychologyResult(BaseModel):
    """Outcome of the psychology test per stream."""
    student_id: str
    scores: dict[str, float]  # stream_name -> aptitude score 0-100
    recommended_streams: list[str]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
