import pygame as pg
import Variables as v
import random as rd

class Pantalla():
    def __init__(self, nombre) -> None:
        pg.init()
        self.pantalla = pg.display.set_mode((v.panta_ancho, v.panta_alto))
        pg.display.set_caption(nombre)

        self.reloj = pg.time.Clock()
        self.tiempo, self.espera = 0, 120 // ((v.velocidad // 10) + 1)

        self.cuadricula = (v.panta_ancho // v.cuadros, v.panta_alto // v.cuadros)
        print(self.cuadricula)

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def dibujar(self):
        self.pantalla.fill(v.clr_fondo)
    
        
        self._bucle()

        pg.display.flip()
        self.reloj.tick(60)

class Snake(Pantalla):
    def __init__(self) -> None:
        super().__init__("Snake")

        self.dosrand = lambda: [rd.randrange(0, v.cuadros), rd.randrange(0, v.cuadros)] 

        self.puntuacion = 0
        self.longitud = 1
        
        self.cabeza = self.dosrand()
        self.cuerpo = [self.cabeza.copy()]
        
        self.move = [0,0]

        self.comida = self.dosrand()

    def _gameover(self):
        self.move = [0,0]
        self.puntuacion = 0
        self.longitud = 1

        self.cabeza = self.dosrand()
        self.cuerpo = [self.cabeza.copy()]

        self.comida = self.dosrand()

    def _serpierte(self):
        for x,y in self.cuerpo:
            posx = x*self.cuadricula[0]
            posy = y*self.cuadricula[1]

            pg.draw.rect(self.pantalla, v.clr_cuerpo, (posx,posy,self.cuadricula[0],self.cuadricula[1]))


        tecla = pg.key.get_pressed()
        if tecla[pg.K_UP] or tecla[pg.K_w] and self.move[1] != 1:
            self.move = [0,-1]
        if tecla[pg.K_DOWN] or tecla[pg.K_s] and self.move[1] != -1:
            self.move = [0,1]
        if tecla[pg.K_LEFT] or tecla[pg.K_a] and self.move[0] != 1:
            self.move = [-1,0]
        if tecla[pg.K_RIGHT] or tecla[pg.K_d] and self.move[0] != -1:
            self.move = [1,0]

        tiempo_real = pg.time.get_ticks()
        if tiempo_real - self.tiempo < self.espera: return
        self.tiempo = tiempo_real


        self.cabeza[0] += self.move[0] ; self.cabeza[1] += self.move[1]

        if len(self.cuerpo) >= self.longitud:
            self.cuerpo.pop(0)
            self.cuerpo.append(self.cabeza.copy())
        else:
            self.cuerpo.append(self.cabeza.copy())

        if self.cabeza[0] < 0 or self.cabeza[0] > v.cuadros or self.cabeza[1] < 0 or self.cabeza[1] > v.cuadros:
            self._gameover()
            
        for x,y in self.cuerpo[:-1]:
            if x == self.cabeza[0] and y == self.cabeza[1]:
                print(self.cabeza)
                print(self.cuerpo)
                self._gameover()

        

        

    def _comida(self):
        posx = self.comida[0]*self.cuadricula[0]
        posy = self.comida[1]*self.cuadricula[1]

        pg.draw.rect(self.pantalla, v.clr_comida, (posx,posy,self.cuadricula[0],self.cuadricula[1]))

        if self.cabeza == self.comida:
            self.longitud += 1
            self.puntuacion += 1 
            self.comida = [rd.randrange(0, v.cuadros), rd.randrange(0, v.cuadros)]
        
    def _bucle(self):
        self._comida()

        self._serpierte()

juego = Snake()

while True:
    juego.input()
    juego.dibujar()