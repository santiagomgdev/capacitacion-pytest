def test_validacion_actualizacion_contrasena(client):
    """Prueba la validación de contraseña durante actualizaciones de usuario"""
    # Crear usuario primero
    datos_usuario = {
        "correo": "actualizacion@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Contraseña",
        "apellido": "Prueba"
    }
    respuesta = client.post("/users/", json=datos_usuario)
    assert respuesta.status_code == 201
    usuario_id = respuesta.json()["id"]
    
    # Prueba actualización válida de contraseña
    respuesta_actualizar = client.put(f"/users/{usuario_id}", json={
        "contrasena": "NuevaContraseña456!"
    })
    assert respuesta_actualizar.status_code == 200
    
    # Prueba actualización inválida (demasiado corta)
    respuesta_actualizar = client.put(f"/users/{usuario_id}", json={
        "contrasena": "Corta1!"
    })
    assert respuesta_actualizar.status_code == 400 or 422
    
    # Prueba actualización inválida (sin carácter especial)
    respuesta_actualizar = client.put(f"/users/{usuario_id}", json={
        "contrasena": "SinEspecial123"
    })
    assert respuesta_actualizar.status_code == 400
    
    # Limpieza
    client.delete(f"/users/{usuario_id}")