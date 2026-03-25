"""Career path data models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class College(BaseModel):
    """College information."""
    name: str
    ranking: int
    city: str
    state: str
    avg_fees_lpa: float
    avg_placement_lpa: float
    total_seats: int
    website: str = ""
    branches: list[str] = Field(default_factory=list)


class CareerOption(BaseModel):
    """A career option within a stream."""
    name: str
    description: str
    industries: list[str] = Field(default_factory=list)
    typical_roles: list[str] = Field(default_factory=list)
    avg_starting_salary_lpa: float = 0.0
    growth_india: str = ""
    growth_abroad: str = ""


class StreamNode(BaseModel):
    """A node in the career path tree."""
    id: str
    name: str
    level: str  # "10th", "12th", "bachelors", "masters", "higher_studies", "jobs"
    children: list[StreamNode] = Field(default_factory=list)
    career_options: list[CareerOption] = Field(default_factory=list)
    top_colleges_india: list[College] = Field(default_factory=list)
    top_colleges_by_state: dict[str, list[College]] = Field(default_factory=dict)
    coaching_institutes: list[str] = Field(default_factory=list)


class CareerTree(BaseModel):
    """Complete career path tree structure."""
    root: StreamNode
