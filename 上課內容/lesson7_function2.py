import random
def lotGenerator():
    lot = set()
    while len(lot) != 7:
        lot.add(random.randint(1,49))
    lotList = list(lot)
    specialNum = lotList.pop()
    for item in sorted(lotList):
        print(item,end="  ")
    print()
    print(f"特別號是:{specialNum}")

if __name__ == "__main__":
    print("大樂透自動選號系統");
    print("===============");
    num = int(input("請輸入您要的組數:"))
    for i in range(num):
        print(f"第{i+1}組")
        lotGenerator()
        print()