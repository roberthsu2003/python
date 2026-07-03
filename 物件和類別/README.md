# 物件和類別 (Objects and Classes)

## 📚 學習目標

- 理解物件導向程式設計 (Object-Oriented Programming, OOP) 的基本概念
- 學會建立與使用類別 (Class) 與實體 (Instance)
- 掌握繼承 (Inheritance) 與方法覆寫 (Method Overriding)
- 理解組合 (Composition) 與繼承的設計差異（Is-a 與 Has-a）
- 掌握封裝 (Encapsulation) 的概念，並學會使用私有屬性與 Property 保護資料
- 掌握多型 (Polymorphism) 與 Duck Typing (鴨子類型)
- 學會使用特殊方法 (Magic Methods / Dunder Methods) 讓物件更自然地運作
- 了解現代 Python 的資料容器 (Named Tuples 與 Dataclasses)

---

## 🏗️ 使用 class 定義類別

### 基本概念

在物件導向程式設計中，我們會將現實世界的事物抽象化為類別：
- **類別 (Class)**：就像是藍圖或模具，定義了該事物的結構。
- **實體 (Instance / Object)**：根據類別建立出來的具體物件。
- **屬性 (Attribute)**：類別內的變數，用來記錄狀態或資料。
- **方法 (Method)**：類別內的函數，用來定義行為或功能。

### 建立一個最簡單的類別

在 Python 中，使用 `class` 關鍵字來定義類別。推薦使用首字母大寫的駝峰命名法 (CamelCase)：

```python
class Person:
    pass

# 建立實體
someone = Person()
```

### 建立一個有自訂初始化功能的類別

當我們建立實體時，Python 會自動呼叫 `__init__` 方法。這通常用來設定物件的初始狀態：

```python
class Person:
    def __init__(self): 
        print("初始化：一個新的人被建立了！")

# 建立實體（會自動執行 __init__）
someone = Person()
# 輸出：初始化：一個新的人被建立了！
```

### 建立一個有屬性與方法的類別

```python
class Person:
    def __init__(self, name):
        # 實體屬性 (Instance Attribute)
        self.name = name
    
    def introduce(self):
        # 實體方法 (Instance Method)
        print(f"哈囉，我的名字是 {self.name}。")

# 建立實體並設定屬性
hunter = Person('艾默小獵人')
print('姓名屬性值:', hunter.name)
# 輸出：姓名屬性值: 艾默小獵人

# 呼叫實體方法
hunter.introduce()
# 輸出：哈囉，我的名字是 艾默小獵人。
```

### 深入理解：`hunter = Person('艾默小獵人')`

這行看似簡單的宣告，在 Python 後台實際上執行了 **6 個步驟**：

1. **尋找 Person 類別** 定義。
2. 在記憶體中**建立一個新的實體物件**。
3. 呼叫類別內的初始化方法 **`__init__(self, name)`**，並把新建立的實體傳遞給 `self`，將引數字串 `'艾默小獵人'` 傳遞給參數 `name`。
4. 在實體中儲存屬性（執行 `self.name = name`，將 `'艾默小獵人'` 儲存至該實體的 `name` 屬性內）。
5. **傳回這個新實體的參考**（記憶體位址）。
6. 將該參考**指派給變數 `hunter`**。

### 🎯 深入理解 `self` 的本質

在類別內部，我們必須使用 `self` 來代表「呼叫此方法的物件實體本身」。

當我們呼叫實體方法時，Python 會自動將呼叫該方法的實體當作第一個參數隱式傳遞給 `self`：

```python
hunter = Person('艾默小獵人')
hunter.introduce()  # 一般且推薦的寫法

# 實際上在 Python 背後運作的原理是：
# 類別名稱.實體方法(實體參考)
Person.introduce(hunter)  # 效果完全相同
```

