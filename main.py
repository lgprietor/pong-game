import turtle as t
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game by Luisga")
screen.listen()
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

screen.onkeypress(paddle.move_up_paddle1,"w")
screen.onkeypress(paddle.move_up_paddle2,"Up")
screen.onkeypress(paddle.move_down_paddle1,"s")
screen.onkeypress(paddle.move_down_paddle2,"Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    x_cor = []
    y_cor = []
    x_cor.append(ball.xcor())
    y_cor.append(ball.ycor())
    ball.move()
    x_cor.append(ball.xcor())
    y_cor.append(ball.ycor())
    # print(x_cor)

    # Detecting collisions with walls upper and lower:

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.angle = ball.angle*-1
        print(ball.angle)

    # Detecting collisions with paddles:

    # Paddle 1:

    if x_cor[-1] - x_cor[-2] < 0 and y_cor[-1] - y_cor[-2] > 0:
        if ball.distance(paddle.paddle1) < 50 and ball.xcor() < -340:
            ball.angle = ball.angle - 90
    elif x_cor[-1] - x_cor[-2] < 0 and y_cor[-1] - y_cor[-2] < 0:
        if ball.distance(paddle.paddle1) < 50 and ball.xcor() < -340:
            ball.angle = ball.angle + 90

    # Paddle 2:

    if x_cor[-1] - x_cor[-2] > 0 and y_cor[-1] - y_cor[-2] < 0:
        if ball.distance(paddle.paddle2) < 50 and ball.xcor() > 340:
            ball.angle = ball.angle - 90
    elif x_cor[-1] - x_cor[-2] > 0 and y_cor[-1] - y_cor[-2] > 0:
        if ball.distance(paddle.paddle2) < 50 and ball.xcor() > 340:
            ball.angle = ball.angle + 90

    print(ball.angle)





screen.exitonclick()