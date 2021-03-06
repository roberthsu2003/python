'''
1. 題目說明:
請開啟PYD402.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA402.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

3. 輸入輸出：
輸入說明
n個數值，直至9999結束輸入

輸出說明
n個數值中的最小值

輸入輸出範例
範例輸入
29
100
948
377
-28
0
-388
9999
範例輸出
-388
'''

num = eval(input())
min_num = num

while num != 9999:
    num = eval(input())
    if num < min_num:
        min_num = num

print(min_num)