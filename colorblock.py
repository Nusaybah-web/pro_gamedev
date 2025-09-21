import pygame
from random import randint

pygame.init()
screen=pygame.display.set_mode((150,150))

class block(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((40,39))
        self.image.fill(color)
        self.rect=self.image.get_rect(topleft=(50,50))

    def change(self,pos):
        self.rect.collidepoint(pos)
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        self.image.fill((r,g,b))


colours=block((20,20,20))
fanta=pygame.sprite.GroupSingle(colours)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            colours.change(event.pos)
        
    fanta.draw(screen)

    pygame.display.update()