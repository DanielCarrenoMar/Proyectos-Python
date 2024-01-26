from Global import  impriMat
from random import randint

Title = "Recorrer matriz escalera"

def program():
    dim = 5
    dezpla = 1

    mat = [[randint(1,9) for _ in range(dim)] for _ in range(dim)]

    impriMat(mat)

    print("".center(30, "-"))
    for j in range(dim-dezpla, -1, -1):
        for i in range(j):
            mat[i][j] = 0

    impriMat(mat)

program()