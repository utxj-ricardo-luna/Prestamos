from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime

class UserCreate(UserBase):
    pass
class UserUpdate(UserBase):
    pass
class User(UserBase):
    id: int
    class Config:
        orm_mode = True
class UserLogin(BaseModel):
    nombreUsuario: Optional[str] = None
    correoElectronico: Optional[str] = None
    numeroTelefono: Optional[str] = None
    contrasena: str
