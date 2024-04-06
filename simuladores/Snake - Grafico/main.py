import pygame as pg
from random import randrange, choice
pg.init()
H = pg.display.Info().current_h
W = pg.display.Info().current_w
CLOCK = pg.time.Clock()

pg.display.set_mode((W//2,H//2), pg.RESIZABLE) 
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
    "dimention": 10,
    "numManzanas": 1,
    "longManzana": 1,
    "speed": 200,
    "multiSnake": False,
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
        self.record = 0

        self.foods = []

        self.snakes = Snake(1,2,self.foods), Snake(3,4,self.foods)
        self.time = 0

        self.conami = False

    def bucle(self):
        dimention = configNumbers["dimention"]
        self.screen.fill(configColors["marco"])
        self.matriz = [[0 for _ in range(dimention)] for _ in range(dimention)]

        for x,y in self.foods:
            self.matriz[y][x] = 5

        if not configNumbers["multiSnake"]: 
            self.snakes[0].bucle(self.matriz, [[pg.K_UP,pg.K_w],[pg.K_DOWN, pg.K_s],[pg.K_LEFT, pg.K_a],[pg.K_RIGHT, pg.K_d]])
        else:
            if not self.conami and sound:
                soundMultiSnake.play()
                self.conami = True
            self.snakes[0].bucle(self.matriz, [[pg.K_UP],[pg.K_DOWN],[pg.K_LEFT],[pg.K_RIGHT]])
            self.snakes[1].bucle(self.matriz,  [[pg.K_w],[pg.K_s],[pg.K_a],[pg.K_d]])

        if len(self.foods) < configNumbers["numManzanas"] and len(zeros := [[j, i] for i, row in enumerate(self.matriz) for j, val in enumerate(row) if val == 0]) > 1:
                ram = choice(zeros)
                self.foods.append(ram)

        realTime = pg.time.get_ticks()
        if realTime - self.time > configNumbers["speed"]: 
            self.time = realTime
            self.snakes[0].tick()
            if configNumbers["multiSnake"]: self.snakes[1].tick()

        self.box = self.screen.get_size()[1] // dimention
        for y in range(dimention):
            for x in range(dimention):
                draw = lambda color: pg.draw.rect(self.screen, color, ((x*self.box + (self.screen.get_size()[0] - dimention*self.box)//2), y*self.box, self.box, self.box))
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

        for s in self.snakes:
            if s.point > self.record:
                self.record = s.point
                if sound: soundRecord.play()
            
        borde1X = (self.screen.get_size()[0] - dimention*self.box)//2
        borde2X = dimention*self.box +(self.screen.get_size()[0] - dimention*self.box)//2
        tam =self.screen.get_size()[1]//20
        if not configNumbers["multiSnake"]:
            self.screen.blit(pg.font.SysFont("Arial", tam).render(f"Puntuacion: {self.snakes[0].point}", True, configColors["point"]), (borde1X,0))
        else:
            self.screen.blit(pg.font.SysFont("Arial", tam).render(f"Puntuacion: {self.snakes[0].point}", True, configColors["point"]), (borde1X,0))
            self.screen.blit(pg.font.SysFont("Arial", tam).render(f"Puntuacion: {self.snakes[1].point}", True, configColors["point"]), (borde1X,tam))
        self.screen.blit(pg.font.SysFont("Arial", tam).render(f"Récord: {self.record}", True, configColors["point"]), (borde2X- tam*6,0))

class Snake():
    def __init__(self, mathead:int, matbody:int, foods:list[int]):
        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]

        self.mathead = mathead
        self.matbody = matbody
        self.foods = foods

        self.point = 0 
        self.time = 0 
        self.head = self.ramd2()
        self.body = [self.head.copy()]
        self.long = 1
        self.move = [0,0]
        self.moved = False

    def gameover(self):
        self.move = [0,0]
        self.point = 0
        self.long = 1

        self.head = self.ramd2()
        self.body = [self.head.copy()]

    def bucle(self, matriz:list, controls:list):
        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]
        self.matriz = matriz
        self.numBox = len(matriz[0])

        for x,y in self.body[:-1]:
            matriz[y][x] = self.matbody
        matriz[self.body[-1][1]][self.body[-1][0]] = self.mathead
        
        key = pg.key.get_pressed()
        if any(key[k] for k in controls[0]) and self.move[1] != 1:
            self.move = [0,-1]
            self.moved = True
        elif any(key[k] for k in controls[1]) and self.move[1] != [0,-1]:
            self.move = [0,1]
            self.moved = True
        elif any(key[k] for k in controls[2]) and self.move[0] != 1:
            self.move = [-1,0]
            self.moved = True
        elif any(key[k] for k in controls[3]) and self.move[0] != -1:
            self.move = [1,0]
            self.moved = True      
    def tick(self):
        self.head[0] += self.move[0]; self.head[1] += self.move[1]

        for food in self.foods:
            if self.head == food:
                self.long += configNumbers["longManzana"]
                self.foods.remove(food)
                self.point += 10

        if len(self.body) >= self.long:
            self.body.pop(0)
            self.body.append(self.head.copy())
        else:
            self.body.append(self.head.copy())

        if self.head[0] < 0 or self.head[0] >= self.numBox or self.head[1] < 0 or self.head[1] >= self.numBox:
            self.gameover()

        if self.matriz[self.head[1]][self.head[0]] not in [0, 5, self.mathead]:
            self.gameover()

        
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

sound = True
if pg.mixer.get_init() is None:
    sound = False
else:
    soundMultiSnake = pg.mixer.Sound('./sounds/snakeMulti.mp3')
    soundRecord = pg.mixer.Sound('./sounds/record.mp3')

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
                    configNumbers["multiSnake"] = True
            else:
                code = []
                index = 0

    pages.bucle()

    pg.display.flip()
    CLOCK.tick(60)