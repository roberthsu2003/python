'''
1. 題目說明:
請開啟PYD406.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA406.py再進行評分。

2. 設計說明：
請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義（State）。假t表所示：

BMI值	代表意義
BMI < 18.5	under weight
18.5 <= BMI < 25	normal
25.0 <= BMI < 30	over weight
30 <= BMI	fat
提示： 
B
M
I
=
體
重
(
k
g
)
/
身
高
2
(
m
)
 ，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。

3. 輸入輸出：
輸入說明
兩個正數（身高cm、體重kg），直至-9999結束輸入

輸出說明
輸出BMI值
BMI值代表意義

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
176
80
BMI: 25.83
State: over weight
170
100
BMI: 34.60
State: fat
-9999

'''
state = ""
height = eval(input())
while height != -9999:
    weight = eval(input())
    bmi = weight / (height / 100 * height /100)
    if weight == -9999:
        break
    elif bmi >= 30:
        state = "fat"
    elif bmi >= 25 and bmi < 29.9:
        state = "over weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        state = "normal"
    elif bmi < 18.5:
        state = "under weight"
    print("BMI:%.2f" % bmi)
    print("State:%s" % state)

    height = eval(input())