#### ⚠️ 重要注意事項
- `__init__` 方法不是強制的，如果不需要初始化屬性，可以不實作。
- 在類別定義內部存取自身的屬性或呼叫內部方法時，必須加上 `self.`。
- 建立實體後，從外部存取屬性或呼叫方法時，使用該實體變數名稱加上點號 `.`（如 `hunter.name`、`hunter.introduce()`）。

---

## 🔄 繼承 (Inheritance)

### 基本概念

- **繼承**能讓我們基於現有的類別建立新類別，以重用並擴充功能，減少重複程式碼。
- **父類別 (Parent Class / Superclass / Base Class)**：被繼承的原始類別。
- **子類別 (Child Class / Subclass / Derived Class)**：繼承父類別後產生的新類別。

### 簡單繼承與方法繼承

當子類別繼承父類別時，會自動獲得父類別定義的所有屬性與方法：

```python
class Car:
    def exclaim(self):
        print("我是一輛車！")
        
class Yugo(Car):
    # 繼承 Car 的所有功能，不需額外定義
    pass

# 建立實體
my_car = Car() 
my_yugo = Yugo() 

# 呼叫方法
my_car.exclaim()  # 輸出：我是一輛車！
my_yugo.exclaim() # 輸出：我是一輛車！
```

---

## 🧩 組合 (Composition)

### 繼承 vs 組合 (Is-a 與 Has-a)

在物件導向設計中，我們常常需要選擇該使用繼承還是組合：
- **繼承 (Inheritance) 是「是一個 (Is-a)」的關係**：例如 Yugo 是一輛車 (`Yugo` is a `Car`)。
- **組合 (Composition) 是「有一個 (Has-a)」的關係**：例如鴨子「有一張」嘴與「有一條」尾巴 (`Duck` has a `Bill` and a `Tail`)。組合是將其他類別的實體作為自己的屬性，設計上比繼承更靈活、耦合度更低。

```python
class Bill:
    def __init__(self, description):
        self.description = description
        
class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail): 
        # 將其他物件組合進來，做為自身的屬性
        self.bill = bill
        self.tail = tail 
    
    def about(self):
        print(f"這隻鴨子有一張 {self.bill.description} 的嘴，和一條 {self.tail.length} 的尾巴。")

# 建立組合物件
duck_bill = Bill('寬寬橘橘')
duck_tail = Tail('長長')
my_duck = Duck(duck_bill, duck_tail)

my_duck.about()  
# 輸出：這隻鴨子有一張 寬寬橘橘 的嘴，和一條 長長 的尾巴。
```

---

## 🔧 覆寫方法 (Method Overriding)

### 概念

當子類別想要修改或完全改寫從父類別繼承來的方法時，可以重新定義該同名方法，這稱為**覆寫**：

```python
class Car:
    def exclaim(self):
        print("我是一輛車！")

class Yugo(Car):
    # 覆寫父類別的方法
    def exclaim(self):
        print("我是一輛 Yugo！雖然很像車子，但更有 Yugo 的獨特風格。")

my_car = Car() 
my_yugo = Yugo()

my_car.exclaim()  # 輸出：我是一輛車！
my_yugo.exclaim() # 輸出：我是一輛 Yugo！雖然很像車子，但更有 Yugo 的獨特風格。
```

### ➕ 子類別增加新方法

子類別不僅能繼承與覆寫，還能增加自己獨特的新方法：

```python
class Car:
    def exclaim(self):
        print("我是一輛車！")

class Yugo(Car):
    def exclaim(self):
        print("我是一輛 Yugo！")
    
    # 子類別獨有的方法
    def need_a_push(self):
        print("需要幫忙推一把嗎？")

my_yugo = Yugo()
my_yugo.need_a_push()  # 輸出：需要幫忙推一把嗎？

my_car = Car()
# my_car.need_a_push()  # 會產生 AttributeError，因為父類別沒有這個方法
```

### 🔗 使用 `super()` 覆寫 `__init__` 方法

在覆寫初始化方法時，我們通常希望能保留父類別原有的初始化邏輯，並加入子類別專屬的屬性。此時可使用 `super()` 來呼叫父類別的方法：

