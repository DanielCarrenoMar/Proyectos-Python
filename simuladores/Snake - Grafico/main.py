import pygame as pg
pg.init()
CLOCK = pg.time.Clock()
H = pg.display.Info().current_h
W = pg.display.Info().current_w
pg.display.set_mode((W-30,H-60), pg.RESIZABLE) 
pg.display.set_caption("Snake")

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
        self.configColors = {
            "fondo": "#000000",
            "cabeza": "#01DF3C",
            "cuerpo": "#10BD3E",
            "comida": "#952121",
            "puntuacion": "#FFFFFF",
        }
        self.configNumbers = {

        }
        
    def bucle(self):
        self.screen.fill("#000000")
        pg.draw.circle(self.screen, "#FFFFFF", (30,30), 10)
        
class Game():
    def __init__(self):
        self.screen = pg.display.get_surface()

    def bucle(self):
        self.screen.fill("#000000")
        
class Pages():
    def __init__(self, pages:list):
        self.main = 0
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

intro, start, game = Intro(), Start(), Game()
pages = Pages([intro, start, game])

while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.display.set_caption("hola3")
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pages.bucle()

    pg.display.flip()
    CLOCK.tick(60)