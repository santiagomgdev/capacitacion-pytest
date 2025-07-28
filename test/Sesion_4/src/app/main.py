from fastapi import FastAPI
from contextlib import asynccontextmanager
from .modules.usuarios.api.dependencies import init_db
from .modules.usuarios.api.v1.usuario import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="API de Gestión de Usuarios",
    description="Aplicación FastAPI con arquitectura limpia para operaciones CRUD de usuarios",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "User Management API is running"}