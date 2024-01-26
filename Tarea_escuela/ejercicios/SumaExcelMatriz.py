from random import randint
from Global import impriMat

"""
Una matriz que al final de cada Fila/Columa se sume el total de la 
Fila/columna y en esquina inferior derecha se sume el total de la matriz
"""

title = "Suma de Matriz"

def program():
    DimX, DimY = int(input("Ingrese ancho: ")), int(input("Ingrese alto: "))

    matriz = [[randint(0,9) for _ in range(DimX)] for _ in range(DimY)]

    impriMat(matriz)

    print("".center(30, "-"))
    newmatriz = matriz.copy()

    for y in range(DimY):
        for x in range(DimX):
            pass

    impriMat(newmatriz)

program()