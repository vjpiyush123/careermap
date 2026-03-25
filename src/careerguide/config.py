"""Configuration loader for CareerGuide application."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    name: str = "CareerGuide Analysis Agent"
    version: str = "0.1.0"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000


class AnalysisConfig(BaseModel):
    max_analysis_duration_seconds: int = 120
    cache_ttl_seconds: int = 3600
    max_college_suggestions: int = 10
    max_concurrent_runs: int = 5


class LLMConfig(BaseModel):
    provider: Literal["ollama", "azure", "openai"] = "ollama"
    tier1_model: str = "llama3.2:3b"
    tier2_model: str = "llama3.2:3b"
    ollama_base_url: str = "http://localhost:11434"
    tier1_max_tokens: int = 2000
    tier2_max_tokens: int = 500
    tier1_temperature: float = 0.1
    tier2_temperature: float = 0.1
    tier1_timeout_seconds: int = 120
    tier2_timeout_seconds: int = 90
    fallback_to_templates: bool = True


class PersistenceConfig(BaseModel):
    db_url: str = "sqlite+aiosqlite:///./careerguide.db"


class ReliabilityConfig(BaseModel):
    api_timeout_seconds: int = 10
    api_max_retries: int = 3
    api_retry_backoff_base_seconds: int = 1
    circuit_breaker_failure_threshold: int = 3
    circuit_breaker_recovery_seconds: int = 30


class Settings(BaseModel):
    app: AppConfig = AppConfig()
    analysis: AnalysisConfig = AnalysisConfig()
    llm: LLMConfig = LLMConfig()
    persistence: PersistenceConfig = PersistenceConfig()
    reliability: ReliabilityConfig = ReliabilityConfig()


def load_settings(config_path: str | Path | None = None) -> Settings:
    """Load settings from YAML config file."""
    if config_path is None:
        config_path = Path(__file__).resolve().parents[2] / "config" / "settings.yaml"
    config_path = Path(config_path)
    if config_path.exists():
        with open(config_path, "r") as f:
            raw = yaml.safe_load(f) or {}
        return Settings(**raw)
    return Settings()


_settings: Settings | None = None


def get_settings() -> Settings:
    """Get cached settings singleton."""
    global _settings
    if _settings is None:
        _settings = load_settings()
    return _settings
