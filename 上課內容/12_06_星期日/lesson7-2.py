#! usr/bin/python3

from random import randint

#建立一組亂數樂透
def randomLot():
    lot = set()
    while (len(lot) <= 7):
        rValue = randint(1, 49)
        lot.add(rValue)
    print('本期大樂透電腦選號號碼如下:')

    lotList = list(lot)
    specialNum = lotList.pop()
    for item in lotList:
        print(item, end=' ')

    print('特別號:%d\n' % specialNum)

if __name__ == "__main__":
    count = int(input("請輸入需要的組數:"))
    for _ in range(count):
        randomLot()



