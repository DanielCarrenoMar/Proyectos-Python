from numpy import *
from numpy.random import shuffle
from random import randint
from colorama import *
just_fix_windows_console()
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
        while True:
            try:
                print(" ")
                x = int(input(Style.RESET_ALL+"elija una casilla.X: "))
                if x == -1:
                    exit()
                y = int(input("elija una casilla.Y: "))
                choise = campo_minas[y-1, x-1]
                break
            except:
                 print("Eliga un numero valido")        
        if choise == -1:
            print(Fore.RED + "EXPLOSION")
            pantalla[y-1, x-1] = -1
            print(Style.RESET_ALL, pantalla)
            break
        else:
            print(Fore.GREEN + "SEGURA")
            bombas = 0
            #OOO
            #O0X
            #OOO
            try:
                #print("derecha",campo_minas[y-1, x])
                if campo_minas[y-1, x] == -1:
                    bombas += 1
            except:
                pass
            #OOO
            #X0O
            #OOO
            try:
                if x-2 >= 0:
                    #print("izquie",campo_minas[y-1, x-2])
                    if campo_minas[y-1, x-2] == -1:
                        bombas += 1
            except:
                pass
            #OOO
            #O0O
            #OXO
            try:
                #print("abajo",campo_minas[y, x-1])
                if campo_minas[y, x-1] == -1:
                        bombas += 1
            except:
                   pass
            #OOO
            #O0O
            #OOX
            try:
                #print("abajo derecha",campo_minas[y, x])
                if campo_minas[y, x] == -1:
                        bombas += 1
            except:
                   pass
            #OOO
            #O0O
            #XOO
            try:
                if x-2 >= 0:
                    #print("abajo izquie",campo_minas[y, x-2])
                    if campo_minas[y, x-2] == -1:
                            bombas += 1
            except:
                   pass
            #XOO
            #O0O
            #OOO
            try:
                if x-2 >= 0 and y-2 >= 0:
                    #print("arriba izquie",campo_minas[y-2, x-2])
                    if campo_minas[y-2, x-2] == -1:
                            bombas += 1
            except:
                   pass
            #OOX
            #O0O
            #OOO
            try:
                if y-2 >= 0:
                    #print("arriba derecha",campo_minas[y-2, x])
                    if campo_minas[y-2, x] == -1:
                            bombas += 1
            except:
                   pass
            #OXO
            #O0O
            #OOO
            try:
                if y-2 >= 0:
                    #print("arriba",campo_minas[y-2, x-1])
                    if campo_minas[y-2, x-1] == -1:
                            bombas += 1
            except:
                pass
            
            if bombas != 0:
                pantalla[y-1, x-1] = bombas
            else:
                pantalla[y-1, x-1] = 10
            print(Style.RESET_ALL, pantalla)
# Crear el campo de minas
#XY = [input("Ingrese dos numeros separados por comas: ").split(",")]
XY = [6,6]
campo_minas = crear_campo(XY, 6)
pantalla =  zeros(XY)

#JUEGO
print(Fore.BLACK+Back.WHITE+"BUSCAMINAS"+Style.RESET_ALL)
print("")
print(pantalla)
juego()


