# ReadpyFile.py
def getTxt():
    tf = open("HelloWorld.py", "r", encoding="utf-8")
    txt = tf.read()
    tf.close()
    return txt
t = getTxt()
eval(t)
# print(eval(getTxt()))