# 迴圈 (Loop)

在撰寫程式時，若有些步驟需要重覆執行數次（例如：計算全班學生成績、不斷接收使用者輸入直到特定按鍵按下），我們可以使用**迴圈結構（Looping Structure）**。Python 提供兩種最核心的迴圈：
1. **`while` 迴圈**：通常用於「未知重複次數」的條件式控制。
2. **`for-in` 迴圈**：通常用於「已知重複次數」或「遍歷集合物件」的情境。

---

## 1. 迴圈基本概念

* **重覆執行**可以讓程式中的某一區段流程，在特定條件下反覆執行，避免撰寫冗長且重複的程式碼。
* 設計迴圈時，必須特別留意**結束條件**的設計，否則一旦條件永遠成立，將會導致程式陷入「死迴圈（Infinite Loop）」。

---

## 2. `while` 迴圈 (條件式控制)

`while` 迴圈如同重複執行的 `if` 判斷式。只要條件成立（`True`），迴圈內的程式碼區塊就會反覆執行，直到條件不成立（`False`）為止。

### 📌 語法與控制結構：
```python
設定控制變數的初始值
while 條件式:
    # 條件成立時執行的工作
    # 調整控制變數的內容 (極為重要！避免死迴圈)
```
* 若一開始條件即不成立，迴圈一次都不會執行。

### 💡 操作範例 1：基本數值倒數
此範例示範數值倒數，每輪將變數 `a` 遞減 1：
```python
# while1.py
a = 6
while a > 0:
    print(a)
    a -= 1 
print("離開後 a 為", a)
```

#### 🧠 自我檢驗小測驗：
> **Q1. 請問執行以下程式碼後，最後輸出的變數 a 值是什麼？**
> ```python
> a = 15 
> while a > 0:
>     a -= 2
> print(a)
> ```
> (1) 0  
> (2) 1  
> (3) -1  

### 💡 操作範例 2：計算 2-10 所有偶數的總和
利用 `while` 迴圈，每次遞增 2，並累加偶數數值：
```python
# loop1.py
total = 0
i = 2
while(i <= 10):
    total += i
    print("第", i/2, "次迴圈的 i =", i, "總和為", total)
    i += 2
```

### 💡 操作範例 3：計算一週花費支出總額
此範例示範如何以 `while` 控制執行次數為 7 次，加總每天的固定支出：
```python
# loop2.py
total = 0
i = 1
while (i <= 7):
    if (i < 7):
        output = '請輸入星期' + str(i) + ' 的花費:'
        n = int(input(output))
    elif (i == 7):
        n = int(input("請輸入星期日的花費:"))
    total += n
    i += 1
print(f'本星期的支出為 {total} 元')
```

### 💡 操作範例 4：小明存錢買機車
使用條件控制，當存款金額尚未達到 30,000 元前，不斷讓使用者輸入存款：
```python
# while2.py
deposit = 0
months = 0
while(deposit < 30000):
    months += 1
    inputNum = int(input('請輸入第' + str(months) + "個月份的存款: "))
    deposit += inputNum

print("恭喜! 已經存夠了，存了", months, "個月的總存款為:", deposit, "元。")
```

---

## 3. `for-in` 迴圈 (定次與遍歷)

`for-in` 迴圈主要配合可反覆讀取的物件（如串列、字串、字典）或 `range()` 產生器，能明確地依序提取其中的每個元素，或指定要執行的次數。

### 3.1 使用 `range()` 產生數值串列
* `range()` 用於產生一個範圍的整數序列，它採用惰性產生（Lazy Evaluation），**不會一次性佔用大量記憶體空間**。
* **語法結構**：`range(start, stop, step)`
  - `start`：起始值，預設為 0。
  - `stop`：結束值（**產生的值不包含此結束值**）。
  - `step`：步長（每次的變動量），預設為 1。

