import turtle as t


class Paddle(t.Turtle):

    def __init__(self):
        super().__init__()
        self.paddles = []
        self.paddle_body()
        self.paddle1 = self.paddles[0]
        self.paddle2 = self.paddles[1]

    def paddle_body(self):
        for i in range(-1, 2, 2):
            paddle = t.Turtle()
            paddle.penup()
            paddle.speed("fastest")
            paddle.goto(x=270 * i, y=0)
            paddle.shape("square")
            paddle.color("white")
            paddle.setheading(90)
            paddle.shapesize(stretch_len=3, stretch_wid=0.5, outline=1)
            self.paddles.append(paddle)

    def move_up_paddle1(self):

        self.paddle1.setheading(90)
        self.paddle1.forward(20)

    def move_up_paddle2(self):

        self.paddle2.setheading(90)
        self.paddle2.forward(20)

    def move_down_paddle1(self):
        self.paddle1.setheading(270)
        self.paddle1.forward(20)

    def move_down_paddle2(self):
        self.paddle2.setheading(270)
        self.paddle2.forward(20)