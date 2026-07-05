# Pydantic 預設值與自訂驗證及序列化

本單元將帶您學習 Pydantic 的進階控制技術，包括：如何使用 **`default_factory`** 產生動態與獨立的預設值、如何透過 **`@field_serializer`** 自訂欄位序列化輸出格式，以及如何利用 **`@field_validator`** 在資料載入前與載入後進行自訂驗證與清洗。

---

## 1. 動態預設值與 Default Factories

💡 **學習觀念：靜態預設值的陷阱（所有實例共享同一個預設值）**
在定義 BaseModel 欄位時，如果您直接將函式呼叫的結果（如 `random.randint(...)` 或 `datetime.now()`）指定為預設值，該函式**只會在類別被載入時執行一次**。隨後建立的所有實例，都會共享這同一個時間點或數值。

```python
from datetime import datetime, timezone
from pydantic import BaseModel, Field
import random

# 錯誤示範：直接呼叫 method 指定為預設值，導致所有實例共享同一個亂數
class Scores(BaseModel):
    chinese:int = random.randint(50, 100)

s1 = Scores()
s2 = Scores()
s3 = Scores()

print(s1, s2, s3)
```

**輸出結果：**
```text
chinese=94 chinese=94 chinese=94
```

---

💡 **學習觀念：使用 `default_factory` 進行動態預設值初始化**
要解決上述問題，我們必須使用 `Field(default_factory=...)`，傳入一個**可呼叫的對象 (Callable)**（如 `random.randint` 或 `datetime.now` 的 lambda 函式）。這樣一來，每次實例化模型時，Pydantic 都會重新執行該函式，從而為每個實例動態且獨立地產生預設值。

```python
# 正確做法：使用 default_factory
class Scores(BaseModel):
    chinese:int = Field(default_factory=lambda: random.randint(50, 100))

s1 = Scores()
s2 = Scores()
s3 = Scores()

print(s1, s2, s3)
```

**輸出結果：**
```text
chinese=95 chinese=83 chinese=99
```

---

## 2. 自訂序列化 (Custom Serializers)

在許多實務場景中，雖然資料在模型內部是以高精度的 float 或 datetime 保存，但在將模型轉換為 Dict 或 JSON 回傳時，我們希望限制其格式（如：浮點數保留兩位小數、時間輸出特定格式）。

💡 **學習觀念：預設的浮點數與時間輸出**
預設情況下，呼叫 `model_dump()` 或 `model_dump_json()` 時，Pydantic 會以標準格式輸出數值，這有時並不符合前端或 API 的特定要求。

```python
class Model(BaseModel):
    number:float

m1 = Model(number=1.0)
print(m1.model_dump())
```

**輸出結果：**
```text
{'number': 1.0}
```

---

```python
# 1/3 的浮點數預設會輸出非常多的小數位數
m2 = Model(number=1/3)
print(m2.model_dump())
```

**輸出結果：**
```text
{'number': 0.3333333333333333}
```

---

💡 **學習觀念：標準 ISO 8601 時間格式轉換**
當序列化成 JSON 時，由於 JSON 格式不支援 Datetime 類型，Pydantic 會自動呼叫 `dt.isoformat()` 將時間轉換為符合 ISO 8601 標準的字串格式。

```python
# datetime 預設格式
dt = datetime.now(timezone.utc)
print(dt.isoformat())
```

**輸出結果：**
```text
2024-03-14T05:35:52.712213+00:00
```

---

```python
class Model(BaseModel):
    dt:datetime

m = Model(dt=datetime.now(timezone.utc))
print(repr(m))
```

**輸出結果：**
```text
Model(dt=datetime.datetime(2024, 3, 14, 5, 38, 58, 929109, tzinfo=datetime.timezone.utc))
```

---

```python
# model_dump_json 會自動將 datetime 轉成 ISO 字串
print(m.model_dump_json())
```

**輸出結果：**
```text
{"dt":"2024-03-14T05:38:58.929109Z"}
```

---

💡 **學習觀念：使用 `@field_serializer` 自訂序列化格式**
我們可以使用 `@field_serializer("欄位名稱")` 裝飾器，自訂模型在進行序列化（如 `model_dump()`）時，該欄位所要輸出的格式與內容。

```python
from pydantic import field_serializer

class Model(BaseModel):
    number:float

    @field_serializer("number")
    def serialize_float(self, value):
        return round(value, 2) # 自訂只保留兩位小數

m = Model(number=1/3)
print(m.model_dump())
```

**輸出結果：**
```text
{'number': 0.33}
```

---

```python
print(m.model_dump_json())
```

**輸出結果：**
```text
{"number":0.33}
```

---

