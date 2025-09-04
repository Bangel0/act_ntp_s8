#Ejercicio 10:
"""Desarrolla una función que consuma datos desde la API https://playground.mockoon.com/users. La función debe:

Importar la biblioteca requests
Realizar una petición GET a la URL usando requests.get()
Verificar que el código de estado sea 200
Convertir la respuesta JSON a DataFrame usando pd.DataFrame(response.json())
Mostrar las primeras 5 filas con df.head()
Implementar manejo de errores con try/except para problemas de conexión
Mostrar información del DataFrame obtenido"""


import requests
import pandas as pd

def obtener_usuarios_api():
    url = "https://playground.mockoon.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return

    try:
        datos = response.json()
    except ValueError as e:
        print(f"Error al decodificar JSON: {e}")
        return


    try:
        df = pd.DataFrame(datos)
    except Exception as e:
        print(f"Error al crear DataFrame: {e}")
        return


    print("Primeras 5 filas del DataFrame:\n")
    print(df.head(), "\n")


    print("Información del DataFrame:\n")
    print(df.info())


obtener_usuarios_api()
