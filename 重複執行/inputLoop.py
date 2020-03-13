#!usr/bin/python3

"""
*問題 inputLoop.py
#設計一個程式，使用者輸入一個M, 再輸入另一個數N,然後程式可以求出M*1 + M*2 + M*3 + M*4 + M*5....... + M*N的值

顯示==========================
輸入M:5
輸入N:4
M*1 + M*2 + M*3 + ......+ M*N = 50
"""

m = int(input('輸入M:'))
n = int(input('輸入N:'))
sum = 0
for num in range(n):
    num += 1
    if num != n:
        print(m,'*',num,' + ',end='')
    else:
        print(m,'*',num,' = ',end='')

    sum += m * num

print(sum)