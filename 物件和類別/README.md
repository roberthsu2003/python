# 物件和類別 (Objects and Classes)

## 📚 學習目標

- 理解物件導向程式設計的基本概念
- 學會建立和使用類別 (Class)
- 掌握繼承 (Inheritance) 和多型 (Polymorphism)
- 了解封裝 (Encapsulation) 的概念
- 學會使用特殊方法 (Magic Methods)

## 🎯 類別規劃說明表 (AI自動產生Class指南)

### 基礎類別設計模板

```yaml
# 類別規劃說明表 - 由淺至深
class_design:
  # 第一層：基礎類別
  basic_class:
    name: "基礎類別名稱"
    description: "類別的主要功能描述"
    attributes:
      - name: "屬性名稱"
        type: "資料型別"
        description: "屬性說明"
        access: "public/private/protected"
    methods:
      - name: "方法名稱"
        parameters: ["參數1", "參數2"]
        return_type: "回傳型別"
        description: "方法功能說明"
        access: "public/private/protected"
    
  # 第二層：繼承類別
  inherited_class:
    parent: "父類別名稱"
    name: "子類別名稱"
    description: "子類別的特殊功能"
    additional_attributes:
      - name: "新增屬性"
        type: "資料型別"
        description: "屬性說明"
    additional_methods:
      - name: "新增方法"
        parameters: ["參數1"]
        return_type: "回傳型別"
        description: "方法功能說明"
    overridden_methods:
      - name: "覆寫的方法"
        description: "新的實作方式"
    
  # 第三層：進階功能
  advanced_features:
    magic_methods:
      - name: "__init__"
        description: "初始化方法"
      - name: "__str__"
        description: "字串表示"
      - name: "__eq__"
        description: "相等比較"
    properties:
      - name: "屬性名稱"
        getter: "getter方法"
        setter: "setter方法"
        description: "屬性功能"
    class_methods:
      - name: "類別方法"
        description: "類別層級功能"
    static_methods:
      - name: "靜態方法"
        description: "獨立功能"
```



## 🏗️ 使用 class 定義類別

### 基本概念

- **變數**：稱為屬性 (Instance Attribute)
- **函式**：稱為方法 (Instance Method)

### 建立一個最簡單的類別

```python
class Person():
    pass

# 建立實體
someone = Person()
```

### 建立一個有自訂初始化功能的類別

```python
class Person():
    def __init__(self): 
        pass
```

**說明**：`self` 參數代表呼叫這個實體的參考

### 建立一個有屬性的類別

```python
class Person():
    def __init__(self, name):
        self.name = name

# 建立實體並設定屬性
hunter = Person('Elmer Fudd')
print('The mighty hunter:', hunter.name)
# 輸出：The mighty hunter: Elmer Fudd
```

### 深入理解：`hunter = Person('Elmer Fudd')`

這行程式同時代表 **6 個步驟**：

1. **尋找 Person 類別**
2. **在記憶體內建立實體**
3. **呼叫 Person 類別內的 `__init__(self, name)`，將引數字串 'Elmer Fudd' 傳遞給參數 name**
4. **儲存 'Elmer Fudd' 至實體的 name 屬性內**
5. **傳出這個實體的參考**
6. **將參考儲存至 hunter 變數**

### ⚠️ 重要注意事項

- `__init__` 方法不是一定要實作的
- 在類別定義內存取屬性必須使用 `self.name`
- 建立實體後存取屬性必須使用參考名稱 `.name`（如 `hunter.name`）

## 🔄 繼承 (Inheritance)

### 基本概念

- 透過建立全新的類別，以便擴充現有的類別功能
- 有繼承關係時，區分為父類別和子類別

### 簡單繼承範例

```python
class Car():
    pass

class Yugo(Car):
    pass

# 建立實體
give_me_a_car = Car() 
give_me_a_yugo = Yugo()
```

### 方法繼承

