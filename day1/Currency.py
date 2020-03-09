money = input() + "1"
if (money[0:3] == "RMB"):
    USD = eval(money[3:-1])/6.78
    print("USD{:.2f}".format(USD))
else:
    RMB = eval(money[3:-1])*6.78
    print("RMB{:.2f}".format(RMB))