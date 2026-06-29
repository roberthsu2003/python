# 函式和Comprehension

## 為什麼要有自訂函數

在撰寫程式時，如果沒有自訂函數（Function），當程式邏輯變得複雜或需要重複執行時，程式碼會變得非常臃腫且難以閱讀。

以**猜數字遊戲**為例，若原本的單次遊戲流程如下：

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
    if(keyin >=min and keyin <= max):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了",count,"次")
            break
        elif (keyin > target):
            max = keyin
            print("再小一點")
        elif (keyin < target):
            min = keyin
            print("再大一點")
        print("您猜了",count,"次\n")
    else:
        print("請輸入提示範圍內的數字")
```

### 觀念說明：增加「是否再玩一次」的需求

如果我們想要在遊戲結束後，**詢問使用者是否要再玩一次**，我們有兩種設計方式：

#### 1. 不使用自訂函數的寫法（邏輯複雜）
如果沒有函數，我們必須使用**巢狀迴圈（雙重迴圈）**來控制：
- 外層迴圈：負責控制「是否要重玩遊戲」。
- 內層迴圈：負責控制「單次猜數字的遊戲流程」。

此時會遇到以下問題：
1. **巢狀結構過深**：程式碼縮排層級變多，降低可讀性。
2. **狀態管理混亂**：每次重新遊戲時，我們都必須在外部手動重設 `min`, `max`, `count`, `target` 等變數。
3. **流程控制複雜**：內層迴圈的 `break` 只能跳出猜數字迴圈，我們還需要額外的邏輯來判斷何時跳出外層迴圈。

**實作範例（無函數版本）：**
```python
import random

while True:
    # 每次新遊戲開始，都必須手動重新初始化這些變數
    min_val = 1
    max_val = 100
    count = 0
    target = random.randint(1, 100)
    print("===============猜數字遊戲=================:\n")
    
    # 內層迴圈：單次遊戲流程
    while True:
        count += 1
        keyin = int(input("猜數字範圍{0}~{1}: ".format(min_val, max_val)))
        if keyin >= min_val and keyin <= max_val:
            if keyin == target:
                print("賓果!猜對了, 答案是:", target)
                print("您猜了", count, "次")
                break  # 只跳出內層迴圈
            elif keyin > target:
                max_val = keyin
                print("再小一點")
            elif keyin < target:
                min_val = keyin
                print("再大一點")
            print("您猜了", count, "次\n")
        else:
            print("請輸入提示範圍內的數字")
            
    # 內層遊戲結束後，在外層詢問是否繼續
    play_again = input("是否要再玩一次？(y/n): ")
    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break  # 跳出外層迴圈
```

---

#### 2. 使用自訂函數的寫法（邏輯清晰、簡單）
如果我們將「**單次猜數字遊戲的完整邏輯**」封裝成一個自訂函數 `play_game()`，整個邏輯會變得非常乾淨：
- **職責分離（Single Responsibility）**：`play_game()` 只專注於「玩一次遊戲的過程」，而主程式只專注於「是否繼續玩遊戲」。
- **自動狀態重設**：每次呼叫 `play_game()` 時，函式內部的區域變數（`min_val`, `max_val`, `count`, `target`）都會自動重新建立並初始化，完全不需要手動重設。
- **避免巢狀結構**：主程式只需用一個簡單的單層迴圈呼叫函式即可。

**實作範例（自訂函數版本）：**
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
                break  # 結束此函式中的迴圈，函式執行完畢即返回
            elif keyin > target:
                max_val = keyin
                print("再小一點")
            elif keyin < target:
                min_val = keyin
                print("再大一點")
            print("您猜了", count, "次\n")
        else:
            print("請輸入提示範圍內的數字")

# 主程式流程：只負責控制「是否繼續遊玩」
while True:
    play_game()  # 呼叫函式，開始一局新遊戲
    play_again = input("是否要再玩一次？(y/n): ")
    if play_again.lower() != 'y':
        print("遊戲結束，謝謝遊玩！")
        break
```

