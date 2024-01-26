from Global import  impriMat
from random import randint

Title = "Recorrer matriz reloj de arena"

def program():
    dim = int(input("Ingrese dimension de la matriz: "))

    mat = [[randint(1,9) for _ in range(dim)] for _ in range(dim)]

    impriMat(mat)

    print("".center(30, "-"))

    for j in range(dim):
        for i in range(0+j,dim-j) :
            mat[j][i] = 0

    for j in range(dim-1,-1,-1):
        for i in range(0+j,dim-2-j,-1) :
            mat[j][i] = 0

    impriMat(mat)

program()