#### 📝 語法展示：
```python
# 1. 單一參數：預設從 0 開始，到 3 之前結束
for x in range(3): 
    print(x)  # 輸出: 0, 1, 2
    
# 可以用 list() 轉型觀測其產生的數值清單
print(list(range(0, 3)))  # 輸出: [0, 1, 2]

# 2. 負步長遞減 (從大到小)
print(list(range(2, -1, -1)))  # 輸出: [2, 1, 0]

# 3. 指定步長遞增
print(list(range(0, 11, 2)))  # 輸出: [0, 2, 4, 6, 8, 10]
```

#### 🧠 自我檢驗小測驗：
> **Q2. 請問 `range(6, 10)` 執行後會產生哪些整數？**
> (1) 6, 7, 8, 9  
> (2) 6, 7, 8, 9, 10  
> (3) 7, 8, 9  
>
> **Q3. 請問 `range(0, 8, 2)` 執行後會產生哪些整數？**
> (1) 0, 2, 4, 6, 8  
> (2) 0, 2, 4, 6  
> (3) 0, 2, 8  

### 3.2 `for-in` 搭配 `range()` 實戰

#### 💡 操作範例 1：學生成績輸入程式
設計一個輸入成績的程式，記錄 5 位學生成績，並顯示班上總分及平均分：
```python
# range1.py
total = 0
students = 5
for i in range(students):
    studentScore = int(input('請輸入第' + str(i+1) + '位學生的成績:'))
    total += studentScore

print("全班總成績為:" + str(total) + "分,平均分數為" + str(total/students) + "分")
```

#### 💡 操作範例 2：1 到 100 的累加
我們可以使用 `for` 迴圈或 `while` 迴圈來計算 1 到 100 的總和，對比如下：

##### 1️⃣ 使用 `for` 迴圈寫法 (更簡潔)
```python
# various_loop1.py
total = 0
for i in range(1, 101):
    total += i
print(f"1 加到 100 的總合是 {total}") 
```

##### 2️⃣ 使用 `while` 迴圈寫法
```python
# various_loop2.py
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"1 加到 100 的總合是 {total}") 
```

#### 💡 操作範例 3：1 到 100 的奇數與偶數加總
使用 `for` 迴圈，在每輪以 `%` 運算子判斷奇偶數並分開累加：
```python
evenTotal = 0
oddTotal = 0

for i in range(1, 101):
    if i % 2 == 0:
        evenTotal += i
    else:
        oddTotal += i

print(f"1加到100偶數的加總為 {evenTotal}")
print(f"1加到100奇數的加總為 {oddTotal}") 
```

➡️ [進階練習：for 迴圈與 if 判斷整合 (奇偶數與倍數)](practice1.md)

---

### 3.3 `for-in` 遍歷集合物件
`for-in` 迴圈最適合用來讀取各種容器（如串列、字串、字典）中的每一個元素。

#### 1️⃣ 遍歷串列 (List)
```python
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits: 
    print(rabbit)
```

#### 2️⃣ 遍歷字串 (String)
字串在 Python 中是序列，每次會取出一個字元：
```python
word = 'cat'
for letter in word:
    print(letter)  # 依序輸出: c, a, t
```

#### 3️⃣ 遍歷字典 (Dictionary)
* 預設遍歷取得的是字典的 **鍵 (key)**。
* 使用 `.values()` 遍歷可取得 **值 (value)**。
* 使用 `.items()` 遍歷可取得包含 `(key, value)` 的元組，並可直接使用「拆解法」同時取出兩個變數。

```python
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

# (1) 遍歷 Key (預設)
for card in accusation:
    print(card)

# (2) 遍歷 Value
for value in accusation.values(): 
    print(value)

# (3) 使用 items() 與拆解法同時取出鍵與值
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
```

#### 4️⃣ 使用 `zip()` 同步平行讀取多個串列
當我們有數個長度相同的串列，想在同一輪迴圈同步讀取時，可以使用 `zip()`：
```python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts): 
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
```

---

## 4. 迴圈控制與中斷 (`break` / `continue` / `else`)

