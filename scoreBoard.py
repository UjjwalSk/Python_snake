from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier", 25, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!!!", align="center",
                   font=("Arial", 25, "normal"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()
