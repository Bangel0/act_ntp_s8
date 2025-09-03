# Ejercicio 4: DataFrame desde Diccionario
"""Desarrolla una función que cree un DataFrame desde un diccionario con datos de productos. La función debe:

Crear un diccionario con las claves: 'Producto', 'Precio', 'Categoria'
Incluir al menos 3 productos con sus datos (ej: Laptop, Smartphone, Tablet)
Convertir el diccionario a DataFrame usando pd.DataFrame(diccionario)
Mostrar el DataFrame completo
Acceder a una columna específica (ejemplo: df['Precio'])
Mostrar información básica del DataFrame con df.info()"""

import pandas as pd

def productos():

    dato= {
        "producto" :["Celular","Ron","Queso"],
        "Precio" :[1000,2500,5000],
        "Categoria": ["Tecnología","licor","lacteos"]
    }

    df =pd.DataFrame(dato)
    print(df)
    print(dato["Precio"])
    print(dato["producto"])
    print(dato["Categoria"])
    print("-----------------------")
    df.info()

productos()
