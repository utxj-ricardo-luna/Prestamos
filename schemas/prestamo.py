from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class PrestamoBase(BaseModel):
    idPrestamo: int
    idUsuario: int
    idMaterial: int
    tipoUsuario: str
    fechaPrestamo: datetime
    fechaDevolucion: datetime
    estatus: bool
    fechaRegistro: datetime
    fechaActualizacion: datetime

class PrestamoCreate(PrestamoBase):
    pass
class PrestamoUpdate(PrestamoBase):
    pass
class Prestamo(PrestamoBase):
    id: int
    class Config:
        orm_mode = True