# Pydantic 基礎模型與巢狀結構

本單元將帶您認識 **Pydantic V2** 的核心使用方式。Pydantic 是 Python 中最流行的資料驗證與解析工具，它能確保輸入資料符合您定義的型別，並自動進行型態轉換，是建構穩健應用程式（特別是 Web API）的關鍵利器。

---

## 1. 基礎模型建立與驗證

在開始使用之前，我們先確認環境中的 Pydantic 版本。

💡 **學習觀念：確認 Pydantic 版本**
Pydantic 在 V2版本進行了重大的底層重構（以 Rust 重新實作），效能提升了 10~100 倍，且 API 有不少變動。本教學完全採用最新的 **Pydantic V2** 規範。

```python
#檢查版本
import pydantic
print(pydantic.__version__)
```

**輸出結果：**
```text
2.6.3
```

---

💡 **學習觀念：定義 BaseModel (基礎模型)**
在 Pydantic 中，所有的資料結構都繼承自 `BaseModel`。我們利用 Python 3.5+ 引入的**型別提示 (Type Hints)** 來宣告每個欄位預期的資料型別。

```python
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

```

---

💡 **學習觀念：實例化與資料驗證**
當我們建立 `Person` 物件時，Pydantic 會自動檢查傳入的參數是否符合型別定義，並建立一個具備型別安全保障的資料物件。

```python
p = Person(first_name="John", last_name="Smith", age=42)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='John', last_name='Smith', age=42)
```

---

💡 **學習觀念：自動型態轉換 (Type Coercion) 與驗證錯誤 (ValidationError)**
* **型態轉換**：當傳入資料的型態與定義不完全相符，但能夠被合理轉換時（例如字串 `"42"` 轉成整數 `42`），Pydantic 會自動為您完成轉換。
* **驗證錯誤**：當資料完全無法被合理轉換時（例如字串 `"junk"` 轉成整數 `age`），Pydantic 會丟出 `ValidationError`，並提供極為詳細的錯誤原因。

```python
#驗証
from pydantic import ValidationError

p = Person(first_name="John", last_name="Smith", age="42") #age: int,如果可以會自動轉換為"42" to 42
print(p)

try:
   Person(first_name="John", last_name="Smith", age="junk") #age: int,無法轉換,會raise ValidationError
except ValidationError as error: 
   print(error)
```

**輸出結果：**
```text
first_name='John' last_name='Smith' age=42
1 validation error for Person
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='junk', input_type=str]
    For further information visit https://errors.pydantic.dev/2.6/v/int_parsing
```

---

💡 **學習觀念：屬性讀取與修改**
您可以直接使用 `.` 點號來存取 Pydantic 模型的欄位值。

```python
#可以使用.取出field
p = Person(first_name="John", last_name="Smith", age=42)
print(p.first_name)
```

**輸出結果：**
```text
John
```

---

```python
#可以修改field內容
p.first_name = "James"
print(p)
```

**輸出結果：**
```text
first_name='James' last_name='Smith' age=42
```

---

> [!WARNING]
> **💡 學習觀念：屬性修改與型別驗證的盲區**
> 預設情況下，Pydantic **僅在物件初始化時進行型別驗證**。一旦物件建立完成，後續直接修改欄位值（如 `p.age = "junk"`），Pydantic 預設是**不會**重新進行驗證的，這會導致物件內含非法型別。若需要強制在修改時也進行驗證，必須在模型設定中開啟 `validate_assignment = True`。

```python
#小心,這樣是不會驗證型別
p.age = "junk"
print(p)
```

**輸出結果：**
```text
first_name='James' last_name='Smith' age='junk'
```

---

## 2. 反序列化 (Deserializing Data)

當我們從 API 或資料庫讀取資料時，通常會得到 Python 字典（Dict）或 JSON 字串。我們可以使用 Pydantic 內建的方法將這些資料還原為物件。

💡 **學習觀念：將 Dict 轉成 Pydantic 模型 (model_validate)**
使用 `model_validate()` 可以快速將 Python 的 `dict` 資料轉換成我們定義 Pydantic 模型實例，同時自動進行型別檢查與轉換。

