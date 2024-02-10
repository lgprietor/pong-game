import turtle as t
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

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

    screen.update()



screen.exitonclick()