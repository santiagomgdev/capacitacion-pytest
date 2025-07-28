from dataclasses import dataclass
from typing import Optional
from src.models.asociado import Asociado

@dataclass
class AsociadoInterface:
    id: Optional[int]
    nombre: str
    edad: int
    
    @classmethod
    def from_model(cls, asociado: Asociado) -> 'AsociadoInterface':
        return cls(
            id=asociado.id,
            nombre=asociado.nombre,
            edad=asociado.edad
        )
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad
        }