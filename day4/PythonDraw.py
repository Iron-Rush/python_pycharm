# turtle 海龟库
import turtle
# turtle.setup(width, height, startx, starty) 窗体宽度，窗体高度，起始点横坐标，起始点纵坐标
turtle.setup(650, 350, 200, 200)#初始化窗体大小和位置，setup函数非必须
turtle.penup()#抬起画笔，不记录轨迹
turtle.fd(-250)#向前行走-250，倒退250 bk(250)
turtle.pendown()#落下画笔,继续绘画
turtle.pensize(25)#画笔宽度，海龟腰围pensize=width
turtle.pencolor("purple")#color为颜色字符串或r,g,b值,
turtle.pencolor(0.63, 0.13, 0.94)#也可以传入定义好的rgb元组turtle.pencolor((0.63.0s.13.0.94))
turtle.seth(-40)#海龟朝向变为绝对的-40度
for i in range(4):#生成0-3的序列
    turtle.circle(40, 80)#绘制向上40为半径，80度的圆弧
    turtle.circle(-40, 80)#绘制向下40为半径，80度的圆弧
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
