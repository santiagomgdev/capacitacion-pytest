def test_registro_usuario_caso_feliz(client):
    datos_usuario = {
        "correo": "john.doe@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "John",
        "apellido": "Doe"
    }
    
    respuesta = client.post("/users/", json=datos_usuario)
    
    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["correo"] == "john.doe@example.com"
    assert datos["nombre"] == "John"
    assert datos["apellido"] == "Doe"
    assert datos["activo"] is True
    assert "id" in datos
    assert "created_at" in datos
    assert "updated_at" in datos
    assert "contrasena" not in datos  # La contraseña no debe ser devuelta