"""LLM pipeline using LangGraph StateGraph + Ollama.

Produces enriched narratives from deterministic analysis results.
Falls back to template-based narratives if LLM is unavailable.
"""

from __future__ import annotations

import logging
from typing import Any, TypedDict

import httpx
from langgraph.graph import END, StateGraph

from careerguide.config import get_settings
from careerguide.llm.templates import generate_template_report
from careerguide.models.analysis import AnalysisResult, LLMEnrichedReport

logger = logging.getLogger(__name__)


class PipelineState(TypedDict):
    """State flowing through the LangGraph pipeline."""
    analysis: AnalysisResult
    executive_summary: str
    stream_recommendation: str
    career_guidance: str
    dependency_explanation: str
    source: str
    error: str | None


async def _call_ollama(prompt: str, tier: int = 1) -> str | None:
    """Call the Ollama API. Returns None on failure."""
    settings = get_settings()
    model = settings.llm.tier1_model if tier == 1 else settings.llm.tier2_model
    max_tokens = settings.llm.tier1_max_tokens if tier == 1 else settings.llm.tier2_max_tokens
    temperature = settings.llm.tier1_temperature if tier == 1 else settings.llm.tier2_temperature
    timeout = settings.llm.tier1_timeout_seconds if tier == 1 else settings.llm.tier2_timeout_seconds

    try:
        timeouts = httpx.Timeout(connect=10.0, read=float(timeout), write=10.0, pool=10.0)
        async with httpx.AsyncClient(timeout=timeouts) as client:
            response = await client.post(
                f"{settings.llm.ollama_base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_predict": max_tokens,
                        "temperature": temperature,
                    },
                },
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
    except httpx.ReadTimeout:
        logger.warning("Ollama call timed out after %ss (model=%s)", timeout, model)
        return None
    except Exception as exc:
        logger.warning("Ollama call failed [%s]: %s", type(exc).__name__, exc)
        return None


def _validate_llm_output(text: str, analysis: AnalysisResult) -> bool:
    """Validate LLM output mentions real entities from the deterministic results."""
    if not text or len(text.strip()) < 20:
        return False
    # Verify the stream name is mentioned
    if analysis.stream_analysis.stream_name.lower() not in text.lower():
        return False
    return True


def _build_summary_prompt(analysis: AnalysisResult) -> str:
    sa = analysis.stream_analysis
    return f"""Write a career analysis summary for {analysis.student_name}, a {analysis.standard} student ({analysis.board}, {analysis.state}). 10th: {analysis.percentage_10th}%, 12th: {analysis.percentage_12th or 'N/A'}%. Stream: {sa.stream_name}, Score: {sa.suitability_score}/100. Top picks: {', '.join(analysis.top_2_recommendations)}. Careers: {', '.join(sa.career_options[:3])}.
Write exactly 3 sentences. Be factual."""


def _build_recommendation_prompt(analysis: AnalysisResult) -> str:
    sa = analysis.stream_analysis
    return f"""Recommend {sa.stream_name} for this student. Score: {sa.suitability_score}/100. Pros: {'; '.join(sa.pros[:2])}. Cons: {'; '.join(sa.cons[:2])}. Careers: {', '.join(sa.career_options[:3])}. Salary: Rs {sa.avg_starting_salary_lpa} LPA.
Write exactly 3 sentences of recommendation. Be data-driven."""


def _build_guidance_prompt(analysis: AnalysisResult) -> str:
    sa = analysis.stream_analysis
    colleges = ", ".join(c.college_name for c in sa.top_colleges[:3])
    subjects = ", ".join(sa.subjects_12th[:3]) if sa.subjects_12th else "relevant subjects"
    exams = ", ".join(sa.entrance_exams[:3]) if sa.entrance_exams else "entrance exams"
    coaching = ", ".join(sa.coaching_institutes[:2]) if sa.coaching_institutes else "coaching centres"
    return f"""Give step-by-step career guidance for {sa.stream_name}. Subjects: {subjects}. Exams: {exams}. Coaching: {coaching}. Top colleges: {colleges}.
Write exactly 3 sentences of actionable guidance covering preparation steps."""


