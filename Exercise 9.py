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

def ex9():
    for i in range(3, 13):
        polygon(i, 10*i, i)
            
ex9()

