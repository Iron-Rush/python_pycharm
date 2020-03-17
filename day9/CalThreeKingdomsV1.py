# CalThreeKingdomsV1.py
import jieba
# 三国演义高频词分析
def getTxt():
    txt = open("Threekingdoms.txt", "r", encoding="utf-8").read()
    return txt
kingdomsTxt = getTxt()
words = jieba.lcut(kingdomsTxt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>15}".format(word, count))
# print(getTxt()[0:20])