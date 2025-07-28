import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_caracteres_especiales_nombres(client: AsyncClient):
    """Prueba la creación de usuario con caracteres especiales en nombres"""
    casos_prueba = [
        {"nombre": "José", "apellido": "García"},  # Acentos en español
        {"nombre": "François", "apellido": "Müller"},  # Francés y alemán
        {"nombre": "Александр", "apellido": "Петров"},  # Cirílico
        {"nombre": "田中", "apellido": "太郎"},  # Japonés
        {"nombre": "O'Connor", "apellido": "McDonald"},  # Apóstrofes
        {"nombre": "Van Der Berg", "apellido": "Smith-Jones"},  # Guiones y espacios
    ]
    
    ids_usuarios = []
    for i, nombres in enumerate(casos_prueba):
        datos_usuario = {
            "correo": f"caracteres.especiales{i}@example.com",
            "contrasena": "SecurePass123!",
            **nombres
        }
        
        respuesta = await client.post("/users/", json=datos_usuario)
        assert respuesta.status_code == 201, f"Falló para nombres: {nombres}"
        
        usuario_creado = respuesta.json()
        assert usuario_creado["nombre"] == nombres["nombre"]
        assert usuario_creado["apellido"] == nombres["apellido"]
        ids_usuarios.append(usuario_creado["id"])
    
    # Limpieza
    for usuario_id in ids_usuarios:
        await client.delete(f"/users/{usuario_id}")