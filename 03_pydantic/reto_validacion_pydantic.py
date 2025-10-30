"""Crea una aplicación FastAPI con un endpoint POST específico:

Un endpoint en la ruta /productos que reciba información de un producto y devuelva una confirmación de registro.

Requisitos específicos:

1. Crea un modelo Pydantic llamado Producto con los siguientes campos:

nombre: string (obligatorio)
precio: float (obligatorio)
categoria: string (obligatorio)
disponible: boolean (opcional, valor por defecto True)
descripcion: string (opcional, puede ser None)
2. Implementa el endpoint POST que:

Reciba un objeto Producto como parámetro
Devuelva un JSON con un mensaje de confirmación que incluya el nombre del producto y su precio
El mensaje debe tener el formato: "Producto [nombre] registrado con éxito con precio [precio]€"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# modelo
class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    disponible: bool = True
    descripcion: Optional[str]

# ruta post
@app.post("/productos")
def registrar_producto(producto: Producto):
    return {
        "mensaje": f"Producto {producto.nombre} registrado con éxito con precio {producto.precio}€"
    }

