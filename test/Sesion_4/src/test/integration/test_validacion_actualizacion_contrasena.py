import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_validacion_actualizacion_contrasena(client: AsyncClient):
    """Prueba la validación de contraseña durante actualizaciones de usuario"""
    # Crear usuario primero
    datos_usuario = {
        "correo": "actualizacion.contraseña@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Contraseña",
        "apellido": "Prueba"
    }
    respuesta = await client.post("/users/", json=datos_usuario)
    assert respuesta.status_code == 201
    usuario_id = respuesta.json()["id"]
    
    # Prueba actualización válida de contraseña
    respuesta_actualizar = await client.put(f"/users/{usuario_id}", json={
        "contrasena": "NuevaContraseña456!"
    })
    assert respuesta_actualizar.status_code == 200
    
    # Prueba actualización inválida (demasiado corta)
    respuesta_actualizar = await client.put(f"/users/{usuario_id}", json={
        "contrasena": "Corta1!"
    })
    assert respuesta_actualizar.status_code == 400
    
    # Prueba actualización inválida (sin carácter especial)
    respuesta_actualizar = await client.put(f"/users/{usuario_id}", json={
        "contrasena": "SinEspecial123"
    })
    assert respuesta_actualizar.status_code == 400
    
    # Limpieza
    await client.delete(f"/users/{usuario_id}")