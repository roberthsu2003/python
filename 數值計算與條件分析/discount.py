#!usr/bin/python3

'''
請使用者輸入一個任意數，程式會顯示此數的平方值及立方值
'''
money = int(input("請輸入購買金額:"))
if money >= 100000:
    payMoney = money * 0.8
elif money >= 50000:
    payMoney = money * 0.85
elif money >= 30000:
    payMoney = money * 0.9
elif money >= 10000:
    payMoney = money * 0.95
else:
    payMoney = money

print('實付金額是:', payMoney, '元')
