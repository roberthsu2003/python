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
        lot.add(random.randint(1,49))
    print('本期大樂透電腦選號號碼如下:')
    for item in lot:
        print(item, end=' ')
    print('\n')

    lotList = list(lot)
    print('特別號:',lotList.pop())
