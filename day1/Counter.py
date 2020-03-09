inputStr = input()
outNum = eval(inputStr)#评估函数 eval()去掉最外层引号，执行内部语句

# ls = inputStr.split(' ')
# while '' in ls:
#     ls.remove('')
print("{:.2f}".format(outNum))