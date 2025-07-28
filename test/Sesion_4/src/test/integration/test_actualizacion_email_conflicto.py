import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_actualizacion_email_conflicto(client: AsyncClient):
    """Prueba que actualizar el correo de usuario a uno existente falle"""
    # Crear primer usuario
    datos_usuario1 = {
        "correo": "usuario1@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Usuario",
        "apellido": "Uno"
    }
    respuesta1 = await client.post("/users/", json=datos_usuario1)
    assert respuesta1.status_code == 201
    usuario1_id = respuesta1.json()["id"]
    
    # Crear segundo usuario
    datos_usuario2 = {
        "correo": "usuario2@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Usuario",
        "apellido": "Dos"
    }
    respuesta2 = await client.post("/users/", json=datos_usuario2)
    assert respuesta2.status_code == 201
    usuario2_id = respuesta2.json()["id"]
    
    # Intentar actualizar el correo de usuario2 al de usuario1
    respuesta_actualizar = await client.put(f"/users/{usuario2_id}", json={
        "correo": "usuario1@example.com"
    })
    assert respuesta_actualizar.status_code == 400
    assert "ya está en uso" in respuesta_actualizar.json()["detail"]
    
    # Limpieza
    await client.delete(f"/users/{usuario1_id}")
    await client.delete(f"/users/{usuario2_id}")