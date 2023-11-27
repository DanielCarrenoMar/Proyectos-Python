from colorama import Fore, Back, Style
from os import system
from time import sleep

tablero = [["0","0","0","0","0","1","0","0","0","1"],
           ["0","0","0","0","1","0","0","0","1","0"],
           ["0","0","0","1","0","0","0","1","0","0"],
           ["0","0","1","1","0","0","0","1","0","0"],
           ["0","1","0","1","0","0","0","1","0","0"],
           ["1","0","0","1","0","0","0","1","0","0"],
           ["0","0","0","1","0","0","0","1","0","0"],
           ["0","0","0","1","0","0","0","1","0","0"],
           ["0","0","0","1","0","0","0","1","0","0"],
           ["0","0","0","1","0","0","0","1","0","0"]]

def imprimir(tabla):
    print("-".center(50,"-"))
    for y in range(len(tabla)):
        for x in range(len(tabla[0])):
            match tabla[y][x]:
                case "0":
                    print(Fore.WHITE+"# "+Style.RESET_ALL, end=" ")
                case "1":
                    print(Fore.RED+"X "+Style.RESET_ALL, end=" ")
                case "!":
                    print(Fore.BLUE+"! "+Style.RESET_ALL, end=" ")
                case _:
                    print(tabla[y][x], end=" ")
        print()

def rellenado(tablero,relleno,x,y):
    coord= [(x,y)]
    while len(coord) > 0:
        x,y = coord.pop()
        if tablero[y][x] == "0":
            tablero[y][x] = relleno
            system("cls")
            imprimir(tablero)
            print(coord)
            sleep(0.2)
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i) != abs(j) and 0 <= x+i < len(tablero[0]) and 0 <= y+j < len(tablero):
                    if tablero[y+j][x+i] == "0":
                        if (x+i,y+j) not in coord:
                            print(x+i,y+j)
                            coord.append((x+i,y+j))
                    

rellenado(tablero,"!",9,9)