from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""Create a turtle player that starts at the bottom
of the screen and listen for the "Up" keypress to move the turtle north."""
car = CarManager()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.is_finish = FINISH_LINE_Y
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        # if self.ycor() < 280:
        self.forward(MOVE_DISTANCE)

    def reset_position(self):

            self.goto(STARTING_POSITION)
            car.speed_up()
