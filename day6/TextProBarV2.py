# TextProBarV2.py
import time
for i in range(101):
    # \r打印前先回到行首 end=''打印结束后不去换行
    print("\r{:3}#".format(i), end="")
    time.sleep(0.1)