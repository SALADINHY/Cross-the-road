from ast import Str
from turtle import Turtle
import random
colors=["blue","yellow","red","black","pink","purple"]
starting=5
move_distance=10

class Car(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.speed=move_distance
    def create_cars(self):
        rand_num=random.randint(1,5)
        if rand_num == 5:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)
    def level_up(self):
        self.speed+=5
    