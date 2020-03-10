#海龟绘图
import turtle

# turtle.setup(width, height, startx, starty) 窗体宽度，窗体高度，起始点横坐标，起始点纵坐标
turtle.setup(650, 350, 200, 200) #初始化窗体大小和位置，setup函数非必须
# goto利用窗体内绝对坐标，索引海龟前进
# (0,0)坐标位于窗体最中心
turtle.goto(100, 0)
turtle.goto(100, -100)
turtle.goto(0, 0)

#利用海龟前进方向控制海龟
# 前进turtle.fd(d)
turtle.fd(100)
# 后退turtle.bk(d)
turtle.bk(150)
# 曲线运动turtle.circle(r,angle)
turtle.circle(30, 180)#(半径，圆弧角度）
# turtle.seth(angle)
# 改变海龟头朝方向,只改变头朝方向，不行进
# angle为相对于画布坐标的绝对角度，不是相对于海龟头朝方向的角度
turtle.seth(0)
# turtle.left/right(angle)
# 根据海龟当前的头朝向，进行相对转弯
turtle.right(20)
turtle.fd(100)


# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2/3)
# turtle.done()
