<<<<<<< HEAD
#Ejecuar en la terminal: uvicorn nombre_Carpeta.nombre_fichero:app --reload | uvicorn 01_metodos_GET.prueba:app --reload

from typing import Union
=======
# EJECUTAR EN LA TERMINAL: uvicorn 01_metodos_GET.prueba:app --reload
>>>>>>> 3b99a89795d9caea9c654fbf6f2a3d4ba6cebbb5

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"Hello": "World"}
=======
    return {"Hello": "World"}
>>>>>>> 3b99a89795d9caea9c654fbf6f2a3d4ba6cebbb5
