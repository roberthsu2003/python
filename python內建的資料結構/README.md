# Python 內建資料結構完整指南

## 概述

Python 提供四種主要的內建資料結構，每種都有其特定的用途和特性：

- **List (列表)**: 有序、可變的資料集合
- **Tuple (元組)**: 有序、不可變的資料集合  
- **Dictionary (字典)**: 鍵值對的無序集合
- **Set (集合)**: 無序、不重複元素的集合

## 資料結構比較表

| 特性 | List | Tuple | Dictionary | Set |
|------|------|-------|------------|-----|
| 語法 | `[]` | `()` | `{}` | `set()` 或 `{}` |
| 可變性 | 可變 | 不可變 | 可變 | 可變 |
| 有序性 | 有序 | 有序 | 無序 (Python 3.7+保持插入順序) | 無序 |
| 重複元素 | 允許 | 允許 | Key不允許 | 不允許 |
| 索引存取 | 支援 | 支援 | 不支援 | 不支援 |

---

## 1. List (列表)

### 1.1 基本概念

List 是 Python 中最常用的資料結構，具有以下特性：

- **有序性**: 元素按照插入順序排列
- **可變性**: 可以動態增加、修改、刪除元素
- **異質性**: 可以儲存不同資料類型的元素
- **索引存取**: 支援正負索引存取

### 1.2 建立 List

```python
# 基本語法
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_data = [1, 'Python', 3.14, True]

# 使用 list() 函數
another_empty_list = list()
string_to_list = list('Python')  # ['P', 'y', 't', 'h', 'o', 'n']
range_to_list = list(range(1, 6))  # [1, 2, 3, 4, 5]

# 從其他資料結構轉換
tuple_to_list = list(('a', 'b', 'c'))  # ['a', 'b', 'c']
```

### 1.3 索引與切片

#### 索引存取
```python
cities = ['台北', '台中', '高雄', '台南']

# 正向索引 (從 0 開始)
print(cities[0])   # '台北'
print(cities[1])   # '台中'

# 負向索引 (從 -1 開始)
print(cities[-1])  # '台南'
print(cities[-2])  # '高雄'
```

#### 索引對照表
| 元素 | 台北 | 台中 | 高雄 | 台南 |
|------|------|------|------|------|
| 正向索引 | 0 | 1 | 2 | 3 |
| 負向索引 | -4 | -3 | -2 | -1 |

#### 切片操作
```python
data = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

print(data[2:])     # ['l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print(data[:3])     # ['H', 'e', 'l']
print(data[3:5])    # ['l', 'l']
print(data[::2])    # ['H', 'l', 'o', 'o', 'l']
print(data[::-1])   # ['d', 'l', 'r', 'o', 'W', 'o', 'l', 'l', 'e', 'H']
```

### 1.4 List 操作方法

#### 新增元素
```python
fruits = ['apple', 'banana']

# append() - 在末尾添加單一元素
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']

# extend() - 擴展多個元素
fruits.extend(['grape', 'kiwi'])
print(fruits)  # ['apple', 'banana', 'orange', 'grape', 'kiwi']

# insert() - 在指定位置插入元素
fruits.insert(1, 'mango')
print(fruits)  # ['apple', 'mango', 'banana', 'orange', 'grape', 'kiwi']

# 使用 + 運算符
more_fruits = fruits + ['pear', 'peach']
```

#### 修改元素
```python
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10      # 修改單一元素
numbers[1:3] = [20, 30]  # 修改多個元素
print(numbers)  # [10, 20, 30, 4, 5]
```

#### 刪除元素
```python
items = ['a', 'b', 'c', 'd', 'e']

# remove() - 根據值刪除第一個匹配的元素
items.remove('c')
print(items)  # ['a', 'b', 'd', 'e']

# pop() - 刪除並返回指定位置的元素
last_item = items.pop()      # 刪除最後一個元素
print(last_item)  # 'e'
second_item = items.pop(1)   # 刪除索引為1的元素
print(second_item)  # 'b'

# del - 刪除指定位置或切片
del items[0]        # 刪除第一個元素
del items[:]        # 清空列表
```

#### 查找與統計
```python
data = ['apple', 'banana', 'apple', 'orange', 'apple']

# index() - 查找元素的索引
print(data.index('banana'))  # 1

# count() - 統計元素出現次數
print(data.count('apple'))   # 3

# in 運算符 - 檢查元素是否存在
print('banana' in data)      # True
print('grape' in data)       # False
```

