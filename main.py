
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PalabrasEntrada(BaseModel):
    palabras: list[str]

@app.post("/elegir")
def elegir_palabra(entrada: PalabrasEntrada):
    elegida = random.choice(entrada.palabras)
    return {"palabra_elegida": elegida}
