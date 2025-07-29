def test_desactivacion_reactivacion_usuario(client):
    """Prueba el flujo de desactivación y reactivación de usuario"""
    # Crear usuario
    datos_usuario = {
        "correo": "desactivacion@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Desactivación",
        "apellido": "Prueba"
    }
    respuesta = client.post("/users/", json=datos_usuario)
    assert respuesta.status_code == 201
    usuario_id = respuesta.json()["id"]
    assert respuesta.json()["activo"] is True
    
    # Desactivar usuario
    respuesta_desactivar = client.put(f"/users/{usuario_id}", json={
        "activo": False
    })
    assert respuesta_desactivar.status_code == 200
    assert respuesta_desactivar.json()["activo"] is False
    
    # Verificar que el usuario sigue siendo accesible pero inactivo
    respuesta_get = client.get(f"/users/{usuario_id}")
    assert respuesta_get.status_code == 200
    assert respuesta_get.json()["activo"] is False
    
    # Reactivar usuario
    respuesta_reactivar = client.put(f"/users/{usuario_id}", json={
        "activo": True
    })
    assert respuesta_reactivar.status_code == 200
    assert respuesta_reactivar.json()["activo"] is True
    
    # Limpieza
    client.delete(f"/users/{usuario_id}")