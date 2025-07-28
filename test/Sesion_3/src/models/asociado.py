from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Asociado(Base):
    __tablename__ = "asociados"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    edad: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Asociado(id={self.id!r}, nombre={self.nombre!r}, edad={self.edad!r})"