透過自訂函數，我們成功將複雜的巢狀迴圈解構為簡單的線性呼叫，不僅程式碼變得更容易閱讀，也更容易進行功能擴充（例如：未來要加入難度選擇或計分功能時，只需修改 `play_game` 函式，主程式完全不需改動）。

[進階練習](./practice1.md)

## 良好函式設計的 5 個原則（簡化版 SOLID）
| **原則** | **說明**      |
| ------ | ----------- |
| 單一職責   | 每個函式只做一件事   |
| 易讀命名   | 使用有意義的名字    |
| 可測試    | 可以透過不同輸入做測試 |
| 可重用    | 通用邏輯、少用硬編碼  |
| 錯誤處理   | 適當處理例外狀況    |



## 自訂函數 Functions
- 自訂函數名稱與內容的安排:
	- 函數區塊以 def 開始，後接函數名稱和括號 ( )
	- 括號 ( ) 接上冒號後下一行縮排就是函數的內容
- 不支援多個同名的自訂函數:
	- 如果有同名的自訂函數則支援最後一個函數。
- 若對函數操作有任何疑問:
	- 可用 help(函數名稱) 取得說明文件。
- 自訂函數接收資料:
	- 傳入函數的參數放在 ( ) 內。
	- 可以接收多個，以逗點隔開。
	- 接收參數可以是變數，也可以是 list。
	- 函數若設定接收參數，呼叫函數時一定要給參數。
	- 接收參數可設定為不固定數量。
	- 若不接收則為空白。
- 自訂函數傳回資料:
	- 若要傳回資料，則請於函數最後一行執行 return()語法
	- return( ) 可以傳回一個運算式或者資料
	- 函數結束時不一定要傳回資料
	- 不傳回資料方式:
		- return( ) 內沒有資料
		- 省略 return( )
		- 寫成 return

## python函式設計練習表
| **題號** | **題目名稱**       | **題目說明**                   |
| ------ | -------------- | -------------------------- |
| 1      | say_hello      | 寫一個函式，輸入名字，輸出 Hello, 名字    |
| 2      | is_even        | 輸入一個整數，回傳是否為偶數（True/False） |
| 3      | sum_list       | 傳入一個數字串列，回傳總和              |
| 4      | find_max       | 輸入一串數字，找出最大值並回傳            |
| 5      | calculate_bmi  | 傳入身高（公尺）與體重（公斤），回傳 BMI 值   |
| 6      | convert_temp   | 攝氏與華氏互換（攝氏 → 華氏，華氏 → 攝氏）   |
| 7      | is_prime       | 判斷是否為質數（Prime Number）      |
| 8      | count_vowels   | 計算字串中有幾個母音（a, e, i, o, u）  |
| 9      | reverse_string | 回傳字串反轉結果                   |
| 10     | get_grade      | 傳入分數，根據標準回傳等級（A~F） |

### 1. 自訂函數沒有參數也沒有傳回值

```python
# 範例：定義一個印出歡迎詞的簡單函式
def say_welcome():
    print("歡迎光臨 Python 程式設計課！")

# 呼叫函式
say_welcome()
```

```python
# 範例：使用 pass 定義一個不做任何事的空函式
def do_nothing():
    pass

do_nothing()
```

### 2. 自訂函數有接收參數但無傳回值

```python
# 範例（對應題號 1: say_hello）：接收名字，並印出問候語
def say_hello(name):
    print(f"Hello, {name}!")

# 呼叫函式並傳入引數
say_hello("Alice")
say_hello("Bob")
```

---

### 3. 自訂函數有接收參數也有傳回值

使用 `return` 可以將運算結果傳回給呼叫端。這是最常用且最符合 SOLID 原則中「單一職責」與「可測試性」的函式設計方式（因為函式只專注於邏輯計算，將輸出/輸入的控制權留給呼叫端）。

