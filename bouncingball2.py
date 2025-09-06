import pygame

pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("bouncing ball")
pygame.display.update()

ball=pygame.draw.circle(surface=screen,color="red",center=[100,100],radius=20)

speed=[1,1]

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    clock.tick(400)

    screen.fill("black")

    ball=ball.move(speed)

    if ball.right>=1000 or ball.left<=0:
        speed[0]=-speed[0]
    
    if ball.top<0 or ball.bottom>600:
        speed[1]=-speed[1]

    pygame.draw.circle(surface=screen,color="red",center=ball.center,radius=20)

    pygame.display.update()