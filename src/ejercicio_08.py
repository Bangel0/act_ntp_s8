#Ejercicio 8: DataFrame desde Archivo JSON
"""Crea una función que:

Genere un archivo JSON con una estructura de lista de objetos
Cada objeto debe representar un vehículo con propiedades: marca, modelo, año
Guarde el archivo usando la biblioteca json de Python
Lea el archivo usando pd.read_json('vehiculos.json')
Muestre el DataFrame resultante y sus tipos de datos con df.dtypes"""

import json
import pandas as pd

def vehiculos():
    lista_vehiculos = "vehiculos.json"
    
    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Mustang", "año": 2018},
        {"marca": "Chevrolet", "modelo": "Onix", "año": 2021}
    ]
    
    with open(lista_vehiculos, "w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, ensure_ascii=False, indent=4)
    

    try:
        df = pd.read_json(lista_vehiculos)
        print("DataFrame de vehículos:\n")
        print(df)
        print("\nTipos de datos en cada columna:\n")
        print(df.dtypes)
    except FileNotFoundError:
        print(f"Error: El archivo '{lista_vehiculos}' no existe.")

vehiculos()