```python
# 範例一（對應題號 2: is_even）：判斷整數是否為偶數並傳回 True/False
def is_even(number):
    return number % 2 == 0

# 呼叫函式並使用結果
result = is_even(7)
print(f"7 是偶數嗎？ {result}")  # 輸出: 7 是偶數嗎？ False

if is_even(10):
    print("10 是偶數")
```

```python
# 範例二（對應題號 5: calculate_bmi）：傳入身高（公尺）與體重（公斤），回傳 BMI
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

my_bmi = calculate_bmi(1.75, 70)
print(f"計算出的 BMI 為: {my_bmi:.2f}")
```

[進階練習](./practice2.md)

### 4. 傳入容器與字串的函式練習

函式的參數可以接收任何 Python 物件，包括串列（List）或字串（String）。

```python
# 範例一（對應題號 3: sum_list）：傳入數字串列，回傳總和
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

scores = [85, 90, 78, 92]
print(f"總分為: {sum_list(scores)}")  # 輸出: 總分為: 345
```

```python
# 範例二（對應題號 9: reverse_string）：傳入字串，回傳反轉字串
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))  # 輸出: nohtyP
```

### 5. 複雜邏輯與條件分支練習

當函式內部包含較複雜的邏輯或多重條件分支時，早期回傳（Early Return）是保持程式碼乾淨的好方法。

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

[進階練習](./practice3.md)

### 6. 函數傳回多值

- Python 的函數可以傳回多值，這是透過將多個值自動打包成 `tuple` 實現的。
- 接收時，可以使用「多重賦值（Unpacking）」一次拆解給多個變數。

```python
# 範例：找出串列中的最大值與最小值並同時回傳
def get_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)  # 自動打包成 tuple 回傳

scores = [85, 92, 78, 60, 99]
min_score, max_score = get_min_max(scores)  # 拆解 Tuple
print(f"最低分: {min_score}, 最高分: {max_score}")
```

## python專案用的主程式架構

在開發較具規模的 Python 專案時，我們通常不會把執行邏輯直接裸露寫在檔案的頂層，而是會封裝在一個名為 `main()` 的主主程式函式中，並使用 Python 特有的入口保護機制。

### 1. 為什麼需要主程式架構？
當 Python 檔案（模組）被其他檔案 `import` 時，Python 會自動將該檔案「從頭到尾執行一遍」。
如果我們將專案的測試代碼或執行邏輯寫在最外層（頂層），那麼其他人在 import 我們的函式庫時，就會無意間觸發這些執行邏輯。

為了區分「**此檔案是被直接執行**」還是「**被當作模組載入**」，我們會使用內建變數 `__name__`。

### 2. 核心觀念：`__name__` 與 `__main__`
- **直接執行該檔案時**：內建變數 `__name__` 的值會被自動設為 `"__main__"`。
- **被其他檔案 import 時**：`__name__` 的值會是「該檔案的檔名」（不含 `.py` 後綴）。

因此，我們可以使用條件判斷 `if __name__ == '__main__':` 來確保只有在檔案被**直接執行**時，才會啟動主程式。

### 3. 標準的主程式（main.py）範例

```python
# main.py

def calculate_average(scores):
    return sum(scores) / len(scores)

def main():
    # 專案的主程式入口與控制邏輯
    student_scores = [85, 90, 78, 92]
    avg = calculate_average(student_scores)
    print(f"學生成績平均為: {avg:.2f}")

# 程式的入口點 (Entry Point)
if __name__ == '__main__':
    main()
```

> **💡 設計主程式架構的好處：**
> 1. **模組化與可測試性**：其他程式碼可以安全地 import `calculate_average` 函式來使用，而不會執行 `main()` 裡的測試邏輯。
> 2. **變數隔離**：`main()` 內部的變數都屬於區域變數，不會污染到全域空間，這也是良好程式設計（SOLID）的重要實踐。

---

### 變數影響範圍：命名空間 (Namespace) 與作用域 (Scope)

在 Python 中，變數可以在哪裡被讀取或修改，取決於它被定義在什麼**命名空間（Namespace）**中。初學者需要特別留意哪些語法會建立新的命名空間，而哪些不會。

