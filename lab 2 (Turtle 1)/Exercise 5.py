import turtle
turtle.shape('turtle')
import math
turtle.speed(10)

def ex5():
    for j in range(50, 151, 10):
        for i in range(4):
            turtle.forward(j)
            turtle.left(90)
        turtle.penup()
        turtle.backward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.pendown()

ex5()
