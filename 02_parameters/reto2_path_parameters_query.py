"""Crea un endpoint en FastAPI que permita obtener información de productos específicos utilizando tanto path parameters como query parameters.

Debes crear:

1. Un endpoint con la ruta /products/{product_id} donde product_id es un path parameter de tipo entero  

2. El endpoint debe aceptar tres query parameters opcionales:

include_price: booleano con valor por defecto False
include_stock: booleano con valor por defecto False
format: string con valor por defecto "summary"
3. La función debe devolver un diccionario con:

product_id: el ID del producto recibido como path parameter
name: un string que diga "Producto {product_id}"
category: un string que diga "Categoría {product_id % 3 + 1}" (esto dará categorías 1, 2 o 3)
price: solo si include_price es True, devolver un precio calculado como {product_id * 10}.99
stock: solo si include_stock es True, devolver un stock calculado como {product_id * 5}
format: el valor del query parameter format recibido"""


from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def obtener_producto(product_id: int,
                    include_price: bool = False,
                    include_stock:bool = False,
                    format: str = "summary"):
    
    producto = {"product_id":product_id,
               "name" : f"Producto{product_id}",
               "category" : f"Categoria{product_id % 3 + 1}",
               "format" : format}
    
    if include_price: # añadir precio si include_price es True
        producto["price"] = f"{product_id * 10}.99"
        
    if include_stock: # añadir stock si include_stock es True
        producto["stock"] = product_id * 5 
    
    return producto  
    
    

