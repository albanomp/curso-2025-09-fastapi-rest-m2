from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Endpoint con path parameter (user_id) y query parameters opcionales
@app.get("/users/{user_id}")
def obtener_usuario(user_id: int, include_email: bool = False, format: str = "basic"):
    """
    Endpoint para obtener información de un usuario específico.

    Args:
        user_id (int): ID del usuario (path parameter)
        include_email (bool, opcional): Si True, incluye el email del usuario.
        format (str, opcional): Formato de respuesta. Por defecto "basic".
    """

