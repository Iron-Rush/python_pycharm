# DefStudy.py
def fact(n, m = 1): #m为可选参数，必须放在必选参数后
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m
def fact2(n, *b):   #*b为可变参数，不确定数目
    global ls       #声明为全局变量
    ls = ['f', 'F', '!']
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s
out = fact(5, 5)            #调用fact函数，按参数顺序传入两个参数
out1 = fact(n = 5, m = 5)   #调用fact函数，
out2 = fact(5)

print("out={},out1={},out2={}".format(out,out1,out2))
out3 = fact2(10, 3, 2)
print(out3)
print(ls)