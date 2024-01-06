"""
* ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
"""

from os import system
from random import randrange

participantes = []

def menu():
    system("cls")
    print("Bienvenido al sorteo de aDEViento".center(50,"-"))
    print("1. Añadir participante")
    print("2. Mostrar participantes")
    print("3. Eliminar participante")
    print("4. Realizar sorteo")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def show(parti):
    system("cls")
    print("Participantes:")
    for parti in parti:
        print(parti)

def lottery(parti):
    system("cls")
    print("Realizando sorteo...".center(50,"-"))
    print("El ganador es: ", parti[randrange(len(parti))])
    input("Pulsa una tecla para continuar...")
while True:
    try:
        choise = menu()
        if choise == "1":
            system("cls")
            nuevo = input("Introduce el nombre del participante: ")
            if nuevo not in participantes: participantes.append(nuevo)
        elif choise == "2":
            show(participantes)
            input("Pulsa una tecla para continuar...")
        elif choise == "3":
            show(participantes)
            print("Eliminar participante".center(50,"-"))
            eliminar = input("Introduce el nombre del participante a eliminar: ")
            if eliminar in participantes: participantes.remove(eliminar)
        elif choise == "4":
            show(participantes)
            print("Realizar sorteo".center(50,"-"))
            input("Pulsa una tecla para realizar el sorteo...")
            lottery(participantes)
        elif choise == "5":
            print("Saliendo del programa...".center(50,"-"))
            break

    except ValueError:
        print("El valor introducido no es correcto")

    