#### 🔑 核心規則：
1. **會建立獨立命名空間的語法**：
   - 只有 `def` (函式)、`class` (類別) 以及整個 `module` (檔案) 會建立自己獨立的作用域 (Scope)。
2. **不會建立獨立命名空間的語法**：
   - 常見的控制結構如 `if`、`for`、`while`、`with` 等，雖然它們有縮排區塊，但**不會**建立新的命名空間！在這些區塊內定義的變數，依然屬於外層的作用域。

---

### 1. 函式 (Function) 會建立獨立作用域 (Namespace)

在函式內部定義的變數屬於 **區域變數 (Local Variable)**，只在該函式內部有效，不會影響到函式外的 **全域變數 (Global Variable)**。

#### 操作範例：區域變數與全域變數隔離 (fun3.py)
```python
a = 5

def func_sum():
    a = 10  # 這是在函式內部建立的新變數 a，只在函式內有效 (區域變數)
    print("函數內:", a)

print("函數外1:", a)  # 輸出: 5
func_sum()           # 輸出: 10
print("函數外2:", a)  # 輸出: 5 (外面的 a 沒有被改變)
```

#### 操作範例：函式內讀取全域變數 (fun3-1.py)
如果函式內部沒有同名的區域變數，Python 會自動向外尋找（遵循 LEGB 規則）並讀取全域變數。
```python
a = 5

def func_sum():
    print("函數內:", a)  # 內部沒有宣告 a，所以直接讀取外部全域變數 a

print("函數外1:", a)  # 輸出: 5
func_sum()           # 輸出: 5
print("函數外2:", a)  # 輸出: 5
```

#### 操作範例：經典錯誤 - 未宣告先使用 (fun3-2.py)
如果在函式內部有對變數進行賦值動作（例如 `a = ...`），Python 會在編譯時將其視為區域變數。這會導致在賦值之前如果試圖讀取它，會產生錯誤。
```python
a = 5

def func_sum():
    # 因為下面有 a = a + 1，Python 認定內部的 a 是區域變數
    # 但在執行 a + 1 時，區域變數 a 尚未被賦予初始值，因此會報錯！
    a = a + 1 
    print("函數內:", a)

print("函數外1:", a)
func_sum()  # 會拋出 UnboundLocalError: local variable 'a' referenced before assignment
```

#### 💡 解決方案：使用 `global` 關鍵字修改全域變數
如果我們**確實想要**在函式內部修改全域變數的值，可以使用 `global` 關鍵字來聲明，告訴 Python：「請直接操作全域的那一個變數，不要建立區域變數」。

```python
a = 5

def func_sum():
    global a  # 聲明 a 為全域變數
    a = a + 1  # 現在可以安全地讀取並修改全域變數 a
    print("函數內:", a)

print("函數外1:", a)  # 輸出: 5
func_sum()           # 輸出: 6
print("函數外2:", a)  # 輸出: 6 (全域變數成功被修改)
```

---

### 2. if / for / while / with 縮排**不會**建立命名空間

與 C/C++ 或 Java 的區塊作用域（Block Scope）不同，Python 的 `if`、`for` 等控制流程**不會**將變數鎖在縮排內。

#### 操作範例：在 if 區塊內定義變數
```python
if True:
    x = 100  # 在 if 的縮排中定義變數

# 在 if 外面依然可以直接讀取與修改 x
print("if 外面讀取 x:", x)  # 輸出: 100
```
> **⚠️ 注意**：如果 `if` 條件沒有成立（例如 `if False:`），那麼變數將不會被定義，此時在外面存取它依然會拋出 `NameError`。

#### 操作範例：在 for 迴圈中定義變數
```python
for i in range(3):
    temp_val = i * 2  # 迴圈內部定義的變數

# 迴圈結束後，temp_val 與 迴圈變數 i 依然在外部作用域中存在！
print("迴圈外的 i:", i)          # 輸出: 2
print("迴圈外的 temp_val:", temp_val)  # 輸出: 4
```

