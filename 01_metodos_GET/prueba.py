#Ejecuar en la terminal: uvicorn nombre_Carpeta.nombre_fichero:app --reload | uvicorn 01_metodos_GET.prueba:app --reload

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
