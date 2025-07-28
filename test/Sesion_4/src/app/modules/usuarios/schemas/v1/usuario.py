from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioCreateRequest(BaseModel):
    correo: EmailStr
    contrasena: str = Field(..., min_length=8, max_length=128)
    nombre: str = Field(..., min_length=1, max_length=50)
    apellido: str = Field(..., min_length=1, max_length=50)

class UsuarioUpdateRequest(BaseModel):
    correo: Optional[EmailStr] = None
    contrasena: Optional[str] = Field(None, min_length=8, max_length=128)
    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    apellido: Optional[str] = Field(None, min_length=1, max_length=50)
    activo: Optional[bool] = None

class UsuarioResponse(BaseModel):
    id: int
    correo: str
    nombre: str
    apellido: str
    activo: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True