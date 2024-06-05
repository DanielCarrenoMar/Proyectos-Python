import datetime
from os import system
from colorama import Fore, just_fix_windows_console, Back, Style

"""
1.-Usando archivos de texto (secuenciales), crear las siguientes estructuras de
archivos, para el registro de los empleados de la UCAB:
Departamentos ( CódigoDpto, NombreDpto) y
Empleados (Cédula, Nombre, Sexo, CodigoDpto, Sueldo)
o Para el Sexo use los valores “M” y “F”
o Para los CódigosDpto use valores enteros
Para ello, elabore los programas en Python que :
* Reciba por pantalla los Códigos y nombre de los departamentos y los almacene
    en un archivo llamado DEPARTAMENTOS
* Reciba por pantalla la cédula, el nombre, el sexo, el código del departamento y
    el sueldo de cada uno de los Empleados y los almacene en un archivo llamado
    EMPLEADOS. El programa debe permitir ingresar varios empleados hasta que
    el usuario decida no ingresar más. No solicitar con antelación la cantidad de
    empleados a almacenar.
* A partir de los archivos creados , DEPARTAMENTOS y EMPLEADOS, generar
    un listado (archivo de salida tipo TEXTO) llamado REPORTE que contenga por
    Depatamento los Empleados que tienen un sueldo en un rango dado..
    El archivo de salida (al que llamaremos Reporte.TXT) debe mostrar el titulo
    “Empleados por departamento con sueldo entre xxxx – yyyyy Bs.“ y luego para cada
    Departamento mostrar su Código y su Nombre y debajo debe mostrar la cédula,
    nombre , sexo y sueldo de los empleados. A CONTINUACIÓN SE DA UN
    EJEMPLO DEL REPORTE DE SALIDA SOLICITADO. Este ejercicio deben
    hacerlo luego usando los archivos de entrada en formato Binario. 
"""

def cabeceraTXT(txt:str, maxSueldo, minSueldo, departamento):
    date = datetime.datetime.now()
    fecha = f"{date.year}/{date.month}/{date.day}"
    hora = f"{date.hour}:{date.minute}"
    with open(txt, "w") as t:
        t.write(f"UCAB                                                        FECHA : {fecha}\n")
        t.write(f"                                                            HORA : {hora}\n")
        t.write("                    EMPLEADOS POR DEPARTAMENTOS\n")
        t.write(f"                CON SUELDO Entre {minSueldo} y {maxSueldo} Bs\n")
        t.write(f"DEPARTAMENTO : {departamento}\n")
        t.write(f"\n")
        t.write(f" CEDULA:          NOMBRE:           SEXO:             SUELDO:\n")
        t.write(f"********         ********          ********         *********\n")
        t.write(f"\n")

