import turtle
turtle.shape('turtle')
import math
turtle.speed(10)

def ex7():
    for i in range(720):
        turtle.forward(i**(1/7))
        turtle.left(1)
ex7()
