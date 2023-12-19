import turtle
import time
from Snake import Snake
from Fruit import Fruit
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

Snake = Snake()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

fruit = Fruit()
scoreboard = ScoreBoard()
score = 0
game_is_on = True

while game_is_on:
    screen.update()
    frame_rate = 0.1
    time.sleep(frame_rate)

    Snake.move()

    if Snake.segments[0].xcor() > 285 or Snake.segments[0].xcor() < -285 or Snake.segments[0].ycor() > 285 or Snake.segments[0].ycor() < -285:
        scoreboard.game_over()
        game_is_on = False


    if Snake.segments[0].distance(fruit) < 15:
        scoreboard.increase_score()
        fruit.change_position()
        Snake.extend()
        print(score)

    for segment in Snake.segments[1:]:
        if Snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()















screen.exitonclick()