from time import sleep
from colorama import *
just_fix_windows_console()
class pieza:
    def __init__(self, X, Y):
        self.X = int(X)
        self.Y = int(Y)

        if self.X > 8:
            self.X = 8
    #Se encarga de mostrar los posibles movimientos
    def movimiento(self):
        i = 1
        letras = ["a","b","c","d","f","g","h"]
        for y in range(1,9):
            for x in range(1,9):
                if x == self.X + 1 and y == self.Y + 2:
                    print(str(i) + "-","Casilla", letras[x-1]+str(y))
                    i += 1
                if x == self.X - 1 and y == self.Y + 2:
                    print(str(i) + "-","Casilla", letras[x-1]+str(y))
                    i += 1
                if x == self.X - 1 and y == self.Y - 2:
                    print(str(i) + "-","Casilla", letras[x-1]+str(y))
                    i += 1
                if x == self.X + 1 and y == self.Y - 2:
                    print(str(i) + "-","Casilla", letras[x-1]+str(y))
                    i += 1

    #Se encarga de mostrar el tablero donde se encuntra la pieza
    def tablero(self):
        tablero = Fore.WHITE +"1|"
        i = 0
        print(Fore.WHITE +"   a b c d e f g h")
        for y in range(1,9):
            for x in range(1,9):
                i +=1
                if x == self.X + 1 and y == self.Y + 2:
                    tablero += Fore.RED +" X" # + str(x) + str(y)
                elif x == self.X - 1 and y == self.Y + 2:
                    tablero += Fore.RED +" X"
                elif x == self.X - 1 and y == self.Y - 2:
                    tablero += Fore.RED +" X"
                elif x == self.X + 1 and y == self.Y - 2:
                    tablero += Fore.RED +" X"
                elif x == self.X and y == self.Y:
                    tablero += Fore.BLUE +" P"
                else:
                    tablero += Fore.WHITE +" #" #+ "(" + str(x) +"-"+ str(y) + ")"
                
                if i > 7:
                    tablero += "|"
                    print(tablero.center(30, " "))
                    tablero = str(y+1)+"|"
                    i = 0
        
# Pedir coordenadas de la pieza
while True:
    try:
        PosX = int(input("Posicion X: "))
        PosY = int(input("posicion Y: "))
        if PosX > 0 and PosY > 0 and PosX < 9 and PosY < 9:
                caballo = pieza(PosX,PosY)
                break
        else:
            print(Fore.MAGENTA +"Numero ingresado invalido")
            print(Style.RESET_ALL)
    except:
        print(Fore.MAGENTA +"Numero ingresado invalido")
        print(Style.RESET_ALL)

#Interfaz
while True:
    print(Fore.BLUE + "PIEZA CABALLO".center(30, " "))
    print(("Coord X: " + str(caballo.X) + " Coord Y: " + str(caballo.Y)).center(30, " "))

    print(Fore.RED + "POSIBLES MOVIMIENTOS".center(30, " "))
    caballo.movimiento()

    print(Fore.GREEN + "TABLERO".center(30, " "))
    caballo.tablero()
    
    print(Style.RESET_ALL)
    break