當父類別有方法時，子類別也會繼承這個方法：

```python
class Car():
    def exclaim(self):
        print("I'm a Car!")
        
class Yugo(Car):
    pass

# 建立實體
give_me_a_car = Car() 
give_me_a_yugo = Yugo() 

# 呼叫方法
give_me_a_car.exclaim()  # 輸出：I'm a Car!
give_me_a_yugo.exclaim() # 輸出：I'm a Car!
```

**說明**：呼叫方法 `exclaim()` 時，程式自動會將實體的參考傳給參數 `self`

## 🔧 覆寫方法 (Method Overriding)

### 概念

子類別透過覆寫更改父類別方法的功能

```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

# 建立實體
give_me_a_car = Car() 
give_me_a_yugo = Yugo()

# 呼叫方法
give_me_a_car.exclaim()  # 輸出：I'm a Car!
give_me_a_yugo.exclaim() # 輸出：I'm a Yugo! Much like a Car, but more Yugo-ish.
```

### 覆寫 `__init__` 方法

```python
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

# 建立實體
person = Person('Fudd') 
doctor = MDPerson('Robert') 
lawyer = JDPerson('Alice') 

# 查看結果
print(person.name)   # 輸出：Fudd
print(doctor.name)   # 輸出：Doctor Robert
print(lawyer.name)   # 輸出：Alice, Esquire
```

### 使用 `**kwargs` 呼叫父類別

[詳細範例](./sample1.ipynb)

## ➕ 子類別增加新方法

```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    
    def need_a_push(self):
        print("A little help here?")

# 建立實體
give_me_a_car = Car()
give_me_a_yugo = Yugo()

# 呼叫子類別特有的方法
give_me_a_yugo.need_a_push()  # 輸出：A little help here?

# 父類別無法呼叫子類別的方法
# give_me_a_car.need_a_push()  # 會產生 AttributeError
```

## 🔗 使用 `super()` 呼叫父類別

### 方法一：使用 `super()`

```python
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email): 
        super().__init__(name)  # 呼叫父類別的 __init__
        self.email = email

# 建立實體
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)   # 輸出：Bob Frapples
print(bob.email)  # 輸出：bob@frapples.com
```

### 方法二：直接呼叫父類別

```python
class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

## 🎯 理解 `self`

```python
car = Car() 
car.exclaim()  # 輸出：I'm a Car!

# 也可以使用這種語法，但不建議使用
# 類別名稱.實體方法(實體參考)
Car.exclaim(car)  # 輸出：I'm a Car!
```

## 🛡️ 實體 Property 屬性

### 概念

- 實作屬性 (Attribute) 的 Getter 和 Setter 方法成為一個新屬性 (Property)
- 目的是讓實體不可以直接存取屬性

### 方法一：使用 `property()` 函數

```python
class Duck():
    def __init__(self, input_name): 
        self.hidden_name = input_name

    def get_name(self): 
        print('inside the getter') 
        return self.hidden_name
        
    def set_name(self, input_name): 
        print('inside the setter') 
        self.hidden_name = input_name

    name = property(get_name, set_name)

# 使用範例
fowl = Duck('Howard') 
print(fowl.name)        # 輸出：inside the getter Howard
fowl.name = 'Daffy'     # 輸出：inside the setter
print(fowl.name)        # 輸出：inside the getter Daffy
```

### 方法二：使用裝飾器 (Decorators)

```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    
    @property
    def name(self):
        print('inside the getter') 
        return self.hidden_name
    
    @name.setter
    def name(self, input_name): 
        print('inside the setter') 
        self.hidden_name = input_name

# 使用範例
fowl = Duck('Howard') 
print(fowl.name)        # 輸出：inside the getter Howard
fowl.name = 'Donald'    # 輸出：inside the setter
print(fowl.name)        # 輸出：inside the getter Donald
```

> **注意**：上方的範例，實際上還是可以直接存取 `hidden_name` (attribute)

### 僅建立 Getter Property

```python
class Circle():
    def __init__(self, radius): 
        self.radius = radius

    @property
    def diameter(self): 
        return 2 * self.radius

