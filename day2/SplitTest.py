f = open('log.txt', 'r')
str = f.readline()
# str = '2020年3月6日 13:40:47 1 2 3 4 5'
ls = str.split()
print(ls[0])