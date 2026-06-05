"""College directory data — loads from JSON files at import time."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path as _Path

from careerguide.models.career import College

_DATA_DIR = _Path(__file__).resolve().parent / "colleges"

# Stream key -> list of JSON filenames to load
_STREAM_FILES: dict[str, list[str]] = {
    "engineering": ["engineering.json", "iiit.json"],
    "medical": ["medical.json"],
    "law": ["law.json"],
    "science": ["science.json"],
    "commerce": ["commerce.json"],
    "education": ["education.json"],
    "design": ["design.json"],
    "arts": ["arts.json"],
    "performing_arts": ["performing_arts.json"],
    "sports": ["sports.json"],
    "civil_services": ["civil_services.json"],
    "hospitality": ["hospitality.json"],
    "agriculture": ["agriculture.json"],
    "defence": ["defence.json"],
}


@lru_cache(maxsize=1)
def _load_stream_map() -> dict[str, list[College]]:
    """Load all JSON files and build the stream->colleges map (cached)."""
    result: dict[str, list[College]] = {}
    for stream, files in _STREAM_FILES.items():
        colleges: list[College] = []
        for fname in files:
            raw = json.loads((_DATA_DIR / fname).read_text(encoding="utf-8"))
            colleges.extend(College.model_validate(c) for c in raw)
        result[stream] = colleges
    return result


# ======================================================================
# ACCESSOR FUNCTIONS
# ======================================================================

def get_college_directory(stream: str = "engineering") -> list[College]:
    """Return full college directory, optionally filtered by stream."""
    smap = _load_stream_map()
    if stream in smap:
        return smap[stream]
    # "all" or unknown -- return everything
    result: list[College] = []
    for colleges in smap.values():
        result.extend(colleges)
    return result


def get_college_streams() -> list[str]:
    """Return available streams in the college directory."""
    return [s for s, c in _load_stream_map().items() if c]


def get_college_by_state(state: str, stream: str = "all") -> list[College]:
    """Return colleges in a given state."""
    return [c for c in get_college_directory(stream) if c.state.lower() == state.lower()]


def get_college_by_type(institute_type: str, stream: str = "all") -> list[College]:
    """Return colleges of a given institute type."""
    return [c for c in get_college_directory(stream)
            if c.institute_type.lower() == institute_type.lower()]


def get_college_by_branch(branch_short: str, stream: str = "all") -> list[College]:
    """Return colleges offering a specific branch."""
    return [c for c in get_college_directory(stream)
            if any(b.short_name.lower() == branch_short.lower() for b in c.branches)]


def get_all_branches(stream: str = "all") -> list[str]:
    """Return sorted unique branch short names across all colleges."""
    return sorted({b.short_name for c in get_college_directory(stream) for b in c.branches})


def get_all_institute_types(stream: str = "all") -> list[str]:
    """Return sorted unique institute types."""
    return sorted({c.institute_type for c in get_college_directory(stream)})


def get_all_college_states(stream: str = "all") -> list[str]:
    """Return sorted unique states from college directory."""
    return sorted({c.state for c in get_college_directory(stream)})
