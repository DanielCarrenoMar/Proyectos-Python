import ejercicios as ej
from os import system
from colorama import *
just_fix_windows_console()

def pedir_opcion_valida(opciones):
    while True:
        try:
            opcion = int(input("Elija una opcion: "))
            if opcion in opciones:
                return opcion
            else:
                print("Opcion invalida")
        except ValueError:
            print("Opcion invalida")

# Listas de las distintas funciones
repetitivas = []
condicionales = []

#Agregar todas las funciones y clasificarlas por su tipo
for nombre in dir(ej):
    objeto = getattr(ej, nombre)
    
    if objeto.__class__.__name__ == 'function' and nombre.startswith('f_'):
        if nombre.endswith('_repe'):
            repetitivas.append(nombre)
        elif nombre.endswith('_cond'):
            condicionales.append(nombre)

print("MENU DE TAREAS".center(50, "-"))
print("")

print("1 - CONDICIONALES")
print("2 - REPETITIVAS")
print("")

seleccion = pedir_opcion_valida([1, 2])

system('cls')

if seleccion == 1:
    print("CONDICIONALES".center(50, " "))
    print("".center(50, "-"))

    for cond in condicionales:
        print(f"{condicionales.index(cond)+1} - {cond[2:-5].replace('_', ' ').capitalize()}")

    seleccion = pedir_opcion_valida(range(1, len(condicionales)+1))

    system('cls')
    
    eval("ej."+condicionales[seleccion-1])()

elif seleccion == 2:
    print("REPETITIVAS".center(50, " "))
    print("".center(50, "-"))
    
    for repe in repetitivas:
        print(f"{repetitivas.index(repe)+1} - {repe[2:-5].replace('_', ' ').capitalize()}")

    seleccion = pedir_opcion_valida(range(1, len(repetitivas)+1))

    system('cls')

    eval("ej."+repetitivas[seleccion-1])()
