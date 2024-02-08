import turtle as t
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

screen.update()


screen.onkeypress(paddle.move_up_paddle1,"w")
screen.onkeypress(paddle.move_up_paddle2,"Up")
screen.onkeypress(paddle.move_down_paddle1,"s")
screen.onkeypress(paddle.move_down_paddle2,"Down")





screen.exitonclick()