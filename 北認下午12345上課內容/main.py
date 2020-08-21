import random

min = 1
max = 100
count = 0
target = random.randint(min,max)
print("=============猜數字遊戲==================\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍{0:d}~{1:d}:".format(min,max)))
    if keyin >= min and keyin <= max:
        if(keyin == target):
            print("賓果!猜對了, 答案是:%d" % target)
            print("妳猜了%d次" % count)
            break
        elif(keyin > target):
            max = keyin
            print("再小一點")
        elif(keyin < target):
            min = keyin
            print("再大一點")
        print("您猜了%d次\n" % count)
    else:
        print("請輸入提示範圍內的數字")