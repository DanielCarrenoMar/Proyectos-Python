from colorama import Fore, Style

def impriMat (matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            try:
                if matriz[y][x] == 0: print(F"{Fore.RED}{matriz[y][x]}{Style.RESET_ALL}", end=" ")
                else: print(matriz[y][x], end=" ")
            except IndexError: print(" ", end=" ")
        print("")

def pedirDatos(tipo:str, mensaje:str):
    while True:
        try:
            if tipo == "str":
                return str(input(mensaje))
            
            elif tipo == "int":
                return int(input(mensaje))
            
            elif tipo == "float":
                return float(input(mensaje))
            
            elif tipo == "nota20":
                nota = float(input(mensaje))
                if nota > 0 and nota <= 20: 
                    return nota
                else:
                    raise ValueError()
            else:
                raise SyntaxError("Se debe ingresar un argumento valido")
        except ValueError:
            print(Fore.RED + "Dato Invalido" + Style.RESET_ALL)

def crearMat(dim:int):
    return [[0 for _ in range(dim)] for _ in range(dim)]