```python
class Person:
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email): 
        # 呼叫父類別的 __init__ 來初始化 name
        super().__init__(name)  
        # 初始化子類別專屬的屬性
        self.email = email

bob = EmailPerson('阿寶', 'bob@example.com')
print(bob.name)   # 輸出：阿寶
print(bob.email)  # 輸出：bob@example.com
```

### 深入實務：使用 `*args` 與 `**kwargs` 搭配 `super()`

如果父類別的參數很多，或者在多重繼承架構下，為了讓子類別能更具彈性地傳遞參數給父類別，我們通常會使用不定長度參數 `*args` 與關鍵字參數 `**kwargs`：

```python
class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def __init__(self, capacity, *args, **kwargs):
        # 將多餘的參數打包轉交給父類別 Appliance 初始化
        super().__init__(*args, **kwargs)
        self.capacity = capacity

# 關鍵字參數 brand 與 power 會被 **kwargs 收集，並傳遞給 Appliance
washer = WashingMachine(capacity='10公斤', brand='Panasonic', power='110V')
print(f"品牌: {washer.brand}, 電壓: {washer.power}, 容量: {washer.capacity}")
# 輸出：品牌: Panasonic, 電壓: 110V, 容量: 10公斤
```

---

## 🛡️ 封裝 (Encapsulation) 與屬性控制

### 概念

封裝的核心思想是限制外部程式直接修改物件內部的核心資料，改由特定的方法（如 Getter 與 Setter）來進行安全的讀取與寫入，以避免非預期的資料錯誤。

### 🔒 使用雙底線 `__` 建立私有屬性

在 Python 中，以雙底線 `__` 開頭的屬性名稱會被啟用「名稱重整 (Name Mangling)」，這讓外部無法直接存取該屬性，達到私有化 (Private) 的效果：

```python
class Duck:
    def __init__(self, name):
        self.__name = name  # 私有屬性

    def get_name(self):
        return self.__name

fowl = Duck('小黃鴨')
# print(fowl.__name)  # 會產生 AttributeError，無法直接存取

# 必須透過方法來取得
print(fowl.get_name())  # 輸出：小黃鴨
```

### 實體 Property 屬性 (Getter / Setter)

使用 Property 能讓我們將 Getter 與 Setter 方法包裝起來，讓外部程式看起來像存取一般屬性一樣直觀，但內部能執行資料驗證與日誌記錄。

#### 方法一：使用 `property()` 函數

```python
class Duck:
    def __init__(self, name):
        self.__name = name

    def get_name(self): 
        print('執行 Getter') 
        return self.__name
        
    def set_name(self, input_name): 
        print('執行 Setter') 
        if not input_name:
            raise ValueError("姓名不能為空！")
        self.__name = input_name

    # 將方法封裝為名為 name 的 property 屬性
    name = property(get_name, set_name)

fowl = Duck('小黃鴨')
print(fowl.name)        # 自動呼叫 get_name，輸出：執行 Getter \n 小黃鴨
fowl.name = '唐老鴨'     # 自動呼叫 set_name，輸出：執行 Setter
print(fowl.name)        # 輸出：唐老鴨
```

#### 方法二：使用裝飾器 (Decorators) - 推薦做法

這是 Python 中最常見且優雅的 Property 實作方式：

```python
class Duck:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        print('裝飾器：執行 Getter') 
        return self.__name
    
    @name.setter
    def name(self, input_name): 
        print('裝飾器：執行 Setter') 
        if not input_name:
            raise ValueError("姓名不能為空！")
        self.__name = input_name

fowl = Duck('小黃鴨')
print(fowl.name)        # 取得屬性
fowl.name = '唐老鴨'     # 修改屬性
```

#### 唯讀 Property (Read-only Property)

如果只定義 `@property` (Getter) 而不定義對應的 `.setter` 方法，該屬性便成為唯讀屬性：

