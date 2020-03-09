import turtle
turtle.pensize(4)
# 画圆
turtle.circle(15)
turtle.circle(100)
# 画五角星
turtle.color('blue','red')
turtle.begin_fill()
for i in range(5):
    turtle.fd(200)
    turtle.rt(144)
turtle.end_fill()