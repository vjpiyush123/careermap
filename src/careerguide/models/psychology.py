"""Psychology test data models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class TestOption(BaseModel):
    """A single answer option for a question."""
    text: str
    stream_weights: dict[str, float] = Field(default_factory=dict)


class PsychologyQuestion(BaseModel):
    """A question in the psychology aptitude test."""
    id: int
    text: str
    options: list[TestOption]
    category: str  # e.g. "analytical", "creative", "social", "practical"


class PsychologyTest(BaseModel):
    """Complete psychology test definition."""
    questions: list[PsychologyQuestion]
    version: str = "1.0"
