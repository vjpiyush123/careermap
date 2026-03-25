"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import asyncio

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from careerguide.app import create_app
from careerguide.db.models import Base
from careerguide.db.session import get_session_factory


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def db_engine():
    """In-memory SQLite for tests."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def db_session(db_engine):
    factory = async_sessionmaker(db_engine, expire_on_commit=False)
    async with factory() as session:
        yield session


@pytest_asyncio.fixture
async def app(db_engine):
    """Create test FastAPI app with in-memory DB."""
    import careerguide.db.session as db_mod

    # Override the module-level engine and factory
    original_engine = db_mod._engine
    original_factory = db_mod._session_factory

    db_mod._engine = db_engine
    db_mod._session_factory = async_sessionmaker(db_engine, expire_on_commit=False)

    application = create_app()
    yield application

    db_mod._engine = original_engine
    db_mod._session_factory = original_factory


@pytest_asyncio.fixture
async def client(app):
    """Async HTTP client for testing API routes."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
