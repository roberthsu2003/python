'''
1. 題目說明:
請開啟PYD608.py檔案，依下列題意進行作答，建立3*3矩陣並輸出矩陣最大值與最小值的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA608.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

輸入輸出範例
範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
'''

size = 3
mat = []
for i in range(size):
    mat.append([])
    for j in range(size):
        mat[i].append(eval(input()))

max_num = min_num = mat[0][0]
max_index = min_index = [0, 0]

for i in range(size):
    for j in range(size):
        if mat[i][j] > max_num:
            max_num = mat[i][j]
            max_index = [i, j]
        elif mat[i][j] < min_num:
            min_num = mat[i][j]
            min_index = [i, j]

print("Index of the largest number %d is:(%d, %d)" % (max_num, max_index[0],max_index[1]))

print("Index of the smallest number %d is:(%d, %d)" % (min_num, min_index[0],min_index[1]))