## Default Factories

- defualt value,如果使用method()產生不同的default value值,是無法完成的,如下範例


```python
from datetime import datetime, timezone
from pydantic import BaseModel,Field
import random

# defualt value,如果使用method()產生不同的default value值,是無法完成的,如下範例

class Scores(BaseModel):
    chinese:int = random.randint(50, 100)

s1 = Scores()
s2 = Scores()
s3 = Scores()

s1, s2, s3
```




    (Scores(chinese=94), Scores(chinese=94), Scores(chinese=94))




```python
#要解決這個問題就必需使用default factories

class Scores(BaseModel):
    chinese:int = Field(default_factory=lambda:random.randint(50,100))

s1 = Scores()
s2 = Scores()
s3 = Scores()

s1, s2, s3
```




    (Scores(chinese=95), Scores(chinese=83), Scores(chinese=99))



## Custome Serializers(自訂欄位的輸出)


```python
class Model(BaseModel):
    number:float

```


```python
m1 = Model(number=1.0)
m1.model_dump()
```




    {'number': 1.0}




```python
#m2的number輸出不是我要的
m2 = Model(number=1/3)
m2.model_dump()
```




    {'number': 0.3333333333333333}




```python
#datetime預設的輸出格式
dt = datetime.now(timezone.utc)
dt.isoformat()
```




    '2024-03-14T05:35:52.712213+00:00'




```python
#想改變輸出格式
class Model(BaseModel):
    dt:datetime

m = Model(dt=datetime.now(timezone.utc))
m
```




    Model(dt=datetime.datetime(2024, 3, 14, 5, 38, 58, 929109, tzinfo=datetime.timezone.utc))




```python
#josn是純文字,沒有datetime資料類型,自動執行isoformat()
m.model_dump_json()
```




    '{"dt":"2024-03-14T05:38:58.929109Z"}'




```python
#改變json輸出的格式,不要使用預設的格式
from pydantic import field_serializer

class Model(BaseModel):
    number:float

    @field_serializer("number")
    def serialize_float(self,value):
        return round(value,2)

m = Model(number=1/3)
m.model_dump()
```




    {'number': 0.33}




```python
m.model_dump_json()
```




    '{"number":0.33}'




```python
#只改變json輸出的格式,不要使用預設的格式,不改變model_dump()
from pydantic import field_serializer

class Model(BaseModel):
    number:float
    dt:datetime = Field(default_factory=lambda:datetime.now(timezone.utc))

    @field_serializer("number")
    def serialize_float(self,value):
        return round(value,2)
    
    @field_serializer("dt",when_used='json-unless-none') #dt不是None,才做下面的動作
    def serialize_datatime_tojson(self,value):
        return value.strftime("%Y/%-m/%-d %I:%M %p")

m = Model(number=1/3)

m.model_dump() #不會改變
```




    {'number': 0.33,
     'dt': datetime.datetime(2024, 3, 14, 5, 59, 58, 557387, tzinfo=datetime.timezone.utc)}




```python
m.model_dump_json() #使用自訂的輸出格式
```




    '{"number":0.33,"dt":"2024/3/14 05:59 AM"}'



## Custome Validators


```python
from pydantic import field_validator,BaseModel

class Model(BaseModel):
    absolute: int = Field(ge=0)#限定只可以是大於等於0,ge,gt,le,lt

Model(absolute=-5) #出錯

```


```python
class Model(BaseModel):
    absolute: int 

    @field_validator("absolute",mode='before')
    @classmethod
    def make_absolute(cls, value):
        print(f'running custom validator:{value=},{type(value)=}')
        return abs(value)

Model(absolute=0)
```

    running custom validator:value=0,type(value)=<class 'int'>





    Model(absolute=0)




```python
Model(absolute=-10)
```

    running custom validator:value=-10,type(value)=<class 'int'>





    Model(absolute=10)




```python
Model(absolute="-10")
```

    running custom validator:value=-10,type(value)=<class 'int'>





    Model(absolute=10)




```python
class Model(BaseModel):
    numbers:list[int] = []

    @field_validator("numbers")
    @classmethod
    def ensure_unique(cls, numbers):
        if len(set(numbers)) != len(numbers):
            raise ValueError("elements must be unique")
        return numbers
```


```python
Model(numbers=[1,2,3])

```




    Model(numbers=[1, 2, 3])




```python
from pydantic import ValidationError
try:
    Model(numbers=["1", 1, "2", 3.0])
except ValidationError as ex:
    print(ex)
```

    1 validation error for Model
    numbers
      Value error, elements must be unique [type=value_error, input_value=['1', 1, '2', 3.0], input_type=list]
        For further information visit https://errors.pydantic.dev/2.6/v/value_error

