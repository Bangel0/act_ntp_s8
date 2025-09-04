#Ejercicio 6: DataFrame desde Lista de Listas
"""Implementa una función que cree un DataFrame desde una lista de listas. La función debe:

Crear una lista de listas donde cada sublista representa datos de un libro
Definir los nombres de las columnas: ['Titulo', 'Autor', 'Año']
Crear el DataFrame usando pd.DataFrame(datos, columns=nombres_columnas)
Incluir al menos 3 libros con sus datos
Mostrar el DataFrame y sus dimensiones con df.shape"""


import pandas as pd

def libros():
    
    datos = [
        ["Cien Años de Soledad", "Gabriel García Márquez", 1967],
        ["Don Quijote de la Mancha", "Miguel de Cervantes", 1605],
        ["1984", "George Orwell", 1949]
    ]
    
    nombres_columnas = ['Titulo', 'Autor', 'Año']
    
    df = pd.DataFrame(datos, columns=nombres_columnas)
    
    print("DataFrame de libros:\n")
    print(df)
    print("\nDimensiones del DataFrame:", df.shape)

libros()

