# Cal_PI_V2.py
from random import random
from time import perf_counter
DARTS = 1000 * 1000     #区域中抛洒点的总数
hits = 0.0              #在圆内部点的总数
start = perf_counter()  #启动计时
for i in range(1, DARTS + 1):   #对所有点进行抛洒
    x, y = random(), random()   #随机生成坐标
    dist = pow(x ** 2 + y ** 2, 0.5)    #计算点距离圆心的距离， x^2+y^2，开根号
    if dist <= 1.0:     #判断点是否落在圆内
        hits += 1
pi = 4 * (hits/DARTS)
print("圆周率的值为：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter() - start))