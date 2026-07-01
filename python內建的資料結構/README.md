# Python 內建資料結構完整指南

Python 提供了四種功能強大的內建資料結構，用於組織、管理和操作資料。掌握這些資料結構的特性與適用場景，是編寫高效且優雅程式碼的關鍵。

---

## 1. 內建資料結構特性比較

在開始之前，我們先通過這張表了解四大資料結構的核心特性對比：

| 特性 | List (列表) | Tuple (元組) | Dictionary (字典) | Set (集合) |
| :--- | :--- | :--- | :--- | :--- |
| **宣告語法** | 中括號 `[]` | 小括號 `()` | 大括號 `{key: value}` | `set()` 或 大括號 `{val}` |
| **可變性 (Mutable)** | 可變 | **不可變** | 可變 | 可變 |
| **有序性 (Ordered)** | 有序 | 有序 | 無序 (3.7+ 保留插入順序) | 無序 |
| **重複元素** | 允許 | 允許 | **鍵 (Key) 不可重複**，值可重複 | **不允許** |
| **索引存取** | 支援 | 支援 | 不支援索引，改以 **Key** 存取 | 不支援 |

---

## 2. List (列表)

List 是 Python 中最通用的資料結構。它是有序且可變的集合，能動態增刪，並且可容納不同資料型別。

### 2.1 建立 List
```python
# 1. 基本宣告
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_data = [1, 'Python', 3.14, True]  # 支援不同型別

# 2. 使用 list() 函數與生成器轉換
string_to_list = list('Python')    # 輸出: ['P', 'y', 't', 'h', 'o', 'n']
range_to_list = list(range(1, 6))  # 輸出: [1, 2, 3, 4, 5]
tuple_to_list = list(('a', 'b'))   # 輸出: ['a', 'b']
```

### 2.2 索引與切片
List 的索引與切片操作方式與字串完全一致：
```python
cities = ['台北', '台中', '高雄', '台南']

print(cities[0])   # 正向首元素: '台北'
print(cities[-1])  # 反向尾元素: '台南'

# 切片操作 [start:end:step]
data = ['a', 'b', 'c', 'd', 'e']
print(data[1:4])   # 輸出: ['b', 'c', 'd'] (不包含 index 4)
print(data[::-1])  # 列表反轉: ['e', 'd', 'c', 'b', 'a']
```

### 2.3 List 常見操作方法
```python
fruits = ['蘋果', '香蕉']

# append() - 尾端追加單一元素
fruits.append('橘子')  # ['蘋果', '香蕉', '橘子']

# extend() - 尾端合併另一個序列的所有元素
fruits.extend(['葡萄', '奇異果'])  # ['蘋果', '香蕉', '橘子', '葡萄', '奇異果']

# insert() - 在指定索引處插入元素
fruits.insert(1, '芒果')  # ['蘋果', '芒果', '香蕉', '橘子', '葡萄', '奇異果']

# 修改元素
fruits[0] = '紅蘋果'  # ['紅蘋果', '芒果', '香蕉', '橘子', '葡萄', '奇異果']

# 刪除元素
fruits.remove('香蕉')  # 依值移除第一個匹配項
popped_item = fruits.pop(2)  # 移除並回傳索引為 2 的元素 ('橘子')
print(fruits)  # ['紅蘋果', '芒果', '葡萄', '奇異果']
```

### 2.4 排序與反轉
```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - 原地排序 (改變原列表)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# sorted() - 回傳一個排序後的「新列表」 (原列表不變)
original = [5, 2, 8]
new_list = sorted(original)
print(original)  # [5, 2, 8]
print(new_list)  # [2, 5, 8]
```

### 2.5 二維列表 (巢狀列表)
常用於表示矩陣或表格式資料。
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 輸出: 6 (第二列第三行)
```

---

## 3. Tuple (元組)

Tuple 是不可變（Immutable）的有序資料結構。一旦建立，就不能新增、刪除或修改其中的元素。

### 3.1 建立 Tuple
```python
empty_tuple = ()
single_item = ('蘋果',)  # ⚠️ 注意：單一元素的 Tuple 後方必須加上逗號！
coordinates = (10.0, 20.0)

# 使用 tuple() 轉型
list_to_tuple = tuple([1, 2, 3])  # 輸出: (1, 2, 3)
```

### 3.2 Tuple 的解包 (Unpacking)
將 Tuple 內的元素快速拆解並指派給多個變數。
```python
point = (100, 200)
x, y = point
print(f"X軸: {x}, Y軸: {y}")  # X軸: 100, Y軸: 200

# 應用：極簡變數交換
a, b = 10, 20
a, b = b, a  # 交換
print(a, b)  # 輸出: 20, 10
```

### 3.3 為什麼需要 Tuple？
1. **安全保護**：防止程式無意中修改敏感資料（如 API 金鑰、配置、座標）。
2. **效能優勢**：由於結構不可變，Python 核心對 Tuple 的記憶體分配更為優化，執行效率比 List 高。
3. **可作為字典的 Key**：不可變的屬性使 Tuple 可以作為 Dictionary 的鍵，而 List 則不行。

---

## 4. Dictionary (字典)

Dictionary 是一種鍵值對（Key-Value Pair）的無序映射結構。每個鍵（Key）必須是唯一的且不可變，值（Value）則可以為任意型別。

### 4.1 建立 Dictionary
```python
# 1. 基礎宣告
student = {
    'name': '愛麗絲',
    'age': 20,
    'grade': 'A'
}