```python
# dict to pydantic
data = {
    "first_name": "John",
    "last_name": "Smith",
    "age":42,
}

p = Person.model_validate(data)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='John', last_name='Smith', age=42)
```

---

💡 **學習觀念：將 JSON 字串轉成 Pydantic 模型 (model_validate_json)**
在處理 API 請求時，最常收到的是原始的 JSON 字串。Pydantic V2 提供了 `model_validate_json()`，這個方法是直接在 Rust 底層進行 JSON 解析與驗證，效能遠高於先將 JSON 用 `json.loads()` 轉成 `dict` 再進行 `model_validate()`。

```python
#json to pydantic
data_json = '''
{
    "first_name": "John",
    "last_name": "Smith",
    "age":42
}
'''

p = Person.model_validate_json(data_json)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='John', last_name='Smith', age=42)
```

---

## 3. 必要欄位 (Required) 與選用欄位 (Optional)

在設計資料模型時，我們必須決定哪些欄位是使用者必須提供的，哪些是可以缺省的。

💡 **學習觀念：預設均為必要欄位 (Required Fields)**
在 Pydantic 中，**只要欄位沒有給予預設值，預設全部都是必要欄位**。如果初始化時漏掉了這些欄位，Pydantic 就會拋出 `missing` 類型的 `ValidationError`。

```python
#預設都為Required Fields(所有欄位必需有值)
try:
    Person(age=42)
except ValidationError as e:
    print(e)
```

**輸出結果：**
```text
2 validation errors for Person
first_name
  Field required [type=missing, input_value={'age': 42}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/missing
last_name
  Field required [type=missing, input_value={'age': 42}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/missing
```

---

```python
#Require Filed
data = {"age":42}

try:
    Person.model_validate(data)
except ValidationError as e:
    print(e)
```

**輸出結果：**
```text
2 validation errors for Person
first_name
  Field required [type=missing, input_value={'age': 42}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/missing
last_name
  Field required [type=missing, input_value={'age': 42}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/missing
```

---

💡 **學習觀念：利用預設值定義選用欄位 (Optional Fields)**
若要在初始化時允許欄位缺省，我們只需在定義模型時**為其指定一個預設值**即可。
透過讀取 `Model.model_fields` 可以看到每個欄位的定義後設資料（例如 `required=True` 代表必要，`required=False` 代表非必要）。

```python
#利用default value,成為optional Field,輸入資料時可有可無
#驗證欄位是否為required
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int = 0

print(Person.model_fields) #age有default value 0,所有required=False
```

**輸出結果：**
```text
{'first_name': FieldInfo(annotation=str, required=True), 'last_name': FieldInfo(annotation=str, required=True), 'age': FieldInfo(annotation=int, required=False, default=0)}
```

---

```python
#Required=true代表初始化時,Field欄位一定要有資料
#Required=false代表初始化時,Field欄位資料可有可無
p = Person(first_name="John", last_name="Smith")
print(p)
p = Person(first_name="john", last_name="Smith", age=10)
print(p)
```

**輸出結果：**
```text
first_name='John' last_name='Smith' age=0
first_name='john' last_name='Smith' age=10
```

---

## 4. 可為空的欄位 (Nullable Fields)

💡 **學習觀念：Nullable Fields (可以為 None 的欄位)**
在 Python 中，`0` 是整數、`""` 是字串，但很多時候某些資料不存在時會是 `None`。我們可以使用 `str | None = None`（或是 Python 3.10 前的 `Optional[str] = None`）來宣告允許為 `None` 的選用欄位。

```python
#0是整數,str是類型,None也是一個類型
#str | None,代表可以接受2種類型
class Person(BaseModel):
    first_name: str | None = None
    last_name: str
    age: int = 0

print(Person.model_fields)
```

**輸出結果：**
```text
{'first_name': FieldInfo(annotation=Union[str, NoneType], required=False, default=None), 'last_name': FieldInfo(annotation=str, required=True), 'age': FieldInfo(annotation=int, required=False, default=0)}
```

