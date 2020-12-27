#!usr/bin/python3.8
'''
#============================================================================
# Name        : biglottery.py
#撰寫一個大樂透電腦自動選號程式，程式執行會以亂數的方式顯示1-49之間七個不重複的大樂透號碼。

#============================================================

本期大樂透電腦選號號碼如下:

2 28 8 42 49 20 15

特別號:15

'''

import random

if __name__ == '__main__':
     lot = set()
    while(len(lot) <= 7):
        rValue = randint(1, 49)
        lot.add(rValue)
    print('本期大樂透電腦選號號碼如下:')

    lotList = list(lot)
    specialNum = lotList.pop()
    for item in lotList:
        print(item, end=' ')

    print('特別號:%d' % specialNum )
