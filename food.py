from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.respawn()

    def respawn(self):
        new_xy = (random.randrange(-280,280,20), random.randrange(-280,280,20))
        self.setposition(new_xy)
