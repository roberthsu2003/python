'''
1. 題目說明:
請開啟PYD610.py檔案，依下列題意進行作答，依輸入值計算四週的平均溫度及最高、最低溫度，使輸出值符合題意要求。作答完成請另存新檔為PYA610.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

3. 輸入輸出：
輸入說明
四週各三天的溫度

輸出說明
平均溫度
最高溫度
最低溫度

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
下圖中的 粉紅色點 為 空格

'''

num_week = 4
num_day = 3
temp = []

for i in range(num_week):
    temp.append([])
    print("Week %d:" % (i+1))
    for j in range(num_day):
        temp[i].append(eval(input("Day %d:" % (j+1))))

comb = []
for i in range(num_week):
    comb.extend(temp[i])

avg = sum(comb) / (num_week * num_day)
print("Average:%.2f" % avg)
print("Highest:", max(comb))
print("Lowest:", min(comb))