#### 操作範例：with 區塊
```python
# 假設我們建立/開啟一個暫時檔案
with open("temp.txt", "w") as f:
    inner_var = "哈囉"

# 在 with 區塊外面依然可以讀取 inner_var 與 f
print("with 外面讀取 inner_var:", inner_var)  # 輸出: 哈囉
print("with 外面讀取 f 是否關閉:", f.closed)    # 輸出: True (檔案已關閉，但變數 f 依然可存取)
```

> **💡 教學小結：**
> 初學者在編寫 Python 時，不用擔心 `if` 或 `for` 會把變數「鎖住」拿不出來；但相對地，在函式 `def` 內部的變數則有嚴格的隔離保護，外部無法直接取得。

---

## 參數傳遞機制：傳不可變與可變實體

在許多程式語言中，參數傳遞可區分為 **Call by Value（傳值呼叫）** 與 **Call by Reference（傳址呼叫）**。
然而在 Python 中，本質上所有的參數傳遞都是 **Call by Object Reference（傳送物件的參考）**。其行為特性取決於傳遞的**物件本身是不可變（Immutable）還是可變（Mutable）**。

---

### 1. 傳送不可變實體（行為像 Call by Value）

當我們傳入 **不可變物件**（如：整數 `int`、浮點數 `float`、字串 `str`、元組 `tuple` 等）給函式時，行為類似於 Call by Value：
- 在函式內部修改該參數時，由於物件本身不能被修改，Python 會在記憶體中建立一個全新的物件，並將區域變數指向它。
- 這代表**函式內部對參數的修改，完全不會影響到函式外部原始變數的值**。

#### 操作範例：傳遞整數物件 
```python
def turbo(speed):
    print('加速前（函式內）速度:', speed)
    speed += 10  # 建立新的整數物件，並讓區域變數 speed 指向它
    print('加速後（函式內）速度:', speed)
    return speed

if __name__ == '__main__':
    original_speed = 80
    
    # 呼叫函式：傳入整數 80
    new_speed = turbo(original_speed)
    
    print('加速後（函式外）new_speed:', new_speed)         # 輸出: 90
    print('加速後（函式外）original_speed:', original_speed) # 輸出: 80 (原本的變數完全不受影響)
```

---

### 2. 傳送可變實體

當我們傳入 **可變物件**（如：列表 `list`、字典 `dict`、集合 `set` 等）給函式時，行為類似於 Call by Reference：
- 函式內部與外部的變數，都會指向記憶體中的**同一個物件**。
- 在函式內部對該物件進行修改（如：修改列表內的元素）時，由於物件本身是可變的，會直接在該物件上進行修改 (In-place Modification)。
- 這代表**函式內部對參數內容的修改，會直接同步反映在函式外部的原始變數上**（不需要 return 回傳）。

#### 操作範例：傳遞列表物件 (callByReference.py)
```python
def turbo(listSpeed):
    print('加速前（函式內）速度:', listSpeed[0])
    listSpeed[0] += 10  # 直接修改傳入之列表物件的內容
    print('加速後（函式內）速度:', listSpeed[0])

if __name__ == '__main__':
    s = 80
    listS = [s]  # 將整數打包進可變的列表 (List) 中
    
    # 呼叫函式：傳入列表
    turbo(listS)
    
    # 由於列表是可變的，外部的列表內容已經被函式直接改變了！
    print('加速後（函式外）速度:', listS[0])  # 輸出: 90
```

[進階練習](./practice4.md)

---

### 💡 觀念總結與比較

| 傳遞型態 | 常見資料類型 | 函式內部修改參數時的行為 | 外部變數是否受影響 | 模擬之傳遞方式 |
| :--- | :--- | :--- | :--- | :--- |
| **不可變物件** (Immutable) | `int`, `float`, `str`, `tuple` | 建立新物件，將區域變數重新指向它 | ❌ 否，外部變數維持原值 | **Call by Value** (傳值) |
| **可變物件** (Mutable) | `list`, `dict`, `set` | 直接在原物件內部進行修改 (In-place) | ✅ 是，外部變數內容會被修改 | **Call by Reference** (傳址) |

