import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_escenarios_usuario_no_encontrado(client: AsyncClient):
    """Prueba varios escenarios de usuario no encontrado"""
    # Obtener usuario inexistente
    respuesta = await client.get("/users/99999")
    assert respuesta.status_code == 404
    assert "no encontrado" in respuesta.json()["detail"]
    
    # Actualizar usuario inexistente
    respuesta = await client.put("/users/99999", json={
        "nombre": "Actualizado"
    })
    assert respuesta.status_code == 404
    
    # Eliminar usuario inexistente
    respuesta = await client.delete("/users/99999")
    assert respuesta.status_code == 404