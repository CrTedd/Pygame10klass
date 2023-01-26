from random import randint
import pygame as pg
import sys
import time
from pygame import *
 
W = 400
H = 400
WHITE = (255, 255, 255)
Check = True    #переменная для движения противников
count = 0       #глобальный счетчик
FPS = 30
SUBENS = ((255,0,0), (255,0,0), (255,0,0))
ENS = []

UP = False  #состояние клавиш движения
DOWN = False
RIGHT = False
LEFT = False
 
clock = pg.time.Clock()

sc = pg.display.set_mode((W, H))
    
class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
    
Player1 = Sprite(W/2,(H - H/3),(255,255,255))
enemies = pg.sprite.Group()
enemies.add(Sprite(145, 35, (255,0,0)), Sprite(255, 35, (255,0,0)))
enemies.add(Sprite(365, 35, (255,0,0)), Sprite(475, 35, (255,0,0)))
enemies.add(Sprite(35, 35, (255,0,0)), Sprite(585, 35, (255,0,0)))

for i in range (0, 5, 1):
    Enemy += '1'

def Eny (Ey, count):
    if count % 100 == 0:
        enemies.sprites().rect.y = Ey
        Ey += 10
        
running = True

while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == KEYDOWN:           #Обработка нажатия кнопок
            if event.key == K_w: UP = True     #Клавиши движения
            if event.key == K_s: DOWN = True
            if event.key == K_a: LEFT = True
            if event.key == K_d: RIGHT = True

            if event.key == K_ESCAPE: running = False   #Клавиша ESC

        if event.type == KEYUP:             #Обработка отпускания клавиш
            if event.key == K_w: UP = False    #Клавиши движения
            if event.key == K_s: DOWN = False
            if event.key == K_a: LEFT = False
            if event.key == K_d: RIGHT = False


    sc.fill((0,0,0))
    sc.blit(Player1.image, Player1.rect)
    enemies.draw(sc)
    pg.display.update()
    pg.display.flip()
    pg.time.delay(20)

    if UP and Player1.rect.y > H-H/3 : Player1.rect.y -= 2   #Движение корабля игрока
    if DOWN and Player1.rect.y < H - 55 : Player1.rect.y += 2
    if LEFT and Player1.rect.x > 0 : Player1.rect.x -= 2
    if RIGHT and Player1.rect.x < W - 50 : Player1.rect.x += 2

    count+=1
    if count % 30 == 0:
        Check = not Check
    Eny(enemies.sprites().rect.y, count)
    if Check:
        enemies.sprites().rect.x -= 2
        
        #count += 1
    elif not Check:
        enemies.sprites().rect.x += 2
        #count += 1
    enemies.update()


    
pg.quit()
