import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_validacion_reglas_negocio(client: AsyncClient):
    """Prueba la validación de varias reglas de negocio"""
    # Prueba nombre vacío
    respuesta = await client.post("/users/", json={
        "correo": "test@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "",
        "apellido": "Usuario"
    })
    assert respuesta.status_code == 422  # Error de validación Pydantic
    
    # Prueba apellido vacío
    respuesta = await client.post("/users/", json={
        "correo": "test@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Prueba",
        "apellido": ""
    })
    assert respuesta.status_code == 422  # Error de validación Pydantic
    
    # Prueba formatos de correo inválidos
    emails_invalidos = [
        "noesuncorreo",
        "@example.com",
        "test@",
        "test..test@example.com",
        "test@example",
    ]
    
    for correo in emails_invalidos:
        respuesta = await client.post("/users/", json={
            "correo": correo,
            "contrasena": "SecurePass123!",
            "nombre": "Prueba",
            "apellido": "Usuario"
        })
        assert respuesta.status_code == 422, f"Debe rechazar correo inválido: {correo}"