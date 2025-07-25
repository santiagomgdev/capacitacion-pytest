class Database:
    
    def __init__(self):
        self.asociados = {}  # Formato: {asociado_id: {"nombre_asociado": str, "correo": str}}
    
    def add_asociado(self, asociado_id: int, nombre_asociado: str, correo: str) -> bool:
        if asociado_id in self.asociados:
            raise ValueError("Usuario ya existe")
        
        asociado_encontrado = False
        for asociado in self.asociados.values():
            if asociado["nombre_asociado"] == nombre_asociado:
                asociado_encontrado = True
                break

        if asociado_encontrado:
            raise ValueError("Usuario duplicado")

        self.asociados[asociado_id] = {
            "nombre_asociado": nombre_asociado,
            "correo": correo,
        }
        return True
    
    def get_asociado_by_id(self, asociado_id: int) -> dict | None:
        return self.asociados.get(asociado_id)
    
    def get_asociado_by_username(self, nombre_asociado: str) -> dict | None:
        for asociado_id, data in self.asociados.items():
            if data["nombre_asociado"] == nombre_asociado:
                return {"asociado_id": asociado_id, **data}
        return None
    
    def delete_asociado(self, asociado_id: int) -> bool:
        if asociado_id in self.asociados:
            del self.asociados[asociado_id]
            return True
        return False
