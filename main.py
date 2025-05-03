from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes poner ["https://tu-usuario.github.io"] para más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PalabrasInput(BaseModel):
    palabras: list[str]

@app.post("/elegir")
def elegir_palabra(data: PalabrasInput):
    return {"palabra_elegida": random.choice(data.palabras)}

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la Caracola Mágica!"}

@app.post("/elegir")
async def elegir(request: Request):
    datos = await request.json()
    opciones = datos.get("opciones", [])
    if not opciones:
        return JSONResponse(content={"error": "No se proporcionaron opciones"}, status_code=400)
    return {"palabra_elegida": random.choice(opciones)}

# ✅ Este es el nuevo endpoint para UptimeRobot
@app.get("/ping")
def ping():
    return {"status": "ok"}

