#!/usr/bin/python3
'''
試使用陣列配合for迴圈，找尋陣列中最小值的程式，程式執行時會要求將輸入數值的數量，輸入完畢會顯示所輸入數值中的最小值
'''

if __name__ == "__main__":
    integers = []
    nums = int(input("請輸入數值的數量:"))
    for i in range(nums):
        inputNum = int(input(f'請輸入第{i+1}數值:'))
        integers.append(inputNum)

    integers.sort()

    print(f"最小值是{integers[0]}")

