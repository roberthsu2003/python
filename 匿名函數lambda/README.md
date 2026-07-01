# 進階函式應用與匿名函數 (Lambda)

在 Python 中，函式不僅僅是執行程式碼的區塊，它更是一個獨立的物件。這使得 Python 支援許多進階的函式編程手法，例如將函式作為參數傳遞、在函式內部定義函式、使用閉包，以及編寫無名稱的「匿名函數（Lambda）」。

---

## 1. 函式是一等公民 (First-Class Citizens)

在 Python 中，「函式是一等公民」代表函式與整數、字串等一般物件擁有同等地位：
- 可以被指派給變數。
- 可以作為引數傳遞給另一個函式。
- 可以作為另一個函式的回傳值。

#### 💡 範例一：將函式指派給變數
```python
def answer():
    print(42)

# 將函式 answer 賦值給變數 run_func (注意此處不加括號)
run_func = answer

# 透過變數呼叫函式
run_func()  # 輸出: 42
```

#### 💡 範例二：將函式當作參數傳遞
```python
def run_something(func):
    func()  # 執行傳入的函式

run_something(answer)  # 輸出: 42
```

#### 💡 範例三：傳入帶有引數的函式
```python
def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)  # 輸出: 14
```

#### 💡 範例四：結合不定數量參數 (`*args`)
```python
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    # 將接收到的 args 解包後傳入目標函式
    return func(*args)

result = run_with_positional_args(sum_args, 1, 2, 3, 4)
print(result)  # 輸出: 10
```

### 💡 實戰生活主題範例：自動化報表產生器
> **為什麼此場景需要「函式作為參數」？**  
> 假設一個報表系統要先後執行「讀取資料 → 過濾資料 → 輸出結果」三個步驟。
> 將每個步驟包裝成函式，再透過一個「流水線」函式按序呼叫，
> 可以讓每個步驟自由抽換，不必改動主流程。
```python
def read_data():
    print("[步驟1] 從資料庫讀取學生成績...")
    return [88, 45, 92, 60, 33, 77]

def filter_pass(data):
    print("[步驟2] 過濾出及格 (≥60) 的成績...")
    return [s for s in data if s >= 60]

def output_result(data):
    print(f"[步驟3] 最終及格名單：{data}")

def run_pipeline(steps):
    """按序執行一連串步驟，並將上一步的回傳值傳入下一步"""
    result = steps[0]()          # 執行第一個步驟
    for step in steps[1:]:
        result = step(result)    # 每個步驟接收上一步的輸出

# 將三個步驟以「函式物件清單」傳入，隨時可以抽換任一步驟
run_pipeline([read_data, filter_pass, output_result])
```
##### 🖥️ 終端機預期輸出結果：
```text
[步驟1] 從資料庫讀取學生成績...
[步驟2] 過濾出及格 (≥60) 的成績...
[步驟3] 最終及格名單：[88, 92, 60, 77]
```

---

## 2. 內部函式 (Inner Functions) 與 閉包 (Closures)

### 內部函式
我們可以在一個函式的內部，定義另一個函式。內部函式可以用來封裝邏輯，避免外部直接存取。

```python
def outer(a, b):
    # 定義內部函式
    def inner(c, d):
        return c + d
    # 在內部呼叫並回傳結果
    return inner(a, b)

print(outer(4, 7))  # 輸出: 11
```

### 閉包 (Closures)
如果內部函式引用了外部函式的變數，且外部函式**將這個內部函式作為物件回傳**，此時就形成了一個「閉包（Closure）」。閉包可以「記住」它被建立時的外部環境狀態。

```python
def make_intro_speaker(saying):
    # 內部函式記住了外部傳入的變數 saying
    def speak(name):
        return f"{name} 說: '{saying}'"
    return speak  # 回傳函式物件，不加括號

# 建立兩個具有不同狀態的閉包
duck_speaker = make_intro_speaker("呱呱")
cat_speaker = make_intro_speaker("喵喵")

# 呼叫閉包
print(duck_speaker("唐老鴨"))  # 輸出: 唐老鴨 說: '呱呱'
print(cat_speaker("哆啦A夢"))  # 輸出: 哆啦A夢 說: '喵喵'
```

