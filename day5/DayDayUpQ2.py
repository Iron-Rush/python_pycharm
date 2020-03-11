#DayDayUpQ2
# 定义每天进步、退步的变量
dayfactor = 0.005
# 每天进步一点点
dayup = pow(1 + dayfactor, 365)
# 每天退步一点点
daydown = pow(1 - dayfactor, 365)
print("每天进步的力量：{:.2f}每天退步的力量：{:.2f}".format(dayup,daydown))