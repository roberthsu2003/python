# 函數的參數和引數的介紹


## List 的傳送與接收（參數傳遞機制）

在 Python 中，將 List 作為參數傳遞給函式時，傳遞的是**物件的參照（Reference）**。這意味著函式內外指向的是同一個記憶體位址的 List。

根據在函式內部的操作方式，會產生兩種不同的結果：
1. **修改既有 List（In-place Modification）**：若使用索引修改元素，或使用 `append()`、`extend()`、`insert()`、`pop()` 等方法，會直接修改原始 List，記憶體位址不變。
2. **重新指派（Reassignment）**：若在函式內使用 `=` 將參數指派給一個新的 List 物件，則該參數會指向新的記憶體位址，而原始的 List 則不會受到任何影響。

---

#### 💡 操作範例 1：修改既有元素 (In-place)
在函式內透過索引值修改 List 的內容。
```python
# fun4.py
def changeme(mylist): 
    print("函式內修改前 id:", id(mylist)) 
    mylist[2] = 'a'  # 修改既有元素
    print("函式內修改後 id:", id(mylist)) 
    print("函式內內容:", mylist) 
    return

mylist = [10, 20, 30] 
print("原始 id:", id(mylist))
changeme(mylist)
print("執行完函式後的內容:", mylist)  # 內容已被修改，id 保持一致
```

#### 💡 操作範例 2：重新指派 (Reassignment)
在函式內使用 `=` 重新指派一個新的 List。
```python
# fun4-1.py
def changeme(mylist): 
    print("函式內指派前 id:", id(mylist)) 
    mylist = [1, 2, 3, 4]  # 重新指派新物件，mylist 變數轉向新位址
    print("函式內指派後 id:", id(mylist)) 
    print("函式內內容:", mylist) 
    return

mylist = [10, 20, 30] 
print("原始 id:", id(mylist))
changeme(mylist)
print("執行完函式後的內容:", mylist)  # 原始 List 未受影響
```

#### 💡 操作範例 3：使用方法修改 (In-place)
在函式內使用 `append()` 方法新增元素。
```python
# fun4-2.py
def changeme(mylist): 
    print("函式內修改前 id:", id(mylist)) 
    mylist.append([1, 2])  # 於尾端新增子 List
    print("函式內修改後 id:", id(mylist)) 
    print("函式內內容:", mylist) 
    return

mylist = [10, 20] 
print("原始 id:", id(mylist))
changeme(mylist)
print("執行完函式後的內容:", mylist)  # 內容已被修改，id 保持一致
```

---

## List 運算子行為：`+=` 與 `+` 的差異

對於可變物件（如 List）而言，`+=` 與 `+` 運算子有著本質上的不同：
* **`+` 運算子**：會將兩個 List 合併並**建立一個全新**的 List 物件，然後重新指派。
* **`+=` 運算子**：在 List 上相當於呼叫 `extend()` 方法，屬於**就地修改（In-place）**，不會改變原有的記憶體位址。

> [!NOTE]
> 對於 List 而言：
> `x = x + [89, 99]` 會產生新物件（id 改變）。
> `x += [89, 99]` 則是在原物件上追加元素（id 不變）。

#### 💡 操作範例 4：使用 `+` 運算子（建立新物件）
```python
# list-add1.py
x = y = [0, 1, 2] 
print("初始 x, y:", x, y) 
print("初始 id:", id(x), id(y)) 

x = x + [89, 99]  # 建立新 List 並指派給 x，此時 x 與 y 指向不同物件
print("運算後 x, y:", x, y) 
print("運算後 id:", id(x), id(y)) 
print("x is y:", x is y)  # 輸出 False
```

#### 💡 操作範例 5：使用 `+=` 運算子（就地修改）
```python
# list-add2.py
a = b = [0, 1, 2]
print("初始 a, b:", a, b) 
print("初始 id:", id(a), id(b)) 

a += [89, 99]  # 就地修改 a 指向的 List，此時 a 與 b 仍指向同一個物件
print("運算後 a, b:", a, b) 
print("運算後 id:", id(a), id(b)) 
print("a is b:", a is b)  # 輸出 True
```

---

## List 的切片取值與固定間隔 (Slicing)

