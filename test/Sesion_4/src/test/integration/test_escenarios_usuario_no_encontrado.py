def test_escenarios_usuario_no_encontrado(client):
    """Prueba varios escenarios de usuario no encontrado"""
    # Obtener usuario inexistente
    respuesta = client.get("/users/99999")
    assert respuesta.status_code == 404
    assert "no encontrado" in respuesta.json()["detail"]
    
    # Actualizar usuario inexistente
    respuesta = client.put("/users/99999", json={
        "nombre": "Actualizado"
    })
    assert respuesta.status_code == 404
    
    # Eliminar usuario inexistente
    respuesta =  client.delete("/users/99999")
    assert respuesta.status_code == 404