---

```python
p = Person(last_name="Simth")
print(repr(p))
```

**輸出結果：**
```text
Person(first_name=None, last_name='Simth', age=0)
```

---

💡 **學習觀念：型別自動轉換清單與自訂型別範例**
Pydantic 也支援對更複雜的型別（如 `list`）進行成員的型態自動轉換。例如傳入 `[1, "2", 3.0]` 時，會自動轉換為 `[1, 2, 3]`。

```python
class Person(BaseModel):
    first_name: str | None = None
    last_name: str
    age: int = 0
    lucky_numbers:list[int] = []

print(Person.model_fields)
```

**輸出結果：**
```text
{'first_name': FieldInfo(annotation=Union[str, NoneType], required=False, default=None), 'last_name': FieldInfo(annotation=str, required=True), 'age': FieldInfo(annotation=int, required=False, default=0), 'lucky_numbers': FieldInfo(annotation=list[int], required=False, default=[])}
```

---

```python
p = Person(last_name="smith",lucky_numbers=[1, "2", 3.0]) #[1, "2", 3.0]自動轉成整數
print(repr(p))
```

**輸出結果：**
```text
Person(first_name=None, last_name='smith', age=0, lucky_numbers=[1, 2, 3])
```

---

```python
for number in p.lucky_numbers:
    print(type(number))
```

**輸出結果：**
```text
<class 'int'>
<class 'int'>
<class 'int'>
```

---

## 5. 欄位別名與序列化設定 (Aliases & Serialization)

在實務中，外部 API 傳給我們的 JSON 常有不符合 Python 變數命名規範的表頭（如包含空白或大寫字，例如 `First Name` 或 `LASTNAME`）。

💡 **學習觀念：欄位別名 (Aliases)**
我們可以使用 `Field(alias="別名")` 來使 Pydantic 在讀取外部資料時，能夠正確將這些特殊的欄位名稱對應至 Python 符合 PEP 8 規範的蛇形命名欄位。

```python
from pydantic import Field

data = {
    "id":100,
    "First Name":"John",
    "LASTNAME":"Smith",
    "age in years": 42
}

class Person(BaseModel):
    id_: int = Field(alias="id")
    first_name: str = Field(alias="First Name")
    last_name: str = Field(alias="LASTNAME")
    age: int = Field(alias="age in years")

p = Person.model_validate(data)
print(repr(p))
```

**輸出結果：**
```text
Person(id_=100, first_name='John', last_name='Smith', age=42)
```

> 💡 **為什麼這裡使用 `id_` 而不是 `id`？**
>
> 1. **避免遮蔽 Python 內建函式 (PEP 8 規範)**：
>    在 Python 中，`id` 是一個內建函式（例如呼叫 `id(obj)` 可以取得物件的記憶體位址）。如果我們宣告變數或欄位為 `id`，雖然程式能正常執行，但會「遮蔽（Shadow）」掉這個內建函式，導致後續在同一個範疇中無法直接使用它。
>    根據 PEP 8 風格指南，當變數名稱與 Python 內建關鍵字或函式衝突時，推薦在尾端加上單個底線（如 `id_`、`type_`、`class_`）來區隔。
>
> 2. **消除 Linter 警告 (Linter Warning)**：
>    在開發工具（如 VS Code、PyCharm）中，若使用 `id`，靜態程式碼分析工具（Linter，如 Ruff、Pylint）會發出警示。Linter 警告（Warning）與語法錯誤（Error）不同，它不會讓程式崩潰，但代表該寫法存在潛在風險或不符合社群最佳實踐。
>
> 3. **Pydantic 的橋梁作用**：
>    透過 `id_: int = Field(alias="id")`，Pydantic 在讀取外部資料時會尋找外部欄位 `"id"`，但在 Python 程式中我們可以安全、乾淨地使用 `id_`，完美解決命名衝突問題。

---