def pedirMenu(text, min, max):
    while True:
        print(text, end="")
        try:
            valor = abs(int(input()))
            if min <= valor <= max:
                break
            print(Fore.RED+"Ingrese una opccion valida"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Ingrese una opccion valida"+Style.RESET_ALL)

    return valor

def pedirNum(text):
    while True:
        print(text, end="")
        try:
            valor = abs(int(input()))
            break
        except ValueError:
            print(Fore.RED+"Ingrese un valor valida"+Style.RESET_ALL)

    return valor

def pedirSexo(text):
    while True:
        print(text, end="")
        valor = input()
        if valor.lower() == "m" or valor.lower() == "f":
            break
        print(Fore.RED+"Ingrese un valor valida"+Style.RESET_ALL)

    return valor.upper()

def layer_menu():
    global page
    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print(f"{Fore.RED}1.{Fore.BLUE} Agregar departamento")
    print(f"{Fore.RED}2.{Fore.BLUE} Agregar empleado")
    print(f"{Fore.RED}3.{Fore.BLUE} Generar reporte")
    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print(Style.RESET_ALL, end="")
    
    page =  pedirMenu("OPCCION: ", 1, 3)
    system("cls")

def layer_agregarDepartamento():
    global page
    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print("CREAR DEPARTAMENTO")
    print("".center(30, "-"))
    print(Style.RESET_ALL, end="")

    codigo = pedirNum("Codigo: ")

    print("Nombre: ", end="")
    nombre = input()

    with open("DEPARTAMENTOS.bin", "rb") as f:
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            print(lineaFormat[0], str(codigo))
            if lineaFormat[0] == str(codigo):
                system("cls")
                print(f"{Fore.RED}ERROR: Codigo de departamento repetido{Style.RESET_ALL}")
                return

    with open("DEPARTAMENTOS.bin", "ab") as f:
        f.write(f"{codigo}|{nombre}\n".encode())

    page = 0
    system("cls")

def layer_agregarEmpleado(): # Empleados (Cédula, Nombre, Sexo, CodigoDpto, Sueldo)
    global page
    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print("AÑADIR EMPLEADO")
    print("Departamentos:")

    with open("DEPARTAMENTOS.bin", "rb") as f:
        existe = False
        print(Fore.BLUE, end="")
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            print("* "+lineaFormat[1]+ ": "+ lineaFormat[0])

    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print(Style.RESET_ALL, end="")

    cedula = pedirNum("Cedula: ")

    print("Nombre: ", end="")
    nombre = input()

    sexo = pedirSexo("Sexo (M / F): ")

    codigo = pedirNum("Codigo de departamento: ")

    sueldo = pedirNum("Sueldo en bs: ")

    with open("DEPARTAMENTOS.bin", "rb") as f:
        existe = False
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            if lineaFormat[0] == str(codigo):
                existe = True
        if not  existe:
            system("cls")
            print("ERROR: Codigo de departamento inexistente")
            return

    with open("EMPLEADOS.bin", "rb") as f:
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            if lineaFormat[0] == str(cedula):
                system("cls")
                print(f"{Fore.RED}ERROR: Cedula de empleado repetida{Style.RESET_ALL}")
                return

    with open("EMPLEADOS.bin", "ab") as f:
        f.write(f"{cedula}|{nombre}|{sexo}|{codigo}|{sueldo}\n".encode())

    page = 0
    

    system("cls")
    pass

def layer_generarReporte():
    global page
    depaNombre = ""
    print(Fore.GREEN, end="")
    print("".center(30, "-"))

    print("GENERAR REPORTE")

    with open("DEPARTAMENTOS.bin", "rb") as f:
        existe = False
        print(Fore.BLUE, end="")
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            print("* "+lineaFormat[1]+ ": "+ lineaFormat[0])

    print(Fore.GREEN, end="")
    print("".center(30, "-"))
    print(Style.RESET_ALL, end="")

    depaCodigo = pedirNum("Codigo de departamento: ")
    minSueldo = pedirNum("Rango e sueldo inferior: ")
    maxSueldo = pedirNum("Rango e sueldo superior: ")

    with open("DEPARTAMENTOS.bin", "rb") as f:
        existe = False
        while linea := f.readline():
            lineaFormat = linea.decode().replace("\n", "").split("|")
            if lineaFormat[0] == str(depaCodigo):
                cabeceraTXT("REPORTE.txt", minSueldo, maxSueldo, f"{lineaFormat[1]} {lineaFormat[0]}")
                existe = True
                break
        if not  existe:
            system("cls")
            print(f"{Fore.RED}ERROR: Codigo de departamento inexistente{Style.RESET_ALL}")
            return

    with open("REPORTE.txt", "a") as fRepor:
        total = 0
        totalGeneral = 0
        with open("EMPLEADOS.bin", "rb") as fEmple:
            while linea := fEmple.readline():
                lineaFormat = linea.decode().replace("\n", "").split("|")
                totalGeneral += 1
                if lineaFormat[3] == str(depaCodigo) and  minSueldo < int(lineaFormat[4]) < maxSueldo:
                    fRepor.write(f"{lineaFormat[0]}            {lineaFormat[1]}                {lineaFormat[2]}                  {lineaFormat[4]}\n")
                    total += 1
        fRepor.write(f"                      Total de empleados {total}\n")
        fRepor.write(f"Total GENERAL de empleados {totalGeneral}\n")

    input("Reporte hecho. pulsa enter para continuar...")

    page = 0    
    system("cls")

page = 0
def main ():
    system("cls")
    try:
        open("DEPARTAMENTOS.bin", "xb")
        open("EMPLEADOS.bin", "xb")
    except:
        pass

    layers = [layer_menu, layer_agregarDepartamento, layer_agregarEmpleado, layer_generarReporte]

    while True:
        layers[page]()
        if (page == -1): break

    pass

if __name__ == "__main__":

    main()
