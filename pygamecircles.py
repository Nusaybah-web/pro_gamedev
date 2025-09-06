import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

class circle:
    def __init__(self,pos):
        self.pos=pos
    def draw(self):
        self.drawcir=pygame.draw.circle(screen,"black",self.pos,10)

drawing=False

c=circle(pygame.mouse.get_pos())

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEMOTION:
            c=circle(pygame.mouse.get_pos())
            c.draw()
            pygame.display.update()
            
