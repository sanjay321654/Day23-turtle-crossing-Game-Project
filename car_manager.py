from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "grey", "white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

"""Create cars that are 20px high by 40px wide that are randomly generated along the
 y-axis and move to the left edge of the screen. No cars should be generated
 in the top and bottom 50px of the screen"""


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def creating_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=3.5, stretch_wid=1.5)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