Python 的切片語法為 `list[start:stop:step]`，其中第三個參數 `step` 代表**固定間隔（步長）**。
* `step` 為正數時，表示由左向右提取。
* `step` 為負數時，表示由右向左提取（常用於反轉 List）。

#### 💡 操作範例 6：多種步長切片範例
```python
# list-try.py
x = range(100)  # 產生 0 到 99 的序列

# 1. 反轉序列
for i in x[::-1]:
    print(i)

# 2. 每隔 2 個元素取一個 (偶數)
for i in x[::2]:
    print(i)

# 3. 每隔 3 個元素取一個
for i in x[::3]: 
    print(i)
	
# 4. 指定範圍 (索引 10 到 39) 且每隔 6 個元素取一個
for i in x[10:40:6]:
    print(i)
```


## 說明文件 (Docstrings)

在 Python 中，寫在函式定義內第一行的字串，被稱為 **說明文件（Docstrings）**。其目的是為函式提供一份結構清晰的「使用手冊」，說明函式的作用、參數格式及回傳值。

好的 Docstring 可以透過三個雙引號 `"""` 來撰寫多行內容，這是 Python 的最佳實踐之一。

### 💡 範例：標準的 Docstring 寫法
```python
def calculate_triangle_area(base, height):
    """
    計算直角三角形的面積。
    
    參數:
    base (float): 三角形的底邊長度 (公分)
    height (float): 三角形的高 (公分)
    
    回傳:
    float: 計算出的三角形面積 (平方公分)
    """
    return (base * height) / 2
```

### 💡 如何讀取說明文件？
我們可以使用兩種常見的方式來查閱函式的說明文件：

- **方法一：特殊屬性 `__doc__`**
  直接在程式碼中存取並印出函式的 `__doc__` 屬性。
  ```python
  print(calculate_triangle_area.__doc__)
  ```

- **方法二：內建函式 `help()`**
  在開發或互動式環境中，使用 `help()` 查詢函式的使用說明。
  ```python
  help(calculate_triangle_area)
  ```
 
**預期輸出：**
  
  ```text
  Help on function calculate_triangle_area in module __main__:

  calculate_triangle_area(base, height)
      計算直角三角形的面積。
      
      參數:
      base (float): 三角形的底邊長度 (公分)
      height (float): 三角形的高 (公分)
      
      回傳:
      float: 計算出的三角形面積 (平方公分)
  ```
  
[進階範例](./practice3.md)  

## 函式的引數呼叫與參數設定

當我們定義函式（宣告「參數」）並呼叫它（傳入「引數」）時，Python 提供了多種靈活的傳遞方式。學會如何閱讀函式定義的「說明書」，是寫出乾淨、好讀程式碼的關鍵。

---

### 1. 位置引數與關鍵字引數

在呼叫函式傳入值時，常見有兩種傳參方式：
- **位置引數呼叫 (Positional Arguments)**：依照參數定義的「順序」傳遞。
- **關鍵字（名稱）引數呼叫 (Keyword Arguments)**：明確指定「參數名稱 = 值」，可以不按順序傳遞。

#### 💡 示範函式：菜單選擇
```python
def make_menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
```

#### 💡 呼叫方式一：位置引數呼叫 (Positional)
完全依靠參數的位置順序來傳遞。
```python
# '白酒' 傳給 wine, '牛排' 傳給 entree, '蛋糕' 傳給 dessert
print(make_menu('白酒', '牛排', '蛋糕'))
# 輸出: {'wine': '白酒', 'entree': '牛排', 'dessert': '蛋糕'}
```

#### 💡 呼叫方式二：關鍵字引數呼叫 (Keyword)
明確指定參數名稱，順序可任意打亂，這讓程式碼的意圖非常清楚。
```python
print(make_menu(entree='牛排', dessert='冰淇淋', wine='白酒'))
# 輸出: {'wine': '白酒', 'entree': '牛排', 'dessert': '冰淇淋'}
```

