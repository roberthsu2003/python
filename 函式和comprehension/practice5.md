# Python 課堂練習設計

## 今日教學重點

list 的綜合表達式

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
# 原始學生分數資料
students_scores = [("小明", 55), ("小華", 85), ("小美", 92), ("小白", 48), ("小綠", 60)]

passed_students = [f"{name}: {score}分" for name, score in students_scores if score >= 60]

# 結果: ['小華: 85分', '小美: 92分', '小綠: 60分']
```

## 使用的 Python 技術

例如:

- list
- tuple
- list comprehension
- for
- if
- f-string
- 變數指定
- 條件篩選

## 學習目標

學生可以學會:

- 使用 list comprehension 從原本的 list 產生新的 list
- 在 list comprehension 中使用 `for` 取出 tuple 裡的資料
- 在 list comprehension 中加入 `if` 條件來篩選資料

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

某間書店有一份書籍價格資料,每一筆資料包含「書名」和「價格」。

請使用 list comprehension,找出價格小於等於 300 元的書籍,並產生新的清單。新清單中的每個項目格式為:

```python
"書名: 價格元"
```

## 與課堂範例的對應

- 沿用的語法/概念:list comprehension、tuple 拆解、f-string、`for` 迴圈、`if` 條件篩選
- 換掉的部分:從「學生分數是否及格」改成「書籍價格是否小於等於 300 元」

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
# 原始書籍價格資料
books_prices = [("Python 入門", 450), ("漫畫學英文", 280), ("資料科學基礎", 520), ("故事寫作課", 300), ("時間管理", 199)]

# 請完成:使用 list comprehension 找出價格小於等於 300 元的書籍
cheap_books = [
    # 請完成
]

print(cheap_books)

# 預期結果:
# ['漫畫學英文: 280元', '故事寫作課: 300元', '時間管理: 199元']
```

學生需要完成:

1. 從 `books_prices` 中取出每一本書的書名與價格
2. 使用 `if` 判斷價格是否小於等於 300
3. 用 f-string 組合出 `"書名: 價格元"` 的文字格式

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
# 原始書籍價格資料
books_prices = [("Python 入門", 450), ("漫畫學英文", 280), ("資料科學基礎", 520), ("故事寫作課", 300), ("時間管理", 199)]

# 使用 list comprehension 找出價格小於等於 300 元的書籍
cheap_books = [
    f"{book}: {price}元" for book, price in books_prices if price <= 300
]

print(cheap_books)

# 預期結果:
# ['漫畫學英文: 280元', '故事寫作課: 300元', '時間管理: 199元']
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:建立一個書籍價格清單,每筆資料包含書名和價格


# 步驟 2:使用 list comprehension 產生新的清單


# 步驟 3:在 list comprehension 中取出每一本書的書名和價格


# 步驟 4:只保留價格小於等於 300 元的書籍


# 步驟 5:把每筆符合條件的資料轉成「書名: 價格元」的文字格式


# 步驟 6:印出最後產生的新清單
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:建立一個書籍價格清單,每筆資料包含書名和價格
books_prices = [("Python 入門", 450), ("漫畫學英文", 280), ("資料科學基礎", 520), ("故事寫作課", 300), ("時間管理", 199)]

# 步驟 2:使用 list comprehension 產生新的清單
cheap_books = [

# 步驟 3:在 list comprehension 中取出每一本書的書名和價格
    f"{book}: {price}元" for book, price in books_prices

# 步驟 4:只保留價格小於等於 300 元的書籍
    if price <= 300
]

# 步驟 5:把每筆符合條件的資料轉成「書名: 價格元」的文字格式
# 已在 list comprehension 的 f-string 中完成

# 步驟 6:印出最後產生的新清單
print(cheap_books)
```

---

# 延伸挑戰題

## 題目

書店現在想找出「價格大於等於 300 元」的書籍,並在輸出文字中加上「高價書」標記。

請使用 list comprehension 產生新的清單,格式如下:

```python
"書名: 價格元，高價書"
```

## 提示

可以思考:

- `if price >= 300` 應該放在 list comprehension 的哪個位置?
- f-string 裡可以同時放入書名、價格和固定文字嗎?
- 條件如果改成 `>` 或 `>=`,結果會有什麼不同?

---

# 思考問題

1. 為什麼 `for book, price in books_prices` 可以一次取出書名和價格?
2. 如果把 `if price <= 300` 拿掉,產生的新清單會有什麼變化?
3. 這題如果不用 list comprehension,改用一般 `for` 迴圈加上 `append()`,程式會怎麼寫?

---

# 建議查詢方向

學生可以搜尋:

1. Python list comprehension 用法
2. Python tuple unpacking 拆解資料
3. Python f-string 格式化文字

