# TestOS.py
import os.path
# OS学习
print(os.path.abspath("PredictTheGame.py"))
print(os.path.normpath("PredictTheGame.py"))
pathA= os.path.abspath("PredictTheGame.py")
pathB = os.path.normpath(pathA)
print(pathA.count("\\"))
print(pathB)
print(os.path.dirname("PredictTheGame.py"))
print("当前系统的cpu数量:{}".format(os.cpu_count()))