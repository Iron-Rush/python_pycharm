# NumberTube2.py
import turtle
import time
# 绘制一小块空白
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单段数码管
    drawGap()       #线段绘制前，添加空白
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()       #线段绘制完后，添加空白
    turtle.right(90)

# 绘制整个数码管函数
def drawNumber(number):
    drawLine(True) if number in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)  #一号数码管
    drawLine(True) if number in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)  #二号数码管
    drawLine(True) if number in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)  #三号数码管
    drawLine(True) if number in [0, 2, 6, 8] else drawLine(False)  #四号数码管
    turtle.left(90)                                                         #左转九十度，绘制上半部分
    drawLine(True) if number in [0, 4, 5, 6, 8, 9] else drawLine(False)  #五号数码管
    drawLine(True) if number in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)  #六号数码管
    drawLine(True) if number in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)  #七号数码管
    turtle.left(180)    #初始化画笔朝向
    # 初始化画笔下一次绘制位置
    turtle.penup()
    turtle.fd(20)
# 绘制日期函数，将日期拆分为单个数字，调用drawNumber()函数
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial", 18, "normal"))
        elif i == '+':
            turtle.write("日",font=("Arial", 18, "normal"))
        else:
            drawNumber(eval(i)) #通过eval()函数，将字符串变为数字
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
    # drawDate('20200313')
    turtle.hideturtle()
    turtle.done()
main()

# drawNumber(8)