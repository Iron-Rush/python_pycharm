# CalHamletV1.py
def getText():
    txt = open("Hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!@#$%^&*()_+{}\'|:"<>?,./;[]\\_-+=~`':
        txt = txt.replace(ch, "")
    return txt

hamletTxt = getText()
# d = dict()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())    #将字典元素放到列表中
# print(items[1])
# lambda函数，传入的x为键值对的元组，通过x[1]，返回元组中的值
# reverse默认为False升序，True为降序
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))  #单词居左，槽宽为10；计数居右，槽宽为5
# for w in hamletTxt:
#     d[w] = d.get(w, 0) + 1
# print(len(d))
# print(d)