# 模組與套件 (Modules and Packages)

在開發規模較大的 Python 專案時，將所有的程式碼寫在同一個檔案中會使程式碼難以維護。Python 提供了**模組（Module）**與**套件（Package）**的機制，讓程式碼能夠依據功能進行模組化拆分與重用。

---

## 1. 使用與匯入模組 (Importing Modules)

在 Python 中，**一個 `.py` 檔案就是一個模組**，模組的名稱就是該檔案的名稱（不含副檔名）。

### 📌 匯入模組的四種語法

| 匯入方式 | 說明 | 呼叫方式 |
| :--- | :--- | :--- |
| `import 模組` | 載入整份模組。最安全，不會發生命名衝突。 | `模組.方法()` |
| `import 模組 as 簡寫` | 載入整份模組，並為其設定一個簡短的別名（Alias）。 | `簡寫.方法()` |
| `from 模組 import 成員` | 只載入模組中的特定函式、類別或變數。 | `成員()` (直接呼叫) |
| `from 模組 import *` | 載入該模組內所有的公開成員。**⚠️ 不建議使用**，極易造成命名衝突。 | `成員()` (直接呼叫) |

---

### 2. 常用內建功能與模組範例

以內建的 `random`（隨機數）與 `math`（數學）模組為例，展示如何匯入並使用它們：

#### 💡 隨機數模組 `random` 範例 (rand_demo.py)
```python
import random

# 1. 隨機整數: 產生 0 到 100 之間(包含100)的整數
rand_int = random.randint(0, 100)
print(f"隨機整數 (0~100): {rand_int}")

# 2. 隨機偶數: 產生 0 到 100 之間的偶數 (指定間隔為 2)
rand_even = random.randrange(0, 101, 2)
print(f"隨機偶數 (0~100): {rand_even}")

# 3. 隨機浮點數: 產生 0.0 到 1.0 之間的隨機小數
rand_float = random.random()
print(f"隨機浮點數 (0~1): {rand_float}")

# 4. 隨機選取特定數量的字元
sample_chars = random.sample('abcdefghij', 3)
print(f"隨機選取 3 個字元: {sample_chars}")

# 5. 從清單中隨機選取一個元素
fruits = ['apple', 'pear', 'peach', 'orange', 'lemon']
selected_fruit = random.choice(fruits)
print(f"隨機選取水果: {selected_fruit}")

# 6. 重新隨機洗牌清單
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
```

#### 💡 數學模組 `math` 範例
```python
import math

x = 80.456

# 1. 平方根 (x 必須大於 0)
print("平方根:", math.sqrt(64))  # 輸出: 8.0

# 2. 次方運算 (2的3次方)
print("2的3次方:", math.pow(2, 3))  # 輸出: 8.0

# 3. 無條件進位 (ceil): 取得不小於 x 的最小整數
print("math.ceil(80.456) =", math.ceil(x))  # 輸出: 81

# 4. 無條件捨去 (floor): 取得確認不大於 x 的最大整數
print("math.floor(80.456) =", math.floor(x))  # 輸出: 80

# 5. 四捨五入 (注意: round 是 Python 內建函式，不用引用 math)
print("round(80.456, 2) =", round(x, 2))  # 輸出: 80.46
```

---

## 3. 建立自訂模組

在同一個目錄下，我們可以建立多個 `.py` 檔案，彼此之間可以互相 import 引用。

#### 💡 步驟一：建立自訂模組 `report.py`
這個模組專注於提供氣象描述的功能。
```python
# report.py
import random

def get_description():
    """隨機回傳今日氣象預報"""
    possibilities = ['晴天', '雨天', '下雪', '起霧', '陰天', '天曉得']
    return random.choice(possibilities)
```

#### 💡 步驟二：建立主程式 `weatherman.py` 載入並使用該模組
```python
# weatherman.py
import report  # 載入我們自訂的 report 模組

def main():
    # 呼叫自訂模組中的函式
    description = report.get_description()
    print("今日天氣預報:", description)

if __name__ == '__main__':
    main()
```
當我們在終端機執行 `python weatherman.py` 時，程式會順利印出今日的天氣。

---

## 4. 命令列引數與搜尋路徑

### 命令列引數 (Command-Line Arguments)
當我們在終端機啟動 Python 腳本時，可以附帶傳入額外的參數。這些參數會被自動收集至內建 `sys` 模組的 `sys.argv` 列表中（第一個元素預設為該主程式的檔案路徑）。