### 💡 實戰生活主題範例：購物網站折扣計算器
> **為什麼此場景需要閉包？**  
> 電商平台針對不同的會員等級（普通會員、VIP、黑卡會員）有不同的折扣率。
> 使用閉包，我們可以用「工廠函式」根據傳入的折扣率，
> 動態「製造」出各自專屬的計算函式，每個函式各自「記住」自己的折扣率，
> 而不需要每次呼叫都重複傳入折扣參數。
```python
def make_discount_calculator(discount_rate):
    """折扣計算器工廠：根據折扣率，產出一個專屬的計算函式"""
    def calculate(original_price):
        final_price = original_price * discount_rate
        saving = original_price - final_price
        print(f"  原價: ${original_price:.0f}  →  折扣後: ${final_price:.0f}  (省了 ${saving:.0f})")
        return final_price
    return calculate

# 為不同會員等級各自建立一個專屬的計算器（閉包）
member_calc   = make_discount_calculator(1.0)   # 普通會員：無折扣
vip_calc      = make_discount_calculator(0.9)   # VIP 會員：9 折
blackcard_calc = make_discount_calculator(0.75) # 黑卡會員：75 折

print("=== 購買一台 $12,000 的筆電 ===")
print("普通會員：")
member_calc(12000)
print("VIP 會員：")
vip_calc(12000)
print("黑卡會員：")
blackcard_calc(12000)
```
##### 🖥️ 終端機預期輸出結果：
```text
=== 購買一台 $12,000 的筆電 ===
普通會員：
  原價: $12000  →  折扣後: $12000  (省了 $0)
VIP 會員：
  原價: $12000  →  折扣後: $10800  (省了 $1200)
黑卡會員：
  原價: $12000  →  折扣後: $9000  (省了 $3000)
```

---

## 3. 匿名函數 (Lambda)

當我們需要一個臨時、簡單的函式，且該函式只會使用一次時，特別適合使用 **Lambda 匿名函數**，而不需要大費周章用 `def` 命名定義它。

#### 📌 核心規則：
1. **語法**：`lambda 參數1, 參數2, ... : 運算式`
2. **自動回傳**：Lambda 內部只有單一表達式，該表達式的計算結果會**自動回傳**，不需要（也不能）寫 `return`。
3. **功能局限**：Lambda 只能包含單一運算式，不能包含多行陳述式（如 `if-elif-else` 分支流程或 `while` 迴圈）。

#### 💡 傳統函式與 Lambda 的對比
```python
# 1. 傳統函式
def add(x, y):
    return x + y

# 2. 等同效果的 Lambda 匿名函數
lambda_add = lambda x, y: x + y

print(add(5, 3))        # 輸出: 8
print(lambda_add(5, 3)) # 輸出: 8
```

#### 💡 實用場景一：結合列表 (List) 儲存多個運算公式
由於 Lambda 是表達式，它可以出現在不允許出現 `def` 的地方，例如儲存在清單內：
```python
# 將不同的運算公式存入清單
calculators = [
    lambda x: x ** 2,  # 平方
    lambda x: x ** 3,  # 立方
    lambda x: x ** 4   # 四次方
]

# 依序使用不同的公式計算數值 3
for calc in calculators:
    print(calc(3))  # 依序輸出 9, 27, 81
```

#### 💡 實用場景二：結合條件表達式 (Ternary Operator)
雖然 Lambda 不能包含複雜的多行 `if` 分支，但可以使用單行條件表達式（`A if condition else B`）：
```python
# 找出兩數中的最小值
find_min = lambda x, y: x if x < y else y

print(find_min(50, 30))  # 輸出: 30
```

#### 💡 實用場景三：結合字典實現 Switch-Case 流程控制
```python
score = int(input('請輸入分數: '))
level = score // 10

# 利用字典對應不同 level 的 lambda 函式
actions = {
    10: lambda: print('極佳 (Perfect)'),
    9 : lambda: print('優等 (A)'),
    8 : lambda: print('甲等 (B)'),
    7 : lambda: print('乙等 (C)'),
    6 : lambda: print('丙等 (D)'),
}

# 取得對應的函式並執行，若低於 60 分則輸出 "不及格"
actions.get(level, lambda: print('不及格 (F)'))()
```

### 💡 實戰生活主題範例：商品清單客製化排序
> **為什麼此場景需要 Lambda？**  
> 電商平台的商品清單需要依照不同條件排序（最低價、評分最高、CP 值）。
> 每個排序條件只需一個簡單的取值規則，用 `def` 另外命名三個函式過於累贅。
> 搭配 `sorted()` 的 `key` 參數，Lambda 讓排序邏輯和呼叫寫在同一行，一目了然。
```python
products = [
    {"name": "藍牙耳機", "price": 1200, "rating": 4.5},
    {"name": "手機殼",   "price":  150, "rating": 4.8},
    {"name": "行動電源", "price":  890, "rating": 4.2},
    {"name": "充電線",   "price":   99, "rating": 4.6},
]

# 1. 依「價格」由低到高排序
by_price = sorted(products, key=lambda p: p["price"])
print("依價格排序（最便宜優先）：")
for p in by_price:
    print(f"  {p['name']:<8} ${p['price']}")

# 2. 依「評分」由高到低排序
by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)
print("\n依評分排序（最高分優先）：")
for p in by_rating:
    print(f"  {p['name']:<8} ★{p['rating']}")
```
##### 🖥️ 終端機預期輸出結果：
```text
依價格排序（最便宜優先）：
  充電線     $99
  手機殼     $150
  行動電源   $890
  藍牙耳機   $1200

依評分排序（最高分優先）：
  手機殼     ★4.8
  充電線     ★4.6
  藍牙耳機   ★4.5
  行動電源   ★4.2
```

