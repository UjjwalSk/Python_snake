from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-500, 500), randint(-300, 300))
