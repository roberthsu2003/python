'''
1. 題目說明:
請開啟PYD408.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA408.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
偶數的個數
奇數的個數

輸入輸出範例
範例輸入
69
48
19
91
83
22
18
37
82
40
範例輸出
Even numbers: 5
Odd numbers: 5
'''

even = odd = 0

for i in range(10):
    a = int(input())
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers", odd)