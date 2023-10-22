from random import randint
from typing import Any
from colorama import *
import os
from pynput import keyboard

#VARIABLES GLOBALES
colores = [Fore.BLACK+Back.BLACK,Fore.RED+Back.RED,Fore.BLUE+Back.BLUE, Fore.MAGENTA+Back.MAGENTA, Fore.GREEN+Back.GREEN, Fore.YELLOW+Back.YELLOW, Fore.LIGHTRED_EX+Back.LIGHTRED_EX, Fore.LIGHTBLUE_EX+Back.LIGHTBLUE_EX] #PALETA DE COLORES

class Pantalla:
    def __init__(self,dx,dy,jx,jy,jdx,jdy,colores):
        #PANTALLA MADRE
        self.dimX = dx 
        self.dimY = dy 
        self.pantalla =[]
        self.memoria =[]

        #PANTALLA DE JUEGO
        self.juegoX = jx
        self.juegoDimX = jdx
        self.juegoY = jy
        self.juegoDimY = jdy

        #Cofiguracion
        self.colores = colores

        #Inicializar
        self._NewArray(self.pantalla)
        self._NewArray(self.memoria)

    def _NewArray(self,arreglo):
        #VARIABLES
        pixelesX = []

        for y in range(self.dimY):
            for x in range(self.dimX):
                pixelesX.append(0)
            arreglo.append(pixelesX)
            pixelesX = []

    def _showArray(self,arreglo):
        impresion = ""
        salto_linea = 0
        #LOGICA
        for y in range( self.juegoY, self.juegoY+ self.juegoDimY):
            for x in range( self.juegoX, self.juegoY+ self.juegoDimX):
                impresion +=  self.colores[ arreglo[y][x]]+" #" + Style.RESET_ALL
            print(Fore.WHITE+Back.WHITE+"# "+impresion+Fore.WHITE+Back.WHITE+"# "+Style.RESET_ALL)
            salto_linea = 0
            impresion = ""

    def MostarPantalla(self):
        self._showArray(self.pantalla)

    def MostarMemoria(self):
        self._showArray(self.memoria)

    def _IslineFull( self,linea):
        y = 24-linea
        for lin in range( self.juegoX,  self.juegoX+ self.juegoDimX):
            if self.memoria[y][lin] == 0:
                return (False)
        return (True)  

    def _DelLine( self,linea):
        num = 35-linea #juegoY + juegoDimY - linea
        
        for lin in range(self.juegoY+1, num+1):
            for x in range(self.dimX):
                 self.memoria[num-lin][x] =  self.memoria[num-lin-1][x]

    def VerificarLineas(self):
        for i in range(self.juegoDimY ):
            if Game._IslineFull(i) == True:
                Game._DelLine(i)

    def SetMemoria(self):
        for y in range(self.dimY):
            for x in range(self.dimX):
                self.pantalla[y][x] = self.memoria[y][x]          

    def ClearPantalla(self):
        for y in range(self.dimY):
            for x in range(self.dimX):
                self.pantalla[y][x] = 0

#OBJETOS 
map_piezas = [
    #L
    [[[0,0],[0,1],[0,2],[1,2]],
    [[0,1],[1,1],[2,1],[2,0]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,1],[0,0],[1,0],[2,0]]],
    #Cuadrado
    [[[0,0],[0,1],[1,0],[1,1]],
    [[0,0],[0,1],[1,0],[1,1]],
    [[0,0],[0,1],[1,0],[1,1]],
    [[0,0],[0,1],[1,0],[1,1]]],
    #L Espejo
    [[[1,0],[1,1],[1,2],[0,2]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[1,0],[0,0],[0,1],[0,2]],
    [[0,0],[1,0],[2,0],[2,1]]],
    #Linea
    [[[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[2,0],[3,0]]],
    # T
    [[[0,1],[1,1],[2,1],[1,0]],
    [[0,0],[0,1],[0,2],[1,1]],
    [[0,0],[1,0],[2,0],[1,1]],
    [[0,1],[1,0],[1,1],[1,2]]],
    # Culebra
    [[[0,0],[0,1],[1,1],[1,2]],
    [[0,1],[1,1],[1,0],[2,0]],
    [[0,0],[0,1],[1,1],[1,2]],
    [[0,1],[1,1],[1,0],[2,0]]],
    # Culebra invertida
    [[[1,0],[1,1],[0,1],[0,2]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[1,0],[1,1],[0,1],[0,2]],
    [[0,0],[1,0],[1,1],[2,1]]]
]

