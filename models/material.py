from sqlalchemy import Column, Integer, String, DateTime, Enum,Boolean
from config.db import Base
import enum

class TipoMaterial(str,enum.Enum):
    Canion = "Cañon"
    Computadora = "Computadora"
    Laptop = "Laptop"
    CableHDMI = "Cable HDMI"
    Extencion = "Extensión"
    Monitor = "Monitor"
class Estado(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    Mantenimiento = "Mantenimiento"
    
class Material(Base):
    __tablename__="tbb_material"

    id = Column(Integer, primary_key=True,autoincrement=True)
    marca = Column(String(60))
    modelo = Column(String(60))
    tipoMaterial = Column(Enum(TipoMaterial))
    estado = Column(Enum(Estado))
    estatus = Column(Boolean)
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)