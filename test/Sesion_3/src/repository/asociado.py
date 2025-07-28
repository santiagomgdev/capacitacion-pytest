from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.interface.asociado import AsociadoInterface
from src.models.asociado import Asociado

asociado = Asociado()

def obtener_asociado(nombre_asociado: str) -> AsociadoInterface:
    conexion = create_engine("mysql+pymysql://usuario:hola123@172.20.1.20:3306/bdatlantissico", echo=True)
    sesion = Session(conexion)
    
    consulta = select(Asociado).where(Asociado.nombre == nombre_asociado) # SQLAlchemy lo define como stmt -> statement
    asociado = sesion.execute(consulta).scalar()

    return AsociadoInterface(
        id=asociado.id,
        nombre=asociado.nombre,
        edad=asociado.edad
    )