#### 💡 呼叫方式三：混合呼叫 (Mixed)
我們也可以同時混用位置與關鍵字引數。
- **⚠️ 鐵律**：**位置引數必須全部排在關鍵字引數的前面！** 一旦在呼叫時使用了關鍵字引數，後面所有的引數就都必須是關鍵字引數。
```python
# 正確寫法：前兩個是位置，最後一個是關鍵字
print(make_menu('紅酒', '雞排', dessert='蛋糕'))

# ❌ 錯誤寫法 (會拋出 SyntaxError: positional argument follows keyword argument)
# print(make_menu(wine='紅酒', '雞排', '蛋糕')) 
```

---

### 2. 參數預設值 (Default Arguments)

我們可以在定義函式時，為部分參數設定預設值。當呼叫者沒有傳入這些引數時，程式會自動使用預設值。

- **⚠️ 限制**：**沒有設定預設值的參數（必填參數），必須排在有預設值參數的前面！**

```python
# dessert 預設為 '奶昔'
def make_menu_default(wine, entree, dessert='奶昔'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 1. 省略有預設值的引數
print(make_menu_default('紅酒', '雞排'))
# 輸出: {'wine': '紅酒', 'entree': '雞排', 'dessert': '奶昔'}

# 2. 傳入新的值覆蓋預設值
print(make_menu_default('紅酒', '雞排', '蛋糕'))
# 輸出: {'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}
```

#### ⚠️ 經典陷阱：不要將「可變物件」（如空列表 `[]`）設為預設值！
在 Python 中，函式的預設值物件是在**函式被定義（載入）時就建立的**，且只會被建立一次。如果使用可變物件（如 list）作為預設值，每次呼叫都會共用同一個 list，產生意想不到的錯誤。

- **❌ 錯誤示範（Buggy）**：
  ```python
  def buggy(arg, result=[]):  # 共用同一個 list 實體
      result.append(arg)
      return result

  print(buggy('a'))  # 輸出: ['a']
  print(buggy('b'))  # 輸出: ['a', 'b'] (非預期的累積！)
  ```

- **✅ 正確示範（Non-buggy）**：
  使用 `None` 作為預設值，並在函式內部動態建立新的空列表。
  ```python
  def non_buggy(arg, result=None):
      if result is None:
          result = []  # 每次呼叫時，動態建立一個全新的空列表
      result.append(arg)
      return result

  print(non_buggy('a'))  # 輸出: ['a']
  print(non_buggy('b'))  # 輸出: ['b'] (正常運作！)
  ```

---

### 3. 進階參數控制：僅限位置與僅限關鍵字參數（`/` 與 `*`）

為了讓函式的使用說明書（介面）更嚴謹，Python 提供了特別的符號 `/` 與 `*` 來規範引數的傳遞方式：

- **`/`（左側僅限位置）**：在 `/` 左側的參數，**必須**使用位置引數傳入，**不能**使用名稱傳入。
- **`*`（右側僅限關鍵字）**：在 `*` 右側的參數，**必須**使用關鍵字引數傳入，**不能**使用位置傳入。

#### 💡 語法範例
```python
def configure_user(name, age, /, country="台灣", *, role="Member", debug=False):
    """
    name, age     -> 位於 / 左側，必須是位置引數。
    country       -> 夾在 / 與 * 之間，可使用位置或關鍵字傳遞。
    role, debug   -> 位於 * 右側，必須是關鍵字引數。
    """
    print(f"User: {name}, Age: {age}, Country: {country}, Role: {role}, Debug: {debug}")
```

#### 💡 測試呼叫
```python
# 1. 正確呼叫
configure_user("Alice", 25, "日本", role="Admin", debug=True)

# 2. ❌ 錯誤：對 name 或 age 使用關鍵字傳遞 (拋出 TypeError)
# configure_user(name="Alice", age=25, role="Admin")

# 3. ❌ 錯誤：對 role 使用位置傳遞 (拋出 TypeError)
# configure_user("Alice", 25, "日本", "Admin")
```

[進階範例](./practice4.md)

---

### 4. 接收不定數量的引數：`*args` 與 `**kwargs`

當我們不確定使用者會傳入多少個引數時，可以使用星號標記來自動接收並打包：
- **`*args` (位置參數打包)**：收集多餘的位置引數，並打包成一個 **Tuple**。
- **`**kwargs` (關鍵字參數打包)**：收集多餘的關鍵字引數，並打包成一個 **Dictionary**。

