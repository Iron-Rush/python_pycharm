# TestMap.py
# ls = ["123", "333", "999"]
ls = "123,7777,211"
detals = []
# map(fun, x)   将函数Fun的功能，逐一作用于第二个参数的每一个元素
detals.append(list(map(eval, ls.split(","))))
print(detals[0][0])