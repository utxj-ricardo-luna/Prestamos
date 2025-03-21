import models.prestamo
import schemas.prestamo
from sqlalchemy.orm import Session

def get_prestamo(db: Session, id: int):
    return db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id == id).first()
def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.prestamo.Prestamo).offset(skip).limit(limit).all()
def create_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoCreate):
    db_prestamo = models.prestamo.Prestamo(
        idUsuario = prestamo.idUsuario,
        idMaterial = prestamo.idMaterial,
        fechaPrestamo = prestamo.fechaPrestamo,
        fechaDevolucion = prestamo.fechaDevolucion,
        estatus = prestamo.estatus,
        fechaRegistro = prestamo.fechaRegistro,
        fechaActualizacion = prestamo.fechaActualizacion 
        )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id: int, prestamo: schemas.prestamo.PrestamoUpdate):
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id == id).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            setattr(db_prestamo, var, value) if value else None
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
