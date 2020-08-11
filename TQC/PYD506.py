'''1. 題目說明:
請開啟PYD506.py檔案，依下列題意進行作答，依使用者輸入的數字作為參數傳遞進行公式計算，使輸出值符合題意要求。作答完成請另存新檔為PYA506.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式  
a
x
2
+
b
x
+
c
=
0
  的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

提示：輸出有順序性

3. 輸入輸出：
輸入說明
三個整數，分別為a、b、c

輸出說明
代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】

輸入輸出範例
範例輸入1
2
-3
1
範例輸出1
1.0, 0.5
範例輸入2
9
9
8
範例輸出2
Your equation has no root.

'''

def compute(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        res1 = (-b + delta**0.5) / (2 * a)
        res2 = (-b - delta**0.5) / (2 * a)
        return str(res1) + ", " + str(res2)

a = eval(input())
b = eval(input())
c = eval(input())

result = compute(a, b, c)
if result == None:
    print("Your equation has no root.")
else:
    print(result)