# 自訂的function
import random

def big_lot():
    lot = set()

    while (len(lot) < 7):
        lot.add(random.randint(1, 49))
    lot_list = list(lot)
    specialNum = lot_list.pop()

    for item in lot_list:
        print(item, end=' ')
    print(f'特別號:{specialNum}')
    print("============")

if __name__ == '__main__':
    group = int(input('請輸入大樂透電腦選號組數:'))
    for _ in range(group):
        a = 5
        big_lot()

print(a)
