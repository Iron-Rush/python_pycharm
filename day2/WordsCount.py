#jieba是优秀的中文分词第三方库
#对中文文本进行分词操作，产生包含词语的列表
#jieba是第三方库，需要额外安装

# import jieba  #import方法一，简单库名
# from jieba import lcut  #import方法二，混合命名
import jieba as jb  #import方法三，复杂库名起别名
f = open("万古天帝第一章.txt","r",encoding="gbk")  #打开目标文本文件
text = f.read()  #读取文件中的文本，保存至text中
f.close()  #关闭文件
#中文分词,分词后保存至列表中
# ls = jieba.lcut(text)  #调用方法一
# ls = lcut(text)   #调用方法二
ls = jb.lcut(text)  #调用方法三
d = {}  #初始化字典d
for w in ls: #遍历列表d
    d[w] = d.get(w, 0) + 1 #将词语设为键，对其对应的值进行累加
for k in d:  #遍历字典d，输出频次高与标准的词语
    if d[k] >= 10 and k != "\n":
        print('"{}"出现{}次'.format(k, d[k]))