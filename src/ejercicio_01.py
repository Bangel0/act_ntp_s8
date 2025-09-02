# Ejercicio 1: Análisis de Ventas Diarias con Series
"""
Crea una función que genere una Serie de Pandas con las ventas diarias de una tienda (7 días). La función debe:

Crear una Serie con ventas diarias (ejemplo: [150, 200, 180, 220, 175, 190, 165])
Acceder al valor del índice 3 usando serie[3]
Calcular el promedio de ventas usando .mean()
Ordenar por valores usando .sort_values()
Mostrar todos los resultados con print()
"""


import pandas 

def VentasDiarias ():


    VentasDiarias = pandas.Series([300,750,520,360,124,250,100])

    print (VentasDiarias[3])
    print ("---------------------------")
    print(VentasDiarias.mean())
    print ("---------------------------")
    print(VentasDiarias.sort_values())
    print ("---------------------------")

VentasDiarias()