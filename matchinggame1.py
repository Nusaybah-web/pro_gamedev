import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

surfers=pygame.image.load("gamesubway.png")
ludo=pygame.image.load("gameludo.png")
cc=pygame.image.load("gamecandycrush.jpg")
tr=pygame.image.load("gametemplerun.png")

font=pygame.font.SysFont("arial",30)

text1=font.render("subway surfers",True,"black")
text2=font.render("candy cruch",True,"black")
text3=font.render("ludo",True,"black")
text4=font.render("temple run",True,"black")

screen.blit(surfers,(20,20))
screen.blit(text1,(150,20))

screen.blit(ludo,(20,130))
screen.blit(text2,(130,150))

pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pos=pygame.mouse.get_pos()
                c1=pygame.draw.circle(surface=screen,color="black",center=pos,radius=10)
                pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                pos2=pygame.mouse.get_pos()
                c2=pygame.draw.circle(surface=screen,color="black",center=pos2,radius=10)
                pygame.draw.line(surface=screen,color="black",start_pos=pos,end_pos=pos2,width=1)
                pygame.display.update()
