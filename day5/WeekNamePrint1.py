# WeekNamePrint1
weeks = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入周几："))
pos = (weekId - 1) * 3
print(weeks[pos:pos+3])