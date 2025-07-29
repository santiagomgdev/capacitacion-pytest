from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..dependencies import get_db_session, get_user_service
from ...schemas.v1.usuario import UsuarioCreateRequest, UsuarioUpdateRequest, UsuarioResponse
from ...domain.exceptions import UsuarioExistenteException, UsuarioNoEncontradoException

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UsuarioCreateRequest,
    session: AsyncSession = Depends(get_db_session)
):
    user_service = get_user_service(session)
    try:
        user = await user_service.crear_usuario(
            correo=user_data.correo,
            contrasena=user_data.contrasena,
            nombre=user_data.nombre,
            apellido=user_data.apellido
        )
        return UsuarioResponse(
            id=user.id,
            correo=user.correo,
            nombre=user.nombre,
            apellido=user.apellido,
            activo=user.activo,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except (UsuarioExistenteException, ValueError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[UsuarioResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_db_session)
):
    user_service = get_user_service(session)
    users = await user_service.obtener_todos_usuarios(skip=skip, limit=limit)
    return [
        UsuarioResponse(
            id=user.id,
            correo=user.correo,
            nombre=user.nombre,
            apellido=user.apellido,
            activo=user.activo,
            created_at=user.created_at,
            updated_at=user.updated_at
        ) for user in users
    ]

@router.get("/{user_id}", response_model=UsuarioResponse)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    user_service = get_user_service(session)
    try:
        user = await user_service.obtener_usuario_por_id(user_id)
        return UsuarioResponse(
            id=user.id,
            correo=user.correo,
            nombre=user.nombre,
            apellido=user.apellido,
            activo=user.activo,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except UsuarioNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{user_id}", response_model=UsuarioResponse)
async def update_user(
    user_id: int,
    user_data: UsuarioUpdateRequest,
    session: AsyncSession = Depends(get_db_session)
):
    user_service = get_user_service(session)
    try:
        user = await user_service.actualizar_usuario(
            usuario_id=user_id,
            correo=user_data.correo,
            contrasena=user_data.contrasena,
            nombre=user_data.nombre,
            apellido=user_data.apellido,
            activo=user_data.activo
        )
        return UsuarioResponse(
            id=user.id,
            correo=user.correo,
            nombre=user.nombre,
            apellido=user.apellido,
            activo=user.activo,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except UsuarioNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except (UsuarioExistenteException, ValueError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    user_service = get_user_service(session)
    try:
        await user_service.eliminar_usuario(user_id)
    except UsuarioNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))