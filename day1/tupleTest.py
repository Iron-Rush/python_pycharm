# 元组类型 元组一旦创建，不可被修改 但可增加新的部分
t1 = ()
print(t1) #()

# 一个元素的tuple定义时必须加一个逗号，
t2 = (1,)
print(t2) #(1,)
t3 = (1,3,5,6)
print(t3) #(1, 3, 5, 6)

# 计算元组元素个数
print(len(t3))

print(t3[2:]) #(5, 6)
print(t3[0:3:2]) #(1, 5)

print(max(t3))
print(min(t3))

t4=(1,2,3,[4,5])
t4[3][0] = 7
t4[3][1] = 8
print(t4) #(1, 2, 3, [7, 8])

# tuple不可变，但可以增加新的部分
t1 = t2 + t3
print(t1) #(1, 1, 3, 5, 6)

# 将列表转换为元组
l = [1,2,3]
print(tuple(l)) #(1, 2, 3)