在迴圈執行過程中，我們常需要提早中斷迴圈或跳過某些輪次，這時可以使用以下三個關鍵字：
* **`break`**：直接強制結束整個迴圈，跳至迴圈外的下一行程式。
* **`continue`**：跳過目前這一輪剩下的程式碼，直接回到迴圈開頭準備執行下一輪。
* **`else`**：若迴圈是「正常執行完畢」（**沒有因為 break 而中斷**），則在迴圈結束後執行 else 區塊。

### 4.1 `break` 的應用 (無限迴圈)
使用 `while True:` 配合 `if` 與 `break` 可以在未知迴圈執行次數時，進行有效的輸入流程控制。

#### 💡 操作範例 1：輸入英文字母 (按 q 離開)
使用 `while True` 建立不確定執行次數的迴圈，當使用者輸入 'q' 時以 `break` 中斷：
```python
while True:
    stuff = input("請輸入小寫英文字[按q會離開]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())
print("程式結束")
```

➡️ [進階練習：英文單字卡輸入程式(while 配合 break)](practice3.md)

#### 💡 操作範例 2：學生成績輸入防錯程式
小美是一位教師，設計一個輸入成績的程式，如果輸入負數表示輸入結束，隨後計算總分與平均分：
```python
# while1_s.py
num = 0
total = 0
while(True):
    num += 1
    score = int(input('請輸入第' + str(num) + '位學生的成績(輸入負數離開): '))    
    if(score < 0):
        break
    total += score
    
# 已經跳出 while    
print('全班總成績為:', total, "平均分數為:", "%.2f" % (total/(num-1)) )
```

---

### 4.2 `continue` 的應用

#### 💡 操作範例：累加正偶數
設計一個程式讓使用者輸入數值，只有正偶數值會被加總，若輸入奇數則跳過，輸入負數則結束程式：
```python
# continue.py
total = 0
num = 0
while True:    
    input_value = int(input(f"請輸入第{num+1}個數值: "))
    if input_value < 0:
        break
    num += 1
    if input_value % 2 == 1:
        continue  # 跳過本次，直接準備下一次輸入
    total += input_value    
    
print(f"輸入的次數是{num}，所有輸入的正偶數的加總是:{total}")
```

➡️ [進階練習：while 迴圈整合 continue 與 break](practice4.md)

---

### 4.3 迴圈的 `else` 區塊
在 `while` 或 `for` 迴圈後加上 `else`，只有在迴圈結束且沒有觸發 `break` 時才會執行。這在搜尋、比對資料時非常實用。

#### 💡 操作範例 1：`while-else` 檢查偶數
```python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position] 
    if number % 2 == 0:
        print('發現偶數', number)
        break
    position += 1
else:  # 迴圈正常結束 (陣列裡沒有任何偶數)
    print('沒有偶數')
```

#### 💡 操作範例 2：`for-else` 起司檢查
```python
cheeses = []
for cheese in cheeses:
    print('我喜歡的 cheese 有', cheese)
    break
else:  # 迴圈一次都沒跑，或正常結束時執行
    print('沒有任何 cheese') 
```

---

## 5. 巢狀迴圈 (Nested Loops)

當我們在迴圈內部又寫了另一個迴圈，便稱為「巢狀迴圈」。外層迴圈執行一次，內層迴圈就必須完整地跑完一輪。

### 💡 操作範例 1：巢狀迴圈繪製直角三角形
外層迴圈控制高度（列數），內層迴圈控制每列印出的數量：
```python
# fornest1.py
for i in range(1, 6):
    for _ in range(i):
        print("#", end='')
    print()
```

### 💡 操作範例 2：數字倒三角排列
試寫出下列數字排列，外層迴圈遞減，內層迴圈依據外層當前變數重複列印：
```python
# nestedLoop1.py
# 顯示:
# 55555
# 4444
# 333
# 22
# 1
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end='')
    print()
```