```python
class Circle:
    def __init__(self, radius): 
        self.radius = radius

    @property
    def diameter(self): 
        # 直徑是由半徑動態計算而來，不允許外部直接修改
        return 2 * self.radius

c = Circle(5) 
print(c.radius)     # 輸出：5
print(c.diameter)   # 輸出：10

c.radius = 7 
print(c.diameter)   # 輸出：14

# c.diameter = 20   # 會產生 AttributeError，因為沒有 setter
```

---

## 🏢 類別屬性與方法 (Class Level)

### 概念

- **實體屬性與方法**：與特定物件實體綁定。
- **類別屬性 (Class Attribute)**：由該類別建立的所有實體共用的變數。
- **類別方法 (Class Method)**：屬於類別本身的方法，第一個參數必須是 `cls`（代表類別本身）。使用 `@classmethod` 裝飾器。
- **靜態方法 (Static Method)**：只是剛好寫在類別內部的獨立工具函數，不需要讀寫實體或類別的狀態。使用 `@staticmethod` 裝飾器。

### 類別方法與類別屬性範例

```python
class Animal:
    total_count = 0  # 類別屬性：記錄所有動物實體的總數量
    
    def __init__(self, name):
        self.name = name  # 實體屬性
        Animal.total_count += 1
        
    @classmethod
    def show_total_count(cls):
        # cls 代表類別本身
        print(f"[{cls.__name__}] 目前共建立了 {cls.total_count} 個動物實體。")

# 建立多個實體
dog = Animal('旺財')
cat = Animal('咪咪')
bird = Animal('小鳥')

# 使用類別名稱直接呼叫類別方法
Animal.show_total_count()  # 輸出：[Animal] 目前共建立了 3 個動物實體。
```

### 靜態方法範例

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        # 單純的數學運算，不依賴類別或實體屬性
        return (c * 9/5) + 32

# 不需要建立實體即可直接呼叫
f = TemperatureConverter.celsius_to_fahrenheit(25)
print("華氏溫度:", f)  # 輸出：77.0
```

---

## 🦆 多型 (Polymorphism) 與 Duck Typing

### 概念

多型允許不同的類別實作相同名稱的方法。

Python 對於多型的實作非常靈活，採用了 **Duck Typing (鴨子類型)**：
> **「如果它走路像鴨子，叫聲也像鴨子，那它就可以被當作鴨子。」**

在 Python 中，一個函數或方法只關心傳入物件**是否支援特定方法**，而不在乎該物件的**實際類別繼承結構**。

### Duck Typing 範例

```python
class RealDuck:
    def quack(self):
        return "呱呱呱！"
    def fly(self):
        return "正在振翅飛翔！"

class Goose:
    def quack(self):
        return "啵啵啵！"
    def fly(self):
        return "正在低空滑翔！"

class ToyDuck:
    def quack(self):
        return "嗶嗶嗶！"
    # 玩具鴨不會飛，不實作 fly 方法

# 通用測試函數，只要求傳入的物件擁有 quack 方法
def make_it_quack(duck_like_obj):
    print(f"聲音: {duck_like_obj.quack()}")

real = RealDuck()
goose = Goose()
toy = ToyDuck()

# 三個完全不同繼承關係的物件，皆可成功使用該函數
make_it_quack(real)   # 輸出：聲音: 呱呱呱！
make_it_quack(goose)  # 輸出：聲音: 啵啵啵！
make_it_quack(toy)    # 輸出：聲音: 嗶嗶嗶！
```

---

## ✨ 特殊方法 (Magic Methods / Dunder Methods)

### 基本概念

特殊方法（也稱雙底線方法）是 Python 內建的特定方法。當我們對物件進行 `+`、`==`、`len()` 等操作時，Python 在後台會呼叫對應的特殊方法。

### 比較方法與運算子重載

預設情況下，自訂類別的實體使用 `==` 比較的是記憶體位址。我們可以透過覆寫特殊方法，讓比較更符合我們的邏輯：

```python
class Word:
    def __init__(self, text):
        self.text = text
    
    # 覆寫相等比較運算子 ==
    def __eq__(self, other):
        # 忽略大小寫進行比較
        return self.text.lower() == other.text.lower()

