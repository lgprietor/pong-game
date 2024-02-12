import turtle as t

class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.angle = 60
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.8)
        self.speed("fastest")

    def move(self):

        self.setheading(self.angle)
        self.forward(20)

    def reset(self):
        self.home()
        if self.angle > 0:
            self.angle += 90
        elif self.angle < 0:
            self.angle -= 90



