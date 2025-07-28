from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from ....core.models.usuario import Base
from ..repository.usuario import SQLUsuarioRepository
from ..service.usuario import UsuarioService

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

def get_user_service(session: AsyncSession) -> UsuarioService:
    repository = SQLUsuarioRepository(session)
    return UsuarioService(repository)