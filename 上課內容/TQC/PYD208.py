'''
1. 題目說明:
請開啟PYD208.py檔案，依下列題意進行作答，依輸入值進行進位轉換，使輸出值符合題意要求。作答完成請另存新檔為PYA208.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。

提示：轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。

3. 輸入輸出：
輸入說明
一個數值

輸出說明
將此數值轉換成十六進位值

輸入輸出範例
範例輸入1
13
範例輸出1
D
範例輸入2
8
範例輸出2
8
'''

num = int(input())

if 0<= num <=9:
    hex_num = num
elif num == 10:
    hex_num = 'A'
elif num == 11:
    hex_num = 'B'
elif num == 12:
    hex_num = 'C'
elif num == 13:
    hex_num = 'D'
elif num == 14:
    hex_num = 'E'
elif num == 15:
    hex_num = 'F'

print(hex_num)