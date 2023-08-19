from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

with open("High_Score.txt") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.color("#18DED5")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def calculate_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.set_high_score()

    def set_high_score(self):
        with open("High_Score.txt", mode="w") as file:
            file.write(str(self.high_score))

