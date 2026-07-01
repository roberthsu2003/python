# Python 條件分析

程式語言可以協助我們進行資料分析與流程控制，根據不同的條件判定（成立與否），引導程式走向不同的執行路徑。

Python 的條件分析控制主要包含：
* **單一選擇** (`if`)
* **雙向選擇** (`if-else`)
* **多向選擇** (`if-elif-else`)

---

## 1. 關係運算子與布林值

在進行條件分析前，我們必須先使用**關係運算子（Relational Operators）**對資料進行比較。關係運算的結果一律為布林值（`bool`）：`True`（成立）或 `False`（不成立）。

### 關係運算子對照表
| 運算子 | 意義 | 範例 | 結果 |
| :---: | :--- | :--- | :--- |
| `<` | 小於 | `5 < 3` | `False` |
| `<=` | 小於等於 | `5 <= 5` | `True` |
| `>` | 大於 | `7 > 3` | `True` |
| `>=` | 大於等於 | `7 >= 10` | `False` |
| `==` | 等於（檢查兩邊是否相等） | `5 == 5` | `True` |
| `!=` | 不等於（檢查兩邊是否不相等）| `5 != 5` | `False` |

> **⚠️ 注意**：比較「等於」使用的是雙等號 `==`，單等號 `=` 是「指派運算子」，切勿混淆。

```python
# 互動式環境測試
x = 7
print(x == 5)  # 輸出: False
print(x == 7)  # 輸出: True
print(5 < x)   # 輸出: True
```

---

## 2. 條件控制結構

### 2.1 單一選擇 (`if`)
單一選擇用於「只有當條件成立時，才會執行特定程式區塊」的情境。如果條件不成立，則直接跳過該區塊，繼續往下執行。

#### 📌 語法結構：
```python
if 條件式:
    # 條件成立 (True) 時執行的程式碼區塊
    # 必須使用「縮排」（通常為 4 個空格）
```

#### 💡 操作範例 1
```python
# if-1.py
a = 21
if a > 18:
    print("大於 18")

print("執行結束")
```

#### 🧠 自我檢驗小測驗：
> **Q1. 請問執行以下程式碼後，最後輸出的結果是哪一個？**
> ```python
> a = 15
> if a >= 14:
>     a -= 2 
>     print(a)
> ```
> (1) 14  
> (2) 15  
> (3) 13  

---

### 2.2 雙向選擇 (`if-else`)
當條件成立時要做某件事，而條件**不成立**時要做另一件事，此時可使用 `if-else`。

#### 📌 語法結構：
```python
if 條件式:
    # 條件成立 (True) 時執行
else:
    # 條件不成立 (False) 時執行
```

#### 💡 操作範例 2：及格判定與二分法
```python
# if2.py
a = 21
if a > 18:
    print("大於 18") 
else:
    print("小於等於 18") 

print("執行結束") 
```

#### 🧠 自我檢驗小測驗：
> **Q2. 請問執行以下程式碼後，輸出的結果是什麼？**
> ```python
> a = 12
> if a != 12:
>     print("不等於 12") 
> else:
>     print("等於 12") 
> print("執行結束")
> ```
> (1) 等於 12  
> (2) 不等於 12 \n 執行結束  
> (3) 等於 12 \n 執行結束  

---

### 2.3 巢狀選擇 (Nested `if`)
當我們在一個條件判斷內部，又需要進行額外的條件判斷時，就會使用**巢狀結構**。

#### 💡 操作範例 3：動物分類
```python
# 巢狀判斷範例
furry = True 
small = True 

if furry:
    if small:
        print("它是貓!")
    else:
        print("它是熊!")
else:
    if small:
        print("它是小蜥蜴")
    else:
        print("它是人類或是沒毛的熊")
```

#### 💡 操作範例 4：數學虛數根計算
根據不同的輸入限制，計算實數根或判定為虛數。
```python
# 如果 x 不是負數，則傳回值為 x ** (1 / y)
# 如果 x 是負數而且 y 為偶數，則傳回值為 "虛數"
# 如果 x 是負數而且 y 為奇數，則傳回值為 -(-x) ** (1 / y)

x = int(input('請輸入 x: '))
y = int(input('請輸入 y: '))

if x >= 0:
    root = x ** (1 / y)
else:
    if y % 2 == 0:
        root = "虛數"
    else:
        root = -(-x) ** (1 / y)
print('root =', root)
```

