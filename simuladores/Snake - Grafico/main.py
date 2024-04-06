import pygame as pg
from random import randrange
pg.init()

H = pg.display.Info().current_h
W = pg.display.Info().current_w
CLOCK = pg.time.Clock()

pg.display.set_mode((W-30,H-60), pg.RESIZABLE) 
pg.display.set_caption("Snake")

configColors = {
    "marco": "#FFFFFF",
    "background": "#000000",
    "head": "#01DF3C",
    "body": "#10BD3E",
    "head2": "#FFFFFF",
    "body2": "#1FF000",
    "comida": "#952121",
    "point": "#FFFFFF",
}
configNumbers = {
    "dimention": 20,
    "numManzanas": 1,
}

class Intro():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.alpha = -5
        self.imgLogo = pg.image.load("./images/logo.png")
        
    def bucle(self):
        self.screen.fill("#000000")
        width, height = self.screen.get_size()

        imgLogo_copy = self.imgLogo.copy()
        imgLogo_copy = pg.transform.scale(imgLogo_copy, (height,height))
        imgSize = imgLogo_copy.get_size()
        imgLogo_copy.set_alpha(self.alpha)
        self.screen.blit(imgLogo_copy, ((width-imgSize[0])/2,0))
        self.alpha += 1

        if self.alpha > 155:
            return True

class Start():
    def __init__(self):
        self.screen = pg.display.get_surface()
        
    def bucle(self):
        self.screen.fill("#000000")
        pg.draw.circle(self.screen, "#FFFFFF", (30,30), 10)

class Game():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]

        self.snake1 = Snake(1,2)
        self.snake2 = Snake(3,4)

        self.point = 0
        self.record = 0

        self.comida = [self.ramd2() for _ in range(configNumbers["numManzanas"])]

        self.conami = False

    def _manzana(self):
        pass

    def bucle(self):
        self.screen.fill(configColors["marco"])
        self.matriz = [[0 for _ in range(configNumbers["dimention"])] for _ in range(configNumbers["dimention"])]

        if not multiSnake: 
            self.snake1.bucle(self.matriz, configNumbers["dimention"], 500, [[pg.K_UP,pg.K_w],[pg.K_DOWN, pg.K_s],[pg.K_LEFT, pg.K_a],[pg.K_RIGHT, pg.K_d]])
        else:
            if not self.conami and sound:
                soundMultiSnake.play()
                self.conami = True
            self.snake1.bucle(self.matriz, configNumbers["dimention"], 500, [[pg.K_UP],[pg.K_DOWN],[pg.K_LEFT],[pg.K_RIGHT]])
            self.snake2.bucle(self.matriz, configNumbers["dimention"], 500,  [[pg.K_w],[pg.K_s],[pg.K_a],[pg.K_d]])


        self.box:float = self.screen.get_size()[1] // configNumbers["dimention"]
        for y in range(configNumbers["dimention"]):
            for x in range(configNumbers["dimention"]):
                draw = lambda color: pg.draw.rect(self.screen, color, ((x*self.box + (self.screen.get_size()[0] - configNumbers["dimention"]*self.box)//2), y*self.box, self.box, self.box))
                if self.matriz[y][x] == 0:
                    draw(configColors["background"])
                elif self.matriz[y][x] == 1:
                    draw(configColors["head"])
                elif self.matriz[y][x] == 2:
                    draw(configColors["body"])
                elif self.matriz[y][x] == 3:
                    draw(configColors["head2"])
                elif self.matriz[y][x] == 4:
                    draw(configColors["body2"])
                elif self.matriz[y][x] == 5:
                    draw(configColors["comida"])

class Snake():
    def __init__(self, mathead:int, matbody:int):
        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]

        self.mathead = mathead
        self.matbody = matbody

        self.time = 0
        self.head = self.ramd2()
        self.body = [self.head.copy()]
        self.long = 1
        self.move = [[0,0]]
        self.moved = False

    def gameover(self):
        self.move = [[0,0]]
        self.point = 0
        self.long = 1

        self.head = self.ramd2()
        self.body = [self.head.copy()]

        self.comida = [self.ramd2() for _ in range(configNumbers["numManzanas"])]

    def bucle(self, matriz:list, numBox:int,wait:int, controls:list):
        matriz[self.body[-1][1]][self.body[-1][0]] = self.mathead
        for x,y in self.body[:-1]:
            matriz[y][x] = self.matbody
        
        key = pg.key.get_pressed()
        if any(key[k] for k in controls[0]) and self.move[-1][1] != 1 and self.move[-1] != [0,-1]:
            self.move.append([0,-1])
            self.moved = True
        elif any(key[k] for k in controls[1]) and self.move[-1][1] != -1 and self.move[-1] != [0,1]:
            self.move.append([0,1])
            self.moved = True
        elif any(key[k] for k in controls[2]) and self.move[-1][0] != 1 and self.move[-1] != [-1,0]:
            self.move.append([-1,0])
            self.moved = True
        elif any(key[k] for k in controls[3]) and self.move[-1][0] != -1 and self.move[-1] != [1,0]:
            self.move.append([1,0])
            self.moved = True
        if (len(self.move)) > 3:
            self.move.pop(0)

        realTime = pg.time.get_ticks()
        if realTime - self.time < wait: return
        self.time = realTime

        if (len(self.move) > 1): self.head[0] += self.move[1][0] ; self.head[1] += self.move[1][1]; self.move.pop(0)
        else: self.head[0] += self.move[0][0] ; self.head[1] += self.move[0][1]

        if len(self.body) >= self.long:
            self.body.pop(0)
            self.body.append(self.head.copy())
        else:
            self.body.append(self.head.copy())

        if self.head[0] < 0 or self.head[0] >= numBox or self.head[1] < 0 or self.head[1] >= numBox:
            self.gameover()
            pass

        for x,y in self.body[:-1]:
            if x == self.head[0] and y == self.head[1]:
                self.gameover()
                pass
    
    def manzana(self):
        pass

        
class Pages():
    def __init__(self, pages:list):
        self.main = 2
        self.pages = pages
        
    def bucle(self):
        if self.pages[self.main].bucle(): self.next()
    def next(self):
        self.main += 1
        self.main %= len(self.pages)
    def back(self):
        self.main -= 1
        self.main %= len(self.pages)
    def goto(self, num:int):
        self.main = num
        self.main %= len(self.pages)

multiSnake = False
sound = True
if pg.mixer.get_init() is None:
    sound = False
else:
    soundMultiSnake = pg.mixer.Sound('./sounds/snakeMulti.mp3')

intro, start, game = Intro(), Start(), Game()
pages = Pages([intro, start, game])

CODE = [pg.K_UP, pg.K_UP, pg.K_DOWN, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_LEFT, pg.K_RIGHT, pg.K_b, pg.K_a]
code = []
index = 0

while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.display.set_caption("hola3")
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.KEYDOWN:
            if event.key == CODE[index]:
                code.append(event.key)
                if index < 9: index += 1
                
                if code == CODE:
                    index = 0
                    multiSnake = True
            else:
                code = []
                index = 0

    pages.bucle()

    pg.display.flip()
    CLOCK.tick(60)