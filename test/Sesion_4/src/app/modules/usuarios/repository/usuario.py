from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..domain.adapter.usuario import UsuarioRepository
from ..domain.entities.usuario import Usuario
from ....core.models.usuario import UsuarioModel

class SQLUsuarioRepository(UsuarioRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    def _model_to_entity(self, model: UsuarioModel) -> Usuario:
        return Usuario(
            id=model.id,
            correo=model.correo,
            contrasena_hash=model.contrasena_hash,
            nombre=model.nombre,
            apellido=model.apellido,
            activo=model.activo,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
    
    def _entity_to_model(self, entity: Usuario) -> UsuarioModel:
        return UsuarioModel(
            id=entity.id,
            correo=entity.correo,
            contrasena_hash=entity.contrasena_hash,
            nombre=entity.nombre,
            apellido=entity.apellido,
            activo=entity.activo,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
    
    async def create(self, usuario: Usuario) -> Usuario:
        model = self._entity_to_model(usuario)
        model.id = None
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return self._model_to_entity(model)
    
    async def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        result = await self.session.execute(
            select(UsuarioModel).where(UsuarioModel.id == usuario_id)
        )
        model = result.scalar_one_or_none()
        return self._model_to_entity(model) if model else None
    
    async def get_by_email(self, correo: str) -> Optional[Usuario]:
        result = await self.session.execute(
            select(UsuarioModel).where(UsuarioModel.correo == correo)
        )
        model = result.scalar_one_or_none()
        return self._model_to_entity(model) if model else None
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Usuario]:
        result = await self.session.execute(
            select(UsuarioModel).offset(skip).limit(limit)
        )
        models = result.scalars().all()
        return [self._model_to_entity(model) for model in models]
    
    async def update(self, usuario: Usuario) -> Usuario:
        result = await self.session.execute(
            select(UsuarioModel).where(UsuarioModel.id == usuario.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"usuario con ID {usuario.id} no encontrado")
        
        model.correo = usuario.correo
        model.contrasena_hash = usuario.contrasena_hash
        model.nombre = usuario.nombre
        model.apellido = usuario.apellido
        model.activo = usuario.activo
        model.updated_at = usuario.updated_at
        
        await self.session.commit()
        await self.session.refresh(model)
        return self._model_to_entity(model)
    
    async def delete(self, usuario_id: int) -> bool:
        result = await self.session.execute(
            select(UsuarioModel).where(UsuarioModel.id == usuario_id)
        )
        model = result.scalar_one_or_none()
        if not model:
            return False
        
        await self.session.delete(model)
        await self.session.commit()
        return True