first = Word('Python')
second = Word('python')
third = Word('Java')

print(first == second)  # 輸出：True
print(first == third)   # 輸出：False
```

### 常用特殊方法對照表

| 比較方法 | 運算子 | 說明 |
|---------|--------|------|
| `__eq__(self, other)` | `==` | 相等比較 |
| `__ne__(self, other)` | `!=` | 不相等比較 |
| `__lt__(self, other)` | `<` | 小於比較 |
| `__gt__(self, other)` | `>` | 大於比較 |
| `__le__(self, other)` | `<=` | 小於等於比較 |
| `__ge__(self, other)` | `>=` | 大於等於比較 |

| 數學方法 | 運算子 | 說明 |
|---------|--------|------|
| `__add__(self, other)` | `+` | 加法運算 |
| `__sub__(self, other)` | `-` | 減法運算 |
| `__mul__(self, other)` | `*` | 乘法運算 |
| `__truediv__(self, other)` | `/` | 除法運算 |
| `__mod__(self, other)` | `%` | 取餘數運算 |
| `__pow__(self, other)` | `**` | 次方運算 |

| 其他方法 | 函數 | 說明 |
|---------|------|------|
| `__str__(self)` | `str()` / `print()` | 回傳適合一般使用者閱讀的簡短字串 |
| `__repr__(self)` | `repr()` | 回傳適合開發者偵錯 (Debug) 的詳細描述字串 |
| `__len__(self)` | `len()` | 回傳物件的長度或大小 |

### 字串表示方法 `__str__` 與 `__repr__` 差別範例

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        # 給一般使用者看的易讀字串
        return f"《{self.title}》- 作者: {self.author}"
    
    def __repr__(self):
        # 給開發者偵錯用的詳細字串，通常格式為 "類別名稱(屬性=值)"
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("Python 快速上手", "陳小明")
print(book)         # 自動呼叫 __str__，輸出：《Python 快速上手》- 作者: 陳小明
print(repr(book))   # 呼叫 __repr__，輸出：Book(title='Python 快速上手', author='陳小明')
```

---

## 📦 資料容器類別 (Data Containers)

當類別只用來存放資料，沒有複雜的行為時，Python 提供了幾種更輕量、更快速的實作方式。

### 1. Named Tuples (具名元組)

Named Tuples 適合用於簡單、不可變 (Immutable) 的資料結構：

```python
from collections import namedtuple 

# 定義 Named Tuple 結構
Duck = namedtuple('Duck', 'bill tail') 

# 建立實體
duck = Duck('寬橘嘴', '長尾巴') 
print(duck)           # 輸出：Duck(bill='寬橘嘴', tail='長尾巴')
print(duck.bill)      # 輸出：寬橘嘴
print(duck.tail)      # 輸出：長尾巴

# 使用關鍵字參數或字典建立
parts = {'bill': '細黃嘴', 'tail': '短尾巴'}
duck2 = Duck(**parts)
```

### 2. Dataclasses (資料類別) - 現代 Python 推薦

Python 3.7+ 引入了 `dataclasses` 模組。使用 `@dataclass` 裝飾器，我們不需要手寫 `__init__`、`__repr__` 與 `__eq__`，Python 會自動幫我們生成，且支援可變的欄位與預設值：

```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    vip_level: int
    email: str = "未提供"  # 預設值

# 自動生成 __init__ 方法
member = User('林小華', 3)
print(member)  
# 自動生成 __repr__，輸出：User(username='林小華', vip_level=3, email='未提供')

member2 = User('林小華', 3)
print(member == member2)  
# 自動生成 __eq__ 比較屬性值，輸出：True
```

---

## 📝 練習題

### 基礎練習
1. 建立一個 `Student` 類別，包含姓名 (name)、學號 (student_id) 與分數 (score) 屬性。
2. 實作 `__str__` 方法，回傳：`"學生：姓名 (學號：學號)"`。
3. 建立 `GraduateStudent` 子類別，繼承 `Student` 並增加論文題目屬性 (thesis)。

