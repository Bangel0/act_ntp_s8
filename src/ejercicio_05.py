# Ejercicio 5: DataFrame desde Lista de Diccionarios
"""Crea una función que genere un DataFrame desde una lista de diccionarios. La función debe:

Crear una lista que contenga diccionarios, cada uno representando un empleado
Cada diccionario debe tener las claves: 'empleado', 'salario', 'departamento'
Incluir al menos 3 empleados con sus datos
Convertir la lista a DataFrame usando pd.DataFrame(lista_diccionarios)
Mostrar el DataFrame resultante
Acceder a filas específicas usando índices"""

import pandas as pd

def pago():

    datos = [

        {"empleado": "Ana", "salario": 2500, "departamento": "Ventas"},
        {"empleado": "Luis", "salario": 3000, "departamento": "IT"},
        {"empleado": "Marta", "salario": 2800, "departamento": "Recursos Humanos"}

        ]

    df = pd.DataFrame(datos)
    print(df)
    print("--------------------")
    print(df.iloc[0])
    print("--------------------") #Se accede al indice por fila
    print(df.iloc[1])
    print("--------------------")
    print(df.iloc[2])

pago()