# 使用範例
c = Circle(5) 
print(c.radius)     # 輸出：5
print(c.diameter)   # 輸出：10

c.radius = 7 
print(c.diameter)   # 輸出：14

# c.diameter = 20   # 會產生 AttributeError，因為沒有 setter
```

## 🔒 建立 Private 屬性

### 使用雙底線 `__` 建立私有屬性

```python
class Duck():
    def __init__(self, input_name): 
        self.__name = input_name  # 私有屬性
    
    @property
    def name(self):
        print('inside the getter') 
        return self.__name
    
    @name.setter
    def name(self, input_name): 
        print('inside the setter') 
        self.__name = input_name

# 使用範例
fowl = Duck('Howard') 
print(fowl.name)        # 輸出：inside the getter Howard
fowl.name = 'Donald'    # 輸出：inside the setter
print(fowl.name)        # 輸出：inside the getter Donald

# fowl.__name  # 會產生 AttributeError，無法直接存取私有屬性
```

## 🏢 類別方法和類別屬性

### 概念

- 類別方法是為類別建立獨自的類別功能
- 使用 `@classmethod` 修飾詞建立類別方法
- 使用類別方法和類別屬性時，必須使用 `類別名稱.類別屬性` 或 `類別名稱.類別方法`
- 建立類別方法必須要有一個參數 `cls`，`cls` 代表類別

### 範例

```python
class A():
    count = 0  # 類別屬性
    
    def __init__(self):
        A.count += 1
        
    def exclaim(self):
        print("I'm an A!")
        
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

# 建立多個實體
easy_a = A()
breezy_a = A()
wheezy_a = A()

# 呼叫類別方法
A.kids()  # 輸出：A has 3 little objects.
```

### 靜態類別方法

```python
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# 呼叫靜態方法
CoyoteWeapon.commercial()  # 輸出：This CoyoteWeapon has been brought to you by Acme
```

## 🦆 Duck Typing

### 概念

「如果它走路像鴨子，叫聲像鴨子，那它就是鴨子」- 重點在於行為，而不是型別

### 範例

```python
class Quote():
    def __init__(self, person, words): 
        self.person = person 
        self.words = words
    
    def who(self):
        return self.person
    
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

# 建立實體
hunter = Quote('Elmer Fudd', "I'm hunting wabbits") 
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc") 
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season") 

# 使用相同介面
print(hunter.who(), 'says:', hunter.says())    # Elmer Fudd says: I'm hunting wabbits.
print(hunted1.who(), 'says:', hunted1.says())  # Bugs Bunny says: What's up, doc?
print(hunted2.who(), 'says:', hunted2.says())  # Daffy Duck says: It's rabbit season!

# 完全不同的類別，但有相同的方法
class BabblingBrook():
    def who(self):
        return 'Brook'
    
    def says(self):
        return 'Babble'

brook = BabblingBrook()

# 通用函數，接受任何有 who() 和 says() 方法的物件
def who_says(obj):
    print(obj.who(), 'says', obj.says())

# 都可以使用相同的函數
who_says(hunter)   # Elmer Fudd says I'm hunting wabbits.
who_says(hunted1)  # Bugs Bunny says What's up, doc?
who_says(hunted2)  # Daffy Duck says It's rabbit season!
who_says(brook)    # Brook says Babble
```

## ✨ 特殊方法 (Magic Methods)

### 基本概念

特殊方法讓物件可以像內建型別一樣運作

### 比較方法

```python
class Word():
    def __init__(self, text):
        self.text = text
    
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

# 使用自訂方法
first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))  # True
print(first.equals(third))   # False

# 使用特殊方法讓比較更自然
class Word():
    def __init__(self, text):
        self.text = text
    
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

