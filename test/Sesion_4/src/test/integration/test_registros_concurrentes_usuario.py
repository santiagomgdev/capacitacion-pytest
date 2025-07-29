import pytest


@pytest.mark.asyncio
async def test_registros_concurrentes_usuario(client):
    """Prueba registros concurrentes de usuario para detectar condiciones de carrera"""
    import asyncio
    
    async def crear_usuario(sufijo_email: int):
        datos_usuario = {
            "correo": f"concurrente{sufijo_email}@example.com",
            "contrasena": "SecurePass123!",
            "nombre": f"Usuario{sufijo_email}",
            "apellido": "Prueba"
        }
        return client.post("/users/", json=datos_usuario)
    
    # Crear varios usuarios concurrentemente
    tareas = [crear_usuario(i) for i in range(5)]
    respuestas = await asyncio.gather(*tareas)
    
    # Todos deben funcionar con emails únicos
    for respuesta in respuestas:
        assert respuesta.status_code == 201
    
    # Verificar que todos los usuarios tengan IDs únicos
    ids_usuarios = [respuesta.json()["id"] for respuesta in respuestas]
    assert len(set(ids_usuarios)) == len(ids_usuarios), "Todos los IDs de usuario deben ser únicos"
    
    # Limpieza
    for usuario_id in ids_usuarios:
        client.delete(f"/users/{usuario_id}")