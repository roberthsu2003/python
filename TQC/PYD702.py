'''
1. 題目說明:
請開啟PYD702.py檔案，依下列題意進行作答，將兩數組合併並進行排序，使輸出值符合題意要求。作答完成請另存新檔為PYA702.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

3. 輸入輸出：
輸入說明
兩個數組，直至-9999結束輸入

輸出說明
排序前的數組
排序後的串列

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
'''
tup1 = ()
tup2 = ()
print("Create tuple1:")
while True:
    num = eval(input())
    if num == -9999:
        break
    tup1 += (num,)

print("Create tuple2:")
while True:
    num = eval(input())
    if num == -9999:
        break
    tup2 += (num,)

tup_comb = tup1 + tup2
print("Combined tuple before sorting:", tup_comb)

lst_comb = list(tup_comb)
print("Combined list after sorting:", sorted(lst_comb))