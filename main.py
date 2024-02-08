import turtle as t
from paddle import Paddle

screen = t.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.listen()

paddle = Paddle()

screen.onkey(paddle.move_up_paddle1,"w")
screen.onkey(paddle.move_up_paddle2,"Up")
screen.onkey(paddle.move_down_paddle1,"s")
screen.onkey(paddle.move_down_paddle2,"Down")





screen.exitonclick()