import random as r
from turtle import Turtle

class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5 )
        self.speed("fastest")
        self.goto(r.randint(-280, 280), r.randint(-280, 280))


    def change_position(self):
        self.goto(r.randint(-280, 280), r.randint(-280, 280))