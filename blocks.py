import pygame,random

pygame.init()
screen=pygame.display.set_mode((600,600))

class block(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.image.fill(color)
        self.rect=self.image.get_rect()

coke=pygame.sprite.Group()
whites=pygame.sprite.Group()

red=block("red")
coke.add("red")

for i in range(50):
    white=block("white")
    white.rect.x=(random.randint(0,600))
    white.rect.y=(random.randint(0,600))
    whites.add(white)
    coke.add(white)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    coke.draw(screen)

    pygame.display.update()