#### 排序與反轉
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - 原地排序
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - 返回新的排序列表
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (不變)
print(sorted_list)  # [1, 1, 3, 4, 5]

# reverse() - 反轉列表
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

### 1.5 二維列表
```python
# 建立二維列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 存取元素
print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6

# 實際應用範例
students_scores = [
    ['Alice', 85, 92, 78],
    ['Bob', 79, 85, 88],
    ['Charlie', 92, 88, 95]
]

for student in students_scores:
    name = student[0]
    scores = student[1:]
    average = sum(scores) / len(scores)
    print(f"{name}: 平均分數 {average:.1f}")
```

### 1.6 List 複製
```python
original = [1, 2, 3, 4, 5]

# 淺複製方法
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# 注意：直接賦值不是複製
reference = original  # 這只是創建引用，不是複製
original[0] = 100
print(reference)  # [100, 2, 3, 4, 5] - 會跟著改變
print(copy1)      # [1, 2, 3, 4, 5] - 不會改變
```

---

## 2. Tuple (元組)

### 2.1 基本概念

Tuple 是不可變的有序資料結構：

- **不可變性**: 一旦建立就無法修改
- **有序性**: 元素有固定的順序
- **效能優勢**: 比 List 更快
- **可作為字典的鍵**: 因為不可變

### 2.2 建立 Tuple

```python
# 基本語法
empty_tuple = ()
single_item = ('item',)  # 注意逗號
coordinates = (10, 20)
mixed_tuple = (1, 'hello', 3.14, True)

# 不使用括號（但建議使用）
point = 10, 20
colors = 'red', 'green', 'blue'

# 使用 tuple() 函數
list_to_tuple = tuple([1, 2, 3])
string_to_tuple = tuple('abc')  # ('a', 'b', 'c')
```

### 2.3 Tuple 操作

```python
data = ('apple', 'banana', 'cherry', 'date')

# 索引存取（與 List 相同）
print(data[0])   # 'apple'
print(data[-1])  # 'date'

# 切片操作
print(data[1:3])  # ('banana', 'cherry')

# 解包 (Unpacking)
fruits = ('apple', 'banana', 'cherry')
first, second, third = fruits
print(first)   # 'apple'
print(second)  # 'banana'

# 變數交換
a, b = 10, 20
a, b = b, a  # 交換值
print(a, b)  # 20, 10
```

### 2.4 Tuple 方法

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - 統計元素出現次數
print(numbers.count(2))  # 3

# index() - 查找元素索引
print(numbers.index(3))  # 2

# len() - 獲取長度
print(len(numbers))  # 7

# in 運算符
print(2 in numbers)  # True
```

---

## 3. Dictionary (字典)

### 3.1 基本概念

Dictionary 是鍵值對的集合：

- **鍵值對結構**: 每個元素都是 key:value 的形式
- **鍵的唯一性**: 每個鍵只能出現一次
- **可變性**: 可以動態增加、修改、刪除鍵值對
- **快速查找**: 基於哈希表實現，查找效率高

### 3.2 建立 Dictionary

```python
# 基本語法
empty_dict = {}
student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}

# 使用 dict() 函數
dict_from_list = dict([('a', 1), ('b', 2), ('c', 3)])
dict_from_kwargs = dict(name='Bob', age=25, city='Taipei')

# 從其他結構建立
keys = ['name', 'age', 'city']
values = ['Charlie', 30, 'Kaohsiung']
person = dict(zip(keys, values))
```

### 3.3 Dictionary 操作

#### 存取與修改
```python
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# 存取值
print(student['name'])  # 'Alice'
print(student.get('age'))  # 20
print(student.get('phone', 'N/A'))  # 'N/A' (預設值)

# 修改值
student['age'] = 21
student['phone'] = '0912345678'  # 新增鍵值對

# 刪除鍵值對
del student['grade']
phone = student.pop('phone')  # 刪除並返回值
```

#### 字典方法
```python
data = {'a': 1, 'b': 2, 'c': 3}

# keys(), values(), items()
print(list(data.keys()))    # ['a', 'b', 'c']
print(list(data.values()))  # [1, 2, 3]
print(list(data.items()))   # [('a', 1), ('b', 2), ('c', 3)]

# update() - 更新字典
data.update({'d': 4, 'e': 5})
data.update([('f', 6), ('g', 7)])

