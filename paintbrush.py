import pygame,random

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("black")
pygame.display.update()


currentcol=(255,255,255)

drawing=False
pos1=None

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                drawing=True
                pos1=event.pos
                pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                drawing=False
                pygame.display.update()

        elif event.type==pygame.MOUSEMOTION:
            if drawing:
                pos2=event.pos
                pygame.draw.line(screen,currentcol,pos1,pos2)
                pos1=pos2
                pygame.display.update()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                currentcol=(r,g,b)

    
