import pygame as pg
import Variables as v
import random as rd
import socket as sk
import threading as th
from time import sleep
from server import HOST, PORT

class Pantalla():
    def __init__(self, nombre) -> None:
        pg.init()

        self.pantalla = pg.display.set_mode((v.panta_ancho, v.panta_alto))
        pg.display.set_caption(nombre)

        self.reloj = pg.time.Clock()
        self.tiempo, self.espera = 0, 200 // ((v.velocidad // 10) + 1)

        self.cuadricula = (v.panta_ancho // v.cuadros, v.panta_alto // v.cuadros)

        self.CODE = [pg.K_UP, pg.K_UP, pg.K_DOWN, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_LEFT, pg.K_RIGHT, pg.K_b, pg.K_a]
        self.code = []
        self.index = 0

        self.activo = True

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.activo = False
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == self.CODE[self.index]:
                    self.code.append(event.key)
                    if self.index < 9: self.index += 1
                    
                    if self.code == self.CODE:
                        self.index = 0
                        self._conami()
                else:
                    self.code = []
                    self.index = 0

    def dibujar(self):
        self.pantalla.fill(v.clr_fondo)
    
        
        self._bucle()

        pg.display.flip()
        self.reloj.tick(30)

class Snake(Pantalla):
    def __init__(self) -> None:
        super().__init__(v.titulo)

        self.dosrand = lambda: [rd.randrange(0, v.cuadros), rd.randrange(0, v.cuadros)] 

        self.puntuacion = 0
        self.record = 0
        
        self.cabeza = self.dosrand()
        self.cuerpo = [self.cabeza.copy()]
        self.longitud = 1
        self.move = [0,0]
        self.movido = False

        self.comida = [self.dosrand() for _ in range(v.manzanas)]
        
    def _gameover(self):
        self.move = [0,0]
        self.puntuacion = 0
        self.longitud = 1

        self.cabeza = self.dosrand()
        self.cuerpo = [self.cabeza.copy()]

        self.comida = [self.dosrand() for _ in range(v.manzanas)]

    def _serpierte(self):
        posx = self.cuerpo[-1][0]*self.cuadricula[0]
        posy = self.cuerpo[-1][1]*self.cuadricula[1]

        pg.draw.rect(self.pantalla, v.clr_cabeza, (posx,posy,self.cuadricula[0],self.cuadricula[1]))

        for x,y in self.cuerpo[:-1]:
            posx = x*self.cuadricula[0]
            posy = y*self.cuadricula[1]
            pg.draw.rect(self.pantalla, v.clr_cuerpo, (posx,posy,self.cuadricula[0],self.cuadricula[1]))
        
        tecla = pg.key.get_pressed()
        if self.movido == False:
            if (tecla[pg.K_UP] or tecla[pg.K_w] )and self.move[1] != 1:
                self.move = [0,-1]
                self.movido = True
            elif (tecla[pg.K_DOWN] or tecla[pg.K_s]) and self.move[1] != -1:
                self.move = [0,1]
                self.movido = True
            elif (tecla[pg.K_LEFT] or tecla[pg.K_a]) and self.move[0] != 1:
                self.move = [-1,0]
                self.movido = True
            elif (tecla[pg.K_RIGHT] or tecla[pg.K_d]) and self.move[0] != -1:
                self.move = [1,0]
                self.movido = True
            
            
        tiempo_real = pg.time.get_ticks()
        if tiempo_real - self.tiempo < self.espera: return
        self.tiempo = tiempo_real

        self.cabeza[0] += self.move[0] ; self.cabeza[1] += self.move[1]
        self.movido = False

        if len(self.cuerpo) >= self.longitud:
            self.cuerpo.pop(0)
            self.cuerpo.append(self.cabeza.copy())
        else:
            self.cuerpo.append(self.cabeza.copy())

        if self.cabeza[0] < 0 or self.cabeza[0] >= v.cuadros or self.cabeza[1] < 0 or self.cabeza[1] >= v.cuadros:
            self._gameover()
            
        for x,y in self.cuerpo[:-1]:
            if x == self.cabeza[0] and y == self.cabeza[1]:
                self._gameover()

    def _comida(self):
        for x,y in self.comida:
            posx = x*self.cuadricula[0]
            posy = y*self.cuadricula[1]

            pg.draw.rect(self.pantalla, v.clr_comida, (posx,posy,self.cuadricula[0],self.cuadricula[1]))

        for i in range(len(self.comida)):
            if self.comida[i] == self.cabeza:
                self.longitud += v.long_por_manzana
                self.puntuacion += 100
                self.comida[i] = self.dosrand()
                return
            if self.comida[i] in self.cuerpo:
                self.comida[i] = self.dosrand()

    def _puntuacion(self):
        if self.puntuacion > self.record:
            self.record = self.puntuacion

        self.pantalla.blit(pg.font.SysFont("Arial", 20).render(f"Puntuacion: {self.puntuacion}", True, v.clr_puntuacion), (0,0))
        self.pantalla.blit(pg.font.SysFont("Arial", 20).render(f"Récord: {self.record}", True, v.clr_puntuacion), (v.panta_ancho//2.5,0))
        self.pantalla.blit(pg.font.SysFont("Arial", 20).render(f"Nombre: {username}", True, v.clr_puntuacion), (v.panta_ancho//1.4,0))

    def _conami(self):
        self.puntuacion += 1000
        v.clr_fondo = rd.choice([v.amarillo, v.naranja, v.rosado, v.morado, v.celeste, v.gris, v.azul_oscuro, v.azul, v.colmena1, v.colmena2, v.colmena3])

    def _bucle(self):
        self._comida()
        self._serpierte()
        self._puntuacion()

class Intro(Pantalla):
    def __init__(self):
        super().__init__(v.titulo)

        self.alpha = 0
        self.imgLogo = pg.transform.scale(pg.image.load("logo.png").convert_alpha(), (v.panta_ancho,v.panta_alto))

    def _bucle(self):
        self.pantalla.fill(v.clr_fondo)

        imgLogo_copy = self.imgLogo.copy()
        imgLogo_copy.set_alpha(self.alpha)
        self.pantalla.blit(imgLogo_copy, (0,-40))
        self.alpha += 3

        if any(pg.key.get_pressed()): return "Comenzar" # Si se pulsa cualquier tecla comienza el juego

        if self.alpha >= 250: return "Comenzar"

        pg.display.flip()
        self.reloj.tick(60)

username = "Desconectado"

intro = Intro()
juego = Snake()

def receiveMessages():
    global username
    while juego.activo and intro.activo:
        try:
            message = client.recv(1024).decode("utf-8")
            if message.startswith("/U "):
                username = message[3:]
                client.send(username.encode("utf-8"))
        except:
            if client.fileno() != -1: client.close()
            break

def writeMessages():
    while juego.activo and intro.activo:
        message = f"{username} {juego.record}"
        client.send(message.encode("utf-8"))
        sleep(3)

    client.send("/exit".encode("utf-8"))
    client.close()

try:
    client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    client.connect((HOST, PORT))

    receiveThread = th.Thread(target=receiveMessages)
    receiveThread.start()

    writeThread = th.Thread(target=writeMessages)
    writeThread.start()
except:
    print("Jugando sin conexion")

while True:
    intro.input()
    if intro._bucle() == "Comenzar": break

while True:
    juego.input()
    juego.dibujar()