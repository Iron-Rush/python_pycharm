numbs = input()
length = len(numbs)
rst = ""
i = 0
d = {"1":"一","2":"二","3":"三","4":"四","5":"五","6":"六","7":"七","8":"八","9":"九","0":"零"}
while (i < length):
    rst += d[numbs[i]]
    i += 1
    print("rst = {}".format(rst))
print(rst)