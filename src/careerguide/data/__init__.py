"""Data layer — static career and psychology data."""

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
from careerguide.data.psychology_data import (
    compute_psychology_scores,
    get_psychology_test,
)
from careerguide.data.state_data import (
    get_all_state_data,
    get_all_states,
    get_state_data,
)

__all__ = [
    "build_career_tree",
    "compute_psychology_scores",
    "get_all_state_data",
    "get_all_states",
    "get_all_stream_names",
    "get_career_options",
    "get_coaching_institutes",
    "get_entrance_exams",
    "get_industries",
    "get_psychology_test",
    "get_state_data",
    "get_stream_data",
    "get_stream_growth",
    "get_top_colleges_by_state",
    "get_top_colleges_india",
]
