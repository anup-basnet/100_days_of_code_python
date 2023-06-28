from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
            return int(high_score)

    def set_high_score(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
        self.score = 0
        self.update_scoreboard()
