from fastapi import FastAPI
from routes.users import user
from routes.material import material
from routes.prestamo import prestamo

app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de prestamo de material educativo."
)

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)