# AutoTraceDraw.py
import turtle as t
# 初始化绘画环境
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")    #将文本中每行的换行符转换为空字符串
    datals.append(list(map(eval, line.split(",")))) #在detals列表中放入列表(二维列表)
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if(datals[i][1]):
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()