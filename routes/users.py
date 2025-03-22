from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud.users
import config.db
from jwt_config import solicita_token
from portadortoken import Portador
import schemas.users
import models.users
from typing import List

user = APIRouter()
# Configurar CORS
user.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo este dominio (o usa ["*"] para todos)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permitir todos los encabezados
)

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@user.get("/users/",response_model=List[schemas.users.User], tags=["Usuarios"], dependencies=[Depends(Portador())])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db = db , skip = skip, limit=limit)
    return db_users
@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"], dependencies=[Depends(Portador())])
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user= crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db, usuario=user.nombreUsuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

@user.put("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"], dependencies=[Depends(Portador())])
async def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"], dependencies=[Depends(Portador())])
async def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_user

@user.post("/login/",response_model=schemas.users.UserLogin, tags=["User Login"])
def read_credentials(usuario:schemas.users.UserLogin, db: Session = Depends(get_db)):
    db_credentials = crud.users.get_user_by_creentials(db, username=usuario.nombreUsuario,correo=usuario.correoElectronico, telefono= usuario.numeroTelefono, password=usuario.contrasena)
    if db_credentials is None:
        return JSONResponse(content={'mensaje':'Acceso denegado'},status_code=404)
    token:str=solicita_token(usuario.dict())
    return JSONResponse(status_code=200,content=token)
