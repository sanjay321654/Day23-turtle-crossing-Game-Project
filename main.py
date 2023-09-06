import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating random number of cars.
    car_manager.creating_car()
    car_manager.move()

    # Detect when player hits the cars.
    for car in car_manager.all_cars:
        if car.distance(player) < 28:
            game_is_on = False
            score.game_over()
    # If the player reaches the destination then back the started position.

    if player.ycor() == player.is_finish:
        player.reset_position()
        score.increase_score()
        car_manager.speed_up()

screen.exitonclick()
