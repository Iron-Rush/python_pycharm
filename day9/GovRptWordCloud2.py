# GovRptWordCloud2.py
import jieba
import wordcloud
# from scipy.misc import imread
# import imageio
from imageio import imread
mk = imread("fivestar2.png")
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=750, background_color="white", mask=mk)
w.font_path = "msyhl.ttc"
w.max_words = 500
w.generate(txt)
w.to_file("GovRptMk.png")