#### 基礎練習答案：
```python
class Student:
    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
    
    def __str__(self):
        return f"學生：{self.name} (學號：{self.student_id})"
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'D'

class GraduateStudent(Student):
    def __init__(self, name, student_id, score, thesis):
        super().__init__(name, student_id, score)
        self.thesis = thesis
    
    def __str__(self):
        return f"{super().__str__()} (論文：{self.thesis})"
```

### 進階練習
1. 建立一個 `BankAccount` 類別，使用私有屬性與 Property 保護餘額 (balance)，確保餘額不能為負數，提款時需檢查餘額。
2. 實作 `__add__` 方法，使兩個帳戶可以相加，回傳一個新帳戶（餘額為兩者相加，戶名合併）。
3. 建立 `SavingsAccount` 繼承 `BankAccount`，並增加利息計算方法 `apply_interest(rate)`。

#### 進階練習答案：
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            raise ValueError("初始餘額不能為負數！")
        self.__balance = balance  # 私有屬性

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金額必須大於零！")
        self.__balance += amount
        print(f"{self.owner} 存款成功：+{amount} 元，目前餘額：{self.__balance} 元")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("提款金額必須大於零！")
        if amount > self.__balance:
            raise ValueError("提款失敗：餘額不足！")
        self.__balance -= amount
        print(f"{self.owner} 提款成功：-{amount} 元，目前餘額：{self.__balance} 元")

    def __add__(self, other):
        # 支援兩個帳戶相加
        if not isinstance(other, BankAccount):
            return NotImplemented
        new_owner = f"{self.owner} & {other.owner}"
        new_balance = self.balance + other.balance
        return BankAccount(new_owner, new_balance)

    def __str__(self):
        return f"帳戶擁有者: {self.owner}, 餘額: {self.balance} 元"


class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        # rate 為利率百分比，如 0.02 代表 2%
        if rate <= 0:
            raise ValueError("利率必須大於零！")
        interest = self.balance * rate
        self.deposit(interest)
        print(f"已發放利息：+{interest} 元")
