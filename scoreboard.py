from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=260)
        self.updated_score()

    def updated_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.updated_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 30, "bold"))
