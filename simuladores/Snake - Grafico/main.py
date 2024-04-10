import pygame as pg
import pygame_menu as pgm
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
    "food": "#952121",
    "ui": "#FFFFFF",
    "ui2": "#FFFFFF",
}
configNumbers = {
    "dimention": 25,
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
        
    def bucle(self, events:list):
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
        mytheme = pgm.Theme()
        mytheme.title_bar_style = pgm.widgets.MENUBAR_STYLE_SIMPLE
        mytheme.widget_font_color = "#1F4C52"
        mytheme.selection_color = "#132F33"
        mytheme.background_color = "#DAEBEE"
        mytheme.title_font_color = "#DAEBEE"
        mytheme.title_background_color = "#255243"
        mytheme.title_background_color = "#255243"

        screenW, screenH = self.screen.get_size()
        self.menuColors = pgm.pygame_menu.Menu('Colores', screenW, screenH,theme=mytheme, center_content=True)
        def changeColor(*args, **kwargs):
            configColors.update({kwargs["kwargs"]: args[0]})
        self.menuColors.add.color_input('Marco: ', color_type='hex', onchange=changeColor, kwargs="marco", default=configColors["marco"])
        self.menuColors.add.color_input('Texto: ', color_type='hex', onchange=changeColor, kwargs="ui", default=configColors["ui"])
        self.menuColors.add.color_input('Fondo: ', color_type='hex', onchange=changeColor, kwargs="background", default=configColors["background"])
        self.menuColors.add.color_input('Comida: ', color_type='hex', onchange=changeColor, kwargs="food", default=configColors["food"])
        self.menuColors.add.color_input('Cabeza: ', color_type='hex', onchange=changeColor, kwargs="head", default=configColors["head"])
        self.menuColors.add.color_input('Cuerpo: ', color_type='hex', onchange=changeColor, kwargs="body", default=configColors["body"])
        self.menuColors.add.vertical_margin(20)
        self.menuColors.add.label("Jugador 2")
        self.menuColors.add.color_input('Texto: ', color_type='hex', onchange=changeColor, kwargs="ui2", default=configColors["ui2"])
        self.menuColors.add.color_input('Cabeza: ', color_type='hex', onchange=changeColor, kwargs="head2", default=configColors["head2"])
        self.menuColors.add.color_input('Cuerpo: ', color_type='hex', onchange=changeColor, kwargs="body2", default=configColors["body2"])

        self.menuNumber = pgm.pygame_menu.Menu('Reglas de juego', screenW, screenH,theme=mytheme, center_content=True)
        def changeNumber(*args, **kwargs):
            configNumbers.update({kwargs["kwargs"]: args[0]})
        self.menuNumber.add.text_input('Tamaño del tablero: ', default=str(configNumbers["dimention"]), input_type=pgm.locals.INPUT_INT, maxchar=3, onchange=changeNumber, kwargs="dimention")

        self.menu = pgm.pygame_menu.Menu('Configuracion', screenW, screenH,theme=mytheme, columns=1, rows=4, center_content=True)
        sound = pgm.sound.Sound()
        sound.load_example_sounds()
        self.menu.set_sound(sound, True)
        def next(): global page; page = 2
        self.menu.add.button('Iniciar', next)
        self.menu.add.button('Reglas de juego', self.menuNumber)
        self.menu.add.button('Colores', self.menuColors)
        self.menu.add.button('Salir', pgm.events.EXIT)
        
    def bucle(self, events:list):
        if self.menu.is_enabled():
            for event in events:
                if event.type == pg.VIDEORESIZE:
                    screenW, screenH = self.screen.get_size()
                    self.menu.resize(screenW, screenH)
                    self.menuColors.resize(screenW, screenH)
                    self.menuNumber.resize(screenW, screenH)
        
            self.menu.update(events)
            self.menu.draw(self.screen)

class Game():
    def __init__(self):
        self.screen = pg.display.get_surface()

        self.foods = []

        self.snakes = Snake(1,2,self.foods), Snake(3,4,self.foods)
        self.time = 0

        self.conami = False
    def reset(self):
        self.foods = []
        self.snakes = Snake(1,2,self.foods), Snake(3,4,self.foods)
        for s in self.snakes:
            s.reset = True

    def bucle(self, events:list):
        global page
        dimention = configNumbers["dimention"]
        self.screen.fill(configColors["marco"])
        self.matriz = [[0 for _ in range(dimention)] for _ in range(dimention)]

        print(self.foods)
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
                print("Añadido comida ",ram)
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
                    print(configColors["body2"])
                    draw(configColors["body2"])
                elif self.matriz[y][x] == 5:
                    draw(configColors["food"])
            
        borde1X = (self.screen.get_size()[0] - dimention*self.box)//2
        borde2X = dimention*self.box +(self.screen.get_size()[0] - dimention*self.box)//2
        textTam =self.screen.get_size()[1]//20
        if not configNumbers["multiSnake"]:
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Puntuacion: {self.snakes[0].point}", True, configColors["ui"]), (borde1X,0))
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Récord: {self.snakes[0].record}", True, configColors["ui"]), (borde2X- textTam*6,0))
        else:
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Puntuacion 1: {self.snakes[0].point}", True, configColors["ui"]), (borde1X,0))
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Puntuacion 2: {self.snakes[1].point}", True, configColors["ui2"]), (borde1X,textTam))
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Récord 1: {self.snakes[0].record}", True, configColors["ui"]), (borde2X- textTam*6,0))
            self.screen.blit(pg.font.SysFont("Arial", textTam).render(f"Récord 2: {self.snakes[1].record}", True, configColors["ui2"]), (borde2X- textTam*6,textTam))

        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.reset()
                page = 1

class Snake():
    def __init__(self, mathead:int, matbody:int, foods:list[int]):
        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]

        self.mathead = mathead
        self.matbody = matbody
        self.foods = foods

        self.reset = True
        self.point = 0 
        self.record = 0
        self.time = 0 
        self.head = self.ramd2()
        self.body = [self.head.copy()]
        self.long = 1
        self.move = [0,0]
        self.moved = False

    def gameover(self):
        if sound: 
            soundGameOver.play()
        self.move = [0,0]
        self.point = 0
        self.long = 1

        self.head = self.ramd2()
        self.body = [self.head.copy()]

    def bucle(self, matriz:list, controls:list):
        if self.reset:
            self.reset = False
            self.record = self.point
            self.head = self.ramd2()
            self.body = [self.head.copy()]
            self.long = 1
            self.move = [0,0]
            self.point = 0

        if self.point > self.record:
                self.record = self.point
                if sound: soundRecord.play()

        self.ramd2 = lambda: [randrange(0, configNumbers["dimention"]), randrange(0, configNumbers["dimention"])]
        self.matriz = matriz
        self.numBox = len(matriz[0])

        for x,y in self.body[:-1]:
            matriz[y][x] = self.matbody
        matriz[self.body[-1][1]][self.body[-1][0]] = self.mathead
        
        key = pg.key.get_pressed()
        if self.moved == False:
            if any(key[k] for k in controls[0]) and self.move[1] != 1:
                self.move = [0,-1]
                self.moved = True
            elif any(key[k] for k in controls[1]) and self.move[1] != -1:
                self.move = [0,1]
                self.moved = True
            elif any(key[k] for k in controls[2]) and self.move[0] != 1:
                self.move = [-1,0]
                self.moved = True
            elif any(key[k] for k in controls[3]) and self.move[0] != -1:
                self.move = [1,0]
                self.moved = True      
    def tick(self):
        self.moved = False
        self.head[0] += self.move[0]; self.head[1] += self.move[1]

        for food in self.foods:
            if self.head == food:
                self.long += configNumbers["longManzana"]
                self.foods.remove(food)
                self.point += 10
                if sound: soundPoint.play()

        if len(self.body) >= self.long:
            self.body.pop(0)
            self.body.append(self.head.copy())
        else:
            self.body.append(self.head.copy())

        if self.head[0] < 0 or self.head[0] >= self.numBox or self.head[1] < 0 or self.head[1] >= self.numBox:
            self.gameover()

        if self.matriz[self.head[1]][self.head[0]] not in [0, 5, self.mathead]:
            self.gameover()

page = 1

sound = True
if pg.mixer.get_init() is None:
    sound = False
else:
    soundMultiSnake = pg.mixer.Sound('./sounds/snakeMulti.mp3')
    soundRecord = pg.mixer.Sound('./sounds/record.mp3')
    soundPoint = pg.mixer.Sound('./sounds/point.mp3')
    soundGameOver = pg.mixer.Sound('./sounds/gameOver.mp3')

intro, start, game = Intro(), Start(), Game()
pages = [intro, start, game]


CODE = [pg.K_UP, pg.K_UP, pg.K_DOWN, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_LEFT, pg.K_RIGHT, pg.K_b, pg.K_a]
code = []
index = 0

while True:
    events = pg.event.get()
    for event in events:
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

    pages[page].bucle(events)

    pg.display.flip()
    CLOCK.tick(60)