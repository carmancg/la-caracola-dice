from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# ✅ CORS para evitar error 405 con OPTIONS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con tu dominio si lo deseas restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la Caracola Mágica!"}

@app.post("/elegir")
async def elegir(request: Request):
    datos = await request.json()
    opciones = datos.get("opciones", [])
    
    if not opciones or not isinstance(opciones, list):
        return JSONResponse(content={"error": "Se necesita una lista de opciones"}, status_code=400)
    
    palabra_elegida = random.choice(opciones)
    return {"palabra_elegida": palabra_elegida}

@app.api_route("/ping", methods=["GET", "HEAD"])
def ping():
    return {"status": "ok"}
