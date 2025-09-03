# Ejercicio 3: Operaciones Matemáticas con Series
"""Desarrolla una función que cree dos Series de precios y descuentos, y realice operaciones matemáticas entre ellas. La función debe:

Crear dos Series: precios [100, 150, 200] y descuentos [10, 20, 15]
Realizar resta entre precios y descuentos
Multiplicar la Serie de precios por un valor escalar (ejemplo: precios * 1.16 para IVA)
Mostrar los resultados de todas las operaciones
Demostrar que las operaciones se realizan elemento por elemento"""

import pandas as pd

def promocion():
    
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])
    
  
    resta = precios - descuentos
    precios_iva = precios * 1.16  
    

    print("Precios originales:\n", precios)
    print("----------------------------")
    print("\nDescuentos:\n", descuentos)
    print("----------------------------")
    print("\nResta (precios - descuentos):\n", resta)
    print("----------------------------")
    print("\nPrecios con IVA (precios * 1.16):\n", precios_iva)


promocion()