💡 **學習觀念：指定序列化時機與條件 (`when_used`)**
我們可以透過指定 `when_used` 參數來決定此自訂序列化器在哪個階段才生效。
例如 `when_used='json-unless-none'` 代表**只在輸出為 JSON 字串時才執行此轉換**，而在一般的 `model_dump()`（轉成 dict）時則維持原本的高精度或原生物件類型，這能極大地保護原始資料在內部計算時的精度。

```python
class Model(BaseModel):
    number:float
    dt:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_serializer("number")
    def serialize_float(self, value):
        return round(value, 2)
    
    # 只在輸出成 JSON 且不為 None 時，將 datetime 改用自訂格式格式化
    @field_serializer("dt", when_used='json-unless-none')
    def serialize_datatime_tojson(self, value):
        return value.strftime("%Y/%-m/%-d %I:%M %p")

m = Model(number=1/3)

# 輸出成 Dict：此時 dt 仍維持原生的 datetime 物件型態
print(m.model_dump())
```

**輸出結果：**
```text
{'number': 0.33, 'dt': datetime.datetime(2024, 3, 14, 5, 59, 58, 557387, tzinfo=datetime.timezone.utc)}
```

---

```python
# 輸出成 JSON：此時 dt 會套用我們自訂的字串格式
print(m.model_dump_json())
```

**輸出結果：**
```text
{"number":0.33,"dt":"2024/3/14 05:59 AM"}
```

---

## 3. 自訂驗證器 (Custom Validators)

Pydantic 提供了內建的條件檢查（如 `ge` 大於等於，`le` 小於等於），但對於更複雜的商業邏輯，我們需要定義自己的驗證器。

💡 **學習觀念：Pydantic 內建的基本數值限制**
我們可以使用 `Field(ge=0)` 等屬性快速限制欄位的基本數值範疇。

```python
try:
    class Model(BaseModel):
        absolute: int = Field(ge=0) # ge 代表 greater than or equal to (大於等於)
    Model(absolute=-5)
except ValidationError as e:
    print(e)
```

**輸出結果：**
```text
1 validation error for Model
absolute
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-5, input_type=int]
    For further information visit https://errors.pydantic.dev/2.6/v/greater_than_equal
```

---

💡 **學習觀念：使用 `@field_validator` 自訂資料的前置處理 (mode='before')**
藉由設定 `@field_validator("欄位", mode='before')`，我們可以在 Pydantic 內建的型別檢查之前搶先拿到原始資料，並將其進行自訂轉換或清理（例如將傳入的負數自動轉為絕對值）。
*   `mode='before'`：在 Pydantic 驗證前執行，適合用於清洗或預先轉換髒資料。
*   `mode='after'`（預設）：在 Pydantic 完成基礎型別驗證後執行，此時傳入的值已經被轉為正確的 Python 型別。

```python
class Model(BaseModel):
    absolute: int 

    @field_validator("absolute", mode='before')
    @classmethod
    def make_absolute(cls, value):
        print(f'running custom validator: {value=}, {type(value)=}')
        return abs(int(value))

print(Model(absolute=0))
```

**輸出結果：**
```text
running custom validator: value=0, type(value)=<class 'int'>
absolute=0
```

---

```python
print(Model(absolute=-10))
```

**輸出結果：**
```text
running custom validator: value=-10, type(value)=<class 'int'>
absolute=10
```

---

```python
# 即使傳入的是字串 "-10"，因為使用了 mode='before' 且有進行 int 轉型，依然能成功解析並處理
print(Model(absolute="-10"))
```

**輸出結果：**
```text
running custom validator: value='-10', type(value)=<class 'str'>
absolute=10
```

---

💡 **學習觀念：確保成員唯一性驗證實務**
本範例說明如何使用 `@field_validator` 對複合型別（如 `list`）的內部成員進行進階邏輯檢查（例如：不可有重複元素，否則拋出 `ValueError`）。

```python
class Model(BaseModel):
    numbers: list[int] = []

    @field_validator("numbers")
    @classmethod
    def ensure_unique(cls, numbers):
        # 使用 set 檢查長度是否一致，以確認元素是否唯一
        if len(set(numbers)) != len(numbers):
            raise ValueError("elements must be unique")
        return numbers
```

---

```python
# 沒有重複值，驗證成功
print(Model(numbers=[1,2,3]))
```

**輸出結果：**
```text
Model(numbers=[1, 2, 3])
```

---

```python
# Pydantic 會先將 "1" 自動轉換為 1，從而導致 [1, 1, 2, 3]，違反了 ensure_unique 規則
try:
    Model(numbers=["1", 1, "2", 3.0])
except ValidationError as ex:
    print(ex)
```

**輸出結果：**
```text
1 validation error for Model
numbers
  Value error, elements must be unique [type=value_error, input_value=['1', 1, '2', 3.0], input_type=list]
    For further information visit https://errors.pydantic.dev/2.6/v/value_error
```
