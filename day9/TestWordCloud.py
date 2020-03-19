# TestWordCloud.py
#from scipy.misc import imread
# from scipy.misc import imread
import wordcloud
w = wordcloud.WordCloud()
w.width = 800
w.height = 500
# w.generate("Python and WordCloud")
# w.generate("Python Python")
w.font_path = "msyhl.ttc"
w.generate("蕾宝宝 小可爱 懒蛋蛋 小可爱")
w.background_color = 'white'
w.to_file("outFile1.png")
