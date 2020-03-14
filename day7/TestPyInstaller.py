# TestPyInstaller.py
# 科赫曲线绘制
import turtle
def koch(size, n):  #科赫直线的长度size，绘制的阶数n
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]: #先向前行绘制，左转60度绘制，右转60度绘制，左转60度绘制
            turtle.left(angle)
            koch(size/3, n-1) 
def main():
    turtle.setup(800, 800)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    # koch(200,3)     #3阶科赫曲线
    #科赫雪花为3段3阶科赫曲线绘制而成
    level = 3
    koch(400, 3)
    turtle.right(120)
    koch(400, 3)
    turtle.right(120)
    koch(400, 3)
    turtle.right(120)
    turtle.hideturtle()
    turtle.done()

main()