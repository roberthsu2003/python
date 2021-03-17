import random

if __name__ == "__main__":
    lot = set()
    while(len(lot) <= 7):
        lot.add(random.randint(1, 49))
    print('本期大樂透電腦選號號碼如下:')
    lotList = list(lot)
    specialNum = lotList.pop()
    for item in lotList:
        print(item, end=' ')

    print(f'特別號:{specialNum}')