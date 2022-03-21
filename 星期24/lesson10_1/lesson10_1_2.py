#內建的module(模組)和package(套件)
import random
import random as rd
from random import choice,randint
#from random import choice as ci
#from random import *

def getWeek():
    return choice(["星期一","星期二","星期三","星期四","星期五","星期六","星期日"])

if __name__ == "__main__":
    print(getWeek())
