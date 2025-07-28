import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_validacion_contrasena_casos_extremos(client: AsyncClient):
    """Prueba la validación de contraseña con varios casos extremos"""
    usuario_base = {
        "correo": "test@example.com",
        "nombre": "Prueba",
        "apellido": "Usuario"
    }
    
    # Prueba longitud mínima (8 caracteres)
    contrasena_min_valida = "Ab1!wxyz"
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": contrasena_min_valida})
    assert respuesta.status_code == 201
    
    # Limpieza para la siguiente prueba
    await client.delete(f"/users/{respuesta.json()['id']}")
    
    # Prueba longitud máxima (128 caracteres)
    contrasena_max_valida = "A1!" + "x" * 125  # 128 caracteres en total
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": contrasena_max_valida})
    assert respuesta.status_code == 201
    
    # Limpieza para la siguiente prueba
    await client.delete(f"/users/{respuesta.json()['id']}")
    
    # Prueba contraseña demasiado larga (129 caracteres)
    contrasena_larga_invalida = "A1!" + "x" * 126  # 129 caracteres en total
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": contrasena_larga_invalida})
    assert respuesta.status_code == 400
    
    # Prueba contraseña sin carácter especial
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": "SecurePass123"})
    assert respuesta.status_code == 400
    
    # Prueba contraseña sin mayúscula
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": "securepass123!"})
    assert respuesta.status_code == 400
    
    # Prueba contraseña sin minúscula
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": "SECUREPASS123!"})
    assert respuesta.status_code == 400
    
    # Prueba contraseña sin dígito
    respuesta = await client.post("/users/", json={**usuario_base, "contrasena": "SecurePass!"})
    assert respuesta.status_code == 400