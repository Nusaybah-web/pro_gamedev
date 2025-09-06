import pgzrun,random

WIDTH=500
HEIGHT=500


gravity=2000

class ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.radius=30

    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,"red")

red=ball(20,20)

def draw():
    screen.clear()
    red.draw()

def update(t):
    uy=red.vy 
    red.vy+=gravity*t
    red.y+=(uy+red.vy)*0.5*t

    if red.y>=HEIGHT:
        red.y=HEIGHT
        red.vy=-red.vy*0.9
    
    red.x+=red.vx*t

    if red.x>=WIDTH or red.x<=0:
        red.vx=-red.vx

    
def on_key_down(key):
    if key==keys.SPACE:
        red.vy=-500



pgzrun.go()

