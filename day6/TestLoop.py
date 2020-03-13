# TestLoop.py
s = 'PYTHON'
while s != '':
    for c in s:
        print(c, end='')
    s = s[:-1]


for i in "I LOVE U":
    print(i, end='')
    if i == ' ':
        print()

a = 3
while a > 0:
    a -= 1
    print(a)
    if a == 0:
        print('continue,a={}'.format(a))
        continue
        # break
else:
    print("while正常执行完毕")