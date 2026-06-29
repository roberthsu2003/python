# Python 課堂練習設計

## 今日教學重點

while 迴圈的應用和小遊戲

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
import random

min = 1
max = 100
count = 0
target = random.randint(1, 100)

print("===============猜數字遊戲=================:\n")

while(True):
    count += 1
    keyin = int(input("猜數字範圍{0}~{1}: ".format(min, max)))
    if(keyin >= min and keyin <= max):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了", count, "次")
            break
        elif(keyin > target):
            max = keyin
            print("再小一點")
        elif(keyin < target):
            min = keyin
            print("再大一點")
        print("您猜了", count, "次\n")
    else:
        print("請輸入提示範圍內的數字")
```

## 使用的 Python 技術

例如:

- `import random`
- `random.randint()`
- `input()`
- `int()`
- 變數
- `while` 迴圈
- `if / elif / else` 判斷
- `break`
- 計數器變數
- 範圍檢查

## 學習目標

學生可以學會:

- 使用 `while` 迴圈讓遊戲重複進行
- 使用 `if / elif / else` 判斷遊戲結果
- 使用變數記錄次數、分數或遊戲狀態

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個「剪刀石頭布連勝挑戰」小遊戲。

玩家每一回合輸入:

- `1` 代表剪刀
- `2` 代表石頭
- `3` 代表布

電腦會隨機出拳。程式要判斷玩家是勝利、失敗或平手。玩家只要累積贏 `3` 次，遊戲就結束，並顯示總共玩了幾回合。

如果玩家輸入的數字不是 `1~3`，要提示「請輸入 1~3」，而且該次不計入回合數。

## 與課堂範例的對應

- 沿用的語法/概念: `random.randint()`、`while` 迴圈、`input()`、`int()`、`if / elif / else`、計數器、`break`
- 換掉的部分: 原本是猜數字範圍提示，這次改成剪刀石頭布的回合制小遊戲

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
import random

win_count = 0
round_count = 0

print("===============剪刀石頭布連勝挑戰=================")
print("1:剪刀  2:石頭  3:布")
print("先贏 3 次就過關!\n")

while True:
    keyin = int(input("請出拳(1剪刀 2石頭 3布): "))

    if keyin >= 1 and keyin <= 3:
        # 請完成: 回合數加 1

        computer = random.randint(1, 3)

        print("玩家出拳:", keyin)
        print("電腦出拳:", computer)

        if keyin == computer:
            print("平手")
        elif (keyin == 1 and computer == 3) or (keyin == 2 and computer == 1) or (keyin == 3 and computer == 2):
            print("你贏了這一回合")
            # 請完成: 勝利次數加 1
        else:
            print("你輸了這一回合")

        print("目前勝利次數:", win_count)
        print("目前回合數:", round_count, "\n")

        # 請完成: 如果勝利次數達到 3 次,印出過關訊息並結束迴圈

    else:
        print("請輸入 1~3\n")
```

學生需要完成:

1. 每次有效出拳時，讓回合數加 `1`
2. 玩家贏的時候，讓勝利次數加 `1`
3. 勝利次數達到 `3` 次時，用 `break` 結束遊戲

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
import random

win_count = 0
round_count = 0

print("===============剪刀石頭布連勝挑戰=================")
print("1:剪刀  2:石頭  3:布")
print("先贏 3 次就過關!\n")

while True:
    keyin = int(input("請出拳(1剪刀 2石頭 3布): "))

    if keyin >= 1 and keyin <= 3:
        round_count += 1

        computer = random.randint(1, 3)

        print("玩家出拳:", keyin)
        print("電腦出拳:", computer)

        if keyin == computer:
            print("平手")
        elif (keyin == 1 and computer == 3) or (keyin == 2 and computer == 1) or (keyin == 3 and computer == 2):
            print("你贏了這一回合")
            win_count += 1
        else:
            print("你輸了這一回合")

        print("目前勝利次數:", win_count)
        print("目前回合數:", round_count, "\n")

        if win_count == 3:
            print("恭喜過關!你總共玩了", round_count, "回合")
            break

    else:
        print("請輸入 1~3\n")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:匯入 random 模組


# 步驟 2:建立變數 win_count,用來記錄玩家贏了幾次


