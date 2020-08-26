#!usr/bin/python3.8

'''
#============================================================================
# Name        : guess.py
#猜數字遊戲

===============猜數字遊戲=================:

猜數字範圍1~100:50
再小一點
您猜了 1 次

猜數字範圍1~50:25
再大一點
您猜了 2 次

猜數字範圍25~50:34
再大一點
您猜了 3 次

猜數字範圍34~50:46
再小一點
您猜了 4 次

猜數字範圍34~46:40
賓果!猜對了, 答案是: 40
您猜了 5 次
#====================================
'''
import random
min = 1
max = 100
count = 0
target = random.randint(min, max)
print("============猜數字遊戲====================")
while(True):
    count += 1
    keyin=int(input("猜數字範圍{}~{}:".format(min, max)))
    if(keyin >= min and keyin <=max):
        if(keyin == target):
            print("賓果!猜對了,答案是:", target)
            print("您猜了%d次" % count)
            break
        elif keyin > target:
            max = keyin
            print("再小一點")
        elif keyin < target:
            min = keyin
            print("再大一點")
        print("您已經猜了%d次\n" % count)
    else:
        print("請輸入提示範圍內的數字")


