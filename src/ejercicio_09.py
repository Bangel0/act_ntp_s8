#Ejercicio 9: DataFrame desde Array NumPy
"""Implementa una función que cree un DataFrame desde un array de NumPy. La función debe:

Crear un array de NumPy 2D usando np.array() con datos de ventas trimestrales
El array debe tener al menos 3 filas y 3 columnas con datos numéricos
Especificar los nombres de las columnas al crear el DataFrame
Usar pd.DataFrame(array_numpy, columns=['Q1', 'Q2', 'Q3'])
Mostrar el DataFrame y verificar sus tipos de datos"""

import numpy as np
import pandas as pd

def crear_dataframe_numpy():

    array_numpy = np.array([
        [1500, 2000, 1800],
        [2200, 2100, 2500],
        [1700, 1600, 1900]
    ])

    df = pd.DataFrame(array_numpy, columns=['Q1', 'Q2', 'Q3'])
    
    print("DataFrame de ventas trimestrales:\n")
    print(df)
    
    print("\nTipos de datos en cada columna:\n")
    print(df.dtypes)

crear_dataframe_numpy()
