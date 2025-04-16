from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"message":"Hola, Mundo"}

#http://127.0.0.1:8000/libros/3
@app.get("/libros/{id}")
def mostrar_libro(id:int):
    return {"data": id}