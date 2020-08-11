'''
1. 題目說明:
請開啟PYD808.py檔案，依下列題意進行作答，進行社會安全碼格式檢查，使輸出值符合題意要求。作答完成請另存新檔為PYA808.py再進行評分。

2. 設計說明：
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。

3. 輸入輸出：
輸入說明
一個字串（格式為ddd-dd-dddd，d表示數字）

輸出說明
判斷是否符合SSN格式

輸入輸出範例
範例輸入1
329-48-4977
範例輸出1
Valid SSN
範例輸入2
837-a3-3000
範例輸出2
Invalid SSN
'''

s = input()

isSSN = (len(s) == 11)
if isSSN:
    for i in range(len(s)):
        if i ==3 or i==6:
            if s[i] != '-':
                isSSN = False
                break
        elif not s[i].isdigit():
            isSSN = False
            break

if isSSN:
    print("Valid SSN")
else:
    print("Invalid SSN")