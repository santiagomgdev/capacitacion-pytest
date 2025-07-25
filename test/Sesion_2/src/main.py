class AsociadosAtlantis:
    """
    Formato: 
    {
    asociado_id: 
        {
        "nombre": str, 
        "correo": str, 
        "activo": bool
        }
    }
    """

    def __init__(self):
        self.asociados = {}  

    def add_asociado(self, asociado_id: int, nombre: str, correo: str, activo: bool = True) -> bool:
        if asociado_id in self.asociados:
            raise ValueError("Asociado ya existe")
        
        if any(asociado["correo"] == correo for asociado in self.asociados.values()):
            raise ValueError("Asociado con correo duplicado")

        self.asociados[asociado_id] = {
            "nombre": nombre,
            "correo": correo,
            "activo": activo
        }
        return True

    def get_asociado_by_id(self, asociado_id: int) -> dict | None:
        return self.asociados.get(asociado_id)

    def get_asociado_by_email(self, correo: str) -> dict | None:
        for asociado_id, data in self.asociados.items():
            if data["correo"] == correo:
                return {"asociado_id": asociado_id, **data}
        return None

    def delete_asociado(self, asociado_id: int) -> bool:
        if asociado_id in self.asociados:
            del self.asociados[asociado_id]
            return True
        return False

    def desactivar_asociado(self, asociado_id: int) -> bool:
        if asociado := self.asociados.get(asociado_id):
            asociado["activo"] = False
            return True
        return False
    
    def purgar_asociados_inactivos(self) -> int:
        ids_inactivos = [id_ for id_, c in self.asociados.items() if not c["activo"]]
        for id_ in ids_inactivos:
            del self.asociados[id_]
        return len(ids_inactivos)
    
    def obtener_estadisticas(self) -> dict:
        return {
            "total_asociados": len(self.clients),
            "asociados_activos": sum(1 for c in self.clients.values() if c["active"]),
        }