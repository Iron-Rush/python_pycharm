# CalStatisticsV1.py
# 基本统计值
# 总个数：len()
# 求和：for..in
# 平均值：总和/总个数
# 方差：各数据与平均数差的平方的和的平均数
# 中位数:排序,然后...奇数则找中间1个，偶数则找中间两个取平均

# 定义函数，获取用户不定长度的输入
def getNum1():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums
def getNum2():
    nums = []
    NumStr = input("请输入数字并以'，'隔开：")
    nums = NumStr.split(',')
    return nums
# 定义求和函数
def getSum(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s
# 定义求平均数函数
def getAvg(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)
# 定义方差函数    （各数据与平均数差的平方的和的平均数）
def dev(numbers, avg):
    # print(numbers)
    # print(len(numbers))
    sdev = 0.0
    for num in numbers:
        # sdev += ((num - avg)**2)
        sdev = sdev + (num - avg) ** 2
    return pow(sdev / (len(numbers)-1), 0.5)
# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    med = 0.0
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
n = getNum1()
avg = getAvg(n)
size = len(n)
# all = sum(numbers)    #系统求和函数
all = getSum(n)         #自定义的遍历求和函数
avg = all/size          #根据和求平均
# print("平均值：{}，方差：{:.2f}，中位数：{}".format(avg,dev(n,avg),median(n)))
print("平均值：{}，方差：{:.2f}，中位数：{}".format(avg,dev(n,avg),median(n)))
# print(avg)
# print(dev(n,avg))
# print(median(n))

# print(all1 == all2)
# print(getNum2())