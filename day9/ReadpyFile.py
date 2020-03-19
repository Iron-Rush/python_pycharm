# ReadpyFile.py
def getTxt():
    tf = open("HelloWorld.py", "r+", encoding="utf-8")
    txt = tf.read()
    ls = ['\n#\t', '中国', '美国', '英国']
    tf.writelines(ls)
    tf.close()
    return txt
print(getTxt())
# t = getTxt()
# eval(t)
# print(eval(getTxt()))