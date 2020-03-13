#!usr/bin/python3

"""
*問題 commonfactor.py
設計一個程式，可以由鍵盤輸入兩個數值，並求出這2個數值的最大公因數和最小公倍數

顯示======================================
求兩數的最大公因數和最小公倍數
請輸入第一個整數:XXX
請輸入第二個整數:XXX

計算結果:
14 和 35 的最大公因數:7
14 和 35 的最小倍數是:70

"""

print('求兩數的最大公因數和最小公倍數')
n = int(input('請輸入第一個整數:'))
m = int(input('請輸入第二個整數:'))

if(n>m):
    max = n
    min = m
else:
    max = m
    min = n

for num in range(min):
    num += 1
    if((min % num) == 0 and (max % num) == 0):
        maxResult = num

minResult = (n / maxResult) * (m / maxResult) * maxResult

print('{0:d}和{1:d}的最大公因數:{2:d}'.format(n,m,maxResult))
print('{0:d}和{1:d}的最小公倍數:{2:.0f}'.format(n,m,minResult))


