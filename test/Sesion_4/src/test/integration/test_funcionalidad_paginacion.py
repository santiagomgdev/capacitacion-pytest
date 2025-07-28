import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_funcionalidad_paginacion(client: AsyncClient):
    """Prueba la paginación con parámetros skip y limit"""
    # Crear varios usuarios para probar paginación
    ids_usuarios = []
    for i in range(15):
        datos_usuario = {
            "correo": f"paginacion{i}@example.com",
            "contrasena": "SecurePass123!",
            "nombre": f"Usuario{i}",
            "apellido": "Prueba"
        }
        respuesta = await client.post("/users/", json=datos_usuario)
        assert respuesta.status_code == 201
        ids_usuarios.append(respuesta.json()["id"])
    
    # Prueba paginación por defecto (debe devolver todos los usuarios, hasta el límite)
    respuesta = await client.get("/users/")
    assert respuesta.status_code == 200
    todos_usuarios = respuesta.json()
    assert len(todos_usuarios) >= 15
    
    # Prueba paginación con límite
    respuesta = await client.get("/users/?limit=5")
    assert respuesta.status_code == 200
    usuarios_limitados = respuesta.json()
    assert len(usuarios_limitados) == 5
    
    # Prueba paginación con skip
    respuesta = await client.get("/users/?skip=5&limit=5")
    assert respuesta.status_code == 200
    usuarios_skip = respuesta.json()
    assert len(usuarios_skip) == 5
    
    # Asegura resultados diferentes para distintas páginas
    respuesta = await client.get("/users/?skip=0&limit=5")
    primera_pagina = respuesta.json()
    respuesta = await client.get("/users/?skip=5&limit=5")
    segunda_pagina = respuesta.json()
    
    ids_primera_pagina = {usuario["id"] for usuario in primera_pagina}
    ids_segunda_pagina = {usuario["id"] for usuario in segunda_pagina}
    assert ids_primera_pagina.isdisjoint(ids_segunda_pagina), "Las páginas no deben solaparse"
    
    # Limpieza
    for usuario_id in ids_usuarios:
        await client.delete(f"/users/{usuario_id}")