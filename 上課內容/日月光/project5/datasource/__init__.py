import os
import matplotlib.pyplot as plt
import time

def getMathGraphic():
    mathPath = 'datasource/math.txt'
    #print(os.path.exists(mathPath))
    with open(mathPath) as file:
        content = file.read()
        contentList = content.split('\n')
        names = []
        scores = []
        for item in contentList:
            itemList = item.split(',')
            names.append(itemList[0])
            scores.append(int(itemList[1]))
        plt.plot(names,scores)
        now=int(time.time())
        plt.savefig(f'datasource/{now}')