from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("courier", "24", "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score_board()
    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)