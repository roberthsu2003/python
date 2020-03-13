#!usr/bin/python3
'''
#問題 min.py
#試使用陣列配合for迴圈，找尋陣列中最小值的程式，程式執行時會要求將輸入數值的數量，輸入完畢會顯示所輸入數值中的最小值
#=====================================================================
請輸入數值:4
請輸入第1數值:4
請輸入第2數值:5
請輸入第3數值:6
請輸入第4數值:7
4 | 5 | 6 | 7 | 最小值是:4
#=====================================================================
'''

if __name__ == '__main__':
    integers = list()
    nums = int(input("請輸入數值:"))
    for i in range(nums):
        inputNum = int(input('請輸入第{:d}數值:'.format(i+1)))
        integers.append(inputNum)

    integers.sort()

    for item in integers:
        print(item,end=" | ")

    print("最小值是:",integers[0])