# 現在可以直接使用 == 比較
first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)  # True
print(first == third)   # False
```

### 常用特殊方法

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
| `__add__(self, other)` | `+` | 加法 |
| `__sub__(self, other)` | `-` | 減法 |
| `__mul__(self, other)` | `*` | 乘法 |
| `__truediv__(self, other)` | `/` | 除法 |
| `__mod__(self, other)` | `%` | 取餘數 |
| `__pow__(self, other)` | `**` | 次方 |

| 其他方法 | 函數 | 說明 |
|---------|------|------|
| `__str__(self)` | `str()` | 字串表示 |
| `__repr__(self)` | `repr()` | 詳細字串表示 |
| `__len__(self)` | `len()` | 長度 |

### 字串表示方法

```python
class Word():
    def __init__(self, text):
        self.text = text
        
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
        
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return 'Word("' + self.text + '")'

# 使用範例
first = Word('ha')
print(first)        # 使用 __str__：ha
print(repr(first))  # 使用 __repr__：Word("ha")
```

## 🧩 組合 (Composition)

### 概念

組合是「有一個」的關係，比繼承更靈活

```python
class Bill():
    def __init__(self, description):
        self.description = description
        
class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail): 
        self.bill = bill
        self.tail = tail 
    
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

# 建立組合物件
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()  # 輸出：This duck has a wide orange bill and a long tail
```

## 📦 Named Tuples

### 概念

Named Tuples 是輕量級的類別，適合簡單的資料結構

```python
from collections import namedtuple 

# 定義 Named Tuple
Duck = namedtuple('Duck', 'bill tail') 

# 建立實體
duck = Duck('wide orange', 'long') 
print(duck)           # Duck(bill='wide orange', tail='long')
print(duck.bill)      # wide orange
print(duck.tail)      # long

# 使用字典建立
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)          # Duck(bill='wide orange', tail='long')

# 使用關鍵字參數
duck3 = Duck(bill='wide orange', tail='long')

# 建立新的實體（不可變）
duck4 = duck3._replace(tail='magnificent', bill='crushing') 
print(duck4)          # Duck(bill='crushing', tail='magnificent')
```

## 📝 練習題

### 基礎練習

1. **建立一個 `Student` 類別**，包含姓名、學號、成績等屬性
2. **實作 `__str__` 方法**，讓學生資訊更容易顯示
3. **建立 `GraduateStudent` 子類別**，繼承 `Student` 並增加論文題目屬性

### 進階練習

1. **建立一個 `BankAccount` 類別**，使用 Property 保護餘額
2. **實作 `__add__` 方法**，讓兩個帳戶可以相加
3. **建立 `SavingsAccount` 和 `CheckingAccount` 子類別**

### 實作範例

```python
# 學生類別範例
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

## 🎯 學習重點總結

1. **封裝**：使用 Property 和私有屬性保護資料
2. **繼承**：重用程式碼，建立類別階層
3. **多型**：相同介面，不同實作
4. **組合**：靈活的物件關係設計
5. **特殊方法**：讓物件行為更自然

## 類別範例說明表

### 第一層：基礎類別設計

#### 1. 簡單資料容器類別
**需求描述**：建立一個學生類別，用來儲存學生的基本資料，包括姓名、學號、年齡。需要能夠建立學生物件、取得學生資訊、修改學生資料。

**AI生成提示**：
```
請建立一個Student類別，包含以下功能：
- 屬性：姓名(name)、學號(student_id)、年齡(age)
- 方法：初始化方法、取得學生資訊的方法、修改年齡的方法
- 要求：使用適當的資料型別，提供清晰的錯誤處理
```

#### 2. 計算功能類別
**需求描述**：建立一個計算機類別，能夠進行基本的數學運算，包括加法、減法、乘法、除法。需要記錄計算歷史，並能顯示最後的計算結果。

