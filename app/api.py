from fastapi import FastAPI

app = FastAPI()


@app.get("/hola/{nombre}", response_model=dict)
async def hello(nombre: str):
    """
    Saluda a la persona con el nombre proporcionado.

    Args:
        name (str): El nombre de la persona a saludar.

    Returns:
        dict: Un diccionario que contiene el nombre saludo.
    """
    return {
        "nombre": nombre
    }
