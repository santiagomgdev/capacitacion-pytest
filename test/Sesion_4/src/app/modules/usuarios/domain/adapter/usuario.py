from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    async def create(self, user: Usuario) -> Usuario:
        pass
    
    @abstractmethod
    async def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        pass
    
    @abstractmethod
    async def get_by_email(self, correo: str) -> Optional[Usuario]:
        pass
    
    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Usuario]:
        pass
    
    @abstractmethod
    async def update(self, usuario: Usuario) -> Usuario:
        pass
    
    @abstractmethod
    async def delete(self, usuario_id: int) -> bool:
        pass