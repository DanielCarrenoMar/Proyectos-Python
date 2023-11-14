from random import randrange
from time import sleep
import threading
from os import system
from colorama import Fore, Back, Style
"""
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 """

aciertos = 0
numA = 1
numB = 1
pierde = False
seg = 5

def numero_longitud(long):
    num = ""
    for i in range(long):
        num += str(randrange(0,9))
    return int(num)

def operacion_aleatoria(num1, num2):
    i = randrange(0,100)
    if i >= 0 and i < 25:
        print(F"· {num1} + {num2} ·")
        return num1 + num2
    elif i >= 25 and i < 50:
        print(F"· {num1} - {num2} ·")
        return num1 - num2
    elif i >= 50 and i < 75:
        print(F"· {num1} x {num2} ·")
        return num1 * num2
    elif i >= 75 and i <= 100:
        print(F"· {num1} / {num2} ·")
        return num1 / num2
    
def fin_juego():
    system("cls")
    print(Fore.RED + "PERDISTE" + Style.RESET_ALL)
    print(F"Acertaste {aciertos} veces")
    exit()
    
def crono():
    global seg
    while seg > 0:
        seg -= 1
        sleep(1)
    fin_juego()

threading_emails = threading.Thread(name="cronometro",target=crono)
threading_emails.start()

while True:
    num1 = numero_longitud(numA)
    num2 = numero_longitud(numB)
    resultado =  operacion_aleatoria(num1,num2)
    
    if float(input("Ingrese resultado: ")) != resultado:
        system("cls")
        seg = 0
        break

    seg = 5
    aciertos += 1
    system("cls")
    sleep(1)