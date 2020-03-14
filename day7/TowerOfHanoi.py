# TowerOfHanoi
count = 0
# 定义汉诺塔
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}——>{}".format(1,src,dst))   #基例，将最小的圆盘搬到目标塔
        count += 1                              #搬运次数+1
    else:
        hanoi(n-1,src,mid,dst)                  #链条，将n-1从初始塔，搬到中转塔，可以借助目标塔
        print("{}:{}——>{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)                  #将n-1从中转塔搬到目标塔，可以借助初始塔

hanoi(3,"A","B","C")
print(count)