#### 💡 操作範例：`*args` 接收任意數量的位置引數
```python
def print_args(required_item, *args):
    print("必填項目:", required_item)
    print("其他位置引數 Tuple:", args)

print_args("外套", "圍巾", "手套", "帽子")
# 輸出:
# 必填項目: 外套
# 其他位置引數 Tuple: ('圍巾', '手套', '帽子')
```

#### 💡 操作範例：`**kwargs` 接收任意數量的關鍵字引數
```python
def print_kwargs(**kwargs):
    print("關鍵字引數 Dictionary:", kwargs)

print_kwargs(wine='紅酒', entree='牛排', dessert='蛋糕')
# 輸出:
# 關鍵字引數 Dictionary: {'wine': '紅酒', 'entree': '牛排', 'dessert': '蛋糕'}
```

[進階練習](./practice5.md)

---

### 5. 呼叫時的引數解包 (Unpacking)

如果在呼叫函式時使用 `*` 或 `**`，其作用與定義時**剛好相反**：它是將現有的 Tuple / List 或 Dictionary **解開**，再一個一個傳入函式中。

#### 💡 tuple/list 解包 (`*`)
```python
def calc_sum(a, b, c):
    return a + b + c

numbers = (10, 20, 30)

# 使用 * 解開 tuple，等同於傳入 calc_sum(10, 20, 30)
result = calc_sum(*numbers)
print("解包計算結果:", result)  # 輸出: 60
```

#### 💡 dict 解包 (`**`)
```python
def person_info(name, age, city):
    print(f"姓名: {name}, 年齡: {age}, 城市: {city}")

info = {"name": "Jack", "age": 24, "city": "台北"}

# 使用 ** 解開字典，等同於傳入 person_info(name="Jack", age=24, city="台北")
person_info(**info)

```

#### 範例1

```python
# 目標
# 建立python的自訂function,讓學生了解什麼是
# 引數位置呼叫 (Positional Arguments)
# 引數名稱呼叫 (Keyword Arguments)  
# 混合呼叫 (Mixed Arguments)

# 定義一個示範函數
def introduce_person(name, age, city="台北", hobby="閱讀"):
    """
    介紹一個人的基本資訊
    
    參數:
    name: 姓名 (必需參數)
    age: 年齡 (必需參數)
    city: 居住城市 (預設值: "台北")
    hobby: 興趣 (預設值: "閱讀")
    """
    return f"大家好，我是{name}，今年{age}歲，住在{city}，我喜歡{hobby}。"

print("=== 1. 引數值呼叫 (Positional Arguments) ===")
print("按照參數定義的順序傳遞值")
result1 = introduce_person("小明", 25, "台中", "游泳")
print(result1)
print()

print("=== 2. 引數名稱呼叫 (Keyword Arguments) ===")  
print("使用參數名稱來指定值，順序可以不同")
result2 = introduce_person(hobby="畫畫", city="高雄", age=30, name="小華")
print(result2)
print()

print("=== 3. 混合呼叫 (Mixed Arguments) ===")
print("位置參數必須在前，關鍵字參數在後")
result3 = introduce_person("小美", 28, hobby="旅遊")  # name, age用位置參數，hobby用關鍵字參數
print(result3)
print()
```

[進階練習](./practice1.md)

#### 範例2

```python
def calculate_total(price, quantity, discount=0, tax_rate=0.05):
    """
    計算商品總價
    
    參數:
    price: 單價
    quantity: 數量  
    discount: 折扣金額 (預設值: 0)
    tax_rate: 稅率 (預設值: 0.05)
    """
    subtotal = price * quantity - discount
    total = subtotal * (1 + tax_rate)
    return total

print("=== 購物計算範例 ===")
print("1. 引數值呼叫:")
total1 = calculate_total(100, 3, 50, 0.1)
print(f"總價: ${total1:.2f}")

print("\n2. 引數名稱呼叫:")
total2 = calculate_total(tax_rate=0.08, discount=20, quantity=2, price=150)
print(f"總價: ${total2:.2f}")

print("\n3. 混合呼叫:")
total3 = calculate_total(120, 4, tax_rate=0.07)  # price, quantity用位置參數
print(f"總價: ${total3:.2f}")
```

[進階練習](./practice2.md)



