#TextProBarV1.py
import time #引入time库
scale = 10
print("{0:—^20}".format("执行开始"))    #打印开始的标签
for i in range(scale + 1):
    a = '*' * i             #已加载任务进度
    b = '.' * (scale - i)   #未加载任务进度
    c = (i/scale) * 100     #已加载占全部任务百分比
    print("{:^3.0f}%[{}—>{}]".format(c,a,b))
    time.sleep(0.1)         #休眠
print("{0:—^20}".format("执行结束"))    #打印结束标签