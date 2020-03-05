l = [1,2,4,5,9,9,11]
# 序列元素的下标从0开始
# tuple元素不可赋值
# 基本样式[下限:上限:步长]
print(l[1])
# 2
print(l[0:3:2])
# [1, 4]
print(l)
# [1, 2, 4, 5, 9, 9, 11]

# list元素是可以改变的
l[1] = 100
print(l)
# [1, 100, 4, 5, 9, 9, 11]

# insert在list指定位置插入项目
l.insert(1,"新来的")
print(l)
# [1, '新来的', 100, 4, 5, 9, 9, 11]

# append在List末尾添加一个项目
l.append("排队队")
print(l)
# [1, '新来的', 100, 4, 5, 9, 9, 11, '排队队']

# pop移除给定位置的项目
l.pop(5)
print(l)
# [1, '新来的', 100, 4, 5, 9, 11, '排队队']

# pop()移除最后的项目
l.pop()
print(l)
# [1, '新来的', 100, 4, 5, 9, 11]

# 删除指定的项目，不是项目位置 (从前往后，只删一个)
l.remove("新来的")
print(l)
# [1, 100, 4, 5, 9, 11]

# 倒序排序
l.reverse()
print(l)
# [11, 9, 5, 4, 100, 1]

# 降序排序
l.sort(reverse=True)
print(l)
#[1, 100, 4, 5, 9, 11]

# 升序排序
l.sort(reverse=False)
print(l)
# [1, 4, 5, 9, 11, 100]

print(max(l))
print(min(l))
print(len(l))