def _build_dependency_prompt(analysis: AnalysisResult) -> str:
    sa = analysis.stream_analysis
    return f"""Explain this scoring: Academic 40% + Interest 30% + Psychology 30% = {sa.suitability_score}/100. Psychology taken: {'Yes' if analysis.psychology_alignment else 'No'}.
Write exactly 2 sentences explaining the methodology in simple terms."""


# ─── LangGraph node functions ──────────────────────────────────────────

async def generate_summary_node(state: PipelineState) -> dict[str, Any]:
    prompt = _build_summary_prompt(state["analysis"])
    result = await _call_ollama(prompt, tier=1)
    if result and _validate_llm_output(result, state["analysis"]):
        return {"executive_summary": result.strip(), "source": "llm"}
    fallback = generate_template_report(state["analysis"])
    return {"executive_summary": fallback.executive_summary, "source": "template_fallback"}


async def generate_recommendation_node(state: PipelineState) -> dict[str, Any]:
    prompt = _build_recommendation_prompt(state["analysis"])
    result = await _call_ollama(prompt, tier=1)
    if result and _validate_llm_output(result, state["analysis"]):
        return {"stream_recommendation": result.strip()}
    fallback = generate_template_report(state["analysis"])
    return {"stream_recommendation": fallback.stream_recommendation_narrative}


async def generate_guidance_node(state: PipelineState) -> dict[str, Any]:
    prompt = _build_guidance_prompt(state["analysis"])
    result = await _call_ollama(prompt, tier=2)
    if result and _validate_llm_output(result, state["analysis"]):
        return {"career_guidance": result.strip()}
    fallback = generate_template_report(state["analysis"])
    return {"career_guidance": fallback.career_guidance_narrative}


async def generate_dependency_node(state: PipelineState) -> dict[str, Any]:
    prompt = _build_dependency_prompt(state["analysis"])
    result = await _call_ollama(prompt, tier=2)
    if result and len(result.strip()) >= 20:
        return {"dependency_explanation": result.strip()}
    fallback = generate_template_report(state["analysis"])
    return {"dependency_explanation": fallback.dependency_explanation}


def build_pipeline() -> StateGraph:
    """Build the LangGraph StateGraph for report generation."""
    graph = StateGraph(PipelineState)

    graph.add_node("summary", generate_summary_node)
    graph.add_node("recommendation", generate_recommendation_node)
    graph.add_node("guidance", generate_guidance_node)
    graph.add_node("dependency", generate_dependency_node)

    graph.set_entry_point("summary")
    graph.add_edge("summary", "recommendation")
    graph.add_edge("recommendation", "guidance")
    graph.add_edge("guidance", "dependency")
    graph.add_edge("dependency", END)

    return graph


async def run_llm_pipeline(analysis: AnalysisResult) -> LLMEnrichedReport:
    """Run the full LLM pipeline to generate enriched narratives.

    If LLM is unavailable or fallback is configured, uses template narratives.
    """
    settings = get_settings()

    # Check if we should skip LLM entirely
    if settings.llm.fallback_to_templates:
        try:
            # Quick health check on Ollama
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(f"{settings.llm.ollama_base_url}/api/tags")
                if resp.status_code != 200:
                    raise ConnectionError("Ollama not reachable")
        except Exception:
            logger.info("Ollama unavailable, using template fallback")
            return generate_template_report(analysis)

    initial_state: PipelineState = {
        "analysis": analysis,
        "executive_summary": "",
        "stream_recommendation": "",
        "career_guidance": "",
        "dependency_explanation": "",
        "source": "",
        "error": None,
    }

    try:
        graph = build_pipeline()
        app = graph.compile()
        final_state = await app.ainvoke(initial_state)

        return LLMEnrichedReport(
            analysis_id=analysis.id,
            executive_summary=final_state["executive_summary"],
            stream_recommendation_narrative=final_state["stream_recommendation"],
            career_guidance_narrative=final_state["career_guidance"],
            dependency_explanation=final_state["dependency_explanation"],
            source=final_state.get("source", "llm"),
        )
    except Exception as exc:
        logger.error("LLM pipeline failed: %s — falling back to templates", exc)
        return generate_template_report(analysis)
