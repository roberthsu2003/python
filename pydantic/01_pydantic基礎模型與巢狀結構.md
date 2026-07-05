## Pydantic V2

### Basic Model


```python
#檢查版本
import pydantic
pydantic.__version__
```




    '2.6.3'




```python
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

```


```python
p = Person(first_name="John", last_name="Smith", age=42)
p
```




    Person(first_name='John', last_name='Smith', age=42)




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

    first_name='John' last_name='Smith' age=42
    1 validation error for Person
    age
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='junk', input_type=str]
        For further information visit https://errors.pydantic.dev/2.6/v/int_parsing



```python
#可以使用.取出field
p = Person(first_name="John", last_name="Smith", age=42)
print(p.first_name)

```

    John



```python
#可以修改field內容
p.first_name = "James"
print(p)
```

    first_name='James' last_name='Smith' age=42



```python
#小心,這樣是不會驗証型別
p.age = "junk"
print(p)
```

    first_name='James' last_name='Smith' age='junk'


## Deserializing Data


```python
# dict to pydantic

data = {
    "first_name": "John",
    "last_name": "Smith",
    "age":42,
}

p = Person.model_validate(data)
p
```




    Person(first_name='John', last_name='Smith', age=42)




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
p
```




    Person(first_name='John', last_name='Smith', age=42)



## Required vs Optional Fields


```python
#預設都為Required Fields(所有欄位必需有值)
try:
    Person(age=42)
except ValidationError as e:
    print(e)

```

    2 validation errors for Person
    first_name
      Field required [type=missing, input_value={'age': 42}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.6/v/missing
    last_name
      Field required [type=missing, input_value={'age': 42}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.6/v/missing



```python
#Require Filed
data = {"age":42}

try:
    Person.model_validate(data)
except ValidationError as e:
    print(e)
```

    2 validation errors for Person
    first_name
      Field required [type=missing, input_value={'age': 42}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.6/v/missing
    last_name
      Field required [type=missing, input_value={'age': 42}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.6/v/missing



```python
#利用default value,成為optional Field,輸入資料時可有可無
#驗證欄位是否為required
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int = 0

Person.model_fields #age有default value 0,所有required=False
```




    {'first_name': FieldInfo(annotation=str, required=True),
     'last_name': FieldInfo(annotation=str, required=True),
     'age': FieldInfo(annotation=int, required=False, default=0)}




```python
#Required=true代表初始化時,Field欄位一定要有資料
#Required=false代表初始化時,Field欄位資料可有可無
p = Person(first_name="John", last_name="Smith")
print(p)
p = Person(first_name="john", last_name="Smith", age=10)
print(p)
```

    first_name='John' last_name='Smith' age=0
    first_name='john' last_name='Smith' age=10


## Nullable Fields(可以存None的欄位)




```python
#0是整數,str是類型,None也是一個類型
#str | None,代表可以接受2種類型
class Person(BaseModel):
    first_name: str | None = None
    last_name: str
    age: int = 0

Person.model_fields
```




    {'first_name': FieldInfo(annotation=Union[str, NoneType], required=False),
     'last_name': FieldInfo(annotation=str, required=True),
     'age': FieldInfo(annotation=int, required=False, default=0)}




```python
p = Person(last_name="Simth")
p
```




    Person(first_name=None, last_name='Simth', age=0)




```python
class Person(BaseModel):
    first_name: str | None = None
    last_name: str
    age: int = 0
    lucky_numbers:list[int] = []

Person.model_fields
```




    {'first_name': FieldInfo(annotation=Union[str, NoneType], required=False),
     'last_name': FieldInfo(annotation=str, required=True),
     'age': FieldInfo(annotation=int, required=False, default=0),
     'lucky_numbers': FieldInfo(annotation=list[int], required=False, default=[])}




```python
p = Person(last_name="smith",lucky_numbers=[1, "2", 3.0]) #[1, "2", 3.0]自動轉成整數
p
```




    Person(first_name=None, last_name='smith', age=0, lucky_numbers=[1, 2, 3])




```python
for number in p.lucky_numbers:
    print(type(number))