---

### 2.4 多向選擇 (`if-elif-else`)
當存在多個條件分支且彼此互斥時，使用 `elif` 可以簡化過多的巢狀結構，大幅提升程式碼的可讀性。

#### 📌 語法結構：
```python
if 條件式A:
    # 條件A 成立時執行
elif 條件式B:
    # 條件A 不成立，但條件B 成立時執行
else:
    # 以上條件皆不成立時執行
```

#### 💡 重構對比：巢狀 vs. `if-elif-else`
以下是將學生分數換算成等級的程式，對比這兩種寫法：

##### ❌ 巢狀多層寫法 (可讀性差)
```python
score = int(input("請輸入分數:"))
if score >= 90:
    grade = '優'
else:
    if score >= 80:
        grade = '甲'
    else:
        if score >= 70:
            grade = '乙'
        else:
            if score >= 60:
                grade = '丙'
            else:
                grade = '丁'
```

##### ✅ `if-elif-else` 平鋪重構 (清晰易懂)
```python
score = int(input("請輸入分數:"))
if score >= 90:
    grade = '優'
elif score >= 80:
    grade = '甲'
elif score >= 70:
    grade = '乙'
elif score >= 60:
    grade = '丙'
else:
    grade = '丁'
```

#### ⚠️ 關鍵觀念：邏輯順序與範圍重疊陷阱 (Bug 分析)
在多向選擇中，**條件的判定是由上而下依序進行的**。一旦某個條件成立，後面的所有條件都會被直接跳過。因此，條件範圍有重疊時，必須注意擺放順序：

```python
# if3-2.py (❌ 錯誤的設計範例)
age = int(input("請輸入年紀? "))
if age > 12:
    print("少年")
elif age > 18:  # ⚠️ 此處永遠無法執行！因為任何大於 18 的數字，都已經在大於 12 時被攔截了
    print("青少年")
else:
    print("青年")
```
> **💡 正確寫法**：應該從小排到大，或從大排到小，例如：
> `if age > 18:` ➡️ `elif age >= 12:` ➡️ `else:`

#### 🧠 自我檢驗小測驗：
> **Q3. 請問執行以下程式碼（a = 11）後，輸出的結果是什麼？**
> ```python
> a = 11
> if a > 18:
>     print("大於 18")
> elif a > 12:
>     print("大於 12 小於等於 18")
> else:
>     print("小於等於 12")
> ```
> (1) 大於 18  
> (2) 大於 12 小於等於 18  
> (3) 小於等於 12  

---

## 3. 異常處理 (`try-except`) 與資料驗證

### 3.1 為什麼需要異常處理？
當我們使用 `input()` 取得使用者輸入並嘗試用 `int()` 或 `float()` 強制轉型時，如果使用者輸入了非數字的字元（例如 `"abc"`），程式將會引發 `ValueError` 崩潰並中斷執行。
為了防止這種情況，我們可以使用 `try-except` 語法來擷取並處理異常。

```python
# 基礎防錯範例
try:
    money = int(input("請輸入金額: "))
    print("輸入的金額為:", money)
except ValueError:
    print("輸入格式錯誤，請輸入整數數字！")
```

### 3.2 實戰：加分程序與資料範圍驗證
將異常處理與範圍限制結合。要求學生分數最高為 300 分，符合條件加分 5%，如果超過 300 則以 300 分計：

```python
try:
    score = int(input("請輸入學生分數(最高300分): "))
    if score <= 300:
        is_add = input("學生是否符合加分條件?(y/n): ")

        if is_add == "y":
            score *= 1.05
            if score > 300:
                score = 300

        print(f"學生分數是 {round(score)}")
    else:
        print("學生分數不可以大於 300 分！")
except ValueError:
    print("格式錯誤！請輸入有效的整數數值。")
```

---

