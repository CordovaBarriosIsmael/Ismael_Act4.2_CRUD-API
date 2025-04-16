#servicios web
#Alumno: Ismael Cordova Barrios
#Fecha: 15 - Abril - 2025

from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

menu_data: List[Dict[str, any]] = [
    {"id": 1, "nombre": "Hamburguesa Clásica", "descripcion": "Deliciosa hamburguesa de carne con queso, lechuga, tomate y cebolla."},
    {"id": 2, "nombre": "Papas Fritas", "descripcion": "Crujientes papas fritas sazonadas."},
    {"id": 3, "nombre": "Refresco Grande", "descripcion": "Refresco de cola de 600 ml."},
    {"id": 4, "nombre": "Hot Dog Especial", "descripcion": "Pan con salchicha, mostaza, catsup y cebolla caramelizada."},
    {"id": 5, "nombre": "Nuggets de Pollo (6 piezas)", "descripcion": "Nuggets de pollo empanizados y crujientes."},
]

#http://127.0.0.1:8000/menu
@app.get("/menu")
def obtener_menu():
    """
    Devuelve la lista de platillos del menú con ID y la cantidad total.
    """
    cantidad_menu = len(menu_data)
    return {"cantidad": cantidad_menu, "menu": menu_data}


#http://127.0.0.1:8000/menu/1
#http://127.0.0.1:8000/menu/2
#http://127.0.0.1:8000/menu/3
#http://127.0.0.1:8000/menu/4
#http://127.0.0.1:8000/menu/5
@app.get("/menu/{item_id}")
def obtener_item_menu(item_id: int):
    """
    Devuelve la información de un platillo específico del menú por su ID.
    """
    for item in menu_data:
        if item["id"] == item_id:
            return {"item": item}
    return {"mensaje": f"Ítem con ID {item_id} no encontrado en el menú"}

@app.get("/")
def index():
    return {"message": "Bienvenido a la API de Sabor Xpress. Visita /menu para ver nuestro menú con IDs y cantidad."}
