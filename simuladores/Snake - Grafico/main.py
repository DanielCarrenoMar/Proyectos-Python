import pygame as pg
pg.init()
CLOCK = pg.time.Clock()
H = pg.display.Info().current_h
W = pg.display.Info().current_w
pg.display.set_mode((W-30,H-60), pg.RESIZABLE) 
pg.display.set_caption("hola")

class Intro():
    def __init__(self):
        self.screen = pg.display.get_surface()
        
    def bucle(self):
        self.screen.fill("#000000")
        pg.draw.circle(self.screen, "#FFFFFF", (30,30), 10)
        
class Game():
    def __init__(self):
        self.screen = pg.display.get_surface()
        
    def bucle(self):
        self.screen.fill("#FFFFFF")
        
class Pages():
    def __init__(self, pages:list):
        self.main = 0
        self.pages = pages
        
    def bucle(self):
        self.pages[self.main].bucle()
    def next(self):
        self.main += 1
        self.main %= len(self.pages)
    def back(self):
        self.main -= 1
        self.main %= len(self.pages)
    def goto(self, num:int):
        self.main = num
        self.main %= len(self.pages)

intro, game = Intro(), Game()
controler = Pages([intro, game])

while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.display.set_caption("hola3")
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    controler.bucle()

    pg.display.flip()
    CLOCK.tick(60)