```

---

## 🎯 學習重點總結

1. **封裝**：使用 Property 與私有屬性 (`__` 雙底線) 保護敏感資料，控制外部存取。
2. **繼承**：重用程式碼，建立類別之間的階層與父子關係。
3. **組合**：更靈活的物件關係設計，符合 Has-a 的關係。
4. **多型與 Duck Typing**：透過相同介面呼叫不同實作，只專注於物件行為而非型態。
5. **特殊方法**：利用 Dunder Methods 實作運算子重載與內建功能對接。

---

## 類別範例說明表

### 第一層：基礎類別設計

#### 1. 簡單資料容器類別
- **需求描述**：建立一個學生類別，用來儲存學生的基本資料，包括姓名、學號、年齡。需要能夠建立學生物件、取得學生資訊、修改學生資料。
- **AI 生成提示**：
```text
請建立一個 Student 類別，包含以下功能：
- 屬性：姓名 (name)、學號 (student_id)、年齡 (age)
- 方法：初始化方法、取得學生資訊的方法、修改年齡的方法
- 要求：使用適當的資料型態，提供清晰的錯誤處理機制
```

#### 2. 計算功能類別
- **需求描述**：建立一個計算機類別，能夠進行基本的數學運算，包括加法、減法、乘法、除法。需要記錄計算歷史，並能顯示最後的計算結果。
- **AI 生成提示**：
```text
請建立一個 Calculator 類別，包含以下功能：
- 屬性：當前結果 (current_result)、計算歷史 (history)
- 方法：加法、減法、乘法、除法、清除歷史、取得結果
- 要求：處理除零例外錯誤，並記錄每次計算的運算式和結果
```

### 第二層：繼承與擴展

#### 3. 繼承關係類別
- **需求描述**：建立一個動物類別作為父類別，然後建立貓和狗兩個子類別。動物類別有基本屬性如名稱、年齡，以及發出聲音的方法。貓和狗各自有不同的叫聲 and 特殊行為。
- **AI 生成提示**：
```text
請建立以下類別結構：
1. Animal 父類別：包含名稱、年齡屬性，以及 make_sound() 方法
2. Cat 子類別：繼承 Animal，實作貓的叫聲 "喵"，增加 climb_tree() 方法
3. Dog 子類別：繼承 Animal，實作狗的叫聲 "汪"，增加 fetch_ball() 方法
要求：使用 super() 呼叫父類別方法，實作適當的繼承關係
```

#### 4. 多層次繼承類別
- **需求描述**：建立一個交通工具的類別階層。最上層是 Vehicle 類別，包含基本屬性如品牌、型號、年份。第二層是 Car 和 Motorcycle，各自有特定的屬性。第三層是 ElectricCar 和 GasCar，繼承自 Car 但有不同特性。
- **AI 生成提示**：
```text
請建立交通工具類別階層：
1. Vehicle 類別：品牌、型號、年份、啟動方法
2. Car 類別：繼承 Vehicle，增加座位數、車門數
3. Motorcycle 類別：繼承 Vehicle，增加引擎容量
4. ElectricCar 類別：繼承 Car，增加電池容量、充電方法
5. GasCar 類別：繼承 Car，增加油箱容量、加油方法
要求：實作適當的初始化方法，並使用 super() 呼叫父類別
```

### 第三層：進階功能與封裝

#### 5. 封裝與 Property 類別
- **需求描述**：建立一個銀行帳戶類別，包含帳號、戶名、餘額。餘額不能為負數，提款時需要檢查餘額是否足夠。使用 Property 來保護餘額屬性，提供存款、提款、查詢餘額的功能。
- **AI 生成提示**：
```text
請建立一個 BankAccount 類別，包含以下功能：
- 私有屬性：帳號、戶名、餘額（使用雙底線保護）
- Property：餘額的 getter 和 setter，確保餘額不被設為負數
- 方法：存款 (deposit)、提款 (withdraw)
- 要求：提款時檢查餘額，餘額不足時拋出 ValueError 例外，使用 Property 保護資料
```

#### 6. 類別方法與靜態方法
- **需求描述**：建立一個商品類別，包含商品編號、名稱、價格、庫存。需要能夠統計所有商品的總價值，以及根據價格範圍篩選商品。使用類別方法來管理商品統計，靜態方法來進行價格驗證。
- **AI 生成提示**：
```text
請建立一個 Product 類別，包含以下功能：
- 實體屬性：商品編號、名稱、價格、庫存
- 類別屬性：商品列表、總商品數
- 類別方法：統計總價值、取得平均價格、根據價格篩選商品
- 靜態方法：驗證價格是否合理、格式化價格顯示
- 要求：使用 @classmethod 和 @staticmethod 裝飾器，實作適當的類別層級功能
```

### 第四層：特殊方法與運算子重載

#### 7. 特殊方法與比較類別
- **需求描述**：建立一個分數類別，包含分子 and 分母。需要能夠進行分數的加法、減法、乘法、除法運算，以及比較兩個分數的大小。實作適當的特殊方法讓分數物件能夠像數字一樣運算。
- **AI 生成提示**：
```text
請建立一個 Fraction 類別，包含以下功能：
- 屬性：分子、分母
- 特殊方法：__init__、__str__、__repr__、__eq__、__lt__、__gt__
- 數學運算：__add__、__sub__、__mul__、__truediv__
- 要求：自動化簡分數，並處理分母為零的情況，實作所有比較運算子
```

#### 8. 容器類別設計
- **需求描述**：建立一個購物車類別，能夠添加商品、移除商品、計算總價、顯示購物車內容。需要實作類似列表的行為，包括索引存取、長度查詢、迭代功能。
- **AI 生成提示**：
```text
請建立一個 ShoppingCart 類別，包含以下功能：
- 特殊方法：__init__、__len__、__getitem__、__setitem__、__delitem__、__iter__
- 方法：添加商品、移除商品、清空購物車、計算總價、顯示內容
- 要求：實作索引存取與迭代功能，並提供適當的錯誤處理
```

### 第五層：設計模式與組合

#### 9. 單例模式類別
- **需求描述**：建立一個設定管理類別，確保整個應用程式中只有一個設定實體。需要能夠載入設定檔、取得設定值、修改設定值，並提供全域存取點。
- **AI 生成提示**：
```text
請建立一個 Settings 類別，實作單例模式：
- 確保只有一個實體存在
- 方法：載入設定、取得設定值、設定新值、儲存設定
- 屬性：設定字典、設定檔路徑
- 要求：使用 __new__ 方法實作單例模式，並提供執行緒安全的實作
```

#### 10. 觀察者模式類別
- **需求描述**：建立一個事件系統，包含事件發送者 and 多個觀察者。當事件發生時，所有註冊的觀察者都會收到通知。實作添加觀察者、移除觀察者、發送事件的功能。
- **AI 生成提示**：
```text
請建立一個事件系統，包含以下類別：
1. Event 類別：事件基本資訊
2. Subject 類別：事件發送者，包含觀察者列表
3. Observer 類別：觀察者介面，定義 update 方法
4. ConcreteObserver 類別：具體觀察者實作
要求：實作觀察者模式，提供註冊、移除與通知功能
```

### 第六層：實際應用案例

#### 11. 資料庫操作類別
- **需求描述**：建立一個資料庫連接管理類別，能夠建立連接、執行查詢、處理結果集、關閉連接。需要實作連接池管理，提供安全的資料庫操作介面。
- **AI 生成提示**：
```text
請建立一個 DatabaseManager 類別，包含以下功能：
- 連接管理：建立連接、關閉連接、連接池管理
- 查詢操作：執行 SQL 查詢、取得結果集、處理錯誤
- 事務管理：開始事務、提交 (commit)、回滾 (rollback)
- 要求：使用上下文管理器 (__enter__ 與 __exit__)，實作連接池，提供安全的資料庫操作
```

#### 12. API 客戶端類別
- **需求描述**：建立一個 HTTP API 客戶端類別，能夠發送 GET、POST、PUT、DELETE 請求，處理 JSON 資料，管理認證資訊。需要實作重試機制、錯誤處理、請求日誌。
- **AI 生成提示**：
```text
請建立一個 APIClient 類別，包含以下功能：
- HTTP 方法：GET、POST、PUT、DELETE
- 認證管理：API 金鑰、Bearer Token 支援
- 錯誤處理：重試機制、異常例外處理、狀態碼檢查
- 日誌記錄：請求與回應的日誌記錄
- 要求：使用 requests 庫，實作重試裝飾器，提供完整的錯誤處理機制
```

---

### 使用指南

#### 如何向 AI 描述類別需求：

1. **明確功能需求**：清楚描述類別需要做什麼事。
2. **列出具體屬性與方法**：詳細說明需要哪些欄位和行為。
3. **指定特殊技術要求**：如繼承關係、封裝需求、特殊方法或裝飾器。
4. **提供使用場景**：說明如何呼叫並使用這個類別。
5. **指定錯誤處理機制**：如邊界情況處理、自訂例外拋出等。

#### AI 生成類別的最佳實踐：

1. **從簡單結構開始**：先建立類別骨架與初始化方法，再逐步增加功能。
2. **測試驅動**：為每個重要方法提供使用範例，以驗證正確性。
3. **完整錯誤處理**：考慮邊界情況與例外處理，避免程式崩潰。
4. **詳盡文件說明**：為類別和方法添加清晰的 Docstring (文件字串)。
5. **遵循 Python 開發慣例**：使用 PEP 8 命名規範（類別用大駝峰，屬性與方法用底線分隔的 snake_case），並靈活運用設計模式。
