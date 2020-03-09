#飞雪连天射白鹿，笑书神侠倚碧鸳
import jieba as jb
#以列表的形式给出作品名
fnames = {"飞狐外传", "雪山飞狐", "万古天帝3", "万古天帝4", "万古天帝5", "万古天帝6"}

#高频字提取
#定义高频字读取函数，读取出现频率最高的前20的字，打印并返回字符串
def PrintHighFreWord(fname):
    text = open(fname, "r", encoding="gbk").read()#读取整篇小说至text中
    d = {}; cnt = 0; rst = ""#初始化字典d
    #利用字典d，记录text中每个字符出现的次数(键：字符；值：出现次数)
    for w in text:
        # cnt += 1
        d[w] = d.get(w, 0) + 1
    #删除字典中出现的常用字符del[字符]
    #防止文章中没有使用目标字符，导致del报错，做try-except处理
    for w in "，。“” ：？\n:":
        try:
            del d[w]
        except:
            pass
    #将字典变成二元元组的列表
    ls = list(d.items())
    #利用lambda函数排序(根据第二个元素进行排序，True为降序，False为升序)
    ls.sort(key=lambda x: x[1], reverse=True)
    # print(ls)
    # 循环，提取前二十个字组成字符串，以便返回str
    for i in range(20):
        # print(ls[i])
        word, count = ls[i]#word存储高频字，count用于存储频次
        rst += word         #拼接高频字到字符串中
    print(rst)
    return rst

# 高频词提取
def PrintHighFreWords(fname):
    text = open(fname, "r", encoding="gbk").read()
    d = {}; cnt = 0; rst = ""
    for w in jb.lcut(text):
        cnt += 1
        #如果不是词语则跳过
        if len(w) == 1:
            continue
        d[w] = d.get(w, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(50):
        word, count = ls[i]
        rst += word + ","
    print(rst)
    return rst

#高频字
text = PrintHighFreWord("雪山飞狐" + ".txt")
A = set(text.split("\n")[-1])   #set函数生成集合
#利用for循环，遍历全部作品
for fname in fnames:
    txt = PrintHighFreWord(fname + ".txt")
    A &= set(txt.split("\n")[-1])   #将前20的字符集计算交集(&=)，并输出
print(A)
#高频词
text = PrintHighFreWords("雪山飞狐" + ".txt")
#strip() 方法用于移除字符串头尾指定的字符
A = set(text.strip(",").split(","))
for fname in fnames:
    text = PrintHighFreWords(fname + ".txt")
    A &= set(text.strip(",").split(","))
print(A)