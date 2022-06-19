from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.referesh()


    def referesh(self):
        randomx = random.randint(-230, 230)
        randomy = random.randint(-230, 200)
        self.speed("fastest")
        self.goto(x=randomx, y=randomy)