---


## None的使用

- None代表變數佔著一個記憶體空間，但沒有儲存任何東西
- None轉換為boolean值時代表為False

```python
>>> thing = None
>>> if thing:
			print("It's some thing")
		else:
			print("It's no thing")
			
輸出結果 =============
It's no thing
```

使用 is 檢查是否為None

```python
>>> if thing is None:
			print("It's nothing")
		else:
			print("It's something")
輸出結果 =============
It's no thing		
```

以下，代表是None

- '' 空字串
- [] 空陣列
- (,) 空tuple
- {} 空的dictionary
- set() 空的set

```python
>>> def is_none(thing):
			if thing is None:
				print("It's None")
			elif thing:
				print("It's True")
			else:
				print("It's False")
```

 
## 使用 Comprehensions 語法快速建立容器

Comprehensions（解析式或推導式）是 Python 一種非常強大且優雅的語法，它能讓我們用簡短的一行程式碼，快速建立 List、Dictionary、Set 或 Generator。

---

### 1. 列表解析式 (List Comprehensions)

#### 📌 基本語法
`[ expression for item in iterable ]`

#### 💡 對比：建立包含 1 到 5 的列表
- **傳統的 `for` 迴圈作法**：
  ```python
  number_list = []
  for number in range(1, 6):
      number_list.append(number)
  # 結果: [1, 2, 3, 4, 5]
  ```
- **使用 List Comprehension 的作法**：
  ```python
  number_list = [number for number in range(1, 6)]
  # 結果: [1, 2, 3, 4, 5]
  ```

#### 💡 變化一：在表達式中進行運算
我們可以在表達式（expression）中對元素進行修改。例如：希望列表內的每個數字都減 1：
```python
number_list = [number - 1 for number in range(1, 6)]
# 結果: [0, 1, 2, 3, 4]
```

#### 💡 變化二：加上條件篩選 (if)
`[ expression for item in iterable if condition ]`
只將符合條件的元素加入列表中。例如：只篩選出 1 到 5 之間的奇數：
- **List Comprehension**：
  ```python
  odd_list = [number for number in range(1, 6) if number % 2 == 1]
  # 結果: [1, 3, 5]
  ```
- **相當於傳統的寫法**：
  ```python
  odd_list = []
  for number in range(1, 6):
      if number % 2 == 1:
          odd_list.append(number)
  ```

#### 💡 變化三：巢狀迴圈 (Nested Loops)
我們可以在一行解析式中寫入雙重（甚至多重）迴圈。例如：產生 row 和 col 的配對座標：
- **傳統的寫法**：
  ```python
  cells = []
  for row in range(1, 4):
      for col in range(1, 3):
          cells.append((row, col))
  ```
- **List Comprehension 的寫法**：
  ```python
  cells = [(row, col) for row in range(1, 4) for col in range(1, 3)]
  # 結果: [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
  ```

---

### 2. 字典解析式 (Dictionary Comprehensions)

#### 📌 基本語法
`{ key_expression : value_expression for item in iterable }`

我們可以快速將一個可反覆的物件轉換成字典。
#### 操作範例：計算字串中每個字母出現的次數
```python
word = 'letters'

# key 不會重複，重複的 key 會被新的 value 覆蓋
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)  
# 輸出: {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
```

> **💡 優化技巧**：上面的寫法中，重複的字母會被反覆執行 `word.count()`。我們可以先將字串轉為 `set` 以去除重複字母，提升計算效率：
> ```python
> word = 'letters'
> letter_counts = {letter: word.count(letter) for letter in set(word)}
> print(letter_counts)
> # 輸出: {'e': 2, 's': 1, 'r': 1, 'l': 1, 't': 2} (順序可能因 set 而不同)
> ```

---

