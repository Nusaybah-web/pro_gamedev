import pygame,random

pygame.init()
screen=pygame.display.set_mode((800,700))

bg1=pygame.image.load("flappybirdBG1.png")
bg2=pygame.image.load("flappybirdBG2.png")

gameover=False
score=0

font=pygame.font.SysFont("arial",40)

clock=pygame.time.Clock()

flying=False

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
        self.velocity=0
        self.click=False
    def update(self):
        if flying==True:
            self.velocity+=1
            if self.rect.y<500:
                self.rect.y+=self.velocity
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.velocity=-15
                self.click=True
            else:
                self.click=False
            self.counter+=1
            if self.counter>5:
                self.conter=0
                self.index+=1
                if self.index>=3:
                    self.index=0
                self.image=self.birds[self.index]
        
        
        
            

flappybirds=pygame.sprite.Group()

flappies=bird(40,300)
flappybirds.add(flappies)

x=0

while True:
    clock.tick(15)

    screen.blit(bg2,(0,0))
    screen.blit(bg1,(x,532))

    if flying==True and gameover==False:
        x-=5
        if x==-35:
            x=0

    flappybirds.draw(screen)
    flappybirds.update()

    if flappies.rect.y>=500:
        gameover=True
        flying=False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    

    pygame.display.update()