# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
min = 1
max = 99
count = 0
target = random.randint(1,max+1)
print("===========猜數字遊戲==================:\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍%d~%d" % (min, max)))
    if keyin == target:
        print("賓果!猜對了,答案是:", target)
        print("您猜了%d次" % count)
        break;
    elif keyin > target:
        max = keyin
        print("再小一點")
    elif keyin < target:
        min = keyin
        print("再大一點")
    
    print("您猜了", count ,"次\n")

