# Python 課堂練習設計

## 今日教學重點

帶有參數和傳回值的 function

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
# 範例二（對應題號 5: calculate_bmi）：傳入身高（公尺）與體重（公斤），回傳 BMI
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

my_bmi = calculate_bmi(1.75, 70)
print(f"計算出的 BMI 為: {my_bmi:.2f}")
```

## 使用的 Python 技術

- function
- function 參數
- return 傳回值
- 變數
- 數學運算
- 呼叫 function
- print()
- f-string 格式化輸出

## 學習目標

學生可以學會:

- 定義一個帶有參數的 function
- 在 function 裡面進行計算並使用 `return` 回傳結果
- 呼叫 function，接收回傳值，並印出結果

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請設計一個 function `calculate_total_price(unit_price, quantity)`，傳入商品單價與購買數量，計算並回傳商品總價。

例如:一個商品單價是 120 元，購買 3 個，總價就是 360 元。最後請呼叫這個 function，並印出計算出的總價。

## 與課堂範例的對應

- 沿用的語法/概念:定義 function、傳入兩個參數、在 function 中進行數學運算、使用 `return` 回傳結果、呼叫 function、用 `print()` 輸出結果
- 換掉的部分:原本是計算 BMI，現在改成計算商品總價

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
# 定義 function:傳入商品單價與數量，回傳總價
def calculate_total_price(unit_price, quantity):
    # 請完成:計算商品總價
    total_price =

    # 請完成:回傳商品總價


# 呼叫 function，計算單價 120 元、數量 3 個的總價
my_total = calculate_total_price(120, 3)

# 請完成:印出計算出的總價
print()
```

學生需要完成:

1. 在 function 裡面計算 `unit_price * quantity`
2. 使用 `return` 回傳計算結果
3. 使用 `print()` 印出總價

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
# 定義 function:傳入商品單價與數量，回傳總價
def calculate_total_price(unit_price, quantity):
    # 請完成:計算商品總價
    total_price = unit_price * quantity

    # 請完成:回傳商品總價
    return total_price


# 呼叫 function，計算單價 120 元、數量 3 個的總價
my_total = calculate_total_price(120, 3)

# 請完成:印出計算出的總價
print(f"商品總價為: {my_total} 元")
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
# 步驟 1:定義一個 function，名稱為 calculate_total_price，參數有 unit_price 和 quantity


# 步驟 2:在 function 裡面，計算商品總價，公式是單價乘以數量


# 步驟 3:使用 return 回傳商品總價


# 步驟 4:呼叫 function，傳入單價 120 與數量 3，並把回傳值存入變數 my_total


# 步驟 5:使用 print() 印出商品總價
```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
# 步驟 1:定義一個 function，名稱為 calculate_total_price，參數有 unit_price 和 quantity
def calculate_total_price(unit_price, quantity):

    # 步驟 2:在 function 裡面，計算商品總價，公式是單價乘以數量
    total_price = unit_price * quantity

    # 步驟 3:使用 return 回傳商品總價
    return total_price


# 步驟 4:呼叫 function，傳入單價 120 與數量 3，並把回傳值存入變數 my_total
my_total = calculate_total_price(120, 3)

# 步驟 5:使用 print() 印出商品總價
print(f"商品總價為: {my_total} 元")
```

---

# 延伸挑戰題

## 題目

請再設計一個 function `calculate_discount_price(total_price, discount)`，傳入原本總價與折扣數，回傳打折後的價格。

例如:總價是 1000 元，折扣數是 0.8，表示打八折，最後價格是 800 元。

## 提示

可以思考:

- function 可以傳入不同的數字進行計算
- 折扣後價格可以用 `total_price * discount`
- 回傳值可以再用變數接起來，再用 `print()` 印出

---

# 思考問題

1. 為什麼 function 裡面要使用 `return`，而不是只在 function 裡面 `print()`？
2. 如果呼叫 `calculate_total_price(200, 5)`，程式會回傳什麼結果？
3. 如果把 `return total_price` 刪掉，`my_total` 會得到什麼？

---

# 建議查詢方向

學生可以搜尋:

1. Python function return 用法
2. Python function 參數範例
3. Python f-string 輸出變數

