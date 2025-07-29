def test_limites_caracteres_correo(client):
    """Prueba la validación de correo con límites de caracteres"""
    # Prueba longitud máxima de correo (254 caracteres en total)
    parte_local_larga = "a" * 60  # 60 caracteres para la parte local
    dominio_largo = "b" * 60 + ".example.com"  # Dominio largo
    correo_largo_valido = f"{parte_local_larga}@{dominio_largo}"
    
    datos_usuario = {
        "correo": correo_largo_valido,
        "contrasena": "SecurePass123!",
        "nombre": "Prueba",
        "apellido": "Usuario"
    }
    
    respuesta = client.post("/users/", json=datos_usuario)
    # Debe funcionar si el correo está dentro de los límites
    if len(correo_largo_valido) <= 254:
        assert respuesta.status_code == 201
    else:
        assert respuesta.status_code == 400