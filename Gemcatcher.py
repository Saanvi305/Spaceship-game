import pgzrun
import random

WIDTH=600
HEIGHT=600
score=0
TITLE="Gemcatcher"
gameover=0

gem=Actor("gem")
gem.x=random.randint(20,550)
gem.y=20

ship=Actor("ship")
ship.x=100
ship.y=450

def draw():
    screen.fill("blue")
    if gameover:
        screen.draw.text("gameover",color="red",topleft=(10,10))

        screen.draw.text("Score:"+str(score),color="red",topleft=(20,20))
    else:
        gem.draw()
        ship.draw()
     
        screen.draw.text("Score:"+str(score),color="red",topleft=(20,20))
    

                    

def update():
    global score,gameover
    gem.y=gem.y+2
    if gem.y>HEIGHT:
        gem.x=random.randint(20,550)
        gem.y=20
        gameover=True
    if keyboard.left:
        ship.x=ship.x-2
    if keyboard.right:
        ship.x=ship.x+2
    if gem.colliderect(ship):
        score+=10
        gem.x=random.randint(20,550)
        gem.y=20









pgzrun.go()