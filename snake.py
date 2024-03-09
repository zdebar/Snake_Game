from turtle import Screen, Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for i in range(0,3):
            segment = Turtle("square")
            segment.color("white")
            segment.up()
            segment.setposition(0-20*i, 0)
            self.segments.append(segment)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_xy = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(new_xy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