### 💡 操作範例 3：列印九九乘法表
雙層 `for` 迴圈遍歷，並使用格式化對齊：
```python
# forNest2.py
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i:<2d}*{j:2d} ={i*j:2d}", end='  ')
    print()
```

➡️ [進階練習：巢狀迴圈與圖形繪製](practice2.md)

---

## 6. 綜合實戰應用

### 6.1 猜數字遊戲 (範圍縮小版)
此實戰使用 `random.randint` 產生一個 1 到 100 的隨機目標值。使用者不斷輸入猜測，程式除了計次外，也會根據使用者猜測動態更新猜測範圍：
```python
# guess.py
import random
min_val = 1
max_val = 100
count = 0
target = random.randint(1, 100)
print("===============猜數字遊戲================:\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍{0}~{1}: ".format(min_val, max_val)))
    if(keyin >= min_val and keyin <= max_val):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了", count, "次")
            break
        elif (keyin > target):
            max_val = keyin
            print("再小一點")
        elif (keyin < target):
            min_val = keyin
            print("再大一點")
        print("您猜了", count, "次\n")
    else:
        print("請輸入提示範圍內的數字")
```

➡️ [進階練習：猜數字遊戲與流程邏輯](practice5.md)

---

### 6.2 猜單雙數遊戲
```python
import random

while True:
    user = input("請猜單(1)或雙(0)，輸入 q 離開：")
    if user == 'q':
        break
    if user not in ['0', '1']:
        print("請輸入 1 或 0")
        continue
    number = random.randint(1, 100)
    print(f"隨機數字是：{number}")
    if number % 2 == int(user):
        print("你猜對了！\n")
    else:
        print("你猜錯了！\n")
```

---

### 6.3 乘法累加計算器
設計一個程式，使用者輸入 M 與 N，求出 $M \times 1 + M \times 2 + \dots + M \times N$ 的值：
```python
# inputLoop.py
m = int(input('輸入 M:'))
n = int(input('輸入 N:'))
total = 0
for num in range(n):
    num += 1
    if num != n:
        print(m, '*', num, ' + ', end='')
    else:
        print(m, '*', num, ' = ', end='')

    total += m * num

print(total)
```

---

### 6.4 最大公因數與最小公倍數
輸入兩個數值，並求出這兩個數值的最大公因數 (GCD) 和最小公倍數 (LCM)：
```python
# commonfactor.py
print('求兩數的最大公因數和最小公倍數')
n = int(input('請輸入第一個整數:'))
m = int(input('請輸入第二個整數:'))

if(n > m):
    max_val = n
    min_val = m
else:
    max_val = m
    min_val = n

# 尋找最大公因數
maxResult = 1
for num in range(min_val):
    num += 1
    if((min_val % num) == 0 and (max_val % num) == 0):
        maxResult = num

# 計算最小公倍數 (LCM = (A * B) / GCD)
minResult = (n / maxResult) * (m / maxResult) * maxResult

print('{0:d} 和 {1:d} 的最大公因數: {2:d}'.format(n, m, maxResult))
print('{0:d} 和 {1:d} 的最小公倍數: {2:.0f}'.format(n, m, minResult))
```

---

### 6.5 質數判定
設計一個程式，輸入 end 值，印出 1 到 end 的所有質數：
```python
end = int(input("請輸入 end 值: "))
print(f"1 到 {end} 的質數是:")
for num in range(2, end + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num}", end=" ")
```

---

### 🧠 小測驗解答：
* **Q1**：`(3)` —— 數值變化為 15 ➡️ 13 ➡️ 11 ➡️ 9 ➡️ 7 ➡️ 5 ➡️ 3 ➡️ 1 ➡️ -1，此時 -1 不大於 0 跳出迴圈，輸出 -1。
* **Q2**：`(1)` —— `range(6, 10)` 包含 6, 7, 8, 9，但不包含 10。
* **Q3**：`(2)` —— `range(0, 8, 2)` 從 0 開始每步加 2，為 0, 2, 4, 6，但不包含結束值 8。
