import turtle as t


class Paddle(t.Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_body()

    def paddle_body(self):
        for i in range (0,2):
            paddle = t.Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(stretch_len=0.5, stretch_wid=3, outline=1)
            paddle.goto()
