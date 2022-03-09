#大樂透電腦選號
import random


def lotGenerator():
    lot = set()
    while (len(lot) < 7):
        lot.add(random.randint(1, 49))
    lot_list = list(lot)
    special = lot_list.pop()
    for item in lot_list:
        print(item, end=' ')
    print(f'特別號:{special}')


if __name__ == "__main__":
    print("========大樂透電腦選號==============")
    groups = int(input("請問需要幾組號碼:"))
    for _ in range(groups):
        lotGenerator()