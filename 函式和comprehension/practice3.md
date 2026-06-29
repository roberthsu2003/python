# Python 課堂練習設計

## 今日教學重點

function 的早期回傳（Early Return）

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
# 範例（對應題號 10: get_grade）：根據分數回傳等級 A~F
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(get_grade(85))  # 輸出: B
print(get_grade(105)) # 輸出: Invalid Score
```

## 使用的 Python 技術

- function
- parameter
- return
- if
- 比較運算子
- 邏輯運算子 `or`
- print()

## 學習目標

學生可以學會:

- 在 function 中使用 `return` 回傳結果
- 使用 early return 先處理不合法資料
- 透過多個 `if` 判斷，依條件回傳不同結果

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個 function `get_ticket_price(age)`，根據乘客年齡回傳票價。

規則如下:

- 年齡小於 0 或大於 120，回傳 `"Invalid Age"`
- 年齡小於 6，回傳 `0`
- 年齡小於 12，回傳 `100`
- 年齡小於 65，回傳 `250`
- 其他情況，回傳 `120`

## 與課堂範例的對應

- 沿用的語法/概念:function、parameter、return、if 判斷、early return、比較運算子
- 換掉的部分:從「根據分數判斷成績等級」改成「根據年齡判斷票價」

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
def get_ticket_price(age):
    # 請完成:如果年齡小於 0 或大於 120，回傳 "Invalid Age"

    # 請完成:如果年齡小於 6，回傳 0

    if age < 12:
        return 100

    # 請完成:如果年齡小於 65，回傳 250

    return 120


print(get_ticket_price(5))    # 輸出: 0
print(get_ticket_price(10))   # 輸出: 100
print(get_ticket_price(30))   # 輸出: 250
print(get_ticket_price(80))   # 輸出: 120
print(get_ticket_price(130))  # 輸出: Invalid Age
```

學生需要完成:

1. 判斷不合法年齡並提早回傳
2. 判斷 6 歲以下票價
3. 判斷一般成人票價

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
def get_ticket_price(age):
    if age < 0 or age > 120:
        return "Invalid Age"

    if age < 6:
        return 0

    if age < 12:
        return 100

    if age < 65:
        return 250

    return 120


print(get_ticket_price(5))    # 輸出: 0
print(get_ticket_price(10))   # 輸出: 100
print(get_ticket_price(30))   # 輸出: 250
print(get_ticket_price(80))   # 輸出: 120
print(get_ticket_price(130))  # 輸出: Invalid Age
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 定義一個 function，名稱為 get_ticket_price，參數為 age

# 如果 age 小於 0 或 age 大於 120，回傳 "Invalid Age"

# 如果 age 小於 6，回傳 0

# 如果 age 小於 12，回傳 100

# 如果 age 小於 65，回傳 250

# 其他情況回傳 120

# 呼叫 get_ticket_price(5)，並印出結果

# 呼叫 get_ticket_price(10)，並印出結果

# 呼叫 get_ticket_price(30)，並印出結果

# 呼叫 get_ticket_price(80)，並印出結果

# 呼叫 get_ticket_price(130)，並印出結果
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 定義一個 function，名稱為 get_ticket_price，參數為 age
def get_ticket_price(age):
    # 如果 age 小於 0 或 age 大於 120，回傳 "Invalid Age"
    if age < 0 or age > 120:
        return "Invalid Age"

    # 如果 age 小於 6，回傳 0
    if age < 6:
        return 0

    # 如果 age 小於 12，回傳 100
    if age < 12:
        return 100

    # 如果 age 小於 65，回傳 250
    if age < 65:
        return 250

    # 其他情況回傳 120
    return 120


# 呼叫 get_ticket_price(5)，並印出結果
print(get_ticket_price(5))

# 呼叫 get_ticket_price(10)，並印出結果
print(get_ticket_price(10))

# 呼叫 get_ticket_price(30)，並印出結果
print(get_ticket_price(30))

# 呼叫 get_ticket_price(80)，並印出結果
print(get_ticket_price(80))

# 呼叫 get_ticket_price(130)，並印出結果
print(get_ticket_price(130))
```

---

# 延伸挑戰題

## 題目

請設計 `get_ticket_type(age)`，除了判斷票價，也要回傳票種名稱。

例如:

- 不合法年齡回傳 `"Invalid Age"`
- 6 歲以下回傳 `"Free Ticket"`
- 6 到 11 歲回傳 `"Child Ticket"`
- 12 到 64 歲回傳 `"Adult Ticket"`
- 65 歲以上回傳 `"Senior Ticket"`

## 提示

可以思考:

- 哪一個條件應該最先判斷?
- 每個 `return` 執行後，function 還會不會繼續往下跑?
- 條件順序改變後，結果會不會不同?

---

# 思考問題

1. 為什麼要先判斷 `age < 0 or age > 120`，而不是最後才判斷?
2. 如果 `if age < 6:` 改成 `if age <= 6:`，哪些年齡的結果會改變?
3. 這題沒有使用 `elif`，只用多個 `if`，為什麼仍然可以得到正確結果?

---

# 建議查詢方向

學生可以搜尋:

1. Python function return 用法
2. Python if 判斷條件順序
3. Python early return 範例

---

