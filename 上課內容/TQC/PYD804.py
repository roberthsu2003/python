'''
1. 題目說明:
請開啟PYD804.py檔案，依下列題意進行作答，將字串轉換成大寫及首字大寫，使輸出值符合題意要求。作答完成請另存新檔為PYA804.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
全部大寫
每個字的第一個字母大寫

輸入輸出範例
範例輸入
learning python is funny
範例輸出
LEARNING PYTHON IS FUNNY
Learning Python Is Funny
'''
st = input()

str1 = st.upper()
print(str1)

str2 = st.title()
print(str2)
