# (1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#
# (2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指华氏度87.65度；
TempStr = input()

length = len(TempStr)
if (TempStr[0]) in ('C','c'):
    F = (eval(TempStr[1:length])*1.8)+32
    print("F{:.2f}".format(F))
    TempStr += "1"
    F = (eval(TempStr[1:-1])*1.8)+32
    print("F{:.2f}".format(F))
else:
    C = (eval(TempStr[1:length])-32)/1.8
    print("C{:.2f}".format(C))
    TempStr += "1"
    C = (eval(TempStr[1:-1])-32)/1.8
    print("C{:.2f}".format(C))