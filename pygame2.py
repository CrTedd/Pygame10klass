from random import randint
import pygame as pg
import sys
 
W = 400
H = 400
WHITE = (255, 255, 255)
 
 
class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
 
sc = pg.display.set_mode((W, H))
 
# координата x будет случайна
Player1 = Sprite(W/2,(H - H/3),(255,255,255))
enemies = pg.sprite.Group()
enemies.add(Sprite(145, 35, (255,0,0)), Sprite(255, 35, (255,0,0)))
enemies.add(Sprite(365, 35, (255,0,0)), Sprite(475, 35, (255,0,0)))
enemies.add(Sprite(585, 35, (255,0,0)))


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
 
    sc.fill((0,0,0))
    pg.display.update()
    pg.time.delay(20)
    enemies.draw(sc)
    enemies.update()
