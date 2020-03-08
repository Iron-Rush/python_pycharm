#飞雪连天射白鹿，笑书神侠倚碧鸳

fnames = {"飞狐外传", "雪山飞狐", "万古天帝3", "万古天帝4", "万古天帝5", "万古天帝6"}
def PrintHighFreWords(fname):
    text = open(fname, "r", encoding="gbk").read()
    d = {}; cnt = 0; rst = ""
    for w in text:
        # cnt += 1
        d[w] = d.get(w, 0) + 1
    for w in "，。“” ：？\n:":
        try:
            del d[w]
        except:
            pass
    ls = list(d.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        # print(ls[i])
        word, count = ls[i]
        rst += word
    print(rst)
    return rst

text = PrintHighFreWords("雪山飞狐" + ".txt")
A = set(text.split("\n")[-1])
for fname in fnames:
    txt = PrintHighFreWords(fname + ".txt")
    A &= set(txt.split("\n")[-1])
print(A)
