from random import randint
import turtle


number_of_turtles = 5
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
pool[1].penup()
pool[1].goto(-300, -300)
pool[1].pendown()
pool[1].goto(300, -300)
pool[1].goto(300, 300)
pool[1].goto(-300, 300)
pool[1].goto(-300, -300)
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(-180, 180))



for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
