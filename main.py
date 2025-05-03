from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

# Endpoint raíz, opcional, útil para pruebas
@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la Caracola Mágica!"}

# Endpoint principal: POST con lista de opciones
@app.post("/elegir")
async def elegir(request: Request):
    datos = await request.json()
    opciones = datos.get("opciones", [])
    
    if not opciones or not isinstance(opciones, list):
        return JSONResponse(content={"error": "Se necesita una lista de opciones"}, status_code=400)
    
    palabra_elegida = random.choice(opciones)
    return {"palabra_elegida": palabra_elegida}

# Endpoint para monitoreo desde UptimeRobot
@app.get("/ping")
def ping():
    return {"status": "ok"}
