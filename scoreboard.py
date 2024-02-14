import turtle as t

LIMIT = 280
PACE = 10
FONT = ("Courier", 60, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.scores = []
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-(LIMIT*2))
        self.score_player_1()
        self.score_player_2()


        for i in range(0, LIMIT * 2, PACE):
            self.pendown()
            self.forward(PACE)
            self.penup()
            self.forward(PACE)

    def score_player_1(self):
        new_turtle = t.Turtle()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x=-100, y=200)
        new_turtle.hideturtle()
        new_turtle.write(f"{self.score1}", move=False, align="center", font=FONT)
        self.scores.append(new_turtle)

    def score_player_2(self):
        new_turtle = t.Turtle()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x=100, y=200)
        new_turtle.hideturtle()
        new_turtle.write(f"{self.score1}", move=False, align="center", font=FONT)
        self.scores.append(new_turtle)

    def update_score_paddle1(self):
        self.score1 += 1
        self.scores[0].clear()
        self.scores[0].write(f"{self.score1}", move=False, align="center", font=FONT)

    def update_score_paddle2(self):
        self.score2 += 1
        self.scores[1].clear()
        self.scores[1].write(f"{self.score2}", move=False, align="center", font=FONT)

