import pygame

pygame.init()
screen=pygame.display.set_mode((600,700))
screen.fill("white")

score=0

font=pygame.font.SysFont("arial",20)

pictures= {
    "Candycrush":pygame.image.load("gamecandycrush.jpg"),
    "Ludo":pygame.image.load("gameludo.png"),
    "TempleRun":pygame.image.load("gametemplerun.png"),
    "SubwaySurfers":pygame.image.load("gamesubway.png"),
}

cordnates={
    "Candycrush":pygame.Rect(100,100,100,100),
    "Ludo":pygame.Rect(100,250,100,100),
    "TempleRun":pygame.Rect(100,400,100,100),
    "SubwaySurfers":pygame.Rect(100,550,100,100),
}

tc={
    "Candycrush":pygame.Rect(400,100,100,100),
    "Ludo":pygame.Rect(400,250,100,100),
    "TempleRun":pygame.Rect(400,400,100,100),
    "SubwaySurfers":pygame.Rect(400,550,100,100),
}

names={
    "Candycrush":"Candycrush",
    "Ludo":"Ludo",
    "TempleRun":"TempleRun",
    "SubwaySurfers":"SubwaySurfers",
}



for name,pos in cordnates.items():
    screen.blit(pictures[name],(pos.x,pos.y))

for name,pos in tc.items():
    text=font.render(name,True,"black")
    screen.blit(text,(pos.x,pos.y))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos1=pygame.mouse.get_pos()

        elif event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()

            sl=None
            el=None

            for lable,rect in cordnates.items():
                if rect.collidepoint(pos1):
                    sl=lable

            for lable,rect in tc.items():
                if rect.collidepoint(pos2):
                    el=lable

            if el and sl:
                pygame.draw.line(screen,"black",pos1,pos2,3)
                if names[sl]==el:
                    score+=1
                    print(score)
                else:
                    print("wrong match")
            
        pygame.display.update()


