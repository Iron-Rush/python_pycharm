# TurtleCreate.py
import turtle as t
# t.penup()
t.pendown()
t.seth(-90)
t.fd(160)
t.pensize(20)
t.colormode(255)
for j in range(10):
    t.speed(1000)
    t.pencolor(25*j, 5*j, 15*j)
    t.seth(130)
    t.fd(220)
    for i in range(23):
        t.circle(-80, 10)
    t.seth(100)
    for i in range(23):
        t.circle(-80, 10)
    t.fd(220)