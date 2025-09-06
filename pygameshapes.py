import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()



class shapes:
    def __init__(self,colour,pos):
        self.screen=screen
        self.colour=colour
        self.pos=pos

    def draw(self):
        self.drawrect=pygame.draw.rect(screen,self.colour,self.pos)

red=shapes("red",(20,20,50,50))
green=shapes("green",(80,100,40,40))
blue=shapes("blue",(200,300,100,100))

class circles:
    def __init__(self,colour,pos,radius):
        self.colour=colour
        self.pos=pos
        self.radius=radius
    def draw2(self):
        self.drawcir=pygame.draw.circle(screen,self.colour,self.pos,self.radius)
    def grow(self):
        self.radius+=5
        self.drawcir=pygame.draw.circle(screen,self.colour,self.pos,self.radius)
        

red2=circles("red",(50,50),100)
green3=circles("green",(80,100),80)
blue4=circles("blue",(200,300),50)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
        if event.type==pygame.MOUSEBUTTONDOWN:
            red2.draw2()
            green3.draw2()
            blue4.draw2()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            red2.grow()
            green3.grow()
            blue4.grow()
            pygame.display.update()

    
    red.draw()
    green.draw()
    blue.draw()
    pygame.display.update()