#!usr/bin/python3

'''
#continue.py
#請設計一個程式，讓使用者輸入數值，只有加總正偶數值，不加總正奇數值，如果輸入負數，結束程式。

顯示:========================================
請輸入第1個數值:456
請輸入第2個數值:455
請輸入第3個數值:123
請輸入第4個數值:-1
所有輸入的正偶數的加總是:xxxxxxx
=============================================

'''

num = 0
sum = 0
while(True):
    num += 1
    inputNum = int(input("請輸入第"+ str(num) + "個數值:"))
    if(inputNum < 0):
        break
    elif (inputNum % 2 == 1):
        continue
    else:
        sum += inputNum
print("所有輸入的正偶數的加總是:", sum)

