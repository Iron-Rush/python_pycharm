# DayDayUpQ1
# 天天向上的力量，每天进步0.1%
dayup = pow(1.001, 365) #0.001的365次方
# 天天退步的力量，每天退步0.1%
daydown = pow(0.999, 365)#0.999的365次方
print("向上的力量：{:.2f}，向下的力量：{:.2f}".format(dayup, daydown))