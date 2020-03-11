# 打印十二个星组图标
x = 9800
for i in range(12):
    print(chr(x + i),end=' | ')
print()
str = "python"
# strout = str.center(20,"-")
strout = str.center(20)
print(strout)
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))