**AI生成提示**：
```
請建立一個Calculator類別，包含以下功能：
- 屬性：當前結果(current_result)、計算歷史(history)
- 方法：加法、減法、乘法、除法、清除歷史、取得結果
- 要求：處理除零錯誤，記錄每次計算的運算式和結果
```

### 第二層：繼承與擴展

#### 3. 繼承關係類別
**需求描述**：建立一個動物類別作為父類別，然後建立貓和狗兩個子類別。動物類別有基本屬性如名稱、年齡，以及發出聲音的方法。貓和狗各自有不同的叫聲和特殊行為。

**AI生成提示**：
```
請建立以下類別結構：
1. Animal父類別：包含名稱、年齡屬性，以及make_sound()方法
2. Cat子類別：繼承Animal，實作貓的叫聲"喵"，增加climb_tree()方法
3. Dog子類別：繼承Animal，實作狗的叫聲"汪"，增加fetch_ball()方法
要求：使用super()呼叫父類別方法，實作適當的繼承關係
```

#### 4. 多層次繼承類別
**需求描述**：建立一個交通工具的類別階層。最上層是Vehicle類別，包含基本屬性如品牌、型號、年份。第二層是Car和Motorcycle，各自有特定的屬性。第三層是ElectricCar和GasCar，繼承自Car但有不同特性。

**AI生成提示**：
```
請建立交通工具類別階層：
1. Vehicle類別：品牌、型號、年份、啟動方法
2. Car類別：繼承Vehicle，增加座位數、車門數
3. Motorcycle類別：繼承Vehicle，增加引擎容量
4. ElectricCar類別：繼承Car，增加電池容量、充電方法
5. GasCar類別：繼承Car，增加油箱容量、加油方法
要求：實作適當的初始化方法，使用super()呼叫父類別
```

### 第三層：進階功能與封裝

#### 5. 封裝與Property類別
**需求描述**：建立一個銀行帳戶類別，包含帳號、戶名、餘額。餘額不能為負數，提款時需要檢查餘額是否足夠。使用Property來保護餘額屬性，提供存款、提款、查詢餘額的功能。

**AI生成提示**：
```
請建立一個BankAccount類別，包含以下功能：
- 私有屬性：帳號、戶名、餘額（使用雙底線保護）
- Property：餘額的getter和setter，確保餘額不為負數
- 方法：存款(deposit)、提款(withdraw)、查詢餘額(get_balance)
- 要求：提款時檢查餘額，餘額不足時拋出異常，使用Property保護資料
```

#### 6. 類別方法與靜態方法
**需求描述**：建立一個商品類別，包含商品編號、名稱、價格、庫存。需要能夠統計所有商品的總價值，以及根據價格範圍篩選商品。使用類別方法來管理商品統計，靜態方法來進行價格驗證。

**AI生成提示**：
```
請建立一個Product類別，包含以下功能：
- 實體屬性：商品編號、名稱、價格、庫存
- 類別屬性：商品列表、總商品數
- 類別方法：統計總價值、取得平均價格、根據價格篩選商品
- 靜態方法：驗證價格是否合理、格式化價格顯示
- 要求：使用@classmethod和@staticmethod裝飾器，實作適當的類別層級功能
```

### 第四層：特殊方法與運算子重載

#### 7. 特殊方法與比較類別
**需求描述**：建立一個分數類別，包含分子和分母。需要能夠進行分數的加法、減法、乘法、除法運算，以及比較兩個分數的大小。實作適當的特殊方法讓分數物件能夠像數字一樣運算。

**AI生成提示**：
```
請建立一個Fraction類別，包含以下功能：
- 屬性：分子、分母
- 特殊方法：__init__、__str__、__repr__、__eq__、__lt__、__gt__
- 數學運算：__add__、__sub__、__mul__、__truediv__
- 要求：自動化簡分數，處理分母為零的情況，實作所有比較運算子
```

