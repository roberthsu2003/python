#!usr/bin/python3.8

'''
# Name        : bubble.py
#任由使用者輸入任意個數的數值序列,程式會將此數值序列由小到大和由大到小排序後顯示
#============================================================

請輸入要排序的數值個數:5
請輸入第1個數值:45
請輸入第2個數值:78
請輸入第3個數值:24
請輸入第4個數值:69
請輸入第5個數值:91
排序前
45.0 78.0 24.0 69.0 91.0
由小到大排序後:
24.0 45.0 69.0 78.0 91.0
由大到小排序後:
91.0 78.0 69.0 45.0 24.0 
#============================================================
'''

if __name__ == '__main__':
    nums = int(input('請輸入要排序的數值個數:'))
    integers = list()
    for i in range(nums):
        inputNum = float(input('請輸入第{:d}個數值:'.format(i+1)))
        integers.append(inputNum)

    print("排序前")
    for i in integers:
        print(i, end=' ')
    print()
    print('由小到大排序後:')
    for i in sorted(integers):
        print(i, end=' ')
    print()
    print('由大到小排序後:')
    for i in sorted(integers,reverse=True):
        print(i, end=' ')
    print()