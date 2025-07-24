def clasificar_edad_asociado(edad: int) -> str:
    if edad < 18: return "Menor de edad"
    elif edad < 65: return "Adulto"
    return "Persona mayor"