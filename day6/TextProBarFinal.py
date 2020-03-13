# TextProBarFinal.py
import time
scale = 50
print("执行开始".center(scale//2,"—"))
start = time.perf_counter()
for i in range(scale + 1):
    done = '*' * i
    undone = '.' * (scale - i)
    process = (i/scale) * 100
    # process = i/scale
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(process,done,undone,dur), end='')
    # print("\r{:^3.0%}[{}->{}]{:.2f}s".format(process, done, undone, dur), end='')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale//2, '—'))