#! usr/bin/python3

from random import randint


if __name__ == "__main__":
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


