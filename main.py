from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# ✅ Middleware CORS para aceptar peticiones desde cualquier origen (como tu frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "*" por tu dominio si lo deseas restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ruta raíz opcional
@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido a la Caracola Mágica!"}

# ✅ Ruta principal que recibe lista de palabras y devuelve una al azar
@app.post("/elegir")
async def elegir(request: Request):
    datos = await request.json()
    opciones = datos.get("palabras", [])  # Coincide con el frontend

    if not opciones or not isinstance(opciones, list):
        return JSONResponse(content={"error": "Se necesita una lista de palabras"}, status_code=400)

    palabra_elegida = random.choice(opciones)
    return {"palabra_elegida": palabra_elegida}

# ✅ Ruta para UptimeRobot
@app.api_route("/ping", methods=["GET", "HEAD"])
def ping():
    return {"status": "ok"}
