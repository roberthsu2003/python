#!usr/bin/python3
'''
*問題 nestedLoop1.py
試寫出下列數字排列的程式
顯示=================================

55555
4444
333
22
1

'''

for i in range(5,0,-1):
    for j in range(i):
        print(i,end='')
    print()
