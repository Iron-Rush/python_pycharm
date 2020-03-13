# PrintScore.py
score = eval(input("请输入成绩："))
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'c'
elif score >= 60:
    grade = 'D'
else:
    grade = '不及格'
print(grade)