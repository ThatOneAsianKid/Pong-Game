from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
PLAYER_1_X_CORD = -100
PLAYER_2_X_CORD = 100
Y_CORD = 200

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(PLAYER_1_X_CORD, Y_CORD)
        self.write(self.l_score, False, align=ALIGNMENT, font=FONT)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(PLAYER_2_X_CORD, Y_CORD)
        self.write(self.r_score, False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)