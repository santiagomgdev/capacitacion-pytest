def test_registro_correo_duplicado(client):
    """Prueba que se prevenga el registro de correo duplicado"""
    datos_usuario = {
        "correo": "duplicate@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "Primero",
        "apellido": "Usuario"
    }
    
    # El primer registro debe funcionar
    respuesta1 = client.post("/users/", json=datos_usuario)
    assert respuesta1.status_code == 201
    
    # El segundo registro con el mismo correo debe fallar
    datos_usuario["nombre"] = "Segundo"
    respuesta2 = client.post("/users/", json=datos_usuario)
    assert respuesta2.status_code == 400
    assert "ya existe" in respuesta2.json()["detail"]