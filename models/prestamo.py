from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import models.users
import models.material
import enum

class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"
class Prestamo(Base):
    __tablename__="tbb_prestamo"

    id = Column(Integer, primary_key=True,autoincrement=True)
    idUsuario = Column(Integer, ForeignKey("tbb_usuarios.id"), primary_key=True)
    idMaterial = Column(Integer, ForeignKey("tbb_material.id"), primary_key=True)
    fechaPrestamo = Column(DateTime)
    fechaDevolucion = Column(DateTime)
    estatus = Column(Boolean)
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