## 4. 邏輯運算子 (`and`, `or`, `not`)

當我們有多個條件要合併判斷時，可以使用邏輯運算子。

### 邏輯運算子對照表
| 運算子 | 意義 | 說明 | 範例 |
| :---: | :--- | :--- | :--- |
| `and` | 且 (AND) | 左右兩個條件**都為真**時，結果才為真。 | `(5 < 8) and (3 > 5)` ➡️ `False` |
| `or`  | 或 (OR)  | 左右兩個條件**只要一個為真**，結果即為真。 | `(5 < 8) or (3 > 5)` ➡️ `True` |
| `not` | 非 (NOT) | 反轉布林值，真變假，假變真。 | `not (5 < 3)` ➡️ `True` |

### 4.1 消除巢狀的藝術
使用邏輯運算子能有效減少程式碼的縮排層級。例如，判斷國文與數學分數給予獎金：

* **巢狀判斷 (層級多) ❌**
```python
bonus = 0
if chinese == 100:
    if math == 100:
        bonus = 1000
    else:
        bonus = 500
elif math == 100:
    bonus = 500
```

* **使用邏輯運算子 (簡潔清晰) ✅**
```python
bonus = 0
if chinese == 100 and math == 100:
    bonus = 1000
elif chinese == 100 or math == 100:
    bonus = 500
```

### 4.2 實用邏輯判斷技巧

* **鏈狀比較運算**：Python 支援 `5 < x < 10` 這種數學直覺的鏈式寫法，等同於 `5 < x and x < 10`。
* **隱式布林值判定**：在 Python 中，空容器（如空列表 `[]`、空字串 `""`）在條件句中會被自動當作 `False`。

```python
some_list = []
if some_list:
    print("列表中有東西")
else:
    print("列表是空的")  # 輸出此行
```

#### 🧠 自我檢驗小測驗：
> **Q4. 請問執行以下程式碼（a = 14）後，最後會輸出什麼？**
> ```python
> # if4.py
> a = 14
> if a >= 12 and a < 18:
>     print("ok-1")
> else:
>     print("cancel-1") 
> 	
> if 12 <= a < 18:
>     print("ok-2") 
> else:
>     print("cancel-2")
> 	
> if not a > 18:
>     print("ok-3") 
> else:
>     print("cancel-3")
> ```
> (1) ok-1 \n ok-2 \n ok-3
> (2) ok-1 \n cancel-2 \n ok-3
> (3) cancel-1 \n ok-2 \n cancel-3
>
> **Q5. 請問執行以下程式碼（a = 11）後的輸出是？**
> ```python
> a = 11
> if a >= 12 or a < 18:
>     print("ok-1") 
> else:
>     print("cancel-1")
> ```
> (1) ok-1  
> (2) cancel-1  
> (3) 無任何輸出

---

## 5. 課後練習與實作 (Homework)

### Homework 1：密碼檢查
* **檔案名稱**：[password.py](password.py)
* **需求**：讓使用者輸入密碼，若密碼為 `1234` 則輸出 `「密碼正確!歡迎光臨!」`，若錯誤則顯示錯誤並提示重新輸入。

### Homework 2：消費折扣計算
* **檔案名稱**：[discount.py](discount.py)
* **需求**：輸入顧客的購買金額，根據以下區間計算實付金額：
  - 100,000元以上打 8 折。
  - 50,000元以上打 85 折。
  - 30,000元以上打 9 折。
  - 10,000元以上打 95 折。
* **範例輸出**：輸入 `130000` ➡️ 顯示 `實付金額是: 104000.0 元`

### Homework 3：BMI 計算與診斷
* **檔案名稱**：[bmi.py](bmi.py)
* **需求**：輸入身高（公分）與體重（公斤），計算出 BMI 值，並依據下表診斷身體狀態：
  - $\text{BMI} = \text{體重(公斤)} / (\text{身高(公尺)})^2$
  
| BMI 值 | BMI < 18.5 | 18.5 <= BMI < 25 | 25 <= BMI < 30 | BMI >= 30 |
| :---: | :---: | :---: | :---: | :---: |
| **身體狀態** | 太輕 | 正常 | 過重 | 肥胖 |

