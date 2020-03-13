# BodyMassIndex.py
# BMI，国际上常用的衡量人梯肥胖和健康程度的重要标准，主要用于统计分析
# 定义：BMI = 体重(kg) / 身高^2(m^2)
# def BMI_International (BMI):
#     if BMI < 18.5:
#         return '偏瘦'
#     elif 18.5 <= BMI < 25:
#         return '正常'
#     elif 25 <= BMI <30:
#         return '偏胖'
#     else:
#         return '肥胖'
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]："))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
# who = BMI_International(bmi)
who1, who2 = '', ''
if bmi < 18.5:
    who1, who2 = '偏瘦', '偏瘦'
elif 18.5 <= bmi < 24:
    who1, who2 = '正常', '正常'
elif 24 <= bmi < 25:
    who1, who2 = '正常', '偏胖'
elif 25 <= bmi < 28:
    who1, who2 = '偏胖', '偏胖'
elif 28 <= bmi < 30:
    who1, who2 = '偏胖', '肥胖'
else:
    who1, who2 = '肥胖', '肥胖'
print("BMI 指标为：国际'{0}'，国内'{1}'".format(who1, who2))