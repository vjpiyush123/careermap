#!/usr/bin/env python3
"""Build static HTML site for GitHub Pages deployment.

Renders the Career Options page and a landing page into pure HTML files
that can be served from any static host (GitHub Pages, Netlify, etc.).

Usage:
    python build_static.py              # builds to _site/
    python build_static.py --base /     # for root domain hosting
    python build_static.py --base /careermap  # for repo-based GitHub Pages

The --base flag sets the URL prefix for all asset/link paths.
Default: "" (relative paths — works everywhere).
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from urllib.parse import urlparse

from jinja2 import Environment, FileSystemLoader

# ── Import data layer ──────────────────────────────────────────────────
from careerguide.data import (
    build_career_tree,
    get_all_branches,
    get_all_college_states,
    get_all_institute_types,
    get_all_state_data,
    get_all_states,
    get_all_stream_names,
    get_college_directory,
    get_college_streams,
    get_stream_data,
)

# ── Paths ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src" / "careerguide"
TEMPLATES_DIR = SRC_DIR / "templates"
STATIC_TEMPLATES_DIR = ROOT_DIR / "static_templates"  # overrides for static build
STATIC_DIR = SRC_DIR / "static"
OUT_DIR = ROOT_DIR / "_site"


# ── Mock request object for templates ──────────────────────────────────
class _MockURL:
    def __init__(self, path: str):
        self.path = path


class _MockRequest:
    def __init__(self, path: str):
        self.url = _MockURL(path)


# ── Build helpers ──────────────────────────────────────────────────────
def build(base_path: str = "") -> None:
    """Render all static pages and copy assets to OUT_DIR."""
    base = base_path.rstrip("/")

    # Clean & create output dir
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    # Set up Jinja2 environment — static_templates overrides regular templates
    env = Environment(
        loader=FileSystemLoader([str(STATIC_TEMPLATES_DIR), str(TEMPLATES_DIR)]),
        autoescape=True,
    )

    # Global template context — rewrite asset paths with base prefix
    def _render(template_name: str, context: dict, output_name: str) -> None:
        tpl = env.get_template(template_name)
        html = tpl.render(**context)
        # Rewrite absolute paths to use base prefix
        if base:
            html = html.replace('href="/', f'href="{base}/')
            html = html.replace('src="/', f'src="{base}/')
        (OUT_DIR / output_name).write_text(html, encoding="utf-8")
        print(f"  ✓ {output_name}")

    print(f"Building static site → {OUT_DIR}/")
    print(f"Base path: '{base or '(relative)'}'")
    print()

    # ── 1. Career Options page (the main content) ─────────────────────
    tree = build_career_tree()
    streams = get_all_stream_names()
    stream_details = {s: get_stream_data(s) for s in streams}

    _render("career_options.html", {
        "request": _MockRequest("/careeroptions"),
        "tree": tree,
        "streams": streams,
        "stream_details": stream_details,
    }, "careeroptions.html")

    # ── 2. State Opportunities page ───────────────────────────────────
    states = get_all_states()
    state_data = get_all_state_data()

    _render("state_opportunities.html", {
        "request": _MockRequest("/stateopportunities"),
        "states": states,
        "state_data": state_data,
    }, "stateopportunities.html")

    # ── 3. College Directory page ──────────────────────────────────────
    college_streams = get_college_streams()
    colleges = [c.model_dump() for c in get_college_directory("all")]
    all_college_states = get_all_college_states("all")
    all_types = get_all_institute_types("all")
    all_branches = get_all_branches("all")

    _render("colleges.html", {
        "request": _MockRequest("/colleges"),
        "streams": college_streams,
        "colleges_json": colleges,
        "all_states": all_college_states,
        "all_types": all_types,
        "all_branches": all_branches,
    }, "colleges.html")

    # ── 4. Feedback page ──────────────────────────────────────────────
    _render("feedback.html", {
        "request": _MockRequest("/feedback"),
        "streams": streams,
    }, "feedback.html")

    # ── 5. Landing / index page ───────────────────────────────────────
    index_html = env.from_string(INDEX_TEMPLATE).render(
        base=base,
        request=_MockRequest("/"),
        streams=streams,
    )
    if base:
        index_html = index_html.replace('href="/', f'href="{base}/')
        index_html = index_html.replace('src="/', f'src="{base}/')
    (OUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("  ✓ index.html")

    # ── 6. Copy static assets ─────────────────────────────────────────
    static_out = OUT_DIR / "static"
    shutil.copytree(STATIC_DIR, static_out)
    print("  ✓ static/ (css, js)")

    # ── 7. Create .nojekyll for GitHub Pages ──────────────────────────
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")
    print("  ✓ .nojekyll")

    print(f"\nDone! {OUT_DIR.relative_to(Path.cwd())}/ ready for deployment.")


# ── Landing page template ─────────────────────────────────────────────
INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CareerGuide — AI-Powered Career Stream Guidance</title>
    <script>
        (function(){
            var t=localStorage.getItem('cg-theme')||'dark';
            document.documentElement.setAttribute('data-theme',t);
        })();
    </script>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-brand">
            <a href="/">🎓 CareerGuide</a>
        </div>
        <div class="nav-links">
            <a href="/" class="nav-link active">Home</a>
            <a href="/careeroptions.html" class="nav-link">Career Options</a>
            <a href="/colleges.html" class="nav-link">Colleges</a>
            <a href="/stateopportunities.html" class="nav-link">State Guide</a>
            <a href="/feedback.html" class="nav-link">Feedback</a>
            <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" title="Toggle dark/light mode" aria-label="Toggle theme">
                <span class="theme-icon" id="themeIcon"></span>
            </button>
        </div>
    </nav>

    <main class="container">
        <div class="page-header" style="text-align:center; padding:3rem 0 1rem;">
            <h1 style="font-size:2.5rem;">🎓 CareerGuide</h1>
            <p class="subtitle" style="font-size:1.1rem; max-width:600px; margin:0.75rem auto;">
                AI-powered career stream guidance for students after 10th &amp; 12th.
                Explore 14 career streams with roadmaps, entrance exams, colleges, and international opportunities.
            </p>
        </div>

        <div style="text-align:center; margin:2rem 0; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
            <a href="/careeroptions.html" class="btn btn-primary" style="font-size:1.1rem; padding:0.9rem 2.5rem;">
                Explore Career Options →
            </a>
            <a href="/colleges.html" class="btn btn-primary" style="font-size:1.1rem; padding:0.9rem 2.5rem;">
                College Directory →
            </a>
            <a href="/stateopportunities.html" class="btn btn-secondary" style="font-size:1.1rem; padding:0.9rem 2.5rem;">
                State Guide →
            </a>
        </div>

        <div class="stats-grid" style="margin-top:3rem;">
            <div class="stat-card">
                <div class="stat-number">14</div>
                <div class="stat-label">Career Streams</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">7</div>
                <div class="stat-label">Info Tabs per Stream</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">140+</div>
                <div class="stat-label">Colleges Listed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">50+</div>
                <div class="stat-label">Entrance Exams</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">33</div>
                <div class="stat-label">States & UTs</div>
            </div>
        </div>

        <div class="dashboard-section" style="margin-top:2rem;">
            <h2>Available Streams</h2>
            <div class="radio-grid" style="margin-top:1rem;">
                {% for stream in streams %}
                <a href="/careeroptions.html" class="radio-label" style="text-decoration:none; color:var(--text-primary);">
                    <span>📘</span> <span>{{ stream }}</span>
                </a>
                {% endfor %}
            </div>
        </div>
    </main>

    <footer class="footer">
        <p>&copy; 2026 CareerGuide — AI-powered career stream guidance</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>"""


# ── CLI ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build static site for GitHub Pages")
    parser.add_argument(
        "--base",
        default="",
        help="Base URL path prefix (e.g. /careermap for github.io/careermap). "
             "Leave empty for relative paths.",
    )
    args = parser.parse_args()
    build(args.base)
