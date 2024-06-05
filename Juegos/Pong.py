import turtle as tim
from time import sleep
from math import tan

speed = 3
multi = -1.3
score_1 = 0
score_2 = 0

sc = tim.Screen()

sc.title("Pong")
sc.bgcolor("black")
sc.setup(width=800, height=600)

ball = tim.Turtle()

ball.color("red")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = speed
ball.dy = speed
ball.speed(0)

pen = tim.Turtle()

pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(F"Player 1: {score_1}  Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))
pen.speed(0)

player1 = tim.Turtle()

player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.penup()
player1.goto(-350, 0)

player2 = tim.Turtle()

player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.penup()
player2.goto(350, 0)

def up1():
    if player1.ycor() > 240: return
    y = player1.ycor()
    player1.sety(y + 20)

def down1():
    if player1.ycor() < -220: return
    y = player1.ycor()
    player1.sety(y - 20)

def up2():
    if player2.ycor() > 240: return
    y = player2.ycor()
    player2.sety(y + 20)

def down2():
    if player2.ycor() < -220: return
    y = player2.ycor()
    player2.sety(y - 20)

def clickLeft(x,y):
    tim.setheading(0)
    tim.forward(100)

tim.listen()

tim.onscreenclick(clickLeft, 1)
tim.onkey(up1, "w")
tim.onkey(down1, "s")
tim.onkey(up2, "Up")
tim.onkey(down2, "Down")

def resetball():
    pen.clear()
    pen.write(F"Player 1: {score_1}  Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))
    ball.goto(0, 0)
    ball.dx = speed
    ball.dy = speed


##############
#### GAME ####
##############

while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 380:
        score_1 += 1
        resetball()

    elif ball.xcor() < -380:
        score_2 += 1
        resetball()

    if ball.xcor() < -330 and ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50:
        ball.dx *= multi
    
    elif ball.xcor() > 330 and ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50:
        ball.dx *= multi
