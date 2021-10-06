import random
min = 1
max = 100
count = 0
target = random.randint(1,100)
print("===============猜數字遊戲==================\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍"+str(min)+"~"+str(max)+":"))
    if(keyin >= min and keyin <= max):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了",count,"次")
            break
        elif(keyin > target):
            print("再小一點")
            max = keyin - 1
        elif(keyin < target):
            print("再大一點")
            min = keyin + 1
        print("您已經猜了", count, "次")
    else:
        print("請輸入提示範圍內的數字")

print("game over")