### 3. 集合解析式 (Set Comprehensions)

#### 📌 基本語法
`{ expression for item in iterable if condition }`

集合解析式會自動去除重複的元素。
```python
# 找出 1 到 5 中，除以 3 餘數為 1 的數字
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)
# 輸出: {1, 4} (集合會自動去重，且不保證順序)
```

---

### 4. 產生器解析式 (Generator Comprehensions)

#### 📌 特點
- **注意**：用小括號 `()` 包裹起來的不是 "Tuple Comprehension"，而是會產生一個**產生器 (Generator) 物件**。
- **優勢**：產生器不會在記憶體中一次生成並儲存所有的資料，而是當你需要時（例如在 `for` 迴圈中）才一個一個計算並吐出，非常節省記憶體！
- **特性**：**只能讀取一次**。一旦走訪完畢，該產生器就空了。

```python
# 建立一個產生器
number_thing = (number for number in range(1, 6))
print(type(number_thing))  # 輸出: <class 'generator'>

# 走訪產生器
for number in number_thing:
    print(number)  # 依序輸出 1, 2, 3, 4, 5

# 試圖再次讀取它：
try_again = list(number_thing)
print(try_again)  # 輸出: [] (已經被消耗完畢，無法再次讀取)
```

如果想要一次把產生器轉為清單，可以使用 `list(generator)`：
```python
number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
print(number_list)  # 輸出: [1, 2, 3, 4, 5]
```

---

### 5. 名稱空間查詢：locals() 與 globals()

Python 提供兩個內建函式，方便我們檢視目前作用域中的命名空間內容：

- `locals()`：回傳包含目前**區域命名空間**所有變數的字典。
- `globals()`：回傳包含目前**全域命名空間**所有變數的字典。

```python
animal = 'fruitbat'  # 全域變數

def change_local():
    animal = 'wombat'  # 區域變數
    print("內部 locals():", locals())

change_local()
# 輸出: 內部 locals(): {'animal': 'wombat'}

print("外部 globals():", globals()['animal'])
# 輸出: 外部 globals(): fruitbat (可以從全域字典中讀取變數)
```

---

### 6. 函式的元數據 (Metadata)：__name__ 與 __doc__

在 Python 中，函式也是物件，它擁有自帶的屬性可以供我們查詢：
- `func.__name__`：取得函式的名稱（字串格式）。
- `func.__doc__`：取得函式的說明文件（Docstring，即函式內部的多行註解 `'''`）。

```python
def amazing():
    '''這是一個非常棒的函式說明文件。
    用來說明這個函式的功能與用法。'''
    print("這是一個輸出測試")

# 讀取函式的屬性
print("函式名稱:", amazing.__name__)
# 輸出: 函式名稱: amazing

print("函式說明文件:", amazing.__doc__)
# 輸出:
# 函式說明文件: 這是一個非常棒的函式說明文件。
#     用來說明這個函式的功能與用法。
```

---

### 7. 錯誤與例外處理 (Try...Except)

在程式執行過程中，難免會遇到錯誤（例如索引超出範圍、除以零等），這時程式會崩潰並拋出錯誤訊息（Exception）。我們可以使用 `try...except` 來捕捉並處理這些例外狀況，讓程式能優雅地繼續運行。

```python
# 沒處理錯誤的狀況：程式會直接崩潰
short_list = [1, 2, 3]
position = 5
# print(short_list[position])  # 會拋出 IndexError: list index out of range 錯誤並中斷程式
```

#### 💡 基本防禦性處理
```python
short_list = [1, 2, 3]
position = 5

try:
    print(short_list[position])
except IndexError:
    # 只有在發生 IndexError 時才會執行這裡
    print(f"錯誤：索引值 {position} 超出範圍，請輸入 0 到 {len(short_list)-1} 之間的數字。")
```

