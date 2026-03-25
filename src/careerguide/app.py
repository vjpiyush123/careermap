"""FastAPI application entry point."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from careerguide.config import get_settings
from careerguide.db.session import init_db
from careerguide.routes import router

logger = logging.getLogger("careerguide")

_STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown lifecycle."""
    settings = get_settings()
    logging.basicConfig(
        level=logging.DEBUG if settings.app.debug else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger.info("CareerGuide v%s starting up", settings.app.version)
    await init_db()
    logger.info("Database initialised")
    yield
    logger.info("CareerGuide shutting down")


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app.name,
        version=settings.app.version,
        lifespan=lifespan,
    )
    app.include_router(router)

    # Mount static files
    if _STATIC_DIR.exists():
        app.mount("/static", StaticFiles(directory=str(_STATIC_DIR)), name="static")

    return app


app = create_app()
