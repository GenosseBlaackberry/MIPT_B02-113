import turtle as t

def artist(a):
    for i in a:
        t.penup()
        if i[2]:
            t.pendown()
        t.left(i[0])
        t.forward(i[1])


data = open('text.txt', 'r')
a = eval(data.read())
data.close()

for i in input():
      artist(a[int(i)])