#### 💡 捕捉多種不同類規模的錯誤
我們可以使用多個 `except` 區塊，分別處理不同類型的錯誤，並用 `as` 取得錯誤訊息。
```python
short_list = [1, 2, 3]

while True:
    value = input('輸入索引值 (輸入 q 結束): ')
    if value == 'q':
        break
    try:
        position = int(value)          # 可能會拋出 ValueError (若輸入非數字字串)
        print(short_list[position])    # 可能會拋出 IndexError (若數字超出範圍)
    except IndexError as err:
        print("索引錯誤，此位置沒有元素！詳細訊息:", err)
    except ValueError as err:
        print("輸入格式錯誤，必須輸入整數！詳細訊息:", err)
    except Exception as other:
        # 捕捉所有其他未預期的錯誤
        print("發生其他未預期錯誤:", other)
```

---

### 8. 自訂例外類別與主動拋出錯誤 (Raise)

當我們需要建立專案特有的商務邏輯限制時，可以透過繼承 `Exception` 類別來建立自定義的例外，並使用 `raise` 關鍵字主動拋出它。

```python
# 1. 建立自訂的例外類別
class UppercaseException(Exception):
    pass

# 2. 測試主動拋出例外
words = ['apple', 'banana', 'ORANGE', 'grape']

try:
    for word in words:
        if word.isupper():
            # 當遇到大寫單字時，主動拋出我們自訂的例外
            raise UppercaseException(f"不允許大寫單字: {word}")
        print(f"處理單字: {word}")
except UppercaseException as exc:
    print(f"捕捉到自訂錯誤 -> {exc}")


### 9. 在函式（Function）內進行例外處理與傳遞

在設計函式時，錯誤與例外處理（`try...except`）的安排方式主要有以下三種模式：

#### 💡 模式一：函式內部自行處理例外 (Self-contained Handling)
函式內部自己包裝 `try...except`，當錯誤發生時在內部直接解決，不影響外部呼叫端的流程。這適合用於「容錯性高、有預設回傳值」的場景。

```python
def safe_divide(a, b):
    """安全除法，內部自行處理 ZeroDivisionError"""
    try:
        return a / b
    except ZeroDivisionError:
        print("【函式內部處理】錯誤：除數不能為零！")
        return None  # 發生錯誤時，回傳 None 作為安全值

# 呼叫測試
print(safe_divide(10, 2))  # 輸出: 5.0
print(safe_divide(10, 0))  # 輸出: None (程式不會崩潰，錯誤已在函式內部被消化)
```

---

#### 💡 模式二：例外的向上傳遞 (Exception Propagation)
如果函式內部**沒有**撰寫 `try...except`，當錯誤發生時，Python 會自動將例外「向上傳遞」給呼叫該函式的外層程式。外層程式可以使用 `try...except` 來捕捉並處理。

```python
def divide(a, b):
    """此函式內部不處理例外，若 b 為 0 會直接拋出 ZeroDivisionError"""
    return a / b

# 呼叫端（外部）處理例外
try:
    result = divide(10, 0)  # 呼叫時拋出錯誤，錯誤會傳遞到這裡
    print("計算結果:", result)
except ZeroDivisionError as err:
    print(f"【外部呼叫端捕捉】呼叫函式時發生錯誤: {err}")
```

---

#### 💡 模式三：函式內捕捉後重新拋出 (Re-raising Exceptions)
有時我們希望在函式內部「先進行部分處理」（例如記錄日誌、釋放資源），但依然希望將錯誤丟回給呼叫端處理。此時可以在 `except` 區塊中使用不帶任何參數的 `raise` 關鍵字，將原本的例外重新拋出。

```python
def get_user_age(user_data, user_id):
    try:
        return user_data[user_id]
    except KeyError as err:
        print(f"【系統日誌】嘗試讀取不存在的鍵: {user_id}")
        raise  # 重新拋出剛才捕捉到的 KeyError，讓呼叫端決定如何應對

# 測試資料
user_db = {"Alice": 25, "Bob": 30}

try:
    age = get_user_age(user_db, "Charlie")
except KeyError:
    print("【外部處理】找不到該使用者，請確認帳號是否輸入正確。")
```




