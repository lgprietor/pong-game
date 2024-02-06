import turtle as t
from paddle import Paddle

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

paddle = Paddle()


screen.exitonclick()