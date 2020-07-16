'''
1. 題目說明:
請開啟PYD05.py檔案，依下列題意進行作答，計算兩個正整數的最大公因數，使輸出值符合題意要求。作答完成請另存新檔為PYA508.py再進行評分。。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

3. 輸入輸出：
輸入說明
兩個正整數（以半形逗號分隔）

x,y

輸出說明
最大公因數

輸入輸出範例
範例輸入1
12,8
範例輸出1
4
範例輸入2
4,6
範例輸出2
2
'''

def compute(a, b):
    gcd = 1
    k = 1

    if a > 0 and b > 0:
        while k <= a and k <=b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return gcd
    
x, y = eval(input())
gcd = compute(x,y)
print(gcd)