#### 8. 容器類別設計
**需求描述**：建立一個購物車類別，能夠添加商品、移除商品、計算總價、顯示購物車內容。需要實作類似列表的行為，包括索引存取、長度查詢、迭代功能。

**AI生成提示**：
```
請建立一個ShoppingCart類別，包含以下功能：
- 特殊方法：__init__、__len__、__getitem__、__setitem__、__delitem__、__iter__
- 方法：添加商品、移除商品、清空購物車、計算總價、顯示內容
- 要求：實作索引存取、迭代功能、適當的錯誤處理
```

### 第五層：設計模式與組合

#### 9. 單例模式類別
**需求描述**：建立一個設定管理類別，確保整個應用程式中只有一個設定實體。需要能夠載入設定檔、取得設定值、修改設定值，並提供全域存取點。

**AI生成提示**：
```
請建立一個Settings類別，實作單例模式：
- 確保只有一個實體存在
- 方法：載入設定、取得設定值、設定值、儲存設定
- 屬性：設定字典、設定檔路徑
- 要求：使用__new__方法實作單例，提供執行緒安全的實作
```

#### 10. 觀察者模式類別
**需求描述**：建立一個事件系統，包含事件發送者和多個觀察者。當事件發生時，所有註冊的觀察者都會收到通知。實作添加觀察者、移除觀察者、發送事件的功能。

**AI生成提示**：
```
請建立一個事件系統，包含以下類別：
1. Event類別：事件基本資訊
2. Subject類別：事件發送者，包含觀察者列表
3. Observer類別：觀察者介面，定義update方法
4. ConcreteObserver類別：具體觀察者實作
要求：實作觀察者模式，提供註冊、移除、通知功能
```

### 第六層：實際應用案例

#### 11. 資料庫操作類別
**需求描述**：建立一個資料庫連接管理類別，能夠建立連接、執行查詢、處理結果集、關閉連接。需要實作連接池管理，提供安全的資料庫操作介面。

**AI生成提示**：
```
請建立一個DatabaseManager類別，包含以下功能：
- 連接管理：建立連接、關閉連接、連接池
- 查詢操作：執行SQL查詢、取得結果集、處理錯誤
- 事務管理：開始事務、提交、回滾
- 要求：使用上下文管理器(__enter__、__exit__)，實作連接池，提供安全的資料庫操作
```

#### 12. API客戶端類別
**需求描述**：建立一個HTTP API客戶端類別，能夠發送GET、POST、PUT、DELETE請求，處理JSON資料，管理認證資訊。需要實作重試機制、錯誤處理、請求日誌。

**AI生成提示**：
```
請建立一個APIClient類別，包含以下功能：
- HTTP方法：GET、POST、PUT、DELETE
- 認證管理：API金鑰、Bearer Token
- 錯誤處理：重試機制、異常處理、狀態碼檢查
- 日誌記錄：請求日誌、回應日誌
- 要求：使用requests庫，實作重試裝飾器，提供完整的錯誤處理
```

### 使用指南

#### 如何向AI描述類別需求：

1. **明確功能需求**：清楚描述類別需要做什麼
2. **列出具體方法**：說明需要哪些方法和屬性
3. **指定特殊要求**：如繼承關係、封裝需求、特殊方法
4. **提供使用場景**：說明如何使用這個類別
5. **指定技術要求**：如使用的裝飾器、異常處理等

#### AI生成類別的最佳實踐：

1. **從簡單開始**：先建立基本結構，再逐步增加功能
2. **測試驅動**：為每個方法提供使用範例
3. **錯誤處理**：考慮邊界情況和異常處理
4. **文件說明**：為類別和方法添加清晰的註解
5. **遵循慣例**：使用Python的命名慣例和設計模式

## 📚 延伸學習資源

- [Python 官方文件 - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python 設計模式](https://refactoring.guru/design-patterns/python)

