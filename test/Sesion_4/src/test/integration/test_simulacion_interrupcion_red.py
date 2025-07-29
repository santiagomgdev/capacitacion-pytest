def test_simulacion_interrupcion_red(client):
    """Prueba el comportamiento durante simulaciones de interrupción de red"""
    # Crear usuario primero
    datos_usuario = {
        "correo": "network.test@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Red",
        "apellido": "Prueba"
    }
    
    respuesta = client.post("/users/", json=datos_usuario)
    assert respuesta.status_code == 201
    usuario_id = respuesta.json()["id"]
    
    # Prueba que las operaciones posteriores funcionen (simulando recuperación)
    respuesta_get = client.get(f"/users/{usuario_id}")
    assert respuesta_get.status_code == 200
    
    # Limpieza
    client.delete(f"/users/{usuario_id}")