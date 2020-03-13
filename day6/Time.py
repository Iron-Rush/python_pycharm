import time
def wait(t):
    time.sleep(t)

print(time.time())# 获取系统时间的时间戳，浮点格式
# 1583940690.1049292
print(time.ctime())# 最易读的字符串格式时间
# Wed Mar 11 23:31:30 2020
print(time.gmtime())# 计算机可处理的时间格式，struct_time
# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=11, tm_hour=15, tm_min=31, tm_sec=30, tm_wday=2, tm_yday=71, tm_isdst=0)

print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))

start = time.perf_counter()
wait(5)
# for i in range(200):
#     x = 1 + 1
end = time.perf_counter()
print("start:{},end:{},时间为：{}".format(start, end, end-start))