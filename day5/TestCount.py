#不确定尾数，不是bug
print(0.1 + 0.2) #0.30000000000000004

z = 1.2 - 4 + 5.6 + 89j#复数
print(z)
print(z.real)#实部
print(z.imag)#虚部
print(int(z.real))
print(float("123")+1)
# 整数除
print(10//3)

powout = pow(3,pow(3,99),10000)
print(powout)
print(round(10.1066, 2))

l1 = {1,9,11,25,-1,100}
print(min(l1))
d1 = {}
for i in range(6):
    d1[i] = d1.get(i, 0) + 1
print(d1)
print(min(d1))