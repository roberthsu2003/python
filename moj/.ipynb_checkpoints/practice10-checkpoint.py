import random
min_val = 1
max_val = 100
count = 0
target = random.randint(1, 100)
print("===============猜數字遊戲================:\n")
while(True):
    count += 1
    keyin = int(input(f"猜數字範圍{min_val}~{max_val}: "))
    if(keyin >= min_val and keyin <= max_val):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了", count, "次")
            break
        elif (keyin > target):
            max_val = keyin-1
            print("再小一點")
        elif (keyin < target):
            min_val = keyin + 1
            print("再大一點")
        print("您猜了", count, "次\n")
    else:
        print("請輸入提示範圍內的數字")