import models.material
import schemas.material
from sqlalchemy.orm import Session

def get_material(db: Session, id: int):
    return db.query(models.material.Material).filter(models.material.Material.id == id).first()
def get_user_by_marca(db: Session, material: str):
    return db.query(models.material.Material).filter(models.material.Material.marca == material).first()
def get_materiales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.material.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.material.MaterialCreate):
    db_material = models.material.Material(
        marca = material.marca,
        primerApellido = material.modelo,
        segundoApellido = material.tipoMaterial,
        estado = material.estado,
        estatus = material.estatus,
        fechaRegistro = material.fechaRegistro,
        fechaActualizacion = material.fechaActualizacion 
        )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: schemas.material.MaterialUpdate):
    db_material = db.query(models.material.Material).filter(models.material.Material.id == id).first()
    if db_material:
        for var, value in vars(material).items():
            setattr(db_material, var, value) if value else None
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(models.material.Material).filter(models.material.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
