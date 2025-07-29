def formatear_nombre_cliente(nombre: str, apellido: str) -> str:
    nombre = nombre.strip().title()  # Limpiar entrada
    apellido = apellido.strip().title() if apellido else ""
    
    if not nombre and not apellido:
        return ""  # Caso especial: entradas vacías
    
    if apellido:
        return f"{apellido.upper()}, {nombre}"
    return nombre.upper()  # No se proporcionó apellido