* **範例輸出**：身高 `177`、體重 `80` ➡️ `您的BMI是 25.53544`，`「您的體重過重」`

### Homework 4：2017 ACC/AHA 血壓分類診斷
依據下表的收縮壓與舒張壓，判定血壓健康狀態：

| 分類 | 收縮壓 (sbp) | 關係 | 舒張壓 (dbp) |
| :--- | :---: | :---: | :---: |
| **正常** | < 120 | 且 | < 80 |
| **血壓升高** | 120 ~ 129 | 且 | < 80 |
| **高血壓一期** | 130 ~ 139 | 或 | 80 ~ 89 |
| **高血壓二期** | >= 140 | 或 | >= 90 |
| **單純收縮期高血壓** | >= 130 | 且 | < 80 |

#### 💡 實作邏輯對比與討論

* **方法一：使用多個 `if`（條件重疊問題）**
  此寫法每個 `if` 都會執行。需要注意如果多個條件同時成立，`suggestion` 會被後面的值蓋掉。此外，最後必須做單純收縮期高血壓判定。
  ```python
  sbp = int(input("請輸入收縮壓:"))
  dbp = int(input("請輸入舒張壓:"))
  suggestion = ""
  if sbp < 120 and dbp < 80:
      suggestion = "正常"
  if 120 <= sbp <= 129 and dbp < 80:
      suggestion = "血壓升高"
  if 130 <= sbp <= 139 or 80 <= dbp <= 89:
      suggestion = "高血壓一期"
  if sbp >= 140 or dbp >= 90:
      suggestion = "高血壓二期"
  if sbp >= 130 and dbp < 80:
      suggestion = "單純收縮期高血壓"
  print(suggestion)
  ```

* **方法二：階梯式 `if-elif-else`（推薦，由重度往輕度排除）**
  使用 `elif` 必須注意先排除「高血壓二期」與「高血壓一期」等嚴重狀態，而「單純收縮期高血壓」因為條件與其他一期/二期狀態有交集，需要格外小心其優先權。
  ```python
  sbp = int(input("請輸入收縮壓:"))
  dbp = int(input("請輸入舒張壓:"))
  
  if sbp >= 140 or dbp >= 90:
      suggestion = "高血壓二期"
  elif sbp >= 130 and dbp < 80:
      suggestion = "單純收縮期高血壓"
  elif sbp >= 130 or 80 <= dbp <= 89:
      suggestion = "高血壓一期"
  elif sbp >= 120 and dbp < 80:
      suggestion = "血壓升高"
  else:
      suggestion = "正常"
  print(suggestion)
  ```

* **方法三：使用 `pyinputplus` 套件進行安全輸入**
  引入第三方套件以確保使用者輸入必定是合法的整數數字：
  ```python
  import pyinputplus as pyip
  sbp = pyip.inputInt(prompt="請輸入收縮壓:")
  dbp = pyip.inputInt(prompt="請輸入舒張壓:")
  
  if sbp >= 140 or dbp >= 90:
      status = '高血壓二期'
  elif sbp >= 130 and dbp < 80:
      status = '單純收縮期高血壓'
  elif sbp >= 130 or (80 <= dbp < 90):
      status = '高血壓一期'
  elif sbp >= 120 and dbp < 80:
      status = '血壓升高'
  else:
      status = '正常'
  print(status)
  ```

---

### 🧠 小測驗解答：
* **Q1**：`(3)` —— `15 >= 14` 成立，`a` 減 2 變 13。
* **Q2**：`(3)` —— `a != 12` 不成立，走 `else` 輸出 "等於 12"，隨後執行外部的 `print("執行結束")`。
* **Q3**：`(3)` —— `11` 不滿足前兩者，走 `else` 輸出 "小於等於 12"。
* **Q4**：`(1)` —— 14 滿足 `12 <= a < 18`，且滿足 `not 14 > 18` (即 `not False` = `True`)。
* **Q5**：`(1)` —— 雖然 `11 >= 12` 為 False，但 `11 < 18` 為 True，使用 `or` 運算子結果為 True。
