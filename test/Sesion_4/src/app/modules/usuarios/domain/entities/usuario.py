import re
import bcrypt
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Usuario:
    id: Optional[int]
    correo: str
    contrasena_hash: str
    nombre: str
    apellido: str
    activo: bool
    created_at: datetime
    updated_at: datetime
    
    @staticmethod
    def validar_correo(correo: str) -> None:
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            raise ValueError("Formato de correo electrónico inválido")
        
        if len(correo) > 254:
            raise ValueError("La dirección de correo electrónico es demasiado larga")
        
        parte_local, dominio = correo.rsplit('@', 1)
        if len(parte_local) > 64:
            raise ValueError("La parte local del correo electrónico es demasiado larga")
    
    @staticmethod
    def validar_contrasena(contrasena: str) -> None:
        if len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        
        if len(contrasena) > 128:
            raise ValueError("La contraseña no debe exceder los 128 caracteres")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
            raise ValueError("La contraseña debe contener al menos un carácter especial")
        
        if not re.search(r'\d', contrasena):
            raise ValueError("La contraseña debe contener al menos un dígito")
        
        if not re.search(r'[A-Z]', contrasena):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        
        if not re.search(r'[a-z]', contrasena):
            raise ValueError("La contraseña debe contener al menos una letra minúscula")
    
    @staticmethod
    def hash_contrasena(contrasena: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(contrasena.encode('utf-8'), salt).decode('utf-8')
    
    @classmethod
    def crear_nuevo(cls, correo: str, contrasena: str, nombre: str, apellido: str) -> 'Usuario':
        cls.validar_correo(correo)
        cls.validar_contrasena(contrasena)
        
        if not nombre.strip():
            raise ValueError("First name cannot be empty")
        
        if not apellido.strip():
            raise ValueError("Last name cannot be empty")
        
        now = datetime.now()
        return cls(
            id=None,
            correo=correo.lower().strip(),
            contrasena_hash=cls.hash_contrasena(contrasena),
            nombre=nombre.strip(),
            apellido=apellido.strip(),
            activo=True,
            created_at=now,
            updated_at=now
        )
    
    def actualizar_correo(self, nuevo_correo: str) -> None:
        self.validar_correo(nuevo_correo)
        self.correo = nuevo_correo.lower().strip()
        self.updated_at = datetime.now()
    
    def cambiar_contrasena(self, nueva_contrasena: str) -> None:
        self.validar_contrasena(nueva_contrasena)
        self.contrasena_hash = self.hash_contrasena(nueva_contrasena)
        self.updated_at = datetime.now()
    
    def actualizar_nombre(self, nombre: str = None, apellido: str = None) -> None:
        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío")
            self.nombre = nombre.strip()
        
        if apellido is not None:
            if not apellido.strip():
                raise ValueError("El apellido no puede estar vacío")
            self.apellido = apellido.strip()
        
        self.updated_at = datetime.now()
    
    def establecer_estado_activo(self, activo: bool) -> None:
        self.activo = activo
        self.updated_at = datetime.now()