#### 💡 範例：收集命令列參數 (args_demo.py)
```python
# args_demo.py
import sys

# sys.argv 是一個 list
print("所有傳入的引數列表:", sys.argv)
```
- **執行測試**：
  ```bash
  $ python args_demo.py apple banana 123
  所有傳入的引數列表: ['args_demo.py', 'apple', 'banana', '123']
  ```

### 模組搜尋路徑 (Module Search Path)
當你執行 `import xxx` 時，Python 會依序在 `sys.path` 列表定義的目錄中尋找該模組。如果找不到，就會拋出 `ModuleNotFoundError`。
```python
import sys

# 印出 Python 搜尋模組的順序目錄
for path in sys.path:
    print(path)
```
> **💡 搜尋順序**：首先會從「目前工作目錄」開始找，接著找 Python 的標準函式庫目錄，最後找安裝第三方套件的 `site-packages` 目錄。

---

## 5. 自製套件 (Packages)

**套件（Package）就是一個包含了多個模組的「資料夾」**。利用套件，我們可以對模組進行二級目錄管理。

### 📌 建立套件的結構
假設我們要建立一個名為 `happy` 的套件，該套件內包含一個 `my_mod` 模組：
```text
專案目錄/
├── main.py (主程式)
└── happy/ (套件資料夾)
    ├── __init__.py (初始化檔案，可以是空白檔案)
    └── my_mod.py (子模組)
```

1. **`__init__.py`**：是用來宣告這個資料夾是 Python 套件的標誌性檔案。在 Python 3.3 之後可以省略，但為了向後相容與便於在檔案中加入套件層級的初始化代碼，建議依然建立它。
2. 撰寫 `happy/my_mod.py` 內容：
   ```python
   def happy_python():
       print("Happy Python!")
   ```

### 📌 呼叫套件內模組的語法

- **寫法一：完整路徑匯入**
  ```python
  import happy.my_mod
  happy.my_mod.happy_python()
  ```
- **寫法二：from-import 匯入**
  ```python
  from happy.my_mod import happy_python
  happy_python()
  ```

---

## 6. 進階套件管理

### 1. `__init__.py` 配合 `__all__` 的進階使用

在套件或模組的 `__init__.py` 中，我們可以使用特殊變數 `__all__` 列表，來定義「當外部執行 `from package import *` 時，有哪些成員可以被導出」。

```python
# mymodule.py

def spam():
    print("Spam!")

def grok():
    print("Grok!")

# 外部不可讀取此變數
secret_code = 9999

# 限定只導出 spam 與 grok
__all__ = ['spam', 'grok']
```

---

### 2. 使用相對路徑在套件內部互相 import

當套件內部的子模組需要互相引用時，可以使用**相對路徑**語法（`.` 代表當前目錄，`..` 代表上一級目錄）：

```text
mypackage/
├── __init__.py
├── A/
│   ├── __init__.py
│   ├── spam.py
│   └── grok.py
└── B/
    ├── __init__.py
    └── bar.py
```

- 在 `mypackage/A/spam.py` 中引用同目錄的 `grok.py`：
  ```python
  from . import grok
  ```
- 在 `mypackage/A/spam.py` 中引用相鄰目錄 `B/bar.py`：
  ```python
  from ..B import bar
  ```
> **⚠️ 限制**：相對路徑 `from . import` 只能在「被當作套件載入」時正常運作。如果直接執行 `python spam.py`，會因為該檔案被視為 `__main__` 找不到父套件而拋出 `ImportError` 錯誤。

---

### 3. 將大模組重構拆分成多個小檔案

當一個模組檔案太大時，我們可以將它轉化為「套件目錄」，並在 `__init__.py` 中匯入所有分散在小檔案的類別，對外保持一模一樣的載入介面，實現「對內拆分，對外統一」。

#### 💡 舊的單一檔案 `mymodule.py`：
```python
class A:
    def spam(self):
        print('A.spam')
    
class B:
    def bar(self):
        print('B.bar')
```

#### 💡 重構後的套件結構：
```text
mymodule/
├── __init__.py
├── a.py (存放類別 A)
└── b.py (存放類別 B)
```

1. **`mymodule/a.py`**：
   ```python
   class A:
       def spam(self):
           print('A.spam')
   ```
2. **`mymodule/b.py`**：
   ```python
   class B:
       def bar(self):
           print('B.bar')
   ```
3. **`mymodule/__init__.py`**（核心：在這裡把分散的類別導入，對外合併）：
   ```python
   from .a import A
   from .b import B
   ```

#### 💡 外部使用者的呼叫方式（完全不受拆分影響，無痛升級）：
```python
import mymodule

obj_a = mymodule.A()
obj_a.spam()  # 輸出: A.spam

obj_b = mymodule.B()
obj_b.bar()   # 輸出: B.bar
```
