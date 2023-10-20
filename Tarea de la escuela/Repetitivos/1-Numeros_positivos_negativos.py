from os import system
from colorama import *
just_fix_windows_console()

def numeros_positivos(numeros):
    for i in numeros:
        if i > 0:
            print(Fore.LIGHTGREEN_EX,f"{i} es positivo."+Style.RESET_ALL, end=" ")
        else:
            print(Fore.LIGHTRED_EX,f"{i} es negativo."+Style.RESET_ALL, end=" ")

numeros = []
for i in range(3):
    numeros.append(int(input("Numero: ")))

print("")
numeros_positivos(numeros)