# 2. 用 dict() 連接成字典
keys = ['name', 'age']
values = ['鮑伯', 25]
person = dict(zip(keys, values))  # {'name': '鮑伯', 'age': 25}
```

### 4.2 存取、修改與防錯
```python
info = {'name': '卡蘿', 'age': 30}

# 1. 存取值
print(info['name'])  # '卡蘿'

# ⚠️ 注意：如果 key 不存在，直接用中括號存取會引發 KeyError！
# print(info['phone'])  # KeyError

# 2. 安全存取：使用 get() 提供預設值避免當機
print(info.get('phone', '無此聯絡電話'))  # 輸出: '無此聯絡電話'

# 3. 新增與修改
info['age'] = 31              # 修改既有鍵值
info['email'] = 'test@mail.com' # 新增全新鍵值對
```

### 4.3 遍歷與字典方法
```python
scores = {'國文': 85, '數學': 92, '英文': 78}

# 1. 遍歷鍵與值 (.items())
for subject, score in scores.items():
    print(f"科目: {subject}, 分數: {score}")

# 2. 獲取所有 Key 或 Value
print(list(scores.keys()))    # ['國文', '數學', '英文']
print(list(scores.values()))  # [85, 92, 78]
```

---

## 5. Set (集合)

Set 是一個不重複元素的無序集合。常用於去除重複資料、快速成員判定，以及數學集合運算（交集、聯集、差集）。

### 5.1 建立 Set
```python
# ⚠️ 注意：{} 代表空字典，建立空集合必須使用 set()
empty_set = set() 
numbers = {1, 2, 3, 3, 4}  # 重複元素會自動被過濾
print(numbers)  # 輸出: {1, 2, 3, 4}
```

### 5.2 集合的常用操作
```python
fruits = {'蘋果', '香蕉'}

# 新增
fruits.add('橘子')

# 移除 (discard 不會因為元素不存在而報錯，比 remove 更安全)
fruits.discard('西瓜')  # 不會出錯
fruits.discard('香蕉')

# 成員判定
print('蘋果' in fruits)  # 輸出: True
```

### 5.3 數學集合運算 (實戰精華)
```python
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# 1. 交集 (Intersection) - 兩邊都有
print(setA & setB)  # 輸出: {4, 5}

# 2. 聯集 (Union) - 合併所有
print(setA | setB)  # 輸出: {1, 2, 3, 4, 5, 6, 7, 8}

# 3. 差集 (Difference) - A 有但 B 沒有
print(setA - setB)  # 輸出: {1, 2, 3}

# 4. 對稱差集 - 兩邊不重複的元素
print(setA ^ setB)  # 輸出: {1, 2, 3, 6, 7, 8}
```

---

## 6. 資料結構的效能比較與選擇指南

### 6.1 時間複雜度對比

| 操作 | List (列表) | Tuple (元組) | Dictionary (字典) | Set (集合) |
| :--- | :---: | :---: | :---: | :---: |
| **依索引取值** | $O(1)$ | $O(1)$ | - | - |
| **搜尋特定元素** | $O(n)$ | $O(n)$ | $O(1)$ (極快) | $O(1)$ (極快) |
| **插入/新增元素** | $O(n)$ (尾端為 $O(1)$) | - | $O(1)$ | $O(1)$ |
| **刪除特定元素** | $O(n)$ | - | $O(1)$ | $O(1)$ |

### 6.2 實用選擇心法
* **選擇 `List`**：當您需要「保留資料插入順序」、允許重複、且後續需要依索引編號定位存取時。
* **選擇 `Tuple`**：當您的資料一旦產生便「不需要修改」（例如資料庫唯讀紀錄、座標點、系統配置），需要安全防寫時。
* **選擇 `Dictionary`**：當您需要「將鍵對應到值」（如商品名對照價格、學生學號對照資料），且需要極速搜尋時。
* **選擇 `Set`**：當您需要對一整批資料「進行去重（過濾重複）」，或需要比對兩批資料的交集、聯集時。

---

## 7. 常見錯誤與最佳實踐

### 7.1 修改遍歷中的 List (常見錯誤 ❌)
在 `for` 迴圈中直接刪除目前正在迭代的列表元素，會打亂索引機制，導致漏掉部分元素或引發錯誤。
```python
# ❌ 錯誤做法
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 會造成列表索引位移，漏掉檢查！

#  正確做法：使用列表推導式建立新列表
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

### 7.2 淺複製 (Shallow Copy) 問題 (常見錯誤 ❌)
```python
# ❌ 錯誤做法：直接指派給新變數
original = [1, 2, 3]
copied = original      # 這只是建立了「引用」，雙方指向同一個物件
copied[0] = 99
print(original)        # 輸出: [99, 2, 3] (原列表被意外更改了！)

#  正確做法：使用 copy()
original = [1, 2, 3]
copied = original.copy()
copied[0] = 99
print(original)        # 輸出: [1, 2, 3] (原列表完好無損)
```

### 7.3 實用最佳實踐
* **使用 `enumerate()` 同時獲取索引與值**：
```python
for index, value in enumerate(['蘋果', '香蕉']):
    print(f"索引 {index} 是 {value}")
```
* **使用 `zip()` 同時遍歷多個序列**：
```python
names = ['愛麗絲', '鮑伯']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} 今年 {age} 歲")
```