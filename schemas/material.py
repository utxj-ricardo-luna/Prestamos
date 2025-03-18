from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class MaterialBase(BaseModel):
    marca: str
    modelo: str
    tipoMaterial: str
    estado: str
    estatus: bool
    fechaRegistro: datetime
    fechaActualizacion: datetime

class MaterialCreate(MaterialBase):
    pass
class MaterialUpdate(MaterialBase):
    pass
class Material(MaterialBase):
    id: int
    class Config:
        orm_mode = True