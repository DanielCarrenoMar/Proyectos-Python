"""
Hacer un programa en Python que encuentre e imprima la matriz transpuesta de una matriz MAT.
La matriz transpuesta de la matriz MAT se encuentra intercambiando las filas por las columnas y las columnas por las filas.

"""
from random import randint
from colorama import Fore, Back, Style, just_fix_windows_console
just_fix_windows_console()

def mostrar_matriz(matriz,color):
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            print(color,matriz[y][x], end = " ")
        print(Style.RESET_ALL)

def matriz_transpuesta(matriz):
    Tfila = []
    Tmatriz = []

    for x in range(len(matriz[0])):
        for y in range(len(matriz)):
            Tfila.append(matriz[y][x])

        Tmatriz.append(Tfila)
        Tfila = []

    return Tmatriz

while True:
    try:
        filas = int(input(F"Ingrese el número de {Back.LIGHTBLACK_EX}filas{Style.RESET_ALL}: "))
        columnas = int(input(F"Ingrese el número de {Back.LIGHTBLACK_EX}columnas{Style.RESET_ALL}: "))
        break
    except ValueError:
        print(Fore.RED + "Error, ingrese un número entero" + Style.RESET_ALL)

matriz = [[randint(0,9) for x in range(columnas)] for y in range(filas)]
Tmatriz = []

Tmatriz = matriz_transpuesta(matriz)

print(Fore.BLACK + Back.BLUE + "La matriz original es: " + Style.RESET_ALL)
mostrar_matriz(matriz, Back.LIGHTBLUE_EX+Fore.BLACK)
print(Fore.BLACK + Back.RED + "La matriz transpuesta es: " + Style.RESET_ALL)
mostrar_matriz(Tmatriz, Back.LIGHTRED_EX+Fore.BLACK)
