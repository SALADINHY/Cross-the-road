from turtle import Screen
import time
from Player import Player
from car import Car
screen = Screen();
screen.setup(width=600,height=600)
screen.tracer(0)
player = Player()
game_on = True
screen.listen()
screen.onkey(player.fw,"w")
screen.onkey(player.left,"a")
screen.onkey(player.down,"s")
screen.onkey(player.right,"d")
car=Car()
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()
    for i in car.all_cars :
        if i.distance(player) < 25:
            game_on=False
            print("Game off")
    if player.finish():
        player.start()
        car.level_up()
        player.level_up()