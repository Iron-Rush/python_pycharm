# Recursive.py
# n! n的阶乘，递归求法
def fact(n):
    if n == 0:      #n=0为基例，停止递归，返回1
        return 1
    else:
        return n * fact(n-1)    #递归，继续求解

# 字符串反转递归求法
def rvs(s):
    if s == '':     #若s为空，返回s本身
        return s
    else:           #对s初首字符之外进行反转，并将首字符拼接至末尾
        return rvs(s[1:]) + s[0]

# 斐波那契数列    1、1、2、3、5、8、13、21、34、…
# F(n) = F(n-1) + F(n-2)
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
out = fact(5)
print(out)
strIn = "你好啊~"
strOut = rvs(strIn)
print(strOut)
print(f(10))