💡 **學習觀念：將模型序列化 (Serializing) 為 Dict 與 JSON**
Pydantic 提供了 `model_dump()`（轉成 dict）與 `model_dump_json()`（轉成 JSON 字串）來將模型還原為標準 Python/Web 資料格式。
預設導出會使用 Python 程式內所定義的欄位名稱 (即 `first_name` 等)。

```python
# Serializing
#pydantic to dict
print(p.model_dump())
```

**輸出結果：**
```text
{'id_': 100, 'first_name': 'John', 'last_name': 'Smith', 'age': 42}
```

---

```python
# Serializing
#pydantic to json
print(p.model_dump_json())
```

**輸出結果：**
```text
{"id_":100,"first_name":"John","last_name":"Smith","age":42}
```

---

💡 **學習觀念：以別名輸出 (Serializing with Alias)**
如果我們產生的 JSON 資料需要回傳給其他只吃特定格式（如原本的 `First Name`）的 API，可以加上 `by_alias=True` 參數來讓 Pydantic 以別名輸出資料。

```python
# Serializing
#pydantic to python with alias
print(p.model_dump(by_alias=True))
```

**輸出結果：**
```text
{'id': 100, 'First Name': 'John', 'LASTNAME': 'Smith', 'age in years': 42}
```

---

```python
# Serializing
#pydantic to python with alias
print(p.model_dump_json(by_alias=True))
```

**輸出結果：**
```text
{"id":100,"First Name":"John","LASTNAME":"Smith","age in years":42}
```

---

💡 **學習觀念：建立與載入資料時的別名限制**
一般情況下，如果欄位被定義了 `alias`，那麼當我們直接用變數建構模型時，**必須**使用 alias 名稱，而不能用 Python 中的變數名稱，否則會驗證失敗拋出遺失欄位的錯誤。

```python
class Person(BaseModel):
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")

data = {
    "lastName": "Smith"
}

p = Person.model_validate(data)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name=None, last_name='Smith')
```

---

```python
#小心建立時要用alias Name
try:
    Person(last_name="Smith")
except ValidationError as e:
    print(e)
```

**輸出結果：**
```text
1 validation error for Person
lastName
  Field required [type=missing, input_value={'last_name': 'Smith'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/missing
```

---

## 6. 使用 Model Config 允許同名或別名建立

💡 **學習觀念：利用 ConfigDict 啟用 `populate_by_name`**
如果希望在建立模型時，**不論用 python 欄位原名（`first_name`）或 alias 別名（`firstName`）都能夠被成功解析**，可以在模型內配置 `model_config = ConfigDict(populate_by_name=True)`。

```python
from pydantic import ConfigDict

class Person(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")

p = Person(first_name="John", lastName="Smith")
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='John', last_name='Smith')
```

---

```python
data = {
    "first_name": "John",
    "lastName": "Smith"
}
p = Person.model_validate(data)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='John', last_name='Smith')
```

---

> [!CAUTION]
> **💡 學習觀念：靜態預設值與時間點共享問題（Log 範例）**
> 當我們直接將 `datetime.now()` 賦值為欄位的預設值時，這個時間點只會在**模組載入（或類別定義）的那一刻**被計算一次。此後所有建立的 Log 實例，其預設時間都會是同一個，無法取得當下的時間。要解決此問題，我們必須使用 `default_factory`。

**錯誤示範（時間被固定在定義時）：**
```python
# 錯誤示範：直接呼叫 datetime.now() 指定為預設值
from datetime import datetime, timezone
class Log(BaseModel):
    dt: datetime = datetime.now(timezone.utc)
    message: str

log1 = Log(message="message 1")
print(repr(log1))
```

**輸出結果：**
```text
Log(dt=datetime.datetime(2026, 7, 6, 11, 7, 11, 35122, tzinfo=datetime.timezone.utc), message='message 1')
```

**正確示範（使用 `default_factory`）：**
要解決上述問題，我們必須使用 `Field(default_factory=...)`，傳入一個可呼叫對象（Callable，例如 lambda 函式）。這樣每次建立新的模型實例時，Pydantic 都會重新執行該函式，動態取得當下的時間點。（更詳細的說明與範例，請參考下一個單元：[02. Pydantic 預設值與自訂驗證及序列化](./02_pydantic預設值與自訂驗證及序列化.md)）

