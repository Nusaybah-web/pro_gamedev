import pygame,random

pygame.init()
screen=pygame.display.set_mode((600,600))

score=0

clock=pygame.time.Clock()

gameover=False

class block(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.image.fill(color)
        self.rect=self.image.get_rect()
    def reset(self):
        self.rect.x=random.randint(10,590)
        self.rect.y=random.randint(-300,-20)
    def update(self):
        self.rect.y+=1
        if self.rect.y==600:
            self.reset()


class redblock(block):
    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class blueblock(block):
    global gameover
    def update(self):
        self.rect.y+=1

class yellowblock(block):
    def update(self):
        self.rect.y+=1
        if self.rect.y==600:
            self.reset()

coke=pygame.sprite.Group()
whites=pygame.sprite.Group()
yellows=pygame.sprite.Group()
blues=pygame.sprite.Group()

red=redblock("red")
coke.add(red)

for i in range(30):
    white=block("white")
    whites.add(white)
    coke.add(white)

for i in range(5):
    blue=blueblock("blue")
    blues.add(blue)
    coke.add(blue)

for i in range(5):
    yellow=yellowblock("yellow")
    yellows.add(yellow)
    coke.add(yellow)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
   

    clock.tick(200)

    screen.fill("black")

    coke.update()

    fanta=pygame.sprite.spritecollide(red,whites,dokill=False)
    redbull=pygame.sprite.spritecollide(red,blues,dokill=False)
    mountaindew=pygame.sprite.spritecollide(red,yellows,dokill=False)

    for i in fanta:
        i.reset()

    for i in redbull:
        score+=5
        i.reset()

    for i in mountaindew:
        gameover=True

    if gameover:
        print(score)
        exit()

    coke.draw(screen)

    pygame.display.update()

