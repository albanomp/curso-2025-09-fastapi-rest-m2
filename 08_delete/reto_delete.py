"""
Crea una aplicación FastAPI que permita eliminar libros de una biblioteca digital. Debes implementar un endpoint DELETE que elimine un libro específico por su ID.

Instrucciones paso a paso:

1.Importa FastAPI y HTTPException
2.Crea una instancia de FastAPI llamada app
3.Define una lista llamada libros con estos datos iniciales:
4.Implementa un endpoint DELETE en la ruta /libros/{libro_id} que:
ºReciba libro_id como parámetro de tipo entero
ºBusque el libro en la lista por su ID
ºSi encuentra el libro, lo elimine de la lista y devuelva un mensaje de confirmación
ºSi no encuentra el libro, lance una HTTPException con código 404 y el mensaje "Libro no encontrado"
ºEl endpoint debe devolver un diccionario con la clave "mensaje" y el valor "Libro eliminado correctamente" cuando la eliminación sea exitosa.

"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

libros = [
    {"id": 1, "titulo": "El Quijote", "autor": "Cervantes"},
    {"id": 2, "titulo": "Cien años de soledad", "autor": "García Márquez"},
    {"id": 3, "titulo": "1984", "autor": "Orwell"}
]

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for i, libro in enumerate(libros):
        if libro["id"] == libro_id:
            libros.pop(i)
            return {"mensaje": "Libro eliminado correctamente"}
    
    raise HTTPException(status_code=404, detail="404 - Libro no encontrado")


