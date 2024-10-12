from random import randint
import pgzrun
WIDTH = 600
HEIGHT=500
score = 0
gameover = False

bee=Actor("zoidberg")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200
    
def draw():
    screen.clear()
    screen.blit("back",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("score: " + str(score),color = "black",topleft = (10,10))

    if gameover:
        screen.fill("blue")
        screen.draw.text("time up you have lost! Your Final Score: " +str(score),midtop = (WIDTH/2,10) )

def fly():
    flower.x = randint(50,WIDTH-50)
    flower.y = randint(50,HEIGHT-50)

def time_up():
    global gameover
    gameover = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x-2

    if keyboard.right:
        bee.x = bee.x+2

    if keyboard.up:
        bee.y = bee.y-2


    if keyboard.down:
        bee.y = bee.y+2

    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score += 1000
        fly()

clock.schedule(time_up,60.0)
pgzrun.go()

