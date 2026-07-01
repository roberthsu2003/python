# Python 內建資料結構完整指南

Python 提供了四種功能強大的內建資料結構，用於組織、管理和操作資料。掌握 these 資料結構的特性與適用場景，是編寫高效且優雅程式碼的關鍵。

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

### 💡 實戰生活主題範例：待辦事項清單 (Todo List)
> **為什麼此場景需要 List？**  
> 待辦事項必須「保留建立的先後順序（有序性）」，且在一天中我們需要「動態新增新任務」或「完成並移除任務（可變性）」。這與 List 的特性完全吻合。
```python
# 初始化待辦清單
todo_list = ["回覆客戶郵件", "準備下午會議簡報", "去銀行辦事"]

# 1. 新增今日臨時指派的任務 (使用 append)
todo_list.append("購買晚餐食材")
print("目前的待辦事項:", todo_list)

# 2. 順利完成第一項任務 (使用 pop(0) 移除並回傳)
completed_task = todo_list.pop(0)
print(f"【完成】: {completed_task}")
print("剩餘的待辦事項:", todo_list)
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

### 💡 實戰生活主題範例：GPS 經緯度座標 (Location Coordinates)
> **為什麼此場景需要 Tuple？**  
> 台北 101 的 GPS 經緯度座標是「固定不可被任意修改」的常數資料。如果使用 List 儲存，可能會因為其他程式的 Bug 意外將緯度寫入錯誤的值（例如 `coords[0] = 99.9`）。使用 Tuple 可以防禦此類修改，提供唯讀的安全保障。
```python
# 台北 101 的經緯度座標 (緯度, 經度)
taipei_101_coords = (25.0339, 121.5645)

# 嘗試修改緯度值
try:
    taipei_101_coords[0] = 35.1234  # ❌ 嘗試修改
except TypeError as e:
    print("【修改失敗】提示:", e)  # 輸出: 'tuple' object does not support item assignment

# 正確且安全地解包讀取
lat, lon = taipei_101_coords
print(f"地標座標安全讀取 -> 緯度: {lat}, 經度: {lon}")
```

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

### 💡 實戰生活主題範例：英文單字翻譯查詢 (Dictionary Lookup)
> **為什麼此場景需要 Dictionary？**  
> 如果使用 List 來存上萬個單字與翻譯對照，每次查詢都需要從頭到尾掃描列表，效率極差 ($O(n)$)。Dictionary 採用雜湊表 (Hash Table) 技術，不論裡面有三萬個單字還是一百萬個單字，都能以 $O(1)$ 的極速時間瞬間查詢定位。
```python
# 建立一個英翻中對照字典
eng_to_zhtw = {
    "apple": "蘋果",
    "banana": "香蕉",
    "cherry": "櫻桃",
    "durian": "榴槤"
}

# 模擬快速輸入查詢
search_key = "banana"
# 使用 get 方法防錯，若查無此字便顯示提示
chinese_translation = eng_to_zhtw.get(search_key, "抱歉，字典中無此單字。")

print(f"單字 '{search_key}' 的中文翻譯是: {chinese_translation}")
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

### 5.3 數學集合運算
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

### 💡 實戰生活主題範例：社群平台共同好友判定 (Mutual Friends)
> **為什麼此場景需要 Set？**  
> 好友名單在邏輯上是不允許重複的人名。透過集合運算，我們可以免除繁複的雙層 `for` 迴圈比對，直接用簡單的 `&` (交集) 運算子在一瞬間抓出兩人的「共同好友」，且運算效能極高。
```python
# 宣告愛麗絲與鮑伯的朋友集合
alice_friends = {"小明", "小華", "小強", "美美"}
bob_friends = {"小強", "美美", "大雄", "胖虎"}

# 1. 交集運算 (&)：尋找兩人的「共同好友」
mutual = alice_friends & bob_friends
print("共同好友:", mutual)  # 輸出: {'小強', '美美'}

# 2. 差集運算 (-)：尋找「愛麗絲有，但鮑伯沒有」的好友
unique_to_alice = alice_friends - bob_friends
print("僅愛麗絲擁有的好友:", unique_to_alice)  # 輸出: {'小明', '小華'}
```

