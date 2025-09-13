import pygame,random

pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("bouncing ball")
pygame.display.update()

class ball:
    def __init__(self,color,pos,radius,speed):
        self.color=color
        self.x,self.y=pos
        self.radius=radius
        self.xspeed,self.yspeed=speed
    def display(self):
        self.drawcir=pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

    def move(self):
        self.x+=self.xspeed
        self.y+=self.yspeed
        if self.x>=1000 or self.x<=0:
            self.xspeed=-self.xspeed

        if self.y>=600 or self.y<=0:
            self.yspeed=-self.yspeed

red=ball("red",(200,200),22,[1,2])
blue=ball("green",(300,200),20,[2,2])
green=ball("pink",(200,300),18,[2,1])
orange=ball("blue",(400,200),21,[3,3])
pink=ball("orange",(200,400),19,[2,3])

colours=[red,blue,green,orange,pink]

clock=pygame.time.Clock()

while True:
    clock.tick(400)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    screen.fill("black")
    for i in colours:
        i.display()
        i.move()


    pygame.display.update()