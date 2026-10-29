from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import clientes, productos, pedidos, reportes

app = FastAPI(
    title='Taller 3 ADSO - Tienda',
    version='3.0',
    description='API relacional: clientes, productos, pedidos y detalles'
)

app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(pedidos.router)
app.include_router(reportes.router)
app.mount(
    '/ui',
    StaticFiles(directory=Path(__file__).resolve().parent / 'static', html=True),
    name='ui'
)

@app.get('/', tags=['Inicio'])
def inicio():
    return {'mensaje': 'API tienda ADSO', 'documentacion': '/docs'}
