import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("2P game")

bg=pygame.image.load("space.png")
red=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("redship.png"),(50,50)),270)
yellow=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellowship.png"),(50,50)),90)

border=pygame.Rect(375,0,30,600)

class ships(pygame.sprite.Sprite):
    def __init__(self,x,y,image,side):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect(topleft=(x,y))
        self.health=10
        self.side=side
    def move1(self,keys):
        if self.rect.y>=0:
            if keys[pygame.K_UP]:
                self.rect.y-=2
        if self.rect.y<=550:
            if keys[pygame.K_DOWN]:
                self.rect.y+=2
        if self.rect.x>=410:
            if keys[pygame.K_LEFT]:
                self.rect.x-=2
        if self.rect.x<=750:
            if keys[pygame.K_RIGHT]:
                self.rect.x+=2
    def move2(self,keys):
        if self.rect.y>=0:
            if keys[pygame.K_w]:
                self.rect.y-=2
        if self.rect.y<=550:
            if keys[pygame.K_s]:
                self.rect.y+=2
        if self.rect.x>=0:
            if keys[pygame.K_a]:
                self.rect.x-=2
        if self.rect.x<=320:
            if keys[pygame.K_d]:
                self.rect.x+=2
    def shoot(self,bulletgroup):
        if self.side=="left":
            bullet=laser(self.rect.right,self.rect.centery,8,color="blue")
        elif self.side=="right": 
            bullet=laser(self.rect.left,self.rect.centery,-8,color="orange")

        bulletgroup.add(bullet)


class laser(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,color):
        self.image=pygame.Surface((5,2))
        self.image.fill(color)
        self.rect=self.image.get_rect(center=(x,y))
        self.speed=speed
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x<=0 or self.rect.x>=800:
            self.kill()                                       
    

bulletgroup=pygame.sprite.Group()

yellowship=ships(200,300,yellow,"left")
redship=ships(600,300,red,"right")

allsprite=pygame.sprite.Group(yellowship,redship)

gameover=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RCTRL:
                redship.shoot(bulletgroup)
        
            if event.key==pygame.K_e:
                yellowship.shoot(bulletgroup)

    keys=pygame.key.get_pressed()
    redship.move1(keys)
    yellowship.move2(keys)
    bulletgroup.update()

    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"white",border)

    allsprite.draw(screen)
    bulletgroup.draw(screen)

    pygame.display.update()