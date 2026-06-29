# Python 課堂練習設計

## 今日教學重點

while 迴圈整合 `continue`、`break`

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
# break
# continue
# 請設計一個程式，讓使用者輸入數值，只有加總正偶數值，不加總正奇數值，如果輸入負數，結束程式。
sum = 0
num = 0
while True:    
    input_value = int(input(f"請輸入第{num+1}個數值: "))
    if input_value < 0:
        break
    num += 1
    if input_value % 2 == 1:
        continue    
    sum += input_value    
    
print(f"輸入的次數是{num}，所有輸入的正偶數的加總是:{sum}")
```

## 使用的 Python 技術

- `input()`
- `int()`
- 變數
- `while True`
- `if` 判斷
- `break`
- `continue`
- `%` 取餘數
- 累加運算

## 學習目標

學生可以學會:

- 使用 `while True` 建立不確定次數的重複輸入
- 使用 `break` 在指定條件下結束迴圈
- 使用 `continue` 跳過不需要處理的資料
- 在迴圈中統計輸入次數與累加符合條件的資料

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個「回收瓶數統計程式」。

讓使用者不斷輸入每一批回收的寶特瓶數量。  
如果輸入負數，代表今日統計結束。  
每一批輸入的非負數都要算作一次輸入。  
但是只有「偶數瓶」的批次會直接列入回收總數；如果輸入的是「奇數瓶」，代表需要人工複查，這一批先不加入總數。

最後輸出今天輸入了幾批資料，以及已確認可計算的偶數瓶總數。

## 與課堂範例的對應

- 沿用的語法/概念:`while True`、`input()`、`int()`、`if`、`break`、`continue`、`%`、累加
- 換掉的部分:原本是單純輸入數值並加總正偶數；新題目改成回收瓶數統計，奇數瓶代表需人工複查，不列入總數

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
total_bottles = 0
count = 0

while True:
    bottles = int(input(f"請輸入第{count + 1}批回收瓶數: "))

    # 請完成:如果 bottles 小於 0，就結束迴圈

    count += 1

    # 請完成:如果 bottles 是奇數，就跳過這一次迴圈

    # 請完成:把偶數瓶數加到 total_bottles

print(f"今天共輸入{count}批資料，已確認的偶數瓶總數是:{total_bottles}")
```

學生需要完成:

1. 判斷輸入負數時使用 `break` 結束迴圈
2. 判斷奇數瓶時使用 `continue` 跳過累加
3. 將符合條件的偶數瓶數加到總數中

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
total_bottles = 0
count = 0

while True:
    bottles = int(input(f"請輸入第{count + 1}批回收瓶數: "))

    if bottles < 0:
        break

    count += 1

    if bottles % 2 == 1:
        continue

    total_bottles += bottles

print(f"今天共輸入{count}批資料，已確認的偶數瓶總數是:{total_bottles}")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 建立變數 total_bottles，用來記錄已確認的偶數瓶總數

# 建立變數 count，用來記錄已輸入的批次數

# 使用 while True 建立可以重複輸入的迴圈

    # 讓使用者輸入第 count + 1 批回收瓶數，並轉換成整數

    # 如果輸入的瓶數小於 0，代表統計結束，離開迴圈

    # 將輸入批次 count 加 1

    # 如果輸入的瓶數是奇數，代表需要人工複查，跳過這一次迴圈

    # 將偶數瓶數加到 total_bottles 中

# 輸出今天共輸入幾批資料，以及已確認的偶數瓶總數
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 建立變數 total_bottles，用來記錄已確認的偶數瓶總數
total_bottles = 0

# 建立變數 count，用來記錄已輸入的批次數
count = 0

# 使用 while True 建立可以重複輸入的迴圈
while True:

    # 讓使用者輸入第 count + 1 批回收瓶數，並轉換成整數
    bottles = int(input(f"請輸入第{count + 1}批回收瓶數: "))

    # 如果輸入的瓶數小於 0，代表統計結束，離開迴圈
    if bottles < 0:
        break

    # 將輸入批次 count 加 1
    count += 1

    # 如果輸入的瓶數是奇數，代表需要人工複查，跳過這一次迴圈
    if bottles % 2 == 1:
        continue

    # 將偶數瓶數加到 total_bottles 中
    total_bottles += bottles

# 輸出今天共輸入幾批資料，以及已確認的偶數瓶總數
print(f"今天共輸入{count}批資料，已確認的偶數瓶總數是:{total_bottles}")
```

---

# 延伸挑戰題

## 題目

請修改回收瓶數統計程式，增加「有效批次數」統計。

程式最後要輸出:

- 總共輸入幾批非負數資料
- 有幾批是偶數瓶，可直接列入統計
- 偶數瓶總數是多少

## 提示

可以思考:

- 需要新增哪一個變數來記錄有效批次數?
- 這個變數應該放在 `continue` 前面還是後面累加?
- 如果輸入奇數瓶，哪些統計資料應該增加，哪些不應該增加?

---

# 思考問題

1. 為什麼判斷 `bottles < 0` 要放在 `count += 1` 前面?
2. 如果把 `continue` 拿掉，奇數瓶的資料會不會被加進總數?為什麼?
3. 如果把 `total_bottles += bottles` 放在奇數判斷之前，程式結果會發生什麼變化?

---

# 建議查詢方向

學生可以搜尋:

1. Python while True 用法
2. Python break continue 差異
3. Python % 取餘數 判斷奇數偶數

