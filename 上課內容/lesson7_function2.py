import random
lot = set()
while len(lot) != 7:
    lot.add(random.randint(1,49))

print("本期大樂透電腦選號號碼如下:")
lotList = list(lot)
specialNum = lotList.pop()
for item in sorted(lotList):
    print(item,end="  ")
print()
print(f"特別號是:{specialNum}")