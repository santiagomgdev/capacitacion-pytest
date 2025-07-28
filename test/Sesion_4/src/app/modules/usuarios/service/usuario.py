from typing import List, Optional
from ..domain.entities.usuario import Usuario
from ..domain.adapter.usuario import UsuarioRepository
from ..domain.exceptions import UsuarioExistenteException, UsuarioNoEncontradoException

class UsuarioService:
    def __init__(self, repositorio_usuario: UsuarioRepository):
        self.repositorio_usuario = repositorio_usuario

    async def crear_usuario(self, correo: str, contrasena: str, nombre: str, apellido: str) -> Usuario:
        usuario_existente = await self.repositorio_usuario.get_by_email(correo.lower().strip())
        if usuario_existente:
            raise UsuarioExistenteException(f"El usuario con correo {correo} ya existe")
        usuario = Usuario.create_new(correo, contrasena, nombre, apellido)
        return await self.repositorio_usuario.create(usuario)

    async def obtener_usuario_por_id(self, usuario_id: int) -> Usuario:
        usuario = await self.repositorio_usuario.get_by_id(usuario_id)
        if not usuario:
            raise UsuarioNoEncontradoException(f"Usuario con ID {usuario_id} no encontrado")
        return usuario

    async def obtener_usuario_por_correo(self, correo: str) -> Usuario:
        usuario = await self.repositorio_usuario.get_by_email(correo.lower().strip())
        if not usuario:
            raise UsuarioNoEncontradoException(f"Usuario con correo {correo} no encontrado")
        return usuario

    async def obtener_todos_usuarios(self, skip: int = 0, limit: int = 100) -> List[Usuario]:
        return await self.repositorio_usuario.get_all(skip, limit)

    async def actualizar_usuario(self, usuario_id: int, correo: str = None, contrasena: str = None,
                                nombre: str = None, apellido: str = None,
                                activo: bool = None) -> Usuario:
        usuario = await self.obtener_usuario_por_id(usuario_id)

        if correo is not None:
            usuario_existente = await self.repositorio_usuario.get_by_email(correo.lower().strip())
            if usuario_existente and usuario_existente.id != usuario_id:
                raise UsuarioExistenteException(f"El correo {correo} ya está en uso")
            usuario.actualizar_correo(correo)

        if contrasena is not None:
            usuario.cambiar_contrasena(contrasena)

        if nombre is not None or apellido is not None:
            usuario.actualizar_nombre(nombre, apellido)

        if activo is not None:
            usuario.establecer_estado_activo(activo)

        return await self.repositorio_usuario.update(usuario)

    async def eliminar_usuario(self, usuario_id: int) -> bool:
        usuario = await self.obtener_usuario_por_id(usuario_id)
        return await self.repositorio_usuario.delete(usuario.id)
