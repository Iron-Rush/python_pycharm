try:
    f = open('D:\Work\PythonWorkspace\untitled\day2\log.txt', 'r')
    # print(f.read())
    # avg, cnt = 0, 0-
    # for line in f:
    #     ls = line.split()
    #     cnt += 1
    #     avg += eval(ls[2])
    # print("平均的温度值是：{:.2f}".format(avg/cnt))
    f.close()
except:
    print("文件打开错误")