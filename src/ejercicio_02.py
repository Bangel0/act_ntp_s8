# Ejercicio 2: Series con Índices Personalizados
"""Implementa una función que cree una Serie con datos de calificaciones de estudiantes usando índices personalizados (nombres de materias). La función debe:

Crear una Serie con índices personalizados: pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])
Acceder a un valor específico por índice: serie['Ciencias']
Mostrar información básica de la Serie
Calcular estadísticas básicas como suma y promedio"""


import pandas as pd

def calificacionesMateria():
    
    serie = pd.Series([95, 80, 75], index=["Matematicas", "Ingles", "Quimica"])
    
   
    print(serie["Matematicas"])
    print("-----------------------")
    print(serie["Ingles"])
    print("-----------------------")
    print(serie["Quimica"])
    print("-----------------------")
    
   
    print("Información de la Serie:")
    print(serie)
    
    
    print("Suma:", serie.sum())
    print("Promedio:", serie.mean())
    
    
    return serie


calificacionesMateria()
