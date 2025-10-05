import pygame,random

pygame.init()
screen=pygame.display.set_mode((800,700))

bg1=pygame.image.load("flappybirdBG1.png")
bg2=pygame.image.load("flappybirdBG2.png")

gameover=False
score=0

font=pygame.font.SysFont("arial",40)

clock=pygame.time.Clock()

flying=True

class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.index=0
        self.birds=[]
        for i in range(1,4):
            flappy=pygame.image.load(f"flappybird{i}.png")
            self.birds.append(flappy)
        self.image=self.birds[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.counter=0
    def update(self):
        if gameover==False:
            self.counter+=1
            if self.counter>5:
                self.conter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image=self.birds[self.index]
        if flying==True:
            self.rect.y+=10
            if self.rect.y>532:
                self.rect.y=532

flappybirds=pygame.sprite.Group()

flappies=bird(40,400)
flappybirds.add(flappies)

while True:
    clock.tick(10)

    screen.blit(bg2,(0,0))
    screen.blit(bg1,(0,532))

    flappybirds.draw(screen)
    flappybirds.update()

    if flappies.rect.y==532:
        gameover=True
        flying=False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True

    pygame.display.update()