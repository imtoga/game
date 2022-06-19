from turtle import Screen
from snack_structure import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
food = Food()
score = Score()

screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()
    if s.head.distance(food) < 15 :
        score.scoring()
        food.referesh()
        s.extend()
    if s.head.xcor() > 250 or s.head.xcor() < -250 or s.head.ycor() > 250 or s.head.ycor() < -250:
        game_is_on = False
        score.game_over()

    for segment in s.snakes[1:]:
        if s.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