```

    <class 'int'>
    <class 'int'>
    <class 'int'>


## Aliases and the Field Class(要求傳入資料的欄位名稱)


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
p
```




    Person(id_=100, first_name='John', last_name='Smith', age=42)




```python
# Serializing
#pydantic to dict

p.model_dump()
```




    {'id_': 100, 'first_name': 'John', 'last_name': 'Smith', 'age': 42}




```python
# Serializing
#pydantic to json
p.model_dump_json()
```




    '{"id_":100,"first_name":"John","last_name":"Smith","age":42}'




```python
# Serializing
#pydantic to python with alias
p.model_dump(by_alias=True)
```




    {'id': 100, 'First Name': 'John', 'LASTNAME': 'Smith', 'age in years': 42}




```python
# Serializing
#pydantic to python with alias
p.model_dump_json(by_alias=True)
```




    '{"id":100,"First Name":"John","LASTNAME":"Smith","age in years":42}'




```python
class Person(BaseModel):
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")

data = {
    "lastName": "Smith"
}

p = Person.model_validate(data)
p
```




    Person(first_name=None, last_name='Smith')




```python
#小心建立時要用alias Name
try:
    Person(last_name="Smith")
except ValidationError as e:
    print(e)

```

    1 validation error for Person
    lastName
      Field required [type=missing, input_value={'last_name': 'Smith'}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.6/v/missing


## 利用Model Config:Populate By Name
## 建立時,可以同時使用FieldName 也可以使用 aliasName



```python
from pydantic import ConfigDict

class Person(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")

p = Person(first_name="John", lastName="Smith")
p
```




    Person(first_name='John', last_name='Smith')




```python
data = {
    "first_name": "John",
    "lastName": "Smith"
}
p = Person.model_validate(data)
p
```




    Person(first_name='John', last_name='Smith')




```python
# defautl value 可以使用method()
from datetime import datetime, timezone
class Log(BaseModel):
    dt: datetime = datetime.now(timezone.utc)
    message:str

log1 = Log(message="message 1")
log1
```




    Log(dt=datetime.datetime(2024, 2, 28, 5, 15, 27, 35122, tzinfo=datetime.timezone.utc), message='message 1')



## # Nested Models(巢狀Models)


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
p
```




    Person(first_name='Arthur', last_name='Clarke', born=Born(place=Place(country='Lunar Colony', city='Central City'), dt=datetime.date(2001, 1, 1)))




```python
p.born.place.city
```




    'Central City'




```python
p.model_dump()
```




    {'first_name': 'Arthur',
     'last_name': 'Clarke',
     'born': {'place': {'country': 'Lunar Colony', 'city': 'Central City'},
      'dt': datetime.date(2001, 1, 1)}}




```python
p.model_dump_json()
```




    '{"first_name":"Arthur","last_name":"Clarke","born":{"place":{"country":"Lunar Colony","city":"Central City"},"dt":"2001-01-01"}}'




```python
from pprint import pprint
pprint(p.model_dump())
```

    {'born': {'dt': datetime.date(2001, 1, 1),
              'place': {'city': 'Central City', 'country': 'Lunar Colony'}},
     'first_name': 'Arthur',
     'last_name': 'Clarke'}



```python
print(p.model_dump_json(indent=2))
```

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


## RootModel(適用於json,python資料結構的root是List)



```python
from typing import List

from pydantic import RootModel


class Pets(RootModel):
    root: List[str]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
    
pets = Pets.model_validate(['dog', 'cat'])
print(pets[0])
print([pet for pet in pets])
```

    dog
    ['dog', 'cat']


## 有關於__iter__(self)和__getitem__(self.item) 說明範例


```python
#實作for_in迴圈,__iter__(self),必需傳出interator物件,使用iter()會傳出iter的物件
def __iter__(self):
        return iter(self.root)

#實作subscript[]
def __getitem__(self, item):
        return self.root[item]
```
