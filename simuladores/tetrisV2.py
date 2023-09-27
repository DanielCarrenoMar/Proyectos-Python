from random import randint
from typing import Any
from colorama import *
import os
import time
from pynput.keyboard import Listener
from pynput import keyboard

#VARIABLES GLOBALES
colores = [Fore.BLACK+Back.BLACK,Fore.RED+Back.RED,Fore.BLUE+Back.BLUE, Fore.MAGENTA+Back.MAGENTA, Fore.GREEN+Back.GREEN, Fore.YELLOW+Back.YELLOW, Fore.LIGHTRED_EX+Back.LIGHTRED_EX] #PALETA DE COLORES

#PANTALLA MADRE
dimensionX = 30 
dimensionY = 30 
pantalla_madre =[]

#PANTALLA DE JUEGO
juegoX = 10
juegoDimX = 10
juegoY = 10
juegoDimY = 15

#Funciones
def generar_pantalla():
        #VARIABLES
        global dimensionX
        global dimensionY
        global colores
        pixelesX = []
        pixeles_generados = []
        
        #INICIO
        for y in range(dimensionY):
            for x in range(dimensionX):
                pixelesX.append(0)
            pixeles_generados.append(pixelesX)
            pixelesX = []

        return(pixeles_generados)

def actualizar_pantalla(pantalla):
    #VARIABLES
    global juegoX
    global juegoDimX
    global juegoY
    global juegoDimY
    global colores
    impresion = ""
    salto_linea = 0
    #LOGICA
    for y in range(juegoY,juegoY+juegoDimY):
        for x in range(juegoX,juegoY+juegoDimX):
            impresion += colores[pantalla[y][x]]+" #" + Style.RESET_ALL
        print(Fore.WHITE+Back.WHITE+"# "+impresion+Fore.WHITE+Back.WHITE+"# "+Style.RESET_ALL)
        salto_linea = 0
        impresion = ""

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
    [[0,0],[0,1],[1,0],[1,1]]]
]

class Pieza:
    def __init__(self,color,pieza,x,y):
        self.x = x
        self.y = y
        self.mascaraX = 0
        self.mascaraY = 0
        self.rotacion = 0
        self.color = color
        self.pieza = pieza

    def bajar(self):
        self.y += 1

    def dere(self):
        coordenadas_mas_dere = {}
        espacio = False
        for x,y in map_piezas[self.pieza][self.rotacion]:
            if y not in coordenadas_mas_dere or x > coordenadas_mas_dere[y]:
                coordenadas_mas_dere[y] = x
        for x in coordenadas_mas_dere:
            x = coordenadas_mas_dere[y]
            if pantalla_madre[self.y + y][self.x + x + 1] == 0:
                espacio = True

        if self.x <= juegoX+juegoDimX-self.mascaraX-1 and espacio == True:
            self.x += 1

    def izqu(self):
        if self.x >= juegoX+self.mascaraX-1:
            self.x -= 1

    def rotar(self):
        if self.rotacion < 3:
            self.rotacion += 1
        else:
            self.rotacion = 0

    def dibujar(self):
        self.mascaraX = 0
        self.mascaraY = 0
        for dibujo in range(4):
            pantalla_madre[self.y + map_piezas[self.pieza][self.rotacion][dibujo][1]][self.x + map_piezas[self.pieza][self.rotacion][dibujo][0] ] = self.color
            if map_piezas[self.pieza][self.rotacion][dibujo][0] >= self.mascaraX:
                self.mascaraX = map_piezas[self.pieza][self.rotacion][dibujo][0]+1
            if map_piezas[self.pieza][self.rotacion][dibujo][1] >= self.mascaraY:
                self.mascaraY = map_piezas[self.pieza][self.rotacion][dibujo][1]+1

    def colision(self):
        coordenadas_mas_bajas = {}

        if self.y+self.mascaraY >= juegoY+juegoDimY:
                return(True)
        
        for x,y in map_piezas[self.pieza][self.rotacion]:
            if x not in coordenadas_mas_bajas or y > coordenadas_mas_bajas[x]:
                coordenadas_mas_bajas[x] = y
        for x in coordenadas_mas_bajas:
            y = coordenadas_mas_bajas[x]
            if pantalla_madre[self.y + y + 1][self.x + x] != 0:
                return(True)

    def congelar(self):
        for dibujo in range(4):
            memoria[self.y + map_piezas[self.pieza][self.rotacion][dibujo][1]][self.x + map_piezas[self.pieza][self.rotacion][dibujo][0] ] = self.color
        self.existe = False

############################
####### JUEGO TETRIS #######
############################

pieza_en_juego = False
memoria = generar_pantalla()

while True:
    #La pantalla se pone en blanco
    pantalla_madre = generar_pantalla()
    #Se la logica
    for y in range(dimensionY):
        for x in range(dimensionX):
            pantalla_madre[y][x] = memoria[y][x]

    #Eleguir aleatoiamente piezas
    if pieza_en_juego == False:
        eleguir_pieza = randint(0,0)
        eleguir_color = randint(1,len(colores)-1)
        pieza = Pieza(eleguir_color,pieza=eleguir_pieza,x=randint(10,18),y=7)
        pieza_en_juego = True
        
    #Controles por teclas
    with keyboard.Events() as events:
        event = events.get(0.2)
        if event is not None:
            if event.key == keyboard.Key.right:
                pieza.dere()
            if event.key == keyboard.Key.left:
                pieza.izqu()
            if event.key == keyboard.Key.up:
                pieza.rotar()

    pieza.dibujar()
    pieza.bajar()

    if pieza.colision() == True:
        pieza.congelar()
        pieza_en_juego = False

    #Se muestra la pantalla y se elimina
    actualizar_pantalla(pantalla_madre)
    #actualizar_pantalla(memoria)
    time.sleep(0.2)
    os.system("cls")
    