# clear() - 清空字典
data.clear()

# copy() - 複製字典
original = {'x': 1, 'y': 2}
copy_dict = original.copy()
```

### 3.4 字典遍歷

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# 遍歷鍵
for name in scores:
    print(f"{name}: {scores[name]}")

# 遍歷鍵值對
for name, score in scores.items():
    print(f"{name}: {score}")

# 遍歷值
for score in scores.values():
    print(f"Score: {score}")
```

### 3.5 巢狀字典

```python
company = {
    'employees': {
        'john': {'position': 'manager', 'salary': 50000},
        'jane': {'position': 'developer', 'salary': 45000}
    },
    'departments': ['IT', 'HR', 'Finance']
}

# 存取巢狀資料
print(company['employees']['john']['salary'])  # 50000
```

---

## 4. Set (集合)

### 4.1 基本概念

Set 是不重複元素的無序集合：

- **唯一性**: 不允許重複元素
- **無序性**: 元素沒有固定順序
- **可變性**: 可以動態增加、刪除元素
- **數學集合操作**: 支援聯集、交集、差集等操作

### 4.2 建立 Set

```python
# 基本語法
empty_set = set()  # 注意：{} 是空字典，不是空集合
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, 'hello', 3.14}

# 從其他結構建立
list_to_set = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}
string_to_set = set('hello')  # {'h', 'e', 'l', 'o'}
```

### 4.3 Set 操作

#### 基本操作
```python
fruits = {'apple', 'banana', 'cherry'}

# 添加元素
fruits.add('orange')
fruits.update(['grape', 'kiwi'])

# 刪除元素
fruits.remove('banana')     # 如果元素不存在會報錯
fruits.discard('mango')     # 如果元素不存在不會報錯
popped = fruits.pop()       # 隨機刪除並返回一個元素

# 檢查元素
print('apple' in fruits)    # True
print(len(fruits))          # 集合大小
```

#### 集合運算
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 聯集 (Union)
union = set1 | set2         # {1, 2, 3, 4, 5, 6, 7, 8}
union = set1.union(set2)    # 同上

# 交集 (Intersection)
intersection = set1 & set2  # {4, 5}
intersection = set1.intersection(set2)  # 同上

# 差集 (Difference)
difference = set1 - set2    # {1, 2, 3}
difference = set1.difference(set2)  # 同上

# 對稱差集 (Symmetric Difference)
sym_diff = set1 ^ set2      # {1, 2, 3, 6, 7, 8}
sym_diff = set1.symmetric_difference(set2)  # 同上
```

### 4.4 Set 的實際應用

```python
# 去除重複元素
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]

# 快速查找
large_dataset = set(range(1000000))
print(999999 in large_dataset)  # 非常快速的查找

# 找出兩個列表的共同元素
list1 = ['apple', 'banana', 'cherry']
list2 = ['banana', 'cherry', 'date']
common = list(set(list1) & set(list2))  # ['banana', 'cherry']
```

---

## 5. 實際應用範例

### 5.1 學生成績管理系統

```python
# 使用多種資料結構的綜合範例
class StudentManager:
    def __init__(self):
        # 使用字典儲存學生資料
        self.students = {}
        # 使用集合儲存所有科目
        self.subjects = set()
    
    def add_student(self, student_id, name):
        """新增學生"""
        self.students[student_id] = {
            'name': name,
            'scores': {}  # 字典儲存各科成績
        }
    
    def add_score(self, student_id, subject, score):
        """新增成績"""
        if student_id in self.students:
            self.students[student_id]['scores'][subject] = score
            self.subjects.add(subject)
    
    def get_student_average(self, student_id):
        """計算學生平均分數"""
        if student_id in self.students:
            scores = list(self.students[student_id]['scores'].values())
            return sum(scores) / len(scores) if scores else 0
        return None
    
    def get_subject_statistics(self, subject):
        """計算科目統計"""
        scores = []
        for student in self.students.values():
            if subject in student['scores']:
                scores.append(student['scores'][subject])
        
        if scores:
            return {
                'average': sum(scores) / len(scores),
                'max': max(scores),
                'min': min(scores),
                'count': len(scores)
            }
        return None

# 使用範例
manager = StudentManager()
manager.add_student('S001', 'Alice')
manager.add_student('S002', 'Bob')

