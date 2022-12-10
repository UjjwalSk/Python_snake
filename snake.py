import turtle
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_block(pos)

    def add_block(self, pos):
        block = turtle.Turtle("square")
        block.penup()
        block.color("white")
        block.goto(pos)
        self.blocks.append(block)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for i in range(len(self.blocks)-1, 0, -1):
            self.blocks[i].goto(self.blocks[i-1].xcor(),
                                self.blocks[i-1].ycor())
        self.head.forward(MOVE)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