```python
from datetime import datetime, timezone
from pydantic import Field

class Log(BaseModel):
    # 使用 default_factory 傳入 lambda，動態且獨立地產生預設值
    dt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    message: str

log1 = Log(message="message 1")
print(repr(log1))
```

**輸出結果：**
```text
Log(dt=datetime.datetime(2026, 7, 6, 11, 8, 45, 123456, tzinfo=datetime.timezone.utc), message='message 1')
```

---

## 7. 巢狀模型 (Nested Models)

💡 **學習觀念：巢狀模型定義**
當我們要解析複雜的資料結構（如 JSON 包含多層 Object）時，可以定義多個繼承 `BaseModel` 的類別，並將一個 Model 作為另一個 Model 的欄位型別，這即是**巢狀模型 (Nested Models)**。

```python
data = {
    "firstName": "Arthur",
    "lastName": "Clarke",
    "born":{
        "place":{
            "country":"Lunar Colony",
            "city": "Central City"
        },
        "date":"2001-01-01"
    }
}
```

---

```python
from datetime import date
class Place(BaseModel):
    country: str
    city: str

class Born(BaseModel):
    place:Place
    dt:date = Field(alias="date")

class Person(BaseModel):
    first_name:str | None = Field(alias="firstName",default=None)
    last_name:str = Field(alias="lastName")
    born:Born

p=Person.model_validate(data)
print(repr(p))
```

**輸出結果：**
```text
Person(first_name='Arthur', last_name='Clarke', born=Born(place=Place(country='Lunar Colony', city='Central City'), dt=datetime.date(2001, 1, 1)))
```

---

```python
print(p.born.place.city)
```

**輸出結果：**
```text
Central City
```

---

```python
print(p.model_dump())
```

**輸出結果：**
```text
{'first_name': 'Arthur', 'last_name': 'Clarke', 'born': {'place': {'country': 'Lunar Colony', 'city': 'Central City'}, 'dt': datetime.date(2001, 1, 1)}}
```

---

```python
print(p.model_dump_json())
```

**輸出結果：**
```text
{"first_name":"Arthur","last_name":"Clarke","born":{"place":{"country":"Lunar Colony","city":"Central City"},"dt":"2001-01-01"}}
```

---

```python
from pprint import pprint
pprint(p.model_dump())
```

**輸出結果：**
```text
{'born': {'dt': datetime.date(2001, 1, 1),
          'place': {'city': 'Central City', 'country': 'Lunar Colony'}},
 'first_name': 'Arthur',
 'last_name': 'Clarke'}
```

---

```python
print(p.model_dump_json(indent=2))
```

**輸出結果：**
```text
{
  "first_name": "Arthur",
  "last_name": "Clarke",
  "born": {
    "place": {
      "country": "Lunar Colony",
      "city": "Central City"
    },
    "dt": "2001-01-01"
  }
}
```

---

## 8. RootModel ── 最外層為清單時的解析

💡 **學習觀念：RootModel 封裝與迭代**
有時 API 回傳的 JSON 最外層是陣列 `[...]` 而不是物件 `{...}`。在 Pydantic V2 中，我們使用 `RootModel` 進行最外層的封裝，並能透過實作魔術方法 `__iter__` 與 `__getitem__` 來讓模型實例直接支援 `for...in` 迴圈與 `[index]` 的索引取值。

```python
from typing import List
from pydantic import RootModel

class Pets(RootModel):
    root: List[str]

    # 實作迭代以支援 for-in 迴圈
    def __iter__(self):
        return iter(self.root)

    # 實作 subscript 支援以允許用 [index] 索引取值
    def __getitem__(self, item):
        return self.root[item]
    
pets = Pets.model_validate(['dog', 'cat'])
print(pets[0])
print([pet for pet in pets])
```

**輸出結果：**
```text
dog
['dog', 'cat']
```
