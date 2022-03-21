#內建的module(模組)和package(套件)
import random

def getWeek():
    return random.choice(["星期一","星期二","星期三","星期四","星期五","星期六","星期日"])

print(getWeek)
print(getWeek())