---

## 4. 高階函式應用：`map()` 與 `filter()`

Lambda 最強大的應用場景，是做為參數傳遞給內建的高階函式如 `map()` 與 `filter()`。

### 1. map() 函式
- **用途**：將一個序列（如 list）中的每一個元素，逐一傳入指定的函式進行運算，並回傳包含所有運算結果的 map 物件（通常會再轉回 list 顯示）。
- **語法**：`map(function, sequence)`

```python
# 範例：將清單中的所有數字乘以 2

# 傳統做法（需要先定義一個函式）
def multiply2(x):
    return x * 2

result_def = list(map(multiply2, [1, 2, 3, 4]))
print("傳統函式 map:", result_def)  # 輸出: [2, 4, 6, 8]

# 使用 Lambda 的優雅做法（一行搞定，免命名）
result_lambda = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print("Lambda 搭配 map:", result_lambda)  # 輸出: [2, 4, 6, 8]
```
> **⚠️ 易混淆點對比**：
> 如果我們直接寫 `[1, 2, 3, 4] * 2`，在 Python 中代表「複製清單」，會得到 `[1, 2, 3, 4, 1, 2, 3, 4]`。
> 唯有透過 `map` 才能實現「將清單中的每個元素內部數值翻倍」。

#### 💡 進階技巧：處理複雜資料結構與多重清單
```python
# 從字典清單中，只取出所有的 points
students = [
    {'name': 'python', 'points': 10},
    {'name': 'java', 'points': 8}
]

points_list = list(map(lambda x: x['points'] * 10, students))
print("加權分數:", points_list)  # 輸出: [100, 80]

# 將兩個清單對應元素相加
list_a = [1, 2, 3]
list_b = [10, 20, 30]
sum_list = list(map(lambda x, y: x + y, list_a, list_b))
print("對應相加:", sum_list)  # 輸出: [11, 22, 33]
```

### 2. filter() 函式
- **用途**：將序列中的元素逐一傳入函式進行布林值判斷，只保留判斷結果為 `True` 的元素，過濾掉 `False` 的元素。
- **語法**：`filter(function, sequence)`

```python
# 範例一：過濾出清單中的所有偶數
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("過濾出偶數:", evens)  # 輸出: [2, 4, 6]

# 範例二：從字典清單中，過濾出名字為 'python' 的資料
dict_list = [
    {'name': 'python', 'points': 10},
    {'name': 'java', 'points': 8}
]
python_data = list(filter(lambda x: x['name'] == 'python', dict_list))
print("過濾出特定語系:", python_data)
# 輸出: [{'name': 'python', 'points': 10}]
```

### 💡 實戰生活主題範例：外送平台訂單處理系統
> **為什麼此場景需要 `map()` 與 `filter()`？**  
> 外送平台每天處理大量訂單：先用 `filter()` 篩選出「尚未完成」的訂單，
> 再用 `map()` 統一計算每筆訂單的「含運費總金額」。
> 相較於 `for` 迴圈配合 `if` 判斷，兩者搭配 Lambda 使程式碼更簡潔易讀。
```python
orders = [
    {"id": "A001", "item": "珍珠奶茶",   "price": 65,  "status": "completed"},
    {"id": "A002", "item": "牛肉麵",     "price": 180, "status": "pending"},
    {"id": "A003", "item": "雞排便當",   "price": 120, "status": "pending"},
    {"id": "A004", "item": "水果沙拉",   "price": 90,  "status": "completed"},
    {"id": "A005", "item": "手搖飲料組", "price": 210, "status": "pending"},
]

DELIVERY_FEE = 30  # 固定運費

# 步驟一：用 filter() 篩選出「待處理」的訂單
pending_orders = list(filter(lambda o: o["status"] == "pending", orders))

# 步驟二：用 map() 為每筆待處理訂單計算含運費的總金額
totals = list(map(
    lambda o: {"id": o["id"], "item": o["item"], "total": o["price"] + DELIVERY_FEE},
    pending_orders
))

print(f"待處理訂單共 {len(totals)} 筆（含 ${DELIVERY_FEE} 運費）：")
for t in totals:
    print(f"  [{t['id']}] {t['item']:<10} → 應付金額 ${t['total']}")
```
##### 🖥️ 終端機預期輸出結果：
```text
待處理訂單共 3 筆（含 $30 運費）：
  [A002] 牛肉麵      → 應付金額 $210
  [A003] 雞排便當    → 應付金額 $150
  [A005] 手搖飲料組  → 應付金額 $240
```
