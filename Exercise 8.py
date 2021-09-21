import turtle
turtle.shape('turtle')
import math
turtle.speed(10)

def ex8():
    for j in range(50, 151, 10):
        for i in range(4):
            turtle.forward(j+2.5*i)
            turtle.left(90)
            
ex8()
