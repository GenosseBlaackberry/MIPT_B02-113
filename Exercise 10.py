import turtle
turtle.shape('turtle')
import math
turtle.speed(10)

def polygon(n, r, alpha, spin=1, par=True, T=True):
    pos =[]
    if par:
        a=r
    else:
        a=r*(2*math.sin(math.pi/n))
    if T:
        turtle.penup()
        turtle.forward(a/(2*math.sin(math.pi/n)))
        turtle.left(spin*180-90*(n-2)/n)
        turtle.pendown()
    for i in range(alpha):
        turtle.forward(a)
        turtle.left(spin*360/n)
        pos.append(turtle.position())
    if T:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.right(spin*180-90*(n-2)/n)
    return pos

def ex10(n=10):
    for i in range(n):
        polygon(360, 30, 360, 1, 0, 0)
        turtle.left(360/n)
            
ex10()