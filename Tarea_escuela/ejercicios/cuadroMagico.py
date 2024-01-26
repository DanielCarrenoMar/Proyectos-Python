from Global import pedirDatos, impriMat, crearMat
from time import sleep

def program():
    dim = pedirDatos("int", "Ingrese la dimension de la matriz: ")

    mat = crearMat(dim)
    impriMat(mat)
    
    x = 1
    y = 0
    dim -= 1

    for i in range(1,len(mat)*len(mat[0])+1):
        print("--------")
        mat[y][x] = i
        print(x,y)
        impriMat(mat)

        y -= 1
        x += 1

        if x < 0: x = dim
        if x > dim: x = 0

        if y < 0: y = dim
        if y > dim: y = 0

        if mat[y][x] != 0:
            y += 1
            x -= 1

            if x < 0: x = dim
            if x > dim: x = 0

            if y < 0: y = dim
            if y > dim: y = 0

            y += 1

        sleep(0.5)

program()