try:
    # f = open('D:/Work/PythonWorkspace/untitled/day2/log.txt', 'r')
    f = open('log.txt', 'r')#打开文件
    # print(f.readline())
    # print(f.read())
    avg, cnt = 0, 0#变量初始化，avg为温度累计，cnt为条数累计
    for line in f:
        ls = line.split()
        cnt += 1#统计日志条数
        avg += eval(ls[2])#去引号，转化为数字，累计温度总和
    print("平均的温度值是：{:.2f}".format(avg/cnt))
    f.close()#关闭文件
except:
    print("文件打开错误")