manager.add_score('S001', '數學', 85)
manager.add_score('S001', '英文', 92)
manager.add_score('S002', '數學', 78)
manager.add_score('S002', '英文', 88)

print(f"Alice 平均分數: {manager.get_student_average('S001'):.1f}")
print(f"數學科統計: {manager.get_subject_statistics('數學')}")
```

### 5.2 資料處理範例

```python
# 處理銷售資料
sales_data = [
    ('2024-01-01', 'Product A', 100, 1500),
    ('2024-01-01', 'Product B', 50, 2000),
    ('2024-01-02', 'Product A', 80, 1500),
    ('2024-01-02', 'Product C', 30, 3000),
]

# 使用字典統計每日銷售額
daily_sales = {}
for date, product, quantity, price in sales_data:
    if date not in daily_sales:
        daily_sales[date] = 0
    daily_sales[date] += quantity * price

# 使用集合找出所有產品
all_products = set(item[1] for item in sales_data)

# 使用列表排序找出最佳銷售日
sorted_days = sorted(daily_sales.items(), key=lambda x: x[1], reverse=True)

print("每日銷售額:")
for date, amount in daily_sales.items():
    print(f"{date}: ${amount:,}")

print(f"\n所有產品: {', '.join(all_products)}")
print(f"最佳銷售日: {sorted_days[0][0]} (${sorted_days[0][1]:,})")
```

---

## 6. 效能比較與選擇指南

### 6.1 時間複雜度比較

| 操作 | List | Tuple | Dictionary | Set |
|------|------|-------|------------|-----|
| 存取元素 | O(1) | O(1) | O(1) | - |
| 搜尋元素 | O(n) | O(n) | O(1) | O(1) |
| 插入元素 | O(n) | - | O(1) | O(1) |
| 刪除元素 | O(n) | - | O(1) | O(1) |

### 6.2 選擇指南

**使用 List 當：**
- 需要有序的資料
- 需要通過索引存取元素
- 需要允許重複元素
- 需要頻繁修改資料

**使用 Tuple 當：**
- 資料不需要修改
- 需要作為字典的鍵
- 需要更好的效能
- 表示固定的資料結構（如座標點）

**使用 Dictionary 當：**
- 需要鍵值對應關係
- 需要快速查找
- 需要描述性的資料存取

**使用 Set 當：**
- 需要唯一元素
- 需要快速查找
- 需要集合運算（聯集、交集等）
- 需要去除重複元素

---

## 7. 常見錯誤與最佳實踐

### 7.1 常見錯誤

```python
# 錯誤：修改正在遍歷的列表
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    if num % 2 == 0:
        numbers.remove(num)  # 危險！

# 正確：使用列表推導式或建立新列表
numbers = [num for num in numbers if num % 2 != 0]

# 錯誤：淺複製問題
matrix = [[0] * 3] * 3  # 所有行都指向同一個列表
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# 正確：
matrix = [[0] * 3 for _ in range(3)]
```

### 7.2 最佳實踐

```python
# 使用列表推導式
squares = [x**2 for x in range(10)]

# 使用 enumerate() 獲取索引和值
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")

# 使用 zip() 同時遍歷多個序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 使用 get() 方法安全存取字典
config = {'debug': True}
log_level = config.get('log_level', 'INFO')  # 提供預設值
```

---

## 8. 練習題目

### 基礎練習
1. 建立一個包含 1-10 的列表，找出所有偶數
2. 建立一個字典儲存三個學生的成績，計算平均分數
3. 使用集合找出兩個列表的共同元素和差異元素

### 進階練習
1. 實作一個簡單的圖書管理系統
2. 分析文本中的詞頻統計
3. 建立一個購物車系統，支援商品增減和總價計算

### 挑戰題目
1. 實作 LRU (Least Recently Used) 快取
2. 建立一個簡單的資料庫查詢系統
3. 實作圖的鄰接表表示法

---

## 總結

Python 的內建資料結構各有其特點和適用場景：

- **List**: 最通用的資料結構，適合大多數情況
- **Tuple**: 不可變的有序結構，適合固定資料
- **Dictionary**: 鍵值對映射，適合快速查找
- **Set**: 唯一元素集合，適合去重和集合運算

掌握這些資料結構的特性和使用方法，是成為優秀 Python 程式設計師的基礎。在實際開發中，經常需要組合使用多種資料結構來解決複雜問題。

記住：選擇合適的資料結構不僅能讓程式碼更清晰，還能顯著提升程式的效能。