---

## 6. 實務應用：巢狀表格結構 (List of Dicts)

在實際開發中（例如從資料庫讀取資料、或接收 API 回傳的 JSON 格式），我們最常使用 **「List 包裹 Dictionary (List of Dicts)」** 的巢狀結構來表示一個常見的二維資料表格。

* **List** 代表「所有的資料列 (Rows)」。
* **Dictionary** 代表「每一列資料的欄位與值 (Columns & Values)」。

### 💡 實戰範例：學生成績表格化輸出
下面的範例展示如何宣告一個成績表，並透過遍歷與 `f-string` 對齊排版，將其列印成一個乾淨對齊的二維表格結構：

```python
# 1. 宣告 list[dict] 的巢狀表格結構
students = [
    {"name": "愛麗絲", "國文": 85, "數學": 92, "英文": 78},
    {"name": "鮑伯", "國文": 79, "數學": 85, "英文": 88},
    {"name": "卡蘿", "國文": 92, "數學": 88, "英文": 95}
]

# 2. 列印表格表頭 (使用 f-string 對齊)
# 注意：姓名欄靠左對齊，成績與平均值靠右對齊
print(f"{'姓名':<5} {'國文':>4} {'數學':>4} {'英文':>4} {'平均成績':>5}")
print("-" * 40)

# 3. 遍歷每筆學生記錄並格式化輸出
for student in students:
    name = student["name"]
    chinese = student["國文"]
    math = student["數學"]
    english = student["英文"]
    
    # 計算平均分數
    avg = (chinese + math + english) / 3
    
    # 輸出對齊列
    print(f"{name:<6} {chinese:>6d} {math:>6d} {english:>6d} {avg:>8.1f}")
```

##### 🖥️ 終端機預期輸出結果：
```text
姓名    國文 數學 英文  平均成績
----------------------------------------
愛麗絲     85     92     78     85.0
鮑伯       79     85     88     84.0
卡蘿       92     88     95     91.7
```

---

## 7. 資料結構的效能比較與選擇指南

### 7.1 時間複雜度對比

| 操作 | List (列表) | Tuple (元組) | Dictionary (字典) | Set (集合) |
| :--- | :---: | :---: | :---: | :---: |
| **依索引取值** | $O(1)$ | $O(1)$ | - | - |
| **搜尋特定元素** | $O(n)$ | $O(n)$ | $O(1)$ (極快) | $O(1)$ (極快) |
| **插入/新增元素** | $O(n)$ (尾端為 $O(1)$) | - | $O(1)$ | $O(1)$ |
| **刪除特定元素** | $O(n)$ | - | $O(1)$ | $O(1)$ |

### 7.2 實用選擇心法
* **選擇 `List`**：當您需要「保留資料插入順序」、允許重複、且後續需要依索引編號定位存取時。
* **選擇 `Tuple`**：當您的資料一旦產生便「不需要修改」（例如資料庫唯讀紀錄、座標點、系統配置），需要安全防寫時。
* **選擇 `Dictionary`**：當您需要「將鍵對應到值」（如商品名對照價格、學生學號對照資料），且需要極速搜尋時。
* **選擇 `Set`**：當您需要對一整批資料「進行去重（過濾重複）」，或需要比對兩批資料的交集、聯集時。

---

## 8. 常見錯誤與最佳實踐

### 8.1 修改遍歷中的 List (常見錯誤 ❌)
在 `for` 迴圈中直接刪除目前正在迭代的列表元素，會打亂索引機制，導致漏掉部分元素或引發錯誤。
```python
# ❌ 錯誤做法
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 會造成列表索引位移，漏掉檢查！

#  Correct做法：使用列表推導式建立新列表
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

#  Correct做法：使用 copy()
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
    print(f"{name} is {age} years old")
```