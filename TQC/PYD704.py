'''
1. 題目說明:
請開啟PYD704.py檔案，依下列題意進行作答，將整數儲存至集合（set）中並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA704.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。

3. 輸入輸出：
輸入說明
輸入n個整數至集合，直至-9999結束輸入

輸出說明
集合的長度
集合中的最大值
集合中的最小值
集合內的整數總和

輸入輸出範例
範例輸入
34
-23
29
7
0
-1
-9999
範例輸出
Length: 6
Max: 34
Min: -23
Sum: 46
'''

num = set()
while True:
    inp = eval(input())
    if inp == -9999:
        break
    num.add(inp)

print("Length:", len(num))
print("Max:", max(num))
print("Min:",min(num))
print("Sum:", sum(num))