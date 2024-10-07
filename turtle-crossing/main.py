import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()
player = Player()

car_manager = CarManager()
display = Scoreboard()

screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    display.update_scoreboard()

    # if player collides with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            display.game_over()
            game_is_on = False

    # if player gets to edge of screen
    if player.ycor() == 300:
        player.reset_position()
        display.level_up()
        car_manager.Level_speed()
screen.exitonclick()