# 步驟 3:建立變數 round_count,用來記錄總共玩了幾回合


# 步驟 4:印出遊戲標題與出拳規則


# 步驟 5:使用 while True 讓遊戲可以一直進行


# 步驟 6:請玩家輸入 1、2 或 3,並轉成整數


# 步驟 7:判斷玩家輸入是否在 1~3 之間


# 步驟 8:如果輸入正確,回合數加 1


# 步驟 9:讓電腦隨機產生 1~3 的出拳


# 步驟 10:印出玩家與電腦的出拳結果


# 步驟 11:如果玩家和電腦出拳相同,印出平手


# 步驟 12:如果玩家獲勝,印出勝利訊息,並讓 win_count 加 1


# 步驟 13:如果不是平手也不是勝利,代表玩家輸了


# 步驟 14:印出目前勝利次數與目前回合數


# 步驟 15:如果玩家已經贏 3 次,印出過關訊息,並用 break 結束迴圈


# 步驟 16:如果玩家輸入不是 1~3,印出錯誤提示
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:匯入 random 模組
import random

# 步驟 2:建立變數 win_count,用來記錄玩家贏了幾次
win_count = 0

# 步驟 3:建立變數 round_count,用來記錄總共玩了幾回合
round_count = 0

# 步驟 4:印出遊戲標題與出拳規則
print("===============剪刀石頭布連勝挑戰=================")
print("1:剪刀  2:石頭  3:布")
print("先贏 3 次就過關!\n")

# 步驟 5:使用 while True 讓遊戲可以一直進行
while True:

    # 步驟 6:請玩家輸入 1、2 或 3,並轉成整數
    keyin = int(input("請出拳(1剪刀 2石頭 3布): "))

    # 步驟 7:判斷玩家輸入是否在 1~3 之間
    if keyin >= 1 and keyin <= 3:

        # 步驟 8:如果輸入正確,回合數加 1
        round_count += 1

        # 步驟 9:讓電腦隨機產生 1~3 的出拳
        computer = random.randint(1, 3)

        # 步驟 10:印出玩家與電腦的出拳結果
        print("玩家出拳:", keyin)
        print("電腦出拳:", computer)

        # 步驟 11:如果玩家和電腦出拳相同,印出平手
        if keyin == computer:
            print("平手")

        # 步驟 12:如果玩家獲勝,印出勝利訊息,並讓 win_count 加 1
        elif (keyin == 1 and computer == 3) or (keyin == 2 and computer == 1) or (keyin == 3 and computer == 2):
            print("你贏了這一回合")
            win_count += 1

        # 步驟 13:如果不是平手也不是勝利,代表玩家輸了
        else:
            print("你輸了這一回合")

        # 步驟 14:印出目前勝利次數與目前回合數
        print("目前勝利次數:", win_count)
        print("目前回合數:", round_count, "\n")

        # 步驟 15:如果玩家已經贏 3 次,印出過關訊息,並用 break 結束迴圈
        if win_count == 3:
            print("恭喜過關!你總共玩了", round_count, "回合")
            break

    # 步驟 16:如果玩家輸入不是 1~3,印出錯誤提示
    else:
        print("請輸入 1~3\n")
```

---

# 延伸挑戰題

## 題目

請改成「三戰兩勝剪刀石頭布」。

玩家和電腦各自累積勝利次數，誰先贏 `2` 次，遊戲就結束。最後要印出玩家勝利、電腦勝利，或目前比分。

## 提示

可以思考:

- 是否需要增加 `computer_win_count` 變數?
- 平手時要不要計入回合數?
- 判斷遊戲結束時，是檢查玩家勝利次數，還是電腦勝利次數?

---

# 思考問題

1. 為什麼輸入錯誤時，不應該讓 `round_count` 加 `1`?
2. 如果把 `break` 拿掉，玩家贏 3 次後程式會發生什麼事?
3. 判斷玩家獲勝的條件有三種，能不能用不同寫法讓程式更好讀?

---

# 建議查詢方向

學生可以搜尋:

1. Python `while True` 和 `break` 用法
2. Python `random.randint()` 隨機整數
3. Python `and`、`or` 多條件判斷

