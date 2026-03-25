"""PDF report generation."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from careerguide.models.analysis import FullReport

_TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "templates"
_env = Environment(loader=FileSystemLoader(str(_TEMPLATES_DIR)))


def render_report_html(report: FullReport) -> str:
    """Render a standalone HTML report (for PDF conversion)."""
    template = _env.get_template("report_pdf.html")
    return template.render(report=report)


def generate_pdf(report: FullReport) -> bytes:
    """Generate PDF bytes from a FullReport."""
    from xhtml2pdf import pisa

    html_str = render_report_html(report)
    buf = BytesIO()
    pisa_status = pisa.CreatePDF(html_str, dest=buf)
    if pisa_status.err:
        raise RuntimeError("PDF generation failed")
    return buf.getvalue()
