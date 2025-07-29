def test_flujo_completo_crud_usuario(client):
    """Prueba el flujo completo CRUD: Crear, Leer, Actualizar, Eliminar"""
    # CREAR
    datos_usuario = {
        "correo": "crud.test@example.com",
        "contrasena": "SecurePass123!",
        "nombre": "CRUD",
        "apellido": "Prueba"
    }
    
    respuesta_crear = client.post("/users/", json=datos_usuario)
    assert respuesta_crear.status_code == 201
    usuario_id = respuesta_crear.json()["id"]
    
    # LEER por ID
    respuesta_leer = client.get(f"/users/{usuario_id}")
    assert respuesta_leer.status_code == 200
    assert respuesta_leer.json()["correo"] == "crud.test@example.com"
    
    # LEER todos los usuarios
    respuesta_lista = client.get("/users/")
    assert respuesta_lista.status_code == 200
    assert len(respuesta_lista.json()) >= 1
    
    # ACTUALIZAR
    datos_actualizar = {
        "nombre": "Actualizado",
        "apellido": "Nombre",
        "activo": False
    }
    
    respuesta_actualizar = client.put(f"/users/{usuario_id}", json=datos_actualizar)
    assert respuesta_actualizar.status_code == 200
    usuario_actualizado = respuesta_actualizar.json()
    assert usuario_actualizado["nombre"] == "Actualizado"
    assert usuario_actualizado["apellido"] == "Nombre"
    assert usuario_actualizado["activo"] is False
    
    # ELIMINAR
    respuesta_eliminar = client.delete(f"/users/{usuario_id}")
    assert respuesta_eliminar.status_code == 204
    
    # Verificar eliminación
    respuesta_get_eliminado = client.get(f"/users/{usuario_id}")
    assert respuesta_get_eliminado.status_code == 404