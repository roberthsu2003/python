import random
def one_set_lot():
    lots = set()

    while(len(lots) < 7):
        lots.add(random.randint(1,49))

    lotsList = list(lots)
    special = lotsList.pop()

    for item in lotsList:
        print(item,end=' ')

    print(f"特別號:{special}")

nums = eval(input("請輸入電腦選號的組數:"))

for i in range(nums):
    print(f"第{i+1}組:")
    one_set_lot()
    print("=========")

