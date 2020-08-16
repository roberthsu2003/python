'''
輸入顧客購買金額，若金額在
- 100000元打8折
- 50000打85折
- 30000打9折
- 10000打95折
'''
money = int(input('請輸入購買金額:'))
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
print('實付金額是:', payMoney,'元')