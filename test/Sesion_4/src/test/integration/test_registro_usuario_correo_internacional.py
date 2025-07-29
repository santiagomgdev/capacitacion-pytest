def test_registro_usuario_correo_internacional(client):
    """Prueba el registro con direcciones de correo internacional"""
    casos_prueba = [
        "测试@example.com",  # Caracteres chinos
        "José.García@example.es",  # Español con acentos
        "user@münchen.de",  # Alemán con umlaut
        "test@例え.テスト"  # Dominio japonés
    ]
    
    for i, correo in enumerate(casos_prueba):
        datos_usuario = {
            "correo": correo,
            "contrasena": "SecurePass123!",
            "nombre": f"Usuario{i}",
            "apellido": f"Prueba{i}"
        }
        
        respuesta = client.post("/users/", json=datos_usuario)
        assert respuesta.status_code == 400, f"Falló para el correo: {correo}"