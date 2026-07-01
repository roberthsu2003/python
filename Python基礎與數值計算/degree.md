## 教學重點

import 內建 module(以 `math` 模組為例,搭配 `input()`、型別轉換與 `print()`)

---

# 課堂範例回顧(學生剛才已練習)

## 原始程式

```python
#!usr/bin/python3
'''
讓使用者輸入直角三角形的對邊與斜邊,
利用 sin(x) = 對邊 / 斜邊 計算夾角,
再把弧度(radian)轉換成角度(degree)印出。
'''
import math
opposite = float(input('請輸入直角三角形的對邊長度:'))
hypotenuse = float(input('請輸入直角三角形的斜邊長度:'))
radian = math.asin(opposite / hypotenuse)
degree = math.degrees(radian)
print('夾角的弧度:', radian, '弧度')
print('夾角的角度:', degree, '度')
```

## 使用的 Python 技術

- `import`(匯入內建 module)
- `math.asin()`、`math.degrees()`(呼叫模組函式)
- `input()`
- `float()` 型別轉換
- variable(變數)
- `print()`

## 學習目標

學生可以學會:

- 用 `import` 匯入 Python 內建 module 並呼叫裡面的函式
- 從 module 文件查到適合的函式名稱與用法
- 把使用者輸入轉成數字、運算後輸出結果

---

# 本次練習題目(全新題目,與課堂範例不同)

> 說明:以下是針對相同教學重點設計的「新題目」,情境與資料和課堂範例不同,但用到的 Python 語法一致。

## 題目敘述

請寫一支程式,讓使用者輸入一個圓的**半徑**,利用 `math` 模組計算並印出這個圓的**圓周長**與**面積**。

- 圓周長公式:`2 × π × 半徑`
- 圓面積公式:`π × 半徑²`

其中圓周率 π 不要自己打 3.14,而是改用 `math.pi`;平方的部分請用 `math.pow()` 或 `**` 計算。最後把圓周長與面積分別印出來。

## 與課堂範例的對應

- 沿用的語法/概念:`import math`、呼叫 module 內的成員(`math.pi`、`math.pow`)、`input()`、`float()` 型別轉換、變數、`print()`
- 換掉的部分:情境從「三角函數求角度」換成「圓的周長與面積」;module 成員從 `asin`、`degrees` 換成 `pi`、`pow`;由「函式」改用「常數 `math.pi`」,讓學生認識 module 裡不只有函式,也有常數

---

# 學生練習:半成品

以下兩種版本皆針對「本次練習題目」,教師可依學生程度選用。

## 版本 A:程式碼半成品(挖空補完)

適合剛接觸本主題的學生:程式架構已給,補完標示處即可。

### 任務說明

請完成以下程式中標示 `# 請完成` 的部分。

```python
#!usr/bin/python3
'''
讓使用者輸入圓的半徑,
利用 math 模組計算圓周長與圓面積並印出。
'''
# 請完成:匯入需要的內建 module


# 讀取使用者輸入的半徑,並轉成 float
radius = float(input('請輸入圓的半徑:'))

# 請完成:用 math.pi 計算圓周長(2 × π × 半徑)
circumference = 

# 請完成:用 math.pi 與平方計算圓面積(π × 半徑²)
area = 

print('圓周長:', circumference)
print('圓面積:', area)
```

學生需要完成:

1. 寫出 `import math` 匯入內建 module
2. 用 `math.pi` 寫出圓周長算式
3. 用 `math.pi` 搭配 `math.pow()` 或 `**` 寫出圓面積算式

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是版本 A 補完後的完整正確程式。

```python
#!usr/bin/python3
'''
讓使用者輸入圓的半徑,
利用 math 模組計算圓周長與圓面積並印出。
'''
import math

radius = float(input('請輸入圓的半徑:'))

circumference = 2 * math.pi * radius

area = math.pi * math.pow(radius, 2)

print('圓周長:', circumference)
print('圓面積:', area)
```

## 版本 B:純註解半成品(依註解寫程式)

適合已熟悉本主題、要訓練獨立寫程式的學生:只有註解,沒有程式碼,請依註解逐行寫出完整程式。

### 任務說明

請依照下方每一行註解的說明,寫出對應的 Python 程式碼。

```python
#!usr/bin/python3

# 步驟 1:匯入內建的 math module


# 步驟 2:讀取使用者輸入的圓半徑,並用 float() 轉成小數


# 步驟 3:用 math.pi 計算圓周長(2 × π × 半徑),存到變數


# 步驟 4:用 math.pi 與平方(math.pow 或 **)計算圓面積,存到變數


# 步驟 5:印出圓周長


# 步驟 6:印出圓面積

```

學生需要依序完成每個步驟的程式碼。

### 完成後參考程式碼(教師用,勿發給學生)

> 此區塊僅供教師參考核對,是依版本 B 註解逐步寫出的完整正確程式。

```python
#!usr/bin/python3

# 步驟 1:匯入內建的 math module
import math

# 步驟 2:讀取使用者輸入的圓半徑,並用 float() 轉成小數
radius = float(input('請輸入圓的半徑:'))

# 步驟 3:用 math.pi 計算圓周長(2 × π × 半徑),存到變數
circumference = 2 * math.pi * radius

# 步驟 4:用 math.pi 與平方(math.pow 或 **)計算圓面積,存到變數
area = math.pi * math.pow(radius, 2)

# 步驟 5:印出圓周長
print('圓周長:', circumference)

# 步驟 6:印出圓面積
print('圓面積:', area)
```

---

# 延伸挑戰題

## 題目

讓使用者輸入圓的半徑後,除了印出圓周長與面積,還要用 `round()` 把結果**四捨五入到小數點後 2 位**再印出;另外,改用 `math` 模組裡的另一個成員 `math.tau`(等於 2π)來計算圓周長,觀察結果是否與用 `math.pi` 計算的一樣。

## 提示

可以思考:

- `math` 模組裡除了 `pi`,還有哪些常數可以用?
- `round(數值, 2)` 的第二個參數代表什麼?
- 用 `math.tau` 算圓周長時,公式要怎麼改才正確?

---

# 思考問題

1. 為什麼建議用 `math.pi` 而不是自己打 `3.14`?這對計算結果有什麼影響?
2. 如果把程式最上面的 `import math` 刪掉,執行時會發生什麼事?錯誤訊息會告訴你什麼?
3. 計算圓面積時,用 `math.pow(radius, 2)` 和用 `radius ** 2`,兩種寫法結果一樣嗎?各有什麼優缺點?

---

# 建議查詢方向

學生可以搜尋:

1. 搜尋「Python math 模組 常用函式與常數」,看看 `math` 裡還有什麼可以用
2. 搜尋「Python math.pi 用法」,了解如何使用模組中的常數
3. 搜尋「Python round 四捨五入 小數點位數」,學會控制輸出的小數位數

