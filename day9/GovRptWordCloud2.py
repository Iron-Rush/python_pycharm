# GovRptWordCloud2.py
import jieba
import wordcloud
# from scipy.misc import imread
# import imageio
from imageio import imread
mk = imread("men.png")
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
# ls = ["猪","金牛座","70后","年收入10万以下","低风险职业","非业务员","无社保","一级城市","46-55周岁","定期险客户","疾病险客户","医疗险客户","意外险客户","传统险客户","终止客户"]
txt = " ".join(ls)
print(len(txt))
w = wordcloud.WordCloud(width=1000, height=750, background_color="white", mask=mk)
w.font_path = "msyhl.ttc"
w.max_words = 25
w.generate(txt)
w.to_file("GovRptMk2.png")