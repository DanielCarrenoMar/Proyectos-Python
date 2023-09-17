from numpy import *
from numpy.random import shuffle
from random import randint
from colorama import *

#FUNCIONES
#Crear un campo de minas desordenado con minas personalizadas
def crear_campo(XY, bombas):
    lista = []
    for list in range(XY[0] * XY[1]):
        if list >= bombas:
            lista.append(0)
        else:
            lista.append(-1)
    shuffle(lista)
    campo = array(lista).reshape(XY[0],XY[1])
    shuffle(campo)
    return(campo)

def juego ():
    
    while True:
        x = int(input(Style.RESET_ALL+"elija una casilla.X: "))
        y = int(input("elija una casilla.Y: "))
        #try:
        choise = campo_minas[y-1, x-1]
        if choise == -1:
            print(Fore.RED + "EXPLOSION")
            pantalla[y-1, x-1] = -1
            print(Style.RESET_ALL, pantalla)
            break
        else:
            print(Fore.GREEN + "SEGURA")
            pantalla[y-1, x-1] = 7
            print(Style.RESET_ALL, pantalla)
        #except:
            print("ingresar numero valido")
   



ejemplo = array([[ 0,  0, -1,  0,  0,  0,  0,  0],
                [-1,  0,  0,  0, -1,  0,  0,  0],
                [ 0,  0,  0,  0, -1,  0,  0, -1],
                [ 0,  0, -1,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0, -1,  0],
                [ 0, -1,  0,  0, -1,  0,  0,  0],
                [ 0,  0, -1,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0]])

# Crear el campo de minas
# XY = [input("Ingrese dos numeros separados por comas: ").split(",")]
XY = [2,2]
campo_minas = crear_campo(XY, 2)
pantalla = zeros(XY)

print(campo_minas)
print(" ")
print(pantalla)
juego()


