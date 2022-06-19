from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.shapesize(0.001)
        self.scoring()

    def scoring(self):

        self.clear()
        self.write(f"score = {self.score} ", align=ALIGNMENT, font= FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=('Arial', 30, 'normal'))
