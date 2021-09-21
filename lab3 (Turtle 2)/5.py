from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 1000

length = 100

def boxpainting(obj, length):
    obj.penup()
    obj.goto(-length, -length)
    obj.pendown()
    obj.goto(length, -length)
    obj.goto(length, length)
    obj.goto(-length, length)
    obj.goto(-length, -length)

def wallcheck(obj, length):
    if abs(unit.xcor())>=(length-10):
            obj.left(180-2*unit.heading())
            obj.forward(2)
    if abs(unit.ycor())>=(length-10):
            obj.right(2*unit.heading())
            obj.forward(2)
    

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]

boxpainting(pool[0], length)

for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(randint(-(length-10), (length-10)), randint(-(length-10), (length-10)))
    unit.left(randint(-180, 180))



for i in range(steps_of_time_number):
    for unit in pool:
        wallcheck(unit, length)
        unit.forward(2)
