from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import json
import crud.prestamo
import config.db
import schemas.prestamo
import models.prestamo
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

key=Fernet.generate_key()
f = Fernet(key)

prestamo = APIRouter()

models.prestamo.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@prestamo.get("/prestamos/",response_model=List[schemas.prestamo.Prestamo], tags=["Prestamos"], dependencies=[Depends(Portador())])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_prestamos = crud.prestamo.get_prestamos(db = db , skip = skip, limit=limit)
    return db_prestamos
@prestamo.post("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Prestamos"], dependencies=[Depends(Portador())])
async def read_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo= crud.prestamo.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo
@prestamo.post("/prestamo/", response_model=schemas.prestamo.Prestamo, tags=["Prestamos"], dependencies=[Depends(Portador())])
def create_user(prestamo: schemas.prestamo.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamo.create_prestamo(db=db, prestamo=prestamo)

@prestamo.put("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Prestamos"], dependencies=[Depends(Portador())])
async def update_prestamo(id: int, prestamo: schemas.prestamo.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamo.update_prestamo(db=db, id=id, prestamo=prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no existe, no actualizado")
    return db_prestamo

@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Prestamos"], dependencies=[Depends(Portador())])
async def delete_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamo.delete_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no existe, no se pudo eliminar")
    return db_prestamo