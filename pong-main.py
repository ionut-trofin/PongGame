import turtle
import pygame
import audio  

pygame.init()

wn = turtle.Screen()
wn.title("My first Game!!")
wn.bgcolor("black")
wn.setup(width=1920, height=1080)
wn.tracer(0)


score_a = 0
score_b = 0

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("green")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-700, 0)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("blue")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(700, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("magenta")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy =0.2


pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0   Player B: 0", align= "center", font=("Times New Roman", 24, "normal"))


audio.play_song()



def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -=20
    paddle_right.sety(y)

def toggle_mute():
    global muted
    muted = not muted
    if muted:
        pygame.mixer_music.pause()
    else:
        pygame.mixer_music.unpause()


wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")
wn.onkeypress(toggle_mute, "m")

while True:
        wn.update()
   
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


    #i took the border checking method from a tutorial
        if ball.ycor() > 510:
            ball.sety(510)
            ball.dy *= -1

        if ball.ycor() < -510:
            ball.sety(-510)
            ball.dy *= -1


        if  ball.xcor() > 790:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Times New Roman", 24, "normal"))

        if ball.xcor() < -790:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Times New Roman", 24, "normal"))


        if (ball.xcor() > 680 and ball.xcor() < 690) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
            ball.setx(680)
            ball.dx *= -1

        if (ball.xcor() < -680 and ball.xcor() > -690) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
            ball.setx(-680)
            ball.dx *= -1
