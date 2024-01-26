from Global import pedirDatos
from os import system
from colorama import Fore
from random import randint
"""
Celula, nombre y calificacion de 3 parciales. Ordenar de manera decendente segun promedio
"""

Title = "Almacenar Calificacion de alumnos"

def program():
    datos = []
    add = []
    suma = 0
    numAlum = 2
    colors = [Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN]
    color = randint(0,len(colors)-1)

    for i in range(1, numAlum+1):
        color += 1
        color %= len(colors)

        add.append(pedirDatos("str", F"{colors[color]}({i}){Fore.RESET} Ingrese su celula: "))
        add.append(pedirDatos("str", F"{colors[color]}({i}){Fore.RESET} Ingrese su nombre: "))
        for j in range(1, 4): 
            nota = pedirDatos("nota20", F"{colors[color]}({i}){Fore.RESET} Ingrese la calificacion del parcial {j}: ")
            suma += nota 
            add.append(nota)

        add.append(round(suma/3))
        datos.append(add)
        add = []
    
    system("cls")
    for i in range(len(datos)-1):
        if datos[i][5] < datos[i+1][5]:
            temp = datos[i+1]
            datos[i+1] = datos[i]
            datos[i] = temp

    for dato in datos:
        print(F"Promedio: {dato[5]}. Nombre: {dato[0]}, cedula: {dato[1]}, parcial 1: {dato[2]}, parcial 2: {dato[3]}, parcial 3: {dato[4]}")


program()