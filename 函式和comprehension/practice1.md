# Python 課堂練習設計

## 今日教學重點

function 可以簡單化邏輯思考的複雜度

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
import random

def play_game():
    """負責執行單次猜數字遊戲的函式"""
    min_val = 1
    max_val = 100
    count = 0
    target = random.randint(1, 100)
    print("===============猜數字遊戲=================:\n")
    
    while True:
        count += 1
        keyin = int(input("猜數字範圍{0}~{1}: ".format(min_val, max_val)))
        if keyin >= min_val and keyin <= max_val:
            if keyin == target:
                print("賓果!猜對了, 答案是:", target)
                print("您猜了", count, "次")
                break
            elif keyin > target:
                max_val = keyin
                print("再小一點")
            elif keyin < target:
                min_val = keyin
                print("再大一點")
            print("您猜了", count, "次\n")
        else:
            print("請輸入提示範圍內的數字")

while True:
    play_game()
    play_again = input("是否要再玩一次？(y/n): ")
    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break
```

## 使用的 Python 技術

例如:

- import random
- randint()
- input()
- int()
- print()
- variable
- if / elif / else
- while 迴圈
- break
- function
- function 呼叫
- 字串的 `.format()`
- 字串的 `.lower()`

## 學習目標

學生可以學會:

- 將「一輪遊戲流程」包裝成 function，讓主程式更簡潔。
- 使用 while 迴圈控制單次遊戲與是否繼續遊玩。
- 使用 if 判斷處理不同輸入結果，並根據結果改變變數內容。

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個「心算加法小遊戲」。

每一局遊戲會隨機產生兩個 1 到 50 之間的整數，請使用者輸入這兩個數字相加的答案。如果答對，就顯示答對訊息與嘗試次數，結束這一局；如果答錯，就提示「答案太大」或「答案太小」，讓使用者繼續猜同一題。

請將「單次加法遊戲」寫成 `play_addition_game()` 函式。主程式只負責詢問使用者是否要再玩一次。

## 與課堂範例的對應

- 沿用的語法/概念:random、input、int、print、變數、if 判斷、while True、break、function、主程式呼叫 function、是否繼續遊玩
- 換掉的部分:原本是猜 1 到 100 的隨機數字，改成猜兩個隨機數字相加後的答案

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
import random

def play_addition_game():
    """負責執行單次心算加法遊戲的函式"""
    count = 0

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    # 請完成:計算正確答案，存入 answer 變數
    

    print("===============心算加法小遊戲=================\n")

    while True:
        count += 1

        # 請完成:請使用者輸入 num1 + num2 的答案，並轉成整數
        

        # 請完成:判斷使用者答案是否正確
        if ____________________:
            print("答對了!")
            print("正確答案是:", answer)
            print("您回答了", count, "次")
            break

        # 請完成:如果使用者輸入的答案比正確答案大
        elif ____________________:
            print("答案太大")

        # 請完成:如果使用者輸入的答案比正確答案小
        elif ____________________:
            print("答案太小")

        print("您回答了", count, "次\n")


# 主程式流程：只負責控制「是否繼續遊玩」
while True:
    # 請完成:呼叫函式，開始一局新遊戲
    

    play_again = input("是否要再玩一次？(y/n): ")

    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break
```

學生需要完成:

1. 在 function 裡計算兩個隨機數字相加後的正確答案。
2. 在 while 迴圈中讀取使用者輸入，並用 if / elif 判斷答案大小。
3. 在主程式中呼叫 `play_addition_game()`，讓遊戲可以開始執行。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
import random

def play_addition_game():
    """負責執行單次心算加法遊戲的函式"""
    count = 0

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    answer = num1 + num2

    print("===============心算加法小遊戲=================\n")

    while True:
        count += 1

        keyin = int(input("{0} + {1} = ".format(num1, num2)))

        if keyin == answer:
            print("答對了!")
            print("正確答案是:", answer)
            print("您回答了", count, "次")
            break

        elif keyin > answer:
            print("答案太大")

        elif keyin < answer:
            print("答案太小")

        print("您回答了", count, "次\n")


