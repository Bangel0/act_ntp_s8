#Ejercicio 7: Lectura de Archivo CSV
"""Desarrolla una función que:

Cree un archivo CSV usando la biblioteca csv de Python
Escriba datos de al menos 3 cursos con columnas: curso, instructor, duracion
Lea el archivo CSV usando pd.read_csv('cursos.csv')
Muestre el DataFrame resultante
Implemente manejo de errores para el caso de que el archivo no exista"""

import csv
import pandas as pd

def gestionar_cursos():
    nombre_archivo = "cursos.csv"
  
    cursos = [
        ["curso", "instructor", "duracion"],
        ["Python Básico", "Juan Pérez", "20 horas"],
        ["Machine Learning", "Ana Gómez", "35 horas"],
        ["Bases de Datos", "Carlos Ruiz", "25 horas"]
    ]
    
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(cursos)
    
    try:
        df = pd.read_csv(nombre_archivo)
        print("DataFrame de cursos:\n")
        print(df)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")


gestionar_cursos()
