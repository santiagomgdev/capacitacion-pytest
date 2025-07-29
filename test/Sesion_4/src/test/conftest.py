from fastapi.testclient import TestClient
import asyncio
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.app.core.models.usuario import Base
from src.app.modules.usuarios.api.dependencies import get_db_session
from src.app.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_db.db"

@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture()
async def test_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=True)
    yield engine
    await engine.dispose()

@pytest_asyncio.fixture()
async def test_session_factory(test_engine):
    return sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

@pytest_asyncio.fixture()
async def test_db(test_engine):
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture()
async def db_session(test_session_factory, test_db):
    async with test_session_factory() as session:
        yield session

@pytest_asyncio.fixture()
def client(db_session):
    app.dependency_overrides[get_db_session] = lambda: db_session
    with TestClient(app) as tc:
        yield tc
    app.dependency_overrides.clear()