# 主程式流程：只負責控制「是否繼續遊玩」
while True:
    play_addition_game()

    play_again = input("是否要再玩一次？(y/n): ")

    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 匯入 random 模組


# 定義 play_addition_game 函式，負責執行一局心算加法遊戲


# 在函式中建立 count 變數，記錄使用者回答了幾次


# 隨機產生第一個 1 到 50 之間的整數


# 隨機產生第二個 1 到 50 之間的整數


# 將兩個隨機數字相加，得到正確答案


# 印出遊戲標題


# 使用 while True 建立一局遊戲中的重複回答流程


# 每回答一次，就讓 count 增加 1


# 顯示加法題目，請使用者輸入答案，並轉成整數


# 如果使用者輸入的答案等於正確答案


# 印出答對訊息、正確答案與回答次數


# 使用 break 結束這一局遊戲


# 如果使用者輸入的答案大於正確答案，印出「答案太大」


# 如果使用者輸入的答案小於正確答案，印出「答案太小」


# 每次答錯後，印出目前回答次數


# 在主程式中使用 while True，控制是否繼續玩下一局


# 呼叫 play_addition_game 函式，開始一局新遊戲


# 詢問使用者是否要再玩一次


# 如果使用者輸入的不是 y，就印出結束訊息並離開迴圈
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 匯入 random 模組
import random


# 定義 play_addition_game 函式，負責執行一局心算加法遊戲
def play_addition_game():

    # 在函式中建立 count 變數，記錄使用者回答了幾次
    count = 0

    # 隨機產生第一個 1 到 50 之間的整數
    num1 = random.randint(1, 50)

    # 隨機產生第二個 1 到 50 之間的整數
    num2 = random.randint(1, 50)

    # 將兩個隨機數字相加，得到正確答案
    answer = num1 + num2

    # 印出遊戲標題
    print("===============心算加法小遊戲=================\n")

    # 使用 while True 建立一局遊戲中的重複回答流程
    while True:

        # 每回答一次，就讓 count 增加 1
        count += 1

        # 顯示加法題目，請使用者輸入答案，並轉成整數
        keyin = int(input("{0} + {1} = ".format(num1, num2)))

        # 如果使用者輸入的答案等於正確答案
        if keyin == answer:

            # 印出答對訊息、正確答案與回答次數
            print("答對了!")
            print("正確答案是:", answer)
            print("您回答了", count, "次")

            # 使用 break 結束這一局遊戲
            break

        # 如果使用者輸入的答案大於正確答案，印出「答案太大」
        elif keyin > answer:
            print("答案太大")

        # 如果使用者輸入的答案小於正確答案，印出「答案太小」
        elif keyin < answer:
            print("答案太小")

        # 每次答錯後，印出目前回答次數
        print("您回答了", count, "次\n")


# 在主程式中使用 while True，控制是否繼續玩下一局
while True:

    # 呼叫 play_addition_game 函式，開始一局新遊戲
    play_addition_game()

    # 詢問使用者是否要再玩一次
    play_again = input("是否要再玩一次？(y/n): ")

    # 如果使用者輸入的不是 y，就印出結束訊息並離開迴圈
    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break
```

---

# 延伸挑戰題

## 題目

請將心算小遊戲改成「加減法混合挑戰」。

每一局隨機產生兩個 1 到 50 的整數，再隨機決定這一題要做加法或減法。請使用 function 負責執行一局遊戲，主程式一樣只控制是否繼續遊玩。

## 提示

可以思考:

- 如何用 `random.randint()` 決定這一題是加法還是減法?
- 如果是加法，正確答案要怎麼算? 如果是減法，正確答案要怎麼算?
- 顯示題目時，如何讓畫面出現 `+` 或 `-`?

---

# 思考問題

1. 為什麼把「一局遊戲」寫成 function 之後，主程式會變得比較簡單?
2. 如果把 `count = 0` 寫在 function 外面，玩第二局時可能會發生什麼問題?
3. 這個程式中的 `break` 是結束哪一個迴圈? 會不會直接結束整個程式?

---

# 建議查詢方向

學生可以搜尋:

1. Python random.randint 用法
2. Python function 定義與呼叫
3. Python while True break 用法