class Pieza:
    def __init__(self,color,pieza,x,y,Game):
        self.x = x
        self.y = y
        self.mascaraX = 0
        self.mascaraY = 0
        self.rotacion = 0
        self.color = color
        self.pieza = pieza
        self.game = Game

    def bajar(self):
        self.y += 1

    def dere(self):

        coordenadas_mas_dere = {} 
        espacio = True
        
        for x,y in map_piezas[self.pieza][self.rotacion]:
            if y not in coordenadas_mas_dere or x > coordenadas_mas_dere[y]:
                coordenadas_mas_dere[y] = x

        for y,x in coordenadas_mas_dere.items():
            if self.game.pantalla[self.y + y][self.x + x+1] != 0:
                espacio = False


        if self.x <= self.game.juegoX+self.game.juegoDimX-self.mascaraX-1 and espacio == True:
            self.x += 1

    def izqu(self):
        coordenadas_mas_iz = {}
        espacio = True
        for x,y in map_piezas[self.pieza][self.rotacion]:
            if y not in coordenadas_mas_iz or x < coordenadas_mas_iz[y]:
                coordenadas_mas_iz[y] = x

        for y,x in coordenadas_mas_iz.items():
            if self.game.pantalla[self.y + y][self.x + x - 1] != 0:
                espacio = False

        if self.x >= self.game.juegoX+1 and espacio == True:
            self.x -= 1

    def rotar(self):
        """rotacionfut = self.rotacion
        if self.rotacion < 3:
            rotacionfut = self.rotacion + 1
        else:
            rotacionfut = 0

        for mascara in range(4):
            pantalla_madre[self.y + map_piezas[self.pieza][self.rotacion][mascara][1]][self.x + map_piezas[self.pieza][self.rotacion][dibujo][0] ] = self.color
            if map_piezas[self.pieza][rotacionfut][mascara][0] >= self.mascaraX:
                mascaraXfut = map_piezas[self.pieza][rotacionfut][mascara][0]+1
            if map_piezas[self.pieza][rotacionfut][mascara][1] >= self.mascaraY:
                mascaraYfut = map_piezas[self.pieza][rotacionfut][mascara][1]+1
        
        for x in range(mascaraXfut):
            for y in range(mascaraYfut):
                pass"""

        self.rotacion += 1
        self.rotacion = self.rotacion % 4
 
    def dibujar(self):
        self.mascaraX = 0
        self.mascaraY = 0
        for dibujo in range(4):
            self.game.pantalla[self.y + map_piezas[self.pieza][self.rotacion][dibujo][1]][self.x + map_piezas[self.pieza][self.rotacion][dibujo][0] ] = self.color
            if map_piezas[self.pieza][self.rotacion][dibujo][0] >= self.mascaraX:
                self.mascaraX = map_piezas[self.pieza][self.rotacion][dibujo][0]+1
            if map_piezas[self.pieza][self.rotacion][dibujo][1] >= self.mascaraY:
                self.mascaraY = map_piezas[self.pieza][self.rotacion][dibujo][1]+1

    def colision(self):
        coordenadas_mas_bajas = {}

        if self.y+self.mascaraY >= self.game.juegoY+self.game.juegoDimY:
                return(True)
        
        for x,y in map_piezas[self.pieza][self.rotacion]:
            if x not in coordenadas_mas_bajas or y > coordenadas_mas_bajas[x]:
                coordenadas_mas_bajas[x] = y
        for x in coordenadas_mas_bajas:
            y = coordenadas_mas_bajas[x]
            if self.game.pantalla[self.y + y + 1][self.x + x] != 0:
                return(True)

    def congelar(self):
        for dibujo in range(4):
            x = self.x + map_piezas[self.pieza][self.rotacion][dibujo][0]
            y = self.y + map_piezas[self.pieza][self.rotacion][dibujo][1]

            self.game.memoria[y][x] = self.color
        self.existe = False

        


############################
####### JUEGO TETRIS #######
############################

pieza_en_juego = False
Game = Pantalla(30,30,10,10,10,15,colores)

while True:
    for i in range(2):
                
        #Comprobar linea
        Game.VerificarLineas()
        
        #Sobreescribir
        Game.SetMemoria()

        #Eleguir aleatoiamente piezas
        if pieza_en_juego == False:
            eleguir_pieza = randint(0,len(map_piezas)-1)
            eleguir_color = randint(1,len(colores)-1)
            pieza = Pieza(eleguir_color,pieza=eleguir_pieza,x=randint(10,18),y=7,Game=Game)
            pieza_en_juego = True

        pieza.dibujar()

        if i == 1: 
            if pieza.colision() == True:
                pieza.congelar() 
                pieza_en_juego = False
            else:
                pieza.bajar()

        #Controles por teclas
        with keyboard.Events() as events:
            event = events.get(0.2)
            if event is not None:
                if event.key == keyboard.Key.right: pieza.dere()
                if event.key == keyboard.Key.left:  pieza.izqu()
                if event.key == keyboard.Key.up:    pieza.rotar()

        #Se muestra la pantalla y se elimina
        os.system("cls")
        Game.MostarPantalla()
        #Game.MostarMemoria()
        Game.ClearPantalla()
        #time.sleep(0.1)

