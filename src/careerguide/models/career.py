"""Career path data models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Branch(BaseModel):
    """Branch / department details within a college."""
    name: str
    short_name: str
    ug_seats: int = 0
    pg_seats: int = 0
    phd_seats: int = 0
    dual_degree_seats: int = 0
    cutoff_year: int = 2024
    cutoff_exam: str = ""
    general_opening_rank: int = 0
    general_closing_rank: int = 0
    obc_closing_rank: int = 0
    sc_closing_rank: int = 0
    st_closing_rank: int = 0
    ews_closing_rank: int = 0
    female_closing_rank: int = 0
    avg_placement_lpa: float = 0.0
    median_placement_lpa: float = 0.0
    highest_placement_lpa: float = 0.0
    placement_percentage: float = 0.0
    specializations: list[str] = Field(default_factory=list)


class CourseType(BaseModel):
    """Course type offered by a college."""
    name: str
    duration_years: float
    entrance_exam: str = ""
    eligibility: str = ""
    total_seats: int = 0
    fee_per_year_lpa: float = 0.0
    available_branches: list[str] = Field(default_factory=list)


class College(BaseModel):
    """College information."""
    name: str
    short_name: str = ""
    stream: str = ""
    institute_type: str = ""
    established: int = 0
    ranking: int = 0
    city: str = ""
    state: str = ""
    nirf_ranking: int = 0
    naac_grade: str = ""
    nba_accredited: bool = False
    avg_fees_lpa: float = 0.0
    hostel_fees_per_year: float = 0.0
    fee_waiver_policy: str = ""
    avg_placement_lpa: float = 0.0
    median_placement_lpa: float = 0.0
    highest_placement_lpa: float = 0.0
    placement_percentage: float = 0.0
    top_recruiters: list[str] = Field(default_factory=list)
    total_seats: int = 0
    website: str = ""
    notable_alumni: list[str] = Field(default_factory=list)
    branches: list[Branch] = Field(default_factory=list)
    course_types: list[CourseType] = Field(default_factory=list)
    # Legacy compat: simple branch name list used in stream data
    branch_names: list[str] = Field(default_factory=list)


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
