'''
1. 題目說明:
請開啟PYD202.py檔案，依下列題意進行作答，判斷輸入值是否為3或5的倍數，使輸出值符合題意要求。作答完成請另存新檔為PYA202.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】或【x is a multiple of 5.】；若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為3或者是5的倍數

輸入輸出範例
範例輸入1
55
範例輸出1
55 is a multiple of 5.
範例輸入2
36
範例輸出2
36 is a multiple of 3.
範例輸入3
92
範例輸出3
92 is not a multiple of 3 or 5.
範例輸入4
15
範例輸出4
15 is a multiple of 3 and 5.
'''

a = int(input())
if (a%3 == 0) and (a%5 == 0):
    print("%d is a multiple of 3 and 5." % a)
elif a%3 == 0:
    print("%d is a multiple of 3." % a)
elif a%5 == 0:
    print("%d is a multiple of 5." % a)
else:
    print("%d is not a multiple of 3 or 5." % a)