from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
import crud.material
import config.db
import schemas.material
import models.material
from typing import List

material = APIRouter()

models.material.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@material.get("/materiales/",response_model=List[schemas.users.User], tags=["Materiales"])
async def read_materiales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_material = crud.material.get_material(db = db , skip = skip, limit=limit)
    return db_material
@material.post("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
@material.post("/material/", response_model=schemas.material.Material, tags=["Materiales"])
def create_material(material: schemas.material.MaterialCreate, db: Session = Depends(get_db)):
    return crud.material.create_material(db=db, material=material)

@material.put("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def update_material(id: int, material: schemas.material.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.material.update_material(db=db, id=id, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no existe, no actualizado")
    return db_material

@material.delete("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def delete_materia(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.delete_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no existe, no se pudo eliminar")
    return db_material