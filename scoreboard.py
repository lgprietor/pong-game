import turtle as t

LIMIT = 280
PACE = 10
FONT = ("Courier", 20, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)
        self.score_player_1()
        self.score_player_2()


        for i in range(0, LIMIT * 2, PACE):
            self.speed("fastest")
            self.pendown()
            self.forward(PACE)
            self.penup()
            self.forward(PACE)

    def score_player_1(self):
        new_turtle = t.Turtle()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x=-50, y=270)
        new_turtle.hideturtle()
        new_turtle.write(f"{self.score1}", move=False, align="center", font=FONT)

    def score_player_2(self):
        new_turtle = t.Turtle()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x=50, y=270)
        new_turtle.hideturtle()
        new_turtle.write(f"{self.score1}", move=False, align="center", font=FONT)
