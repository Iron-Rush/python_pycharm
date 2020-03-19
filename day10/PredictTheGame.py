# PredictTheGame.py
# 获取程序运行参数
from random import random

def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(用0到1之间的小数表示)")
# 获取程序运行参数proA,proB,n
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1)："))
    b = eval(input("请输入选手B的能力值(0-1)："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n
# 打印程序运行结果
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，胜率：{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，胜率：{:0.1%}".format(winsB, winsB/n))
# 模拟N场比赛
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        #调用模拟一次比赛函数，分别获得本次比赛双方得分
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        elif scoreA < scoreB:
            winsB += 1
        else:
            i += 1
    return winsA, winsB
# 模拟一场比赛
def simOneGame(proA, proB):
    scoreA, scoreB = 0, 0
    # 默认选手A开始发球
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < proA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < proB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB
# 模拟一局比赛
def gameOver(scoreA, scoreB):
    over = False
    # A/B谁先达到15分，谁获胜，本局比赛结束
    if (scoreA == 15) or (scoreB == 15):
        over = True
    return over

# 主函数
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()