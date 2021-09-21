import turtle as t
from random import *
t.speed(10)
t.shape('turtle')
for i in range(150):
    t.forward(randint(0, 40))
    t.left(randint(-180, 180))
