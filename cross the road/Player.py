from tkinter import CENTER
from turtle import Turtle
move_distance = 10
start=(0,-280)
end=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)
        self.playerspeed=move_distance
    def fw(self):
        new_y=self.ycor()+self.playerspeed
        self.goto(self.xcor(),new_y)
    def left(self):
        new_x=self.xcor()-self.playerspeed
        self.goto(new_x,self.ycor())
    def right(self):
        new_x=self.xcor()+self.playerspeed
        self.goto(new_x,self.ycor())
    def down(self):
        new_y=self.ycor()-self.playerspeed
        self.goto(self.xcor(),new_y)
    def start(self):
        self.goto(start)
    def finish(self):
        if self.ycor()>end:
            return True
        else:
            return False
    def level_up(self):
        self.playerspeed+=3
    